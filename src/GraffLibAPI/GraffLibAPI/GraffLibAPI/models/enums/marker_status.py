from enum import Enum

class MarkerStatus(str, Enum):
    ACTIVE = "ACTIVE"   # Marker is active.
    DISABLED = "DISABLED" # Marker is disabled and is not displayed on the map/greyed out.