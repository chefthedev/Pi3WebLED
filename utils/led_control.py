# Control interface for the onboard ACT LED

import os
import time

# Command values
TRIGGER_NONE = "none"
TRIGGER_MMC0 = "mmc0"
LED_ON = 1
LED_OFF = 0

# Command paths
TRIGGER_PATH = "/sys/class/leds/ACT/trigger"
BRIGHTNESS_PATH = "/sys/class/leds/ACT/brightness"

def led_on():
    # Remove existing LED trigger and sleep to allow change to process
    os.system(f'echo "{TRIGGER_NONE}" | sudo tee {TRIGGER_PATH}')
    time.sleep(0.1)

    # Set the ACT LED Brightness to On
    os.system(f'echo "{LED_ON}" | sudo tee {BRIGHTNESS_PATH}')

def led_off():
    # Remove existing LED trigger and sleep to allow change to process
    os.system(f'echo "{TRIGGER_NONE}" | sudo tee {TRIGGER_PATH}')
    time.sleep(0.1)

    # Set the ACT LED Brightness to Off
    os.system(f'echo "{LED_OFF}" | sudo tee {BRIGHTNESS_PATH}')

def led_default():
    # Apply the default mmc0 (read/write operation) LED trigger and sleep to allow change to process
    os.system(f'echo "{TRIGGER_MMC0}" | sudo tee {TRIGGER_PATH}')
    time.sleep(0.1)

    # Set the ACT LED Brightness to On
    os.system(f'echo "{LED_ON}" | sudo tee {BRIGHTNESS_PATH}')