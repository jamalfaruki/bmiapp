import streamlit as st

# Set page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="🏋️", layout="wide")

# Custom CSS for styling
st.markdown("""
<style>
body {
    background-color: #000000;
}
h1 {
    color: #2c3e50;
}
.slider {
    color: #2980b9;
}
.stButton {
    background-color: white;
    color: blue;
}
.stButton:hover {
    background-color: #219653;
}
</style>
""", unsafe_allow_html=True)

st.title("BMI CALCULATOR")

# Option to select unit system
unit = st.selectbox("Select unit system:", ("Metric (cm, kg)", "Imperial (inches, lbs)"))

if unit == "Metric (cm, kg)":
    height = st.slider("Slide to select your height in cm:", 40, 270, 50)
    weight = st.slider("Slide to select your weight in kg:", 40, 300, 40)
    BMI = weight / (height / 100) ** 2
elif unit == "Imperial (inches, lbs)":
    height = st.slider("Slide to select your height in inches:", 40, 100, 60)
    weight = st.slider("Slide to select your weight in lbs:", 80, 600, 150)
    BMI = (weight / (height ** 2)) * 703  # Conversion for imperial units

st.write("Your BMI is:", round(BMI, 2))

# BMI classification and health advice
if BMI <= 18.4:
    st.error("Underweight")
    st.write("Diet Suggestions: Consider high-calorie foods like nuts, avocados, and whole grains.")
    st.write("Exercise: Focus on strength training to build muscle mass.")
elif 18.5 <= BMI <= 24.9:
    st.success("Normal")
    st.write("Diet Suggestions: Maintain a balanced diet rich in fruits, vegetables, and lean proteins.")
    st.write("Exercise: Regular cardio and strength training are recommended.")
elif 25 <= BMI <= 29.9:
    st.warning("Overweight")
    st.write("Diet Suggestions: Reduce sugar and refined carbs; focus on whole foods.")
    st.write("Exercise: Incorporate more cardio and strength training into your routine.")
elif 30 <= BMI <= 34.9:
    st.warning("Obese")
    st.write("Diet Suggestions: Consult a nutritionist for a personalized diet plan.")
    st.write("Exercise: Aim for at least 150 minutes of moderate aerobic activity each week.")
elif 35 <= BMI <= 39.9:
    st.warning("Severely Obese")
    st.write("Diet Suggestions: Focus on portion control and nutrient-dense foods.")
    st.write("Exercise: Consider working with a trainer for safe exercise options.")
elif BMI >= 40:
    st.warning("Morbidly Obese")
    st.write("Diet Suggestions: Seek professional guidance for a comprehensive weight loss plan.")
    st.write("Exercise: Start with low-impact activities and gradually increase intensity.")

# Additional features
st.sidebar.header("Additional Features")
st.sidebar.write("You can explore more about healthy living, including:")
st.sidebar.write("- Nutrition guidelines")
st.sidebar.write("- Exercise routines")
st.sidebar.write("- Weight management tips")

# Option to reset the calculator
if st.button("Reset"):
    st.experimental_rerun()

# Add a footer with additional resources
st.markdown("""
---
### Learn More
- [Nutritional Guidelines](https://www.choosemyplate.gov/)
- [Exercise Routines](https://www.acefitness.org/)
- [Weight Management Tips](https://www.cdc.gov/healthyweight/index.html)
""", unsafe_allow_html=True)
