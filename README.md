# Student Performance Prediction

This project aims to predict students' academic performance using machine learning techniques. The model analyzes how various demographic, parental, and educational factors influence student test scores in math, reading, and writing. The implementation follows a modular, production-ready structure with data ingestion, transformation, and model training components.

---

## Problem Statement

The goal is to analyze and predict a student's academic performance based on the following input features:

- Gender
- Race/Ethnicity
- Parental level of education
- Type of lunch received
- Completion of a test preparation course

The target is the **average score** derived from math, reading, and writing scores.

---

## Dataset

- **Source**: [Kaggle – Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Format**: CSV
- **Size**: 1000 rows × 8 columns

### Key Features
- Categorical: `gender`, `race/ethnicity`, `parental level of education`, `lunch`, `test preparation course`
- Numerical: `math score`, `reading score`, `writing score`
- Engineered:
  - `total_score` = sum of all three scores
  - `average` = mean of all three scores

---

## Data Preprocessing

- Null check and validation
- Label encoding of categorical variables
- Feature scaling using `StandardScaler`
- Engineered `total_score` and `average` columns

---

## Exploratory Data Analysis (EDA)

Notebook: [`EDA STUDENT PERFORMANCE.ipynb`](https://github.com/AnamAhmed03/student_performace_app/blob/main/notebook/1%20.%20EDA%20STUDENT%20PERFORMANCE%20.ipynb)

Highlights:
- Distribution plots for each score
- Count plots for categorical features
- Grouped comparisons based on gender, lunch, test prep, and parental education
- Correlation analysis to identify key influencing features

---

## Model Training

Notebook: [`MODEL TRAINING.ipynb`](https://github.com/AnamAhmed03/student_performace_app/blob/main/notebook/2.%20MODEL%20TRAINING.ipynb)

### Models Evaluated

| Model                | Description                          |
|---------------------|--------------------------------------|
| Linear Regression    | Baseline model                      |
| Ridge, Lasso         | Regularized models                  |
| Decision Tree        | Simple, interpretable model         |
| Random Forest        | Ensemble model for better accuracy  |

### Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

**Best Performing Model**: `Linear Regression` with **R² ~ 0.88**

---

## Modular ML Pipeline

The project follows a modular structure with reusable components.

### Directory: `src/components/`

| File                    | Responsibility                          |
|-------------------------|------------------------------------------|
| `data_ingestion.py`     | Reads raw data, splits into train/test   |
| `data_transformation.py`| Applies encoding and scaling             |
| `model_trainer.py`      | Trains and evaluates multiple models     |
| `logger.py`             | Handles logging across the pipeline      |
| `exception.py`          | Custom error handling with tracebacks    |
| `utils.py`              | Model saving, loading, and metrics       |

### Directory: `src/pipeline/`
| File                    | Responsibility                          |
|-------------------------|------------------------------------------|
| `predict_pipeline.py`   | Handles real-time predictions by loading the     |
                          | trained model and preprocessor to transform      |
                          | new input data and return predicted performance. |

### Flow Summary

```
Raw CSV → Data Ingestion → Data Transformation → Model Training → Evaluation → Save Best Model
```

---

## Code Execution

### 1. Clone Repository

```bash
git clone https://github.com/AnamAhmed03/student_performace_app.git
cd student_performace_app
```

### 2. Create Virtual Environment

```bash
# Create
python -m venv .venv

# Activate (Windows)
.\.venv\Scripts ctivate

# Activate (Linux/macOS)
source .venv/bin/activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run Pipeline

```bash
python src/components/data_ingestion.py
```

Make sure the dataset file `stud.csv` is available under `notebook/data/`.

---

## Project Structure

```
student_performace_app/
│
├── notebook/
│   ├── 1. EDA STUDENT PERFORMANCE.ipynb
│   └── 2. MODEL TRAINING.ipynb
│
├── src/
│   ├── components/
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   ├── model_trainer.py
│   ├── logger.py
│   ├── exception.py
│   └── utils.py
│
├── artifacts/             # Stores train/test/raw CSVs
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```
