from fuzzy.variables import build_variables
from fuzzy.rulebase import build_rules

def test_rule_count():
    v=build_variables()
    rules=build_rules(v)
    assert len(rules)>=10
