from time import sleep
from datetime import datetime

import cv2

from env import (SENSITIVITY, REFERENCE_IMAGE, INTERVAL,
                 MODE, CAMERA_INDEX, SAVE_PATH)
from hashing import pHash, hamming_dist
from utils import Mode, CameraError
from _logging import logger



logger.info(f"START IN MODE {MODE.name.upper()}")

reference_frame = cv2.imread(REFERENCE_IMAGE)

while True:
    
    camera = cv2.VideoCapture(CAMERA_INDEX)
    if not camera.isOpened():
        _except = CameraError("The camera was not found or could not be opened.")
        logger.critical(msg=_except.message)
        raise _except
    
    ret, current_frame = camera.read()
    if not ret:
        _except = CameraError("Unable to count frame.")
        logger.critical(msg=_except.message)
        raise _except
    
    reference_hash = pHash(reference_frame)
    current_hash = pHash(current_frame)

    hDist = hamming_dist(reference_hash, current_hash)
    if hDist > SENSITIVITY:
        name = f"{SAVE_PATH}C{CAMERA_INDEX}D{datetime.now().date()}T{datetime.now().time()}.jpg"
        if MODE == Mode.reference:
            cv2.imwrite(name, current_frame)

            logger.warning(f"Difference found. The file is written as \"{name}\" to the directory \"{SAVE_PATH}\"")     
        else:
            cv2.imwrite(f"{name}_reference", reference_frame)
            cv2.imwrite(f"{name}_current", current_frame)

            logger.warning(f"Difference found. The files are written as \
                           \n\"{name}_reference\"\n\"{name}_current\"\nto the directory \"{SAVE_PATH}\"")
    else:
        logger.info("No differences found.")

    camera.release()

    if MODE == Mode.previous:
        reference_frame = current_frame
    sleep(INTERVAL)
