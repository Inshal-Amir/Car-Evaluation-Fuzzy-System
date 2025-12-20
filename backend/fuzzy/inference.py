import numpy as np

def predict_one(mamdani,features):
    sim=mamdani["sim"]
    sim.reset()
    for k,val in features.items():
        sim.input[k]=float(val)
    sim.compute()
    y=sim.output.get("cls",None)
    if y is None:
        return 0.0
    return float(y)

def class_probs_from_output(y):
    centers=[0,1,2,3]
    d=[abs(y-c) for c in centers]
    inv=[1/(x+1e-6) for x in d]
    s=sum(inv)
    p=[v/s for v in inv]
    return {"unacc":p[0],"acc":p[1],"good":p[2],"vgood":p[3]}
