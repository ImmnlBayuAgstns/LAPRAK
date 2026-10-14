import json
import os
import joblib
import pandas as pd
from flask import Flask, jsonify, request

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'breast_cancer_GBC_model.pkl')
DATA_PATH = os.path.join(BASE_DIR, 'data.json')

joblib_model = joblib.load(MODEL_PATH)

MODEL_COLUMNS = [
    'Age',
    'Gender',
    'BMI',
    'Family_History',
    'Smoking',
    'Alcohol_Consumption',
    'Physical_Activity',
    'Hormone_Therapy',
    'Menopause_Status',
    'Genetic_Mutation',
    'Tumor_Size_cm',
    'Lymph_Node_Involvement',
    'Mammogram_Result',
    'Blood_Pressure',
    'Cholesterol',
    'Diabetes',
    'Exercise_Days_Per_Week',
    'Breastfeeding_History',
    'Annual_Income_USD',
]


def load_input_data():
    payload = request.get_json(silent=True)

    if payload is not None:
        if isinstance(payload, dict) and 'data' in payload:
            payload = payload['data']
        if isinstance(payload, list):
            return prepare_model_input(payload)

    with open(DATA_PATH, 'r', encoding='utf-8') as file:
        payload = json.load(file)

    if isinstance(payload, dict) and 'data' in payload:
        payload = payload['data']

    if not isinstance(payload, list):
        raise ValueError('JSON input must be a list of records or an object with a "data" list.')

    return prepare_model_input(payload)


def prepare_model_input(records):
    """Validate records and return only the columns expected by the model."""
    input_data = pd.DataFrame(records)
    missing_columns = sorted(set(MODEL_COLUMNS) - set(input_data.columns))

    if missing_columns:
        raise ValueError(
            'The input data is missing model columns: '
            + ', '.join(missing_columns)
            + '. Update data.json to use the same columns as the training data.'
        )

    return input_data[MODEL_COLUMNS]


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = load_input_data()
        prediction = joblib_model.predict(data)
        return jsonify({'prediction': prediction.tolist()})
    except FileNotFoundError:
        return jsonify({'error': f'File not found: {DATA_PATH}'}), 404
    except ValueError as exc:
        return jsonify({'error': str(exc)}), 400
    except Exception as exc:
        return jsonify({'error': f'Prediction failed: {str(exc)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)