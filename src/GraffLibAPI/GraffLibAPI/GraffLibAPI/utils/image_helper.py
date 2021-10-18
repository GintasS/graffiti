def create_image_unique_url(unique_image_name : str, extension : str) -> str:
    return "http://localhost:8000/user-images/" + unique_image_name + "." + extension