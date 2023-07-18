import zmq

from boxbot.config import BOARD_MOTOR_VELOCITY_ENDPOINT
from boxbot.message.motor_velocity_pb2 import MotorVelocity
from controller import Robot


class Board():

    def __init__(self):
        print("Init board simulator.")

        self.context = zmq.Context()
        self.motor_velocity_socket = self.context.socket(zmq.REP)
        self.motor_velocity_socket.bind(BOARD_MOTOR_VELOCITY_ENDPOINT)

        self.robot = Robot()

        self.left_motor = self.robot.getDevice("left wheel motor")
        self.right_motor = self.robot.getDevice("right wheel motor")

    def start(self):
        print("Start board sim.")

        F = 2.0  # frequency 2 Hz
        t = 0.0  # elapsed simulation time

        TIME_STEP = 64

        left_motor_velocity = 0
        right_motor_velocity = 0

        while self.robot.step(TIME_STEP) != -1:

            try:
                motor_velocity_message = self.motor_velocity_socket.recv(zmq.NOBLOCK)
                self.motor_velocity_socket.send_string("ACK")

                motor_velocity = MotorVelocity()
                motor_velocity.ParseFromString(motor_velocity_message)

                #print(motor_velocity)

                left_motor_velocity = motor_velocity.left
                right_motor_velocity = motor_velocity.right

            except zmq.Again:
                # print("No command received")
                pass

            self.left_motor.setPosition(float('inf'))
            self.right_motor.setPosition(float('inf'))

            self.left_motor.setVelocity(left_motor_velocity)
            self.right_motor.setVelocity(right_motor_velocity)


def main():
    board = Board()
    board.start()


if __name__ == '__main__':
    main()
