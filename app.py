import streamlit as st

st.set_page_config(page_title="IMPACT-EVT Risk Calculator", layout="centered")

st.title("🧠 IMPACT-EVT 評分工具")
st.subheader("In-Hospital Mortality Risk After Mechanical Thrombectomy")

# --- Step 1: Baseline Clinical Factors ---
st.header("Step 1: Baseline Clinical Factors")
age = st.radio("Age (年齡)", ["< 70", "70–79", "≥ 80"], horizontal=True)
age_score = {"< 70": 0, "70–79": 1, "≥ 80": 2}[age]

nihss_baseline = st.radio("Baseline NIHSS (原始 NIHSS)", ["≤ 15", "16–20", "> 20"], horizontal=True)
nihss_b_score = {"≤ 15": 0, "16–20": 1, "> 20": 2}[nihss_baseline]

glucose = st.radio("Glucose (血糖, mg/dL)", ["< 130", "≥ 130"], horizontal=True)
glucose_score = {"< 130": 0, "≥ 130": 1}[glucose]

st.divider()

# --- Step 2: Neuroimaging Factors ---
st.header("Step 2: Neuroimaging Factors")
aspects = st.radio("ASPECTS (影像評分)", ["≥ 8", "6–7", "≤ 5"], horizontal=True)
aspects_score = {"≥ 8": 0, "6–7": 1, "≤ 5": 2}[aspects]

collateral = st.radio("Collateral Status (側支循環)", ["Good", "Intermediate", "Poor"], horizontal=True)
collateral_score = {"Good": 0, "Intermediate": 1, "Poor": 2}[collateral]

core_vol = st.radio("Core volume (核心體積, mL)", ["< 30", "30–70", "> 70"], horizontal=True)
core_vol_score = {"< 30": 0, "30–70": 1, "> 70": 2}[core_vol]

st.divider()

# --- Step 3: Procedural & Early Factors ---
st.header("Step 3: Procedural & Early Factors")
recanalization = st.radio("Recanalization mTICI (再通級別)", ["≥ 2b", "< 2b"], horizontal=True)
re_score = {"≥ 2b": 0, "< 2b": 2}[recanalization]

sich = st.radio("siCH (24–48h) (症狀性腦出血)", ["No", "Yes"], horizontal=True)
sich_score = {"No": 0, "Yes": 3}[sich]

nihss_24h = st.radio("NIHSS at 24h (24小時 NIHSS)", ["≤ 10", "11–15", "> 15"], horizontal=True)
nihss_24_score = {"≤ 10": 0, "11–15": 1, "> 15": 2}[nihss_24h]

st.divider()

# --- Risk Stratification Calculation ---
total_score = (age_score + nihss_b_score + glucose_score + 
               aspects_score + collateral_score + core_vol_score + 
               re_score + sich_score + nihss_24_score)

st.header(f"總分 (Total Score): {total_score}")

# 分級邏輯
if 0 <= total_score <= 4:
    risk_level = "Low Risk (低風險)"
    mortality = "< 5%"
    color = "green"
elif 5 <= total_score <= 8:
    risk_level = "Moderate Risk (中風險)"
    mortality = "5–15%"
    color = "orange"
elif 9 <= total_score <= 12:
    risk_level = "High Risk (高風險)"
    mortality = "20–40%"
    color = "#FF4B4B" # Red
else:
    risk_level = "Very High Risk (極高風險)"
    mortality = "> 50%"
    color = "#8B0000" # Dark Red

st.markdown(f"""
<div style="background-color:{color}; padding:20px; border-radius:10px; text-align:center;">
    <h2 style="color:white; margin:0;">{risk_level}</h2>
    <h3 style="color:white; margin:0;">預期住院死亡率: {mortality}</h3>
</div>
""", unsafe_allow_html=True)
