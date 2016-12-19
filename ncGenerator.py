#!/usr/bin/env python

# By: Robert C Fritzen
# M.S. Thesis Research (Northern Illinois University, 2015-2017)
# Opens the met_em_* files in the specified directory.
#  (1) Prompts lat/lon to "Add" snow cover extent to
#  (2) Prompts lat/lon to "Remove" snow cover from.
# Generates two sets of experimental .nc files from which WRF can run on.

# Necessary Imports
import os
import errno
import numpy as np
import math
from netCDF4 import Dataset

# Constants
trgDir = '/media/robert/HDD/WRF/MSThesis/indata/'
dirSnowEnh = '/media/robert/HDD/WRF/MSThesis/SnowEnhanced/'
dirSnowDep = '/media/robert/HDD/WRF/MSThesis/SnowDepleted/'

# Application Class
## Handles all of the program's "duties"
class Application:

	def cot(self, x):
		return 1 / math.tan(x)
		
	def sec(self, x):
		return 1 / math.cos(x)

	def lambertToSpherical(self, x, y, rLat, rLon):
		stdP1 = math.radians(33)
		stdP2 = math.radians(45)
		qPi = 0.25 * math.pi;
		rLatRad = math.radians(rLat)
		rLonRad = math.radians(rLon)
		xRad = math.radians(x)
		yRad = math.radians(y)
		# n
		nNum = log( math.cos(stdP1) * self.sec(stdP2) )
		nDen = log( math.tan(qPi + (0.5 * stdP2)) * self.cot(qPi + (0.5 * stdP1)) )
		n = nNum / nDen
		sN = 1 if n >= 0 else -1
		# F
		fNum = math.cos(stdP1) * math.pow(math.tan(qPi + (0.5 * stdP1)), n)
		F = fNum / n
		# Ro0
		
		# Ro 
		return { 'lat':latDegree, 'lon':lonDegree }
	
	def sphericalToLambert(self, lat, lon, rLat, rLon):
		stdP1 = math.radians(33)
		stdP2 = math.radians(45)
		qPi = 0.25 * math.pi
		latRad = math.radians(lat)
		lonRad = math.radians(lon)
		rLatRad = math.radians(rLat)
		rLonRad = math.radians(rLon)
		n = math.log(math.cos(stdP1) * (1 / math.cos(stdP2))) / math.log(math.tan(qPi + (0.5 * stdP2)) * (1 / (math.tan(qPi + (0.5 * stdP1)))))
		F = (math.cos(stdP1) * math.pow(math.tan(qPi + (0.5 * stdP1)), n)) / n
		Ro0 = F * math.pow((1 / math.tan(qPi + (0.5 * rLatRad))), n)
		print "TEST: Ro: " , F
		Ro = F * math.pow((1 / math.tan(qPi + (0.5 * latRad))), n)
		x = Ro * math.sin(n * (lonRad - rLonRad))
		y = Ro0 - Ro * math.cos(n * (lonRad - rLonRad))
		xDeg = math.degrees(x)
		yDeg = math.degrees(y)
		return { 'x':xDeg, 'y':yDeg }

	def runTests(self):
		print('Code Tester')
		#minLat = raw_input("Define minimum latitude: ")
		#maxLat = raw_input("Define maximum latitude (999 for all): ")
		#minLon = raw_input("Define minimum longitude: ")
		#maxLon = raw_input("Define maximum longitude (999 for all): ")		
		#print('Boundary Conditions:')
		#minLat = int(minLat)
		#maxLat = int(maxLat)
		#minLon = int(minLon)
		#maxLon = int(maxLon)
		#print(minLat)
		#print(maxLat)
		#print(minLon)
		#print(maxLon)	
		# Test the dirSnowEnh variable
		try:
			os.makedirs(dirSnowEnh)
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise		
		# Loop
		print 'Preparing to read the first file from: ', trgDir
		for fileName in os.listdir(trgDir):
			if os.path.isfile(trgDir + fileName):
				print('Opening: ', fileName, '.')	
				fNameIn = trgDir + fileName
				fRead = Dataset(fNameIn, 'r')
				# Fetch important info
				i = fRead.dimensions['south_north']
				j = fRead.dimensions['west_east']
				for varname, ncvar in fRead.variables.iteritems():
					if varname == 'XLONG_M':
						lon = ncvar
					elif varname == 'XLAT_M':
						lat = ncvar
				for x in range(0, j.size):
					print "X = " , x
					for y in range(0, i.size):
						print "LAT: " , lat[:,y,x] , ", LON: " , lon[:,y,x] 
				print 'DONE'		
				break	
				

    # Create the "snow enhanced" files
	def generateSnowEnh(self):
		print('Snow Enhancement')
		minLat = raw_input("Define minimum latitude: ")
		maxLat = raw_input("Define maximum latitude (999 for all): ")
		minLon = raw_input("Define minimum longitude: ")
		maxLon = raw_input("Define maximum longitude (999 for all): ")		
		print('Boundary Conditions:')
		minLat = int(minLat)
		maxLat = int(maxLat)
		minLon = int(minLon)
		maxLon = int(maxLon)
		print(minLat)
		print(maxLat)
		print(minLon)
		print(maxLon)
		# Test the dirSnowEnh variable
		try:
			os.makedirs(dirSnowEnh)
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise		
		# Loop
		print 'Preparing to read files from: ', trgDir
		for fileName in os.listdir(trgDir):
			if os.path.isfile(trgDir + fileName):
				print('Opening: ', fileName, '.')
				fNameIn = trgDir + fileName
				fNameOut = dirSnowEnh + fileName
				fRead = Dataset(fNameIn, 'r')
				fWrite = Dataset(fNameOut, 'w')
				# Fetch important info
				i = fRead.dimensions['south_north']
				j = fRead.dimensions['west_east']
				lLon = getattr(fRead, 'corner_lons')[0]
				lLat = getattr(fRead, 'corner_lats')[0]
				hLon = getattr(fRead, 'corner_lons')[2]
				hLat = getattr(fRead, 'corner_lats')[2]
				hLatPt = hLat + 1 if maxLat == 999 else maxLat
				hLonPt = hLon + 1 if maxLon == 999 else maxLon
				print lLon , ' ' , lLat, ' ' , hLon, ' ', hLat
				print hLatPt
				print hLonPt				
				# Write the attributes from the existing netCDF file to the new one
				for attname in fRead.ncattrs():
					setattr(fWrite, attname, getattr(fRead, attname))
				# Write the dimensions from the existing netCDF file
				for dimname, dim in fRead.dimensions.iteritems():
					fWrite.createDimension(dimname, len(dim))
				# Variables: Read the lat/lon, establish regions where snow must be enhanced
				for vname, nvar in fRead.variables.iteritems():
					if vname == 'XLONG_M':
						lon = nvar
					elif vname == 'XLAT_M':
						lat = nvar	
				for varname, ncvar in fRead.variables.iteritems():
					# Read in remaining data
					var = fWrite.createVariable(varname, ncvar.dtype, ncvar.dimensions)				
					# Finish Writing the data
					for attname in ncvar.ncattrs():
						setattr(var, attname, getattr(ncvar, attname))
					var[:] = ncvar[:]
					# Adjust snow variable...
					if varname == 'SNOW':
						for x in range(0, i.size):
							for y in range(0, j.size):
								if lat[:,x,y] >= minLat and lat[:,x,y] <= hLatPt:
									if lon[:,x,y] >= minLon and lon[:,x,y] <= hLonPt:
										var[:,x,y] += 50
				print('Writing output file to: ', fNameOut, '.')
		print('Done...')
	
	# Create the "Snow depleted" files
	def generateSnowDep(self):
		print('Snow Depletion')
		minLat = raw_input("Define minimum latitude: ")
		maxLat = raw_input("Define maximum latitude (-1 for all): ")
		minLon = raw_input("Define minimum longitude: ")
		maxLon = raw_input("Define maximum longitude (-1 for all): ")
		print('Preparing to read files from: ', trgDir, '. Specified boundary conditions, Lat:[', minLat, ', ', maxLat, '], Lon:[', minLon, ', ', maxLon, '].')
		# Test the dirSnowEnh variable
		try:
			os.makedirs(dirSnowEnh)
		except OSError as exception:
			if exception.errno != errno.EEXIST:
				raise		
		# Loop
		for fileName in os.listdir(trgDir):
			if os.path.isfile(fileName):
				print('Opening: ', fileName, '.')
				fNameIn = trgDir + fileName
				fNameOut = dirSnowDep + fileName
				fRead = Dataset(fNameIn, 'r')
				fWrite = Dataset(fNameOut, 'w')
				# Fetch important info
				i = nc.dimensions['west_east']
				j = nc.dimensions['north_south']
				lLon = nc.getattr('corner_lons')[0]
				lLat = nc.getattr('corner_lats')[0]
				hLon = nc.getattr('corner_lons')[2]
				hLat = nc.getattr('corner_lats')[2]
				hLatPt = maxLat
				hLonPt = maxLon
				if maxLat == -1:
					hLatPt = hLat + 1
				if maxLon == -1:
					hLonPt = hLon + 1
				lats = np.linspace(lLat, hLat, j.size).tolist()
				lons = np.linspace(lLon, hLon, i.size).tolist()					
				# Write the attributes from the existing netCDF file to the new one
				for attname in fRead.ncattrs():
					setattr(fWrite, attname, getattr(fRead, attname))
				# Write the dimensions from the existing netCDF file
				for dimname, dim in fRead.dimensions.iteritems():
					fWrite.createDimension(dimname, len(dim))
				# Variables: Read the lat/lon, establish regions where snow must be enhanced
				for varname, ncvar in fRead.variables.iteritems():
					# Adjust snow variable...
					if varname == 'SNOW':
						for x in range(0, j.size):
							for y in range(0, i.size):
								#SNOW_PT = ncvar[:,x,y]
								if lats[x] > minLat and lats[x] < hLatPt:
									if lons[y] > minLon and lons[y] < minLonPt:
										ncvar[:,x,y] = 0
					# Read in remaining data
					var = fWrite.createVariable(varname, ncvar.dtype, ncvar.dimensions)
					# Finish Writing the data
					for attname in ncvar.ncattrs():
						setattr(var, attname, getattr(ncvar, attname))
					var[:] = ncvar[:]
				print('Writing output file to: ', fNameOut, '.')
		print('Done...')
	
	# Run the program
	def run(self):
		print('NC Generator')
		print('(C) Robert C Fritzen (2016)')
		print('M.S. Thesis Research Project')
		#self.runTests()
		self.generateSnowEnh()
		#self.generateSnowDep()
		print('Program Complete, Check for files in specified directories')
		
if __name__ == "__main__":
    print("Starting")
    Application().run()		
