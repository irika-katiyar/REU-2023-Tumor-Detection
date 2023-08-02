REU-2023-Tumor-Detection

File structure:<br>
pkg - run program.py to predict tumor w/ visualization<br>
data - includes non-augmented image data<br>
src - includes all code files used in creation of project<br>
files - research paper, graph, references<br>

Steps to use pkg:
1. Place MRI images into folder titled Input_Images
2. Run program.py
3. Predicted masks outputted into folder titled Predicted_Masks
4. View visualization of ground truth w/ predictions in FinalVisualization.jpg,
   which is in the pkg folder

Training information:
1. Data can be augmented for training using aug.py
2. Splitting data into train, test, and valid can be done using ttv_split.py
3. Train the network using train.py, note: if starting with a pretrained model,
   indicate its path on line ___ and uncomment

More:
1. Various graphs can be made using the data, all code can be found in src
   with filenames starting with "graph_"
