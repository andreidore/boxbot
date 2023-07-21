import numpy as np
import zmq

from boxbot.config import BOARD_MOTOR_VELOCITY_SERVICE, VISION_IMAGE_TOPIC
from boxbot.message.image_message_pb2 import ImageMessage
from boxbot.message.motor_velocity_message_pb2 import MotorVelocityMessage
from controller import Robot


class Webots():

    def __init__(self):
        print("Init board simulator.")

        self.context = zmq.Context()

        self.motor_velocity_socket = self.context.socket(zmq.REP)
        self.motor_velocity_socket.bind(BOARD_MOTOR_VELOCITY_SERVICE)

        self.image_socket = self.context.socket(zmq.PUB)
        self.image_socket.bind(VISION_IMAGE_TOPIC)

        self.robot = Robot()

        self.left_motor = self.robot.getDevice("left wheel motor")
        self.right_motor = self.robot.getDevice("right wheel motor")

        self.camera = self.robot.getDevice("camera")

    def start(self):
        print("Start board sim.")

        self.camera.enable(50)

        F = 2.0  # frequency 2 Hz
        t = 0.0  # elapsed simulation time

        TIME_STEP = 64

        left_motor_velocity = 0
        right_motor_velocity = 0

        while self.robot.step(TIME_STEP) != -1:

            try:
                motor_velocity_message = self.motor_velocity_socket.recv(zmq.NOBLOCK)
                self.motor_velocity_socket.send_string("ACK")

                motor_velocity = MotorVelocityMessage()
                motor_velocity.ParseFromString(motor_velocity_message)

                # print(motor_velocity)

                left_motor_velocity = motor_velocity.left
                right_motor_velocity = motor_velocity.right

            except zmq.Again:
                # print("No command received")
                pass

            self.left_motor.setPosition(float('inf'))
            self.right_motor.setPosition(float('inf'))

            self.left_motor.setVelocity(left_motor_velocity)
            self.right_motor.setVelocity(right_motor_velocity)

            # Get image from camera

            frame = self.camera.getImageArray()
            frame = np.array(frame, dtype=np.uint8)
            # print(frame.shape)
            image_message = ImageMessage()
            image_message.image_bytes = frame.tobytes()
            image_message.width = frame.shape[1]
            image_message.height = frame.shape[0]
            image_message.channels = frame.shape[2]

            self.image_socket.send(image_message.SerializeToString())


def main():
    Webots().start()


if __name__ == '__main__':
    main()