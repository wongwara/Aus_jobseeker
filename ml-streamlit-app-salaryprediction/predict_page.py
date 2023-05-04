# Import OrdinalEncoder from sklearn.preprocessing
from sklearn.preprocessing import OrdinalEncoder
import streamlit as st
import pandas as pd

def show_predict_page():
    st.title("Software Developer Salary Prediction")

    st.write("""### We need some information to predict the salary""")

    Jobclassification = (
        'Information & Communication Technology',
       'Banking & Financial Services', 'Science & Technology',
       'Education & Training', 'Government & Defence',
       'Consulting & Strategy', 'Healthcare & Medical',
       'Human Resources & Recruitment', 'Marketing & Communications',
       'Retail & Consumer Products', 'Administration & Office Support',
       'Accounting', 'Insurance & Superannuation',
       'Mining, Resources & Energy', 'Real Estate & Property',
       'Manufacturing, Transport & Logistics', 'Engineering',
    )
    
    isRightToWorkRequired = (
        '0',
        '1',
    )

    State = (
        '0',
        '1',
        '2',
    )
    
    Python = (
        '0',
        '1',
    )
    
    SQL = (
        '0',
        '1',
    )
    
    R = (
        '0',
        '1',
    )
    
    Tableau = (
        '0',
        '1',
    )
    
    SAS = (
        '0',
        '1',
    )
    
    Matlab = (
        '0',
        '1',
    )
    
    Hadoop = (
        '0',
        '1',
    )
    
    Spark = (
        '0',
        '1',
    )
    
    Java = (
        '0',
        '1',
    )  
    
    Scala = (
        '0',
        '1',
    )
    
    recruiter = (
        '0',
        '1',
    )
    
    Jobclassification = st.selectbox("Jobclassification", Jobclassification)
    isRightToWorkRequired = st.selectbox("isRightToWorkRequired", isRightToWorkRequired)
    st.write("f': 0, 't': 1")
    State = st.selectbox("State", State)
    st.write("'Australian Capital Territory':0, 'South Australia':1,'Western Australia':2")
    Python = st.selectbox("Python", Python)
    st.write("'Yes':1, 'No':0")
    SQL = st.selectbox("SQL", SQL)
    st.write("'Yes':1, 'No':0")
    R = st.selectbox("R", R)
    st.write("'Yes':1, 'No':0")
    Tableau = st.selectbox("Tableau", Tableau)
    st.write("'Yes':1, 'No':0")
    SAS = st.selectbox("SAS", SAS)
    st.write("'Yes':1, 'No':0")
    Matlab = st.selectbox("Matlab", Matlab)
    st.write("'Yes':1, 'No':0")
    Hadoop = st.selectbox("Hadoop", Hadoop)
    st.write("'Yes':1, 'No':0")
    Spark = st.selectbox("Spark", Spark)
    st.write("'Yes':1, 'No':0")
    Java = st.selectbox("Java", Java)
    st.write("'Yes':1, 'No':0")
    Scala = st.selectbox("Scala", Scala)
    st.write("'Yes':1, 'No':0")
    recruiter = st.selectbox("recruiter", recruiter)
    st.write("'Yes':1, 'No':0")
    
    # Input widgets
    teaser_input = st.text_input(
        "Enter teaser from your search , if None please type (-)",'')
    desktopAdTemplate_input = st.text_input(
        "Enter desktopAdTemplate from your search , if None please type (-)",'')
    
    st.sidebar.text_input('desktopAdTemplate', '')
    
    ok = st.button("Calculate Salary")
    if ok:
        X = np.array([[Jobclassification, isRightToWorkRequired, State,
        Python,SQL,R,Tableau,SAS,Matlab,Hadoop,Spark,Java,Scala,recruiter,
        teaser,desktopAdTemplate
        ]])
        X[:, 0] = Jobclassification.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")
        

