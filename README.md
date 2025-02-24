# Pi3WebLED
A simple web server intended to run on a Raspberry Pi 3 to allow for the remote control of an LED. The Flask web framework is used to serve an HTML GUI,  allowing the user to press command buttons and directly control the state of the embedded ACT LED on the board.

## Technologies Used
* Raspberry Pi 3-B (v1.2)
* Python 3.11
* Venv
* Flask

## Steps to Build
1. Clone the repository on your Raspberry Pi
2. CD into the project directory: `cd {your_prefix}/Pi3WebLED`
3. Create a new virtual environment: `python3 -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Run the application: `sudo python3 main.py`

## Important Note
This program has only been tested on a Raspberry Pi 3-B (v1.2). I cannot guarantee that it will work on other models of the Raspberry Pi, or with different technology stacks.