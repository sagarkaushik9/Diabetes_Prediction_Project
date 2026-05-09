<<<<<<< HEAD
# Diabetes Prediction Project

A machine learning web application that predicts the risk of diabetes using Logistic Regression trained on the Pima Indians Diabetes Dataset.

## Project Structure

```
Diabetes_Prediction_Project/
├── app/
│   └── app.py              # Flask REST API (backend)
├── data/
│   └── diabetes.csv        # Dataset (768 samples, 9 features)
├── frontend/
│   ├── index.html          # Main UI (all 8 clinical inputs)
│   ├── style.css           # Stylesheet (optional, styles now in HTML)
│   └── script.js           # JS logic (optional, now in HTML)
├── models/
│   ├── lr_model.pkl        # Trained Logistic Regression model
│   └── scaler.pkl          # StandardScaler for normalization
├── notebooks/
│   └── diabetes_prediction.ipynb   # Full EDA + training notebook
├── report/                 # (Add your PDF report here)
├── results/                # (Add screenshots/charts here)
├── requirements.txt        # Python dependencies
└── README.md
```

## Model Performance

| Model               | Accuracy | AUC   |
|---------------------|----------|-------|
| Logistic Regression | ~78%     | ~0.83 |
| LDA                 | ~77%     | ~0.82 |

## Input Features

| Feature                   | Description                              | Typical Range |
|---------------------------|------------------------------------------|---------------|
| Pregnancies               | Number of pregnancies                    | 0–17          |
| Glucose                   | Plasma glucose (2h oral glucose test)    | 70–200 mg/dL  |
| Blood Pressure            | Diastolic blood pressure                 | 40–120 mm Hg  |
| Skin Thickness            | Triceps skinfold thickness               | 10–60 mm      |
| Insulin                   | 2-hour serum insulin                     | 0–800 µU/mL   |
| BMI                       | Body Mass Index                          | 18–60 kg/m²   |
| Diabetes Pedigree Function| Family history genetic score             | 0.08–2.42     |
| Age                       | Age in years                             | 21–81         |

## Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/sagarkaushik9/Diabetes_Prediction_Project.git
cd Diabetes_Prediction_Project
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Flask backend
```bash
python app/app.py
```
Server will start at `http://127.0.0.1:5000`

### 4. Open the frontend
Open `frontend/index.html` directly in your browser (double-click it), or use VS Code Live Server extension.

## API Endpoint

**POST** `http://127.0.0.1:5000/predict`

Request body:
```json
{
  "pregnancies": 2,
  "glucose": 148,
  "blood_pressure": 72,
  "skin_thickness": 35,
  "insulin": 0,
  "bmi": 33.6,
  "dpf": 0.627,
  "age": 50
}
```

Response:
```json
{
  "prediction": "Diabetic",
  "probability": 72.4
}
```

## Tech Stack

- **ML**: scikit-learn (Logistic Regression, LDA, StandardScaler)
- **Backend**: Python, Flask, flask-cors
- **Frontend**: HTML, CSS, JavaScript (no framework)
- **Dataset**: Pima Indians Diabetes Dataset (Kaggle / UCI ML Repository)

## Important Note

This tool is for **educational purposes only** and is not a substitute for medical diagnosis. Always consult a qualified healthcare professional.

## Author
Your Name — [GitHub](https://github.com/sagarkaushik9)
=======
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
>>>>>>> 9521909fe542f8f1e547b1ed820b16376b5319b0
