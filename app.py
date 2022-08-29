from flask import Flask, request, jsonify,render_template
import util
app = Flask(__name__,template_folder='template',static_folder='static')
@app.route('/')
def home():
    return render_template('app.html')
@app.route('/predict_heart_disease', methods=['POST','GET'])
def predict_heart_disease():
    age = int(request.form['age'])
    sex = request.form['sex']
    cp = request.form['cp']
    trestbps = request.form['trestbps']
    chol = request.form['chol']
    fbs = request.form['fbs']
    restecg = request.form['restecg']
    thalach = request.form['thalach']
    exang = request.form['exang']
    oldpeak = request.form['oldpeak']
    slope = request.form['slope']
    ca = request.form['ca']
    thal = request.form['thal']
    result=util.disease_or_not(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)
    print(result)
    return render_template("app.html",result=result)
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)