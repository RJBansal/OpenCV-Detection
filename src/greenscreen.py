import cv2
import numpy as np

cap = cv2.VideoCapture(0)


#Specific Color range removal and noise reduction 
while True:

    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_color = np.array([50,50,50]) #change values to better show particular object
    upper_color = np.array([255,255,255])

    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(frame, frame, mask = mask)

    #kernel = np.ones((15,15), np.float32)/225
    #smooth = cv2.filter2D(result,5 -1, kernel)

    #Gaussian Blur
    #blur = cv2.GaussianBlur(result, (15,15), 0)

    #median Blur
    #median_blur = cv2.medianBlur(result, 15)

    #bilateral Blur
    #bilateral_blue = cv2. bilateralFilter(result,15, 75, 75)

    #morphological transformation -> set of operations that process images based on shapes
    kernel_m = np.ones((5,5), np.uint8)
    errosion = cv2.erode(mask, kernel_m, iterations = 1)
    dialation = cv2.dilate(mask, kernel_m, iterations = 1)

    #opening to remove false postivies ->noises in background
    #opening to remove false negative -> noises in main view

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel_m)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_m)

    cv2.imshow('frame', frame)
    cv2.imshow('smooth', mask)
    cv2.imshow('result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

