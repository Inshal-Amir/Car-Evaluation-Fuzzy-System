import os
import json
import numpy as np
from sklearn.metrics import accuracy_score
from data.load_data import load_car_data,encode_df
import skfuzzy.control as ctrl
from fuzzy.variables import build_variables
from fuzzy.rulebase import build_rules
from fuzzy.inference import predict_one

def build_sim_with_rules(rules):
    sys=ctrl.ControlSystem(rules)
    sim=ctrl.ControlSystemSimulation(sys)
    return {"vars":None,"rules":rules,"sim":sim}

def run_ablation(mf_width=0.6,drop_k=3,limit=600):
    df=load_car_data()
    edf=encode_df(df).sample(n=int(limit),random_state=42).reset_index(drop=True)
    v=build_variables(mf_width=mf_width)
    rules=build_rules(v)
    full=build_sim_with_rules(rules)
    keep=rules[:-int(drop_k)] if drop_k>0 else rules
    ab=build_sim_with_rules(keep)
    y_true=edf["class"].to_numpy()
    yp=[]
    ya=[]
    for _,r in edf.iterrows():
        x={"buying":r["buying"],"maint":r["maint"],"doors":r["doors"],"persons":r["persons"],"lug_boot":r["lug_boot"],"safety":r["safety"]}
        yf=int(np.clip(round(predict_one(full,x)),0,3))
        yk=int(np.clip(round(predict_one(ab,x)),0,3))
        yp.append(yf)
        ya.append(yk)
    return {"full_accuracy":float(accuracy_score(y_true,yp)),"ablated_accuracy":float(accuracy_score(y_true,ya)),"drop_k":int(drop_k),"n":int(len(edf))}

def save(out,report_dir):
    os.makedirs(report_dir,exist_ok=True)
    with open(os.path.join(report_dir,"ablation.json"),"w",encoding="utf-8") as f:
        json.dump(out,f,indent=2)

if __name__=="__main__":
    report_dir=os.path.join(os.path.dirname(__file__),"..","reports")
    out=run_ablation()
    save(out,report_dir)
    print(out)
