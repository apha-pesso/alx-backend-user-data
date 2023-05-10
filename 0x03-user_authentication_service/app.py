#!/usr/bin/env python3
'''Basic flask'''
from flask import Flask, jsonify

# Create a flask instance
app = Flask(__name__)


# Create a route
@app.route('/', methods=['GET'], strict_slashes=False)
def first_route():
    '''Return a message'''
    return jsonify({"message": "Bienvenue"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
