# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 11:55:52 2017

@author: taozi
"""


DEBUG_FLAG = True
import string
import linecache


def calcIOU(lineson1,lineson2):                           
        
    IOU=0.0
    one_x=float(lineson1[0])
    one_y=float(lineson1[1])
    one_w=float(lineson1[2])
    one_h=float(lineson1[3])
    two_x=float(lineson2[0])
    two_y=float(lineson2[1])
    two_w=float(lineson2[2])
    two_h=float(lineson2[3])                                        
    if((abs(one_x-two_x)<((one_w+two_w)/2.0))and(abs(one_y-two_y)<((one_h+two_h)/2.0))):  
        lu_x=max((one_x-(one_w/2.0)),(two_x-(two_w / 2.0)))  
        lu_y=min((one_y+(one_h/2.0)),(two_y+(two_h / 2.0)))  
  
        rd_x=min((one_x+(one_w/2.0)),(two_x+(two_w/2.0)))  
        rd_y=max((one_y-(one_h/2.0)),(two_y-(two_h/2.0)))  
  
        inter_w=abs(rd_x-lu_x)  
        inter_h=abs(lu_y-rd_y)  
  
        inter_square=inter_w*inter_h  
        union_square=(one_w*one_h)+(two_w*two_h)-inter_square  
  
        IOU = inter_square / union_square * 1.0     
    else:  
        IOU=0.0
  
    return IOU


files1 = open("D:/test_0926/OK_test/ok_out.txt")   
files2 = open("D:/test_0926/OK_test/OK-ltxt.txt")  


IOU=0.0
cnt=0
lable_ture=0
L1=[]
L2=[]
fulselable=0
IOU_out=[]
lable_num=0
fulselable_out=[]
#line_number = 0

for i in range(2348):
    
    line1 = files1.readline()
    if not line1:
        break
    elif '.jpg' in line1:          
        spl1=line1[:-1].split(' ')
        line_number = 0
        files2.seek(0)
        print spl1[0]
        for line_no, line in enumerate(files2):
            if spl1[0] in line:
                line_number = line_no+1
                break         
        if not line_number:
            continue
        spl3 = linecache.getline("D:/test_0926/OK_test/OK-ltxt.txt", line_number)
        coorson3=spl3[:-1].split(' ')
        print coorson3[0]
        num1=string.atoi(spl1[-1])
        num2=string.atoi(coorson3[-1])
        
        print num1, num2
        lable_num=lable_num+num1  
        if num1==0:
           print 'break' +'\n'
           continue
        else:
            for i in range(num2):
                flage=0
                spl2 = linecache.getline("D:/test_0926/OK_test/OK-ltxt.txt", line_number+i+1)
                for i in range(num1):
                    coor1 = files1.readline()
                    coorson2=spl2[:-1].split(' ')
                    coorson1=coor1.split(' ')[:-1]
                    if coorson1[-1] == "1":
                        print 'IOU'
                        IOU = calcIOU(coorson1[:-1], coorson2 )
                        print IOU
#                        print '\n\n'
                        if IOU > 0.3:
                            flage=1
                            lable_ture=lable_ture+1
                        else:
                            fulselable=fulselable+1
                else:
                     fulselable=fulselable+1
#                        print spl1[0]
#                        print IOU
#                        print fulselable_out            
#                        print '============================================================='
#        print "lable_num:"
#        print lable_num
#        print "lable_ture:"   
#        print lable_ture    
#        print "fulselable:"
#        print fulselable
#        print "done!"
    else:
        continue

print "lable_num:"
print lable_num
print "lable_ture:"   
print lable_ture    
print "fulselable:"
print fulselable
print "done!"
