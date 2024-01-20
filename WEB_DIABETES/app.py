from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open("models/diabetes_classifier.pkl", 'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    BP = CHL = bmi = SMO = STK = HRT = physAct = DRK = genHeal = menHeal = physHeal = WLK = AGE = EDU = INC = ""
    data = []
    if request.method == "POST":
        BP = int(request.form.get('BP'))
        CHL = int(request.form.get('CHL'))
        bmi = int(request.form.get("bmi"))
        SMO = int(request.form.get('SMO'))
        STK = int(request.form.get('STK'))
        HRT = int(request.form.get('HRT'))
        physAct = int(request.form.get('physAct'))
        DRK = int(request.form.get('DRK'))
        genHeal = int(request.form.get('genHeal'))
        menHeal = int(request.form.get('menHeal'))
        physHeal = int(request.form.get('physHeal'))
        WLK = int(request.form.get('WLK'))
        AGE = int(request.form.get('AGE'))
        EDU = int(request.form.get('EDU'))
        INC = int(request.form.get('INC'))
    data = np.array([[BP, CHL, bmi, SMO, STK, HRT, physAct, DRK, genHeal, menHeal, physHeal, WLK, AGE, EDU, INC]])
    
    prediction = model.predict(data)
    prediction = 'No diabetes' if prediction == 0 else "Diabetes"

    return render_template("result.html", KQ = prediction)


if __name__ == "__main__":
    app.run(debug=True)