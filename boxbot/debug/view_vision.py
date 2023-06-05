import pickle

import PySimpleGUI as sg
import cv2
import zmq

from boxbot.config import VISION_ENDPOINT


def main():
    context = zmq.Context()
    print("Subscribe to {}".format(VISION_ENDPOINT))
    socket = context.socket(zmq.SUB)
    socket.connect(VISION_ENDPOINT)
    socket.subscribe("")

    layout = [
        [sg.Image(filename='', key='raw_frame'),
         sg.Image(filename='', key='detection_frame')],

        [sg.Button("OK")]]

    # Create the window
    window = sg.Window("Demo", layout)

    while True:
        frame_bytes = socket.recv()
        # print(frame_bytes)

        vision_message = pickle.loads(frame_bytes)

        # print(img.shape)

        # Now you can process the image
        # cv2.imshow('image', img)
        # print("a1")
        # cv2.waitKey(1)
        # print("a2")

        event, values = window.read(timeout=20)
        # End program if user closes window or
        # presses the OK button
        if event == "OK" or event == sg.WIN_CLOSED:
            break

        frame = vision_message["frame"]
        detection_frame = vision_message["detection_frame"]

        frame_bytes = cv2.imencode('.png', frame)[1].tobytes()
        detection_frame_bytes = cv2.imencode('.png', detection_frame)[1].tobytes()

        window['raw_frame'].update(data=frame_bytes)
        window['detection_frame'].update(data=detection_frame_bytes)

    window.close()


if __name__:
    main()
