#!/usr/bin/python3
"""A minimal Flask web application that displays Hello HBNB! at the root."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a Hello HBNB! greeting at the root route."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
