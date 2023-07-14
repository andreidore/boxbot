import importlib
import os
from multiprocessing import Process

import zmq
from setproctitle import setproctitle  # type: ignore


class Manager:
    managed_process = {
        # "boxbot_controller": "boxbot.controller.controller",
        # "boxbot_board": "boxbot.board.board",
        "boxbot_navigation": "boxbot.navigation.navigation",
        "boxbot_vision": "boxbot.vision.vision",
        # "boxbot_ui": "boxbot.ui.ui",
        "boxbot_web": "boxbot.web.web",
        # "planing": "boxbot.planing.plan",
    }

    managed_process_sim = {
        # "boxbot_controller": "boxbot.controller.controller",
        "boxbot_board": "boxbot.board.board",

    }

    current_managed_process = {}

    running = {}

    def __init__(self):
        print("Init manager")

        self.context = zmq.Context()

    def start(self):
        print("Start manager")

        if os.getenv("NO_PROCESS_MANAGER") is None:

            if os.getenv("SIM"):
                self.current_managed_process = self.managed_process_sim
            else:
                self.current_managed_process = self.managed_process

            for process_name in self.current_managed_process:
                print("Launch process: " + process_name)

                process = Process(name=process_name, target=_launch,
                                  args=(process_name, self.current_managed_process[process_name]))

                process.start()

                self.running[process_name] = process

        else:
            print("No process manager started.")


def _launch(process_name, process_path):
    try:

        # import the process
        mod = importlib.import_module(process_path)

        # rename the process
        setproctitle(process_name)

        # exec the process
        mod.main()
    except KeyboardInterrupt:
        # cloudlog.info("child %s got ctrl-c" % proc)
        pass
    except Exception:
        # can't install the crash handler becuase sys.excepthook doesn't play nice
        # with threads, so catch it here.
        # crash.capture_exception()
        raise


def main():
    """
    Manager.
    :return:
    """

    manager = Manager()
    manager.start()
