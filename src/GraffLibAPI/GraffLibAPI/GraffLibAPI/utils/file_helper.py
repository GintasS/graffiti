from pathlib import Path
import os
import os.path as pathh
from secrets import token_urlsafe

def save_file(file_bytes : bytes, directory : str, unique_image_name : str, file_extension : str):
    new_file = open(str(directory) + "/" + unique_image_name + "." + file_extension, 'wb')
    new_file.write(file_bytes)
    new_file.close()

def get_current_directory(user_id : int) -> str:
    return Path(str(Path.cwd()) + "/GraffLibAPI/static/user-images/" + str(user_id) + "/")

def create_user_image_directory_name():
    return token_urlsafe(16)

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)