from PIL import Image, ImageDraw

im = Image.open("danilova.jpg")
im2 = im.copy()
# Creating a Draw object
draw = ImageDraw.Draw(im)
draw2 = ImageDraw.Draw(im2)

draw.rectangle(xy = (300, 180, 560, 440),
               outline = (0, 0, 255),
               width = 5)

draw2.rectangle(xy = (300, 180, 560, 440),
               outline = (0, 255, 0),
               width = 5) 


im_cropped = im.crop((300, 180, 560, 440)).rotate(90)
im.paste(im_cropped, (300, 180))
im.show()
im.save("danilova_rotate90.jpg", "JPEG")

im_cropped2 = im2.crop((300, 180, 560, 440)).rotate(-120)
im2.paste(im_cropped2, (300, 180))
im2.show()
im2.save("danilova_rotate120.jpg", "JPEG")

