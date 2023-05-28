import cv2


class Vision(object):

    def __init__(self):
        print("Vision init")

        self.capture = cv2.VideoCapture(0)

    def start(self):
        print("Vision start")

        while True:
            ret, frame = self.capture.read()


def main():
    vision = Vision()
    vision.start()


if __name__ == "__main__":
    main()
