# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import struct
#import pdb
def txt2bin(fin,fout):
    #print ""
    #pdb.set_trace()
    Ldx=[]
    Ldy=[]
    Lsx=[]
    Lsy=[]
    Lsv=[]
    while(True):
        oneline=fin.readline()
        if len(oneline) <= 0:
            break;
        [y,x]=oneline.rstrip().split()
        #print x,y

        [sy1,sx1,sv1]=fin.readline().rstrip().split()
        [sy2,sx2,sv2]=fin.readline().rstrip().split()
        [sy3,sx3,sv3]=fin.readline().rstrip().split()
        [sy4,sx4,sv4]=fin.readline().rstrip().split()
        Ldx.append(x)
        Ldy.append(y)
        Lsx.append(sx1)
        Lsy.append(sy1)
        Lsv.append([sv1,sv2,sv3,sv4])

    fin.close()
    
    #pdb.set_trace()
    bts=struct.pack('i',len(Ldy))
    fout.write(bts) 
    for i in range(len(Ldy)):
        bts=struct.pack('i',int(Ldy[i]))
        fout.write(bts)
    for i in range(len(Ldx)):
        bts=struct.pack('i',int(Ldx[i]))
        fout.write(bts)
    for i in range(len(Lsy)):
        bts=struct.pack('i',int(Lsy[i]))
        fout.write(bts)
    for i in range(len(Lsx)):
        bts=struct.pack('i',int(Lsx[i]))
        fout.write(bts)
    for j in range(4):
        for i in range(len(Lsv)):
            bts=struct.pack('f',float(Lsv[i][j]))
            fout.write(bts)
    fout.close()
        
if __name__ == "__main__":
    inname=r"D:\camera_test\data\Slam\Matrices\distortion.txt"
    outname=r"D:\camera_test\data\Slam\Matrices\dist.bin"
    fin=open(inname,"r")
    fout=open(outname,"wb")
    txt2bin(fin,fout)
