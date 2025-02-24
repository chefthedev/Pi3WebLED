# Main entry point for running the Flask web server on the Raspberry Pi 3

from app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)