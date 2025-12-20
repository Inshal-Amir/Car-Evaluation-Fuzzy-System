import numpy as np
import skfuzzy.control as ctrl
from .membership import tri

def build_variables(mf_width=0.6):
    buying=ctrl.Antecedent(np.arange(0,3.01,0.01),"buying")
    maint=ctrl.Antecedent(np.arange(0,3.01,0.01),"maint")
    doors=ctrl.Antecedent(np.arange(0,3.01,0.01),"doors")
    persons=ctrl.Antecedent(np.arange(0,2.01,0.01),"persons")
    lug_boot=ctrl.Antecedent(np.arange(0,2.01,0.01),"lug_boot")
    safety=ctrl.Antecedent(np.arange(0,2.01,0.01),"safety")
    out=ctrl.Consequent(np.arange(0,3.01,0.01),"cls")

    for v in [buying,maint]:
        v["low"]=tri(v.universe,-0.5,0,1)
        v["med"]=tri(v.universe,0,1,2)
        v["high"]=tri(v.universe,1,2,3)
        v["vhigh"]=tri(v.universe,2,3,3.5)

    doors["2"]=tri(doors.universe,-0.5,0,1)
    doors["3"]=tri(doors.universe,0,1,2)
    doors["4"]=tri(doors.universe,1,2,3)
    doors["5more"]=tri(doors.universe,2,3,3.5)


    persons["2"]=tri(persons.universe,-0.5,0,1)
    persons["4"]=tri(persons.universe,0,1,2)
    persons["more"]=tri(persons.universe,1,2,2.5)

    lug_boot["small"]=tri(lug_boot.universe,-0.5,0,1)
    lug_boot["med"]=tri(lug_boot.universe,0,1,2)
    lug_boot["big"]=tri(lug_boot.universe,1,2,2.5)

    safety["low"]=tri(safety.universe,-0.5,0,1)
    safety["med"]=tri(safety.universe,0,1,2)
    safety["high"]=tri(safety.universe,1,2,2.5)

    out["unacc"]=tri(out.universe,-0.5,0,1)
    out["acc"]=tri(out.universe,0,1,2)
    out["good"]=tri(out.universe,1,2,3)
    out["vgood"]=tri(out.universe,2,3,3.5)

    vars={"buying":buying,"maint":maint,"doors":doors,"persons":persons,"lug_boot":lug_boot,"safety":safety,"out":out}
    return vars
