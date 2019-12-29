import numpy as np
import cv2 as cv

def nothing(x):
    pass

cap = cv.VideoCapture(0)
cv.namedWindow("Tracking")
cv.createTrackbar("Lower Hue", "Tracking", 0, 255, nothing)
cv.createTrackbar("Upper Hue", "Tracking", 255, 255, nothing)
cv.createTrackbar("Lower Saturation", "Tracking", 0, 255, nothing)
cv.createTrackbar("Upper Saturation", "Tracking", 255, 255, nothing)
cv.createTrackbar("Lower Value", "Tracking", 0, 255, nothing)
cv.createTrackbar("Upper Value", "Tracking", 255, 255, nothing)

while True:
    frame = cv.imread("Smarties.jpg")
    frame = cv.resize(frame, (1280, 720))

    #_, frame = cap.read()

    # Convert frame to hsv values.
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_hue = cv.getTrackbarPos("Lower Hue", "Tracking")
    upper_hue = cv.getTrackbarPos("Upper Hue", "Tracking")
    lower_saturation = cv.getTrackbarPos("Lower Saturation", "Tracking")
    upper_saturation = cv.getTrackbarPos("Upper Saturation", "Tracking")
    lower_value = cv.getTrackbarPos("Lower Value", "Tracking")
    upper_value = cv.getTrackbarPos("Upper Value", "Tracking")

    # Lower bound
    lower_b = np.array([lower_hue, lower_saturation, lower_value])
    # Upper bound
    upper_b = np.array([upper_hue, upper_saturation, upper_value])

    # Create a mask with areas of the image containing colors within the lower and upper bounds.
    mask = cv.inRange(hsv, lower_b, upper_b)
    # Comnbine original frame with mask to get final frame with only the colors specified in the lower and upper bound.
    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow("frame", frame)
    cv.imshow("mask", mask)
    cv.imshow("res", res)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()