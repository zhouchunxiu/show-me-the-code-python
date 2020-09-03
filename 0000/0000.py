# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。
# pillow文档： https://www.osgeo.cn/pillow/handbook/index.html
from PIL import Image, ImageDraw, ImageFont

# 打开头像
img = Image.open("头像.jpg")
# 获取图片的长、宽
w, h = img.size
# 创建头像的画笔
draw = ImageDraw.Draw(img)
# 创建字体（样式，大小）
myFont = ImageFont.truetype("arial.ttf", 50)
# 画笔颜色
fillcolor = "#ff0000"
# 在头像上画字符串（(x,y), string, 颜色， 字体）
draw.text((w-50, 10), "1", fill=fillcolor, font=myFont)
# 保存修改后的头像
img.save("新头像.jpg", "JPEG")


