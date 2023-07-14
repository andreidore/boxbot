from controller import AnsiCodes

print("This is " + AnsiCodes.RED_FOREGROUND + "red" + AnsiCodes.RESET + "!")

import json


class RobotManager:
    def __init__(self, params):
        self.robot = Supervisor()