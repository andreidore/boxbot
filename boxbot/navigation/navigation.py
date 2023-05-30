import zmq

from boxbot.config import ZMQ_HOST, NAVIGATION_ZMQ_PORT


class Navigation():

    def __init__(self):
        print("Init navigation.")

        self.context = zmq.Context()
        self.board_socket = self.context.socket(zmq.SUB)

        self.board_socket.connect("tcp://{}:{}".format(ZMQ_HOST, NAVIGATION_ZMQ_PORT))
        self.board_socket.subscribe("")

    def start(self):
        print("Start navigation.")

        while True:
            message = self.board_socket.recv_string()
            print("Message: " + message)


def main():
    navigation = Navigation()
    navigation.start()


if __name__ == '__main__':
    main()
