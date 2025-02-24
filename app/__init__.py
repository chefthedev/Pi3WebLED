# Initializes the Flask application and imports route handlers

from flask import Flask

app = Flask(__name__)

from app import routes 