# Control interface for the onboard ACT LED

import os

# Command values
TRIGGER_NONE = "none"
TRIGGER_MMC0 = "mmc0"
LED_ON = 1
LED_OFF = 0

# Command paths
TRIGGER_PATH = "/sys/class/leds/ACT/trigger"
BRIGHTNESS_PATH = "/sys/class/leds/ACT/brightness"

def led_on():
    # Turn the ACT LED on
    os.system(f'echo "{TRIGGER_NONE}" | sudo tee {TRIGGER_PATH}')
    os.system(f'echo "{LED_ON}" | sudo tee {BRIGHTNESS_PATH}')

def led_off():
    # Turn the ACT LED off
    os.system(f'echo "{TRIGGER_NONE}" | sudo tee {TRIGGER_PATH}')
    os.system(f'echo "{LED_OFF}" | sudo tee {BRIGHTNESS_PATH}')

def led_default():
    # Turn the ACT LED to it's default state
    os.system(f'echo "{TRIGGER_MMC0}" | sudo tee {TRIGGER_PATH}')