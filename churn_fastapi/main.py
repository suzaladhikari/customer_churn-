import joblib
from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi import HTTPException
import numpy as np 

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
def predict(data:Data):
    try:
        input_data = np.array([data.gender, data.SeniorCitizen, data.Partner, data.Dependents,data.tenure,  data.PhoneService, data.MultipleLines, data.InternetService, data.OnlineSecurity,data.OnlineBackup, data.DeviceProtection, data.TechSupport,data.StreamingTV, data.StreamingMovies, data.Contract,data.PaperlessBilling, data.PaymentMethod, data.MonthlyCharges,data.TotalCharges])
    
    except Exception as e:
        raise HTTPException(status_code=404, detail = e)



# ###gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
#        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
#        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
#        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
#        'MonthlyCharges', 'TotalCharges', 'Churn'