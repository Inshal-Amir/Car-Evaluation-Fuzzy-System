import os
import json
from experiments.evaluate import run_eval

def run_sensitivity(widths=(0.4,0.5,0.6,0.7,0.8),limit=600):
    rows=[]
    for w in widths:
        r=run_eval(mf_width=float(w),limit=limit)
        rows.append({"mf_width":float(w),"accuracy":r["accuracy"],"baseline_accuracy":r["baseline_accuracy"],"n":r["n"]})
    return rows

def save(rows,report_dir):
    os.makedirs(report_dir,exist_ok=True)
    with open(os.path.join(report_dir,"sensitivity.json"),"w",encoding="utf-8") as f:
        json.dump(rows,f,indent=2)

if __name__=="__main__":
    report_dir=os.path.join(os.path.dirname(__file__),"..","reports")
    rows=run_sensitivity()
    save(rows,report_dir)
    print(rows)
