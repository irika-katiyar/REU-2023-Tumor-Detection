#
# Visualize the algorithm's already-predicted mask to establish ground truth
#

from PIL import Image
import os
import glob
import cv2 as cv
import numpy as np


#
# Helper function which returns contours given a mask
#
def contour(image1, name):
    # predicted mask
    image2 = cv.imread('Predicted_Masks/' + name + '.jpg')
    
    # convert mask image to grayscale and then binary image for correct format for findContours
    image2 = cv.cvtColor(image2, cv.COLOR_BGR2GRAY)
    image2 = np.where(image2 > 100, 255, image2)
    image2 = np.where(image2 <= 100, 0, image2)

    # find contours of image2 (mask)
    contours, hierarchy = cv.findContours(image2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # making new image copy of image1 (original MRI)
    new_image = Image.new('RGB',(224, 224), (250,250,250))
    new_image.paste(image1, (0, 0))

    # draw contours of mask on new_image
    new_image = np.asarray(new_image)
    cv.drawContours(new_image, contours, -1, (255,0,0), 1)

    # convert back to image and save
    new_image = Image.fromarray(new_image, "RGB")
    return new_image, contours


#
# Main method (called from program.py)
#
def main():
    paths = [f for f in glob.glob("Predicted_Masks/*.jpg") if "final" not in f]
    paths.sort(key = lambda s : int(s.split('.')[1]))    

    # we know each image is 224 x 224 (since it was preprocessed this way)
    # adding a small 1 pixel border between images
    img_size, border = 224, 1
    length, width = 2, len(os.listdir("Input_Images"))

    # creating empty image for final visualization
    dimensions = width * (img_size + border), img_size*length + border*(length-1)
    merged_image = Image.new('RGB', dimensions, (250,250,250))

    for i in range(len(paths)):
        name = paths[i].split("/")[-1]
        name = name.split(".")[0] + "." + name.split(".")[1]
        
        # read preprocessed and final mask image
        image1 = Image.open('Preprocessed_Images/' + name + '.jpg')

        # creating contoured image
        new_image = Image.new('RGB',(img_size, length*img_size + (length-1)*border), (250,250,250))
        image3, contours = contour(image1, name)
        
        # pasting all images
        new_image.paste(image1,(0,0))
        new_image.paste(image3,(0, img_size + border))
        
        # at this point, we have one image (actual above predicted) for one slice
        # paste new_image with merged_image
        if i == 0:
            merged_image.paste(new_image, (0, 0))
        else:
            merged_image.paste(new_image, ((img_size + border)*i + border, 0))

    # save final visualization
    merged_image.save("FinalVisualization.jpg","JPEG")