from machine import Pin
from time import sleep
from machine_esp32_heltec_LoRa32 import *

redPin = Pin(pin_LED_R, Pin.OUT)
greenPin = Pin(pin_LED_G, Pin.OUT)
bluePin = Pin(pin_LED_B, Pin.OUT)

def led_color(color):
    if color == "green":
        greenPin.value(1)
        bluePin.value(0)
        redPin.value(0)
    elif color == "yellow":
        greenPin.value(1)
        bluePin.value(0)
        redPin.value(1)
    elif color == "red":
        greenPin.value(0)
        bluePin.value(0)
        redPin.value(1)
    else:
        greenPin.value(0)
        bluePin.value(0)
        redPin.value(0)
    
def led_off():
    greenPin.value(0)
    bluePin.value(0)
    redPin.value(0)

def blink(freq):
    greenPin.value(0)
    bluePin.value(0)
    if str(freq).isdigit:
        for i in range(freq):
            redPin.value(1)
            sleep(1/freq*2)
            redPin.value(0)
            sleep(1/freq*2)
            i = i+1