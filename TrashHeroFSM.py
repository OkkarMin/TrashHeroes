from transitions import Machine


class TrashHero(object):
    states = [
        "initial",
        "setup",
        "ready",  # an object has been thrown, detected by unltrasonic sensor
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
        print("initial state entered")

    def on_enter_setup(self):
        print("setup state entered")
        print("----")
        print("setting up GPIOs")
        print("----")

    def on_enter_ready(self):
        print("ready state entered")
        print("----")
        print("ultrasonic scanning for object")
        print("----")

    def on_enter_detecting_object(self):
        print("detecting_object state entered")
        print("----")
        print("object is being detected by AI")
        print("----")

    def on_enter_left_flap_open(self):
        print("left_flap_open state entered")
        print("----")
        print("left flap is opened")
        print("----")

    def on_enter_right_flap_open(self):
        print("right_flap_open state entered")
        print("----")
        print("right flap is opened")
        print("----")

    def __init__(self):
        self.machine = Machine(
            self,
            states=TrashHero.states,
            transitions=TrashHero.transitions,
            initial="initial",
        )

