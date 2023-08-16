import cv2

image = cv2.imread("Screenshot 2023-08-02 at 22.24.38.png")

print(image.shape)

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)

parameters = cv2.aruco.DetectorParameters()

corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(image, dictionary,
                                                          parameters=parameters)

print(ids)

cv2.aruco.drawDetectedMarkers(image, corners, ids)

cv2.imwrite("aruco.png", image)
