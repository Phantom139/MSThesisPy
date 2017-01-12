* Surface Map
* MSLP, Temperature, and Winds
* By: Robert C. Fritzen
function main(args)
 ctlFile = subwrd(args,1)
 modelHr = subwrd(args,2)
 domain = subwrd(args,3)
 fYr = subwrd(args,4)
 fMo = subwrd(args,5)
 fDy = subwrd(args,6)
 fHr = subwrd(args,7)
 level = 'surface'
 filename = 'sfcmap_'domain'_'modelHr'.png'
 'run /media/robert/HDD/WRF/Plotting/functions/pltdefaults.gs'
'open 'ctlFile
'set datawarn off'
'set t 'modelHr+1
'run /media/robert/HDD/WRF/Plotting/colorbars/color.gs -30 115 2.5 -kind darkseagreen->lightgray->lightsteelblue->magenta->mediumblue->cyan->green->yellow->orange->red->maroon->magenta->white'
'set gxout shade2'
'run /media/robert/HDD/WRF/Plotting/functions/draw_states.gs'
* Draw Temperature
'd (TMP2m-273.16)*9/5+32'
* Draw MSLP Contour Lines
'set gxout contour'
'set ccolor 0'
'set cint 2'
'set clab masked'
'd MSLETmsl/100'
* Draw Wind Barbs
'run /media/robert/HDD/WRF/Plotting/functions/windbarbs.gs 'level' 20 20'
* Draw Pressure Centers
* 'run /media/robert/HDD/WRF/Plotting/functions/HI_LOW.gs'
* Finalize the Image
'run /media/robert/HDD/WRF/Plotting/functions/pltcolorbar.gs -ft 1 -fy 0.33 -line on -fskip 2 -fh .1 -fw .1 -lc 99 -edge triangle -fc 99'
'run /media/robert/HDD/WRF/Plotting/functions/draw_title.gs `42m Temp (`3.`4F) | 10m Wind (kts) | MSLP (mb) | Valid: 'fMo'/'fDy'/'fYr' 'fHr':00:00 Z | WRF ARW V3.8 | M.S. Thesis Robert C. Fritzen'
'run /media/robert/HDD/WRF/Plotting/functions/make_image.gs 'filename
