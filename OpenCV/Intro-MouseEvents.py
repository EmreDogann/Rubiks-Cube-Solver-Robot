import numpy as np
import cv2

#Get a list of all the events in the cv2 directory.
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print (events)

#Mouse Event callback function.
#Whenever a mouse event a triggered, this callback function will be called.
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #Display mouse coordinates.
        font = cv2.FONT_HERSHEY_COMPLEX
        text = str(x) + ', ' + str(y)
        cv2.putText(img, text, (x, y), font, 1, (255, 0, 0), 1)

        #Create new window with color of pixel at mouse coordinates.
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        myColorImage = np.zeros((512, 512, 3), np.uint8)
        #Set all pixels in image to color of the pixel at the mouse coordinates.
        myColorImage[:] = [blue, green, red]

        #Draw circle at mouse coordinates.
        cv2.circle(img, (x, y), 9, (0, 0, 255), -1)

        #Add coordinates to points array.
        points.append((x, y))
        #Connect the last two most recent points in the array with a line.
        if len(points) >= 2:
            cv2.line(img, points[-1], points[-2], (0, 0, 0), 5)

        cv2.imshow('Alaska', img)
        cv2.imshow('Color', myColorImage)

    #If right click, display color values.
    elif event == cv2.EVENT_RBUTTONDOWN:
        #RBG Channels are reversed in OpenCV. So, RGB would be BGR.
        #0 - Blue, 1 - Green, 2 - Red
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        font = cv2.FONT_HERSHEY_COMPLEX
        text = str(blue) + ', ' + str(green) +  ', ' + str(red)
        cv2.putText(img, text, (x, y), font, 1, (255, 0, 128), 1)
        cv2.imshow('Alaska', img)

img = cv2.imread("Alaska.jpg", -1)
#Create black image using Numpy
#img = np.zeros((512, 512, 3), np.uint8)

cv2.imshow("Alaska", img)
points = []

#Set the callback function
cv2.setMouseCallback("Alaska", click_event)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()