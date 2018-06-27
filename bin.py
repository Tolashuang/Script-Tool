# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:39:45 2017

@author: taozi
"""

import struct 

fin1 = open("D://code//txt_bin//x2.txt","r")

fin2 = open("D://code//txt_bin//x10.bin","wb")

for string in fin1:
    
    pi = struct.pack('f',float(string))
    
    fin2.write(pi)

fin1.close()
fin2.close()