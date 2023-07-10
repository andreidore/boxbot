from typing import Tuple

import cv2
import numpy as np

ROBOT_SIZE = 20


def display(level_map, robot_x, robot_y, robot_theta):
    level_map = cv2.cvtColor(level_map, cv2.COLOR_GRAY2BGR)

    robot_image = np.zeros_like(level_map)

    cv2.rectangle(robot_image, (robot_x, robot_y), (robot_x + ROBOT_SIZE, robot_y + ROBOT_SIZE), (0, 0, 255), 2)

    p1 = [robot_x + ROBOT_SIZE // 2, robot_y + ROBOT_SIZE // 2]
    p2 = [robot_x + 40, p1[1]]

    cv2.line(robot_image, p1, p2,
             (0, 0, 255),
             2)

    img2gray = cv2.cvtColor(robot_image, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    # Now black-out the area of logo in ROI
    level_image_bg = cv2.bitwise_and(level_map, level_map, mask=mask_inv)
    # Take only region of logo from logo image.
    robot_image_fg = cv2.bitwise_and(robot_image, robot_image, mask=mask)
    # Put logo in ROI and modify the main image
    frame = cv2.add(level_image_bg, robot_image_fg)

    cv2.imshow('map', frame)


def move_robot(robot_x: int, robot_y: int, robot_theta: float, forward: int, turn: float) -> Tuple[int, int, float]:
    """
    Move robot forward and turn
    """

    # forward_noisy = forward + np.random.normal(0, 0.1, 1)
    forward_noisy = forward

    robot_theta_radians = np.radians(robot_theta)

    _robot_x = robot_x + forward_noisy * np.cos(robot_theta_radians)
    _robot_y = robot_y + forward_noisy * np.sin(robot_theta_radians)

    # _turn = turn + np.random.normal(0, 0.1, 1)
    _turn = turn

    _robot_theta = robot_theta + _turn

    return int(_robot_x), int(_robot_y), int(_robot_theta)  # type: ignore


def main():
    robot_map = cv2.imread("map.png", 0)

    height, width = robot_map.shape

    robot_x = width // 4
    robot_y = height // 4
    robot_theta = 0

    # particles = np.zeros((NUM_PARTICLES, 3))

    while True:
        display(robot_map, robot_x, robot_y, robot_theta)

        forward = 0
        turn = 0

        k = cv2.waitKey(0)

        if k == 0:
            forward = 5
        elif k == 3:
            turn = 25
        elif k == 2:
            turn = -25


        robot_x, robot_y, robot_theta = move_robot(robot_x, robot_y, robot_theta, forward, turn)

        print(robot_x, robot_y, robot_theta)

        print(k)


if __name__ == "__main__":
    main()
