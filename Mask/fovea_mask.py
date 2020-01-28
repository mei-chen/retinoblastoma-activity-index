from PIL import Image, ImageOps, ImageDraw

#crop out the edge around the circle --> mask 
size = (781, 781)
mask = Image.new('L', size, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + size, fill=255)

#draw the centre of the circle at where the fovea is (centre of the middle X) to indicate the points that we would pass 
x, y, r = 390, 392, 2
leftUpPoint = (x-r, y-r)
rightDownPoint = (x+r, y+r)
twoPointList = [leftUpPoint, rightDownPoint]
draw.ellipse(twoPointList, fill='blue')

#Isolate the pixels above and check if they are yellow


#crop
bg_image = Image.open("../background.png")
bg_image.putalpha(mask)
bg_image_crop = bg_image.crop((0, 0, 781, 781))
bg_image_crop.show()
