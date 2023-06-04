import os
import pickle

import cv2
import zmq

from boxbot.config import VISION_RAW_ZMQ_PORT, ZMQ_HOST


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

        self.context = zmq.Context()
        self.vision_socket = self.context.socket(zmq.PUB)

        self.vision_socket.bind("tcp://{}:{}".format(ZMQ_HOST, VISION_RAW_ZMQ_PORT))

    def start(self):
        print("Vision start")

        while True:
            ret, frame = self.capture.read()

            # TODO use a better serialization method
            frame_bytes = pickle.dumps(frame)
            self.vision_socket.send(frame_bytes)

            detector_results = self.detector.detect(frame)


def main():
    vision = Vision()
    vision.start()


if __name__ == "__main__":
    main()
