import cv2
import numpy as np

img1 = cv2.imread("resources/dp_1.1.jpeg")
img1Resize = cv2.resize(img1, (200, 200))
img2 = cv2.imread("resources/dp_2.jpg")
img2Resize = cv2.resize(img2, (200, 200))

horStack = np.hstack((img1Resize, img1Resize, img2Resize))
verStack = np.vstack((img1Resize, img2Resize))


cv2.imshow("hor image", horStack)
cv2.imshow("ver image", verStack)
cv2.waitKey(0)