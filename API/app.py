from flask import Flask, request, redirect, url_for, flash, jsonify, render_template
import numpy as np
import pandas as pd
import pickle as p
import json

app = Flask(__name__)

features = ['Gender', 'Age', 'family_history_with_overweight', 
    'FAVC', 'FCVC', 'NCP', 'CAEC', 'SMOKE', 'CH2O', 'SCC', 'FAF', 
    'TUE', 'CALC', 'MTRANS']

@app.before_first_request
def start():
    global model

    modelfile = 'models\RandomForest_model.pickle'
    model = p.load(open(modelfile, 'rb'))

@app.route('/backgroud_process', methods=['POST', 'GET'])
def background_process():
    Gender = request.args.get('Gender')  
    Age = int(request.args.get('Age'))
    family_history_with_overweight = request.args.get('family_history_with_overweight') 
    FAVC = request.args.get('FAVC')  
    FCVC = request.args.get('FCVC')  
    NCP = request.args.get('NCP')  
    CAEC = request.args.get('CAEC')  
    SMOKE = request.args.get('SMOKE')  
    CH2O = request.args.get('CH2O')  
    SCC = request.args.get('SCC')  
    FAF = request.args.get('FAF')  
    TUE = request.args.get('TUE')  
    CALC = request.args.get('CALC')  
    MTRANS = request.args.get('MTRANS') 

    user_values = [ Gender, Age, family_history_with_overweight, 
    FAVC, FCVC, NCP, CAEC, SMOKE, CH2O, SCC, FAF, 
    TUE, CALC, MTRANS]

    print(user_values)

    data = pd.DataFrame([user_values],columns = features)
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
    return jsonify({'NObesity_prediction':prediction})

@app.route("/", methods=['POST', 'GET'])
def index():
    # Mapping
    gender = {"Female":0, "Male":1}
    fam_history = {"no":0, "yes":0}
    favc = {"no":0, "yes":1}
    fcvc = {"Never":1, "Sometimes":2, "Always":3}
    ncp = {"1":1, "2":2, "3":3, "4 ou plus":4}
    caec = {"No":0,"Sometimes":1,"Frequently":2,"Always":3}
    smoke = {"no":0, "yes":1}
    ch2o = {"Less than a liter":1, "Between 1 and 2L":2, "More than 2L":3}
    scc = {"no":0, "yes":1}
    faf = {"None":0, "1 or 2 days":1, "2 or 4 days":2, "4 or 5 days":3}
    tue = {"0-2 hours":0, "3-5 hours":1, "More than 5 hours":2}
    calc = {"No":0,"Sometimes":1,"Frequently":2,"Always":3}
    mtrans = {"Automobile":1, "Bike":2 , "Motorbike":3, "Public Transportation":4 ,"Walking":5}

    return render_template( 'index.html', gender = gender, fam_history = fam_history,
    favc=favc, fcvc=fcvc, ncp=ncp, caec=caec, smoke=smoke, ch2o=ch2o, 
    scc=scc, faf=faf, tue=tue, calc=calc, mtrans=mtrans)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')