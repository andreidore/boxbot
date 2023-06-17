import os
import pickle

import cv2
import zmq
from deep_sort_realtime.deepsort_tracker import DeepSort

from boxbot.config import VISION_ENDPOINT


class Vision():
    CAMERA_IMAGE_SIZE = (1024, 768)
    IMAGE_SIZE = (640, 360)

    def __init__(self):
        print("Vision init")

        self.capture = cv2.VideoCapture(0)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.CAMERA_IMAGE_SIZE[0])
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.CAMERA_IMAGE_SIZE[1])

        if os.getenv("ENV") == "DEV":
            from boxbot.vision.detector.yolo8_detector import YOLO8Detector
            self.detector = YOLO8Detector()
            from boxbot.vision.extractor.timm_extractor import TimmExtractor
            self.extractor = TimmExtractor()
        else:
            from boxbot.vision.detector.tensorrt_detector import TensorRTDetector
            self.detector = TensorRTDetector()
            from boxbot.vision.extractor.tensorrt_extractor import TensorRTExtractor
            self.extractor = TensorRTExtractor()

        self.tracker = DeepSort(max_age=5)

        print(f"Publishing to {VISION_ENDPOINT}")
        self.context = zmq.Context()
        self.vision_socket = self.context.socket(zmq.PUB)
        self.vision_socket.bind(VISION_ENDPOINT)

        self.publish_frame = True
        self.publish_detection_bbs = True
        self.publish_detection_frame = True

    def start(self):
        print("Vision start")

        while True:
            _, frame = self.capture.read()

            frame = cv2.resize(frame, self.IMAGE_SIZE)

            detector_results = self.detector.detect(frame)
            # detector_results = {}

            vision_message = {}

            if self.publish_frame:
                vision_message["frame"] = frame

            if self.publish_detection_frame:
                vision_message["detection_frame"] = detector_results["detection_frame"]

            detection_bbs = detector_results["bbs"]

            object_chips = self.chipper(frame, detection_bbs)
            embeddings = self.embedder(object_chips)
            #vision_message["frame"] = bbs_frame[0]

            # print(detection_bbs)

            # TODO use a better serialization method
            message_bytes = pickle.dumps(vision_message)

            self.vision_socket.send(message_bytes)

    @staticmethod
    def chipper(frame, bbs):
        """
        Crop frame based on bbox values

        :param frame:
        :param bbs:
        :return:
        """
        chips = []
        for bb in bbs:
            x, y, w, h, p, c = bb
            x = int(x)
            y = int(y)
            w = int(w)
            h = int(h)
            chips.append(frame[y:y + h, x:x + w])
        return chips

    def embedder(self, chips):
        """
        Embeds chips using extractor

        :param chips:
        :return:
        """
        embeddings = []
        for chip in chips:
            embeddings.append(self.extractor.extract(chip))
        return embeddings


def main():
    vision = Vision()
    vision.start()


if __name__ == "__main__":
    main()
