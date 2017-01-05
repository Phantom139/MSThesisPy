* doplots.gs
* By: Robert C Fritzen
* Initializes calls to all other plot scripts
function main(args)
 ctlFile = subwrd(args,1)
 modelHr = subwrd(args,2)
 domain = subwrd(args,3)
 fYr = subwrd(args,4)
 fMo = subwrd(args,5)
 fDy = subwrd(args,6)
 fHr = subwrd(args,7)
* Run All Plots:
* Surface Map
'run /media/robert/HDD/WRF/Plotting/grads_scripts/surface_map.gs 'ctlFile' 'modelHr' 'domain' 'fYr' 'fMo' 'fDy' 'fHr
