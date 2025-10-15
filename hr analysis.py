# ===============================
# HR Analytics: Data Preprocessing (Final Fixed Version)
# ===============================

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

# 1️⃣ Load Dataset
df = pd.read_csv(r"C:\Users\rithi\OneDrive\Documents\fielsss\HR Report\WA_Fn-UseC_-HR-Employee-Attrition.csv")
print("✅ Dataset loaded successfully.")
print(f"Shape: {df.shape}")
print("Columns:", list(df.columns))

# -------------------------------
# 2️⃣ Handle Missing Values
# -------------------------------

# Fill numeric columns with median
num_cols = df.select_dtypes(include='number').columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Fill categorical columns with mode
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("✅ Missing values handled.")

# -------------------------------
# 3️⃣ Encode Categorical Variables
# -------------------------------

# Label Encoding for binary columns (Yes/No etc.)
binary_cols = [col for col in cat_cols if df[col].nunique() == 2]
le = LabelEncoder()
for col in binary_cols:
    df[col] = le.fit_transform(df[col])

# One-Hot Encoding for multi-category columns
multi_cat_cols = [col for col in cat_cols if df[col].nunique() > 2]
df = pd.get_dummies(df, columns=multi_cat_cols, drop_first=True)

print("✅ Encoding complete.")

# -------------------------------
# 4️⃣ Feature Engineering
# -------------------------------

# Derived columns based on HR dataset
if 'YearsAtCompany' in df.columns and 'YearsInCurrentRole' in df.columns:
    df['YearsDiff_Role'] = df['YearsAtCompany'] - df['YearsInCurrentRole']

if 'TrainingTimesLastYear' in df.columns and 'YearsAtCompany' in df.columns:
    df['TrainingPerYear'] = df['TrainingTimesLastYear'] / (df['YearsAtCompany'] + 1)  # avoid divide-by-zero

if 'Age' in df.columns:
    df['AgeGroup'] = pd.cut(df['Age'], bins=[18,30,40,50,60], labels=['18-30','30-40','40-50','50+'])

print("✅ Feature engineering complete.")

# -------------------------------
# 5️⃣ Normalization / Scaling
# -------------------------------

scaler = StandardScaler()
num_features = ['Age', 'YearsAtCompany', 'MonthlyIncome', 
                'YearsSinceLastPromotion', 'TrainingTimesLastYear']

# Ensure only existing columns are scaled
num_features = [col for col in num_features if col in df.columns]
df[num_features] = scaler.fit_transform(df[num_features])

print("✅ Scaling complete.")

# -------------------------------
# 6️⃣ Correlation Heatmap (Numeric Only)
# -------------------------------

numeric_df = df.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr()

plt.figure(figsize=(12,8))
sns.heatmap(corr_matrix, annot=False, cmap='coolwarm')
plt.title("Feature Correlation Matrix (Numeric Features Only)")
plt.show()

print("✅ Correlation matrix displayed.")

# -------------------------------
# 7️⃣ Save Cleaned Dataset
# -------------------------------

output_path = r"C:\Users\rithi\OneDrive\Documents\fielsss\HR Report\WA_Fn-UseC_-HR-Employee-Attrition_CLEANED.csv"
df.to_csv(output_path, index=False)
print(f"✅ Data preprocessing complete. Cleaned dataset saved at:\n{output_path}")
