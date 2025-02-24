# Initializes the Flask application with the proper template directory and imports the route handlers

from flask import Flask

app = Flask(__name__, template_folder='../templates')

from app import routes 