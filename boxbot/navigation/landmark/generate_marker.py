import cv2
import numpy as np

ID = 1
DICT_NAME = "4_4_100"

dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)

maker_image = np.zeros((200, 200), dtype=np.uint8)

dictionary.generateImageMarker(0, 200, maker_image)

print(maker_image.shape)

cv2.imwrite(f"marker_{DICT_NAME}_{ID}.png", maker_image)
