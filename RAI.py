import matplotlib.pyplot as plt 
from PIL import Image, ImageOps, ImageDraw

#read image 
im = Image.open('background.png')
width, height = im.size #get dimensions  #781, 781

#create mask
# mask = Image.open('background.png').convert('L')
# output = ImageOps.fit(im, mask.size, bleed = 0.0, centering=(0.5,0.5))
# output.putalpha(mask)
# output.save('output.png')

#draws an elipse 
# draw = ImageDraw.Draw(im)
# draw.ImageDraw.ellipse([100, 100, 600, 600], fill=None, outline=None, width=0)

#crop image
# left = width / 11
# top = height / 11
# right = 10 * left 
# bottom = 10 * top
# im_crop = im.crop((left, top, right, bottom))

# crop_Width, crop_Height = im_crop.size
# crop_Size = crop_Width * crop_Height 
# print(crop_Size)
# #display image
# im_crop.show()

background = (234, 234, 234, 255)
pink = (244, 212, 187, 255)
pink2 = (244,213,188, 255)
white = (255,255,255,255)
black = (0, 0, 0, 255)

# print(im_crop.format, im_crop.size, im_crop.mode)  

#count yellow area 
tumour = 0 
img_obj = Image.open('./OS/1-ZB-Oct-18-2017.png')
for pixel in img_obj.getdata():
    if pixel != background and pixel != pink and pixel!= pink2 and pixel != white and pixel !=black: 
        tumour += 1 
print(tumour)
RAI = tumour / crop_Size
print("Percentage of tumour is %", RAI )


