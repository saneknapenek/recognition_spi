import os
from environs import Env
from utils import Mode

from _logging import logger



env = Env()
env.read_env(path="settings.env")

SAVE_PATH = env('SAVE_PATH')
if not os.path.exists("SAVE_PATH"):
    os.makedirs("SAVE_PATH")
if not os.path.isdir(SAVE_PATH):
    _except = ValueError(f"\"{SAVE_PATH}\" is not a directory")
    logger.critical(msg=_except.__str__())
    raise _except

REFERENCE_IMAGE = env('REFERENCE_IMAGE')
if os.path.isdir(SAVE_PATH):
    _except = ValueError(f"\"{REFERENCE_IMAGE}\" is a directory")
    logger.critical(msg=_except.__str__())
    raise _except

try:
    SENSITIVITY = int(env('SENSITIVITY'))
    CAMERA_INDEX = int(env('CAMERA_INDEX'))
    INTERVAL = int(env('INTERVAL'))
    MODE = Mode(env('MODE'))
except ValueError as _except:
    logger.critical(msg=_except.__str__())
    raise _except


if SENSITIVITY > 15 or SENSITIVITY < 5:
    _except = ValueError(f"Sensitivity cannot be {SENSITIVITY}. Sensitivity should be in the range [5, 15].")
    logger.critical(msg=_except.__str__())
    raise _except
