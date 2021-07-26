"""
PWM >>> Pulse Width Modulation
Technique to reduce Output Power by toggling the digital pin at varied Duty Cycle
Parameters:
    Frequency
    Duty Cycle

Vout = Vmax * Duty_Cycle

PWM GPIOs = { 0: D3, 2: D4, 4: D2, 5: D1, 12: D6, 13: D7, 14: D5, 15: D8 }
"""
import machine
import time
import math


def pulse(l, t):
    for i in range(20):
        print('DutyCycle : ', int(math.sin(i / 10 * math.pi) * 500 + 500),
              (i / 10 * math.pi), (math.sin(i / 10 * math.pi)))
        l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
        time.sleep(t)


def main():
    led = machine.PWM(machine.Pin(2))
    for i in range(10):
        pulse(led, 1)


if __name__ == '__main__':
    main()
