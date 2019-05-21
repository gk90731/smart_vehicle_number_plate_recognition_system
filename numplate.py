# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:21:44 2018

@author: KUMAR GAURAV"""

import pytesseract
import urllib.request
import cv2
import numpy as np
import os
#f = open('output_recognised.txt','w')
#f.write('0')
#f.close()

while True:
    imgresp = urllib.request.urlopen('http://192.168.43.1:8080/photoaf.jpg')
    imgNp = np.array(bytearray(imgresp.read()),dtype = np.uint8)
    img = cv2.imdecode(imgNp,-1)
    text = pytesseract.image_to_string(img,lang = 'eng')
    print(text)
    #f = open('output_recognised.txt','a')
    #f.write(text)
    #f.close()
    #E:/zuk z2 plus 19.03.2018/OMKAR/All Photos/IMG_0054.JPG