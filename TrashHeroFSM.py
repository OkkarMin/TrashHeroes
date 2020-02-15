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
