#!/usr/bin/env python3
'''Basic flask'''
from flask import Flask, jsonify, request
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
