from matplotlib import pyplot as plt
import cv2 as cv

img = cv.imread("Alaska.jpg", -1)
cv.imshow("Image", img)
img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img2)
plt.xticks([]), plt.yticks([])
plt.show()

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()