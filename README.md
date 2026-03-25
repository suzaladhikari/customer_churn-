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
## Machine Learning Models Performance

| Model             | Precision | Recall  | F1-Score |
|-------------------|-----------|--------|----------|
| Logistic Regression | 49.83%   | 79.94% | 61.39%  |
| Linear SVM         | 47.57%   | 49.73% | 48.63%  |
| Naive Bayes        | 51.44%   | 71.66% | 59.89%  |
| Decision Tree      | 50.18%   | 75.67% | 60.34%  |
| Random Forest      | 49.75%   | 81.02% | 61.65%  |
| XGBoost            | 62.12%   | 48.66% | 54.57%  |


### 🔑 Key Features
1. Predicts whether a customer is likely to churn using a trained machine learning model.
2. Performs data cleaning and preprocessing, including handling missing values and preparing features for modeling.
3. Uses a FastAPI backend to handle requests from the frontend and return predictions.
4. Provides an interactive user interface through a Streamlit application.
5. The entire project is containerized using Docker and Docker Compose for consistent deployment.
6. The backend is deployed on Render, allowing the app to access the model via a live API.


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
1. The user interacts with the application through the Streamlit web interface.
2. The information entered by the user is sent to the FastAPI backend for processing.
3. The backend cleans and prepares the data, then applies the trained machine learning model.
4. The model generates a prediction indicating whether the customer is likely to churn or not.
5. The prediction is sent back and displayed on the Streamlit interface for the user to see.

---

## 🎯 Project Goal
The goal of this project is to:
- Build a real-world machine learning application  
- Understand end-to-end deployment using MLOps tools  
- Create a scalable and production-ready system  
- Apply data science concepts to solve business problems  