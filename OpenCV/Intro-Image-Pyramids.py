import numpy as np
import cv2 as cv

img = cv.imread("Alaska.jpg", -1)
layer = img.copy()
gaussian = [layer]

# Image pyramid ->  nothing but repeated smoothing and subsampling -> useful for blending and reconstruction of images.
# There are two types of image pyramids:
# Gaussian Pyramid -> just repeat filtering and subsampling of an image.

# lower_res = cv.pyrDown(img)
# lower_res2 = cv.pyrDown(lower_res)
# higher_res = cv.pyrUp(lower_res2)
for i in range(6):
    layer = cv.pyrDown(layer)
    gaussian.append(layer)
    # cv.imshow(str(i), layer)

# Laplacian Pyramid -> formed from gaussian pyramids.
# No exclusive method for laplacian pyramid.
# Formed by the difference between a given level in a gaussian pyramid and the expanded (upscaled) version of its upper level (next level up) in the gaussian pyamid.
layer = gaussian[5]
cv.imshow("Upper Level Gaussian Pyramid", layer)
laplacian = [layer]

for i in range(5, 0, -1):
    size = (gaussian[i - 1].shape[1], gaussian[i - 1].shape[0])
    gaussian_extended = cv.pyrUp(gaussian[i], dstsize=size)
    laplacian = cv.subtract(gaussian[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)

cv.imshow("Original Image", img)
# cv.imshow("PyrDown", lower_res)
# cv.imshow("PyrDown2", lower_res2)
# cv.imshow("PyrUp", higher_res)
cv.waitKey(0) & 0xFF
cv.destroyAllWindows()