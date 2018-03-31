import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpeg',1)

cv2.line(img, (50,50), (150,150), (0,0,0), 15)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

##plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
##plt.plot([0,700],[700,700], 'c', linewidth = 5)
##plt.show()

cv2.imwrite('graywatch.jpeg', img)
