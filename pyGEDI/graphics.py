#!/usr/bin/env python

try:
	from osgeo import gdal
except ImportError:
	sys.exit("""You need following module: gdal """)

try:
	import matplotlib.pyplot as plt
except ImportError:
	sys.exit("""You need following module: matplotlib """)
	
try:
	import copy
except ImportError:
	sys.exit("""You need following module: copy """)

try:
	import numpy as np
except ImportError:
	sys.exit("""You need following module: numpy """)


def histRaster(file_TIFF,bins):
    gedi_dataset = gdal.Open(file_TIFF)
    gedi_raster = gedi_dataset.GetRasterBand(1)
    noDataVal = gedi_raster.GetNoDataValue();print(noDataVal)
    scaleFactor = gedi_raster.GetScale()    
    cols = gedi_dataset.RasterXSize; 
    rows = gedi_dataset.RasterYSize;
    gedi_array = gedi_dataset.GetRasterBand(1).ReadAsArray(0,0,cols,rows).astype(np.float)
    gedi_array[gedi_array==int(noDataVal)]=np.nan
    gedi_array=gedi_array/scaleFactor
    gedi_nonan_array = copy.copy(gedi_array)
    gedi_nonan_array = gedi_nonan_array[~np.isnan(gedi_array)]    
    fig,ax= plt.subplots(figsize=(5,5))
    plt.hist(gedi_nonan_array.flatten(),bins=bins) 
    plt.title('Distribution of GEDI points')
    plt.xlabel('GEDI Tree Height (m)'); plt.ylabel('Number of pixels')

def plotSHP(GEDI_shp,metrics,colormap):
    GEDI_shp.plot(column = metrics, alpha = 0.9, markersize =5,cmap=colormap,figsize = (5,5))
    plt.title('GEDI Box', fontsize=15,fontweight='bold')
