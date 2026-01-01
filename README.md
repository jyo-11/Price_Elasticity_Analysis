
# 📊 Price Elasticity of Demand Analysis (Retail)

## 📌 Project Overview

This project analyzes **price elasticity of demand** using retail transaction data to understand how changes in price impact product demand and revenue. A **log–log regression model** is used to estimate elasticity, followed by **pricing scenario simulations** to support data-driven pricing decisions.

The project is built with a **modular, industry-style pipeline** separating data cleaning, modeling, and simulation logic.

---

## 🎯 Objectives

* Measure price elasticity of demand using statistical modeling
* Analyze price–quantity relationships through EDA
* Simulate price changes to evaluate revenue impact
* Build a reusable, version-controlled analytics pipeline

---

## 🗂️ Project Structure

```
Price_Elasticity_Analysis/
│
├── data/
│   └── supermarket_sales.csv
│
├── src/
│   ├── preprocessing.py        # Data loading, cleaning, renaming
│   ├── elasticity_model.py     # Log-log regression using OLS
│   └── simulation.py           # Price & revenue simulations
│
├── notebooks/
│   └── eda.ipynb               # Exploratory Data Analysis
│
├── requirements.txt
└── README.md
```

---

## 📊 Exploratory Data Analysis (EDA)

EDA was performed to:

* Inspect price and quantity distributions
* Identify invalid or missing values
* Validate assumptions required for log–log regression
* Understand demand patterns before modeling

All EDA is documented in `eda.ipynb`.

---

## 📈 Modeling Approach

* Used **log–log regression** to estimate price elasticity:

  [
  \log(Q) = \beta_0 + \beta_1 \log(P) + \epsilon
  ]

* **β₁** represents price elasticity of demand

* Model trained using **Ordinary Least Squares (OLS)** from `statsmodels`

* Input validation ensures all prices and quantities are positive

---

## 🔄 Pricing & Revenue Simulation

Using the estimated elasticity:

* Simulated price changes (±5%, ±10%, ±20%)
* Estimated corresponding demand changes
* Calculated revenue impact for each scenario

This enables **what-if pricing analysis** for decision-making.

---

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Statsmodels**
* **Jupyter Notebook**
* **Git & GitHub**

---

## ✅ Key Outcomes

* Built an end-to-end pricing analytics pipeline
* Estimated demand sensitivity using statistical modeling
* Delivered actionable revenue insights through simulation
* Followed clean, modular, and reproducible code practices

---

## 🚀 How to Run

```bash
pip install -r requirements.txt
```

Run EDA:

```bash
jupyter notebook notebooks/eda.ipynb
```

---

## 📌 Notes

* No dashboard or deployment included
* Focused on modeling correctness and analytical clarity
* Designed to reflect real-world pricing analytics workflows



