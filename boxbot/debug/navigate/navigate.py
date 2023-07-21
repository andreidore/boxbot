import time
from functools import partial
from threading import Thread

import cv2
import numpy as np
import zmq
from kivy.app import App
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

from boxbot.config import BOARD_MOTOR_VELOCITY_SERVICE, VISION_IMAGE_TOPIC
from boxbot.message.image_message_pb2 import ImageMessage
from boxbot.message.motor_velocity_message_pb2 import MotorVelocityMessage

context = zmq.Context()

left = 0
right = 0


class NavigateApp(App):

    def __init__(self):
        super().__init__()
        self.image_raw = None

        self.image_raw_thread = Thread(target=self._image_raw_callback, args=())
        self.image_raw_thread.start()

    def _left_button_on_press(self, button):
        print("Left button pressed")

        global left, right
        left = -10
        right = 10

    def _left_button_on_release(self, button):
        print("Left button pressed")

        global left, right
        left = 0
        right = 0

    def _forward_button_on_press(self, button):
        print("Forward button pressed")

        global left, right
        left = 10
        right = 10

    def _forward_button_on_release(self, button):
        print("Forward button released")

        global left, right
        left = 0
        right = 0

    def _right_button_on_press(self, button):
        print("Right button pressed", button)

        global left, right
        left = 10
        right = -10

    def _right_button_on_release(self, button):
        print("Right button released", button)

        global left, right
        left = 0
        right = 0

    def _build_navigate_menu(self):
        layout = GridLayout(cols=3)

        left_button = Button(text='Left', on_press=self._left_button_on_press, on_release=self._left_button_on_release)
        layout.add_widget(left_button)

        forward_button = Button(text='Forward',
                                on_press=self._forward_button_on_press, on_release=self._forward_button_on_release)
        layout.add_widget(forward_button)

        right_button = Button(text='Right', on_press=self._right_button_on_press,
                              on_release=self._right_button_on_release)
        layout.add_widget(right_button)

        return layout

    def build(self):
        root = BoxLayout(orientation='vertical')
        root.add_widget(self._build_navigate_menu())

        self.image_raw = Image(size_hint=(1, .8))
        root.add_widget(self.image_raw)

        return root

    def _update_image_raw(self, image, dt):
        print(image.shape)

        buf = cv2.flip(image, 0).tostring()

        texture = Texture.create(size=(image.shape[1], image.shape[0]))
        texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
        self.image_raw.texture = texture

    def _image_raw_callback(self):
        print("Start image raw handler thread")

        socket = context.socket(zmq.SUB)
        socket.connect(VISION_IMAGE_TOPIC)  # Connect to the server
        socket.setsockopt_string(zmq.SUBSCRIBE, '')

        # left = 0
        # right = 0

        while True:
            message = socket.recv()  # Wait for the reply from the server

            image_message = ImageMessage()
            image_message.ParseFromString(message)

            frame = np.frombuffer(image_message.image_bytes, dtype=np.uint8).reshape(image_message.height,
                                                                                     image_message.width,
                                                                                     image_message.channels)

            Clock.schedule_once(partial(self._update_image_raw, frame), 0)


def _motor_velocity_handler():
    print("Start motor velocity handler thread")

    socket = context.socket(zmq.REQ)  # REQ stands for REQuest, to represent a client
    socket.connect(BOARD_MOTOR_VELOCITY_SERVICE)  # Connect to the server

    # left = 0
    # right = 0

    while True:
        motor_velocity_message = MotorVelocityMessage()
        motor_velocity_message.left = left
        motor_velocity_message.right = right

        socket.send(motor_velocity_message.SerializeToString())  # Send the command
        message = socket.recv()  # Wait for the reply from the server

        time.sleep(0.1)


if __name__ == '__main__':
    motor_velocity = Thread(target=_motor_velocity_handler, args=())
    motor_velocity.start()

    NavigateApp().run()
