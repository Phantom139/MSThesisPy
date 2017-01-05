function barb_spacing(args)
 level = subwrd(args,1)
 xspacing = subwrd(args,2)
 yspacing = subwrd(args,3)
'set gxout barb'
'set rgb 99 0 0 0'
'set ccolor 99'
'set cthick 1'
'set digsize 0.05'
'define xskip = skip(UGRDprs,'xspacing','yspacing')*2'
'define yskip = skip(VGRDprs,'xspacing','yspacing')*2'
'define iskip = skip(UGRD10m,'xspacing','yspacing')*2'
'define jskip = skip(VGRD10m,'xspacing','yspacing')*2'
if level = surface
 'd iskip;jskip'
endif
if level != surface
 'd xskip;yskip'
endif
