from PIL import Image
image = Image.open("gspot.jpg")
width, height= image.size
a=0
green=0
for x in range(width):
    for y in range(height):
        r,g,b=image.getpixel((x,y))
        # print(r,g,b)
        if(r<g and b<g):
            green=green+1
            image.putpixel((x,y),(255,255,255))
        else:
            image.putpixel((x, y), (0,0,0))
        a=a+1

#image.show()
image.save("mask.jpg")
print("Total Pixel %d"%a)
print("Total Green Pixel  %d"%green)
print(width)
print(height)

img= Image.open("mask.jpg")
w, h= img.size
g=0
for a in range(w):
    for b in range(h):
        r,g,b=img.getpixel((a,b))
        if(r==255 and g==255 and b==255):

            i,o, p = img.getpixel((a-1, b-1))
            if(i==0 and o==0 and p==0):
                img.putpixel((a-1, b-1), (255, 0, 0))

            i, o, p = img.getpixel((a, b - 1))
            if (i == 0 and o == 0 and p == 0):
                img.putpixel((a, b - 1), (255, 0, 0))

            i, o, p = img.getpixel((a + 1, b - 1))
            if (i == 0 and o == 0 and p == 0):
                img.putpixel((a + 1, b - 1), (255, 0, 0))

            i, o, p = img.getpixel((a - 1, b ))
            if (i == 0 and o == 0 and p == 0):
                img.putpixel((a - 1, b ), (255, 0, 0))

            i, o, p = img.getpixel((a + 1, b ))
            if (i == 0 and o == 0 and p == 0):
                img.putpixel((a + 1, b), (255, 0, 0))

            i, o, p = img.getpixel((a - 1, b + 1))
            if (i == 0 and o == 0 and p == 0):
                img.putpixel((a - 1, b + 1), (255, 0, 0))

            i, o, p = img.getpixel((a, b+1))
            if (i == 0 and o == 0 and p == 0):
                img.putpixel((a, b+1), (255, 0, 0))

            i, o, p = img.getpixel((a + 1, b + 1))
            if (i == 0 and o == 0 and p == 0):
                img.putpixel((a + 1, b + 1), (255, 0, 0))

img.show()

