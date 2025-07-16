# Student Performance Prediction

This project applies machine learning techniques to predict student academic performance based on demographic, social, and academic features. The goal is to identify factors that influence performance and provide early intervention insights.


## Problem Statement

Predict the final performance of students using input features such as study time, absences, parental education, previous grades, and more. The problem can be approached as a regression task (predicting final grade) or classification (pass/fail).

---

## Dataset

- Source: UCI Machine Learning Repository – Student Performance Dataset
- Format: CSV
- Key features:
  - Demographics: gender, age
  - Family: parental education, relationship status, support
  - Academic: G1, G2, study time, absences, failures
  - Lifestyle: internet access, health, activities

---

## Data Preprocessing

- Checked and handled missing/null values
- Converted categorical variables using label encoding and one-hot encoding
- Normalized numerical features where necessary
- Removed redundant or low-correlation features

---

## Machine Learning Models Used

| Model               | Purpose                               |
|--------------------|----------------------------------------|
| Linear Regression   | Simple baseline regression             |
| Random Forest       | Ensemble model with better generalization |
| XGBoost             | Optimized boosting algorithm           |
| Decision Tree       | Interpretable baseline model           |

---

## Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Accuracy (if formulated as classification)

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/student-performance-ml.git
   cd student-performance-ml


# Create a virtual env

# 1.Create a virtual env
python -m venv .venv
# 2. Activate it
.\.venv\Scripts\Activate.ps1
# 3. Intitalize git