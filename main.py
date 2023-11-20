## print("Hello World")
import cv2
 
capture = cv2.VideoCapture('./mp4/drone-tracking-1.mp4')
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'./detections/frames/frame_{frameNr}.jpg', frame)
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()
