from PIL import Image
from shoes import imgs
from urllib.request import urlopen

print(imgs)
def url_by_filename(filename):
    url = 'http://pn.lmcdn.ru/product/' + filename[0] + '/' + filename[1] + "/" + filename
    return url

def generate_thumb(filename):
    tmp = open('tmp.jpg', 'wb')
    tmp.write(urlopen(url_by_filename(filename)).read())
    tmp.close()
    img =Image.open('tmp.jpg')
    img.thumbnail((140,200), Image.ANTIALIAS)
    img.save('static/thumbnails/'+filename, "JPEG")

print(url_by_filename(imgs[0]))
for img in imgs:
    generate_thumb(img)