"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小
iphone5 分辨率：1136×640像素
"""
from PIL import Image
import glob
import os

dir = os.path.join(os.getcwd(), "imgs")
save_dir = os.path.join(os.getcwd(), "new_imgs")
# 获取dir下所有图片的路径
paths = glob.glob(dir+"\\*.jpg")

for path in paths:
    img = Image.open(path)
    img.thumbnail((1136, 640))
    save_path = save_dir + "\\" + path.split("\\")[-1]
    img.save(save_path, "JPEG")
