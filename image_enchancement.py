import cv2
import numpy as np

img = cv2.imread("bookpage.jpg")

ret, mask = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret,gray_threshold = cv2.threshold(img_gray, 12, 255, cv2.THRESH_BINARY)
gauss_gray = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

cv2.imshow("original", img)
cv2.imshow("image-gray", img_gray)
cv2.imshow("threshold", gray_threshold)
cv2.imshow("gauss-gray", gauss_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
