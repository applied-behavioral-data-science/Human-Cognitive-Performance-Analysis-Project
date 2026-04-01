import streamlit as st
import pandas as pd

# this is another page. it will show up in the left navigation bar

st.title('Calculate your score!')

# user input

# Age
st.subheader('Age')
age = st.slider("How old are you?", 18, 100, 30)

# Gender
st.subheader('Gender')
gender = st.selectbox(
    "What is your gender?",
    ('Female', 'Male', 'Other')
    )

# Sleep scales: 0-15 hours
st.subheader('Sleep')
sleep = 5 # replace with slider

# Screen time: 0-15 hours
st.subheader('Daily screen time')
screen = st.slider("What''s your daily screen time?", 0,12,4)

# Caffeine intake: 0-400 mg
st.subheader('Caffeine intake')
caffeine = 100 # replace this line with a slider

# Stress Level: 1-10 (1 no/low stress, 10 extreme stress)
st.subheader('Stress level')
stress = st.slider("How stressed are you right now?", 1,10,4)

# Diet
st.subheader('Diet')
diet = st.selectbox('',('Non-Vegetarian','Vegetarian','Vegan'))

# Exercise time: 0-10 hours 
st.subheader('Exercise time')
exercise = st.selectbox("How much do you exercise?", ('Low','Medium','High'))

memory = 50 # delete after model is replaced
rt = 50 # delete after model is replaced

# put user inputs into dataframe
input_data = pd.DataFrame({
    "Age": [age],
    "Sleep_Duration": [sleep],
    "Exercise_Frequency": [exercise],
    "Gender": [gender],
    "Diet_Type": [diet],
    "Caffeine_Intake": [caffeine],
    "Daily_Screen_Time": [screen],
    "Stress_Level": [stress],
    "Memory_Test_Score": [memory],
    "Reaction_Time": [rt]
})

# predict
if st.button("Predict Cognitive Score"):
    prediction = st.session_state.model.predict(input_data)
    st.success(f"Predicted cognitive score: {prediction[0]:.2f}")