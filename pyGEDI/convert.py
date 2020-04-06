#!/usr/bin/env python

import os

try:
	import subprocess
except ImportError:
	sys.exit("""You need following module: subprocess """)

def df2csv(df,filename,outdir):
    try:
        os.makedirs(outdir)
    except:
        print ("Successfully created")        
    df.to_csv(outdir+filename+'.csv', index=False, header=True)  
    return 'DataFrame successfully converted.'

def csv2shp(csv_file,filename,outdir):
    if os.path.exists(csv_file):
        try:
            os.makedirs(outdir)
        except:
            print ("Successfully created")   
        comand= ['ogr2ogr','-oo','X_POSSIBLE_NAMES=lon*','-oo','Y_POSSIBLE_NAMES=lat*','-f','ESRI Shapefile','-wrapdateline','-t_srs','EPSG:4326','-s_srs','EPSG:4326',outdir+filename+'.shp',csv_file]
        subprocess.Popen(comand) 
        return 'File successfully converted.'
    else:
        return 'CSV file does not exist'
    
def shp2tiff(shp_file, layername, pixelsize, nodata, ot, filename,outdir):
    if os.path.exists(shp_file):
        try:
            os.makedirs(outdir)
        except:
            print ("Successfully created")   
        comand=['gdal_rasterize','-tr',pixelsize,pixelsize,'-a_nodata',nodata,'-ot',ot,'-of','GTiff','-co','COMPRESS=LZW','-a',layername,shp_file,outdir+filename+'.tif']
        subprocess.Popen(comand)
        return 'File successfully converted.'

    else:
        return 'SHP file does not exist'


