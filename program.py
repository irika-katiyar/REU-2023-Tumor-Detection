#
# Final program which predicts tumor w/ nice visualization,
# Simply drag your MRI images into Input_Images and run this file.
#


# Navigating to Package folder
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
import preprocess, predict_tumor, final_visualization
os.chdir("..")

# Step 1: preprocess images, result goes into "Preprocessed_Images"
print("Preprocessing images...")
preprocess.main()

# Step 2: predict alive tumor mask, result goes in "Predicted_Masks"
print("Predicting tumor...")
predict_tumor.main()

# Step 3: display results as a nice visualization
print("Saving final visualization...")
final_visualization.main()
print("Done!")