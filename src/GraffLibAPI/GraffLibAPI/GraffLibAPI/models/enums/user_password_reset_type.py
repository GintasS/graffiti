from enum import Enum

class UserPasswordResetType(str, Enum):
    UNAUTHENTICATED = "UNAUTHENTICATED" # Requesting password reset as an unauthenticated user.
    AUTHENTICATED = "AUTHENTICATED" # Requesting password reset as authenticated user.