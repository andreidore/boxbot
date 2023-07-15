import time
from math import pi, sin

import zmq

from boxbot.config import BOARD_ZMQ_PORT, ZMQ_HOST
from controller import Robot


class Board():

    def __init__(self):
        print("Init board simulator.")

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)

        self.socket.bind("tcp://{}:{}".format(ZMQ_HOST, BOARD_ZMQ_PORT))

        self.robot = Robot()

        self.left_motor = self.robot.getDevice("left wheel motor")
        self.right_motor = self.robot.getDevice("right wheel motor")

    def start(self):
        print("Start board sim.")

        F = 2.0  # frequency 2 Hz
        t = 0.0  # elapsed simulation time

        TIME_STEP = 64

        while self.robot.step(TIME_STEP) != -1:

            self.left_motor.setPosition(float('inf'))
            self.right_motor.setPosition(float('inf'))

            self.left_motor.setVelocity(-10)
            self.right_motor.setVelocity(10)




def main():
    board = Board()
    board.start()


if __name__ == '__main__':
    main()
