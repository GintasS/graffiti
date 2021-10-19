from enum import Enum

# The code of the enumerator is quite simple. 
# It just defines a class called RoleType that inherits from Enum 
# and that defines two types: 
# USER and ADMIN.
class RoleType(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"