# Defines the routes for the Flask web server

from app import app

@app.route('/')
def home():
    return "Hello world! Flask is running on the Raspberry Pi 3."