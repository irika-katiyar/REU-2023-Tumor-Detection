#
# Predict alive tumor area
#

import matplotlib.pyplot as plt
import os, cv2, glob, skimage
import numpy as np
import mahotas as mh
from PIL import Image
from tensorflow import keras as kr


#
# Helper function used to perform intensity normalization
# on an image, given min & max threshold value
#
def histNormal(image, min, max):
     image = np.asarray(image).astype(float)
     image = (image - min) / (max - min) * 255
     return np.clip(image, 0, 255)


#
# Predict alive tumor mask, result goes in "Predicted_Masks"
#
def predict():
     paths = glob.glob("Preprocessed_Images/*.jpg")
     os.makedirs("Predicted_Masks", exist_ok=True)
     os.chdir("src/")
     model = kr.models.load_model(os.path.abspath("model.h5"))
     os.chdir("..")

     for path in paths:
          image = cv2.imread(path,0).astype(np.uint8)
          reshape = np.expand_dims([image],axis = 3)
          pred = model.predict(reshape)[0]
          _,pred = cv2.threshold(pred,.3,255,cv2.THRESH_BINARY)

          new_path = os.getcwd() + "/Intermediate_Masks/" + path.split("/")[-1]
          cv2.imwrite(new_path,pred)


#
# Main method (called from program.py)
#
def main():
     predict()