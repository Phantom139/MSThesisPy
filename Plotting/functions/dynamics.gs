function dyanmics(args)
'q dims'

'hgt=hgtprs'
'tmp=tmpprs'
'vwnd=vgrdprs'
'uwnd=ugrdprs'

'pi=3.14159'
'dtr=pi/180'
'a=6.37122e6'
'omega=7.2921e-5'
'g=9.8'
'R=287'

'define f=2*omega*sin(lat*dtr)'
'define p=lev*100'

'dy=cdiff(lat,y)*dtr*a'
'dx=cdiff(lon,x)*dtr*a*cos(lat*dtr)'

'dhgtx=cdiff(hgt,x)'
'dhgty=cdiff(hgt,y)'

'define ug=-1*(g/f)*(dhgty/dy)'
'define vg=(g/f)*(dhgtx/dx)'

'define ua=uwnd-ug'
'define va=vwnd-vg'

'dugx=cdiff(ug,x)'
'dugy=cdiff(ug,y)'
'dvgx=cdiff(vg,x)'
'dvgy=cdiff(vg,y)'

'dtdx=cdiff(tmp,x)/dx'
'dtdy=cdiff(tmp,y)/dy'

'define Q1=-1*(R/p)*(dugx/dx*dtdx + dvgx/dx*dtdy)'
'define Q2=-1*(R/p)*(dugy/dy*dtdx + dvgy/dy*dtdy)'
'define divq=hdivg(Q1,Q2)'
'define tadv=(-uwnd*dtdx-vwnd*dtdy)'

'divg=hdivg(uwnd,vwnd)'
'vort=hcurl(uwnd,vwnd)'

'dvdx=cdiff(vort,x)/dx'
'dvdy=cdiff(vort,y)/dy'

'define vadv=(-uwnd*dvdx-vwnd*dvdy)'

'def1=cdiff(uwnd,x)/dx-cdiff(vwnd,y)/dy-vwnd*tan(dtr*lat)/a'
'def2=cdiff(vwnd,x)/dx+cdiff(uwnd,y)/dy+uwnd*tan(dtr*lat)/a'

'f1=-(dtdx*(divg+def1)+dtdy*(vort+def2))/2'
'f2=(dtdx*(vort-def2)-dtdy*(divg-def1))/2'


'fn=(dtdx*f1+dtdy*f2)/mag(dtdx,dtdy)'
'fs=(dtdx*f2-dtdy*f1)/mag(dtdx,dtdy)'

'fnx=-1*((dtdx*f1)/mag(dtdx,dtdy))*10e9'
'fny=-1*((dtdy*f2)/mag(dtdx,dtdy))*10e9'

'define F=(fn+fs)*1.08e9'

return
