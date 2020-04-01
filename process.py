from PIL import Image, ImageFilter, ImageEnhance
import cv2
import numpy as np

image = Image.open('london_ground.jpg')
width, height = image.size
if (width == 1280 and height == 720):
    # Mask Image
    for x in range(width):
        for y in range(height):
            red, green, blue = image.getpixel((x, y))
            # RED AND BLUE SHOULD BE NON ZERO
            if (red >= 0 and blue >= 0):
                # GREEN MUST BE GREATER THAN RED AND BLUE
                if (red < green and blue < green):
                    # CALCULATE DIFFERENCE
                    zz = green - red
                    xx = green - blue
                    # IF RED AND BLUE IS LESS THAN 20 THAN DIFFERENCE CAN BE 1 OR MORE
                    if (red <= 20 and blue <= 20 and green <= 20):
                        image.putpixel((x, y), (255, 255, 255))
                    # IF RED AND BLUE IS GREATER THAN 200 DO'NT CONSIDER THAT PIXEL
                    elif (red > 100 and blue > 100 and green > 100):
                        image.putpixel((x, y), (0, 0, 0))
                    # DIFFERENCE MUST BE OF 10
                    elif (zz > 10 and xx > 10):
                        image.putpixel((x, y), (255, 255, 255))
                    # FILL BLACK COLOR
                    else:
                        image.putpixel((x, y), (0, 0, 0))
                # GREEN IS NOT LARGER FILL BLACK COLOR
                else:
                    image.putpixel((x, y), (0, 0, 0))
            # INVALID
            else:
                image.putpixel((x, y), (0, 0, 0))
    # SAVE MASK IMAGE
    image.save("mask.jpg")
    # DRAW RECTANGLE
    img = cv2.pyrDown(cv2.imread("mask.jpg", cv2.IMREAD_UNCHANGED))
    ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 127, 255, cv2.THRESH_BINARY)
    contours, hier = cv2.findContours(threshed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    coo = 0
    for c in contours:
        x, y, w, h = cv2.boundingRect(c)
        aa = (w) * (h)
        if aa > 2:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            coo = coo + 1
        else:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)
    # NO OF TREE
    print("NO OF TREE")
    print(coo)
    # SAVE COUNTER IMAGE
    cv2.imwrite("counter.jpg", img)
else:
    print("Insert Proper image")
