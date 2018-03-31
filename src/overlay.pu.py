import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('android.png')

row, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


cv2.imshow('image', img2gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
