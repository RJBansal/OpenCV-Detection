import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('android.png')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2_gray, 220, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)


img1_bg = cv2.bitwise_and(roi, roi, mask = mask)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask_inv)

#add = cv2.add(img1_bg, img2_fg)
add = img1_bg+img2_fg
img1[0:rows, 0:cols] = add


cv2.imshow('original', img2)
cv2.imshow('mask', mask)
cv2.imshow('mask_inverse', mask_inv)
cv2.imshow('bg', img1_bg)
cv2.imshow('fg', img2_fg)
cv2.imshow('final', img1)


cv2.waitKey(0)
cv2.destroyAllWindows()
