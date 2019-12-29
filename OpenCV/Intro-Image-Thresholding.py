import numpy as np
import cv2 as cv

img = cv.imread('Alaska.jpg', 0)

cv.imshow("Image", img)

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()