from gpiozero import DistanceSensor
import RPi.GPIO as GPIO


class UltrasoundSensor(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.sensor = DistanceSensor(trigger=23, echo=24)

    def get_distance(self):
        return self.sensor.distance * 100
