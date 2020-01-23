import os
from PIL import Image, ImageOps, ImageDraw
#open up image
image = Image.open("background.png")

#draw centre circle
draw = ImageDraw.Draw(image)
draw_bg = ImageDraw.Draw(image)
x = 391
y = 391
r = 321
leftUpPoint = (x-r, y-r)
rightDownPoint = (x+r, y+r)
twoPointList = [leftUpPoint, rightDownPoint]
draw.ellipse(twoPointList, fill='black')
#draw.rectangle(twoPointList, fill = 'white')
image.show()


back = Image.new('RGBA', image.size)
back.paste(image, mask = 200 )

#make inverse mask by first filling in entire image black 
draw_bg.rectangle()
