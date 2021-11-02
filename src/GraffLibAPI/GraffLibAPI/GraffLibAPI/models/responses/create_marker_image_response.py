# Marshmallow is a popular Python package for converting complex datatypes, such as objects, to and from native Python datatypes.
from marshmallow import Schema, fields, validate, ValidationError
from marshmallow import post_load
from GraffLibAPI.models.user_model import UserModel, UserModelSchema
from GraffLibAPI.models.image.image_metadata_model import ImageMetadataModelSchema
from GraffLibAPI.models.image.image_location_model import ImageLocationModelSchema
from GraffLibAPI.models.image.image_classification_model import ImageClassificationModelSchema
from GraffLibAPI.configuration.constants import *
from GraffLibAPI.models.enums.graffiti_status import GraffitiStatus
from marshmallow_enum import EnumField

class CreateMarkerImageResponse():
    def __init__(self, image_unique_name, graffiti_status, user_id, image_metadata_model, image_classification_model):
       self.image_unique_name = image_unique_name
       self.graffiti_status = graffiti_status
       self.user_id = user_id
       self.image_metadata_model = image_metadata_model
       self.image_classification_model = image_classification_model

# Note that besides the User class, 
# we also defined a UserSchema. 
# We will use the latter to deserialize and serialize instances of User 
# from and to JSON objects.

# **kwargs absorbs unmatched fields.

class CreateMarkerImageResponseSchema(Schema):
    image_unique_name = fields.Str(required=True, validation=validate.Length(ImageValidation.IMAGE_UNIQUE_NAME_MIN_LENGTH, ImageValidation.IMAGE_UNIQUE_NAME_MAX_LENGTH, error=ImageValidation.IMAGE_UNIQUE_NAME_VALIDATION_MSG))
    graffiti_status = EnumField(GraffitiStatus, required=True)
    user_id = fields.Int(required=True)
    image_metadata_model = fields.Nested(nested=ImageMetadataModelSchema(exclude=['original_image_name']), required=True)
    image_classification_model = fields.Nested(nested=ImageClassificationModelSchema(), required=True)