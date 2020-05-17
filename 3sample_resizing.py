import cv2

image = cv2.imread("resources/dp_1.1.jpeg")

print(image.shape)

resizedImage = cv2.resize(image, (240, 240))
imageGray = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)

print(imageGray.shape)

# Cropping an image - [HEIGHT, WIDTH]
imageCrop = resizedImage[0:100, 0:200]

cv2.imshow('org image', resizedImage)
cv2.imshow('cropped image', imageCrop)
cv2.waitKey(0)