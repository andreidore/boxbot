import time

import zmq

from boxbot.config import BOARD_ZMQ_PORT, ZMQ_HOST
from boxbot.controller.state.idle import IdleState
from boxbot.fsm.fsm import FiniteStateMachine


class Controller():

    def __init__(self):
        print("Init controller")

        self.context = zmq.Context()
        self.board_socket = self.context.socket(zmq.SUB)

        self.board_socket.connect("tcp://{}:{}".format(ZMQ_HOST, BOARD_ZMQ_PORT))
        self.board_socket.subscribe("")

        self.fsm = FiniteStateMachine(IdleState())

    def start(self):
        print("Start controller")

        while True:
            # message = self.board_socket.recv_string()
            # print("Message: " + message)

            self.fsm.update()

            time.sleep(1.0)


def main():
    controller = Controller()
    controller.start()


if __name__ == '__main__':
    main()
