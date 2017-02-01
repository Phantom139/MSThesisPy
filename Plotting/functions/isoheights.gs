function isoheights(args)
 level=subwrd(args,1)
'set gxout contour'
'set ccolor 99'
'set cthick 4'
if (level = surface)
 'd MSLETmsl/100'
endif
if (level != surface)
 'd HGTprs'
endif
