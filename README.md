# 🧭 HR Analytics Dashboard: Employee Retention & Engagement Insights

### 🎯 Objective  
Analyze a company's HR dataset to identify factors affecting **employee retention, engagement, and performance**.  
Build actionable insights and dashboards to help management improve workforce planning and reduce attrition.

---

## 📊 Project Overview  

This project demonstrates **end-to-end data analytics skills** — from **data preprocessing** to **Power BI dashboarding** — aligned with PwC’s “Data, Analytics & AI” internship requirements.

It combines **Python, and Power BI** to clean, analyze, model, and visualize HR data to uncover **key drivers of attrition and engagement**.

---

## 🧠 Key Business Questions

1️⃣ What are the main factors driving employee attrition?  
2️⃣ Which departments or roles have the highest turnover?  
3️⃣ How does job satisfaction and work-life balance influence retention?  
4️⃣ Can we predict which employees are at risk of leaving?  
5️⃣ What actionable steps can management take to improve engagement?

---

## 🧩 Data Sources  

| Dataset | Description |
|----------|--------------|
| Employee Demographics | Age, Gender, Department, Tenure |
| HR Metrics | Promotions, Performance, Training Hours |
| Engagement Survey | Satisfaction, Work-Life Balance, Inclusion |
| Attendance Records | Leave, Overtime, Absenteeism |
| Optional | Payroll/Compensation details |

---

## 🧹 1️⃣ Data Cleaning & Preprocessing (Python )

**Steps:**
- Handle missing values (Median for numeric, Mode for categorical)
- Encode categorical variables (Label Encoding / One-Hot Encoding)
- Create new features:
  - `YearsSinceLastPromotion = Tenure - YearsInCurrentRole`
  - `TrainingPerYear = TrainingHours / Tenure`
- Normalize numerical columns (StandardScaler)
- Check correlation matrix to remove multicollinearity

📘 *Libraries used:* `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`

---

## 🔍 2️⃣ Exploratory Data Analysis (EDA)

**Performed using Python & SQL to find:**
- Attrition trends by department, age, and gender  
- Relationship between income and job level  
- Impact of overtime and work-life balance  
- Correlation heatmaps and boxplots  

**Key Insights:**
- Attrition higher in **Sales & HR** departments  
- **Overtime** and **low satisfaction** strongly correlate with leaving  
- Mid-level employees (2–5 years tenure) most likely to quit  

---

## 🤖 3️⃣ Predictive Modeling (Python)

**Goal:** Predict which employees are at high risk of leaving.

**Models Used:**
- Logistic Regression  
- Decision Tree Classifier  
- Random Forest (best performer)

**Metrics Evaluated:**
- Accuracy  
- Precision, Recall, F1-score  
- ROC-AUC Curve  

**Feature Importance Results:**
- Overtime  
- Job Satisfaction  
- Monthly Income  
- Years at Company  
- Work-Life Balance  

---

## 📈 4️⃣ Dashboard & Visualization (Power BI)

### **Dashboard Pages**
1️⃣ **Overview Dashboard**
   - KPIs: Total Employees, Attrition Count, Attrition Rate, Avg Age, Income, Tenure  
   - Visuals: Donut (Attrition), Clustered Column (Department), Gauge (Satisfaction)

2️⃣ **Attrition Analysis**
   - Attrition by Gender, Department, Travel Type  
   - Heatmap: Attrition vs Age Group & Job Level  

3️⃣ **Engagement & Work-Life**
   - Avg Job Satisfaction by Department  
   - Work-Life Balance vs Tenure  
   - Training Hours vs Performance Rating  

4️⃣ **Retention Risk & Predictive Insights**
   - TreeMap: Attrition by Age & Marital Status  
   - Conditional Table: Highlight high-risk employees  

---

## ⚙️ DAX Measures Used

```DAX
Attrition Rate (%) = 
DIVIDE(
    CALCULATE(
        COUNTROWS('WA_Fn-UseC_-HR-Employee-Attrition'),
        TRIM(UPPER('WA_Fn-UseC_-HR-Employee-Attrition'[Attrition])) = "YES"
    ),
    COUNTROWS('WA_Fn-UseC_-HR-Employee-Attrition')
) * 100
```

## 🧾 5️⃣ Business Recommendations

- ✅ Implement targeted retention programs in high-risk departments
- ✅ Create promotion and recognition programs for early-tenure employees
- ✅ Offer flexible work arrangements to improve work-life balance
- ✅ Conduct diversity & inclusion workshops in low-scoring teams
- ✅ Optimize training programs to increase engagement and performance

## 6️⃣ Management Report Summary

Overall Findings:

- Attrition driven by overtime, low satisfaction, and lack of career growth
- Sales & HR have highest turnover
- Training and inclusion improve retention and performance

Business Impact:
- Potential 20–25% attrition reduction with data-driven HR policies
- 15–20% improvement in satisfaction and engagement scores
- Stronger diversity outcomes through equitable initiatives

## Deliverables

- 📘 HR_Analytics.ipynb – Python code for data analysis and modeling
- 📊 HR_Analytics_Dashboard.pbix – Power BI dashboard file
- 📄 HR_Report_Summary.pdf – Management summary report
- 🧮 HR_Dataset.csv – Simulated dataset used for analysis

## 🧑‍💼 Author

Rithika Ramalingam
🎓 Data Analyst | Python | SQL | Power BI | Machine Learning
📍 India

📧 [rithikaramalingam37@gmail]

🌐 [https://www.linkedin.com/in/rithika-ramalingam-r-02714b244/]
