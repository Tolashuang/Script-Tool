# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 11:06:24 2017

@author: taozi
"""

DEBUG_FLAG = True
import os
from PIL import Image
if DEBUG_FLAG:
    from PIL import ImageDraw
import json
import random


def check_rect(rt,width,height):
    if rt[0]>=0 and rt[2]>0 and rt[0]+rt[2]<=width and rt[1]>=0 and rt[3]>0 and rt[1]+rt[3]<=height:
        return True
    else:
        return False
    
def check_person_labels(str_name):
    flabel = open('D:/PersonData20170626RTXJL/labels/'+str_name+'.json')
    json_obj=json.load(flabel)
    flabel_out = open(r"D:/PersonData20170626RTXJL/labels/"+str_name+".txt","w")
    if not os.access('D:/PersonData20170626RTXJL/CheckImages',os.F_OK):
		os.mkdir('D:/PersonData20170626RTXJL/CheckImages')
   
    cnt=0
    r=0
    for node in json_obj['images']:
        img_name=str(node['file'])
        cnt+=1
        #print str(cnt)
        #rand=1
        rd_num=random.randint(0,9)
        #print rd_num
        
        try:
            img = Image.open('D:/PersonData20170626RTXJL/JPEGImages/'+str_name+'/'+img_name)
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
                
        if len(L)>0:
            spl=img_name.split('.')
            label_name=spl[0]+'.'+spl[1]+'.txt'
            #label_name=spl[0]+'.txt'
            flabel_out.writelines(img_name+' '+str(width)+' '+str(height)+' '+str(len(L))+'\n')
            
            fout = open("D:/PersonData20170626RTXJL//labels_out/"+label_name,"w")
            if DEBUG_FLAG and rd_num==0:
                draw = ImageDraw.Draw(img)
                
            fout.writelines(' '.join([str(spl[0]),str(spl[1]),str(spl[2]),str(width),str(height),str(len(L))])+"\n")
            #else:
            #    pass
            for lnode in L:           
                if not check_rect(lnode,width,height):
                    print img_name
                    print "(%f,%f,%f,%f) is not a valid rect"%(lnode[0],lnode[1],lnode[2],lnode[3])
                    #continue
                flabel_out.writelines(' '.join([str(lnode[0]),str(lnode[1]),str(lnode[2]),str(lnode[3]),lnode[4]])+"\n")
                #lnorm = [(lnode[0]+lnode[2]/2),(lnode[1]+lnode[3]/2),lnode[2],lnode[3]/height]
                
                lnorm = [lnode[0],lnode[1],lnode[2],lnode[3]]

                
                r=r+1
                
                fout.writelines(' '.join([str(lnorm[0]),str(lnorm[1]),str(lnorm[2]),str(lnorm[3]),str(lnode[4])])+"\n")
    
                #a=len(L)
                #print a
        
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
            #if DEBUG_FLAG and rd_num==0:  
                img.save("D:/PersonData20170626RTXJL/CheckImages/"+img_name,qtables='web_low')
               
                img.close
                #del draw
    print str(cnt)
    print str(r)
    print "done!"
    
if __name__ == "__main__":
   
    check_person_labels("1")
    #check_person_labels("2")
    #check_person_labels("3")