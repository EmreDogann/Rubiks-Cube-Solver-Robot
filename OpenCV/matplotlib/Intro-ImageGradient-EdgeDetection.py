from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

# Image gradient -> directional change in the intensity or color in an image.

img = cv.imread("Sudoku.jpg", cv.IMREAD_GRAYSCALE)

# Returns edges in image -> i.e. sharp directional changes in the intensity or color of the image.
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))

# SobelX -> Directional change in the vertical direction -> vertical edge detection.
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
# SobelY -> Directional change in the horizontal direction -> horizontal edge detection.
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# Combine sobelX and sobelY.
sobelCombined = cv.bitwise_or(sobelX, sobelY);

titles = ["Image", "Laplacian", "SobelX", "SobelY", "SobelCombined"]
images = [img, lap,  sobelX, sobelY, sobelCombined]

for i in range(len(images)):
    plt.subplot(3, 2, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()