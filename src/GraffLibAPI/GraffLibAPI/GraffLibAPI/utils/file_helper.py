from pathlib import Path
import os
import os.path as pathh
from secrets import token_urlsafe
import logging
logger = logging.getLogger()


def save_file(file_bytes : bytes, directory : str, unique_image_name : str, file_extension : str):
    file_name_with_extension = unique_image_name + "." + file_extension
    new_file_path = os.path.join(directory, file_name_with_extension)
    logger.warning("SAVING IMAGE TO PATH: " + new_file_path)


    new_file = open(new_file_path, 'wb')
    new_file.write(file_bytes)
    new_file.close()

def get_current_directory(marker_id : str) -> str:
    # "" string creates a new directory!
    full_directory_path = os.path.join(str(Path.cwd()), "GraffLibAPI", "static", "markers", marker_id)
    
    logger.warning("DIRECTORY PATH: " + full_directory_path)
    return full_directory_path

def get_image_full_path(directory : str, image_unique_name : str, file_extension : str):
    file_name_with_extension = image_unique_name + "." + file_extension
    image_full_path = os.path.join(directory, file_name_with_extension)
    
    logger.warning("IMAGE FULL PATH: " + image_full_path)
    return image_full_path

def create_user_image_directory_name():
    return token_urlsafe(16)

def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)