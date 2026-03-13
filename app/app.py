import streamlit as st

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
    gender = st.selectbox("What is your gender",['Male','Female'])
    gender = 1 if gender == 'Male' else 0

    seniorcitizen = st.selectbox("Are you a Senior Citizen",['Yes','No'])
    seniorcitizen = 1 if seniorcitizen == 'Yes' else 0

    
