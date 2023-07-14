from controller import Robot
from math import pi, sin

def main():
    print("Simulator controller.")

    TIME_STEP = 64
    robot = Robot()

    motor = robot.getDevice("left wheel motor")

    F = 2.0  # frequency 2 Hz
    t = 0.0  # elapsed simulation time

    while robot.step(TIME_STEP) != -1:
        position = sin(t * 2.0 * pi * F)
        motor.setPosition(position)
        t += TIME_STEP / 1000.0


if __name__ == "__main__":
    main()
