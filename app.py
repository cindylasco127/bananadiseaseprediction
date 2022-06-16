# -*- coding: utf-8 -*-
"""banana-disease.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/13CF_ITlv3WCmA00qUPpz2n7ysK0mo9AG
"""

# from google.colab import drive
# drive.mount('/content/drive')

import streamlit as st
from PIL import Image
# import matplotlib.pyplot as plt
# import tensorflow_hub as hub
import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.models import *
from tensorflow.keras import preprocessing
import time



## this is part of web app

## ----------------------------------------------- x -----------------------------------------x-------------------------x------------------##


# fig = plt.figure()

st.title('Banana Disease Classifier')

st.markdown("Prediction of the Banana Diseases: Bunchy Top, Moko, Sigatoka and Fusarium Wilt")

def main():
    file_uploaded = st.file_uploader("Select Image", type=["png","jpg","jpeg"])
    class_btn = st.button("Classify")
    if file_uploaded is not None:    
        image = Image.open(file_uploaded)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        
    if class_btn:
        if file_uploaded is None:
            st.write("Invalid command, please upload an image")
        else:
            with st.spinner('Model working....'):
                # plt.imshow(image)
                # plt.axis("off")

                predictions = predict(image)

                time.sleep(1)
                st.success('Classified')
                st.write(predictions)



## This code is for saved model in format as H5 file


def predict(image):
     classifier_model = "classify-vgg19-model-final.h5"
      
     model = load_model(classifier_model)
      
     test_image = image.resize((224,224))
     test_image = preprocessing.image.img_to_array(test_image)
     test_image = test_image / 255.0
     test_image = np.expand_dims(test_image, axis=0)
     class_names = {0 : 'healthy', 1 : 'bunchy top', 2 : 'fusarium wilt', 3 : 'moko', 4 : 'sigatoka'}

     predictions = model.predict(test_image)
     scores = tf.nn.softmax(predictions[0])
     scores = scores.numpy()

    
     result = f"{class_names[np.argmax(scores)]} with a { (100 * np.max(scores)).round(2) } % confidence." 
     return result


## -----------------------------------------------------x---------------------------------------x--------------------------------------------##


## this code for format tflite file
# def predict(image):
#    model = "classify-vgg19-model-final.h5" 


#    interpreter = tf.lite.Interpreter(model_path = model)
#   interpreter.allocate_tensors()
#    input_details = interpreter.get_input_details()
#    output_details = interpreter.get_output_details()
    
#    input_shape = input_details[0]['shape']
#    image = np.array(image.resize((200,200)), dtype=np.float32) 
    
#    image = image / 255.0
#    image = np.expand_dims(image, axis=0)

#    interpreter.set_tensor(input_details[0]['index'], image)
#    interpreter.invoke()
#    output_data = interpreter.get_tensor(output_details[0]['index'])
#    probabilities = np.array(output_data[0])

#    labels = {0 : "healthy", 1 : "bunchy top", 2 : "fusarium wilt", 3 : "moko", 4 : "sigatoka"} 

#    label_to_probabilities = []

#    for i, probability in enumerate(probabilities):
#        label_to_probabilities.append([labels[i], float(probability)])
    
#    sorted(label_to_probabilities, key=lambda element: element[1])

#    result = { 'healthy' : 0 , 'bunchy top' : 0 , 'fusarium wilt' : 0 , 'moko' : 0 , 'sigatoka' : 0}
    
#    result = f"{label_to_probabilities[np.argmax(probability)][0]} with a { (100 * np.max(probabilities)).round(2)} % confidence." 
    
#   return result



if __name__ == "__main__":
    main()
