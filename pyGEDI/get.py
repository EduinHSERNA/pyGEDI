#!/usr/bin/env python

import os, sys, ast, re

try:
	import requests
except ImportError:
	sys.exit("""You need following module: requests """)
try:
	import h5py
except ImportError:
	sys.exit("""You need following module: h5py """)

def getH5(fileh5):
	return h5py.File(fileh5, 'r')

def getLayer(layer, files):
    dictionary={}
    for fileh5 in files:      
        lista=h5layers(fileh5['BEAM0000'])        
        lista=str(lista).replace('[', '').replace(']', '').replace('/BEAM0000/', '')
        lista=ast.literal_eval(lista)       
        r=re.compile('.*'+layer)
        mylistafilter=list(filter(r.match,lista))        
        if len(mylistafilter)>0:
            dictionary[fileh5.filename]=mylistafilter            
    return dictionary

def getBeam(shot_number,file):
    for beam in ['BEAM0000','BEAM0001','BEAM0010','BEAM0011','BEAM0101','BEAM0110','BEAM1000','BEAM1011']: 
        if shot_number in file[beam]['shot_number'][:]:
            break
    return beam


def h5layers(arg):  
    lista=[]
    if isinstance(arg, h5py.Dataset):
        return arg.name
    if isinstance(arg, h5py.Group):
        for i in arg.keys():
            lista.append(h5layers(arg[i]))
    return lista

