# note: if we do pages, the landing page will have the same name as this file, "app".
# we can of course change it later.

import streamlit as st
import pickle
#from sklearn.linear_model import LinearRegression

#set the page config
st.set_page_config(
    layout='wide',
    initial_sidebar_state='expanded',
    page_title="Human Cognitive Performance",
    page_icon="🧠 Human Cognitive Perfornance")
    
st.sidebar.header('🧠 Human Cognitive Performance')

st.sidebar.markdown('''
---
[Sidebar text! We don't *have* to write stuff here,
but it might be a good place to put a link to the repo.]

''')

# page content
# page content
st.title("Human Cognitive Performance Predictor")

st.markdown("""
Welcome to the **Human Cognitive Performance Predictor**.

This app was created to explore how lifestyle and personal factors may relate to cognitive performance.  
Using a trained machine learning model, users can input their own values and receive a predicted cognitive score based on patterns learned from the dataset.

### Included factors
- Age
- Gender
- Sleep Duration
- Daily Screen Time
- Caffeine Intake
- Stress Level
- Diet Type
- Exercise Frequency

### Purpose of the project
The goal of this project is to demonstrate how behavioral and lifestyle variables can be used in a predictive analytics workflow.  
It also provides an interactive way to engage with the model through a simple Streamlit application.

### Getting started
To begin, open the **Try It** page from the sidebar and enter your information.
""")


# load model
with open('maitreya_cognitive_score_model.pkl', 'rb') as f:
    model_file = pickle.load(f)
    #st.write('model loaded!') # just checking it loaded

# save the variable so it can be used in other pages
st.session_state['model'] = model_file

# the following line is just to check what's in it
#st.write(st.session_state.model)