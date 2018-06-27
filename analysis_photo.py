# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 15:30:04 2018

@author: Tolas_huang
"""

import os
import numpy as np
import matplotlib.pyplot as plt
#import pdb
print os.getcwd()
x = []
cfg=[]
weights=[]
lable=[]
recall_3=[]
recall_5=[]


def ana_log(log_name,group_len=256):
    try:
        
        fin=open(log_name,"r")
        while(True):
            online = fin.readline()
            if not online:  
                break  
            line_son = online.split(':')
            if 'lableNum' in line_son:
                line_son_son =  line_son[1]
                lable.append(line_son_son[:-1])
            if 'YOLO >0.3recall' in line_son:
                line_son_son =  line_son[1]
                recall_3.append(line_son_son[:-1])               
            if 'YOLO >0.5recall' in line_son:
                line_son_son =  line_son[1]
                recall_5.append(line_son_son[:-1])
                
        num = len(lable)/5.0 
        x = range(1,int(num)+1)
        print(x)
        print(lable)
        print(recall_3)
        print(recall_5)
        print (num)
        plt.figure(figsize=(8,4))
        
        plt.plot(x,recall_3[4: :5],label="$R>0.3_lable5$",color="red")
        plt.plot(x,recall_5[4: :5],label="$lable5$",color="blue")
        plt.plot(x,recall_3[3: :5],label="$lable4$",color="pink")
        plt.plot(x,recall_5[3: :5],label="$lable4$",color="green")
        plt.plot(x,recall_3[2: :5],label="$lable3$",color="orange")
        plt.plot(x,recall_5[2: :5],label="$lable3$",color="darkgreen")
        plt.plot(x,recall_3[1: :5],label="$lable2$",color="yellow")
        plt.plot(x,recall_5[1: :5],label="$lable2$",color="black")
#        plt.plot(x,recall_3[1: :5],label="$recall_3_lable4$",color="")
#        plt.plot(x,recall_5[3: :5],label="$recall_5_lable4$",color="brown")
#            plt.plot(x,obj,label="$obj$",color="blue")
#            plt.plot(x,recall,label="$recall$",color="green")
        plt.xlabel("weights")
        plt.ylabel("recall")
        plt.title("One Config Analysis")
        plt.legend()
        plt.show()        
            
        fin.close()

        
        
    except IOError:
        print('fail to open data file')


if '__main__' == __name__:

    ana_log("C:/Users/Tolas_huang/Desktop/hand_log_data.txt")


