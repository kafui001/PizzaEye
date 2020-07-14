from flask import Flask, request, jsonify, render_template, redirect
# added 7/13/20

# import numpy as np
# import pickle
# from fastai import *
# from fastai.vision import *
# import os


# cwd = os.getcwd()
# path = cwd + '/model'

# ################
app = Flask(__name__)

# added same day
# doneness_model = load_learner(path,'stage_doneness.pkl')
# shape_model = load_learner(path,'stage_shape.pkl')
# toppings_model = load_learner(path,'stage_topping.pkl')

# #########################
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result',methods = ['GET', 'POST'])
def result():
    if request.method == "POST":
        if request.files:
            new_image = request.files["inputfile"]
            print(new_image)
    

    # predict_doneness = doneness_model.predict(new_image)
    # predict_shape = shape_model.predict(new_image)
    # predict_toppings = toppings_model.predict(new_image)

    # return render_template('result.html',shape = , doneness = , toppings = )
    return render_template('result.html')
if __name__ == '__main__':
    app.run()