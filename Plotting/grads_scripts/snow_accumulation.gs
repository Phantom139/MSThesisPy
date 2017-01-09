* Snow Accumulation Map
* Accumulated Snowfall at a 10-1 ratio
* By: Robert C. Fritzen
function main(args)
 ctlFile = subwrd(args,1)
 modelHr = subwrd(args,2)
 domain = subwrd(args,3)
 fYr = subwrd(args,4)
 fMo = subwrd(args,5)
 fDy = subwrd(args,6)
 fHr = subwrd(args,7)
 filename = 'snowaccum_'domain'_'modelHr'.png'
 'run /media/robert/HDD/WRF/Plotting/functions/pltdefaults.gs'
'open 'ctlFile
'set datawarn off'
'set gxout shade2'
'run /media/robert/HDD/WRF/Plotting/colorbars/color.gs 0 1000 500 -kind white->white'
'd TMP2m'
'run /media/robert/HDD/WRF/Plotting/colorbars/color.gs -levs 0 0.1 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6 6.5 7 7.5 8 8.5 9 9.5 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 27 29 31 33 35 37 39 -kind white-(4)->gray-(0)->paleturquoise-(6)->blue-(0)->indigo-(8)->mediumorchid-(0)->orchid->mediumvioletred->darksalmon->papayawhip'
'run /media/robert/HDD/WRF/Plotting/functions/draw_states.gs'
* Draw Snowfall
'define snaccum = sum((APCPsfc*CSNOWsfc),t=1,t='modelHr+1')/2.54'
'd snaccum'
* Finalize the Image
'run /media/robert/HDD/WRF/Plotting/functions/pltcolorbar.gs -ft 1 -fy 0.33 -line on -fskip 2 -fh .1 -fw .1 -lc 99 -fc 99'
'run /media/robert/HDD/WRF/Plotting/functions/draw_title.gs Accumulated Snowfall (in, 10:1 Ratio) | Valid: 'fMo'/'fDy'/'fYr' 'fHr':00:00 Z | WRF ARW V3.8 | M.S. Thesis Robert C. Fritzen'
'run /media/robert/HDD/WRF/Plotting/functions/make_image.gs 'filename
