import joblib
from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi import HTTPException

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




# ###gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
#        'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
#        'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
#        'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
#        'MonthlyCharges', 'TotalCharges', 'Churn'