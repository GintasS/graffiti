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
from GraffLibAPI.models.responses.create_user_response import *
from GraffLibAPI.models.user_model import UserModel
from GraffLibAPI.models.requests.send_password_recovery_email_request import *
from GraffLibAPI.models.requests.update_unauthenticated_user_password_request import *
from GraffLibAPI.models.requests.update_authenticated_user_password_request import *
from GraffLibAPI.database.entities.user.user_entity import *
from GraffLibAPI.database.entities.user.user_password_reset_entity import *
from GraffLibAPI.database.entities.user.user_password_reset_history_entity import *
from GraffLibAPI.database.db_setup import session
from GraffLibAPI.mappings.mappings import *
from GraffLibAPI.utils.email_sender_helper import *
from GraffLibAPI.utils.user_helper import *

# A blueprint is an object very similar to a flask application object, but instead of creating a new one, 
# it allows the extension of the current application.

# This might be useful if you want to create multiple versions of an API or simply 
# divide services within the same application.
blueprint_users = Blueprint("api-users", __name__, url_prefix="/v1/users")

@blueprint_users.route("", methods=["POST"])
def create_user():
    try:
        user_request = CreateUserRequestSchema().load(request.get_json())
        found_user = session.query(UserEntity).\
            filter(
                or_(
                    UserEntity.user_name.like(user_request.user_name),
                    UserEntity.email.like(user_request.email)
                )
            ).\
            first()

        if found_user is not None:
            return "User already exists", 409

        # Hash password.
        encoded_password = user_request.password.encode("utf-8")
        user_request.password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

        new_user = to_user_entity(user_request)
        session.add(new_user)
        session.commit()

        return { "body": CreateUserResponseSchema().dump(to_create_user_response(new_user)) }, 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500
 
@blueprint_users.route("/password-recovery", methods=["PATCH"])
def send_password_recovery_email():
    try:
        email_request = SendPasswordRecoveryEmailRequestSchema().load(request.get_json())
        found_user = session.query(UserEntity).filter_by(email = email_request.email).first()

        if found_user is None:
            return "User was not found.", 404
        if is_admin(found_user):
            return "This user does not support password reset.", 409

        # Creating an email to send.
        reset_token = token_urlsafe(32)
        password_reset_link = create_password_reset_url(reset_token)
        email_message = create_password_recovery_email(email_request.email, password_reset_link)

        # Sending an email.
        email_credentials = get_email_credentials()
        send_email(email_message, email_credentials)

        # Adding password reset entities to DB.
        password_reset_type = UserPasswordResetType.UNAUTHENTICATED

        password_reset = create_user_password_reset_entity(found_user.id, password_reset_type, reset_token)
        session.add(password_reset)
        session.commit()
           
        password_reset_history = create_user_password_reset_history_entity(password_reset_type, password_reset.id)
        session.add(password_reset_history)      
        session.commit()

        return "", 202
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as err:
        print(err.message)
        return "Internal server errror.", 500

@blueprint_users.route("/password", methods=["POST"])
def update_user_password_after_recovery_email():
    try:
        password_request = UpdateUnauthenticatedUserPasswordRequestSchema().load(request.form)
        password_reset = session.query(UserPasswordResetEntity).filter_by(token=password_request.token).first()
        password_reset_history = session.query(UserPasswordResetHistoryEntity).filter_by(reset_id=password_reset.id).first()
        found_user = session.query(UserEntity).filter_by(id=password_reset.user_id).first()

        # TODO: [SECURITY] Are we exposing sensitive exception data to the user?
        if password_reset is None or password_reset_history is None:
            raise ValueError("Password reset instance was not found. HttpStatusCode: 404")
        if found_user is None:
            raise ValueError("User was not found. HttpStatusCode: 404")
        if is_admin(found_user):
            raise ValueError("Password can't be changed because of the server state. HttpStatusCode: 409")
        if password_reset_history.reset_iniatiated is None or password_reset_history.reset_completed is not None:
            raise ValueError("Password can't be changed because of the server state. HttpStatusCode: 409")

        # Not checking if the new password is the same as the old one because of security.

        # Get current time.
        current_time = dt.datetime.now()

        # Calculate time difference between password reset request and completion (this request).
        tdelta = abs(current_time-password_reset_history.reset_iniatiated).seconds / 3600
        if tdelta > 1:
            raise ValueError("Password can't be changed because of the server state. HttpStatusCode: 409")

        # Add completion data to password reset instance.
        password_reset_history.reset_completed = current_time

        # Reset the password by hashing it via bcrypt.
        encoded_password = password_request.new_password.encode("utf-8")
        found_user.password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

        session.commit()

        return render_template(
            "password-recovery/password-reset-success.html",
            title="GraffLib - Password Reset Success",
            year=dt.datetime.now().year,
        )
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as err:
        return render_template(
            "password-recovery/password-reset-failure.html",
            title="GraffLib - Password Reset Failure",
            year=dt.datetime.now().year,
            reason = str(err)
        )

@blueprint_users.route("/password", methods=["PUT"])
def update_user_password_user_is_authenticated():
    try:
        password_request = UpdateAuthenticatedUserPasswordRequestSchema().load(request.get_json())
        
        # TODO: [OAuth] Check if the you're changing password for the same user who is authenticated.
        # If not, return 422.

        found_user = session.query(UserEntity).filter_by(id=password_request.user_id).first()

        # TODO: [SECURITY] Check if the user password changing algorithm is secure, we are not missing something.
        if found_user is None:
            return "User was not found.", 404

        encoded_old_password = password_request.old_password.encode("utf-8")
        if bcrypt.checkpw(encoded_old_password, found_user.password) == False:
            return "The old password is incorrect.", 409
        if password_request.old_password == password_request.new_password:
            return "The new password and the old password should not be the same.", 409

        # Change user's password.
        encoded_password = password_request.new_password.encode("utf-8")
        found_user.password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())

        reset_token = token_urlsafe(32)
        user_password_reset_entity = create_user_password_reset_entity(found_user.id, UserPasswordResetType.AUTHENTICATED, reset_token)

        session.add(user_password_reset_entity)
        session.commit()

        # Add already completed(time wise) password reset history instance.
        password_change_history = create_user_password_reset_history_entity(UserPasswordResetType.AUTHENTICATED, user_password_reset_entity.id)

        session.add(password_change_history)
        session.commit()

        return "", 204
    except ValidationError as err:
        return jsonify(err.messages), 400
    except:
        return "Internal server errror.", 500