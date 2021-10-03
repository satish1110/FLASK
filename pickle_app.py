from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
from flasgger import Swagger
from sklearn.linear_model import   LogisticRegression

app = Flask(__name__)
Swagger(app)

#pickle_file = open('lin_reg_model.sav','rb')
pickle_file = open('C:\\Users\\satish\\Downloads\\attrition.pkl','rb')
pickle_model = pickle.load(pickle_file)


@app.route("/")
def home():
    return "Welcome to attrition prediction"

@app.route("/predict")
def predict_model():
    """ Predicting the attrition
    ---
    parameters:
      - name: Age
        in: query
        type: number
        required: true
    
    responses:
        200:
            description: Result is 
    """

    # use try exception 
    
    Age  = request.args.get('Age')
    
    output = pickle_model.predict([[Age]])

    return f"The Prediction is {output}"

if __name__ == '__main__':
    app.run(debug = True)