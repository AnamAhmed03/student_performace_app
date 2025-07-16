# Student Performance Prediction

This project applies machine learning techniques to predict student academic performance based on demographic, social, and academic features. The goal is to identify the factors that most influence performance and provide insights for early interventions in the education system.



## Problem Statement

The objective is to analyze how student performance in math, reading, and writing is affected by:

- Gender
- Race/ethnicity
- Parental level of education
- Lunch type (standard vs. free/reduced)
- Completion of test preparation course



##  Dataset

- **Source**: [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)
- **Format**: CSV
- **Shape**: 1000 rows × 8 columns

**Key features:**
- Demographics: `gender`, `race/ethnicity`
- Parental & socioeconomic: `parental level of education`, `lunch`
- Academic: `math score`, `reading score`, `writing score`
- Additional feature added: `average score` (mean of the three scores)

---

##  Data Preprocessing

- Checked for null values
- Encoded categorical variables using `LabelEncoder`
- Standardized numerical features using `StandardScaler`
- Create an additional column `total_score` = sum of all three scrores
- Created an additional column `average` = mean of all three scores



## Exploratory Data Analysis (EDA)

Notebook: [`EDA STUDENT PERFORMANCE.ipynb`](https://github.com/AnamAhmed03/student_performace_app/blob/main/notebook/1%20.%20EDA%20STUDENT%20PERFORMANCE%20.ipynb)

- Distribution plots for scores
- Count plots for categorical variables
- Bar charts to compare group performance
- Grouped analysis based on lunch, test prep, and parental education



##  Model Training

Notebook: [`MODEL TRAINING.ipynb`](https://github.com/AnamAhmed03/student_performace_app/blob/main/notebook/2.%20MODEL%20TRAINING.ipynb)

**Algorithms Used:**

| Model              | Description                        |
|-------------------|------------------------------------|
| Linear Regression | Baseline model                     |
| Ridge & Lasso     | Regularized regression models      |
| Random Forest     | High-performing ensemble model     |
| Decision Tree     | Simple interpretable model         |

**Evaluation Metrics:**
- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)

**Best Model:** Linear Regressor  
**R² Score:** ~0.88 on test data

---

##  How to Run This Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/AnamAhmed03/student_performace_app.git
cd student-performance-predictor


# Create a virtual env

# 1.Create a virtual env
python -m venv .venv
# 2. Activate it
.\.venv\Scripts\Activate.ps1
# 3. Intitalize git