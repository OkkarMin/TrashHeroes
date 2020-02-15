from time import sleep
from UltrasoundSensor import UltrasoundSensor

ultrasound_sensor = UltrasoundSensor()

while True:
    sleep(0.02)
    print(ultrasound_sensor.get_distance())

