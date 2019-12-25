import numpy as np
import cv2

img = cv2.imread("Alaska.jpg")
img2 = cv2.imread("opencv-logo.png")

print (img.shape)   #Returns a tuple of number of rows, columns, and channels
print (img.size)    #Returns total number of pixels
print (img.dtype)   #Returns image datatype
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

#ROI - Region of Interest
#[ymin:ymax, xmin:xmax]
tree = img[147:467, 25:162]
#[ymin:ymax, xmin:xmax]
img[100:420, 273:410] = tree

#Resize both images to make them the same size.
img = cv2.resize(img, (1200, 1000))
img2 = cv2.resize(img2, (1200, 1000))

#You cannot add to images together unless they are of the same size.
dst = cv2.add(img, img2)

#Add images with weights and scalar.
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0)

cv2.imshow("Alaska", dst)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()