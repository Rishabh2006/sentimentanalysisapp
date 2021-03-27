# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import uvicorn
from fastapi import FastAPI
from predict import Predict1
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier= pickle.load(pickle_in)

pickle1_in = open("classifier1.pkl","rb")
vectorizer=pickle.load(pickle1_in)


@app.post('/predict')
def predict_sentiment(data : Predict1):
    
   
    text = data.Review
    vector = vectorizer.transform([text])
    prediction = classifier.predict(vector)[0]
    return prediction

if __name__ == '__temp__':
    uvicorn.run(app, host= '127.0.01', port =8000)