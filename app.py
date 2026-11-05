from flask import Flask, render_template, request
import joblib
import pandas as pd
from pathlib import Path

app = Flask(__name__)
MODEL_PATH = Path("models/aqi_model.pkl")

def get_model():
    if not MODEL_PATH.exists():
        from train_model import train
        train()
    return joblib.load(MODEL_PATH)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None
    if request.method == "POST":
        try:
            values = {
                "PM2.5": float(request.form["pm25"]),
                "PM10": float(request.form["pm10"]),
                "NO2": float(request.form["no2"]),
                "SO2": float(request.form["so2"]),
                "CO": float(request.form["co"]),
                "O3": float(request.form["o3"]),
            }
            model = get_model()
            frame = pd.DataFrame([values])
            prediction = float(model.predict(frame)[0])
            if prediction <= 50:
                level, advice = "Good", "Air quality is satisfactory."
            elif prediction <= 100:
                level, advice = "Satisfactory", "Air quality is acceptable for most people."
            elif prediction <= 200:
                level, advice = "Moderate", "Sensitive people should reduce prolonged outdoor activity."
            elif prediction <= 300:
                level, advice = "Poor", "Reduce prolonged outdoor activity; sensitive groups should take care."
            elif prediction <= 400:
                level, advice = "Very Poor", "Avoid prolonged outdoor activity."
            else:
                level, advice = "Severe", "Avoid outdoor activity and follow local health guidance."
            result = {"aqi": round(prediction, 1), "level": level, "advice": advice}
        except (ValueError, KeyError):
            error = "Please enter valid numeric values in every field."
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
