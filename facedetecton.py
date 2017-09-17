import cv2
import numpy as np

face = cv2.CascadeClassifier('face.xml')
eye = cv2.CascadeClassifier('eye.xml')

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #gauss_gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    face_detect = face.detectMultiScale(gray, 1.3, 5)
    for(x,y,w,h) in face_detect:
        cv2.rectangle(frame, (x,y), ((x+w), (y+h)), (255, 255, 255), 2)
        roi = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eye_detect = eye.detectMultiScale(roi, 1.3, 5)
        for (ex, ey, ew, eh) in eye_detect:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (255, 255, 255), 2)
        frame[0:h, 0:w] = roi_color
        
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
