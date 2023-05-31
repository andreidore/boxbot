import time

import zmq

from boxbot.config import BOARD_ZMQ_PORT, COMMAND_ZMQ_PORT, ZMQ_HOST
from boxbot.controller.state.idle import IdleState
from boxbot.fsm.fsm import FiniteStateMachine


class Controller():

    def __init__(self):
        print("Init controller")

        self.context = zmq.Context()
        self.board_socket = self.context.socket(zmq.SUB)

        self.board_socket.connect("tcp://{}:{}".format(ZMQ_HOST, BOARD_ZMQ_PORT))
        self.board_socket.subscribe("")

        self.command_socket = self.context.socket(zmq.REP)  # REP stands for REPly, to represent a server
        self.command_socket.bind(f"tcp://{ZMQ_HOST}:{COMMAND_ZMQ_PORT}")  # Bin

        self.fsm = FiniteStateMachine(IdleState())

    def start(self):
        print("Start controller")

        while True:
            # message = self.board_socket.recv_string()
            # print("Message: " + message)

            ## command
            try:
                command_message = self.command_socket.recv_string(zmq.NOBLOCK)
                self.command_socket.send_string("ACK")

                print(command_message)
            except zmq.Again:
                #print("No command received")
                pass

            self.fsm.update()

            time.sleep(0.1)


def main():
    controller = Controller()
    controller.start()


if __name__ == '__main__':
    main()
