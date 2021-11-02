"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template

# Library imports
import json
from flask import Blueprint, render_template, request, jsonify
import datetime as dt
from sqlalchemy import update, and_, or_, not_
from marshmallow import ValidationError
from secrets import token_urlsafe
import bcrypt
import hashlib

# Project imports
from GraffLibAPI.models.enums import *
from GraffLibAPI.models.requests.create_user_request import *
from GraffLibAPI.models.requests.create_city_request import *
from GraffLibAPI.models.responses.create_user_response import *
from GraffLibAPI.models.responses.create_city_response import *
from GraffLibAPI.models.user_model import UserModel
from GraffLibAPI.models.city_model import CityModel
from GraffLibAPI.models.requests.send_password_recovery_email_request import *
from GraffLibAPI.models.requests.update_unauthenticated_user_password_request import *
from GraffLibAPI.models.requests.update_authenticated_user_password_request import *
from GraffLibAPI.database.entities.user.user_entity import *
from GraffLibAPI.database.entities.city_entity import *
from GraffLibAPI.database.entities.user.user_password_reset_entity import *
from GraffLibAPI.database.entities.user.user_password_reset_history_entity import *
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.mappings.mappings import *
from GraffLibAPI.utils.email_sender_helper import *
from GraffLibAPI.utils.user_helper import *

blueprint_views = Blueprint("api-views", __name__, url_prefix="/v1")

@blueprint_views.route("/password", methods=["GET"])
def password_reset_unauthenticated():

    try:
        token = request.args.get("token", default = "no-token", type = str)

        password_reset = session.query(UserPasswordResetEntity).filter_by(token=token).first()
        password_reset_history = session.query(UserPasswordResetHistoryEntity).filter_by(reset_id=password_reset.id).first()

        if password_reset is None or password_reset_history is None:
            raise ValueError("Password reset instance was not found. HttpStatusCode: 404")
        if password_reset_history.reset_iniatiated is None or password_reset_history.reset_completed is not None:
            raise ValueError("Password can't be changed because of the server state. HttpStatusCode: 409")       
    
        return render_template(
            "password-recovery/password-reset-unauthenticated.html",
            title='GraffLib - Password Reset',
            year=datetime.now().year,
        )              
    except Exception as err:        
        return render_template(
            "password-recovery/password-reset-failure.html",
            title='GraffLib - Password Reset',
            year=datetime.now().year,
            reason = str(err)
        )