from time import sleep

from Camera import Camera
from transitions import Machine
from ServoMotors import ServoMotors
from UltrasoundSensor import UltrasoundSensor


class TrashHero(object):
    states = [
        "initial",  # dummy state
        "setup",  # setup hardwares and GPIOs
        "ready",  # an object has been thrown, detected by ultrasonic sensor
        "detecting_object",  # an object has been identified, open left or right flap
        "left_flap_open",
        "right_flap_open",
    ]

    transitions = [
        {"trigger": "change_to_setup", "source": "initial", "dest": "setup"},
        {"trigger": "change_to_ready", "source": "setup", "dest": "ready"},
        {
            "trigger": "change_to_detecting_object",
            "source": "ready",
            "dest": "detecting_object",
        },
        {
            "trigger": "change_to_left_flap_open",
            "source": "detecting_object",
            "dest": "left_flap_open",
        },
        {
            "trigger": "change_to_right_flap_open",
            "source": "detecting_object",
            "dest": "right_flap_open",
        },
        {
            "trigger": "change_to_ready",
            "source": ["left_flap_open", "right_flap_open"],
            "dest": "ready",
        },
    ]

    def on_enter_initial(self):
        pass

    def on_enter_setup(self):
        print("----")
        print("setting up GPIOs")
        print("----")

        # Init Hardware and GPIOs
        self.motors = ServoMotors()
        self.ultrasound_sensor = UltrasoundSensor()
        self.camera = Camera()

        # Moves the flaps to initial position
        self.motors.toggleLeftServo()
        self.motors.toggleRightServo()

        # Change to "ready" state
        self.change_to_ready()

    def on_enter_ready(self):
        print("----")
        print("ultrasonic scanning for object")
        print("----")

        # Take a picture when object is been thrown
        while True:
            print("waiting...")
            sleep(0.5)
            object_thrown = self.ultrasound_sensor.get_distance() <= 22
            if object_thrown:
                self.camera.take_photo()
                break

        # Change to "detecting_object" state
        self.change_to_detecting_object()

    def on_enter_detecting_object(self):
        print("----")
        print("object is being detected by AI")
        print("----")

        # Send picture to REST endpoint to determine the recycability

        # Change to "left_flap_open" or "right_flap_open" state depending on what AI reply
        # if (AI_Response == Recyclable):
        #     self.machine.change_to_left_flap_open()
        # elif (AI_Response == Non_Recyclable)
        #     self.machine.change_to_right_flap_open()
        self.change_to_left_flap_open()

    def on_enter_left_flap_open(self):
        print("----")
        print("left flap is opened")
        print("----")

        self.motors.toggleLeftServo()

        # Change to "ready" state
        self.change_to_ready()

    def on_enter_right_flap_open(self):
        print("----")
        print("right flap is opened")
        print("----")

        self.motors.toggleRightServo()

        # Change to "ready" state
        self.change_to_ready()

    def __init__(self):
        self.machine = Machine(
            self,
            states=TrashHero.states,
            transitions=TrashHero.transitions,
            initial="initial",
            queued=True,
        )

