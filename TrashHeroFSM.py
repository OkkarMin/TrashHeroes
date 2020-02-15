from transitions import Machine


class TrashHero(object):
    states = [
        "initial",
        "setup",
        "ready",  # an object has been thrown, detected by unltrasonic sensor
        "detecting_object",
        "object_detected",
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
            "trigger": "change_to_object_detected",
            "source": "detecting_object",
            "dest": "object_detected",
        },
        {
            "trigger": "change_to_left_flap_open",
            "source": "object_detected",
            "dest": "left_flap_open",
        },
        {
            "trigger": "change_to_right_flap_open",
            "source": "object_detected",
            "dest": "right_flap_open",
        },
        {
            "trigger": "change_to_ready",
            "source": ["left_flap_open", "right_flap_open"]
            "dest": "ready",
        },
    ]

    def on_enter_initial(self):
        print("initial state entered")
    
    def on_enter_setup(self):
        print("setup state entered")
    
    def on_enter_ready(self):
        print("ready state entered")
    
    def on_enter_detecting_object(self):
        print("detecting_object state entered")
    
    def on_enter_object_detected(self):
        print("object_detectecd state entered")
    
    def on_enter_left_flap_open(self):
        print("left_flap_open state entered")
    
    def on_enter_right_flap_open(self):
        print("right_flap_open state entered")