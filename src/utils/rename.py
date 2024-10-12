import os

import utils.constants as constants

images_path = os.path.join(constants.cwd, "..", "..", "Imagens")

images = os.scandir(images_path)
num = 1

for image in images:
    if image.is_file():
        os.rename(
            os.path.join(images_path, image.name),
            os.path.join(images_path, f"image{num}.jpg"),
        )
        num += 1
