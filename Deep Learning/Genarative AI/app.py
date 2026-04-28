from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Load trained model
saved = joblib.load("model.joblib")
parameters = saved["parameters"]
scaler = saved["scaler"]

app = FastAPI()

class InputData(BaseModel):
    input: list  # expecting a list of features

@app.post("/predict")
def predict_api(data: InputData):
    new_input = np.array(data.input).reshape(1, -1)
    new_input = scaler.transform(new_input)
    prediction = parameters.predict(new_input)
    return {"prediction": int(prediction[0])}

