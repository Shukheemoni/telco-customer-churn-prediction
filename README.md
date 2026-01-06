# telco-customer-churn-prediction
End-to-end machine learning pipeline for customer churn prediction with class imbalance handling.
Telco Customer Churn Prediction
Project Overview

Customer churn is a major business problem in subscription-based industries such as telecommunications, where retaining existing customers is significantly cheaper than acquiring new ones.

This project builds an end-to-end machine learning pipeline to predict customer churn, with a strong focus on class imbalance handling, recall optimization, and business-oriented evaluation.

Dataset

Source: IBM Telco Customer Churn Dataset

Total Records: 7,043 customers

Target Variable: Churn Value

1 → Customer churned

0 → Customer retained

The dataset contains customer demographics, service usage, billing details, and contract information.

Problem Statement

The goal is to identify customers who are likely to churn so that proactive retention strategies can be applied.

Because churned customers represent a minority class (~26%), traditional accuracy is misleading. Missing a churned customer leads to permanent revenue loss, while incorrectly flagging a retained customer incurs a relatively small cost.

Evaluation Metrics

Primary Metric: Recall (churn class)

Secondary Metric: F1-score

Additional Metric: ROC-AUC

Why Recall?
Recall measures how many actual churn customers are correctly identified. In real business settings, minimizing false negatives (missed churners) is critical.

Approach & Pipeline
1. Data Cleaning & Leakage Prevention

Removed non-predictive identifiers and geographic features

Removed leakage features such as:

Churn Label

Churn Score

Churn Reason

CLTV

Fixed invalid entries in Total Charges and imputed using median values

2. Exploratory Data Analysis

Confirmed class imbalance (~26% churn vs ~74% non-churn)

Analyzed numerical and categorical features against churn

Retained realistic outliers

3. Preprocessing Pipeline

Implemented using Pipeline and ColumnTransformer:

Numerical features

Median imputation

Standard scaling

Categorical features

Most-frequent imputation

One-hot encoding with unseen-category handling

This ensures no data leakage and full reproducibility.

Class Imbalance Handling

Different strategies were used depending on the model:

Logistic Regression & Random Forest

class_weight="balanced"


XGBoost

scale_pos_weight = (# non-churn) / (# churn)


These methods increase the penalty for misclassifying churned customers.

Models Trained

Logistic Regression

Random Forest

XGBoost (final selected model)

All models used the same preprocessing pipeline for fair comparison.

Model Performance
Model	Recall	F1-score
Logistic Regression	0.78	0.62
Random Forest	0.50	0.56
XGBoost (Tuned)	0.79	0.63

ROC-AUC (Final XGBoost): 0.85

Model Selection

XGBoost was selected as the final model due to:

Strong recall performance

Balanced precision–recall trade-off

High ROC-AUC score

Robust handling of nonlinear feature interactions

Effective performance on imbalanced data

Business Insights

The model accurately identifies customers at high risk of churn

Acceptable false positives allow proactive retention at low cost

Churn probabilities can be used for:

Risk-based customer segmentation

Targeted retention campaigns

Optimized marketing and retention spend

Deploying this model can reduce churn rate and improve customer lifetime value

Project Structure
├── data/
│   └── Telco_customer_churn.xlsx
├── notebooks/
│   └── churn_prediction.ipynb
├── src/
│   └── utils.py
├── requirements.txt
└── README.md

Key Skills Demonstrated

End-to-end machine learning pipeline design

Class imbalance handling

Feature preprocessing with ColumnTransformer

Model comparison and selection

Business-driven metric selection

Clean, reusable, production-style code

Practical ML engineering workflow

Final Notes

This project prioritizes real-world machine learning decision-making over raw accuracy. The workflow, evaluation strategy, and business interpretation align closely with industry standards for applied machine learning and ML engineering roles.
