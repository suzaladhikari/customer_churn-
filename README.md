# 📊 Customer Churn Prediction MLOps Project

## 📌 Introduction
Customer churn is one of the biggest challenges for businesses today. Retaining existing customers is often more cost-effective than acquiring new ones, which makes predicting customer behavior extremely valuable.

This project focuses on predicting whether a customer is likely to churn or not using machine learning. By analyzing customer data and patterns, the model provides insights that can help businesses take proactive steps to improve customer retention.


## 🚀 Project Overview
This is a complete end-to-end **MLOps-based Customer Churn Prediction system** that integrates machine learning with modern deployment practices.

The project is designed to simulate a real-world production pipeline where a machine learning model is not only built but also deployed and made accessible through a web application.

## 📁 Project Structure

The project is organized in a modular and scalable way to reflect a real-world MLOps pipeline:


```
├── .vscode/                     # VS Code configuration files

├── app/                         # Streamlit Frontend
│   ├── app.py                   # Main Streamlit application
│   └── streamlitrequirements.txt # Frontend dependencies

├── churn_fastapi/               # FastAPI Backend
│   ├── main.py                  # API endpoints for predictions
│   ├── churnpredictor.pkl       # Trained ML model
│   └── fastrequirements.txt     # Backend dependencies

├── datasets/                    # Data files
│   ├── churnData.csv            # Raw dataset
│   ├── cleaned.csv              # Cleaned dataset
│   ├── formodel.csv             # Processed dataset for training
│   └── modelperformance.csv     # Model evaluation results

├── EDA/                         # Exploratory Data Analysis
│   └── eda.ipynb                # Data analysis and visualization

├── Model Preparation/           # Model development pipeline
│   ├── featureengineering.ipynb # Feature engineering steps
│   └── model.ipynb              # Model training and evaluation

├── docker-compose.yml           # Multi-container Docker setup
├── dockerfile.churnstreamlit    # Dockerfile for Streamlit app
├── dockerfile.fastapi           # Dockerfile for FastAPI backend
```


### 🔑 Key Features
- 📊 Predicts customer churn using a trained machine learning model  
- 🧹 Includes data cleaning and preprocessing (handling null values, feature preparation)  
- ⚡ FastAPI backend for handling model inference requests  
- 🎨 Streamlit frontend for an interactive user interface  
- 🐳 Containerized using Docker and Docker Compose  
- ☁️ Backend deployed on Render for live API access  

## Running the project and other dependencies locally 

## 🐍 How to Run Locally

1. **Clone this repository**  
   Copy and paste the following commands in your terminal:

   ```bash
   git clone https://github.com/your-username/churn-prediction-mlops.git
   cd churn-prediction-mlops
   ```

2. **Install required packages for Streamlit (frontend)**

   ```bash
   pip install -r app/streamlitrequirements.txt
   ```

3. **Install required packages for FastAPI (backend)**

   ```bash
   pip install -r churn_fastapi/fastrequirements.txt
   ```

4. **Run the FastAPI backend**

   ```bash
   uvicorn churn_fastapi.main:app --reload
   ```

5. **Run the Streamlit frontend**

   ```bash
   streamlit run app/app.py
   ```

6. **Access the application**
   - Streamlit App → http://localhost:8501  
   - FastAPI Docs → http://localhost:8000/docs
## 🧠 How the System Works
1. The user interacts with the Streamlit web application  
2. User inputs are sent to the FastAPI backend  
3. The backend processes the data and applies the trained ML model  
4. The model returns a prediction (churn / not churn)  
5. The result is displayed back on the Streamlit interface  

---

## 🎯 Project Goal
The goal of this project is to:
- Build a real-world machine learning application  
- Understand end-to-end deployment using MLOps tools  
- Create a scalable and production-ready system  
- Apply data science concepts to solve business problems  