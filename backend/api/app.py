import os
import json
import numpy as np
from fastapi import FastAPI
from api.schemas import PredictRequest,PredictResponse
from data.load_data import load_car_data,encode_df,value_maps,decode_class
from fuzzy.fis_mamdani import build_mamdani_system
from fuzzy.inference import predict_one,class_probs_from_output
from fuzzy.rulebase import rule_texts
from experiments.evaluate import run_eval,save_eval
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI(title="Car Evaluation Fuzzy Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAP=value_maps()
RULE_TEXTS=rule_texts()
MAM=build_mamdani_system(mf_width=0.6)

def enc_feature(k,v):
    if k in MAP and v in MAP[k]:
        return MAP[k][v]
    raise ValueError(f"Bad value for {k}: {v}")

@app.get("/health")
def health():
    return {"ok":True}

@app.get("/metrics")
def metrics():
    report_dir=os.path.join(os.path.dirname(__file__),"..","reports")
    metrics_path=os.path.join(report_dir,"metrics.json")
    if not os.path.exists(metrics_path):
        out=run_eval(mf_width=0.6)
        save_eval(out,report_dir)
    with open(metrics_path,"r",encoding="utf-8") as f:
        metrics=json.load(f)
    df=load_car_data()
    stats={
        "instances":int(len(df)),
        "features":6,
        "target_classes":["unacc","acc","good","vgood"],
        "class_counts":df["class"].value_counts().to_dict(),
        "missing_values":int(df.isna().sum().sum()),
    }
    return {"stats":stats,"evaluation":metrics}

@app.get("/membership")
def membership():
    v=MAM["vars"]
    out={}
    for name,obj in [("buying",v["buying"]),("maint",v["maint"]),("doors",v["doors"]),("persons",v["persons"]),("lug_boot",v["lug_boot"]),("safety",v["safety"]),("cls",v["out"])]:
        series=[]
        for term in obj.terms:
            mf=obj[term].mf
            series.append({"term":term,"x":obj.universe.tolist(),"y":mf.tolist()})
        out[name]=series
    return out

@app.post("/predict",response_model=PredictResponse)
def predict(req:PredictRequest):
    x={
        "buying":enc_feature("buying",req.buying),
        "maint":enc_feature("maint",req.maint),
        "doors":enc_feature("doors",req.doors),
        "persons":enc_feature("persons",req.persons),
        "lug_boot":enc_feature("lug_boot",req.lug_boot),
        "safety":enc_feature("safety",req.safety),
    }
    y=predict_one(MAM,x)
    ycls=int(np.clip(round(y),0,3))
    probs=class_probs_from_output(y)
    fired=[]
    top=sorted(probs.items(),key=lambda kv:kv[1],reverse=True)[:2]
    fired.append(f"Top classes: {top[0][0]} ({top[0][1]:.3f}), {top[1][0]} ({top[1][1]:.3f})")
    fired.extend(RULE_TEXTS[:5])
    return {"predicted_class":decode_class(ycls),"crisp_output":float(y),"probs":probs,"fired_rules":fired}
