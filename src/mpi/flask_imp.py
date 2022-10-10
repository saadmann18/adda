from flask import Flask, request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)

pickle_in=open('classifier.pkl', 'rb')
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
	return "Welcome All"

#@app.route('/predict')
#def predict_shape_geometry():
#	S11 = request.args.get('S11')
	
	#prediciton = classifier.predict([S11]).reshape(-1, 1)
	#return "The predicted shape is" + str(prediciton)
	#return S11

@app.route('/predict_file', methods=["POST"])
def predict_shape_from_file():
	df_test=pd.read_csv(request.files.get("file"))
	prediction=classifier.predict(df_test)
	return "The predicted shape is" + str(list(prediction))

if __name__ == '__main__':
	app.run()
	print("flask ok")
