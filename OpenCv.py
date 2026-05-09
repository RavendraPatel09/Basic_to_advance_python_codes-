import cv2
import cv2.data
import os

from numpy import eye
classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while True:
    status,frame = cap.read()
    if not status:
        print("Could not read frame")
        break
    faces = classifier.detectMultiScale(frame,1.1,4)
    for face in faces:
        x1=face[0]
        y1=face[1]
        x2=x1+face[2]
        y2=y1+face[3]
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        blink_frame = frame[y1:y2, x1:x2]
        gray = cv2.cvtColor(blink_frame, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(blink_frame, (ex, ey), (ex + ew, ey + eh), (255, 0, 0), 2)
    cv2.imshow('Webcam Face Detection',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()