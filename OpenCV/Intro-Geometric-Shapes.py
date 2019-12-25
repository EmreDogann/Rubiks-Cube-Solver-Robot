import numpy as np
import cv2

#Read image using OpenCV.
img = cv2.imread("Alaska.jpg", -1)

#Create image using Numpy.
#img = np.zeros([512, 512, 3], np.uint8)

#Draw Line
img = cv2.line(img, (0,0), (255,255), (255,0,0), 100)
#Draw Arrow
img = cv2.arrowedLine(img, (0,255), (255,255), (0,0,255), 10)

#Draw Rectangle
img = cv2.rectangle(img, (384, 0), (510, 128), (0,0,255), 10)

#Draw Circle
img = cv2.circle(img, (477, 63), 63, (0,255,0), -1)

#Draw Text
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, "OpenCV", (10, 500), font, 4, (0, 0, 255), 5, cv2.LINE_AA)

cv2.imshow("Alaska", img)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()