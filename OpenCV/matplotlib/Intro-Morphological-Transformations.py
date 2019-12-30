import numpy as np
from matplotlib import pyplot as plt
import cv2 as cv

def changeDilation(x):
    dilation = cv.dilate(mask, kernal, iterations=x)
    images[2] = dilation
    updatePlot()

def changeErosion(x):
    erosion = cv.erode(mask, kernal, iterations=x)
    images[3] = erosion
    updatePlot()

def updatePlot():
    plt.clf()
    for i in range(len(images)):
        plt.subplot(2, 4, i+1), plt.imshow(images[i], "gray")
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.show()

# Morphological transformations -> simple operations based on the image shape -> normally performed on binary images
# Two things required for morphological transformaitons.
# 1st -> the original image.
# 2nd -> Structuring element/kernel -> describes how to change the value of tany pixel by combining it with different amounts of the neighboring pixels.

img = cv.imread("Smarties.jpg", cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

cv.namedWindow("Morphological Transformations")
cv.createTrackbar("Dilation Iterations", "Morphological Transformations", 1, 50, changeDilation)
cv.createTrackbar("Erosion Iterations", "Morphological Transformations", 1, 5, changeErosion)

# Kernal is normally some shape which we want to apply onto some image.
kernal = np.ones((5,5), np.uint8)
dilation = cv.dilate(mask, kernal, iterations=20)
erosion = cv.erode(mask, kernal, iterations=1)
# First erosion will be performed, then dilation.
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
# Inverse of opening -> first dilation, then erosion.
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
# Morphological gradient -> difference bettween dilation and erosion of an image.
gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)
# TopHat -> Difference between an image and opening of the image.
topHat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)

titles = ["Image", "Mask", "Dilation", "Erosion", "Opening", "Closing", "Morphological Gradient", "TopHat"]
images = np.array([img, mask, dilation, erosion, opening, closing, gradient, topHat])

updatePlot()