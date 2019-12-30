from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

# Canny edge dectection is an edge detection operator that uses a multi-stage algorithm to detect a wide range of edges in images.
# Canny edge detection is composed of 5 steps:
# 1. Noise reduction -> Gaussian filter to smooth image.
# 2. Gradient calculation -> find intensity gradient of image.
# 3. Non-maximum suppression -> Get rid of spurious response to edge detection.
# 4. Double threshold -> to data mine the potential edges.
# 5. Edge Tracking by Hysteresis -> to finalise the detection of edges suppressing all the other edges that are weak or not connected to strong edges.

img = cv.imread("sudoku.jpg", 0)
canny = cv.Canny(img, 100, 200)
cv.imshow("Canny Edge Detection", canny)

def update(x):
    canny = cv.Canny(img, cv.getTrackbarPos("Threshold 1", "Canny Edge Detection Thresholds"), cv.getTrackbarPos("Threshold 2", "Canny Edge Detection Thresholds"))
    cv.imshow("Canny Edge Detection", canny)

cv.namedWindow("Canny Edge Detection Thresholds")
cv.createTrackbar("Threshold 1", "Canny Edge Detection Thresholds", 100, 1000, update)
cv.createTrackbar("Threshold 2", "Canny Edge Detection Thresholds", 200, 1000, update)

titles = ["Image", "Canny Edge Detection"]
images = [img, canny]

# for i in range(len(images)):
#     plt.subplot(1, 2, i+1), plt.imshow(images[i], "gray")
#     plt.title(titles[i])
#     plt.xticks([]), plt.yticks([])

# while True:
#     plt.show()
cv.waitKey(0) & 0xFF
cv.destroyAllWindows();