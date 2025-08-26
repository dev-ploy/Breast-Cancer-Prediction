from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
import os
model = pickle.load(open(os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl'), 'rb'))

#flask app
app = Flask(__name__, template_folder="../templates", static_folder="../static")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    feature=request.form['feature']
    features_list=feature.split(',')
    np_features=np.asarray(features_list,dtype=np.float32) #convert into numpy array
    pred=model.predict(np_features.reshape(1,-1)) #prediction for 1 instance

    output=["Cancerous"if pred[0]==1 else "Not Cancerous"]

    return render_template("index.html",message=output)



#Python main

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
