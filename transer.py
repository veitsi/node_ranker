from PIL import Image
import os
from urllib.request import urlopen

max_color = 250


def save_transp(jpgfile, pngfile):
    jpgfile = 'http://pn.lmcdn.ru/product/' + jpgfile[0] + '/' + jpgfile[1] + "/" + jpgfile
    print('is there? ' + jpgfile)

    def is_white():
        if pixdata[x, y][0] > max_color and pixdata[x, y][1] > max_color and pixdata[x, y][2] > max_color:
            return True

    def is_trans():
        if pixdata[x, y][0] == 0 and pixdata[x, y][1] == 0 and pixdata[x, y][2] == 0 and pixdata[x, y][3] == 0:
            return True

    tmp = open('tmp.jpg', 'wb')
    tmp.write(urlopen(jpgfile).read())
    tmp.close()
    img = Image.open('tmp.jpg')
    img = img.convert("RGBA")
    pixdata = img.load()

    # print(pixdata[100,0])
    for y in range(img.size[1]):
        for x in range(img.size[0]):
            # print (y,x, pixdata[x, y][0], pixdata[x, y][1], pixdata[x, y][2]   )
            if is_white():
                pixdata[x, y] = (0, 0, 0, 0)


    x1 = 0
    x2 = img.size[0]
    y1 = 0
    y2 = img.size[1]

    x = 0
    flag = True
    while x < img.size[0] and flag:
        y = 0
        while y < img.size[1] and flag:
            if pixdata[x, y] != (0, 0, 0, 0):
                flag = False
                x1 = x
            y += 1
        x += 1

    y = 0
    flag = True
    while y < img.size[1] and flag:
        x = 0
        while x < img.size[0] and flag:
            if pixdata[x, y] != (0, 0, 0, 0):
                flag = False
                y1 = y
            x += 1
        y += 1

    x = img.size[0] - 1
    flag = True
    while x > -1 and flag:
        y = 0
        while y < img.size[1] and flag:
            if pixdata[x, y] != (0, 0, 0, 0):
                flag = False
                x2 = x
            y += 1
        x -= 1

    y = img.size[1] - 1
    flag = True
    while y > -1 and flag:
        x = 0
        while x < img.size[0] and flag:
            if pixdata[x, y] != (0, 0, 0, 0):
                flag = False
                y2 = y
            x += 1
        y -= 1
    print('calculated  ', x1, y1, x2, y2)

    img.crop((x1, y1, x2, y2)).save(pngfile, "PNG")
    # img.thumbnail((120,120))
    # img.save('out.thumbnail.png',"PNG")