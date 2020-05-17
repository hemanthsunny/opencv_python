import cv2
import numpy as np
from stackImages import *

def getContors(image):
    # To find outer corners, node = cv2.RETR_EXTERNAL
    # Also, can request all information or approximation for compressed values
    contors, hierarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contor in contors:
        contorArea = cv2.contourArea(contor)
        print("area", contorArea)
        # To ignore shapes, less than 1000 area
        if contorArea > 1000:
            cv2.drawContours(imgCopy, contor, -1, (255, 0, 0), 4)
            perimeter = cv2.arcLength(contor, True)
            print('perimeter', perimeter)
            cornerPoints = cv2.approxPolyDP(contor, 0.02*perimeter, True)
            cornerPointsLen = len(cornerPoints)
            x, y, w, h = cv2.boundingRect(cornerPoints)

            if cornerPointsLen == 3: objectType = "Tri"
            elif cornerPointsLen == 4:
                aspectRatio = w / float(h)
                if aspectRatio > 0.95 and aspectRatio < 1.05:
                    objectType = "Squ"
                else:
                    objectType = "Rect"
            elif cornerPointsLen > 4: objectType = "Cir"
            else: objectType = "None"

            cv2.rectangle(imgCopy, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(imgCopy, objectType, (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)


    pass

imgPath = "resources/shapes.png"
img = cv2.imread(imgPath)
imgResize = cv2.resize(img, (512, 512))
imgCopy = imgResize.copy()

imgGrey = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGrey, (7,7), 0.5)
imgCanny = cv2.Canny(imgGrey, 50, 50)
imgBlank = np.zeros_like(imgResize)

getContors(imgCanny)

stackImgs = stackImages(0.5, ([imgResize, imgGrey, imgBlur], [imgCanny, imgCopy, imgBlank]))
cv2.imshow("stack imgs", stackImgs)
cv2.waitKey(0)