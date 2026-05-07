import streamlit as st
import pandas as pd
import os
from datetime import datetime
import pickle
import gspread
from google.oauth2.service_account import Credentials

# load model once
if "model" not in st.session_state:
    model_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "maitreya_cognitive_score_model.pkl")
    with open(model_path, "rb") as f:
        st.session_state.model = pickle.load(f)

        
# this is another page. it will show up in the left navigation bar

st.title('Calculate your score!')

# "Name"
st.subheader("Name")
name = st.text_input("Enter your name")
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
sleep = st.slider("How many hours of sleep do you get per night?", 0,15,7)

# Screen time: 0-15 hours
st.subheader('Daily screen time')
screen = st.slider("What''s your daily screen time?", 0,12,4)

# Caffeine intake: 0-400 mg
st.subheader('Caffeine intake')
user_caffeine = st.slider("How much caffeine do you consume per day? (mg)",
    min_value=0,
    max_value=600,
    value=100,
    step=10,
    help="A typical coffee has ~95mg of caffeine.")

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
    "Caffeine_Intake": [user_caffeine],
    "Daily_Screen_Time": [screen],
    "Stress_Level": [stress],
    "Memory_Test_Score": [memory],
    "Reaction_Time": [rt]
})

# predict
# -----------------------------
# SAVE FUNCTION
# -----------------------------
@st.cache_resource
def get_gsheet_worksheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
    creds = Credentials.from_service_account_info(
        st.secrets["gcp_service_account"], scopes=scopes
    )
    client = gspread.authorize(creds)
    return client.open_by_url(st.secrets["sheet_url"]).sheet1

def save_to_gsheet(data_dict):
    worksheet = get_gsheet_worksheet()
    column_order = [
        "Name", "Timestamp", "Age", "Gender", "Sleep_Duration",
        "Daily_Screen_Time", "Caffeine_Intake", "Stress_Level",
        "Diet_Type", "Exercise_Frequency", "Prediction",
    ]
    worksheet.append_row([data_dict[col] for col in column_order])

# -----------------------------
# BUTTON + PREDICTION
# -----------------------------
if st.button("Predict Cognitive Score", key="predict_score_button"):

    # optional: require name
    if not name.strip():
        st.warning("Please enter your name first.")
        st.stop()

    prediction = st.session_state.model.predict(input_data)
    score = float(prediction[0])

    # show result
    st.success(f"{name}, your predicted cognitive score is: {score:.2f}")

    # progress bar (0–100 scale)
    score_for_bar = max(0, min(int(score), 100))
    st.progress(score_for_bar)

    # indicator
    if score < 40:
        st.error("Indicator: Lower predicted cognitive score")
    elif score < 70:
        st.warning("Indicator: Moderate predicted cognitive score")
    else:
        st.success("Indicator: Higher predicted cognitive score")

    # save data
    result_data = {
        "Name": name,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Age": age,
        "Gender": gender,
        "Sleep_Duration": sleep,
        "Daily_Screen_Time": screen,
        "Caffeine_Intake": user_caffeine,
        "Stress_Level": stress,
        "Diet_Type": diet,
        "Exercise_Frequency": exercise,
        "Prediction": round(score, 2)
    }

    try:
        save_to_gsheet(result_data)
        st.info("Your response was saved to the Google Sheet.")
    except Exception as e:
        st.error(f"Could not save to Google Sheet: {e}")