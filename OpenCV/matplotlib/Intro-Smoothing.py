from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

img = cv.imread("Alaska.jpg", -1)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Low-Pass Filters helps in removing noise/blurring images.
# High-Pass Filters helps in finding edges in images.

kernal = np.ones((5,5), np.float32)/25
# Homogeneous filter -> each output pixel is the mean of its kernal neighbours.
dst = cv.filter2D(img, -1, kernal)

blur = cv.blur(img, (5,5))
# Gaussian filter is nothing but using different-weight-kernal, in both x and y directions.
# Designed to remove high-frequence noise from an image.
gaussian = cv.GaussianBlur(img, (5,5), 0)

# Median filter -> replaces each pixel's value with the median of its neighbouring pixels
# Great when dealing with "salt and pepper" noise.
median = cv.medianBlur(img, 5)

# Smooths the image while retaining the sharp edges.
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)

titles = ["Image", "2D Convolution", "Blur", "Gaussian", "Median", "Bilateral"]
images = [img, dst, blur, gaussian, median, bilateralFilter]

for i in range(len(images)):
    plt.subplot(3, 2, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()