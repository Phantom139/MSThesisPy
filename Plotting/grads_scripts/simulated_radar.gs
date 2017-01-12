* Simulated Radar Reflectivity
* By: Robert C. Fritzen
function main(args)
 ctlFile = subwrd(args,1)
 modelHr = subwrd(args,2)
 domain = subwrd(args,3)
 fYr = subwrd(args,4)
 fMo = subwrd(args,5)
 fDy = subwrd(args,6)
 fHr = subwrd(args,7)
 filename = 'simradar_'domain'_'modelHr'.png'
 'run /media/robert/HDD/WRF/Plotting/functions/pltdefaults.gs'
'open 'ctlFile
'set datawarn off'
'set t 'modelHr+1
'set gxout shade2'
'run /media/robert/HDD/WRF/Plotting/colorbars/color.gs 0 80 2.5 -kind white-(0)->white-(0)->lightgray-(5)->(4,70,28)-(5)->(4,234,28)-(0)->(252,238,4)-(4)->(236,130,4)-(0)->(244,46,4)-(4)->maroon-(0)->magenta->gray->lightgray'
'run /media/robert/HDD/WRF/Plotting/functions/draw_states.gs'
* Draw Radar
'd REFCclm'
* Draw MSLP / Centers
'set gxout contour'
'set ccolor 0'
'set cint 2'
'set clab masked'
'd MSLETmsl/100'
* 'run /media/robert/HDD/WRF/Plotting/functions/HI_LOW.gs'
* Finalize Image
'run /media/robert/HDD/WRF/Plotting/functions/pltcolorbar.gs -ft 1 -fy 0.33 -line on -fskip 2 -fh .1 -fw .1 -lc 99 -edge triangle -fc 99'
'run /media/robert/HDD/WRF/Plotting/functions/draw_title.gs Simulated Radar Reflectivity (DBZ) | Valid: 'fMo'/'fDy'/'fYr' 'fHr':00:00 Z | WRF ARW V3.8 | M.S. Thesis Robert C. Fritzen'
'run /media/robert/HDD/WRF/Plotting/functions/make_image.gs 'filename
