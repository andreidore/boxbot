import pygame
import zmq

from boxbot.config import BOARD_MOTOR_VELOCITY_ENDPOINT
from boxbot.message.motor_velocity_pb2 import MotorVelocity


def main():
    pygame.init()

    display = pygame.display.set_mode((300, 300))

    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ stands for REQuest, to represent a client
    socket.connect(BOARD_MOTOR_VELOCITY_ENDPOINT)  # Connect to the server

    left = 0
    right = 0

    while True:



        # creating a loop to check events that
        # are occurring
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                print("KEYUP")
                left = 0
                right = 0

            # checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    print("LEFT key pressed")

                    left = 10
                    right = -10

                elif event.key == pygame.K_RIGHT:
                    print("RIGHT key pressed")

                    left = -10
                    right = 10



                elif event.key == pygame.K_UP:
                    print("UP key pressed")

                    left = 10
                    right = 10



        motor_speed = MotorVelocity()
        motor_speed.left = left
        motor_speed.right = right

        socket.send(motor_speed.SerializeToString())  # Send the command
        message = socket.recv()  # Wait for the reply from the server
        print(f"Received reply [ {message} ]")


if __name__ == "__main__":
    main()
