import RPi.GPIO as GPIO
from time import sleep


class ServoMotors(object):
    def __init__(self):
        self.left_servo_pin = 27
        self.right_servo_pin = 17

        # For PWM
        self.frequency = 50
        self.a = 10
        self.b = 2

        # SetUp
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.left_servo_pin, GPIO.OUT)
        GPIO.setup(self.right_servo_pin, GPIO.OUT)

        self.left_servo = GPIO.PWM(self.left_servo_pin, self.frequency)
        self.right_servo = GPIO.PWM(self.right_servo_pin, self.frequency)

        self.left_servo.start(0)
        self.right_servo.start(0)

    # Helper function for toggling flaps
    def setDirection(self, servo, direction):
        # PWM duty formula
        duty = self.a / 180 * direction + self.b
        servo.ChangeDutyCycle(duty)
        sleep(1)

    def toggleLeftServo(self):
        self.setDirection(self.left_servo, 50)  # flap down
        sleep(1)
        self.setDirection(self.left_servo, 110)  # flap up

    def toggleRightServo(self):
        self.setDirection(self.right_servo, 90)  # flap down
        sleep(1)
        self.setDirection(self.right_servo, 30)  # flap up

