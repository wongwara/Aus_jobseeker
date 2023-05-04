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
        "0",
        "1",
    )

    State = (
        '0',
        '1',
        '2',
    )
    Python = (
        "0",
        "1",
    )
    SQL = (
        "0",
        "1",
    )
    R = (
        "0",
        "1",
    )
    Tableau = (
        "0",
        "1",
    )
    SAS = (
        "0",
        "1",
    )
    Matlab = (
        "0",
        "1",
    )
    Hadoop = (
        "0",
        "1",
    )
    Spark = (
        "0",
        "1",
    )
    Scala = (
        "0",
        "1",
    )
    recruiter = (
        "0",
        "1",
    )

    Jobclassification = st.selectbox("Jobclassification", Jobclassification)
    isRightToWorkRequired = st.selectbox("isRightToWorkRequired", isRightToWorkRequired)
    State = st.selectbox("State", State)
    Python = st.selectbox("Python", Python)
    SQL = st.selectbox("SQL", SQL)
    R = st.selectbox("R", R)
    Tableau = st.selectbox("Tableau", Tableau)
    SAS = st.selectbox("SAS", SAS)
    Matlab = st.selectbox("Matlab", Matlab)
    Hadoop = st.selectbox("Hadoop", Hadoop)
    Spark = st.selectbox("Spark", Spark)
    Java = st.selectbox("Java", Java)
    Scala = st.selectbox("Scala", Scala)
    recruiter = st.selectbox("recruiter", recruiter)
    
    # Input widgets
    st.sidebar.subheader('Input features')
    teaser = st.sidebar.slider('teaser', {teaser})
    desktopAdTemplate = st.sidebar.slider('desktopAdTemplate', {desktopAdTemplate})
 
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
        

