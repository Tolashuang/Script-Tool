# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 10:40:00 2017

@author: taozi
"""



DEBUG_FLAG = True
import os
from PIL import Image
from xml.etree import ElementTree


fines = open("D:PersonData20170626RTXJL/JPEGImages/2.txt","r")
choose_jpg = open("D:PersonData20170626RTXJL/JPEGImages/name_2.txt","w")

for line in fines:
    if not fines:
        break
    if '.jpg' in line:
        fines = line.split()
        #将目标元素写入到指定的文件夹
        choose_jpg.writelines(fines[0]+"\n")

        
choose_jpg.close()