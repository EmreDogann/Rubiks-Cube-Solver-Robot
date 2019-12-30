import cv2

img = cv2.imread("Alaska.jpg", -1)

print (img)

cv2.imshow("Alaska", img)
cv2.waitKey(5000) & 0xFF
cv2.destroyAllWindows()

cv2.imwrite("Alaska_copy.jpg", img)