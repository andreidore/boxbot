"""

Landmark navigation service.

"""

import cv2  # pylint: disable = no-name-in-module
import numpy as np
import zmq

from boxbot.config import VISION_IMAGE_TOPIC, NAVIGATION_LANDMARK_IMAGE_TOPIC
from boxbot.message.image_message_pb2 import ImageMessage  # pylint: disable = no-name-in-module


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

            image_message = ImageMessage()
            image_message.ParseFromString(message)

            frame = np.frombuffer(image_message.image_bytes,  # pylint disable = c-extension-no-member
                                  dtype=np.uint8)
            frame = frame.reshape(image_message.height, image_message.width, image_message.channels)
            # print(frame.shape)

            # print(gray_frame.shape)

            corners, ids, _ = cv2.aruco.detectMarkers(frame, self.dictionary, # pylint: disable = c-extension-no-member
                                                      parameters=self.parameters)

            if ids:
                print(f"Found {len(ids)} markers.")
                print(ids)

            # Draw rejected markers:
            aruco_frame = cv2.aruco.drawDetectedMarkers(frame, corners, ids) # pylint: disable = c-extension-no-member

            output_image_message = ImageMessage()
            output_image_message.image_bytes = aruco_frame.tobytes()
            output_image_message.width = aruco_frame.shape[1]
            output_image_message.height = aruco_frame.shape[0]
            output_image_message.channels = aruco_frame.shape[2]

            self.landmark_image_socket.send(output_image_message.SerializeToString())


def main():
    """

    Main function.

    :return:
    """
    Landmark().start()


if __name__ == '__main__':
    main()
