#!/usr/bin/env python

import os
import numpy as np
from netCDF4 import Dataset

file = 'test.nc'

def run():
	nc = Dataset(file, mode='r')
	i = nc.dimensions['west_east']
	j = nc.dimensions['south_north']
	SNOW = nc.variables['SNOW']
	
	lowest_lon = getattr(nc, 'corner_lons')[0]
	lowest_lat = getattr(nc, 'corner_lats')[0]
	
	highest_lat = getattr(nc, 'corner_lats')[2]
	highest_lon = getattr(nc, 'corner_lons')[2]
	
	print lowest_lon , ' => ', highest_lon
	print lowest_lat , ' => ', highest_lat
	
	lats = np.linspace(lowest_lat, highest_lat, j.size).tolist();
	lons = np.linspace(lowest_lon, highest_lon, i.size).tolist();
	
	print(lats)
	print(lons)
	
	print SNOW
	#for x in range(0, j.size):
	#	for y in range(0, i.size):
	#		ST = SNOW[:,x,y];
	#		print 'SNOW at ', x, ', ', y, ' (', lats[x], ',', lons[y],'): ', ST
			
			
run();
