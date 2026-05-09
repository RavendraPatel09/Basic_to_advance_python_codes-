import cv2
import cv2.data
import os
print(os.listdir(cv2.data.haarcascades))
model_name = 'haarcascade_frontalface_default.xml'
data_path = cv2.data.haarcascades + model_name
modal = cv2.CascadeClassifier(data_path)
img = cv2.imread("/Users/ravendrapatel/group photo.jpeg")
faces = modal.detectMultiScale(img, 1.1, 4)
print(faces)
for face in faces:
    x1=face[0]
    y1=face[1]
    x2=x1+face[2]
    y2=y1+face[3]
    cv2.rectangle(img,(x1,y1),(x2,y2),[255,0,0],2)
cv2.imshow('image',img)
cv2.waitKey(0)