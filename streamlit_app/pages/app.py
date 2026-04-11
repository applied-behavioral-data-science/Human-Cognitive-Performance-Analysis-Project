import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# LOAD DATA (once)
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("clean_cognitive_data.csv")
    return df

df = load_data()

# -----------------------------
# PAGE TITLE
# -----------------------------
st.title("Caffeine Intake & Cognitive Score")
st.write("Explore how caffeine intake relates to cognitive performance across the dataset.")

# -----------------------------
# USER INPUT
# -----------------------------
st.subheader("Your caffeine intake")
user_caffeine = st.slider(
    "How much caffeine do you consume per day? (mg)",
    min_value=0,
    max_value=600,
    value=100,
    step=10,
    help="A typical coffee has ~95mg of caffeine."
)

st.caption("Common reference points: Tea ≈ 40mg | Coffee ≈ 95mg | Energy drink ≈ 150mg")

margin = 50  # mg window used for chart highlight

st.divider()

# -----------------------------
# SCATTER PLOT: Caffeine vs Cognitive Score
# -----------------------------
st.subheader("Caffeine intake vs cognitive score")

fig = px.scatter(
    df,
    x="Caffeine_Intake",
    y="Cognitive_Score",
    opacity=0.3,
    labels={
        "Caffeine_Intake": "Caffeine intake (mg)",
        "Cognitive_Score": "Cognitive score"
    },
    color_discrete_sequence=["#378ADD"]
)

# Highlight user's caffeine band
fig.add_vrect(
    x0=user_caffeine - margin,
    x1=user_caffeine + margin,
    fillcolor="orange",
    opacity=0.15,
    line_width=0,
    annotation_text="Your range",
    annotation_position="top left"
)

# Vertical line for user input
fig.add_vline(
    x=user_caffeine,
    line_dash="dash",
    line_color="orange",
    line_width=2
)

fig.update_layout(height=400, hovermode="closest")
st.plotly_chart(fig, use_container_width=True)


# -----------------------------
# CAFFEINE vs REACTION TIME
# -----------------------------
st.subheader("Caffeine intake vs reaction time")
st.write("Reaction time is one of the inputs to the cognitive score model.")

fig3 = px.scatter(
    df,
    x="Caffeine_Intake",
    y="Reaction_Time",
    opacity=0.3,
    trendline="lowess",
    labels={
        "Caffeine_Intake": "Caffeine intake (mg)",
        "Reaction_Time": "Reaction time (ms)"
    },
    color_discrete_sequence=["#1D9E75"]
)

fig3.add_vline(
    x=user_caffeine,
    line_dash="dash",
    line_color="orange",
    line_width=2
)

fig3.update_layout(height=350)
st.plotly_chart(fig3, use_container_width=True)


