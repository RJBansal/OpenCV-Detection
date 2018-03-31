import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1, 0, ksize = 5)
    sobely = cv2.Sobel(frame,cv2.CV_64F, 0, 1, ksize = 5)
    sobel = cv2.Sobel(frame,cv2.CV_64F, 1, 1, ksize = 5)

    edges = cv2.Canny(frame, 100, 200) #min and max values for threshold 
    

    cv2.imshow("frame", frame)
    cv2.imshow("laplacian", laplacian)
    cv2.imshow("edge", edges)
    #cv2.imshow("edges2", edges2)
    #cv2.imshow("sobel", sobel)
    
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
