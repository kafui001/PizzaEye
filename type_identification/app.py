import os
from flask import Flask, request, jsonify, render_template, redirect
from werkzeug.utils import secure_filename
# added 7/13/20
import numpy as np
import pickle
from fastai import *
from fastai.vision import *
import os
cwd = os.getcwd()
path = cwd + '/model'
# ################
app = Flask(__name__)
# added same day
doneness_model = load_learner(path,'stage_doneness.pkl')
shape_model = load_learner(path,'stage_shape.pkl')
toppings_model = load_learner(path,'stage_topping.pkl')
#toppings_model = pickle.load(open('model/stage_topping.pkl','rb'))
#with open(f'model/stage_topping.pkl', "rb") as f:
 #   toppings_model = pickle.load(f)
 #   toppings_model = load_learner(f)
# #########################
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/result',methods = ['GET', 'POST'])
def result():
    if request.method == "POST":
        if request.files:       
            new_image = request.files["inputfile"]
            # basepath = os.path.dirname(__file__)
            # file_path = os.path.join(basepath, 'static/images', secure_filename(new_image.filename))
            # new_image.save(file_path)   
            path = "static/images"
            file_path = os.path.join(path, secure_filename(new_image.filename))
            new_image.save(file_path) 
            # new_image = request.files["inputfile"]
            # basepath = os.path.dirname(__file__)
            # file_path = os.path.join(basepath, 'static/images', secure_filename(new_image.filename))
            #new_image.save(file_path)
            #reopening saved image(toppings)
            reopened_image = open_image(file_path)
            predict_toppings = toppings_model.predict(reopened_image)
            print(predict_toppings[0])
            toppings = predict_toppings[0]
            toppings_accuracy = str(max(predict_toppings[2]) *100)
            toppings_accuracy = toppings_accuracy.strip('tensor(')
            toppings_accuracy = (toppings_accuracy.strip(').'))
            print(toppings_accuracy)
            #*******************************************************
            #   working on shape model
            #-------------------------------------------------------
            #reopening saved image(shape)
            shape_image = open_image(file_path)
            predict_shape = shape_model.predict(shape_image)
            print(predict_shape[0])
            #------------------------------------------
            shape = predict_shape[0]
            shape_accuracy = str(max(predict_shape[2]) *100)
            shape_accuracy = shape_accuracy.strip('tensor(')
            shape_accuracy = (shape_accuracy.strip(').'))
            print(shape_accuracy)
            #*******************************************************
            #   working on doneness model
            #-------------------------------------------------------
            #reopening saved image(doneness)
            doneness_image = open_image(file_path)
            predict_doneness = doneness_model.predict(doneness_image)
            print(predict_doneness[0])
            #------------------------------------------
            doneness = predict_doneness[0]
            doneness_accuracy = str(max(predict_doneness[2]) *100)
            doneness_accuracy = doneness_accuracy.strip('tensor(')
            doneness_accuracy = (doneness_accuracy.strip(').'))
            print(doneness_accuracy)
            # return render_template('result.html', address = file_path, 
            #                                       toppings = toppings, 
            #                                       toppings_accuracy = toppings_accuracy, 
            #                                       shape = shape,
            #                                       shape_accuracy = shape_accuracy, 
            #                                       doneness = doneness, 
            #                                       doneness_accuracy = doneness_accuracy )
            # image file name and the prediction is this on above line 
            # new_image.save(secure_filename(new_image.filename))                 
            # print(new_image)
    # predict_doneness = doneness_model.predict(new_image)
    # predict_shape = shape_model.predict(new_image)
    # return render_template('result.html', toppings = )
    return render_template('result.html', address = file_path, 
                                                  toppings = toppings, 
                                                  toppings_accuracy = toppings_accuracy, 
                                                  shape = shape,
                                                  shape_accuracy = shape_accuracy, 
                                                  doneness = doneness, 
                                                  doneness_accuracy = doneness_accuracy )
if __name__ == '__main__':
    app.run(debug=True)