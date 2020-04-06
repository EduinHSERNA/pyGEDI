![https://spotthestation.nasa.gov/](https://github.com/EduinHSERNA/pyGEDI/blob/master/blog/img_logo.png)

## Introduction
The new Global Ecosystem Dynamics Investigation [GEDI](https://gedi.umd.edu/) launched on December 5th, 2018 is operating onboard the International Space Station [ISS](https://spotthestation.nasa.gov/) producing a high-resolution laser collecting 3D data around Earth on forest canopy height, canopy vertical structure, and surface elevation. As it is collecting daily data, a stable and fast platform is essential. For this reason, the library __pyGEDI__ is developed in Python as it can utilize multiple CPUs, GPUs, and is supported by C and [GDAL](https://github.com/OSGeo/gdal). 

__pyGEDI__ provides a high performance, lower cognitive load, and cleaner and more transparent code for data extraction, analysis, processing, and visualization of GEDI's products.

## Package Overview 
__pyGEDI__ has multiple functions for visualization, processing, analysis, and data extraction all in one package. __pyGEDI__ package contains the following functions:  
- Connection to NASA's server.  
- Downloading GEDI data.   
- Clipping of your specific area.  
- Generate multiple files like `.csv`, `.shp`, and `.tif` for GEDI's products.  
- Visualization of waveforms with canopy height and profile metrics.  
- Process `.h5` files.  
- Generate histograms, raster’s of different GEDI metrics.  
- Graph in 3D cloud points.  
- Demonstrative products (correlation GEDI and Airborne Laser Scanning).

![https://github.com/EduinHSERNA/pyGEDI/blob/master/blog/graphics.jpeg](https://github.com/EduinHSERNA/pyGEDI/blob/master/blog/graphics.jpeg)


## Installation  

Options:  
- `pip install pyGEDI`  
- `git clone https://github.com/EduinHSERNA/pyGEDI.git`  

## Loading pyGEDI Package
`from pyGEDI import *`
## Session NASA  
Connect with NASA's server [Register for an Earthdata Login Profile](https://urs.earthdata.nasa.gov/users/new) (if you do not have an account register for a free account by providing your email).  
```
username='write your user name'
password='write your password'

session=sessionNASA(username,password)
```
## Set Parameters  
Define the coordinates of your specific area of interest. The next line will exhibit an example using coordinates in Colombia.
```  
ul_lat= 2.96845  
ul_lon=-73.32586
lr_lat=-1.26845
lr_lon=-70.23869  

bbox=[ul_lat,ul_lon,lr_lat,lr_lon]
```
## Download GEDI Data  
Now that the box is defined, download all GEDI trajectories that have flown over the area(s) of interest. Currently, there are only three products available with 25m resolution.  

This includes:  
- **Level 1 - Geolocated Waveforms**
- **Level 2- Footprint Level Canopy Height**  
- **Level 2- Profile Metrics**  

For more information check [GEDI Finder](https://lpdaacsvc.cr.usgs.gov/services/gedifinder)  

**Note:** GEDI Trajectories contain heavy amounts of data. It is recommended to have good internet for it to download in a more timely manner. Depending on your area of interest and trajectories this may take a couple hours illustrated by the download bar.
```
product_1B='GEDI01_B'
product_2A='GEDI02_A'
product_2B='GEDI02_B'

version='001'

outdir_1B='data/'+product_1B+'.'+version+'/'
outdir_2A='data/'+product_2A+'.'+version+'/'
outdir_2B='data/'+product_2B+'.'+version+'/'

gediDownload(outdir_1B,product_1B,version,bbox,session)
gediDownload(outdir_2A,product_2A,version,bbox,session)
gediDownload(outdir_2B,product_2B,version,bbox,session)
```
Once the download starts it will show a download bar for each file

```
Created the subdirectory   
data/GEDI01_B.001/2019.08.05/
GEDI01_B_2019217151359_O03661_T02309_02_003_01.h5 | 7.405GB | 24.19%   
[███████████████████......................................................]
```

## Research Products for Analysis, Processing, and Visualization    
Access the following notebooks for each respective product.

Notebook:
- [GEDI 2A](https://github.com/EduinHSERNA/pyGEDI/blob/master/notebook/GEDI2_A.ipynb) or [Colab.research](https://colab.research.google.com/drive/17yg17WSpZQr_9Aq2yOHUZumbR-ywM39I)
- [GEDI 2B](https://github.com/EduinHSERNA/pyGEDI/blob/master/notebook/GEDI2_B.ipynb) or [Colab.research](https://colab.research.google.com/drive/1KMxx7WdH4t55vHVx61HKRp_97Tc2-Mk4)
- [WaveForm GEDI 1B,2A,2B](https://github.com/EduinHSERNA/pyGEDI/blob/master/notebook/GEDI_Waveforms.ipynb) or [Colab.research](https://colab.research.google.com/drive/1NnG21nC6ubioMI6rnlRtYgjAp6lcMX0q)
- [Demonstrative products](https://github.com/EduinHSERNA/pyGEDI/blob/master/notebook/Demonstrative%20products.ipynb) or  [Colab.research](https://colab.research.google.com/drive/1LMfL0ssvP1jtWZLdKEZAhl9FOgXXkI8B)
  
## Pendings for v0.3:  
- Time series.  
- Export data to Google Earth Engine.
- Analysis for LEVEL 3 gridded canopy height metrics and variability.
- Analysis for LEVEL 4A and 4B Footprint and gridded aboveground carbon estimates.  
  
# References
- GEDI webpage. Accessed on April 4th 2020 https://gedi.umd.edu/  
- GEDI 1B version 001. Accessed on April 4th 2020 https://lpdaac.usgs.gov/products/gedi01_bv001/  
- GEDI 2A version 001. Accessed on April 4th 2020 https://lpdaac.usgs.gov/products/gedi02_av001/  
- GEDI 2B version 001. Accessed on April 4th 2020 https://lpdaac.usgs.gov/products/gedi02_bv001/  
- GEDI Finder. Accessed on April 4th 2020 https://lpdaacsvc.cr.usgs.gov/services/gedifinder  
- G-Liht webpage. Accessed on April 4th 2020 https://gliht.gsfc.nasa.gov/  
- The files `.h5` for the notebooks are temporally taken from: https://github.com/carlos-alberto-silva/rGEDI/tree/master/inst/extdata   

# Acknowledgements
We would like to thank The University of Maryland and NASA's Goddard Space Flight Center for developing GEDI's mission and for providing free and open data.

# Reporting Issues
Please report any issue regarding the __pyGEDI__ package to:  

- 137eduin[at]gmail[dot]com  
- andreshs[at]umd[dot]edu

pyGEDI blog forthcoming.

# Call for Contributions
__pyGEDI__ appreciates help from a wide range of different backgrounds. Small improvements or fixes are always appreciated. Kindly report any issues with labeling or processing. If you are considering larger contributions outside the traditional coding work, please contact us through the mailing list.


# Citing pyGEDI
Eduin H.SERNA; Andres Hernandez-Serna. pyGEDI: NASA's Global Ecosystem Dynamics Investigation (GEDI) mission data extraction, analysis, processing and visualization. version 0.2, April. 5th 2020, available at: https://pypi.org/project/pyGEDI/


# Disclaimer
__pyGEDI__ package has not been developed by the __GEDI team__. It comes with no guarantee, expressed or implied, and the authors hold no responsibility for its use or reliability of its outputs.

