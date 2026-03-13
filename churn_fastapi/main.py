import joblib
from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi import HTTPException
import numpy as np 
import os
import pandas as pd 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "churnpredictor.pkl")

model = joblib.load(model_path)

class Data(BaseModel):
    gender:int
    SeniorCitizen:int 
    Partner:int 
    Dependents:int
    tenure:int= 0
    PhoneService:int = 0
    MultipleLines:int = 0
    InternetService:int = 0 
    OnlineSecurity:int = 0
    OnlineBackup:int = 0 
    DeviceProtection:int = 0 
    TechSupport:int = 0 
    StreamingTV:int = 0 
    StreamingMovies:int = 0 
    Contract:int
    PaperlessBilling:int = 0 
    PaymentMethod:int
    MonthlyCharges: int
    TotalCharges:int 


app = FastAPI()

@app.get('/checking')
def check():
    return "It is working"
    
@app.post('/predict')
async def predict(data:Data):
    input_dataframe = pd.DataFrame([data.dict()])
    proba = model.predict_proba(input_dataframe)[:,1]
    prediction = proba



