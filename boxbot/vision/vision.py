import os
import pickle

import cv2
import zmq

from boxbot.config import VISION_ENDPOINT


class Vision():
    CAMERA_IMAGE_SIZE = (1280, 1024)

    def __init__(self):
        print("Vision init")

        self.capture = cv2.VideoCapture(0)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.CAMERA_IMAGE_SIZE[0])
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.CAMERA_IMAGE_SIZE[1])

        if os.getenv("DEV") is not None:
            from boxbot.vision.detector.yolo8_detector import YOLO8Detector
            self.detector = YOLO8Detector()
        else:
            from boxbot.vision.detector.tensort_detector import TensortDetector
            self.detector = TensortDetector()

        print(f"Publishing to {VISION_ENDPOINT}")
        self.context = zmq.Context()
        self.vision_socket = self.context.socket(zmq.PUB)
        self.vision_socket.bind(VISION_ENDPOINT)

    def start(self):
        print("Vision start")

        while True:
            _, frame = self.capture.read()

            detector_results = self.detector.detect(frame)

            message = {
                "frame": frame
            }

            if "detection_frame" in detector_results:
                message["detection_frame"] = detector_results["detection_frame"]

            # TODO use a better serialization method
            message_bytes = pickle.dumps(message)

            self.vision_socket.send(message_bytes)


def main():
    vision = Vision()
    vision.start()


if __name__ == "__main__":
    main()
