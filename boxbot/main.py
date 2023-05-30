""""
Main file of boxbot.
"""

from setproctitle import setproctitle

from boxbot.config import __VERSION__
from manager.manager import main as manager_main


def main():
    """
    Main function of boxbot.
    :return:
    """
    setproctitle("boxbot_manager")

    print("Start boxbot.")
    print(f"Version: {__VERSION__}")

    # start manager
    manager_main()


if __name__ == '__main__':
    main()
