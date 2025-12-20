import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from data.load_data import load_car_data,encode_df,decode_class,value_maps
from fuzzy.fis_mamdani import build_mamdani_system
from fuzzy.inference import predict_one
from baseline.crisp_baseline import predict_crisp

def run_eval(mf_width=0.6,limit=None):
    df=load_car_data()
    edf=encode_df(df)
    if limit is not None:
        edf=edf.sample(n=int(limit),random_state=42).reset_index(drop=True)
    mam=build_mamdani_system(mf_width=mf_width)
    y_true=edf["class"].to_numpy()
    y_pred=[]
    y_base=[]
    for _,r in edf.iterrows():
        x={
            "buying":r["buying"],
            "maint":r["maint"],
            "doors":r["doors"],
            "persons":r["persons"],
            "lug_boot":r["lug_boot"],
            "safety":r["safety"],
        }
        y=predict_one(mam,x)
        y_pred.append(int(np.clip(round(y),0,3)))
        y_base.append(int(predict_crisp(x)))
    acc=accuracy_score(y_true,y_pred)
    accb=accuracy_score(y_true,y_base)
    cm=confusion_matrix(y_true,y_pred,labels=[0,1,2,3])
    cmb=confusion_matrix(y_true,y_base,labels=[0,1,2,3])
    rep=classification_report(y_true,y_pred,labels=[0,1,2,3],target_names=["unacc","acc","good","vgood"],zero_division=0,output_dict=True)
    out={
        "accuracy":float(acc),
        "baseline_accuracy":float(accb),
        "report":rep,
        "confusion_matrix":cm.tolist(),
        "baseline_confusion_matrix":cmb.tolist(),
        "mf_width":mf_width,
        "n":int(len(edf)),
    }
    return out

def save_eval(out,report_dir):
    os.makedirs(report_dir,exist_ok=True)
    with open(os.path.join(report_dir,"metrics.json"),"w",encoding="utf-8") as f:
        json.dump(out,f,indent=2)
    cm=pd.DataFrame(out["confusion_matrix"],index=["unacc","acc","good","vgood"],columns=["unacc","acc","good","vgood"])
    cm.to_csv(os.path.join(report_dir,"confusion_matrix.csv"),index=True)
    cmb=pd.DataFrame(out["baseline_confusion_matrix"],index=["unacc","acc","good","vgood"],columns=["unacc","acc","good","vgood"])
    cmb.to_csv(os.path.join(report_dir,"baseline_confusion_matrix.csv"),index=True)
    return out

if __name__=="__main__":
    out=run_eval()
    save_eval(out,os.path.join(os.path.dirname(__file__),"..","reports"))
    print(out["accuracy"],out["baseline_accuracy"])
