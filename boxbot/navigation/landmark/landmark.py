"""

Landmark navigation service.

"""

import cv2  # pylint: disable = no-name-in-module
import numpy as np
import zmq

from boxbot.config import VISION_IMAGE_TOPIC, NAVIGATION_LANDMARK_IMAGE_TOPIC
from boxbot.message.image_message_pb2 import ImageMessage  # pylint: disable = no-name-in-module
from boxbot.message.messages import get_image_from_message


class Landmark:  # pylint: disable=too-few-public-methods
    """

    Landmark navigation service.

    """

    def __init__(self):
        print("Init navigation landmark.")

        self.context = zmq.Context()
        self.vision_image_socket = self.context.socket(zmq.SUB)
        self.vision_image_socket.connect(VISION_IMAGE_TOPIC)  # Connect to the server
        self.vision_image_socket.setsockopt_string(zmq.SUBSCRIBE, '')

        self.landmark_image_socket = self.context.socket(zmq.PUB)
        self.landmark_image_socket.bind(NAVIGATION_LANDMARK_IMAGE_TOPIC)

        self.dictionary = cv2.aruco.getPredefinedDictionary(  # pylint: disable = c-extension-no-member
            cv2.aruco.DICT_4X4_100)  # pylint: disable = c-extension-no-member

        print(dir(self.dictionary))

        # Create parameters to be used when detecting markers:
        self.parameters = cv2.aruco.DetectorParameters()  # pylint: disable = c-extension-no-member

    def start(self):
        """

        Start the landmark navigation service.

        :return:
        """
        print("Start navigation landmark.")

        while True:
            message = self.vision_image_socket.recv()  # Wait for the reply from the server

            # print(type(message))

            image_message = ImageMessage()
            image_message.ParseFromString(message)

            frame = get_image_from_message(image_message)

            # print(frame.shape)

            # print(gray_frame.shape)

            corners, ids, _ = cv2.aruco.detectMarkers(frame, self.dictionary,  # pylint: disable = c-extension-no-member
                                                      parameters=self.parameters)

            if ids is not None:
                print(ids)

            # Draw rejected markers:
            aruco_frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)  # pylint: disable = c-extension-no-member

            aruco_image_message = ImageMessage()
            aruco_image_message.image_bytes = aruco_frame.tobytes()
            aruco_image_message.width = frame.shape[1]
            aruco_image_message.height = frame.shape[0]
            aruco_image_message.channels = frame.shape[2]

            aruco_image_message.k_bytes = image_message.k_bytes

            self.landmark_image_socket.send(aruco_image_message.SerializeToString())


def main():
    """

    Main function.

    :return:
    """
    Landmark().start()


if __name__ == '__main__':
    main()
