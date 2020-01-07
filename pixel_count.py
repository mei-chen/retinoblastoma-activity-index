import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt 
#%matplotlib inline
from PIL import Image
import os

##yellow pixel output
# img = plt.imread('1-ZB-Oct-18-2017.png')


image_obj = Image.open('/Users/mlchen/Code/RAI/ZB/1-ZB-Oct-18-2017.png')

od_cropped_image = image_obj.crop((0,0,781,781))
os_cropped_image = image_obj.crop((960,0,1741,781))

od_cropped_image.save('/Users/mlchen/Code/RAI/cropped_ZB/right.png')

od_cropped_image.show() 
os_cropped_image.show()

# print(img.shape)
# yellowPixels = img(:,:,1) == 251 & img(:,:,2) == 237 & img(:,:,3) == 126
# numYellowPixels = sum(yellowPixels(:))

plt.imshow(img)
plt.show()

# dim = img.shape
# print(dim)
# rows,cols,chan= img.shape

# for i in range(rows):
#   for j in range(cols):
#      k = img[i,j]
#      print(k)

# yellow_light = img[255,253,0]
# light_yellow = img.item(255,255,1)

# print("yellow", yellow)
# print(light_yellow)
# print(img.size)
# print(img.dtype)



# im = Image.open('test.png')

# i = 0
# yellow = 0
# for pixel in im.getdata():
#     print(pixel)
#     while i<255 :
#         if pixel is (255, i, 0):
#              yellow += 1
#         i+=1

#img = plt.imread('test.png')
# img = cv2.imread('test.png')
# retval, threshold = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
# cv2.imshow('threshold', threshold)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img)
# plt.show()

# #from skimage import data,filters
# image = 'test.png'
# image = cv2.imread(image, 1)
# type(image)
# # numpy.ndarray #Image is a NumPy array: 

# # mask = image < 87  
# # image[mask]=255  
# plt.imshow(image, cmap='gray')
