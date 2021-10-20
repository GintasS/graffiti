from enum import Enum

# TODO: Rename this file to be role_type. Update all imports of it in other files.

# The code of the enumerator is quite simple. 
# It just defines a class called RoleType that inherits from Enum 
# and that defines two types: 
# USER and ADMIN.
class RoleType(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"