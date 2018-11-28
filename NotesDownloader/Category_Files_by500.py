# _*_ coding:utf-8 _*_
import os
import os.path
import shutil

rootdir = r'e:\HMV\Notes'
src = ''
dest = ''

for parent,dirnames,filenames in os.walk(rootdir):
    i = 0
    for idx,filename in enumerate(filenames):
        if(idx%490==0):
            i+=1
            path = os.path.join(parent,str(i))
            if not os.path.exists(path):
                os.mkdir(path)
        src = os.path.join(parent,filename)
        dest = os.path.join(path,filename)
        shutil.copyfile(src,dest)

