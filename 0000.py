from pillow import Image, ImageDraw, ImageFont

def add_num(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('D:/code/Arial.ttf', size=90)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width-90, 10), '4', font=myfont, fill=fillcolor)
    img.save('C:/Users/ASUS/Desktop/1wechat.jpg','jpeg')

if __name__ == '__main__':
    image = Image.open('C:/Users/ASUS/Desktop/wechat.jpg')
    add_num(image)