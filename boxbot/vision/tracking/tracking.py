import numpy as np
from filterpy.common import Q_discrete_white_noise
from filterpy.kalman import KalmanFilter


def main():
    filter = KalmanFilter(dim_x=2, dim_z=1)

    Q_std = 0.01
    R_std = 5
    dt = 1.

    filter.x = np.array([-10,0])
    filter.P = np.eye(2) * 500
    filter.R = np.eye(1) * R_std
    filter.Q = Q_discrete_white_noise(dim=2, dt=dt, var=Q_std)
    filter.F = np.array([[1., dt], [0., 1.]])
    filter.H = np.array([[1., 0.]])

    measurements = [1, 2, 3, 4, 5]

    for z in measurements:
        filter.predict()
        filter.update(z)
        print(filter.x)


if __name__ == '__main__':
    main()
