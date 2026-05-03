# 🏗️ Advanced Quote Anomaly Detection System

---

## 1. Context, User, and Problem

### 📌 Context

In the U.S. construction industry, cost evaluation is a critical step in project planning and procurement. However, current workflows rely heavily on manual review and personal experience, which can lead to inconsistencies and missed risks.

---

### 👤 Target Users

- Construction Cost Engineers  
- Quantity Surveyors  
- Project Managers  

---

### ❗ Problem

Users need to quickly determine whether a quotation is:

- overpriced  
- underpriced  
- or within a reasonable market range  

But today:

- Analysis is slow  
- Results are not standardized  
- Hidden risks (e.g., low-quality materials, unrealistic labor pricing) are often overlooked  

---

## 2. Solution and Design

### 💡 What I Built

A Streamlit-based GenAI application that analyzes construction quotation data and generates:

- Price evaluation  
- Abnormal item detection  
- Risk assessment  
- Actionable recommendations  
- Final score (0–100)  

---

### ⚙️ How It Works

1. User inputs quotation data  
2. Data is sent to a large language model (Gemini)  
3. The model returns structured JSON  
4. The app parses and displays a dashboard  

---

### 🧠 Key Design Choices

- Structured prompting (strict JSON output)  
- Fallback logic (no empty sections)  
- Dashboard UI (clear and readable)  

---

## 3. Evaluation and Results

### 🔹 Baseline (Without GenAI)

Traditional workflow:

- Manual evaluation  
- Excel-based comparison  
- Experience-driven decisions  

Limitations:

- Slow  
- Inconsistent  
- Hard to scale  

---

### 🔹 GenAI System Testing

Tested with multiple scenarios:

#### Case 1: Normal Pricing
All items within benchmark → LOW risk  

#### Case 2: High Pricing
Materials exceed benchmark → HIGH risk  

#### Case 3: Low Pricing
Unusually low prices → hidden risks  

#### Case 4: Mixed Case
Combination of high and low → realistic scenario  

---

### 📊 Comparison

| Aspect        | Baseline | GenAI System |
|--------------|--------|-------------|
| Speed        | Slow   | Fast        |
| Consistency  | Low    | High        |
| Structure    | Weak   | Strong      |
| Insight      | Limited| Rich        |

---

### 📌 Findings

- AI improves speed and consistency  
- Structured output enhances usability  
- Both high-cost and low-cost risks can be detected  

---

### ⚠️ Limitations

- Depends on prompt quality  
- No real-time market data  
- Cannot replace human judgment  

---

## 4. Artifact Snapshot

The app includes:

- Input panel  
- Dashboard UI  
- Price evaluation section  
- Risk assessment  
- Recommendations  
- Final score  

---

### ✍️ Example Input
Rebar: 1300 USD/ton
Concrete: 100 USD/m³
Labor: 150 USD/day
Formwork: 10 USD/m²
Steel Plate: 1700 USD/ton


---

## 5. Setup and Usage

### 📦 Install dependencies
pip install streamlit google-generativeai


---

### ▶️ Run the app
streamlit run app.py


---

### ✍️ Sample Test Data
Rebar: 900 USD/ton
Concrete: 150 USD/m³
Labor: 320 USD/day
Formwork: 25 USD/m²
Steel Plate: 1100 USD/ton


---

## 6. Conclusion

This project demonstrates how GenAI can:

- Standardize cost evaluation  
- Improve efficiency  
- Identify hidden risks  

👉 The system is designed to assist human decision-making.

---

## ✅ Submission Notes

- App runs locally  
- Includes test cases  
- Structured README provided  
- No API keys included  