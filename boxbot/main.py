""""
Main file of boxbot.
"""

import os

from manager.manager import Manager


def main():
    """
    Main function of boxbot.
    :return:
    """
    print("Start boxbot.")

    if os.getenv("NO_MANAGER") is None:
        manager = Manager()
        manager.start()
    else:
        print("No manager started.")


if __name__ == '__main__':
    main()
