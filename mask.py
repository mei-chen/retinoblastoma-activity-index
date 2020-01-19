from PIL import Image, ImageOps, ImageDraw

image = Image.open("background.png")
draw = ImageDraw.Draw(image)
x = 391
y = 391
r = 321
leftUpPoint = (x-r, y-r)
rightDownPoint = (x+r, y+r)
twoPointList = [leftUpPoint, rightDownPoint]
draw.ellipse(twoPointList, fill='black')
image.show()

back = Image.new('RGBA', image.size)
back.paste(image, mask = 200 )
back.show()