from enum import Enum

class RoleType(str, Enum):
    USER = "USER" # A normal user.
    ADMIN = "ADMIN" # A user with privilleged access to the system.