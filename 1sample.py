import cv2
import numpy as np
print('package imported')

image = cv2.imread("resources/dp_1.1.jpeg")
resizedImage = cv2.resize(image, (240, 240))
kernel = np.ones((5, 5), np.uint8)

# cvtColor = converts image to different image spaces
# here, converting to grayscale. Generally an image is in BGR.
imageGray = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
imageBlur = cv2.GaussianBlur(imageGray, (7, 7), 0)

# Next, we need to find edge detector using canny function
# Need to set 2 thresholds. Like (100, 100) - More edges, (150, 200) - Less edges
imageCanny = cv2.Canny(resizedImage, 150, 200)

# Next, Dilation - edges are not clearly visible/connected due to their thickness
# Require KernelMatrix, iterations = how much thickness we need
imageDilate = cv2.dilate(imageCanny, kernel, iterations=1)

# Next, erod - edges are not clearly visible/connected due to their thickness
# Require KernelMatrix, iterations = how much thinness we need
imageErode = cv2.erode(imageDilate, kernel, iterations=1)


cv2.imshow("original image", resizedImage)
cv2.imshow("gray image", imageGray)
cv2.imshow("blur image", imageBlur)
cv2.imshow("canny image", imageCanny)
cv2.imshow("dilate image", imageDilate)
cv2.imshow("erode image", imageErode)
cv2.waitKey(0)