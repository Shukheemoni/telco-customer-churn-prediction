# 📡 Telco Customer Churn Prediction

**End-to-end machine learning pipeline for customer churn prediction with class imbalance handling.**

## 📌 Project Overview
Customer churn is a major business problem in subscription-based industries such as telecommunications, where retaining existing customers is significantly cheaper than acquiring new ones.

This project builds an end-to-end machine learning pipeline to predict customer churn, with a strong focus on class imbalance handling, recall optimization, and business-oriented evaluation.

## 📊 Dataset
* **Source:** IBM Telco Customer Churn Dataset
* **Total Records:** 7,043 customers
* **Target Variable:** `Churn Value`
    * `1` = Customer churned
    * `0` = Customer retained
* **Features:** Customer demographics, service usage, billing details, and contract information.

## ❓ Problem Statement
The goal is to identify customers who are likely to churn so that proactive retention strategies can be applied.

Because churned customers represent a minority class (~26%), traditional accuracy is misleading. Missing a churned customer leads to permanent revenue loss, while incorrectly flagging a retained customer incurs a relatively small cost.

## 📉 Evaluation Metrics
* **Primary Metric:** **Recall (Churn Class)**
* **Secondary Metric:** F1-Score
* **Additional Metric:** ROC-AUC

**Why Recall?**
Recall measures how many actual churn customers are correctly identified. In real business settings, minimizing false negatives (missed churners) is critical to preventing revenue loss.

## 🛠️ Approach & Pipeline

### 1. Data Cleaning & Leakage Prevention
* Removed non-predictive identifiers and geographic features.
* **Leakage Removal:** Dropped features that are only known *after* churn occurs, including `Churn Label`, `Churn Score`, `Churn Reason`, and `CLTV`.
* Fixed invalid entries in `Total Charges` and imputed using median values.

### 2. Exploratory Data Analysis (EDA)
* Confirmed class imbalance (~26% churn vs ~74% non-churn).
* Analyzed numerical and categorical features against churn.
* Retained realistic outliers to preserve data integrity.

### 3. Preprocessing Pipeline
Implemented using `Pipeline` and `ColumnTransformer` for full reproducibility:
* **Numerical Features:** Median imputation + Standard Scaling.
* **Categorical Features:** Most-frequent imputation + One-Hot Encoding (with `handle_unknown='ignore'`).

### 4. Class Imbalance Handling
Strategies used to penalize misclassifying churners:
* **Logistic Regression & Random Forest:** `class_weight="balanced"`
* **XGBoost:** `scale_pos_weight` calculated as `(Count Negative) / (Count Positive)`

## 🚀 Model Performance

All models used the same preprocessing pipeline for fair comparison.

| Model | Recall (Churn) | F1-Score |
| :--- | :--- | :--- |
| **Logistic Regression** | 0.78 | 0.62 |
| **Random Forest** | 0.50 | 0.56 |
| **XGBoost (Tuned)** | **0.79** | **0.63** |

* **Final ROC-AUC (XGBoost):** 0.85

## 🏆 Model Selection
**XGBoost** was selected as the final model due to:
* Strong recall performance (0.79).
* Balanced precision–recall trade-off.
* High ROC-AUC score (0.85).
* Robust handling of non-linear feature interactions and imbalanced data.

## 💡 Business Insights
* **Risk Identification:** The model accurately identifies customers at high risk of churn.
* **Cost Efficiency:** Acceptable false positives allow for proactive retention campaigns at a low cost compared to the loss of a customer.
* **Strategic Application:** Churn probabilities can be used for risk-based customer segmentation and optimizing marketing spend.

## 📂 Project Structure

```text
├── data/
│   └── Telco_customer_churn.xlsx
├── notebooks/
│   └── churn_prediction.ipynb
├── src/
│   └── utils.py
├── requirements.txt
└── README.md
