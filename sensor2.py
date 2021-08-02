from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory

import time

# HC SR04の使用するピン
PIN_TRIG = 13
PIN_ECHO = 15

def main():
    # ピン設定
    factory = PiGPIOFactory()
    sensor = DistanceSensor(PIN_ECHO, PIN_TRIG, pin_factory=factory)

    for _ in range(100):
        print('Distance to nearest object is', sensor.distance, 'm')
        time.sleep(1)
    # print("distance:", distance, "cm")

if __name__ == "__main__":
    main()