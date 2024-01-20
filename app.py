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

    name = highBP = highChol = bmi = smoker = stroke = heartDis = physCal = drink = genHlth = menHlth = physHlth = walk = age = edu = inc = ""
    data = []
    if request.method == "POST":
        name = request.form.get('yname')
        highBP = int(request.form.get('recommedBP'))
        highChol = int(request.form.get('recommedChol'))
        bmi = int(request.form.get("bmi"))
        smoker = int(request.form.get('recommedSMK'))
        stroke = int(request.form.get('recommedSTK'))
        heartDis = int(request.form.get('recommedHRT'))
        physCal = int(request.form.get('recommedPHYS'))
        drink = int(request.form.get('recommedDRK'))
        genHlth = int(request.form.get('recommedGEN'))
        menHlth = int(request.form.get('mentalHlth'))
        physHlth = int(request.form.get('physHlth'))
        walk = int(request.form.get('recommedWALK'))
        age = int(request.form.get('recommedAGE'))
        edu = int(request.form.get('recommedEDU'))
        inc = int(request.form.get('recommedINC'))
    data = np.array([[highBP, highChol, bmi, smoker, stroke, heartDis, physCal, drink, genHlth, menHlth, physHlth, walk, age, edu, inc]])
    
    prediction = model.predict(data)
    prediction = 'No diabetes' if prediction == 0 else "Diabetes"

    return render_template("index.html", result = prediction)


if __name__ == "__main__":
    app.run(debug=True)