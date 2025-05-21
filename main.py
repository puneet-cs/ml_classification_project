import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title = "Bajaj Finance Credit Risk Modeling")

st.title("Bajaj Finance Credit Risk Modeling")

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

with row1[0]:
    age = st.number_input('Age', min_value = 18, step = 1, max_value = 100, value = 28)
with row1[1]:
    income = st.number_input("Income", min_value = 0, value = 100000)
with row1[2]:
    loan_amount = st.number_input("Loan amount", min_value = 0, value = 50000)

# calculate loan to income ratio
loan_to_income_ratio = loan_amount / income if income > 0 else 0
with row2[0]:
    st.text("Loan to income ratio")
    st.text(f"{loan_to_income_ratio: .2f}")

with row2[1]:
    loan_tenure_months = st.number_input("Loan tenure months", min_value = 0, value = 36)
with row2[2]:
    avg_dpq_per_delinquency = st.number_input("Avg DPD", min_value = 0, value = 20)

with row3[0]:
    delinquency_ratio = st.number_input('Delinquency ratio', min_value = 0, step = 1, max_value = 100, value = 28)
with row3[1]:
    credit_utilization_ratio = st.number_input("Credit utilization ratio", min_value = 0, max_value = 100, value = 30)
with row3[2]:
    num_open_accounts = st.number_input("num open accounts", min_value = 1,max_value = 4, value = 2)

with row4[0]:
    residence_type = st.selectbox('Residence type', ['Owned', 'Mortgage', 'Rented'])
with row4[1]:
    loan_purpose = st.selectbox("loan purpose", ['Home', 'Education', 'Auto', 'Personal'])
with row4[2]:
    loan_type = st.selectbox("loan type", ['Secured' ,'Unsecured'])

if st.button('Calculate Risk'):
    probability, credit_score, rating = predict(age, income, loan_amount, loan_tenure_months, avg_dpq_per_delinquency,
                                                delinquency_ratio, credit_utilization_ratio, num_open_accounts,
                                                residence_type, loan_purpose, loan_type)
    
    st.write(f"Default Probability: {probability: .2f}")
    st.write(f"Credit Score: {credit_score}")
    st.write(f"Rating: {rating}")