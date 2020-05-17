# Cascades - Train and generate a cascade file (in XML formats)
# Opencv has default cascades - numberPlates, eyes, fullbody
# Can create custom cascades - Ref: https://github.com/opencv/opencv/tree/master/data

import cv2
import numpy as np

cascade = cv2.CascadeClassifier("resources/cascades/haarcascade_frontalface_default.xml")
image = cv2.imread("resources/dp_1.1.jpeg")
imgGrey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

facesInCascade = cascade.detectMultiScale(imgGrey, 1.1, 4)

for x,y,w,h in facesInCascade:
    cv2.rectangle(image, (x,y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow("org img", image)
cv2.waitKey(0)