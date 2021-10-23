# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields
from marshmallow import post_load
from GraffLibAPI.models.user_model import UserModel, UserModelSchema
from GraffLibAPI.models.image_models.image_metadata_model import ImageMetadataModelSchema
from GraffLibAPI.models.image_models.image_location_model import ImageLocationModelSchema
from GraffLibAPI.models.image_models.image_classification_model import ImageClassificationModelSchema
from GraffLibAPI.configuration.constants import *


class CreateUserImageResponse():
    def __init__(self, image_unique_name, url, image_metadata_model, image_classification_model):
       self.image_unique_name = image_unique_name
       self.url = url
       self.image_metadata_model = image_metadata_model
       self.image_classification_model = image_classification_model

# Note that besides the User class, 
# we also defined a UserSchema. 
# We will use the latter to deserialize and serialize instances of User 
# from and to JSON objects.

# **kwargs absorbs unmatched fields.

class CreateUserImageResponseSchema(Schema):
    image_unique_name = fields.Str(min=IMAGE_UNIQUE_NAME_MIN_LENGTH,max=IMAGE_UNIQUE_NAME_MAX_LENGTH)
    url = fields.URL(min=IMAGE_UNIQUE_URL_MAX_LENGTH,max=IMAGE_UNIQUE_URL_MAX_LENGTH, relative=False)
    image_metadata_model = fields.Nested(ImageMetadataModelSchema(exclude=['original_image_name']))
    image_classification_model = fields.Nested(ImageClassificationModelSchema())