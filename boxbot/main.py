""""
Main file of boxbot.
"""

import cv2

from camera.camera import Camera
from landmark.aruco import ArucoManager


def main():
    """
    Main function of boxbot.
    :return:
    """
    print("Start boxbot.")

    # init Camera
    camera = Camera()

    # init ArucoManager
    aruco_manager = ArucoManager()

    while True:
        frame = camera.get_frame()

        aruco_frame = aruco_manager.update(frame)

        cv2.imshow('frame', aruco_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


if __name__ == '__main__':
    main()
