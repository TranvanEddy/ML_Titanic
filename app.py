#import des librairies nécessaires
from flask import Flask, request, render_template
import numpy as np
import joblib

app = Flask(__name__)
model = joblib.load("model1.gz")
@app.route("/")
def home():
    return render_template("index.html")
@app.route('/predict',methods=["POST"]) 
#fonction de traitement des données saisies par l'utilisateur  
def predict():
    data_saisie = [int(x) for x in request.form.values()]
    if(data_saisie[3]==1):
        data_saisie[3]=[1,0,0]
    elif(data_saisie[3]==2):
        data_saisie[3]=[0,1,0]
    else:
        data_saisie[3]=[0,0,1]
    if(data_saisie[4]==0):
        data_saisie[4]=[0,1]
    else:
        data_saisie[4]=[1,0]
    X1= data_saisie[:3]
    for i in data_saisie[3]:
        X1.append(i)
    for i in data_saisie[4]:
        X1.append(i)
    X1.append(data_saisie[5])
    X = [np.array(X1)]
    prediction = model.predict(X)
    prediction1 = model.predict_proba(X)
    if(prediction==0):
        prediction="non"
    else:
        prediction="oui"
    return render_template("index.html", zone_prediction="Auriez-vous survécu? : {}".format(prediction), zone_prediction1="probabilité de [ne pas survivre / survivre]: {}".format(prediction1))
if __name__ == "__main__":
    app.run(debug=True)
