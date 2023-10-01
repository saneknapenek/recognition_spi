from enum import Enum



class Mode(Enum):
    reference = "r"
    previous = "p"


class CameraError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
