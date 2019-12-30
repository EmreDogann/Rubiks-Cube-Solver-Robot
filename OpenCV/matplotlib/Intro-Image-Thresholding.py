import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

# Threasholding is a segmentation technique used for separating an object from it's background. Compare each pixel of an image with a pre-defined threshold value.
# This divides all the pixels of the input image into 2 groups.
# 1st group -> pixels with intensity lower than threshold value.
# 2nd group -> pixels with intensity greater than threshold value.

img = cv.imread('Gradient.jpg', 0)
# Binary thresholding -> either 0 or 1.
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)

# Inverse binary thresholding -> either 0 or 1, but inverted.
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)

# Truncated thresholding -> after the threshold, the pixel value will not change.
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# To zero thresholding -> below threshold, value will be 0. After threshold, value unchanged.
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)

# To zero inverse thresholding -> same as TOZERO but inverted.
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ["Original Image", "Binary", "Binary Inverse", "Trunc", "To Zero", "To Zero Inverse"]
images = [img, th1, th2, th3, th4, th5]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    # Removes x and y numbers.
    # plt.xticks(()), plt.yticks([])

plt.show()

# cv.imshow("Image", img)
# cv.imshow("Threshold", th1)

# cv.waitKey(0) & 0xFF
# cv.destroyAllWindows()