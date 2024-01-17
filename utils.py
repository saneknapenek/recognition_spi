from enum import Enum
from _logging import logger



class Mode(Enum):
    reference = "r"
    previous = "p"


class CameraError(Exception):
    def __init__(self, message: str):
        self.message = message
        logger.error(self.message)
        super().__init__(self.message)
