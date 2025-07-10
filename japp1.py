import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import time

# Set page config
st.set_page_config(page_title="Animated BMI Calculator", page_icon="⚖️", layout="centered")

# Modern CSS & animations
st.markdown("""
<style>
@keyframes pop { 0% {transform: scale(0.95);} 50% {transform: scale(1.05);} 100% {transform: scale(1);} }
@keyframes bounce { 0%, 100% {transform: translateY(0);} 50% {transform: translateY(-8px);} }
@keyframes fadeIn { from {opacity: 0;} to {opacity: 1;} }

.result-box {
    font-size: 28px;
    font-weight: bold;
    color: white;
    padding: 18px;
    border-radius: 16px;
    text-align: center;
    animation: pop 0.8s ease-in-out;
    margin-top: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.15);
}

.badge {
    display: inline-block;
    padding: 8px 16px;
    font-size: 16px;
    font-weight: 600;
    border-radius: 25px;
    background: #111;
    color: #fff;
    animation: bounce 1.2s infinite;
}

.progress-bar {
    background: #ddd;
    border-radius: 8px;
    overflow: hidden;
    margin-top: 15px;
}
.progress-fill {
    height: 24px;
    border-radius: 8px;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    text-align: center;
    color: white;
    font-weight: bold;
    animation: fadeIn 1s ease-in-out;
}

.stButton>button {
    background: linear-gradient(to right, #6a11cb, #2575fc);
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 10px 20px;
    transition: all 0.3s ease-in-out;
}
.stButton>button:hover {
    transform: scale(1.05);
    background: linear-gradient(to right, #5f0fdd, #1a62e6);
}
</style>
""", unsafe_allow_html=True)

st.title("⚖️ BMI CALCULATOR (Animated Edition)")

# Show time/date
st.caption(f"🕒 Current Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Input type
col1, col2 = st.columns(2)
input_mode = col1.radio("Choose Input Type:", ["Slider Input", "Manual Entry"], horizontal=True)
unit = col2.selectbox("Select Unit System:", ["Metric (cm, kg)", "Imperial (in, lbs)"])

# BMI input
if unit == "Metric (cm, kg)":
    height = col1.slider("Height (cm):", 100, 250, 170) if input_mode == "Slider Input" else col1.number_input("Height (cm):", 1.0, 300.0, 170.0)
    weight = col2.slider("Weight (kg):", 30, 200, 70) if input_mode == "Slider Input" else col2.number_input("Weight (kg):", 1.0, 300.0, 70.0)
    bmi = weight / (height / 100) ** 2
else:
    height = col1.slider("Height (in):", 40, 100, 67) if input_mode == "Slider Input" else col1.number_input("Height (in):", 1.0, 120.0, 67.0)
    weight = col2.slider("Weight (lbs):", 80, 400, 150) if input_mode == "Slider Input" else col2.number_input("Weight (lbs):", 1.0, 600.0, 150.0)
    bmi = (weight / (height ** 2)) * 703

bmi_rounded = round(bmi, 2)

# Feedback function
def get_feedback(bmi):
    if bmi <= 18.4:
        return "Underweight", "🔴", "#f39c12"
    elif 18.5 <= bmi <= 24.9:
        return "Normal", "✅", "#2ecc71"
    elif 25 <= bmi <= 29.9:
        return "Overweight", "🟠", "#f1c40f"
    elif 30 <= bmi <= 34.9:
        return "Obese", "⚠️", "#e67e22"
    elif 35 <= bmi <= 39.9:
        return "Severely Obese", "⚠️", "#e74c3c"
    else:
        return "Morbidly Obese", "🚨", "#c0392b"

category, emoji, color = get_feedback(bmi)

# Display result with animation
st.markdown(f"""
<div class="result-box" style="background-color: {color};">
    {emoji} Your BMI is <b>{bmi_rounded}</b> — <span class="badge">{category}</span>
</div>
""", unsafe_allow_html=True)

# Animated progress bar
st.markdown(f"""
<div class="progress-bar">
  <div class="progress-fill" style="width:{min(bmi,60)/60*100:.1f}%;">{bmi_rounded}</div>
</div>
""", unsafe_allow_html=True)

# Save BMI to session history
if "bmi_history" not in st.session_state:
    st.session_state.bmi_history = []

if st.button("📌 Save to History"):
    st.session_state.bmi_history.append((datetime.now().strftime("%Y-%m-%d %H:%M"), bmi_rounded, category))
    st.success("BMI saved!")

# Show mini bar chart of history
if st.session_state.bmi_history:
    st.subheader("📈 Your BMI History")
    df = pd.DataFrame(st.session_state.bmi_history, columns=["Time", "BMI", "Category"])
    st.dataframe(df.tail(5), use_container_width=True)

    with st.expander("📊 Show BMI Trend"):
        st.bar_chart(df.set_index("Time")["BMI"])

    if st.download_button("📥 Download as CSV", df.to_csv(index=False).encode(), "bmi_history.csv", "text/csv"):
        st.success("✅ File ready to download!")

# Goal suggestion
st.subheader("🎯 Set Your Goal")
goal = st.selectbox("Do you want to:", ["Maintain weight", "Lose weight", "Gain weight"])
if goal == "Lose weight":
    st.info("⚠️ Try reducing 500 calories/day for steady loss. Focus on cardio and light meals.")
elif goal == "Gain weight":
    st.warning("🍔 Add 300-500 calories/day. Include protein shakes, nuts, and strength training.")
else:
    st.success("💪 Great! Maintain your daily calories and regular activity.")

# Footer
st.markdown("---")
st.caption("🧠 Built with ❤️ using Streamlit| Zamal's BMI Tool 2025")


