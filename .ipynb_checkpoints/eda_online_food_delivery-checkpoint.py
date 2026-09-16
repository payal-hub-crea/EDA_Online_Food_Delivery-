"""
Exploratory Data Analysis (EDA) - Online Food Delivery Dataset
Internship Task 2

Author: <Your Name>
Description:
    This script performs EDA on the "Online Food Delivery" survey dataset.
    It uses pandas for data handling and matplotlib/seaborn for visualization.
    Outputs (charts) are saved to the 'outputs' folder.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------------------------------------
# 0. Setup
# ---------------------------------------------------------
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (8, 5)

DATA_PATH = "data/online food delivery dataset.csv"
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ---------------------------------------------------------
# 1. Load Data
# ---------------------------------------------------------
df = pd.read_csv(DATA_PATH)

# Drop the unnamed/duplicate column (survey export artifact)
if "Unnamed: 13" in df.columns:
    df = df.drop(columns=["Unnamed: 13"])

# Clean whitespace issues in categorical text (e.g. "Negative ")
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype(str).str.strip()

print("Dataset shape:", df.shape)
print("\nColumn info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())
print("\nFirst 5 rows:")
print(df.head())

# ---------------------------------------------------------
# 2. Summary Statistics
# ---------------------------------------------------------
print("\nNumerical summary:")
print(df.describe())

print("\nCategorical value counts:")
for col in ["Gender", "Marital Status", "Occupation", "Monthly Income",
            "Educational Qualifications", "Customer Type", "Output", "Feedback"]:
    print(f"\n{col}:")
    print(df[col].value_counts())

# ---------------------------------------------------------
# 3. Histograms (distribution of numerical features)
# ---------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.histplot(df["Age"], bins=10, kde=True, ax=axes[0], color="steelblue")
axes[0].set_title("Distribution of Customer Age")
axes[0].set_xlabel("Age")

sns.histplot(df["Family size"], bins=6, kde=True, ax=axes[1], color="darkorange")
axes[1].set_title("Distribution of Family Size")
axes[1].set_xlabel("Family Size")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/01_histograms_age_familysize.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# 4. Bar Charts (categorical features)
# ---------------------------------------------------------
fig, axes = plt.subplots(2, 2, figsize=(13, 10))

sns.countplot(data=df, x="Gender", ax=axes[0, 0], hue="Gender", legend=False, palette="Set2")
axes[0, 0].set_title("Customers by Gender")

sns.countplot(data=df, x="Occupation", ax=axes[0, 1], hue="Occupation", legend=False, palette="Set2")
axes[0, 1].set_title("Customers by Occupation")
axes[0, 1].tick_params(axis="x", rotation=20)

sns.countplot(data=df, x="Monthly Income", ax=axes[1, 0], hue="Monthly Income", legend=False,
              order=df["Monthly Income"].value_counts().index, palette="Set2")
axes[1, 0].set_title("Customers by Monthly Income")
axes[1, 0].tick_params(axis="x", rotation=20)

sns.countplot(data=df, x="Feedback", ax=axes[1, 1], hue="Feedback", legend=False, palette="Set2")
axes[1, 1].set_title("Customer Feedback")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/02_barcharts_categorical.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# 5. Reordering App Usage (Output) vs Feedback
# ---------------------------------------------------------
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Output", hue="Feedback", palette="coolwarm")
plt.title("Will Customer Reorder? (split by Feedback)")
plt.xlabel("Reorders Again (Output)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/03_output_vs_feedback.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# 6. Scatter Plot - Age vs Family Size (colored by Feedback)
# ---------------------------------------------------------
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Age", y="Family size", hue="Feedback", alpha=0.7, palette="Set1")
plt.title("Age vs Family Size (by Feedback)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/04_scatter_age_familysize.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# 7. Correlation Heatmap (numerical columns)
# ---------------------------------------------------------
plt.figure(figsize=(6, 5))
num_cols = ["Age", "Family size", "latitude", "longitude", "Pin code"]
corr = df[num_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap (Numerical Features)")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/05_correlation_heatmap.png", dpi=150)
plt.close()

# ---------------------------------------------------------
# 8. Boxplot - Detect Outliers in Age & Family Size
# ---------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(10, 5))
sns.boxplot(y=df["Age"], ax=axes[0], color="skyblue")
axes[0].set_title("Boxplot - Age")
sns.boxplot(y=df["Family size"], ax=axes[1], color="lightgreen")
axes[1].set_title("Boxplot - Family Size")
plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/06_boxplots_outliers.png", dpi=150)
plt.close()

print(f"\nAll charts saved to the '{OUTPUT_DIR}/' folder.")
print("EDA complete.")
