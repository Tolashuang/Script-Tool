# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 14:20:29 2017

@author: taozi
"""

DEBUG_FLAG = True
import os
from PIL import Image
from xml.etree import ElementTree
import struct


files = open("D://code//txt_bin//distortion.txt")    
fin1 = open("D://code//txt_bin//x2.txt","wb")


fin2 = open("D://code//txt_bin//x3.bin","wb")
   
i = 0
xs = []
ys = []
xi = []
yi = []
value = []
a = []
b = []

for string in files:
    if (i%5 == 0):
#        print string
        strings = string.split(" ");
        xs.append(strings[0])
        ys.append(strings[1])
    
    if (i%5 == 1):
        strings = string.split(" ");
        xi.append(strings[0])
        yi.append(strings[1])
        value.append(strings[2])
        
    if (i%5 == 2):
        strings = string.split(" ");
        value.append(strings[2])
        
    if (i%5 == 3):
        strings = string.split(" ");
        value.append(strings[2])        
        
    if (i%5 == 4):
        strings = string.split(" ");
        value.append(strings[2])        
        
    i = i + 1

fin2.write(struct.pack("i", int(i/5)))

    
for m in xs:
    
    fin1.write(m)
    fin1.write("\n")
    pi = struct.pack('i',int(m))
    fin2.write(pi);
for m in ys:
    
    fin1.write(m)
    pi = struct.pack('i',int(m))
    fin2.write(pi);
    
for m in xi:
    
    fin1.write(m)
    fin1.write("\n")
    pi = struct.pack('i',int(m))
    fin2.write(pi);

for m in yi:
    
    fin1.write(m)
    fin1.write("\n")
    pi = struct.pack('i',int(m))
    fin2.write(pi);
    

for m in value:
    fin1.write(m)
    pi = struct.pack('f',float(m))
    fin2.write(pi);

fin1.close()
fin2.close()

print "finish"


    


