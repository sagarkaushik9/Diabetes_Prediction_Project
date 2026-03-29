from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Fix: allows your HTML frontend to call the API without browser blocking

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH  = os.path.join(BASE_DIR, "..", "models", "lr_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "..", "models", "scaler.pkl")

try:
    model  = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("Model and scaler loaded successfully.")
except Exception as e:
    print(f" Error loading model/scaler: {e}")
    model = scaler = None


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
    if model is None or scaler is None:
        return jsonify({"error": "Model not loaded. Check server logs."}), 500

    data = request.get_json(force=True, silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON body."}), 400

    # Validate all required fields
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
            "prediction":  "Diabetic" if pred == 1 else "Not Diabetic",
            "probability": round(prob * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": f"Prediction failed: {str(e)}"}), 500


@app.route("/health", methods=["GET"])
def health():
    """Simple health check so the frontend can confirm the server is alive."""
    return jsonify({"status": "ok", "model_loaded": model is not None})


if __name__ == "__main__":
    print("Starting Flask server on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
