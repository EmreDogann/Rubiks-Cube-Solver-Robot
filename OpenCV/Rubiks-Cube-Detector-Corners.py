import cv2
import numpy as np

capture = cv2.VideoCapture(0)
capture.set(3, 1280)
capture.set(4, 720)

def callback(num):
    return

cv2.namedWindow('Settings', 0)
cv2.createTrackbar('Block Size', 'Settings', 2, 20, callback)
cv2.createTrackbar('Quality Level', 'Settings', 1, 100, callback)
cv2.createTrackbar('Minimum Distance', 'Settings', 10, 300, callback)
cv2.createTrackbar('Gradient Size', 'Settings', 3, 31, callback)
cv2.createTrackbar('Maximum Corners', 'Settings', 4, 50, callback)
cv2.createTrackbar('k', 'Settings', 4, 100, callback)
cv2.createTrackbar('Blur kSize', 'Settings', 9, 100, callback)
cv2.createTrackbar('Blur Sigma X', 'Settings', 75, 100, callback)
cv2.createTrackbar('Canny Thres 1', 'Settings', 87, 500, callback)
cv2.createTrackbar('Canny Thres 2', 'Settings', 325, 500, callback)

cv2.createTrackbar('Exposure', 'Settings', 5, 10, callback)
cv2.createTrackbar('Focus', 'Settings', 22, 51, callback)

def computeCorners(frame):
    gaus = cv2.getTrackbarPos('Blur kSize', 'Settings')

    if gaus == 0:
        gaus = 1;
    else:
        count = gaus % 2 
        if (count == 0):
            gaus += 1
            
    canny = cv2.Canny(cv2.bilateralFilter(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY), gaus, cv2.getTrackbarPos('Blur Sigma X', 'Settings'), cv2.getTrackbarPos('Blur Sigma X', 'Settings')), cv2.getTrackbarPos('Canny Thres 1', 'Settings'), cv2.getTrackbarPos('Canny Thres 2', 'Settings'))
    cv2.imshow("Canny", canny)

    gauSize = cv2.getTrackbarPos('Gradient Size', 'Settings')

    if gauSize == 0:
        gauSize = 1
    else:
        count = gauSize % 2 
        if (count == 0):
            gauSize += 1

    corners = cv2.goodFeaturesToTrack(canny,
        cv2.getTrackbarPos('Maximum Corners', 'Settings'),
        cv2.getTrackbarPos('Quality Level', 'Settings')/100,
        cv2.getTrackbarPos('Minimum Distance', 'Settings'),
        mask=None,
        blockSize=cv2.getTrackbarPos('Block Size', 'Settings'),
        gradientSize=gauSize, 
        useHarrisDetector=False,
        k=cv2.getTrackbarPos('k', 'Settings')/100)

    radius = 5
    for i in range(corners.shape[0]):
        cv2.circle(frame, (corners[i,0,0], corners[i,0,1]), radius, (0, 0, 255), cv2.FILLED)

    # return dst_norm_scaled;

while (capture.isOpened()):
    ret, frame = capture.read()

    #If frame is available
    if ret:
        capture.set(cv2.CAP_PROP_EXPOSURE, (cv2.getTrackbarPos('Exposure', 'Settings')+1)*-1)
        capture.set(cv2.CAP_PROP_FOCUS, cv2.getTrackbarPos('Focus', 'Settings')*5)

        # newFrame = computeCorners(frame);
        computeCorners(frame)

        cv2.imshow("Webcam Capture", frame);
        # cv2.imshow("Corners", newFrame);

        #Wait 1 millisecond each iteration, if user pressed 'q', exit loop.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
cv2.destroyAllWindows()
