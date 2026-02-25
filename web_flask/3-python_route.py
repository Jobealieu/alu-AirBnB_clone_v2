#!/usr/bin/python3
"""Flask app with optional dynamic route /python/(<text>)."""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display Hello HBNB! at the root route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display HBNB at the /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display C followed by text with underscores replaced by spaces."""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """Display Python followed by text; defaults to 'is cool' if no text."""
    return 'Python {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
