import skfuzzy.control as ctrl
from .variables import build_variables
from .rulebase import build_rules

def build_mamdani_system(mf_width=0.6):
    v=build_variables(mf_width=mf_width)
    rules=build_rules(v)
    system=ctrl.ControlSystem(rules)
    sim=ctrl.ControlSystemSimulation(system)
    return {"vars":v,"rules":rules,"sim":sim}
