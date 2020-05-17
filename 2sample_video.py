import cv2
# Add the video Path like this - cv2.VideoCapture("resources/test_video.mp4")
# default web cam - ID_VALUE = 0
# More than 1 web cam - ID_VALUE = 1
# set the width - ID_VALUE = 3
# set the height - ID_VALUE = 4
# set the brighness - ID_VALUE = 10, Range = 100

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# cap.set(10, 100)

while True:
    success, img = cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

