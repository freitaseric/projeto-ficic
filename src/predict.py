import os

from ultralytics import YOLO

import utils
from utils import constants

model = YOLO(utils.get_best_latest_model())

images = os.scandir(constants.test_images_path)

for image in images:
    image_path = os.path.join(constants.test_images_path, image.name)
    results = model(image_path)

    for result in results:
        result.save(filename=os.path.join(constants.cwd, "predictions", image.name))
