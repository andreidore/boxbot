import time

import zmq

from boxbot.config import BOARD_ZMQ_PORT, ZMQ_HOST


class Board():

    def __init__(self):
        print("Init board.")

        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.PUB)

        self.socket.bind("tcp://{}:{}".format(ZMQ_HOST, BOARD_ZMQ_PORT))

    def start(self):
        print("Start board.")

        while True:
            self.socket.send_string("Hello from board.")
            time.sleep(1)


def main():
    board = Board()
    board.start()


if __name__ == '__main__':
    main()
