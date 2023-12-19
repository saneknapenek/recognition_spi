import os
from environs import Env
from utils import Mode

from _logging import logger



env = Env()
env.read_env(path="settings.env")

SAVE_PATH = env('SAVE_PATH')
if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)
if not os.path.isdir(SAVE_PATH):
    _except = f"\"{SAVE_PATH}\" is not a directory"
    logger.critical(msg=_except)
    exit(1)

REFERENCE_IMAGE = env('REFERENCE_IMAGE')
if not os.path.exists(SAVE_PATH):
    _except = f"\"{REFERENCE_IMAGE}\" not found"
    logger.critical(msg=_except)
    exit(1)

try:
    SENSITIVITY = int(env('SENSITIVITY'))
    CAMERA_INDEX = int(env('CAMERA_INDEX'))
    INTERVAL = int(env('INTERVAL'))
    MODE = Mode(env('MODE'))
except ValueError as _except:
    logger.critical(msg=_except.__str__())
    exit(1)


if SENSITIVITY > 15 or SENSITIVITY < 5:
    _except = f"Sensitivity cannot be {SENSITIVITY}. Sensitivity should be in the range [5, 15]."
    logger.critical(msg=_except)
    exit(1)
