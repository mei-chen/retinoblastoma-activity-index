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

os.remove('./OS.csv')
#os.remove('./OD.csv')

for filename in os.listdir('/Users/mlchen/Code/RAI/ZB/'):
    tumour = 0
    if filename.endswith('.png'):
        color_list = []
        # print(os.path.join('/Users/mlchen/Code/RAI/ZB/', filename))
        img_obj = Image.open(os.path.join('/Users/mlchen/Code/RAI/OS/', filename))
        for pixel in img_obj.getdata():
            if pixel != background and pixel != pink and pixel != pink2 and pixel != white and pixel != black: 
                # color_list.append(pixel)
                tumour += 1

        tumour = ((tumour - 19060)/609961)
        with open('OS.csv', 'at') as f:
            # for row in color_list:
            f.write(filename + ' ' + str(tumour) + '\n')

        #od_cropped_image = img_obj.crop((0,0,781,781))
        # os_cropped_image = img_obj.crop((960,0,1741,781))
        #os_cropped_image = img_obj.crop((0,0,1741,781))
        # od_cropped_image.save(filename + "right")
        # os_cropped_image.save(filename + "left")
        # os_cropped_image.save(filename)
        # number += 1
        