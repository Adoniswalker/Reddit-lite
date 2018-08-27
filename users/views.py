from flask_jwt_extended import (create_access_token, create_refresh_token,
jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt,)
from flask_jwt_extended import JWTManager


def register(username, password)

    USER_LIST = UserModel.get_all_users()

    exists = validator.check_if_user_exists(
        USER_LIST, data['username'], data['email'])

    if exists:
        message = dict(message="Error", body="Sorry, this user already exists")
        return message

    create_user = UserModel.register(username, password)

    message = dict(message="Success", body="User registered Successfully")

def login(username, password):
    check_if_user_exists = UserModel.check_if_exists(username)

    if not check_if_user_exists:
        message = dict(message="Error", body="Sorry, that username doesnt exist")
        return message

    user_check = UserModel.find_by_username(
        data['username'], data['password'])


    if user_check:
        access_token = create_access_token(identity = user_check, expires_delta=False)
        save_token =  UserModel.save_token(access_token)

        message=dict(message="Success", body="Login successful")
        return message

    message = dict(message="Error", body="Sorry, wrong credentials")
    return message

def post_comment(body):

    post_comment = CommentModel.save_comment(body)

    if post_comment:
        return dict(message="Success", body="Message posted successfully")
