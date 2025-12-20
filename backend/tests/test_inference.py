from fuzzy.fis_mamdani import build_mamdani_system
from fuzzy.inference import predict_one

def test_predict_runs():
    mam=build_mamdani_system()
    x={"buying":0,"maint":0,"doors":2,"persons":2,"lug_boot":2,"safety":2}
    y=predict_one(mam,x)
    assert y>=-0.5 and y<=3.5
