import os

import cv2


class Vision(object):

    def __init__(self):
        print("Vision init")

        self.capture = cv2.VideoCapture(0)

        if os.getenv("DEV") is not None:
            from boxbot.vision.detector.yolo8_detector import YOLO8Detector
            self.detector = YOLO8Detector()
        else:
            from boxbot.vision.detector.tensort_detector import TensortDetector
            self.detector = TensortDetector()

    def start(self):
        print("Vision start")

        while True:
            ret, frame = self.capture.read()

            detector_results = self.detector.detect(frame)




def main():
    vision = Vision()
    vision.start()


if __name__ == "__main__":
    main()
