import sys
import os

#plotDef options:
# 1: Plot Both Control & Experimental
# 2: Plot Only Control
# 3: Plot Only Experimental
# 4: Output Commands to Terminal (Debug)
plotDef = 1

pathToPlot = '/media/robert/HDD/WRF/PyPlot/wrfplot.py'
pathToSave_Ctrl = '/media/robert/HDD/WRF/PyPlot/Images/'
pathToSave_Expr = '/media/robert/HDD/WRF/PyPlot/ImagesExpr/'
trgDir_Ctrl = '/media/robert/HDD/WRF/MSThesis/postrun_control/'
trgDir_Expr = '/media/robert/HDD/WRF/MSThesis/postrun_snowench/'
options = '--sfc --t2 --mslp --snow --simdbz --barbsize 1 --tunit F --ua --lvl 925,850 --save'


def run():
	print 'Running Script... Option: ' , plotDef

	if plotDef == 1:
		print '*******************************'
		print '*** PLOTTING BOTH CTRL/EXPR ***'
		print '*******************************'
		print '\n\n'
		print '*******************************'
		print '****** PLOTTING CONTROL *******'
		print '*******************************'
		for fileName1 in os.listdir(trgDir_Ctrl):
			if os.path.isfile(trgDir_Ctrl + fileName1):
				payload = "python " + pathToPlot + " " + options + " --infile " + trgDir_Ctrl + fileName1 + " --outdir " + pathToSave_Ctrl
				print 'Command: ' , payload
				os.system(payload)			
		print '*******************************'
		print '**** PLOTTING EXPERIMENTAL ****'
		print '*******************************'
		for fileName2 in os.listdir(trgDir_Expr):
			if os.path.isfile(trgDir_Expr + fileName2):
				payload = "python " + pathToPlot + " " + options + " --infile " + trgDir_Expr + fileName2 + " --outdir " + pathToSave_Expr
				print 'Command: ' , payload
				os.system(payload)				
	
	elif plotDef == 2:
		print '*******************************'
		print '****** PLOTTING CONTROL *******'
		print '*******************************'
		for fileName1 in os.listdir(trgDir_Ctrl):
			if os.path.isfile(trgDir_Ctrl + fileName1):
				payload = "python " + pathToPlot + " " + options + " --infile " + trgDir_Ctrl + fileName1 + " --outdir " + pathToSave_Ctrl
				print 'Command: ' , payload
				os.system(payload)
				
	elif plotDef == 3:
		print '*******************************'
		print '**** PLOTTING EXPERIMENTAL ****'
		print '*******************************'
		for fileName2 in os.listdir(trgDir_Expr):
			if os.path.isfile(trgDir_Expr + fileName2):
				payload = "python " + pathToPlot + " " + options + " --infile " + trgDir_Expr + fileName2 + " --outdir " + pathToSave_Expr
				print 'Command: ' , payload
				os.system(payload)		
	
	elif plotDef == 4:
		for fileName in os.listdir(trgDir_Ctrl):
			if os.path.isfile(trgDir_Ctrl + fileName):
				payload = "python " + pathToPlot + " " + options + " --infile " + trgDir_Ctrl + fileName + " --outdir " + pathToSave_Ctrl
				print 'Command: ' , payload
				#os.system(payload)	
				
	else:
		print 'Invalid Options'
		
		
run()
