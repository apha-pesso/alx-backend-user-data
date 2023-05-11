#!/usr/bin/env python3
'''Basic flask'''
from flask import Flask, abort, jsonify, make_response, request
from sqlalchemy import except_
from auth import Auth

AUTH = Auth()
# Create a flask instance
app = Flask(__name__)


# Create a route
@app.route('/', methods=['GET'], strict_slashes=False)
def first_route():
    '''Return a message'''
    return jsonify({"message": "Bienvenue"})

# Endpoint to register user


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    '''Endpoint to register user'''
    data = request.form
    # data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return jsonify({"message": "email already registered"}), 400

    return jsonify({"email": f"{email}", "message": "user created"})


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    '''Login function'''
    email = request.form.get('email')
    password = request.form.get('password')

    # check password and email validity
    if AUTH.valid_login(email, password):
        # create a session_id with the email
        session_id = AUTH.create_session(email)

        # store session_id in cookie
        response = make_response('response')
        response.set_cookie("session_id", session_id)

        # return json
        return jsonify({"email": f"{email}", "message": "logged in"})
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
