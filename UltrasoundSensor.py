from gpiozero import DistanceSensor


class UltrasoundSensor(object):
    def __init__(self):
        self.sensor = DistanceSensor(trigger=23, echo=24)

    def get_distance(self):
        return self.sensor.distance * 100
