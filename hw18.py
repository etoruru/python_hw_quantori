#!/usr/bin/env python3

from PIL import Image


file_name = input('Введите имя файла: ')
param = input('Введите размер: ')
size = tuple([int(x) for x in param.split(',')])

saved = f'{file_name}_small.jpg'

img = Image.open(file_name)
img.thumbnail(size)
rgb_img = img.convert('RGB')
rgb_img.save(saved)
rgb_img.show()
