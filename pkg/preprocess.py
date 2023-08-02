#
# Preliminary cropping & resizing of input images,
# Output is saved to Preprocessed_Images folder in pkg
#
import os
import numpy as np
from PIL import Image
from scipy.ndimage import center_of_mass
from tqdm import tqdm


#
# Main method (called from program.py)
#
def main():
     os.makedirs("Preprocessed_Images", exist_ok = True)
     Input_Images = os.listdir("Input_Images")

     # ignoring unnecessary files
     if '.DS_Store' in Input_Images:
          Input_Images.remove('.DS_Store')
     if 'README.md' in Input_Images:
          Input_Images.remove('README.md')

     # cropping and resizing images around tumor
     for file in tqdm(Input_Images):
          image_path = "Input_Images/" + file.split("/")[-1]
          image = Image.open(image_path).convert('L')

          y, x = center_of_mass(np.asarray(image))
          # can change value of 200 depending on proportion of MRI image that has tumor
          image = image.crop((x-200, y-200, x + 200, y + 200))
          image = image.resize((224, 224))

          new_path = "Preprocessed_Images/" + file.split("/")[-1]
          image.save(new_path, "JPEG")