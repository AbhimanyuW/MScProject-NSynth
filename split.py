import splitfolders

# Set the paths for your input dataset and output folders
input_folder = '/Users/abhimanyuwadhwa/Desktop/QMUL/MScProject/DataSet/nsynth-train-all'
output_folder = '/Users/abhimanyuwadhwa/Desktop/QMUL/MScProject/DataSet/nsynth-split'

split_ratios = (0.7, 0.2, 0.1)  # Train, validate, test

# Use the split-folders library to perform the split
splitfolders.ratio(input_folder, output_folder, seed=42, ratio=split_ratios, group_prefix=None)
