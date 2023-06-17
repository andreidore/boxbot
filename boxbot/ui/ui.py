"""

UI for the boxbot project.

"""

import pickle

import PySimpleGUI as sg
import cv2
import zmq

from boxbot.config import VISION_ENDPOINT


class UI():
    def __init__(self):
        print("UI init")

        self.context = zmq.Context()
        print("Subscribe to {}".format(VISION_ENDPOINT))
        self.vision_socket = self.context.socket(zmq.SUB)
        self.vision_socket.connect(VISION_ENDPOINT)
        self.vision_socket.subscribe("")

        layout = [
            [sg.Image(filename='', key='raw_frame'),
             sg.Image(filename='', key='detection_frame')],

            [sg.Button("OK")]]

        # Create the window
        self.window = sg.Window("BoxBot UI", layout)

    def start(self):
        print("UI start")

        while True:
            frame_bytes = self.vision_socket.recv()
            # print(frame_bytes)

            vision_message = pickle.loads(frame_bytes)

            # print(img.shape)

            # Now you can process the image
            # cv2.imshow('image', img)
            # print("a1")
            # cv2.waitKey(1)
            # print("a2")

            event, values = self.window.read(timeout=5)
            # End program if user closes window or
            # presses the OK button
            if event == "OK" or event == sg.WIN_CLOSED:
                break

            frame = vision_message["frame"]
            detection_frame = vision_message["detection_frame"]

            frame_bytes = cv2.imencode('.png', frame)[1].tobytes()
            detection_frame_bytes = cv2.imencode('.png', detection_frame)[1].tobytes()

            self.window['raw_frame'].update(data=frame_bytes)
            self.window['detection_frame'].update(data=detection_frame_bytes)

        self.window.close()


def main():
    ui = UI()
    ui.start()


if __name__ == '__main__':
    main()
