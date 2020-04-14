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

try:
	import pandas as pd
except ImportError:
	sys.exit("""You need following module: pandas """)

try:
	import numpy as np
except ImportError:
	sys.exit("""You need following module: numpy """)


try:
	import subprocess
except ImportError:
	sys.exit("""You need following module: subprocess """)

from pyGEDI.get import *

   
def gediDownload(outdir,product,version,bbox,session):
	try:
		os.makedirs(outdir)
	except OSError:
		print ("Creation of the subdirectory %s failed" % outdir)
	else:
		print ("Created the subdirectory %s" % outdir)  
	
	url='https://lpdaacsvc.cr.usgs.gov/services/gedifinder?product='+product+'&version='+str(version)+'&bbox='+str(bbox)+'&output=json'
	content=requests.get(url)
	listh5=content.json().get('data')

	for url in listh5:
		url_response(outdir,url,session)

def idsBox(fileh5,latlayer,lonlayer,bbox):
    ids=[]
    [ul_lat,ul_lon,lr_lat,lr_lon]=bbox
    for beam in ['BEAM0000','BEAM0001','BEAM0010','BEAM0011','BEAM0101','BEAM0110','BEAM1000','BEAM1011']: 
        x=fileh5[beam][latlayer]        
        y=fileh5[beam][lonlayer]
        for i in range(len(x)):
            if ((abs(x[i])<=abs(ul_lat)) and (abs(x[i])>=abs(lr_lat)) and  (abs(y[i])<=abs(lr_lon)) and (abs(y[i])>=abs(ul_lon))):
                ids+=[(beam,fileh5[beam]['shot_number'][i])]
    return ids

def generateBoxDataFrame(filesh5,layers,idsbox):   
    df=pd.DataFrame()
    for layer in layers:
        colum=[]
        for ids in idsbox:
            for fileh5 in filesh5:
                for i in np.where(fileh5[ids[0]]['shot_number'][:]==ids[1])[0]:
                    if i and (layer in fileh5[ids[0]].keys()):
                        value=[fileh5[ids[0]][layer][i]]  
                        colum+=value 
                if layer in ['beam', 'shot_number', 'sensitivity']:
                    break
        df[layer]=colum
    return df


def generateDataFrame(filesh5,layers):
    df=pd.DataFrame()
    for layer in layers:
        colum=[]
        for beam in ['BEAM0000','BEAM0001','BEAM0010','BEAM0011','BEAM0101','BEAM0110','BEAM1000','BEAM1011']:   
            for fileh5 in filesh5:
                if layer in fileh5[beam].keys():
                    value=fileh5[beam][layer]                    
                    colum+=value  
                if layer in ['beam', 'shot_number', 'sensitivity']:
                    break
        df[layer]=colum
    return df

def url_response(outdir,url,session):        
	fileh5= url[url.rfind('/')+1:] 
	day=url[url.rfind(':')+41:url.rfind('/')+1]  
	path=outdir+day
	try:
		os.makedirs(path)
	except OSError:
		print ("Creation of the subdirectory %s failed" % path)
	else:
		print ("Created the subdirectory %s" % path)  
	path5=outdir+day+fileh5
	with open(path5, 'wb') as f:
		response = session.get(url, stream=True)
		total = response.headers.get('content-length')
		if total is None:
			f.write(response.content)
		else:
			downloaded = 0
			total = int(total)
			for data in response.iter_content(chunk_size=max(int(total/1000), 1024*1024)):
				downloaded += len(data)
				f.write(data)
				done = int(100*downloaded/total)
				gb=float(total/1073741824)

				sys.stdout.write('\r'+url[url.rfind(':')+52:]+' | '+str(gb)[:5]+'GB | '+ str(100*downloaded/total)+ '% [{}{}]'.format('█' * done, '.' * (100 -done)))
				sys.stdout.flush()
	sys.stdout.write('\n')


def waveForm(shot_number,fileh5):
    beam=getBeam(shot_number,fileh5)    
    shot_number_id=list(fileh5[beam]['shot_number'][:]).index(shot_number)

    elevation_bin0=fileh5[beam]['geolocation/elevation_bin0'][()]
    elevation_lastbin=fileh5[beam]['geolocation/elevation_lastbin'][()]
    rx_sample_count=fileh5[beam]['rx_sample_count'][()]
    rx_sample_start_index=fileh5[beam]['rx_sample_start_index'][()]
    
    rx_sample_start_index_n=rx_sample_start_index-min(rx_sample_start_index)+1

    rx_sample_start=int(rx_sample_start_index_n[shot_number_id])
    rx_sample_end=int(rx_sample_start_index_n[shot_number_id] + rx_sample_count[shot_number_id]-1)
    
    rxwaveform=fileh5[beam]['rxwaveform'][rx_sample_start:rx_sample_end][()]
    
    elevation_bin0_i=elevation_bin0[shot_number_id]
    elevation_lastbin_i=elevation_lastbin[shot_number_id]
    
    step=(elevation_bin0_i-elevation_lastbin_i)/rx_sample_count[shot_number_id]
    elevation=np.arange(elevation_lastbin_i,elevation_bin0_i,step)[:-1]
    
    return rxwaveform,elevation[::-1]
