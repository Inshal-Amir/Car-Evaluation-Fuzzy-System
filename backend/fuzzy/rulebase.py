import skfuzzy.control as ctrl

def build_rules(v):
    buying=v["buying"]
    maint=v["maint"]
    doors=v["doors"]
    persons=v["persons"]
    lug_boot=v["lug_boot"]
    safety=v["safety"]
    out=v["out"]

    rules=[]

    rules.append(ctrl.Rule(safety["low"],out["unacc"]))
    rules.append(ctrl.Rule(persons["2"],out["unacc"]))
    rules.append(ctrl.Rule((safety["low"]|persons["2"])&(buying["vhigh"]|maint["vhigh"]),out["unacc"]))

    rules.append(ctrl.Rule((safety["med"]&persons["4"]&(lug_boot["med"]|lug_boot["big"]))&(buying["low"]|buying["med"]),out["acc"]))
    rules.append(ctrl.Rule((safety["med"]&persons["more"])&(maint["low"]|maint["med"]),out["acc"]))
    rules.append(ctrl.Rule((safety["high"]&persons["4"])&(buying["med"]|buying["low"]),out["good"]))
    rules.append(ctrl.Rule((safety["high"]&persons["more"])&(lug_boot["big"]|lug_boot["med"]),out["good"]))

    rules.append(ctrl.Rule((safety["high"]&persons["more"]&lug_boot["big"])&(buying["low"]&maint["low"]),out["vgood"]))
    rules.append(ctrl.Rule((safety["high"]&persons["more"])&(buying["low"]|maint["low"]),out["vgood"]))
    rules.append(ctrl.Rule((safety["high"]&persons["more"])&(buying["med"]&maint["med"])&(doors["4"]|doors["5more"]),out["vgood"]))

    rules.append(ctrl.Rule((buying["vhigh"]&maint["vhigh"])&(safety["med"]|safety["low"]),out["unacc"]))
    rules.append(ctrl.Rule((buying["high"]&maint["high"])&(safety["low"]|persons["2"]),out["unacc"]))

    rules.append(ctrl.Rule((safety["high"]&persons["4"])&(lug_boot["big"])&(maint["med"]|maint["low"]),out["good"]))
    rules.append(ctrl.Rule((safety["med"]&persons["4"])&(lug_boot["small"])&(buying["high"]|maint["high"]),out["unacc"]))
    rules.append(ctrl.Rule((safety["med"]&persons["4"])&(buying["low"]|maint["low"])&(lug_boot["big"]|lug_boot["med"]),out["acc"]))

    return rules

def rule_texts():
    return [
        "IF safety is low THEN class is unacc",
        "IF persons is 2 THEN class is unacc",
        "IF (safety is low OR persons is 2) AND (buying is vhigh OR maint is vhigh) THEN unacc",
        "IF safety is med AND persons is 4 AND (lug_boot is med OR big) AND (buying is low OR med) THEN acc",
        "IF safety is med AND persons is more AND (maint is low OR med) THEN acc",
        "IF safety is high AND persons is 4 AND (buying is med OR low) THEN good",
        "IF safety is high AND persons is more AND (lug_boot is big OR med) THEN good",
        "IF safety is high AND persons is more AND lug_boot is big AND buying is low AND maint is low THEN vgood",
        "IF safety is high AND persons is more AND (buying is low OR maint is low) THEN vgood",
        "IF safety is high AND persons is more AND buying is med AND maint is med AND (doors is 4 OR 5more) THEN vgood",
        "IF buying is vhigh AND maint is vhigh AND (safety is med OR low) THEN unacc",
        "IF buying is high AND maint is high AND (safety is low OR persons is 2) THEN unacc",
        "IF safety is high AND persons is 4 AND lug_boot is big AND (maint is med OR low) THEN good",
        "IF safety is med AND persons is 4 AND lug_boot is small AND (buying is high OR maint is high) THEN unacc",
        "IF safety is med AND persons is 4 AND (buying is low OR maint is low) AND (lug_boot is big OR med) THEN acc",
    ]
