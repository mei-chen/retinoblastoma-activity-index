import cv2
import numpy as np 
from skimage.io import imread
import matplotlib.colors as mcolors

# img = cv2.imread('test.png')

img = imread( 'test.png' )
img_hsv = mcolors.rgb_to_hsv( img )
# img_hsv = img_hsv / (1.0, 1.0, 255.0)
imshow(img_hsv)
# print(img_hsv.format(arr.shape))

x = 0
y = 0
#chage RBG to HSV 
px_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# print(px_hsv.shape())

# print(hsv.shape)
# for i in (hsv.shape[0]):
#     print(i)

# #define range of yellow colour
# lower_yellow = np.array([255,255,0])
# upper_yellow = np.array([255,255,180])

#threshold the RBG to get only yellow 
# mask = cv2.inRange(img, lower_yellow, upper_yellow)

# mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

# cv2.imshow('mask', mask)

cv2.imshow('image', img)
cv2.waitKey(0)
# cv2.destroyAllWindows()