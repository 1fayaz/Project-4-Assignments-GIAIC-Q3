# Project 8: BMI Check – Health Score Calculator (Streamlit App)

import streamlit as st  # type: ignore

st.markdown("""
    <style>
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-weight: bold;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #155c8c;
            transition: 0.3s ease-in-out;
        }
        .result-box {
            font-size: 24px;
            font-weight: 600;
            padding: 12px;
            text-align: center;
            border-radius: 10px;
            margin-top: 15px;
        }
        .lean { background-color: #ffd700; }
        .healthy { background-color: #2ecc71; color: white; }
        .heavy { background-color: #ffa500; }
        .critical { background-color: #e74c3c; color: white; }
    </style>
""", unsafe_allow_html=True)

st.title("💪 FitCheck – Your Health Score")
st.write("Fill in the info below to calculate your health status based on your BMI!")

user_height = st.number_input("📏 Height (in meters):", min_value=0.1, format="%.2f")
user_weight = st.number_input("⚖️ Weight (in kilograms):", min_value=0.1, format="%.2f")

if st.button("📊 Show My Score"):
    if user_height > 0 and user_weight > 0:
        score = user_weight / (user_height ** 2)
        st.success(f"📈 Your Health Score (BMI) is: {score:.2f}")
        st.progress(min(score / 40, 1.0))

        if score < 18.5:
            status = "Leaner Side 🍃"
            style = "lean"
        elif 18.5 <= score < 25:
            status = "Balanced & Healthy ✅"
            style = "healthy"
            st.balloons()
        elif 25 <= score < 30:
            status = "Getting Heavier ⚠️"
            style = "heavy"
        else:
            status = "Critical Zone ❗"
            style = "critical"

        st.markdown(f'<div class="result-box {style}">{status}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Oops! You need to fill both height and weight properly.")

# Signature
st.markdown("🎮 Created by cool coder = ME 😎")
