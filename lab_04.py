"""
Vibration Sensor (SW420 Module)
>> Omni Sensing
"""
import machine


def main():
    status_pin = machine.Pin(4, machine.Pin.IN)
    print("Vibration Sensing")
    while True:
        if status_pin.value() == True:
            print("Vibration")


if __name__ == '__main__':
    main()
