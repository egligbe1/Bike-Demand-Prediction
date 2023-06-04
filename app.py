import numpy as np
import pickle
from xgboost import XGBRegressor
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = np.array(int_features).reshape(1, -1)
    prediction = model.predict(final_features)

    output = round(prediction[0])

    return render_template('index.html', prediction_text='Expected number of bikes is {}'.format(output),
                           disclaimer='Disclaimer: This prediction is based on the demand nature of past data and may not represent the actual current demand.')


if __name__ == "__main__":
    app.run(debug=True)
