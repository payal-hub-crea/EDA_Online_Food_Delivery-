# Exploratory Data Analysis (EDA) – Online Food Delivery Dataset

**Internship Task 2: Exploratory Data Analysis**

This project performs EDA on an Online Food Delivery survey dataset using **pandas** for data handling and **matplotlib / seaborn** for visualization.

---

## 📁 Project Structure

```
├── data/
│   └── online food delivery dataset.csv   # raw dataset
├── outputs/
│   ├── 01_histograms_age_familysize.png
│   ├── 02_barcharts_categorical.png
│   ├── 03_output_vs_feedback.png
│   ├── 04_scatter_age_familysize.png
│   ├── 05_correlation_heatmap.png
│   └── 06_boxplots_outliers.png
├── eda_online_food_delivery.py             # main EDA script
├── requirements.txt
└── README.md
```

## 📊 About the Dataset

The dataset contains **388 survey responses** from customers about their online food ordering habits. It has 13 columns after cleaning, covering demographics (Age, Gender, Marital Status, Occupation, Monthly Income, Education, Family size), location (latitude, longitude, Pin code), customer type, whether they would reorder (`Output`), and their feedback (`Feedback`).

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python eda_online_food_delivery.py
```

All charts will be generated in the `outputs/` folder, and summary statistics will be printed to the console.

## 🔍 Key Findings

1. **Demographics:** Most respondents are young adults — the median age is 24 years (range 18–33). The dataset skews male (222 vs 166 female) and heavily towards **students** (207 of 388), which explains why 187 respondents report **"No Income."**

2. **Family size:** Family sizes are fairly evenly spread between 1 and 6, with a median of 3 — no major outliers, confirmed by the boxplot.

3. **High reorder rate:** 301 out of 388 respondents (≈78%) said they would order again (`Output = Yes`), and feedback is overwhelmingly **positive** (317 positive vs 71 negative) — indicating strong customer satisfaction with online food delivery in this sample.

4. **Feedback vs reorder link:** Customers with positive feedback are far more likely to say they'd reorder, while nearly all "No" (won't reorder) responses cluster with negative feedback — showing feedback sentiment is a strong predictor of retention.

5. **Age vs Family size:** The scatter plot shows no strong correlation between age and family size in this sample, and no clear pattern separating positive vs. negative feedback by these two variables alone.

6. **Correlation heatmap:** Numerical features (Age, Family size, latitude, longitude, Pin code) show weak-to-no linear correlation with each other, suggesting reorder/feedback behavior is driven more by categorical factors (income, occupation, customer type) than by these numeric variables.

7. **No missing data:** The dataset has zero null values across all columns, so no imputation was required — only minor text cleanup (trimming whitespace, dropping a redundant duplicate column).

## 🛠️ Tools Used

- Python 3
- pandas
- matplotlib
- seaborn

---
*Part of my Data Science / Data Analytics internship — Task 2 (EDA).*
