import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
img = cv2.imread('android.png')
codec = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', codec, 20.0, (640,480))



while True:
    ret,frame = cap.read()
    grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.line(grayscale, (50,50), (150,150), (0,0,0), 15)
    cv2.rectangle(grayscale, (50,50), (200,200),(0,0,0), 10)
    cv2.circle(grayscale, (100,50),55,(0,0,0), -1)
    cv2.putText(grayscale, 'rajat', (400,400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 5)

  

    rows, cols, channels = img.shape
    roi = frame[0:rows, 0:cols]

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img_gray, 220, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    frame_bg = cv2.bitwise_and(roi, roi, mask= mask)
    img_fg = cv2.bitwise_and(img, img, mask = mask_inv)

    add = frame_bg + img_fg
    frame[0:rows, 0:cols] = add
    
    out.write(frame)
    cv2.imshow('webcam',frame)
    cv2.imshow('grayscale', grayscale)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows() 



 
    
