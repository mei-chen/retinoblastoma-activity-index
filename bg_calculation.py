import pandas as pd
import numpy as np
import cv2
import matplotlib.pyplot as plt 
#%matplotlib inline
from PIL import Image
import os
import csv

background = (234, 234, 234, 255)
pink = (244, 212, 187, 255)
pink2 = (244,213,188, 255)
white = (255,255,255,255)
black = (0, 0, 0, 255)

tumour = 0
img_obj = Image.open('background.png')
for pixel in img_obj.getdata():
    if pixel != background and pixel != pink and pixel != pink2 and pixel != white and pixel != black: 
    # color_list.append(pixel)
        tumour += 1
print(tumour)
# with open('bg.csv', 'at') as f:
# # for row in color_list:
#     f.write(filename + ' ' + str(tumour) + '\n')