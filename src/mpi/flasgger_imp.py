# flask postman ml app

import pickle
from flask import Flask, request
import pandas as pd
import flasgger
from flasgger import Swagger


app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


@app.route('/')
def welcome():
    """Welcome page

    Returns:
            _type_: Welcome page
    """
    return "Welcome All"

# @app.route('/predict')
# def predict_shape_geometry():
#	S11 = request.args.get('S11')

    # prediciton = classifier.predict([S11]).reshape(-1, 1)
    # return "The predicted shape is" + str(prediciton)
    # return S11
# The prediction data is in list format, so the whole file is transferred for prediction in
# next funciton


@app.route('/predict_file', methods=["POST"])
def predict_shape_from_file():
    """Let's predict some geometric shapes
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: ture

    responses:
        200:
            description: The output values
    """
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction = classifier.predict(df_test)
    return "The predicted shape is" + str(list(prediction))


if __name__ == '__main__':
    app.run()
