"""

    ArucoManager class

    https://betterprogramming.pub/getting-started-with-aruco-markers-b4823a43973c


"""
import cv2


class ArucoManager:

    def __init__(self):
        print("Init landmark.")

        self.dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250)

        # Create parameters to be used when detecting markers:
        self.parameters = cv2.aruco.DetectorParameters()

    def update(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(gray_frame, self.dictionary,
                                                                  parameters=self.parameters)

        # Draw rejected markers:
        aruco_frame = cv2.aruco.drawDetectedMarkers(image=gray_frame, corners=rejectedImgPoints,
                                                    borderColor=(0, 0, 255))

        return aruco_frame
