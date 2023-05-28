import zmq


class Manager:
    managed_process = {
        "vision": "boxbot.vision.vision",
        "sensor": "boxbot.sensor.sensor",
        "planing": "boxbot.planing.plan",
    }

    running = {}

    def __init__(self):
        print("Init manager")

        self.context = zmq.Context()

    def start(self):
        print("Start manager")

        for process_name in self.managed_process:
            self._launch(process_name)

    def _launch(self, process_name):
        print("Launch process: " + process_name)

        self.running[process_name] = "1"
