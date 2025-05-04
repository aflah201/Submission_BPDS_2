import streamlit as st
import pandas as pd
from preprocessing import preprocessing, encoder_Application_mode, encoder_Course, encoder_Daytime_evening_attendance, encoder_Debtor, encoder_Displaced, encoder_Educational_special_needs, encoder_Fathers_occupation, encoder_Marital_status, encoder_Fathers_qualification, encoder_Gender, encoder_International, encoder_Mothers_occupation, encoder_Mothers_qualification, encoder_Nacionality, encoder_Previous_qualification, encoder_Scholarship_holder, encoder_Tuition_fees_up_to_date
from preprocessing import preprocessing
from predictions import predictions

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Student Dropout Prediction')
    st.write('This is a simple web app to predict student dropout based on the student data provided.')

data = pd.DataFrame()

col1, col2, col3 = st.columns(3)
with col1:
    Marital_status = st.selectbox(label='Marital Status', options=encoder_Marital_status.classes_, index=0)
    data["Marital_status"] = [Marital_status]
with col2:
    Application_mode = st.selectbox(label='Application Mode', options=encoder_Application_mode.classes_, index=0)
    data["Application_mode"] = [Application_mode]
with col3:
    Course = st.selectbox(label='Course', options=encoder_Course.classes_, index=0)
    data["Course"] = [Course]

col1, col2, col3 = st.columns(3)
with col1:
    Daytime_evening_attendance = st.selectbox(label='Daytime Evening Attendance', options=encoder_Daytime_evening_attendance.classes_, index=0)
    data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
with col2:
    Previous_qualification = st.selectbox(label='Previous Qualification', options=encoder_Previous_qualification.classes_, index=0)
    data["Previous_qualification"] = [Previous_qualification]
with col3:
    Nacionality = st.selectbox(label='Nacionality', options=encoder_Nacionality.classes_, index=0)
    data["Nacionality"] = [Nacionality]

col1, col2 = st.columns(2)
with col1:
    Mothers_qualification = st.selectbox(label='Mothers Qualification', options=encoder_Mothers_qualification.classes_, index=0)
    data["Mothers_qualification"] = [Mothers_qualification]
with col2:
    Fathers_qualification = st.selectbox(label='Fathers Qualification', options=encoder_Fathers_qualification.classes_, index=0)
    data["Fathers_qualification"] = [Fathers_qualification]

col1, col2 = st.columns(2)
with col1:
    Mothers_occupation = st.selectbox(label='Mothers Occupation', options=encoder_Mothers_occupation.classes_, index=0)
    data["Mothers_occupation"] = [Mothers_occupation]
with col2:
    Fathers_occupation = st.selectbox(label='Fathers Occupation', options=encoder_Fathers_occupation.classes_, index=0)
    data["Fathers_occupation"] = [Fathers_occupation]
    
col1, col2, col3 = st.columns(3)
with col1:
    Displaced = st.selectbox(label='Displaced', options=encoder_Displaced.classes_, index=0)
    data["Displaced"] = [Displaced]
with col2:
    Educational_special_needs = st.selectbox(label='Educational Special Needs', options=encoder_Educational_special_needs.classes_, index=0)
    data["Educational_special_needs"] = [Educational_special_needs]
with col3:
    Debtor = st.selectbox(label='Debtor', options=encoder_Debtor.classes_, index=0)
    data["Debtor"] = [Debtor]

col1, col2, col3, col4 = st.columns(4)
with col1:
    Tuition_fees_up_to_date = st.selectbox(label='Tuition Fees Up To Date', options=encoder_Tuition_fees_up_to_date.classes_, index=0)
    data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
with col2:
    Gender = st.selectbox(label='Gender', options=encoder_Gender.classes_, index=0)
    data["Gender"] = [Gender]
with col3:
    Scholarship_holder = st.selectbox(label='Scholarship Holder', options=encoder_Scholarship_holder.classes_, index=0)
    data["Scholarship_holder"] = [Scholarship_holder]
with col4:
    International = st.selectbox(label='International', options=encoder_International.classes_, index=0)
    data["International"] = [International]

col1, col2, col3, col4 = st.columns(4)
with col1:
    Age_at_enrollment = st.number_input('Age at Enrollment', min_value=16, max_value=70)
    data['Age_at_enrollment'] = [Age_at_enrollment]
with col2:
    Application_order = st.selectbox('Application Order', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    data['Application_order'] = [Application_order]
with col3:
    Admission_grade = st.number_input('Admission Grade', min_value=0, max_value=200)
    data['Admission_grade'] = [Admission_grade]
with col4:
    Previous_qualification_grade = st.number_input('Prev. Qualification Grade', min_value=0, max_value=200)
    data['Previous_qualification_grade'] = [Previous_qualification_grade]

st.header('Curricular Units 1st Semester')
col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_1st_sem_approved = st.number_input('1st Approved', min_value=0, max_value=100)
    data['Curricular_units_1st_sem_approved'] = [Curricular_units_1st_sem_approved]
with col2:
    Curricular_units_1st_sem_enrolled = st.number_input('1st Enrolled', min_value=0, max_value=100)
    data['Curricular_units_1st_sem_enrolled'] = [Curricular_units_1st_sem_enrolled]
with col3:
    Curricular_units_1st_sem_evaluations = st.number_input('1st Evaluation', min_value=0, max_value=100)
    data['Curricular_units_1st_sem_evaluations'] = [Curricular_units_1st_sem_evaluations]
with col4:
    Curricular_units_1st_sem_grade = st.number_input('1st Grade', min_value=0, max_value=100)
    data['Curricular_units_1st_sem_grade'] = [Curricular_units_1st_sem_grade]

Curricular_units_1st_sem_without_evaluations = st.number_input('1st Without Evaluations', min_value=0, max_value=100)
data['Curricular_units_1st_sem_without_evaluations'] = [Curricular_units_1st_sem_without_evaluations]

st.header('Curricular Units 2nd Semester')
col1, col2, col3, col4 = st.columns(4)
with col1:
    Curricular_units_2nd_sem_approved = st.number_input('2nd Approved', min_value=0, max_value=100)
    data['Curricular_units_2nd_sem_approved'] = [Curricular_units_2nd_sem_approved]
with col2:
    Curricular_units_2nd_sem_enrolled = st.number_input('2nd Enrolled', min_value=0, max_value=100)
    data['Curricular_units_2nd_sem_enrolled'] = [Curricular_units_2nd_sem_enrolled]
with col3:
    Curricular_units_2nd_sem_evaluations = st.number_input('2nd Evaluation', min_value=0, max_value=100)
    data['Curricular_units_2nd_sem_evaluations'] = [Curricular_units_2nd_sem_evaluations]
with col4:
    Curricular_units_2nd_sem_grade = st.number_input('2nd Grade', min_value=0, max_value=100)
    data['Curricular_units_2nd_sem_grade'] = [Curricular_units_2nd_sem_grade]

Curricular_units_2nd_sem_without_evaluations = st.number_input('2nd Without Evaluations', min_value=0, max_value=100)
data['Curricular_units_2nd_sem_without_evaluations'] = [Curricular_units_2nd_sem_without_evaluations]

with st.expander('View the Raw Data'):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    data = preprocessing(data)
    with st.expander('View the Preprocessed Data'):
        st.dataframe(data=data, width=800, height=10)
    print(data)
    result = predictions(data)
    st.write(f'The student is predicted to: {result}')