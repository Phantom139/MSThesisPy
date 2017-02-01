* 700mb frontogenesis
* MSLP, Temperature, and Winds
* By: Robert C. Fritzen
function surfacemap(args)
 ctlFile = subwrd(args,1)
 modelHr = subwrd(args,2)
 domain = subwrd(args,3)
 fYr = subwrd(args,4)
 fMo = subwrd(args,5)
 fDy = subwrd(args,6)
 fHr = subwrd(args,7)
 level = 700
 filename = '700fronto_'domain'_'modelHr'.png'
 'run /media/robert/HDD/WRF/Plotting/functions/pltdefaults.gs'
'open 'ctlFile
'set t 'modelHr+1
'set gxout shade2'
'run /media/robert/HDD/WRF/Plotting/functions/draw_states.gs'
'run /media/robert/HDD/WRF/Plotting/colorbars/color.gs -20 60 2.5 -kind dimgray-(7)->white-(0)->(0,150,0,111)->yellow->orange->red->maroon->magenta->indigo->blue->darkturquoise'
'set lev 'level
'run /media/robert/HDD/WRF/Plotting/functions/dynamics.gs'
'd F'
'set cint 30'
'run /media/robert/HDD/WRF/Plotting/functions/isoheights.gs 'level
* Draw Wind Barbs
'run /media/robert/HDD/WRF/Plotting/functions/windbarbs.gs 'level' 20 20'
* Finalize the Image
'run /media/robert/HDD/WRF/Plotting/functions/pltcolorbar.gs -ft 1 -fy 0.33 -line on -fskip 2 -fh .1 -fw .1 -lc 99 -edge triangle -fc 99'
'run /media/robert/HDD/WRF/Plotting/functions/draw_title.gs `4700mb Frontogenesis (`3.`4C 100km`a-1`n 3hr`a-1`n) | Wind (kts) | Valid: 'fMo'/'fDy'/'fYr' 'fHr':00:00 Z | WRF ARW V3.8 | M.S. Thesis Robert C. Fritzen'
'run /media/robert/HDD/WRF/Plotting/functions/make_image.gs 'filename
'close 1'