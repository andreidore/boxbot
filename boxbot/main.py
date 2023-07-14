""""
Main file of boxbot.
"""
import os

from setproctitle import setproctitle

from boxbot.config import __VERSION__
from boxbot.manager.manager import main as manager_main


def main():
    """
    Main function of boxbot.
    :return:
    """
    setproctitle("boxbot_manager")

    print("Start boxbot.")
    print("ENV:", os.getenv("ENV", "PROD"))
    print("SIM:", os.getenv("SIM", True))
    print(f"Version: {__VERSION__}")

    # start manager
    manager_main()


if __name__ == '__main__':
    main()
