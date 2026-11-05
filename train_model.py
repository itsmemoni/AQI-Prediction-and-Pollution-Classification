"""Train a beginner-friendly supervised regression model from the included sample dataset."""
from pathlib import Path
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

DATA = Path("data/aqi_sample_data.csv")
MODEL = Path("models/aqi_model.pkl")

def train():
    df = pd.read_csv(DATA)
    features = ["PM2.5", "PM10", "NO2", "SO2", "CO", "O3"]
    X = df[features]
    y = df["AQI"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=120, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Mean Absolute Error:", round(mean_absolute_error(y_test, predictions), 2))
    print("R2 Score:", round(r2_score(y_test, predictions), 3))
    MODEL.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL)
    print("Model saved to", MODEL)

if __name__ == "__main__":
    train()
