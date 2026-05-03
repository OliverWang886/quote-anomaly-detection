import streamlit as st
from google import genai
import json

# API
client = genai.Client(api_key="AIzaSyA442NR8CmKfycH_2_EcXArgmM97UGLqB8")

st.set_page_config(page_title="AI Cost Audit Tool", layout="wide")

# ================= UI =================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #fff7e6, #fff1f0);
}
.banner {
    background-image: url("https://images.unsplash.com/photo-1503387762-592deb58ef4e");
    background-size: cover;
    padding: 60px;
    border-radius: 15px;
    color: white;
    text-align: center;
}
.card {
    background:white;
    padding:14px;
    border-radius:10px;
    margin-bottom:10px;
    box-shadow:0 2px 6px rgba(0,0,0,0.08);
}
.section {
    background:#fafafa;
    padding:20px;
    border-radius:12px;
    margin-top:15px;
}
</style>
""", unsafe_allow_html=True)

# Banner
st.markdown("""
<div class="banner">
<h1>🏗️ Advanced Quote Anomaly Detection System</h1>
<p>AI-powered cost benchmarking for U.S. construction projects</p>
</div>
""", unsafe_allow_html=True)

# 输入
st.subheader("📥 Input Data (USD Market)")

user_input = st.text_area(
    "Enter quotation data",
    height=150,
    placeholder="""Rebar: 1300 USD/ton
Concrete: 100 USD/m³
Labor: 150 USD/day
Formwork: 10 USD/m²
Steel Plate: 1700 USD/ton"""
)

# ================= 分析 =================
if st.button("🚀 Analyze"):

    if user_input.strip() == "":
        st.warning("Please enter data")
    else:
        try:
            with st.spinner("Analyzing..."):

                prompt = f"""
You are a senior U.S. construction cost expert.

Return STRICT JSON ONLY. No text outside JSON.

JSON FORMAT:

{{
  "price_evaluation": [
    {{
      "item": "",
      "price": "",
      "benchmark": "",
      "classification": "",
      "analysis": ""
    }}
  ],
  "abnormal_items": [
    {{
      "item": "",
      "issue": ""
    }}
  ],
  "risk_assessment": {{
    "level": "",
    "analysis": ""
  }},
  "recommendations": [
    {{
      "title": "",
      "details": ["", "", ""]
    }}
  ],
  "final_score": 0,
  "final_summary": ""
}}

Rules:
- Must fill ALL fields
- No empty arrays
- Provide detailed explanations
- Recommendations must include sub-points

Data:
{user_input}
"""

                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )

                raw = response.text

                # 清洗
                raw = raw.replace("```json", "").replace("```", "")

                data = json.loads(raw)

            # ================= Dashboard =================
            score = data["final_score"]
            risk = data["risk_assessment"]["level"]

            if risk.lower() == "high":
                color = "#ff4d4f"
            elif risk.lower() == "medium":
                color = "#faad14"
            else:
                color = "#52c41a"

            st.markdown("## 📊 Project Dashboard")

            col1, col2 = st.columns([3,1])

            with col1:
                st.markdown(f"""
                <div class="section" style="border-left:6px solid {color}">
                <h3>📌 Executive Summary</h3>
                Risk Level: <b style="color:{color}">{risk}</b>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div style="background:#ff7a45;color:white;padding:25px;border-radius:12px;text-align:center">
                <h1>{score}</h1>
                <p>Score / 100</p>
                </div>
                """, unsafe_allow_html=True)

            # ================= Price Evaluation =================
            st.markdown("### 📊 Price Evaluation")

            colors = ["#ffccc7","#d9f7be","#bae7ff","#fff1b8","#efdbff"]

            for i, item in enumerate(data["price_evaluation"]):
                st.markdown(f"""
                <div class="card" style="border-left:5px solid {colors[i%5]}">
                <b>{item['item']}</b><br>
                Price: {item['price']}<br>
                Benchmark: {item['benchmark']}<br>
                Classification: {item['classification']}<br>
                {item['analysis']}
                </div>
                """, unsafe_allow_html=True)

            # ================= Abnormal =================
            st.markdown("### ⚠️ Abnormal Items")

            for item in data["abnormal_items"]:
                st.markdown(f"""
                <div class="card" style="border-left:5px solid red">
                <b>{item['item']}</b>: {item['issue']}
                </div>
                """, unsafe_allow_html=True)

            # ================= Risk =================
            st.markdown("### 📉 Risk Assessment")

            st.markdown(f"""
            <div class="section" style="border-left:6px solid {color}">
            {data['risk_assessment']['analysis']}
            </div>
            """, unsafe_allow_html=True)

            # ================= Recommendations =================
            st.markdown("### 💡 Recommendations")

            for rec in data["recommendations"]:
                st.markdown(f"""
                <div class="card" style="border-left:5px solid green">
                <b>{rec['title']}</b>
                </div>
                """, unsafe_allow_html=True)

                for sub in rec["details"]:
                    st.markdown(f"""
                    <div style="margin-left:20px;color:#555">
                    • {sub}
                    </div>
                    """, unsafe_allow_html=True)

            # ================= Final =================
            st.markdown("### 🏁 Final Evaluation")

            st.markdown(f"""
            <div class="section" style="border-left:6px solid #1890ff">
            <b>Final Score:</b> {score} / 100<br><br>
            <b>Risk Level:</b> {risk}<br><br>
            {data["final_summary"]}
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error: {e}")