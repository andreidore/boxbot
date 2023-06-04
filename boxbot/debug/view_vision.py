import pickle

import cv2
import zmq

from boxbot.config import ZMQ_HOST, VISION_RAW_ZMQ_PORT


def main():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://{ZMQ_HOST}:{VISION_RAW_ZMQ_PORT}")
    socket.subscribe("")

    while True:
        frame_bytes = socket.recv()
        # print(frame_bytes)

        img = pickle.loads(frame_bytes)

        #print(img.shape)

        # Now you can process the image
        cv2.imshow('image', img)
        #print("a1")
        cv2.waitKey(1)
        #print("a2")


if __name__:
    main()
