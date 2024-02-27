import numpy as np
import cv2

cap = cv2.VideoCapture(0)

    # Change the Resolution of Video /start/
def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def make_720p():
    cap.set(3, 1280)
    cap.set(4, 720)                                                 # All of this functions are for changing the resolution

def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(width, height):                                      # This is for those who want more or less resolution
    cap.set(3, width)
    cap.set(4, height)    
    # Change the Resolution of Video /end/

    # Rescale the Frame not the Video /start/
def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
    # Rescale the Frame not the Video /end/

while(True):
    ret, frame = cap.read()                             # Capture frame-by-frame

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)      # Our operations on the frame come here
    #frame = rescale_frame(frame, percent=200)            # Rescale the frame, This doesn't affect the resolution of the video

    cv2.imshow('frame',frame)                           # Display the resulting frame
    #cv2.imshow('gray',gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()                                           # When everything done, release the capture
cv2.destroyAllWindows()