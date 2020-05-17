import cv2
import numpy as np

def empty(a):
    pass

imgPath = "resources/lambo.png"
img = cv2.imread(imgPath)
imgResize = cv2.resize(img, (256, 256))
imgHsv = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)

# New window creation
cv2.namedWindow("trackbars")
cv2.resizeWindow("trackbars", 640, 240)
cv2.createTrackbar("hue min", "trackbars", 0, 179, empty)
cv2.createTrackbar("hue max", "trackbars", 20, 179, empty)
cv2.createTrackbar("sat min", "trackbars", 110, 255, empty)
cv2.createTrackbar("sat max", "trackbars", 245, 255, empty)
cv2.createTrackbar("val min", "trackbars", 153, 255, empty)
cv2.createTrackbar("val max", "trackbars", 255, 255, empty)


while True:
    h_min = cv2.getTrackbarPos("hue min", "trackbars")
    h_max = cv2.getTrackbarPos("hue max", "trackbars")
    s_min = cv2.getTrackbarPos("sat min", "trackbars")
    s_max = cv2.getTrackbarPos("sat max", "trackbars")
    v_min = cv2.getTrackbarPos("val min", "trackbars")
    v_max = cv2.getTrackbarPos("val max", "trackbars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHsv, lower, upper)
    imgResult = cv2.bitwise_and(imgResize, imgResize, mask=mask)

    horStack = np.hstack([imgResize, imgHsv])

    cv2.imshow("hstack result", horStack)
    cv2.imshow("mask result", mask)
    cv2.imshow("image result", imgResult)
    cv2.waitKey(1)