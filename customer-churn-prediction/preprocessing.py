import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def preprocess(df):
    """
    This function is to cover all the preprocessing steps on the churn dataframe. It involves selecting important features, encoding categorical data, handling missing values,feature scaling and splitting the data
    """
    #Defining the map function
    def binary_map(feature):
        return feature.map({'Yes':1, 'No':0})
    
    # Encode binary categorical features
    df['Gender'] = df['Gender'].apply(binary_map)

    #Drop values based on operational options
    # if (option == "Online"):
    columns = ['Age', 'Gender', 'Location', 'Subscription_Length_Months', 'Monthly_Bill', 'Total_Usage_GB']
    # columns = ['SeniorCitizen', 'Dependents', 'tenure', 'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges', 'MultipleLines_No_phone_service', 'MultipleLines_Yes', 'InternetService_Fiber_optic', 'InternetService_No', 'OnlineSecurity_No_internet_service', 'OnlineSecurity_Yes', 'OnlineBackup_No_internet_service', 'TechSupport_No_internet_service', 'TechSupport_Yes', 'StreamingTV_No_internet_service', 'StreamingTV_Yes', 'StreamingMovies_No_internet_service', 'StreamingMovies_Yes', 'Contract_One_year', 'Contract_Two_year', 'PaymentMethod_Electronic_check']
    #Encoding the other categorical categoric features with more than two categories
    df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
    # elif (option == "Batch"):
    #     pass
    #     df = df[['SeniorCitizen','Dependents','tenure','PhoneService','MultipleLines','InternetService','OnlineSecurity',
    #             'OnlineBackup','TechSupport','StreamingTV','StreamingMovies','Contract','PaperlessBilling','PaymentMethod',
    #             'MonthlyCharges','TotalCharges']]
    #     columns = ['SeniorCitizen', 'Dependents', 'tenure', 'PhoneService', 'PaperlessBilling', 'MonthlyCharges', 'TotalCharges', 'MultipleLines_No_phone_service', 'MultipleLines_Yes', 'InternetService_Fiber_optic', 'InternetService_No', 'OnlineSecurity_No_internet_service', 'OnlineSecurity_Yes', 'OnlineBackup_No_internet_service', 'TechSupport_No_internet_service', 'TechSupport_Yes', 'StreamingTV_No_internet_service', 'StreamingTV_Yes', 'StreamingMovies_No_internet_service', 'StreamingMovies_Yes', 'Contract_One_year', 'Contract_Two_year', 'PaymentMethod_Electronic_check']
    #     #Encoding the other categorical categoric features with more than two categories
    #     df = pd.get_dummies(df).reindex(columns=columns, fill_value=0)
    # else:
    #     print("Incorrect operational options")


    #feature scaling
    #feature scaling
    sc = MinMaxScaler()
    df['Age'] = sc.fit_transform(df[['Age']])
    df['Subscription_Length_Months'] = sc.fit_transform(df[['Subscription_Length_Months']])
    df['Monthly_Bill'] = sc.fit_transform(df[['Monthly_Bill']])
    df['Total_Usage_GB'] = sc.fit_transform(df[['Total_Usage_GB']])
    return df
        




