# from os import environ
# # if environ['USER'] == 'pydev':
#     from urllib.request import urlopen #for localhost
# else:
#     from urllib import urlopen  # on c9.io for python 2
from urllib.request import urlopen #works for python3

def img_exists(img='http://ya.ru/somewwwwwwwwwwww.jpg'):
    try:
        f = urlopen(img)
        return True
    except:
        return False


if __name__ == '__main__':
    print(img_exists('http://ya.ru'))
    print(img_exists('http://pn.lmcdn.ru/product/M/I/MI052EWISL34_1_v2.jpg'))
    print(img_exists())
