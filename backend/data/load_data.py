import os
import pandas as pd

COLS=["buying","maint","doors","persons","lug_boot","safety","class"]

def load_car_data(path=None):
    if path is None:
        path=os.path.join(os.path.dirname(__file__),"raw","car.data")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Missing dataset file at: {path}")
    df=pd.read_csv(path,header=None,names=COLS)
    return df

def value_maps():
    return {
        "buying":{"low":0,"med":1,"high":2,"vhigh":3},
        "maint":{"low":0,"med":1,"high":2,"vhigh":3},
        "doors":{"2":0,"3":1,"4":2,"5more":3},
        "persons":{"2":0,"4":1,"more":2},
        "lug_boot":{"small":0,"med":1,"big":2},
        "safety":{"low":0,"med":1,"high":2},
        "class":{"unacc":0,"acc":1,"good":2,"vgood":3},
    }

def encode_df(df):
    m=value_maps()
    out=df.copy()
    for c in ["buying","maint","doors","persons","lug_boot","safety","class"]:
        out[c]=out[c].map(m[c])
        if out[c].isna().any():
            bad=df.loc[out[c].isna(),c].unique().tolist()
            raise ValueError(f"Unknown values in {c}: {bad}")
    return out

def decode_class(idx):
    inv={0:"unacc",1:"acc",2:"good",3:"vgood"}
    return inv[int(idx)]
