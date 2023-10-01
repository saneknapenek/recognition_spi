from environs import Env
from utils import Mode



env = Env()
env.read_env(path="settings.env")

SAVE_PATH = env('SAVE_PATH')
SENSITIVITY = int(env('SENSITIVITY'))
REFERENCE_IMAGE = env('REFERENCE_IMAGE')
CAMERA_INDEX = int(env('CAMERA_INDEX'))
INTERVAL = int(env('INTERVAL'))
MODE = Mode(env('MODE'))


if SENSITIVITY > 15 or SENSITIVITY < 5:
    raise ValueError(f"Sensitivity cannot be {SENSITIVITY}. Sensitivity should be in the range [5, 15].")
