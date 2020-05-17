import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8) # size of matrix - 256x256

print(image.shape)
# image[:] = 255,0,0
image[300:400, 100:200] = 255,0,0
image[100:200, 300:400] = 255,0,0

# Drawing a line
cv2.line(image, (0, 0), (image.shape[1], image.shape[0]), (255, 0, 255), 1)

# Drawing a rectangle
cv2.rectangle(image, (10, 10), (100, 150), (0, 0, 255), 2)
cv2.rectangle(image, (100, 100), (150, 200), (0, 0, 255), cv2.FILLED)

# a circle
cv2.circle(image, (400, 50), 1, (0, 0, 255), 2)

# putText on image
cv2.putText(image, "OPENCV ", (350, 450), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 1)

cv2.imshow("image", image)
cv2.waitKey(0)