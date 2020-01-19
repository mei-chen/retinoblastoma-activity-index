from PIL import ImageOps, Image, ImageDraw

img = Image.open("background.png")
back = Image.new('RGBA', img.size)
back.paste(img)
poly = Image.new('RGBA', (512,512))
pdraw = ImageDraw.Draw(poly)
pdraw.rectangle([(10,10),(100,100)],
          fill=(255,255,255,200))
inverted_poly = ImageOps.invert(poly)
back.paste(poly, (0,0), mask=inverted_poly)
back.show()