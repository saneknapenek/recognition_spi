from environs import Env



env = Env()
env.read_env()

PATH1 = env('PATH1')
PATH2 = env('PATH2')
SAVE_DIRECTORY = env('SAVE_DIRECTORY')