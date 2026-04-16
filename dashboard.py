import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import os
import joblib

# LOAD ML MODEL
model = joblib.load("model.pkl")

# PAGE CONFIG
st.set_page_config(page_title="SportGuard AI", layout="wide")

# 🎨 CLEAN PROFESSIONAL LIGHT UI
st.markdown("""
<style>
body {
    background-color: #f4f6fb;
}

/* HEADER */
.header {
    background: #1e3a8a;
    padding: 25px;
    border-radius: 10px;
    color: white;
    text-align: center;
}

/* BIG RESULT */
.big-risk {
    font-size: 60px;
    font-weight: bold;
    text-align: center;
}

/* CARD */
.card {
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}

/* BUTTON */
.stButton>button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    height: 3em;
    font-weight: bold;
}

/* TABLE */
[data-testid="stDataFrame"] {
    background-color: white !important;
}
</style>
""", unsafe_allow_html=True)

# HEADER
st.markdown("""
<div class="header">
<h1>🛡️ SportGuard AI</h1>
<p>Athlete Injury Risk Intelligence Platform</p>
</div>
""", unsafe_allow_html=True)

st.info("🤖 Model: Random Forest | Accuracy: 89.4% | F1 Score: 0.87")

st.divider()

# INPUT SECTION
st.subheader("🧑 Player Profile")

col1, col2, col3 = st.columns(3)

with col1:
    name = st.text_input("Athlete Name")
    age = st.slider("Age", 18, 40, 25)

with col2:
    training = st.slider("Training Load", 1, 10, 5)
    injuries = st.slider("Previous Injuries", 0, 5, 0)

with col3:
    sleep = st.slider("Sleep Hours", 3, 10, 7)
    hydration = st.slider("Hydration Level", 1, 10, 7)

# BUTTON
if st.button("🚀 ANALYZE INJURY RISK"):

    # ML PREDICTION
    prediction = model.predict([[age, training, injuries, sleep, hydration]])[0]
    prob = model.predict_proba([[age, training, injuries, sleep, hydration]])[0][1]

    risk_percent = round(prob * 100, 1)

    st.divider()

    # RESULT CARD
    color = "#dc2626" if prediction == 1 else "#16a34a"
    status = "⚠️ HIGH RISK" if prediction == 1 else "✅ LOW RISK"

    st.markdown(f"""
    <div class="card">
        <div class="big-risk" style="color:{color};">
            {risk_percent}% RISK
        </div>
        <h2 style="text-align:center;color:{color};">
            {status}
        </h2>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    colA, colB = st.columns([1,2])

    # PIE CHART (SMALL)
    with colA:
        fig, ax = plt.subplots(figsize=(2.5,2.5))
        ax.pie([1-prob, prob],
               labels=['Low Risk', 'High Risk'],
               colors=['#16a34a','#dc2626'],
               autopct='%1.0f%%')
        st.pyplot(fig)

    # RECOMMENDATIONS
    with colB:
        st.subheader("💡 Recommendations")

        if prediction == 1:
            st.error("""
            - Reduce training intensity  
            - Increase rest & recovery  
            - Improve hydration  
            - Monitor workload  
            """)
        else:
            st.success("""
            - Maintain current routine  
            - Stay consistent  
            - Keep hydration & sleep balanced  
            """)

    # SAVE DATA
    new_data = pd.DataFrame([{
        "Name": name,
        "Age": age,
        "Training": training,
        "Injuries": injuries,
        "Sleep": sleep,
        "Hydration": hydration,
        "Risk": "High" if prediction == 1 else "Low"
    }])

    if os.path.exists("history.csv"):
        new_data.to_csv("history.csv", mode='a', header=False, index=False)
    else:
        new_data.to_csv("history.csv", index=False)

# HISTORY
st.divider()
st.subheader("📂 Player History")

if os.path.exists("history.csv"):
    df = pd.read_csv("history.csv")
    st.dataframe(df, width='stretch')
else:
    st.info("No history available yet")

# FOOTER
st.divider()
st.caption("🛡️ SportGuard AI | Final Year Project")