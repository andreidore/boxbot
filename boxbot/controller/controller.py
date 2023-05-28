import zmq

from boxbot import config
from boxbot.board.board import BOARD_ZMQ_PORT


class Controller():

    def __init__(self):
        print("Init controller")

        self.context = zmq.Context()
        self.board_socket = self.context.socket(zmq.SUB)

        self.board_socket.connect("tcp://{}:{}".format(config.ZMQ_HOST, BOARD_ZMQ_PORT))
        self.board_socket.subscribe("")

    def start(self):
        print("Start controller")

        while True:
            message = self.board_socket.recv_string()
            print("Message: " + message)


def main():
    controller = Controller()
    controller.start()


if __name__ == '__main__':
    main()
