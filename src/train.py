import os

from ultralytics import YOLO

import utils
from utils import constants

model = None

try:
    model = YOLO(utils.get_best_latest_model())
except FileNotFoundError:
    model = YOLO(os.path.join(constants.cwd, "yolo11n.pt"))

model.train(data=os.path.join(constants.dataset_path, "data.yaml"))
