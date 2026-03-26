import streamlit as st

# this is another page. it will show up in the left navigation bar

st.title('Calculate your score!')

# user input
# we should check that these are being used in the model

# Age
st.subheader('Age')
age = st.slider('How old are you?', 18, 100, 30)

# Gender
st.subheader('Gender')
gender = st.selectbox(
    'What is your gender?',
    ('Female', 'Male', 'Nonbinary')
    )

# Sleep scales: 0-15 hours
st.subheader('Sleep')
sleep = st.slider("How many hours do you sleep on an average night?", 0, 15, 8)

# Screen time: 0-15 hours

# Caffeine intake: 0-400 mg

# Stress Level: 1-10 (1 no/low stress, 10 extreme stress)

# Exercise time: 0-10 hours 

# display results
