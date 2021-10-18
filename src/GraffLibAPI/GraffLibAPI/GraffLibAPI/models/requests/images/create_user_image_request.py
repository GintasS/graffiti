# Library includes.
from marshmallow import post_load

# Project includes.
from GraffLibAPI.models.image_models.image_model import ImageModel, ImageModelSchema
from GraffLibAPI.models.image_models.image_metadata_model import ImageMetadataModel, ImageMetadataModelSchema
from GraffLibAPI.models.image_models.image_classification_model import ImageClassificationModel, ImageClassificationModelSchema
from GraffLibAPI.models.image_models.image_location_model import ImageLocationModel, ImageLocationModelSchema

class CreateUserImageRequest(ImageModel):
    def __init__(self, image_metadata_model, image_classification_model):

        # TODO: Fix this manual mapping in this request and in ImageLocationSchema.
        image_metadata_model_object = ImageMetadataModel(image_metadata_model["extension"], image_metadata_model["photographed_time"], image_metadata_model["upload_time"], ImageLocationModel(image_metadata_model["image_location_model"]["coordinates"]))
        image_classification_model_object = ImageClassificationModel(image_classification_model["user_provided_name"], image_classification_model["description"], image_classification_model["graffiti_object"], image_classification_model["image_direction"])

        super(CreateUserImageRequest, self).__init__("", "", image_metadata_model_object, image_classification_model_object)

    def __repr__(self):
        return '<CreateUserImageRequest(name={self.user_id!r})>'.format(self=self)

# TODO: Remove unused comments.


# Note that besides the User class, 
# we also defined a UserSchema. 
# We will use the latter to deserialize and serialize instances of User 
# from and to JSON objects.

# **kwargs absorbs unmatched fields.
class CreateUserImageRequestSchema(ImageModelSchema):
    @post_load
    def make_create_user_image_request(self, data, **kwargs):
        return CreateUserImageRequest(**data)
