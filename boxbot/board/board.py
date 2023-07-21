import time

import zmq

from boxbot.config import BOARD_MOTOR_VELOCITY_SERVICE


class Board():

    def __init__(self):
        print("Init board.")

        self.context = zmq.Context()
        self.motor_velocity_socket = self.context.socket(zmq.REQ)
        self.motor_velocity_socket.bind(BOARD_MOTOR_VELOCITY_SERVICE)

    def start(self):
        print("Start board.")

        while True:

            # message = self.board_socket.recv_string()
            # print("Message: " + message)

            ## command
            try:
                command_message = self.motor_velocity_socket.recv(zmq.NOBLOCK)
                self.motor_velocity_socket.send_string("ACK")

                print(command_message)
            except zmq.Again:
                # print("No command received")
                pass

            time.sleep(0.1)


def main():
    board = Board()
    board.start()


if __name__ == '__main__':
    main()
