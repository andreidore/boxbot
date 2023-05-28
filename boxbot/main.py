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

    manager = Manager()
    manager.start()



if __name__ == '__main__':
    main()
