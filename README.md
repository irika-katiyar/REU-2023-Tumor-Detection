REU-2023-Tumor-Detection

File structure:<br>
pkg - run program.py to predict tumor w/ visualization<br>
data - includes non-augmented image data<br>
src - includes all code files used in creation of project<br>
files - research paper, graph, references<br>

Training information:
1. Data can be augmented for training using augmentation.ipynb
2. Splitting data into train, test, and valid can be done using ttv_split.ipynb
3. Train the network using train.py, note: if starting with a pretrained model,<br>
   indicate its path under the "INITIALIZING FILES ETC" section and uncomment

More:
1. Various graphs can be made using the data, all code can be found in src/graphs
