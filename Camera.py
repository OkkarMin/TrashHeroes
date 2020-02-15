from picamera import PiCamera


class Camera(object):
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (512, 512)

    def take_photo(self):
        self.camera.capture("/home/pi/Desktop/image.jpg")

