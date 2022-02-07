#import cv2
#![](C:/Users/Qualitas/Desktop/1.jpg)
#image = cv2.imread('C:/Users/Qualitas/Desktop/3.jpg')

#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#cv2.imshow('Original image', image)
#cv2.imshow('Gray image', gray)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

import cv2
import numpy as np

image = cv2.imread("C:/Users/Qualitas/Desktop/6.jpg")
# Convert BGR to HSV
#hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
small = cv2.resize(image, (800, 800))
rgb = cv2.cvtColor(small , cv2.COLOR_BGR2RGB)

# define blue color range
light_blue = np.array([50, 45, 50])
dark_blue = np.array([190, 180, 130])

# Threshold the HSV image to get only blue colors
#mask = cv2.inRange(hsv, light_blue, dark_blue)
mask = cv2.inRange(rgb, light_blue, dark_blue)
# Bitwise-AND mask and original image
output = cv2.bitwise_and(small, small, mask=mask)

cv2.imshow("Color Detected", np.hstack((small, output)))
#cv2.imwrite(C:/Users/Qualitas/Desktop ,output)
cv2.waitKey(0)
cv2.destroyAllWindows()