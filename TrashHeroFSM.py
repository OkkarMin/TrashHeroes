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
        {"trigger": "change_to_setup", "source": "initial", "destination": "setup"},
        {"trigger": "change_to_ready", "source": "setup", "destination": "ready"},
        {
            "trigger": "change_to_detecting_object",
            "source": "ready",
            "destination": "detecting_object",
        },
        {
            "trigger": "change_to_object_detected",
            "source": "detecting_object",
            "destination": "object_detected",
        },
        {
            "trigger": "change_to_left_flap_open",
            "source": "object_detected",
            "destination": "left_flap_open",
        },
        {
            "trigger": "change_to_right_flap_open",
            "source": "object_detected",
            "destination": "right_flap_open",
        },
        {
            "trigger": "change_to_ready",
            "source": ["left_flap_open", "right_flap_open"]
            "destination": "ready",
        },
    ]