# Time Series Forecasting of Gold Prices in Sri Lanka Using Machine Learning Models

This project focuses on forecasting gold prices in Sri Lanka using machine learning models, specifically XGBoost and LSTM. Real-world data was collected through web scraping, and several influential economic indicators were incorporated to improve prediction accuracy.

---

## 📌 Project Overview

Gold prices are influenced by a variety of global and local economic factors. In this project, I aimed to build a robust model to predict the gold price in Sri Lanka using historical data and additional economic indicators.

---

## 📅 Data Collection

- **Period Covered**: January 2016 to April 2025  
- **Data Sources**: Scraped from various reliable websites using BeautifulSoup  
- **Features Used**:
  - Historical Gold Prices (LKR)
  - USD to LKR Exchange Rate
  - Petrol 92 Octane Price (LKR)
  - Petrol 95 Octane Price (LKR)

---

## 🧠 Models Used

### 1. XGBoost Regressor ✅
- Achieved high accuracy
- Outperformed the **Random Walk** baseline
- Final Evaluation:
  - **RMSE**: 157.23
  - **MAE**: 94.89
  - **R² Score**: 0.9995

### 2. LSTM Neural Network ❌
- Model trained successfully
- Although it showed promising trends, it **did not outperform** the Random Walk baseline
- Not considered suitable for final forecasting

### 3. Random Walk (Baseline)
- Used as a performance benchmark
  - **RMSE**: 10143.81
  - **MAE**: 7999.62

---

## 🧪 Evaluation Strategy

To validate model performance, a Random Walk baseline was implemented where each prediction is the previous day's price. Any model that beats this baseline is considered viable for time series forecasting. The XGBoost model clearly surpassed this benchmark.

---

## ⚙️ Tech Stack

- **Programming Language**: Python
- **Libraries Used**:
  - scikit-learn
  - pandas
  - numpy
  - tensorflow (for LSTM)
  - xgboost
  - BeautifulSoup (for web scraping)
  - matplotlib (for visualization)

---

## 📈 Results Summary

| Model      | RMSE     | MAE     | R² Score |
|------------|----------|---------|----------|
| Random Walk | 10143.81 | 7999.62 | —        |
| XGBoost     | 157.2303   | 94.8882  | 0.9995   |

---

