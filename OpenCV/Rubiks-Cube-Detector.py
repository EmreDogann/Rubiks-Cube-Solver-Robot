import cv2
import datetime
import numpy as np
import random
import math

capture = cv2.VideoCapture(0)

def callback(num):
    return

cv2.namedWindow('Settings', 0)
cv2.createTrackbar('Canny Thres 1', 'Settings', 87, 500, callback)
cv2.createTrackbar('Canny Thres 2', 'Settings', 325, 500, callback)
cv2.createTrackbar('Blur kSize', 'Settings', 9, 100, callback)
cv2.createTrackbar('Blur Sigma X', 'Settings', 75, 100, callback)
cv2.createTrackbar('Dilation Iterations', 'Settings', 2, 20, callback)
cv2.createTrackbar('Blob Area', 'Settings', 700, 1000, callback)

cv2.createTrackbar('Contour R', 'Settings', 0, 255, callback)
cv2.createTrackbar('Contour G', 'Settings', 0, 255, callback)
cv2.createTrackbar('Contour B', 'Settings', 255, 255, callback)

cv2.createTrackbar('Open Kernel Size', 'Settings', 7, 20, callback)
cv2.createTrackbar('Closed Kernel Size', 'Settings', 5, 20, callback)
cv2.createTrackbar('Open Iterations', 'Settings', 2, 20, callback)
cv2.createTrackbar('Closed Iterations', 'Settings', 5, 20, callback)
cv2.createTrackbar('Exposure', 'Settings', 5, 12, callback)

cv2.namedWindow('Color Thresholds', 0)
cv2.createTrackbar('Red1 Min Hue', 'Color Thresholds', 175, 180, callback)
cv2.createTrackbar('Red1 Max Hue', 'Color Thresholds', 180, 180, callback)
cv2.createTrackbar('Red1 Min Sat', 'Color Thresholds', 210, 255, callback)
cv2.createTrackbar('Red1 Max Sat', 'Color Thresholds', 255, 255, callback)
cv2.createTrackbar('Red1 Min Val', 'Color Thresholds', 229, 255, callback)
cv2.createTrackbar('Red1 Max Val', 'Color Thresholds', 255, 255, callback)

cv2.createTrackbar('Red2 Min Hue', 'Color Thresholds', 0, 180, callback)
cv2.createTrackbar('Red2 Max Hue', 'Color Thresholds', 4, 180, callback)
cv2.createTrackbar('Red2 Min Sat', 'Color Thresholds', 133, 255, callback)
cv2.createTrackbar('Red2 Max Sat', 'Color Thresholds', 255, 255, callback)
cv2.createTrackbar('Red2 Min Val', 'Color Thresholds', 59, 255, callback)
cv2.createTrackbar('Red2 Max Val', 'Color Thresholds', 255, 255, callback)

cv2.createTrackbar('Blue Min Hue', 'Color Thresholds', 102, 180, callback)
cv2.createTrackbar('Blue Max Hue', 'Color Thresholds', 113, 180, callback)
cv2.createTrackbar('Blue Min Sat', 'Color Thresholds', 172, 255, callback)
cv2.createTrackbar('Blue Max Sat', 'Color Thresholds', 255, 255, callback)
cv2.createTrackbar('Blue Min Val', 'Color Thresholds', 75, 255, callback)
cv2.createTrackbar('Blue Max Val', 'Color Thresholds', 255, 255, callback)

cv2.createTrackbar('Yellow Min Hue', 'Color Thresholds', 18, 180, callback)
cv2.createTrackbar('Yellow Max Hue', 'Color Thresholds', 32, 180, callback)
cv2.createTrackbar('Yellow Min Sat', 'Color Thresholds', 40, 255, callback)
cv2.createTrackbar('Yellow Max Sat', 'Color Thresholds', 255, 255, callback)
cv2.createTrackbar('Yellow Min Val', 'Color Thresholds', 75, 255, callback)
cv2.createTrackbar('Yellow Max Val', 'Color Thresholds', 202, 255, callback)

cv2.createTrackbar('Orange Min Hue', 'Color Thresholds', 14, 180, callback)
cv2.createTrackbar('Orange Max Hue', 'Color Thresholds', 24, 180, callback)
cv2.createTrackbar('Orange Min Sat', 'Color Thresholds', 103, 255, callback)
cv2.createTrackbar('Orange Max Sat', 'Color Thresholds', 255, 255, callback)
cv2.createTrackbar('Orange Min Val', 'Color Thresholds', 105, 255, callback)
cv2.createTrackbar('Orange Max Val', 'Color Thresholds', 255, 255, callback)

cv2.createTrackbar('Green Min Hue', 'Color Thresholds', 70, 180, callback)
cv2.createTrackbar('Green Max Hue', 'Color Thresholds', 89, 180, callback)
cv2.createTrackbar('Green Min Sat', 'Color Thresholds', 24, 255, callback)
cv2.createTrackbar('Green Max Sat', 'Color Thresholds', 255, 255, callback)
cv2.createTrackbar('Green Min Val', 'Color Thresholds', 59, 255, callback)
cv2.createTrackbar('Green Max Val', 'Color Thresholds', 255, 255, callback)

cv2.createTrackbar('White Min Hue', 'Color Thresholds', 0, 180, callback)
cv2.createTrackbar('White Max Hue', 'Color Thresholds', 180, 180, callback)
cv2.createTrackbar('White Min Sat', 'Color Thresholds', 0, 255, callback)
cv2.createTrackbar('White Max Sat', 'Color Thresholds', 255, 255, callback)
cv2.createTrackbar('White Min Val', 'Color Thresholds', 130, 255, callback)
cv2.createTrackbar('White Max Val', 'Color Thresholds', 255, 255, callback)

def computeContours(frame):
    colors = {
        'red1': ([cv2.getTrackbarPos('Red1 Min Hue', 'Color Thresholds'), cv2.getTrackbarPos('Red1 Min Sat', 'Color Thresholds'), cv2.getTrackbarPos('Red1 Min Val', 'Color Thresholds')], [cv2.getTrackbarPos('Red1 Max Hue', 'Color Thresholds'), cv2.getTrackbarPos('Red1 Max Sat', 'Color Thresholds'), cv2.getTrackbarPos('Red1 Max Val', 'Color Thresholds')]),  # Red Hue = 180
        'red2': ([cv2.getTrackbarPos('Red2 Min Hue', 'Color Thresholds'), cv2.getTrackbarPos('Red2 Min Sat', 'Color Thresholds'), cv2.getTrackbarPos('Red2 Min Val', 'Color Thresholds')], [cv2.getTrackbarPos('Red2 Max Hue', 'Color Thresholds'), cv2.getTrackbarPos('Red2 Max Sat', 'Color Thresholds'), cv2.getTrackbarPos('Red2 Max Val', 'Color Thresholds')]),  # Red Hue = 0
        'blue': ([cv2.getTrackbarPos('Blue Min Hue', 'Color Thresholds'), cv2.getTrackbarPos('Blue Min Sat', 'Color Thresholds'), cv2.getTrackbarPos('Blue Min Val', 'Color Thresholds')], [cv2.getTrackbarPos('Blue Max Hue', 'Color Thresholds'), cv2.getTrackbarPos('Blue Max Sat', 'Color Thresholds'), cv2.getTrackbarPos('Blue Max Val', 'Color Thresholds')]),   # Blue
        'yellow': ([cv2.getTrackbarPos('Yellow Min Hue', 'Color Thresholds'), cv2.getTrackbarPos('Yellow Min Sat', 'Color Thresholds'), cv2.getTrackbarPos('Yellow Min Val', 'Color Thresholds')], [cv2.getTrackbarPos('Yellow Max Hue', 'Color Thresholds'), cv2.getTrackbarPos('Yellow Max Sat', 'Color Thresholds'), cv2.getTrackbarPos('Yellow Max Val', 'Color Thresholds')]),  # Yellow
        'orange': ([cv2.getTrackbarPos('Orange Min Hue', 'Color Thresholds'), cv2.getTrackbarPos('Orange Min Sat', 'Color Thresholds'), cv2.getTrackbarPos('Orange Min Val', 'Color Thresholds')], [cv2.getTrackbarPos('Orange Max Hue', 'Color Thresholds'), cv2.getTrackbarPos('Orange Max Sat', 'Color Thresholds'), cv2.getTrackbarPos('Orange Max Val', 'Color Thresholds')]),  # Orange
        'green': ([cv2.getTrackbarPos('Green Min Hue', 'Color Thresholds'), cv2.getTrackbarPos('Green Min Sat', 'Color Thresholds'), cv2.getTrackbarPos('Green Min Val', 'Color Thresholds')], [cv2.getTrackbarPos('Green Max Hue', 'Color Thresholds'), cv2.getTrackbarPos('Green Max Sat', 'Color Thresholds'), cv2.getTrackbarPos('Green Max Val', 'Color Thresholds')]),   # Green
        'white': ([cv2.getTrackbarPos('White Min Hue', 'Color Thresholds'), cv2.getTrackbarPos('White Min Sat', 'Color Thresholds'), cv2.getTrackbarPos('White Min Val', 'Color Thresholds')], [cv2.getTrackbarPos('White Max Hue', 'Color Thresholds'), cv2.getTrackbarPos('White Max Sat', 'Color Thresholds'), cv2.getTrackbarPos('White Max Val', 'Color Thresholds')])   # White
    }

    frame2 = frame.copy()

    mask = np.zeros([frame2.shape[0], frame2.shape[1]], dtype=np.uint8)

    open_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cv2.getTrackbarPos('Open Kernel Size', 'Settings'),cv2.getTrackbarPos('Open Kernel Size', 'Settings')))
    close_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (cv2.getTrackbarPos('Closed Kernel Size', 'Settings'),cv2.getTrackbarPos('Closed Kernel Size', 'Settings')))
    for color, (lower, upper) in colors.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        color_mask = cv2.inRange(frame2, lower, upper)
        
        color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, open_kernel, iterations=cv2.getTrackbarPos('Open Iterations', 'Settings'))
        color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_CLOSE, close_kernel, iterations=cv2.getTrackbarPos('Closed Iterations', 'Settings'))

        mask = cv2.bitwise_or(mask, color_mask)

    frame2 = cv2.bitwise_and(frame2, frame2, mask=mask)

    gaus = cv2.getTrackbarPos('Blur kSize', 'Settings')

    if gaus == 0:
        gaus = 1;
    else:
        count = gaus % 2 
        if (count == 0):
            gaus += 1

    canny = cv2.Canny(
        cv2.bilateralFilter(cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY), gaus, cv2.getTrackbarPos('Blur Sigma X', 'Settings'), cv2.getTrackbarPos('Blur Sigma X', 'Settings')),
        cv2.getTrackbarPos('Canny Thres 1', 'Settings'),
        cv2.getTrackbarPos('Canny Thres 2', 'Settings'))

    cv2.imshow("Canny Edge", canny);

    kernel = np.ones((3,3), np.uint8)
    dilated = cv2.dilate(canny, kernel, iterations=cv2.getTrackbarPos('Dilation Iterations', 'Settings'))

    (contours, hierarchy) = cv2.findContours(dilated.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Index used to remove nested squares.
    index = 0
    for cnt in contours:
        if (hierarchy[0,index,3] != -1):
            epsilon = 0.01*cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            area = cv2.contourArea(approx, False)
            arch = cv2.arcLength(approx, True)

            squareness = 4 * math.pi * area / (arch * arch)

            if ((squareness >= 0.6 and squareness <= 1 or len(approx) == 4) and area > cv2.getTrackbarPos('Blob Area', 'Settings')):
                cv2.drawContours(frame2, [approx], 0, (cv2.getTrackbarPos('Contour B', 'Settings'), cv2.getTrackbarPos('Contour G', 'Settings'), cv2.getTrackbarPos('Contour R', 'Settings')), 3)
            else:
                cv2.drawContours(frame2, [approx], 0, (0, 0, 255), 3)
        index += 1


    return frame2;

while (capture.isOpened()):
    ret, frame = capture.read()

    if ret:
        capture.set(cv2.CAP_PROP_EXPOSURE, (cv2.getTrackbarPos('Exposure', 'Settings')+1)*-1)
        newFrame = computeContours(frame);

        cv2.imshow("Webcam Capture", frame);
        cv2.imshow("Contours", newFrame);

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
