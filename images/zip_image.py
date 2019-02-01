# todo 制作图片缩略图

from PIL import Image

def thumbnail_pic():
    a="3.jpg"
    im=Image.open(a)
    im.thumbnail((450,680))
    print(im.format,im.size,im.mode)
    im.save('vv.jpg')
    print('Done!')

if __name__=='__main__':
    thumbnail_pic()
