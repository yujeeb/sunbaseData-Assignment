#Import libraries
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

#load the model from disk
import joblib
model = joblib.load(r"./notebook/model.sav")

#Import python scripts
from preprocessing import preprocess

def main():
    #Setting Application title
    st.title('Customer Churn Prediction App - SunBase Data Internship Assignment')

      #Setting Application description
    st.markdown("""
     :dart:  This Streamlit app is made to predict customer churn for SunBase Data Internship Assignment.
    The application is functional for both online prediction and batch data prediction. \n
    """)
    st.markdown("<h3></h3>", unsafe_allow_html=True)

    #Setting Application sidebar default
    image = Image.open('App.jpg')
    st.sidebar.info('This app is created to predict Customer Churn')
    st.sidebar.image(image)

    st.info("Input data below")
    age = st.number_input('Age', min_value=0, max_value=150, value=0)
    gender = st.selectbox('Gender:', ('Male', 'Female'))
    location = st.selectbox('Location', ('Chicago', 'Houston', 'Los Angeles', 'Miami', 'New York'))
    subscription_length_months = st.number_input('Subscription Length (Months)', min_value=0, max_value=70, value=0)
    monthly_bill = st.number_input('Monthly Bill',min_value=0, max_value=10000, value=0)
    total_usage_GB = st.number_input('Total Usage (GB)',min_value=0, max_value=1000, value=0)

    data = {
            'Age': age,
            'Gender': gender,
            'Location': location,
            'Subscription_Length_Months': subscription_length_months,
            'Monthly_Bill': monthly_bill,
            'Total_Usage_GB': total_usage_GB
            }
    features_df = pd.DataFrame.from_dict([data])
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.write('Overview of input is shown below')
    st.markdown("<h3></h3>", unsafe_allow_html=True)
    st.dataframe(features_df)


    #Preprocess inputs
    preprocess_df = preprocess(features_df)

    prediction = model.predict(preprocess_df)

    if st.button('Predict'):
        if prediction == 1:
            st.warning('Yes, the customer will terminate the service.')
        else:
            st.success('No, the customer is happy with Telco Services.')
    

    # else:
    #     st.subheader("Dataset upload")
    #     uploaded_file = st.file_uploader("Choose a file")
    #     if uploaded_file is not None:
    #         data = pd.read_csv(uploaded_file)
    #         #Get overview of data
    #         st.write(data.head())
    #         st.markdown("<h3></h3>", unsafe_allow_html=True)
    #         #Preprocess inputs
    #         preprocess_df = preprocess(data, "Batch")
    #         if st.button('Predict'):
    #             #Get batch prediction
    #             prediction = model.predict(preprocess_df)
    #             prediction_df = pd.DataFrame(prediction, columns=["Predictions"])
    #             prediction_df = prediction_df.replace({1:'Yes, the customer will terminate the service.', 
    #                                                 0:'No, the customer is happy with Telco Services.'})

    #             st.markdown("<h3></h3>", unsafe_allow_html=True)
    #             st.subheader('Prediction')
    #             st.write(prediction_df)
            
if __name__ == '__main__':
        main()




