#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:    xurongzhong#126.com wechat:pythontesting qq:37391319
# CreateDate: 2018-3-15
# photos.py

import os

import cv2
import numpy as np
from PIL import Image, ImageDraw

def mark_image(filename, dst, poses):
    '''
    files： 文件列表
    dst： 目的文件目录
    poses: 为颜色跟对应的坐标(left, top, right,  bottom)。 
    比如{"green":(1,1,99,100)}
    '''
    image = Image.open(filename)
    d = ImageDraw.Draw(image, 'RGBA')
    for color in poses:
        d.rectangle(poses[color],outline=color)   
    image.save("{}{}{}".format(dst, os.sep, os.path.basename(filename)))
    
def rotate(files, dst, value=180):
    for file_ in files:
        image = Image.open(file_)
        image = image.rotate(value,resample=Image.BICUBIC, expand=1)
        image.save("{}{}{}".format(dst, os.sep, os.path.basename(file_)))    
 
def rotateImage(image, angle):
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

def rotate2(files, dst, value=90):
    for file_ in files:
        img = cv2.imread(file_,0)
        result = rotateImage(img, value)
        cv2.imwrite("{}{}{}".format(dst, os.sep, os.path.basename(file_)), 
                    result)     