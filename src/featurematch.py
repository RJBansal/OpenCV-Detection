import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("scene.jpg")
img2 = cv2.imread("case.jpg")

orb = cv2.ORB_create()
keypoints, des = orb.detectAndCompute(img, None)
keypoints2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

match = bf.match(des, des2)
match = sorted(match, key = lambda x:x.distance)

img3 = cv2.drawMatches(img, keypoints, img2, keypoints2, match[:100], None, flags = 2)
plt.imshow(img3)
plt.show()
