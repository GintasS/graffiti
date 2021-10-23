# Library includes.
from marshmallow import post_load
from marshmallow import Schema, fields, validate, ValidationError

# Project includes.
from GraffLibAPI.models.image_models.image_model import ImageModel, ImageModelSchema
from GraffLibAPI.models.image_models.image_metadata_model import ImageMetadataModel, ImageMetadataModelSchema
from GraffLibAPI.models.image_models.image_classification_model import ImageClassificationModel, ImageClassificationModelSchema
from GraffLibAPI.models.image_models.image_location_model import ImageLocationModel, ImageLocationModelSchema

class CreateUserImageRequest():
    def __init__(self, image_classification_model, user_id):
        self.image_classification_model = image_classification_model
        self.user_id = user_id

    def __repr__(self):
        return '<CreateUserImageRequest(name={self.user_id!r})>'.format(self=self)

# TODO: Remove unused comments.