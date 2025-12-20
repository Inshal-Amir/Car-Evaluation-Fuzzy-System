import numpy as np
from fuzzy.variables import build_variables

def test_membership_shapes():
    v=build_variables()
    buying=v["buying"]
    assert "low" in buying.terms
    assert len(buying.universe)>10
    low=buying["low"].mf
    assert float(np.max(low))<=1.0+1e-6
