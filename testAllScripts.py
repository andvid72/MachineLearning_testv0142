# -*- coding: utf-8 -*-
import runpy
import os
from os import listdir


path=os.getcwd()+'\Scripts'
os.chdir(path)
files = [f for f in listdir(path) if f.endswith('.py')]
files.pop()

for f in files:    
    if f[0:3]!='ex0':
        print(f)
        runpy.run_path(path_name=path + "\\" + f)