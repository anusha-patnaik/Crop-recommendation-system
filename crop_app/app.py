import joblib
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the machine learning model
model = joblib.load('Pickle_RL_Model.pkl')

@app.route('/')
def home():
    return render_template('Home_1.html')

@app.route('/Predict')
def prediction():
    return render_template('Index.html')

@app.route('/form', methods=["POST"])
def brain():
    try:
        # Get form input values
        Nitrogen = float(request.form['Nitrogen'])
        Phosphorus = float(request.form['Phosphorus'])
        Potassium = float(request.form['Potassium'])
        Temperature = float(request.form['Temperature'])
        Humidity = float(request.form['Humidity'])
        Ph = float(request.form['ph'])
        Rainfall = float(request.form['Rainfall'])

        values = [Nitrogen, Phosphorus, Potassium, Temperature, Humidity, Ph, Rainfall]
        
        # Validate input values
        if 0 < Ph <= 14 and Temperature < 100 and Humidity > 0:
            arr = [values]
            acc = model.predict(arr)
            return render_template('prediction.html', prediction=str(acc))
        else:
            return "Sorry... Error in entered values in the form. Please check the values and fill it again."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
