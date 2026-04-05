# Diabetes_Prediction_Project
A machine learning web application that predicts diabetes risk using 3 ML models trained on the Pima Indians Diabetes Dataset.

## Feature Importance Chart

<img width="796" height="949" alt="image" src="https://github.com/user-attachments/assets/e0cd7b2b-ec35-4c89-9df0-e75373d8ed16" />
<img width="796" height="963" alt="image" src="https://github.com/user-attachments/assets/701e962e-5f19-47aa-bd4b-3665e759f371" />



### Model Comparison + Prediction
(results/diabetic_result.png)

## Models Used

| Model | Accuracy |
|---|---|
| Random Forest | 79.87% ✅ Best |
| Logistic Regression | 77.92% |
| SVM | 75.97% |

## Features
- 3 ML models with live switching
- All 8 clinical inputs with validation
- Feature importance chart (Chart.js)
- Flask REST API with CORS
- Color-coded probability result

## How to Run

### 1. Clone the repo
git clone https://github.com/sagarkaushik9/Diabetes_Prediction_Project.git
cd Diabetes_Prediction_Project

### 2. Install dependencies
pip install -r requirements.txt

### 3. Start Flask backend
python app/app.py

### 4. Open frontend
Open frontend/index.html with Live Server in VS Code

## Tech Stack
- Python, Flask, flask-cors
- scikit-learn (LR, Random Forest, SVM)
- HTML, CSS, JavaScript, Chart.js
- Dataset: Pima Indians Diabetes (768 samples)

## Author
Sagar Kaushik — github.com/sagarkaushik9
