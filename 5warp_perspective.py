import cv2
import numpy as np

img = cv2.imread("resources/cards.jpg")
print(img.shape)

width, height = 250, 350
pt1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]])
pt2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pt1, pt2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("org image", img)
cv2.imshow("warp image", imgOutput)
cv2.waitKey(0)