"""

Landmark navigation service.

"""

import cv2  # pylint: disable = no-name-in-module
import zmq

from boxbot.config import VISION_IMAGE_TOPIC, NAVIGATION_LANDMARK_IMAGE_TOPIC
from boxbot.message.messages import decode_image, encode_image


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

            frame = decode_image(message)

            # print(frame.shape)

            # print(gray_frame.shape)

            corners, ids, _ = cv2.aruco.detectMarkers(frame, self.dictionary,  # pylint: disable = c-extension-no-member
                                                      parameters=self.parameters)

            if ids is not None:
                print(ids)

            # Draw rejected markers:
            aruco_frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids)  # pylint: disable = c-extension-no-member

            self.landmark_image_socket.send(encode_image(aruco_frame))


def main():
    """

    Main function.

    :return:
    """
    Landmark().start()


if __name__ == '__main__':
    main()
