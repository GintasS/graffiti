import os
from flask import Blueprint
from pathlib import Path

from GraffLibAPI.utils.compare_image_helper import compare


# A blueprint is an object very similar to a flask application object, but instead of creating a new one,
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply
# divide services within the same application.
blueprint_comparison = Blueprint('api-image-comparison', __name__, url_prefix='/v1')

@blueprint_comparison.route('', methods=['GET'])
def check_similarity(image_uname1, image_uname2):
    try:
        image1_path = Path(str(Path.cwd()) + "/GraffLibAPI/static/user-images/" + str(user_id) + "/" + str(image_uname1))
        image2_path = Path(str(Path.cwd()) + "/GraffLibAPI/static/user-images/" + str(user_id) + "/" + str(image_uname2))
        # Check image existence
        if os.path.exists(image_uname1) != True or os.path.exists(image_uname2) != True:
            return "Sorry. I cannot find those images...", 404

        status = compare(image_uname1,image_uname2)

    except:
        return "Internal server error.", 500

    return {
        'message': 'The same graffiti',
        'body': status
    }



