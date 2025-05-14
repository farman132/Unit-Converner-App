import streamlit as st

# ---------- Custom Style ----------
st.set_page_config(page_title="🌈 Stylish Unit Converter", page_icon="🔁", layout="centered")

# ---------- Title ----------
st.markdown("""
    <h1 style='text-align: center; color: #4B8BBE;'>🔁 Stylish Unit Converter</h1>
    <p style='text-align: center; color: gray;'>Convert 🔄 Length, Weight, Temperature, Area, Volume, and Speed with a beautiful UI 🚀</p>
""", unsafe_allow_html=True)

# ---------- Conversion Functions ----------
def convert_length(value, from_unit, to_unit):
    units = {"Meter": 1, "Kilometer": 1000, "Mile": 1609.34, "Foot": 0.3048}
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {"Kilogram": 1, "Gram": 0.001, "Pound": 0.453592}
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def convert_area(value, from_unit, to_unit):
    units = {"Sq. Meter": 1, "Sq. Kilometer": 1e6, "Acre": 4046.86}
    return value * units[from_unit] / units[to_unit]

def convert_volume(value, from_unit, to_unit):
    units = {"Liter": 1, "Milliliter": 0.001, "Cubic Meter": 1000}
    return value * units[from_unit] / units[to_unit]

def convert_speed(value, from_unit, to_unit):
    units = {"Km/h": 1, "m/s": 3.6, "Miles/h": 1.60934}
    return value * units[from_unit] / units[to_unit]

# ---------- Main UI ----------
st.markdown("### 🧭 Choose What You Want to Convert")
conversion_type = st.selectbox("🧪 Conversion Type", [
    "Length", "Weight", "Temperature", "Area", "Volume", "Speed"
])

st.markdown("### 🔢 Enter the Value to Convert")
value = st.number_input("Value", min_value=0.0, format="%.2f")

unit_options = {
    "Length": ["Meter", "Kilometer", "Mile", "Foot"],
    "Weight": ["Kilogram", "Gram", "Pound"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"],
    "Area": ["Sq. Meter", "Sq. Kilometer", "Acre"],
    "Volume": ["Liter", "Milliliter", "Cubic Meter"],
    "Speed": ["Km/h", "m/s", "Miles/h"]
}

col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From Unit", unit_options[conversion_type])
with col2:
    to_unit = st.selectbox("To Unit", unit_options[conversion_type])

# ---------- Conversion Logic ----------
if value:
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == "Area":
        result = convert_area(value, from_unit, to_unit)
    elif conversion_type == "Volume":
        result = convert_volume(value, from_unit, to_unit)
    elif conversion_type == "Speed":
        result = convert_speed(value, from_unit, to_unit)

    st.markdown("---")
    st.markdown(f"<h2 style='color: green;'>✅ Result: {result:.2f} {to_unit}</h2>", unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 14px;'>✨ Created with 💙 using <strong>Python</strong> and <strong>Streamlit</strong><br><br>👨‍💻 Developed by <strong>Muhammad Farman</strong></p>", unsafe_allow_html=True)





