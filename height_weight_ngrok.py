# -*- coding: utf-8 -*-
"""height-weight-ngrok.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dgUJsCgXAaGSs6H_xxRYG41oVy0Jb7P-
"""

import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('weight_pred_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/getprediction', methods=['POST'])
def getprediction():
    input = [float(x) for x in request.form.values()]
    final_input = [np.array(input)]
    prediction = model.predict(final_input)

    return render_template('index.html', output='Predicted Weight in KGs :{}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)