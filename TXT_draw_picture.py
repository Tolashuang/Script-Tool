# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 11:43:48 2017

@author: taozi
"""

DEBUG_FLAG = True
import os
from PIL import Image
if DEBUG_FLAG:
    from PIL import ImageDraw

import random



def check_rect(rt,width,height):
    if rt[0]>=0 and rt[2]>0 and rt[0]+rt[2]<=width and rt[1]>=0 and rt[3]>0 and rt[1]+rt[3]<=height:
        return True
    else:
        return False
    
def check_person_labels(str_name):
    flabel_out = open('D:/CV-ht/palm_test/'+str_name+'.txt')
    if not os.access('D:/CV-ht/palm_test/CheckImages',os.F_OK):
    		os.mkdir('D:/CV-ht/palm_test/CheckImages')

    for node in flabel_out:
        
        img_name=node.split()
        print img_name[0]
        
        rd_num=random.randint(0,3)
        
        try:
            img = Image.open('D:/palm-photo/'+img_name)
            [width,height]=img.size
            #print img_name
        except IOError:
            print 'fail to open image:'+img_name
            continue
        except:
            print 'Error occurred.'
            continue
        L=[]
        for box in node['boxes']:
            if box['width']>0 and box['height']>0:
                L.append([box['left'],box['top'],box['width'],box['height'],box['object']])
            #if box['object']=='Full':
                #L.append([box['left'],box['top'],box['width'],box['height']])
                

                flabel_out=open("D:/CV-ht/palm_test/palm-photo-out.txt",'w')
                flabel_out.writelines(' '.join([(box[0]),(box[1]),(box[2]),(box[3]),str[box[4]]])+"\n")
                flabel_out.close()
                
                
        if len(L)>0:
            spl=img_name.split('.')
            #label_name=spl[0]+'.'+spl[1]+'.txt'
            label_name=spl[0]+'.txt'
            flabel_out.writelines(img_name+' '+str(width)+' '+str(height)+' '+str(len(L))+'\n')
            #fout = open("./labels_out/"+label_name,"w")
            if DEBUG_FLAG and rd_num==0:
                draw = ImageDraw.Draw(img)
            for lnode in L:           
                if not check_rect(lnode,width,height):
#                    print img_name
#                    print "(%f,%f,%f,%f) is not a valid rect"%(lnode[0],lnode[1],lnode[2],lnode[3])
        
                flabel_out.writelines(' '.join([str(lnode[0]),str(lnode[1]),str(lnode[2]),str(lnode[3]),lnode[4]])+"\n")
                
                if DEBUG_FLAG and rd_num==0:
                    color=(255,0,0)
                    if lnode[4] == 'Full':
                        color=(0,0,255)
                    if lnode[4] == 'Upper':
                        color=(0,255,255)
                    if lnode[4] == 'Head':
                        color=(255,0,0)
                    if lnode[4] == 'Body':
                        color=(0,64,0)
                    draw.line((lnode[0],lnode[1],lnode[0],lnode[1]+lnode[3]),fill=color,width=3)
                    draw.line((lnode[0],lnode[1],lnode[0]+lnode[2],lnode[1]),fill=color,width=3)
                    draw.line((lnode[0]+lnode[2],lnode[1],lnode[0]+lnode[2],lnode[1]+lnode[3]),fill=color,width=3)
                    draw.line((lnode[0],lnode[1]+lnode[3],lnode[0]+lnode[2],lnode[1]+lnode[3]),fill=color,width=3)
            if DEBUG_FLAG and rd_num==0:  
                #img.save("D:/PersonData20170626RTXJL/CheckImages/"+img_name,qtables='web_low')
                #img.show('test')
                img.close
                del draw
    print "done!"
    
if __name__ == "__main__":
    #os.chdir(r"C:\Users\jimmypan\Downloads\PalmData");
    #check_person_labels("palm_part1")
    #check_person_labels("palm_part2")
    #check_person_labels("palm_part3")
    #check_person_labels("palm_part4")    
    #os.chdir(r"D:/PersonData20170626RTXJL/JPEGImages")
    #f=open('list.txt')
    #for line in f:
    #    label_path = line.rstrip()
    #    check_person_labels(label_path)
    #print 'done!'
    #os.chdir(r"C:\Users\jimmypan\Documents\PersonData20170626RTXJL");
    check_person_labels("palm-out")
    #check_person_labels("2")
    #check_person_labels("3")
    
    
