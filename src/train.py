import os

from ultralytics import YOLO

import utils
from utils import constants

model = YOLO(utils.get_best_latest_model())

model.train(data=os.path.join(constants.dataset_path, "data.yaml"))
