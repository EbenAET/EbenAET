"""
Bare bones Qt Py LED blink code
Blinks 3 external LEDs connected to A0, A1, and A2

Circuit:
- LED 1: Anode (long leg) -> A0, Cathode (short leg) -> 220Ω resistor -> GND
- LED 2: Anode (long leg) -> A1, Cathode (short leg) -> 220Ω resistor -> GND  
- LED 3: Anode (long leg) -> A2, Cathode (short leg) -> 220Ω resistor -> GND

Usage:
1. Save this file as code.py on your Qt Py CIRCUITPY drive
2. The board will automatically run it and blink the LEDs
"""

import board
import digitalio
import time

# Setup LED pins
led1 = digitalio.DigitalInOut(board.A0)
led1.direction = digitalio.Direction.OUTPUT

led2 = digitalio.DigitalInOut(board.A1)
led2.direction = digitalio.Direction.OUTPUT

led3 = digitalio.DigitalInOut(board.A2)
led3.direction = digitalio.Direction.OUTPUT

# Blink loop
while True:
    # Turn all LEDs on
    led1.value = True
    led2.value = True
    led3.value = True
    time.sleep(0.5)
    
    # Turn all LEDs off
    led1.value = False
    led2.value = False
    led3.value = False
    time.sleep(0.5)
