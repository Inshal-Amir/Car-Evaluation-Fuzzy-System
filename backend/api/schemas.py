from pydantic import BaseModel

class PredictRequest(BaseModel):
    buying:str
    maint:str
    doors:str
    persons:str
    lug_boot:str
    safety:str

class PredictResponse(BaseModel):
    predicted_class:str
    crisp_output:float
    probs:dict
    fired_rules:list
