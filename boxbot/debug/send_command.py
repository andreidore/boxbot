import argparse

import zmq

from boxbot.config import ZMQ_HOST, COMMAND_ZMQ_PORT


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=['idle', 'goto'], help='Command to be sent')
    parser.add_argument('parameters', nargs='*', help='Parameters for the command')
    args = parser.parse_args()

    print("Command: " + args.command)
    print("Parameters: " + str(args.parameters))

    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # REQ stands for REQuest, to represent a client
    socket.connect(f"tcp://{ZMQ_HOST}:{COMMAND_ZMQ_PORT}")  # Connect to the server

    socket.send_string(args.command)  # Send the command
    message = socket.recv()  # Wait for the reply from the server
    print(f"Received reply [ {message} ]")


if __name__ == '__main__':
    main()
