import argparse


def main():
    parser = argparse.ArgumentParser(description='Send a command.')
    parser.add_argument('command', type=str, help='Command')

    args = parser.parse_args()

    print("Command: " + args.command)


if __name__ == '__main__':
    main()
