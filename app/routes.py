# Defines the routes for the Flask web server

from app import app
from utils.led_control import led_on, led_off, led_default

@app.route('/')
def home():
    # Home route for displaying a hello world statement
    return "Hello world! Flask is running on the Raspberry Pi 3."

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