import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("waldo.jpg")
img2 = cv2.imread("dino.jpg") #change image 

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width, channels = img2.shape #way to get width and height via shape

result = cv2.matchTemplate(img, img2, cv2.TM_CCOEFF_NORMED)
threshold = 0.4

location = np.where(result >= threshold)

for pt in zip(*location[::-1]):
    cv2.rectangle(img, pt, (pt[0]+width, pt[1]+height), (255,255,255), 2)

cv2.imshow('frame', img)
#plt.imshow(img)
#plt.show()
if cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
