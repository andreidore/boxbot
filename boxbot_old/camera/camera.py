import cv2


class Camera:

    def __init__(self):
        print("Init camera.")

        self.capture = cv2.VideoCapture(0)

    def get_frame(self):
        ret, frame = self.capture.read()
        return frame
