from PIL import Image, ImageFilter, ImageEnhance
image = Image.open("tree.jpg")
image.show()
width, height= image.size
a=0
green=0
for x in range(width):
    for y in range(height):
        r,g,b=image.getpixel((x,y))
        if(r<g and b<g):
            green=green+1
            image.putpixel((x,y),(255,255,255))
        else:
            image.putpixel((x, y), (0,0,0))
        a=a+1
image.show()
image.save("mask.jpg")
print("Total Pixel %d"%a)
print("Total Green Pixel  %d"%green)
print(width)
print(height)

img= Image.open("mask.jpg")
img.filter(ImageFilter.FIND_EDGES).save("edge.jpg")

im = Image.open("edge.jpg")
im.show()

# im = im.filter(ImageFilter.MedianFilter())
# enhancer = ImageEnhance.Contrast(im)
# im = enhancer.enhance(2)
# im = im.convert('1')
# im.show()
# im.save('image_clear.jpg')

