from ServoMotors import ServoMotors
from time import sleep

motors = ServoMotors()

while True:
    sleep(1)
    motors.toggleLeftServo()
    sleep(1)
    motors.toggleRightServo()
