# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 17:38:21 2017

@author: taozi
"""



DEBUG_FLAG = True
import string
import linecache


def calcIOU(lineson1,lineson2):                           
        
    IOU=0.0
    intersection=0.0
    one_x=float(lineson1[0])
    one_y=float(lineson1[1])
    one_w=float(lineson1[2])
    one_h=float(lineson1[3])
    two_x=float(lineson2[0])
    two_y=float(lineson2[1])
    two_w=float(lineson2[2])
    two_h=float(lineson2[3])      
    if (one_x > two_x + two_w):
        return 0   
    if (one_y > two_y + two_h):
        return 0  
    if (one_x + one_w < two_x):
        return 0  
    if (one_y + one_y < two_h):
        return 0  
    x=min(one_x+one_w,two_x+two_w) - max(one_x,two_x)                     
    y=min(one_y+one_h,two_y+two_h) - max(one_y,two_y)   
    
    intersection=x*y
    
    IOU=intersection/(one_w*one_h+two_w*two_h-intersection)

    return IOU


files1 = open("D:/model_test/wenqing1116/name_3_out.txt")   
files2 = open("D:/model_test/wenqing1116/name_3_in.txt")  

IOU=0.0
cnt=0
lable_ture=0
fulselable=0
IOU_out=[]
lable_num_in=0
lable_num_out=0
fulselable_out=[]
number_jpg_in=0
number_jpg_out=0


while(1):
    line2 = files2.readline()
    if not line2:
        break
    if '.jpg' in line2:
        number_jpg_in = number_jpg_in + 1
    else:
        continue
    
while(1):
    
    line1 = files1.readline()
    if not line1:
        break
    if '.jpg' in line1:
        number_jpg_out = number_jpg_out + 1          
        spl1=line1[:-1].split(' ')#discard '\n'
        line_number = 0
        files2.seek(0)#pointer to '0'
        print spl1[0]
        for line_no, line in enumerate(files2):
            if spl1[0] in line:
                line_number = line_no+1
                break         
        if not line_number:
            continue
        spl3 = linecache.getline("D:/model_test/wenqing1116/name_3_in.txt", line_number)
        coorson3=spl3[:-1].split(' ')
        print coorson3[0]
        num1=string.atoi(spl1[-1])
        num2=string.atoi(coorson3[-1])
    
        L1=[]
        num_son1=0
        for i in range(num1):
            subline1=files1.readline()
            subline1=subline1.split(' ')
#            print subline1[0]
            L1.append(subline1)
        for n in range(num1):
            if L1[n][4] == "2":  
                L1.append(L1[n])
                num_son1 = num_son1 + 1
                lable_num_out = lable_num_out + 1
        print L1
        
        
            
        L2=[]
        num_son2=0
        for j in range(num2):
            subline2=linecache.getline("D:/model_test/wenqing1116/name_3_in.txt", line_number+j+1)
            subline2=subline2.split()
#            print subline2[0]
            L2.append(subline2)
        for m in range(num2):
            if L2[m][4] == "4"  :
                L2.append(L2[m])
                num_son2 = num_son2 + 1
                lable_num_in = lable_num_in + 1
        print L2
        
        
        if len(L1) == 0:
            continue
  
        if num_son1 != 0:
            
            for n in range(num_son1):      
                
                    for m in range(num_son2):

                            print "IOU"
                            L1son = L1[n]
    #                        print L1son[:4]
                            L2son = L2[m]
    #                        print L2son
                            IOU = calcIOU(L1son[:4],L2son[:4])
                            print IOU
                            if IOU > 0.3:
                                lable_ture = lable_ture + 1

        else:
            continue
        
    else:
        continue
                    
fulselable = lable_num_out - lable_ture


print "number_jpg_in"
print number_jpg_in
print "number_jpg_out"
print number_jpg_out
print "lable_num_in:"
print lable_num_in
print "lable_num_out:"
print lable_num_out
print "lable_ture:"   
print lable_ture    
print "fulselable:"
print fulselable
print "done!"
