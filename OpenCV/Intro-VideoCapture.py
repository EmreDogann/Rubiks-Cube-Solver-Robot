import cv2
import datetime

capture = cv2.VideoCapture(0)
#Get and print frame width and height
print(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)) #Can be substituted with 4.
print(capture.get(cv2.CAP_PROP_FRAME_WIDTH)) #Can be substituted with 3.
#Set width of video.
# capture.set(3, 1980)
#Set height of video.
# capture.set(4, 1080)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter("output.avi", fourcc, 30, (640,480))

while (capture.isOpened()):
    ret, frame = capture.read()

    #If frame is available
    if ret:
        #Write to file
        output.write(frame)

        #Add text and date to video capture
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "Width: " + str(capture.get(3)) + " Height: " + str(capture.get(4))
        date = "Date: " + str(datetime.datetime.now());
        frame = cv2.putText(frame, text, (10, 50), font, 1, 
                            (0, 255, 128), 2, cv2.LINE_AA)

        frame = cv2.putText(frame, date, (10, 100), font, 1, 
                            (0, 255, 128), 2, cv2.LINE_AA)

        #Convert frame to grayscale
        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("WebcamCapture", frame)

        #Wait 1 millisecond each itertion, if user pressed 'q', exit loop.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
output.release()
cv2.destroyAllWindows()
