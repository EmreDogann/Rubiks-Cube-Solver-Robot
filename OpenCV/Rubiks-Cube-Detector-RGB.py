import cv2
import numpy as np
import math

capture = cv2.VideoCapture(0)

def callback(num):
    return

cv2.namedWindow('Settings', 0)
cv2.createTrackbar('Canny Thres 1', 'Settings', 87, 500, callback)
cv2.createTrackbar('Canny Thres 2', 'Settings', 325, 500, callback)
cv2.createTrackbar('Blur kSize', 'Settings', 10, 100, callback)
cv2.createTrackbar('Blur Sigma X', 'Settings', 100, 100, callback)
cv2.createTrackbar('Dilation Iterations', 'Settings', 3, 20, callback)
cv2.createTrackbar('Blob Area', 'Settings', 260, 10000, callback)

cv2.createTrackbar('Epsilon Percent', 'Settings', 7, 100, callback)
cv2.createTrackbar('Max Value', 'Settings', 255, 255, callback)
cv2.createTrackbar('Block Size', 'Settings', 6, 20, callback)
cv2.createTrackbar('C', 'Settings', 4, 255, callback)
cv2.createTrackbar('Contour R', 'Settings', 0, 255, callback)
cv2.createTrackbar('Contour G', 'Settings', 255, 255, callback)
cv2.createTrackbar('Contour B', 'Settings', 0, 255, callback)
cv2.createTrackbar('Exposure', 'Settings', 3, 12, callback)
cv2.createTrackbar('Focus', 'Settings', 26, 51, callback)
cv2.createTrackbar('Closing', 'Settings', 12, 50, callback)

cv2.namedWindow('Color Values', 0)
cv2.createTrackbar('Red Hue', 'Color Values', 0, 180, callback)
cv2.createTrackbar('Red Sat', 'Color Values', 255, 255, callback)
cv2.createTrackbar('Red Val', 'Color Values', 255, 255, callback)

cv2.createTrackbar('Blue Hue', 'Color Values', 115, 180, callback)
cv2.createTrackbar('Blue Sat', 'Color Values', 255, 255, callback)
cv2.createTrackbar('Blue Val', 'Color Values', 255, 255, callback)

cv2.createTrackbar('Yellow Hue', 'Color Values', 29, 180, callback)
cv2.createTrackbar('Yellow Sat', 'Color Values', 255, 255, callback)
cv2.createTrackbar('Yellow Val', 'Color Values', 255, 255, callback)

cv2.createTrackbar('Orange Hue', 'Color Values', 19, 180, callback)
cv2.createTrackbar('Orange Sat', 'Color Values', 255, 255, callback)
cv2.createTrackbar('Orange Val', 'Color Values', 255, 255, callback)

cv2.createTrackbar('Green Hue', 'Color Values', 44, 180, callback)
cv2.createTrackbar('Green Sat', 'Color Values', 255, 255, callback)
cv2.createTrackbar('Green Val', 'Color Values', 255, 255, callback)

cv2.createTrackbar('White Hue', 'Color Values', 0, 180, callback)
cv2.createTrackbar('White Sat', 'Color Values', 0, 255, callback)
cv2.createTrackbar('White Val', 'Color Values', 255, 255, callback)

# colorsHSV = {
#     "Red": ([0, 255, 255]),
#     "Orange": ([19, 255, 255]),
#     "Yellow": ([29, 255, 255]),
#     "Green": ([44, 255, 255]),
#     "Blue": ([115, 255, 255]),
#     "White": ([0, 0, 255])
# }

colorsRGB = {
    "Red": ([255, 0, 0]),
    "Orange": ([255, 162, 0]),
    "Yellow": ([255, 247, 0]),
    "Green": ([136, 255, 0]),
    "Blue": ([0, 42, 255]),
    "White": ([255, 255, 255])
}

def keepOdd(barName, windowName):
    num = cv2.getTrackbarPos(barName, windowName)
    if num == 0:
        num = 1;
    else:
        count = num % 2 
        if (count == 0):
            num += 1
    
    return num

def colourdistanceHSV(color1, color2):
    dh = min(abs(color2[0]-color1[0]), 360-abs(color2[0]-color1[0])) / 180.0
    ds = abs(color2[1]-color1[1])
    dv = abs(color2[2]-color1[2]) / 255.0
    return math.sqrt(dh*dh+ds*ds+dv*dv)

def computeContours(frame):
    colorsHSV = {
        "Red": ([cv2.getTrackbarPos('Red Hue', 'Color Values'), cv2.getTrackbarPos('Red Sat', 'Color Values'), cv2.getTrackbarPos('Red Val', 'Color Values')]),
        "Orange": ([cv2.getTrackbarPos('Orange Hue', 'Color Values'), cv2.getTrackbarPos('Orange Sat', 'Color Values'), cv2.getTrackbarPos('Orange Val', 'Color Values')]),
        "Yellow": ([cv2.getTrackbarPos('Yellow Hue', 'Color Values'), cv2.getTrackbarPos('Yellow Sat', 'Color Values'), cv2.getTrackbarPos('Yellow Val', 'Color Values')]),
        "Green": ([cv2.getTrackbarPos('Green Hue', 'Color Values'), cv2.getTrackbarPos('Green Sat', 'Color Values'), cv2.getTrackbarPos('Green Val', 'Color Values')]),
        "Blue": ([cv2.getTrackbarPos('Blue Hue', 'Color Values'), cv2.getTrackbarPos('Blue Sat', 'Color Values'), cv2.getTrackbarPos('Blue Val', 'Color Values')]),
        "White": ([cv2.getTrackbarPos('White Hue', 'Color Values'), cv2.getTrackbarPos('White Sat', 'Color Values'), cv2.getTrackbarPos('White Val', 'Color Values')])
    }

    frame2 = frame.copy()

    gausBlur = keepOdd('Blur kSize', 'Settings')
    
    gaus = cv2.getTrackbarPos('Block Size', 'Settings')
    if gaus < 3:
        gaus = 3;
    else:
        count = gaus % 2 
        if (count == 0):
            gaus += 1

    # blur = cv2.bilateralFilter(cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY), gausBlur, cv2.getTrackbarPos('Blur Sigma X', 'Settings'), cv2.getTrackbarPos('Blur Sigma X', 'Settings'))
    # blur = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    # blur = cv2.GaussianBlur(frame2, (gausBlur, gausBlur), cv2.getTrackbarPos('Blur Sigma X', 'Settings'))
    # blur = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

    frame2 = cv2.adaptiveThreshold(cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY),
        cv2.getTrackbarPos('Max Value', 'Settings'),
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        gaus,
        cv2.getTrackbarPos('C', 'Settings'))

    se1Size = keepOdd('Closing', 'Settings')
    se1 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (se1Size,se1Size))
    frame2 = cv2.morphologyEx(frame2, cv2.MORPH_CLOSE, se1)

    (contours, hierarchy) = cv2.findContours(frame2.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Index is used to remove nested squares.
    index = 0
    for cnt in contours:
        if (hierarchy[0,index,3] != -1):
            epsilon = (cv2.getTrackbarPos('Epsilon Percent', 'Settings')/100) * cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, epsilon, True)

            area = cv2.contourArea(approx, False)
            # arch = cv2.arcLength(approx, True)

            # squareness = 4 * math.pi * area / (arch * arch)

            if (len(approx) == 4 and area > cv2.getTrackbarPos('Blob Area', 'Settings')):
                # Square detected. Draw square on original image in green.
                M = cv2.moments(cnt)
                if (M["m00"] != 0):
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])
                    
                    cv2.drawContours(frame, [approx], 0, (cv2.getTrackbarPos('Contour B', 'Settings'), cv2.getTrackbarPos('Contour G', 'Settings'), cv2.getTrackbarPos('Contour R', 'Settings')), 3)

                    mask = np.zeros(frame2.shape, np.uint8)
                    cv2.drawContours(mask, [cnt], 0, 255, -1)
                    # pixelpoints = np.transpose(np.nonzero(mask))

                    hsvFrame = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
                    cv2.imshow("HSV Feed", hsvFrame)
                    meanVal = cv2.mean(hsvFrame, mask=mask)
                    color = np.array((int(meanVal[0]), 255, 255), np.uint8)
                    
                    resultColor = {}
                    for k,v in colorsHSV.items():
                        resultColor[k]=colourdistanceHSV(v, color)
                    
                    #THIS WILL WORK FOR EVEN GREY
                    # print(resultColor)
                    finalColor = min(resultColor, key=resultColor.get)
                    print(finalColor)

                    # print(color)
                    
                    cv2.circle(frame, (cX, cY), 7, (0, 0, 0), -1)
                    cv2.circle(frame, (cX, cY), 5, (colorsRGB[finalColor][2], colorsRGB[finalColor][1], colorsRGB[finalColor][0]), -1)
            else:
                # Square NOT detected. Draw square on original image in red.
                cv2.drawContours(frame, [approx], 0, (255, 0, 0), 3)

        index += 1

    return frame2;

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        mousePositions.append([x, y])

cv2.namedWindow("Webcam Capture")
cv2.setMouseCallback('Webcam Capture', draw_circle)
mousePositions = []

while (capture.isOpened()):
    ret, frame = capture.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if ret:
        capture.set(cv2.CAP_PROP_EXPOSURE, (cv2.getTrackbarPos('Exposure', 'Settings')+1)*-1)
        capture.set(cv2.CAP_PROP_FOCUS, cv2.getTrackbarPos('Focus', 'Settings')*5)
        newFrame = computeContours(frame);

        for pos in mousePositions:
            cv2.circle(frame,(pos[0], pos[1]), 5, (255,0,0), -1)
            cv2.putText(frame, (str(pos[0]) + "," + str(pos[1])), (pos[0], pos[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 1, cv2.LINE_AA)

        cv2.imshow("Webcam Capture", frame);
        cv2.imshow("Adaptive Mean Threshold", newFrame);
    else:
        break

capture.release()
cv2.destroyAllWindows()
