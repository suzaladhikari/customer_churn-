import streamlit as st
import pandas as pd 
import requests
import os 
### This is the side bar 
st.sidebar.title("Explore the options")
page = st.sidebar.selectbox("",["🏠 Home",  " ℹ️ About the Model"," 📊  Prediction"," 👨‍💻 Developer"])
if page == '🏠 Home':
    st.title("Churn Detection Model")
    st.header("What is Churn Detection?")
    st.subheader("Churn detection is the process of identifying customers likely to stop using a product or service, often using machine learning to analyze behavior and predict risks. Once you can identify those customers that are at risk of cancelling, you should know exactly what marketing action to take for each individual customer to maximise the chances that the customer will remain.")

    st.divider()

    st.header("Why is the Customer Churn Important ")
    st.subheader("Customer churn is a common problem across businesses in many sectors. If you want to grow as a company, you have to invest in acquiring new clients. Every time a client leaves, it represents a significant investment lost. Both time and effort need to be channelled into replacing them. Being able to predict when a client is likely to leave, and offer them incentives to stay, can offer huge savings to a business.")

    st.divider()
    st.header("Machine Learning and Customer Churn")
    st.subheader("Machine Learning has emerged as powerful tool for churn prediction due to their ability to effectively analyze large, high-dimensional, and dynamic customer datasets.Traditional churn prediction methods, such as rule-based systems and statistical modeling, often failto adequately capture customer behavior's complexities. Conversely, ML approaches like DecisionTrees (DTs), Random Forests (RFs), Support Vector Machines (SVMs), and boosting algorithms (e.g.,XGBoost, LightGBM, CatBoost) have demonstrated strong predictive capabilities with structureddatasets")

    st.write("To explore more about the Models that we have used and to know about Machine Learning Models and Churn Detection, please go to  ℹ️ About the Model.")
    st.warning("⚠️ This is just a demo project. Please donot rely on the result for official conclusion.")



if page == ' 📊  Prediction':
    st.header("Predict the chance of Customer Churn !!")
    st.subheader("Just use the sidebar sliders and checkboxes to adjust the values, and the model will do the rest!")

    st.divider()

    st.subheader('🧍 Personal Info')
    gender = st.selectbox("Customer's Gender",['Male','Female'])
    gender = 1 if gender == 'Male' else 0

    seniorcitizen = st.selectbox("Is Customer Senior Citizen",['Yes','No'])
    seniorcitizen = 1 if seniorcitizen == 'Yes' else 0

    partner = st.selectbox("Does customer have a partner?", ["Yes", "No"])
    partner = 1 if partner == "Yes" else 0
    
    dependents = st.selectbox("Does customer have dependents?", ["Yes", "No"])
    dependents = 1 if dependents == "Yes" else 0

    st.divider()
    st.subheader(' 🌐 Package and Service Details')

    tenure_input = st.text_input("Number of months customer has used the service", value="0")

    try:
        tenure = int(tenure_input)
    except ValueError:
        tenure = 0
        st.warning("Please enter a valid number for tenure.")


    def yes_no_to_int(label):
        value = st.selectbox(label, ["Yes", "No"])
        return 1 if value == "Yes" else 0
    
    phone_service = yes_no_to_int("Does customer have a Phone Service ?")
    multiple_lines = yes_no_to_int("Do customer have Multiple lines?")
    online_security = yes_no_to_int("Does customer have Online Security?")
    online_backup = yes_no_to_int("Does customer have Online Backup?")
    device_protection = yes_no_to_int("Does customer have Device Protection?")
    tech_support = yes_no_to_int("Does customer have Tech Support?")
    streaming_tv = yes_no_to_int("Does customer have Streaming TV?")
    streaming_movies = yes_no_to_int("Does customer have Streaming Movies?")

    internet_service = st.selectbox("Type of Internet Service that the customer is using ",['DSL', 'Fiber optic', 'No'])
    mapping_internet = {'DSL':0, 'Fiber optic':1, 'No':2}
    internet_service = mapping_internet[internet_service]

    st.divider()
    st.subheader(' 📝 Contract and Payment Details')

    paperless_billing = yes_no_to_int("Does customer have Paperless Billing ?")

    contract_type = st.selectbox("Type of Contract that the customer is enrolled in ",['Month-to-month','One year','Two year'])   
    mapping_contract = {'Month-to-month':0, 'One year':1, 'Two year':2 }
    contract_type = mapping_contract[contract_type]

    payment_method = st.selectbox("Type of Payment Method used by the customer ",['Electronic check','Mailed check','Bank transfer (automatic)'
    ,'Credit card (automatic)'])
    mapping_payment = {'Electronic check':0, 'Mailed check':1,'Bank transfer (automatic)':2,   'Credit card (automatic)':3  }
    payment_method = mapping_payment[payment_method] 

    totalmonthlycharges = st.text_input("Total Monthly Charges paid by customer")
    totalcharges = st.text_input("Total Charges paid by customer")
    totalmonthlycharges = float(totalmonthlycharges) if totalmonthlycharges else 0
    totalcharges = float(totalcharges) if totalcharges else 0


    st.text("")
    st.markdown("---")
    st.subheader("Thank you for all the details you have provided! Click predict to see the results! ")

    dataframe_to_be_used = {
        'gender': gender,
        'SeniorCitizen': seniorcitizen,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone_service,
        'MultipleLines': multiple_lines,
        'InternetService': internet_service,
        'OnlineSecurity': online_security,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': streaming_tv,
        'StreamingMovies': streaming_movies,
        'Contract': contract_type,
        'PaperlessBilling': paperless_billing,
        'PaymentMethod': payment_method,
        'MonthlyCharges': totalmonthlycharges,
        'TotalCharges': totalcharges
    }

    dataframe = pd.DataFrame([dataframe_to_be_used])
    API_URL = os.getenv("API_URL", "https://customer-churn-9nt4.onrender.com")
    if st.button("Predict"):
        try:
            response = requests.post(f"{API_URL}/predict", json=dataframe_to_be_used)
            if response.status_code == 200:
                result = response.json()
                st.success(result['prediction'])
            else:
                st.error("Oops! Something went wrong", response.status_code)
        except Exception as e:
            st.error(f"Error connecting to API: {e}")
if page == ' ℹ️ About the Model':

    st.sidebar.markdown("""
    ---  
    ### ⚠️ Disclaimer

    This application was developed as part of a data science project and is based on a relatively small and synthetic dataset. While the model demonstrates how the given parameters help determine the risk of customer churn, it is not an official prediction is based on a small dataset.

    Please explore and learn from this tool, but do not interpret its output as an official conclusion for any major decision.
    """)

    st.title("Models used for the prediction of Churn Detection")

    st.header("Logisitc Regression")

    st.subheader("Logistic Regression was used as an initial model for the prediction of customer churn. The model was hyperparamter tuned with parameters such as 'C' value and regularization penalties. The precision, recall, and f1-score of the model are as follows")

    st.write("Precision: 49.83%")
    st.write("Recall:79.94%")
    st.write("F1-Score:61.39%")

    st.divider()

    st.header("Linear SVM")

    st.subheader("A Linear Support Vector Machine (SVM) model was used for the prediction of customer churn. The model was implemented using a pipeline that includes feature scaling with StandardScaler and classification using LinearSVC. Hyperparameter tuning was performed using GridSearchCV with StratifiedKFold cross-validation to find the optimal value of the regularization parameter 'C'. Class imbalance was handled using a 'balanced' class weight. The precision, recall, and F1-score of the model are as follows")  

    st.write("Precision: 47.57%")
    st.write("Recall: 49.73%")
    st.write("F1-Score: 48.63%")

    st.divider()

    st.header("Naive Bayes")

    st.subheader("A Naive Bayes model was used for the prediction of customer churn. The model was implemented using GaussianNB, which assumes that the features follow a normal distribution. The var_smoothing parameter was set to improve numerical stability. The model was trained on the dataset and evaluated using precision, recall, and F1-score, which are reported below")


    st.write("Precision: 51.44%")
    st.write("Recall: 71.66%")
    st.write("F1-Score: 59.89%")  

    st.divider()

    st.header("Decision Trees")

    st.subheader("A Decision Tree model was used for the prediction of customer churn. The model was implemented using the Gini impurity criterion, and class imbalance was handled using balanced class weights. Hyperparameter tuning was performed using GridSearchCV with StratifiedKFold cross-validation to optimize parameters such as max_depth, min_samples_split, min_samples_leaf, and max_features. The model's performance was evaluated using precision, recall, and F1-score, which are reported below")

    st.write("Precision: 50.18%")
    st.write("Recall: 75.67%")
    st.write("F1-Score: 60.34%")

    st.divider()


    st.header("Random Forest")

    st.subheader("A Random Forest model was used for the prediction of customer churn. The model is an ensemble learning method that builds multiple decision trees and combines their outputs to improve performance and reduce overfitting. The Gini impurity criterion was used for splitting, and class imbalance was handled using balanced class weights. The number of estimators was analyzed using out-of-bag (OOB) scoring, and further hyperparameter tuning was performed using GridSearchCV with StratifiedKFold cross-validation to optimize parameters such as max_features, max_depth, min_samples_split, and min_samples_leaf. The model was evaluated using precision, recall, and F1-score, which are reported below")

    st.write("Precision: 49.75%")
    st.write("Recall: 81.02%")
    st.write("F1-Score: 61.65%")


    st.divider()

    st.header("XGBoost")

    st.subheader("An XGBoost model was used for the prediction of customer churn. XGBoost is a powerful gradient boosting algorithm that builds sequential decision trees, where each new tree corrects the errors of the previous ones. The model was initialized with a learning rate of 0.1. Hyperparameter tuning was performed using GridSearchCV with StratifiedKFold cross-validation to optimize parameters such as n_estimators, colsample_bytree, max_depth, and subsample. The final model was selected based on the best cross-validation performance and evaluated using precision, recall, and F1-score, which are reported below")

    st.write("Precision: 62.12%")
    st.write("Recall: 48.66%")
    st.write("F1-Score: 54.57%")

    st.divider()

    st.title("Other metrics used to select the best model")

    st.header("Here is the dataframe that shows the metrics and the value on all the models used!")




    st.divider()

    st.header("Selected Model : Random Forest Classifier")

    st.subheader("Threshold Optimization Strategy")

    st.write("Since this project focuses on customer churn prediction, the primary goal is to reduce False Negatives — cases where customers who are likely to churn are incorrectly classified as non-churners. Missing such customers can lead to direct business loss, as no retention action would be taken.")

    st.write("To address this, probability thresholds were adjusted instead of relying on the default value of 0.5. The model's predicted probabilities were evaluated across a range of threshold values, and for each threshold, key metrics such as recall, precision, false negative rate (FNR), and false positive rate (FPR) were calculated.")

    st.write("By lowering the threshold, the model becomes more sensitive to identifying churners, which increases recall and reduces the false negative rate. Although this may increase false positives, it is acceptable in this context because it is more important to identify potential churners than to miss them.")

    st.write("The optimal threshold was selected based on achieving a high recall while minimizing the false negative rate, ensuring that the model effectively captures as many churn-risk customers as possible.")

if page == ' 👨‍💻 Developer':
    st.title("Greetings 👋 ¡Hola! 👋 Bonjour")
    st.text("")
    st.subheader("""Hi, I'm Sujal Adhikari, a sophomore at Caldwell University and an aspiring Data Scientist.This churn prediction project is especially meaningful to me—it represents my first real step into applied machine learning and solving business problems using data.Through this project, I explored how companies can identify customers who are likely to leave, and how data-driven insights can help improve retention strategies. Building this from the ground up taught me not just the technical side of machine learning, but also the importance of data cleaning, feature engineering, and model evaluation.There were definitely challenges along the way, but each obstacle helped me grow stronger and more confident in my skills. Every late night debugging models and analyzing results was worth it.This project is just the beginning of my journey into data science. I’m excited to continue learning, building impactful projects, and turning data into meaningful insights.
    """)
    st.text("")
    st.divider()
    
    st.subheader("Thank You 🙏 Gracias! 🙏 Merci")

