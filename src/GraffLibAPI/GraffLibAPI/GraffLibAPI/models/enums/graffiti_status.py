from enum import Enum

class GraffitiStatus(str, Enum):
    ACTIVE = "ACTIVE" # Graffiti has photos from the last 3 months.
    HIDDEN = "HIDDEN" # Graffiti was hidden.
    UNKNOWN = "UNKNOWN" # Graffiti does not have photos from the last year.