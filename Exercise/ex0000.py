#0000题
from PIL import Image, ImageDraw, ImageFont

im = Image.open('E:/code/wechat.jpg')
dr = ImageDraw.Draw(im)
font = ImageFont.truetype('E:/code/Arial.ttf', 160)
dr.text((im.size[0]*0.90, im.size[1]*0.01), '2', font=font, fill="#ff0000")
im.show()
im.save('E:/code/newwechat.jpg')
