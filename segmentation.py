from PIL import Image
image = Image.open("greenspot.jpg")
width, height= image.size;
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
            image.putpixel((x, y), (0,0,0));
        a=a+1

image.show()
print("Total Pixel %d"%a)
print("Total Green Pixel  %d"%green)
print(width)
print(height)

