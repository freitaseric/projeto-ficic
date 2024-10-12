import os
from os import path

cwd = os.getcwd()

runs_path = path.join(cwd, "runs")
runs_detect_path = path.join(runs_path, "detect")

dataset_path = path.join(cwd, "dataset")
test_images_path = path.join(dataset_path, "test", "images")
train_images_path = path.join(dataset_path, "train", "images")
validation_images_path = path.join(dataset_path, "valid", "images")

class_names = ["Mobile phone", "People using a mobile phone"]
