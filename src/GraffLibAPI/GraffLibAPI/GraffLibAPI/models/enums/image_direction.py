from enum import Enum

class ImageDirection(str, Enum):
    FRONT = "FRONT" # more or less at 180 degrees
    ANGLE = "ANGLE" # anything else than 180 degrees