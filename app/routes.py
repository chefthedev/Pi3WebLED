# Defines the routes for the Flask web server

from app import app
from utils.led_control import led_on, led_off, led_default
from flask import render_template

@app.route('/')
def index():
    # Index route for rendering the index html page
    return render_template("index.html")

@app.route('/led/on')
def turn_led_on():
    # LED On route for turning the ACT LED on using the led_control
    led_on()
    return "LED has been turned on!"

@app.route('/led/off')
def turn_led_off():
    # LED Off route for turning the ACT LED off using the led_control
    led_off()
    return "LED has been turned off!"

@app.route('/led/default')
def turn_led_default():
    # LED Default route for turning the ACT LED to the default state using the led_control
    led_default()
    return "LED has been turned to it's default state!"