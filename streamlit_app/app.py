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
st.title("""
This is a title
""")

st.subheader("""
This is a subheader
""")

st.write("""
    We can write something about:
         
     * Our goal with this project
     * The dataset, the variables we chose to analyse, caveats
     * Short summary of our results

    And maybe display the results on different pages.
    """
)

# load model
with open('maitreya_cognitive_score_model.pkl', 'rb') as f:
    model_file = pickle.load(f)
    #st.write('model loaded!') # just checking it loaded

# save the variable so it can be used in other pages
st.session_state['model'] = model_file

# the following line is just to check what's in it
#st.write(st.session_state.model)

st.write ("" hello world "") 

