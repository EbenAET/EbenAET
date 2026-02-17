"""
Sequential LED Fading for Qt Py / Xiao2040
Fades 3 external LEDs up and down in sequence using PWM

Circuit:
- LED 1: Anode (long leg) -> A0, Cathode (short leg) -> 220Ω resistor -> GND
- LED 2: Anode (long leg) -> A1, Cathode (short leg) -> 220Ω resistor -> GND  
- LED 3: Anode (long leg) -> A2, Cathode (short leg) -> 220Ω resistor -> GND

Behavior:
- LED1 fades up to full brightness, then fades down to zero
- LED2 fades up to full brightness, then fades down to zero
- LED3 fades up to full brightness, then fades down to zero
- Sequence repeats indefinitely

Usage:
1. Save this file as code.py on your Qt Py CIRCUITPY drive
2. The board will automatically run it and fade the LEDs in sequence
"""

import board
import pwmio
import time

# Setup LED pins with PWM for brightness control
led1 = pwmio.PWMOut(board.A0, frequency=1000, duty_cycle=0)
led2 = pwmio.PWMOut(board.A1, frequency=1000, duty_cycle=0)
led3 = pwmio.PWMOut(board.A2, frequency=1000, duty_cycle=0)

def fade_up(led, steps=100, delay=0.01):
    """Fade LED from 0% to 100% brightness"""
    for i in range(steps + 1):
        # duty_cycle ranges from 0 (off) to 65535 (full brightness)
        led.duty_cycle = int((i / steps) * 65535)
        time.sleep(delay)

def fade_down(led, steps=100, delay=0.01):
    """Fade LED from 100% to 0% brightness"""
    for i in range(steps, -1, -1):
        # duty_cycle ranges from 0 (off) to 65535 (full brightness)
        led.duty_cycle = int((i / steps) * 65535)
        time.sleep(delay)

# Main loop - fade LEDs in sequence
while True:
    # LED 1: Fade up then down
    fade_up(led1)
    fade_down(led1)
    
    # LED 2: Fade up then down
    fade_up(led2)
    fade_down(led2)
    
    # LED 3: Fade up then down
    fade_up(led3)
    fade_down(led3)
