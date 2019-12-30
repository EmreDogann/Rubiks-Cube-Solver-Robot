import numpy as np
import cv2 as cv

# Adaptive thresholding -> where threshold value is calculated for smaller regions of the image. So the threshold is not the same for every pixel
# Useful for when image has different lighting conditions in different regions of the image.
# Therefore, this method gives better results for images with non-uniform illumination.

img = cv.imread('Sudoku.jpg', 0)
# Binary thresholding -> either 0 or 1.
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 5)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 5)

cv.imshow("Image", img)
cv.imshow("Threshold", th1)
cv.imshow("Adpative Mean Threshold", th2)
cv.imshow("Adpative Gaussian Threshold", th3)

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()