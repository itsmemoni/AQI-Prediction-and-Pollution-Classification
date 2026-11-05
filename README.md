# AQI Prediction and Pollution Level Classification Using Machine Learning

**Team:** 6  
**Route:** A — Supervised Learning

## Project overview
This beginner-friendly academic project predicts an estimated Air Quality Index (AQI) from six pollutant measurements: PM2.5, PM10, NO2, SO2, CO and O3. A Random Forest Regressor is trained using the included sample CSV dataset. The Flask web page accepts measurements and displays the predicted AQI with a pollution category.

## Folder structure
- `app.py` — Flask web application
- `train_model.py` — trains and evaluates the machine-learning model
- `data/aqi_sample_data.csv` — sample training data (synthetic/demo data)
- `models/` — trained model is saved here after training
- `templates/index.html` — web page
- `static/style.css` — page design

## Run on Windows
1. Extract the ZIP file.
2. Open the extracted `AQI_Prediction_ML_Project` folder in VS Code.
3. Open Terminal in VS Code.
4. Create a virtual environment (optional but recommended):
   `py -m venv venv`
5. Activate it in PowerShell:
   `.\venv\Scripts\Activate.ps1`
6. Install packages:
   `py -m pip install -r requirements.txt`
7. Train the model:
   `py train_model.py`
8. Start the website:
   `py app.py`
9. Open `http://127.0.0.1:5000` in your browser.

If PowerShell blocks environment activation, you can skip steps 4–5 and run the install/train/app commands using `py`.

## Important academic note
The included CSV is **synthetic sample data created for demonstrating the project workflow**. It is not official CPCB data and must not be presented as real measured pollution data. For a final research submission, replace it with a documented real dataset (for example, CPCB/official monitoring data), cite its source, clean missing values, and retrain the model. AQI breakpoints and pollutant units should be aligned with the standard required by your project guide.

## Suggested project workflow
Data collection → Data cleaning → Feature selection → Train/test split → Random Forest training → AQI prediction → Pollution category display → Evaluation.

## Team work split (suggestion)
1. Dataset collection and documentation
2. Data preprocessing and analysis
3. Model training and evaluation
4. AQI category mapping and testing
5. Flask frontend and integration
6. Report, diagrams, presentation and validation
