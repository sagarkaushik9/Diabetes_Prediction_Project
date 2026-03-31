from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_model(name):
    path = os.path.join(BASE_DIR, "..", "models", name)
    try:
        return joblib.load(path)
    except Exception as e:
        print(f"Could not load {name}: {e}")
        return None

scaler = load_model("scaler.pkl")
models = {
    "lr":  load_model("lr_model.pkl"),
    "rf":  load_model("rf_model.pkl"),
    "svm": load_model("svm_model.pkl"),
}

MODEL_INFO = {
    "lr":  {"name": "Logistic Regression", "accuracy": 77.92},
    "rf":  {"name": "Random Forest",       "accuracy": 79.87},
    "svm": {"name": "SVM",                 "accuracy": 75.97},
}

REQUIRED_FIELDS = {
    "pregnancies":    (0,   17),
    "glucose":        (0,  300),
    "blood_pressure": (0,  200),
    "skin_thickness": (0,  100),
    "insulin":        (0,  900),
    "bmi":            (0,  100),
    "dpf":            (0,    5),
    "age":            (0,  120),
}


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True, silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON body."}), 400

    model_key = data.get("model", "rf")
    if model_key not in models:
        return jsonify({"error": f"Unknown model. Use: lr, rf, svm"}), 400

    model = models[model_key]
    if model is None or scaler is None:
        return jsonify({"error": "Model not loaded."}), 500

    values = {}
    for field, (lo, hi) in REQUIRED_FIELDS.items():
        val = data.get(field)
        if val is None:
            return jsonify({"error": f"Missing field: {field}"}), 400
        try:
            val = float(val)
        except (TypeError, ValueError):
            return jsonify({"error": f"Field '{field}' must be a number."}), 400
        if not (lo <= val <= hi):
            return jsonify({"error": f"Field '{field}' out of range [{lo}, {hi}]."}), 400
        values[field] = val

    try:
        features = np.array([[
            values["pregnancies"], values["glucose"], values["blood_pressure"],
            values["skin_thickness"], values["insulin"], values["bmi"],
            values["dpf"], values["age"]
        ]])
        scaled = scaler.transform(features)
        pred   = int(model.predict(scaled)[0])
        prob   = float(model.predict_proba(scaled)[0][1])

        return jsonify({
            "prediction":     "Diabetic" if pred == 1 else "Not Diabetic",
            "probability":    round(prob * 100, 2),
            "model_used":     MODEL_INFO[model_key]["name"],
            "model_accuracy": MODEL_INFO[model_key]["accuracy"],
        })
    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


@app.route("/models", methods=["GET"])
def get_models():
    return jsonify({
        key: {"name": info["name"], "accuracy": info["accuracy"], "loaded": models[key] is not None}
        for key, info in MODEL_INFO.items()
    })


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "models_loaded": {k: v is not None for k, v in models.items()}})


if __name__ == "__main__":
    print("Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
