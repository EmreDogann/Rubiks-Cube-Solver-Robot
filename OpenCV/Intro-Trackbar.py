import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

cv.namedWindow("Image")

cv.createTrackbar("B", "Image", 0, 255, nothing)
cv.createTrackbar("G", "Image", 0, 255, nothing)
cv.createTrackbar("R", "Image", 0, 255, nothing)

cv.createTrackbar("CP", "Image", 10, 400, nothing)

switch = "Color/Gray"
cv.createTrackbar(switch, "Image", 0, 1, nothing)

while(True):
    img = cv.imread("Alaska.jpg")

    # b = cv.getTrackbarPos("B", "Image")
    # g = cv.getTrackbarPos("G", "Image")
    # r = cv.getTrackbarPos("R", "Image")
    
    pos = cv.getTrackbarPos("CP", "Image")
    s = cv.getTrackbarPos(switch, "Image")

    font = cv.FONT_HERSHEY_COMPLEX
    cv.putText(img, str(pos), (50, 150), font, 2, (0, 0, 255), 5)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break

    if (s == 0):
        # img[:] = 0
        pass
    else: 
        # Set all pixels to current blue, green, and red channels.
        # img[:] = [b,g,r]

        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    img = cv.imshow("Image", img)
cv.destroyAllWindows()