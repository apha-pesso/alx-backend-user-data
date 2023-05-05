#!/usr/bin/env python3
""" Module of Users views
"""

from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from os import getenv
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_authy() -> str:
    '''Session Authy'''

    # Get the email and password from the request form
    email = request.form.get('email')
    password = request.form.get('password')

    # email validity
    if not email or email == '':
        return jsonify({"error": "email missing"}), 400

    # password validity
    if not password or password == '':
        return jsonify({"error": "password missing"}), 400

    # Retrieve user object with email from post request
    try:
        user = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    user_obj = user[0]
    # Validate password for the boject
    if not user_obj.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Import Auth class
    from api.v1.app import auth

    user_id = user_obj.id

    # Create new session id
    session_id = auth.create_session(user_id)

    # object to json
    user_json = user_obj.to_json()

    # set cookie in response
    response = make_response(user_json)
    session_cookie = getenv('SESSION_NAME')
    response.set_cookie(session_cookie, session_id)
    return response


@app_views.route('/api/v1/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def session_logout() -> str:
    '''Logout'''
    # import
    from api.v1.app import auth

    if auth.destroy_session(request):
        return jsonify({}), 200
    else:
        abort(404)
