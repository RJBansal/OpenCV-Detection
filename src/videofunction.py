import cv2
import numpy as np

cap = cv2.VideoCapture(0)
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

while True:
    ret, frame = cap.read()

    face = frame[150:350, 300:450]
    frame[0:200, 0:150] = face

    #op = img1 + img2
    #op = cv2.add(img1, img2)
    #op = cv2.addWeighted(img1, .6, img2, .4, 0) #last number is gamma value 

    #cv2.imshow("operations", op)
    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows() 
