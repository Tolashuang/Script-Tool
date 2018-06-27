# -*- coding: utf-8 -*-
"""
Created on Thu Feb 08 14:48:28 2018

@author: Tolas_huang
"""

import sys
import os
import threading
import urllib

'''
递归遍历文件夹，得到所有文件名
'''
def dir_list(path):
    allfile = []
    filelist = os.listdir(path)

    for filename in filelist:
        filepath = os.path.join(path, filename)
        if os.path.isdir(filepath):
            dir_list(filepath, allfile)
        else:
            allfile.append(filepath)

    return allfile

'''
保存远程url图片数据
'''
def download_and_save(url,savename):
    try:
        urlopen=urllib.URLopener()
        fp = urlopen.open(url)
        data = fp.read()
        fp.close()
        fid=open(savename,'w+b')
        fid.write(data)
        print "download succeed: "+ url
        fid.close()
    except IOError:
        print "download failed: "+ url


def get_all_iamge(filename):
    fid = open(filename)
    name = filename.split('\\')[-1]
    name = name[:-4]
    lines = fid.readlines()
    for line in lines:
        line_split = line.split(' ')
        image_id = line_split[0]
        image_url = line_split[1]
        if False == os.path.exists('./images' + '/' + name):
            os.mkdir('./images' + '/' + name)
        savefile = './images' + '/' + name + '/' + image_id + '.jpg'  
        #The maxSize of Thread numberr:1000
        while True:
            if(len(threading.enumerate()) < 1000):
                break               
        t = threading.Thread(target=download_and_save,args=(image_url,savefile,))
        t.start()

'''
usage: python download.py .\vgg_face_dataset\files
'''

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print'Usage:python %s faceUrl.txt'%(sys.argv[0])
        sys.exit()
    fileDir = sys.argv[1]
    list = dir_list(fileDir)
    for i in range(len(list)):
        #print list[i]
        get_all_iamge(list[i])