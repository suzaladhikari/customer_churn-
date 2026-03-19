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
        'Tenure': tenure,
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
    API_URL = os.getenv("API_URL", "http://localhost:8000")
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