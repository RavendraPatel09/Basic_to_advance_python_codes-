import cv2
import cv2.data
import os
model_name = 'haarcascade_frontalcatface.xml' 
data_path = cv2.data.haarcascades + model_name
model = cv2.CascadeClassifier(data_path)
img = cv2.imread("/Users/ravendrapatel/Cat image .jpeg")
if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = model.detectMultiScale(gray, 1.1, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Cat Face Detection', img)
