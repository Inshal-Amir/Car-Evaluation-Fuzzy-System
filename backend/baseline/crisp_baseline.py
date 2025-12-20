def predict_crisp(x):
    buying=x["buying"]
    maint=x["maint"]
    persons=x["persons"]
    lug_boot=x["lug_boot"]
    safety=x["safety"]
    if safety==0 or persons==0:
        return 0
    if safety==2 and persons==2 and (buying==0 or maint==0) and lug_boot==2:
        return 3
    if safety==2 and persons==2 and (buying<=1 and maint<=1):
        return 3
    if safety==2 and persons>=1 and lug_boot>=1 and buying<=1:
        return 2
    if safety>=1 and persons>=1 and buying<=1:
        return 1
    return 0
