""""
Main file of boxbot.
"""
import os

from dotenv import load_dotenv
from setproctitle import setproctitle # pylint: disable = no-name-in-module

from boxbot.config import __VERSION__
from boxbot.manager.manager import main as manager_main


def main():
    """
    Main function of boxbot.
    :return:
    """
    setproctitle("boxbot_manager")

    load_dotenv("properties_simulator.env")

    print("Start boxbot.")
    print(f"Version: {__VERSION__}")
    print("ENV:", os.getenv("ENV", "PROD"))
    print("SIM:", os.getenv("SIM"))

    # start manager
    manager_main()


if __name__ == '__main__':
    main()
