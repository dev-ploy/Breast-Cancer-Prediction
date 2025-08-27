from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
import os
model_path = os.path.join(os.path.dirname(__file__), '..', 'model', 'model.pkl')
model=model = pickle.load(open(model_path, 'rb'))

template_path = os.path.join(os.path.dirname(__file__), '..', 'templates')
static_path = os.path.join(os.path.dirname(__file__), '..', 'static')

#flask app
app = Flask(__name__, template_folder=template_path, static_folder=static_path)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        feature=request.form['feature']
        features_list = [f.strip() for f in feature.split(',')]
        try:
            np_features=np.asarray(features_list,dtype=np.float32) #convert into numpy array
            pred=model.predict(np_features.reshape(1,-1)) #prediction for 1 instance
            return render_template("index.html", message=output)
            output=["Cancerous"if pred[0]==1 else "Not Cancerous"]
        except Exception as e:
            return render_template("index.html", message=[f"Error: {str(e)}"])
    # return render_template("index.html",message=output)
    else:
        # Handle GET requests gracefully
        return render_template("index.html", message=["Please submit features using the form."])


#Python main

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
