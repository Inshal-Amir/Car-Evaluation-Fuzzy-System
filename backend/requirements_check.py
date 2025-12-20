import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from data.load_data import load_car_data,encode_df
from fuzzy.fis_mamdani import build_mamdani_system
from experiments.evaluate import run_eval,save_eval
from experiments.sensitivity import run_sensitivity,save as save_sens
from experiments.ablation import run_ablation,save as save_ab

def plot_membership(mam,report_dir):
    v=mam["vars"]
    plots=[("buying",v["buying"]),("maint",v["maint"]),("doors",v["doors"]),("persons",v["persons"]),("lug_boot",v["lug_boot"]),("safety",v["safety"]),("cls",v["out"])]
    for name,obj in plots:
        plt.figure()
        for term in obj.terms:
            plt.plot(obj.universe,obj[term].mf,label=term)
        plt.legend()
        plt.title(f"{name} membership functions")
        plt.xlabel("universe")
        plt.ylabel("membership")
        plt.tight_layout()
        plt.savefig(os.path.join(report_dir,f"membership_{name}.png"))
        plt.close()

def plot_baseline_vs_fuzzy(metrics,report_dir):
    plt.figure()
    plt.bar(["baseline","fuzzy"],[metrics["baseline_accuracy"],metrics["accuracy"]])
    plt.ylim(0,1)
    plt.title("Baseline vs Fuzzy Accuracy")
    plt.tight_layout()
    plt.savefig(os.path.join(report_dir,"baseline_vs_fuzzy.png"))
    plt.close()

def main():
    root=os.path.dirname(__file__)
    report_dir=os.path.join(root,"reports")
    os.makedirs(report_dir,exist_ok=True)

    df=load_car_data()
    edf=encode_df(df)
    assert len(df)==1728

    mam=build_mamdani_system(mf_width=0.6)
    plot_membership(mam,report_dir)

    metrics=run_eval(mf_width=0.6)
    save_eval(metrics,report_dir)
    plot_baseline_vs_fuzzy(metrics,report_dir)

    sens=run_sensitivity(widths=(0.4,0.5,0.6,0.7,0.8),limit=600)
    save_sens(sens,report_dir)

    abl=run_ablation(mf_width=0.6,drop_k=3,limit=600)
    save_ab(abl,report_dir)

    summary={"metrics":metrics,"sensitivity":sens,"ablation":abl}
    with open(os.path.join(report_dir,"summary.json"),"w",encoding="utf-8") as f:
        json.dump(summary,f,indent=2)

    print("DONE. Reports saved to backend/reports")

if __name__=="__main__":
    main()
