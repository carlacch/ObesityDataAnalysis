# SERVER
from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def prediction():
    data = request.get_json()
    prediction = model.predict(data)

    NObesity = {
        0:"Insufficient Weight", 
        1:"Normal Weight", 
        2:"Overweight Level I", 
        3:"Overweight Level II",
        4:"Obesity Type I",
        5:"Obesity Type II",
        6:"Obesity Type III"}
    
    preds = np.empty(len(prediction), dtype=object)
    for i in range(len(prediction)) :
        preds[i] = NObesity.get(prediction[i])

    prediction = np.array2string(preds)
    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'models\RandomForest_model.pickle'
    model = p.load(open(modelfile, 'rb'))
    print('Model loaded')
    app.run(debug=True, host='localhost')