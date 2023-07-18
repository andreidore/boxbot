import time
from threading import Thread

import zmq
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from boxbot.config import BOARD_MOTOR_VELOCITY_ENDPOINT
from boxbot.message.motor_velocity_pb2 import MotorVelocity

context = zmq.Context()

left = 0
right = 0


class NavigateApp(App):

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

        return root


def _motor_velocity_handler():
    print("Start motor velocity handler thread")

    socket = context.socket(zmq.REQ)  # REQ stands for REQuest, to represent a client
    socket.connect(BOARD_MOTOR_VELOCITY_ENDPOINT)  # Connect to the server

    # left = 0
    # right = 0

    while True:
        motor_speed = MotorVelocity()
        motor_speed.left = left
        motor_speed.right = right

        socket.send(motor_speed.SerializeToString())  # Send the command
        message = socket.recv()  # Wait for the reply from the server

        time.sleep(0.1)


if __name__ == '__main__':
    motor_velocity = Thread(target=_motor_velocity_handler, args=())
    motor_velocity.start()

    NavigateApp().run()
