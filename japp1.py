import streamlit as st
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="BMI Calculator", page_icon="🏋️", layout="centered")

# Inject custom CSS and animation
st.markdown("""
<style>
@keyframes pop {
  0%   {transform: scale(0.95);}
  50%  {transform: scale(1.05);}
  100% {transform: scale(1);}
}
.result-box {
    font-size: 26px;
    font-weight: bold;
    color: white;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    animation: pop 0.8s ease-in-out;
    margin-top: 20px;
}
.stButton>button {
    background-color: #0066cc;
    color: white;
    border-radius: 10px;
    padding: 0.5em 1.5em;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #004080;
}
</style>
""", unsafe_allow_html=True)

st.title("🏋️ BMI CALCULATOR")

# Input method and units
col1, col2 = st.columns(2)
input_mode = col1.radio("Input Method:", ["Slider Input", "Manual Entry"], horizontal=True)
unit = col2.selectbox("Unit System:", ("Metric (cm, kg)", "Imperial (inches, lbs)"))

# Get user input
if unit == "Metric (cm, kg)":
    if input_mode == "Slider Input":
        height = col1.slider("Height (cm):", 100, 250, 170)
        weight = col2.slider("Weight (kg):", 30, 200, 70)
    else:
        height = col1.number_input("Height (cm):", min_value=1.0, max_value=300.0, value=170.0)
        weight = col2.number_input("Weight (kg):", min_value=1.0, max_value=300.0, value=70.0)
    bmi = weight / (height / 100) ** 2
else:
    if input_mode == "Slider Input":
        height = col1.slider("Height (in):", 40, 100, 67)
        weight = col2.slider("Weight (lbs):", 80, 400, 150)
    else:
        height = col1.number_input("Height (in):", min_value=1.0, max_value=120.0, value=67.0)
        weight = col2.number_input("Weight (lbs):", min_value=1.0, max_value=600.0, value=150.0)
    bmi = (weight / (height ** 2)) * 703

bmi_rounded = round(bmi, 2)

# AI-based BMI feedback and diet suggestions
def get_bmi_feedback(bmi):
    if bmi <= 18.4:
        return (
            "Underweight", "🔴", "#f39c12",
            "Gain weight with calorie-dense foods.",
            {
                "Breakfast": "Peanut butter toast, banana smoothie with whole milk.",
                "Lunch": "Rice, chicken curry, boiled eggs, mixed salad with olive oil.",
                "Dinner": "Paneer or tofu with brown rice, nuts, and avocado.",
                "Tip": "Include snacks like trail mix, protein bars, and smoothies."
            }
        )
    elif 18.5 <= bmi <= 24.9:
        return (
            "Normal", "✅", "#2ecc71",
            "Maintain a healthy lifestyle.",
            {
                "Breakfast": "Oatmeal with fruits, Greek yogurt, herbal tea.",
                "Lunch": "Grilled chicken or tofu, brown rice, sautéed veggies.",
                "Dinner": "Lentil soup, multigrain bread, green salad.",
                "Tip": "Stay hydrated and stick to portion-controlled meals."
            }
        )
    elif 25 <= bmi <= 29.9:
        return (
            "Overweight", "🟠", "#f1c40f",
            "Exercise and eat whole foods.",
            {
                "Breakfast": "Boiled eggs, apple slices, black coffee/green tea.",
                "Lunch": "Grilled fish or dal, steamed vegetables, quinoa.",
                "Dinner": "Vegetable soup, chapati, cucumber salad.",
                "Tip": "Avoid sugar drinks, fried foods, and try intermittent fasting."
            }
        )
    elif 30 <= bmi <= 34.9:
        return (
            "Obese", "⚠️", "#e67e22",
            "Consult a doctor or nutritionist.",
            {
                "Breakfast": "Low-fat milk, oats, blueberries.",
                "Lunch": "Grilled chicken/fish, salad with no dressing, dal.",
                "Dinner": "Clear soup, green vegetables, light roti.",
                "Tip": "Use a food journal, avoid late-night eating."
            }
        )
    elif 35 <= bmi <= 39.9:
        return (
            "Severely Obese", "⚠️", "#e74c3c",
            "Focus on portion control.",
            {
                "Breakfast": "1 egg white omelet, green tea, slice of apple.",
                "Lunch": "Steamed vegetables, dal, 1 small roti.",
                "Dinner": "Soup, small portion of salad with tofu.",
                "Tip": "Avoid carbs at night, walk 30 mins after meals."
            }
        )
    else:
        return (
            "Morbidly Obese", "🚨", "#c0392b",
            "Seek urgent medical attention.",
            {
                "Breakfast": "Only black coffee/green tea, a handful of soaked almonds.",
                "Lunch": "Boiled vegetables, low-carb soup, small salad.",
                "Dinner": "Steamed spinach, lentils, and herbal tea.",
                "Tip": "Speak to a licensed dietician immediately."
            }
        )

category, emoji, color, advice, diet_plan = get_bmi_feedback(bmi)

# Display BMI result
st.markdown(f"""
<div class="result-box" style="background-color: {color};">
    {emoji} Your BMI is <b>{bmi_rounded}</b> — {category}
</div>
""", unsafe_allow_html=True)

st.write(f"💡 **Advice:** {advice}")
st.metric("BMI Value", bmi_rounded)

# 🍽️ Diet Suggestions
st.subheader("🍽️ AI-Based Diet Suggestions")
st.write(f"📌 Based on your BMI (**{category}**), here's a recommended daily meal plan:")
with st.expander("📋 View Meal Plan"):
    st.markdown(f"""
    **🥣 Breakfast:** {diet_plan['Breakfast']}  
    **🍱 Lunch:** {diet_plan['Lunch']}  
    **🌙 Dinner:** {diet_plan['Dinner']}  
    ---
    **🧠 Tip:** *{diet_plan['Tip']}*
    """)

# Gauge Chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=bmi_rounded,
    title={'text': "BMI Gauge"},
    gauge={
        'axis': {'range': [0, 60]},
        'bar': {'color': color},
        'steps': [
            {'range': [0, 18.5], 'color': "#ffeaa7"},
            {'range': [18.5, 25], 'color': "#55efc4"},
            {'range': [25, 30], 'color': "#fab1a0"},
            {'range': [30, 40], 'color': "#ff7675"},
            {'range': [40, 60], 'color': "#d63031"},
        ]
    }
))
st.plotly_chart(fig)

# BMI History using session_state
if "bmi_history" not in st.session_state:
    st.session_state.bmi_history = []

if st.button("📌 Save to History"):
    st.session_state.bmi_history.append((bmi_rounded, category))
    st.success("BMI saved to history!")

# Show history
if st.session_state.bmi_history:
    st.subheader("📜 Your BMI History")
    for i, (val, cat) in enumerate(st.session_state.bmi_history[::-1], 1):
        st.write(f"{i}. **{val}** — *{cat}*")

# Sidebar Resources
st.sidebar.header("📚 Learn More")
st.sidebar.markdown("""
- [ChooseMyPlate.gov](https://www.choosemyplate.gov/)
- [ACE Fitness](https://www.acefitness.org/)
- [CDC: Healthy Weight](https://www.cdc.gov/healthyweight/)
""")

# Reset option
if st.sidebar.button("🔄 Reset All"):
    st.session_state.bmi_history.clear()
    st.rerun()

# Footer
st.markdown("---")
st.caption("⚙️ Built with ❤️ using Streamlit | Zamal's BMI Tool 2025")

