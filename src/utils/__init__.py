import os
import re

import utils.constants as constants


def get_latest_model():
    try:
        regex = re.compile(r"train(\d+)")
        high_number = 1
        latest_model_folder = ""

        with os.scandir(constants.runs_detect_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    match = regex.match(entry.name)
                    if match:
                        number = int(match.group(1))
                        if number > high_number:
                            high_number = number
                            latest_model_folder = entry.name

        return os.path.join(
            constants.runs_detect_path, latest_model_folder, "weights", "last.pt"
        )
    except FileNotFoundError:
        return f"A pasta {constants.runs_detect_path} não foi localizada!"


def get_best_latest_model():
    try:
        regex = re.compile(r"train(\d+)")
        high_number = 1
        latest_model_folder = ""

        with os.scandir(constants.runs_detect_path) as entries:
            for entry in entries:
                if entry.is_dir():
                    match = regex.match(entry.name)
                    if match:
                        number = int(match.group(1))
                        if number > high_number:
                            high_number = number
                            latest_model_folder = entry.name
        return os.path.join(
            constants.runs_detect_path, latest_model_folder, "weights", "last.pt"
        )
    except FileNotFoundError:
        return f"A pasta {constants.runs_detect_path} não foi localizada!"
