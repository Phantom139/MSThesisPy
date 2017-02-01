dset ^wrfprs_d02.00
index ^wrfprs_d02.00.idx
undef 9.999E+20
title wrfprs_d02.00
*  produced by grib2ctl v0.9.13
* command line options: -verf wrfprs_d02.00
dtype grib 255
pdef 820 425 lccr 30.273000 -111.851000 1 1 38.272000 38.272000 -102.674000 4000 4000
xdef 820 linear -111.851000 0.0421054170193698
ydef 425 linear 30.273000 0.0363636363636364
tdef 1 linear 12Z12feb2009 1mo
*  z has 25 levels, for prs
zdef 25 levels
1000 975 950 925 900 875 850 825 800 775 750 700 650 600 550 500 450 400 350 300 250 200 150 100 50
vars 135
no4LFTX180_0mb  0 132,116,46080 ** 180-0 mb above gnd Best (4-layer) lifted index [K]
ABSVprs 25 41,100,0 ** (profile) Absolute vorticity [/s]
ACPCPsfc  0 63,1,0  ** surface Convective precipitation [kg/m^2]
APCPsfc  0 61,1,0  ** surface Total precipitation [kg/m^2]
BRTMPtoa  0 118,8,0 ** top of atmos Brightness temperature [K]
CAPEsfc  0 157,1,0  ** surface Convective Avail. Pot. Energy [J/kg]
CAPE90_0mb  0 157,116,23040 ** 90-0 mb above gnd Convective Avail. Pot. Energy [J/kg]
CAPE180_0mb  0 157,116,46080 ** 180-0 mb above gnd Convective Avail. Pot. Energy [J/kg]
CAPE255_0mb  0 157,116,65280 ** 255-0 mb above gnd Convective Avail. Pot. Energy [J/kg]
CDCONclm  0 72,200,0 ** atmos column Convective cloud cover [%]
CFRZRsfc  0 141,1,0  ** surface Categorical freezing rain [yes=1;no=0]
CICEPsfc  0 142,1,0  ** surface Categorical ice pellets [yes=1;no=0]
CINsfc  0 156,1,0  ** surface Convective inhibition [J/kg]
CIN90_0mb  0 156,116,23040 ** 90-0 mb above gnd Convective inhibition [J/kg]
CIN180_0mb  0 156,116,46080 ** 180-0 mb above gnd Convective inhibition [J/kg]
CIN255_0mb  0 156,116,65280 ** 255-0 mb above gnd Convective inhibition [J/kg]
CPRATsfc  0 214,1,0  ** surface Convective precip. rate [kg/m^2/s]
CRAINsfc  0 140,1,0  ** surface Categorical rain [yes=1;no=0]
CSNOWsfc  0 143,1,0  ** surface Categorical snow [yes=1;no=0]
DLWRFsfc  0 205,1,0  ** surface Downward long wave flux [W/m^2]
DPTprs 25 17,100,0 ** (profile) Dew point temp. [K]
DPT2m  0 17,105,2 ** 2 m above ground Dew point temp. [K]
DPThlev1  0 17,109,1 ** hybrid level 1 Dew point temp. [K]
DPThlev2  0 17,109,2 ** hybrid level 2 Dew point temp. [K]
DSWRFsfc  0 204,1,0  ** surface Downward short wave flux [W/m^2]
DZDTprs 25 40,100,0 ** (profile) Geometric vertical velocity [m/s]
ELONsfc  0 177,1,0  ** surface East longitude (0-360) [deg]
EVPsfc  0 57,1,0  ** surface Evaporation [kg/m^2]
FRICVsfc  0 253,1,0  ** surface Friction velocity [m/s]
GFLUXsfc  0 155,1,0  ** surface Ground heat flux [W/m^2]
GRMR2mb  0 179,100,2 ** 2 mb Graupel mixing ratio [kg/kg]
GUSTsfc  0 180,1,0  ** surface Surface wind gust [m/s]
HCDChcl  0 75,234,0 ** high cloud level High level cloud cover [%]
HGTsfc  0 7,1,0  ** surface Geopotential height [gpm]
HGTprs 25 7,100,0 ** (profile) Geopotential height [gpm]
HGThlev1  0 7,109,1 ** hybrid level 1 Geopotential height [gpm]
HGThlev2  0 7,109,2 ** hybrid level 2 Geopotential height [gpm]
HGTclb  0 7,2,0 ** cloud base Geopotential height [gpm]
HGThtfl  0 7,204,0 ** highest trop freezing level Geopotential height [gpm]
HGTl215  0 7,215,0  ** unknown level Geopotential height [gpm]
HGTclt  0 7,3,0 ** cloud top Geopotential height [gpm]
HGT0deg  0 7,4,0 ** 0C isotherm level Geopotential height [gpm]
HGTadcl  0 7,5,0 ** adiabatic lifting condensation level Geopotential height [gpm]
HGTtrp  0 7,7,0 ** tropopause Geopotential height [gpm]
HLCY0_3000m   0 190,106,7680 ** 0-3000 m above ground Storm relative helicity [m^2/s^2]
HPBLsfc  0 221,1,0  ** surface Planetary boundary layer height [m]
ICECsfc  0 91,1,0  ** surface Ice concentration (ice=1;no ice=0) [fraction]
LANDsfc  0 81,1,0  ** surface Land cover (land=1;sea=0) [fraction]
LCDClcl  0 73,214,0 ** low cloud level Low level cloud cover [%]
LFTX500_1000mb  0 131,101,12900 ** 500-1000 mb Surface lifted index [K]
LHTFLsfc  0 121,1,0  ** surface Latent heat flux [W/m^2]
MAXREF1000m  0 235,105,1000 ** 1000 m above ground Hourly max of sim. reflect at 1km AGL [dbZ]
MCDCmcl  0 74,224,0 ** mid-cloud level Mid level cloud cover [%]
MSLETmsl  0 130,102,0 ** mean-sea level Mean sea level pressure (ETA model) [Pa]
MSTAV0_100cm  0 207,112,100 ** 0-100 cm underground Moisture availability [%]
NCPCPsfc  0 62,1,0  ** surface Large scale precipitation [kg/m^2]
NLATsfc  0 176,1,0  ** surface Latitude (-90 to +90) [deg]
PEVAPsfc  0 228,1,0  ** surface Pot. evaporation [kg/m^2]
PLI30_0mb  0 24,116,7680 ** 30-0 mb above gnd Parcel lifted index (to 500 hPa) [K]
PRATEsfc  0 59,1,0  ** surface Precipitation rate [kg/m^2/s]
PRESsfc  0 1,1,0  ** surface Pressure [Pa]
PREShlev1  0 1,109,1 ** hybrid level 1 Pressure [Pa]
PREShlev2  0 1,109,2 ** hybrid level 2 Pressure [Pa]
PRESclb  0 1,2,0 ** cloud base Pressure [Pa]
PRESclt  0 1,3,0 ** cloud top Pressure [Pa]
PRMSLmsl  0 2,102,0 ** mean-sea level Pressure reduced to MSL [Pa]
PWAT30_0mb  0 54,116,7680 ** 30-0 mb above gnd Precipitable water [kg/m^2]
PWATclm  0 54,200,0 ** atmos column Precipitable water [kg/m^2]
REFCclm  0 212,200,0 ** atmos column Maximum/Composite radar reflectivity [dbZ]
REFDprs 2 211,100,0 ** (profile) Derived radar reflectivity [dbZ]
REFD4000m  0 211,105,4000 ** 4000 m above ground Derived radar reflectivity [dbZ]
REFD1000m  0 211,105,1000 ** 1000 m above ground Derived radar reflectivity [dbZ]
REFDhlev1  0 211,109,1 ** hybrid level 1 Derived radar reflectivity [dbZ]
REFDhlev2  0 211,109,2 ** hybrid level 2 Derived radar reflectivity [dbZ]
RHprs 25 52,100,0 ** (profile) Relative humidity [%]
RH2m  0 52,105,2 ** 2 m above ground Relative humidity [%]
RWMRprs 2 170,100,0 ** (profile) Rain water mixing ratio [kg/kg]
RWMRhlev1  0 170,109,1 ** hybrid level 1 Rain water mixing ratio [kg/kg]
RWMRhlev2  0 170,109,2 ** hybrid level 2 Rain water mixing ratio [kg/kg]
SFCRsfc  0 83,1,0  ** surface Surface roughness [m]
SHTFLsfc  0 122,1,0  ** surface Sensible heat flux [W/m^2]
SNMRprs 2 171,100,0 ** (profile) Snow mixing ratio [kg/kg]
SNMRhlev1  0 171,109,1 ** hybrid level 1 Snow mixing ratio [kg/kg]
SNMRhlev2  0 171,109,2 ** hybrid level 2 Snow mixing ratio [kg/kg]
SNODsfc  0 66,1,0  ** surface Snow depth [m]
SNOLsfc  0 79,1,0  ** surface Large scale snow [kg/m^2]
SNOMsfc  0 99,1,0  ** surface Snow melt [kg/m^2]
SNOWCsfc  0 238,1,0  ** surface Snow cover [%]
SOILL0_10cm  0 160,112,10 ** 0-10 cm underground Liquid volumetric soil moisture (non-frozen) [fraction]
SOILL10_40cm  0 160,112,2600 ** 10-40 cm underground Liquid volumetric soil moisture (non-frozen) [fraction]
SOILL40_100cm  0 160,112,10340 ** 40-100 cm underground Liquid volumetric soil moisture (non-frozen) [fraction]
SOILL100_200cm  0 160,112,25800 ** 100-200 cm underground Liquid volumetric soil moisture (non-frozen) [fraction]
SOILM0_200cm  0 86,112,200 ** 0-200 cm underground Soil moisture content [kg/m^2]
SOILW0_10cm  0 144,112,10 ** 0-10 cm underground Volumetric soil moisture [fraction]
SOILW10_40cm  0 144,112,2600 ** 10-40 cm underground Volumetric soil moisture [fraction]
SOILW40_100cm  0 144,112,10340 ** 40-100 cm underground Volumetric soil moisture [fraction]
SOILW100_200cm  0 144,112,25800 ** 100-200 cm underground Volumetric soil moisture [fraction]
SPFHprs 25 51,100,0 ** (profile) Specific humidity [kg/kg]
SPFH2m  0 51,105,2 ** 2 m above ground Specific humidity [kg/kg]
SPFH30_0mb  0 51,116,7680 ** 30-0 mb above gnd Specific humidity [kg/kg]
SSRUNsfc  0 235,1,0  ** surface Storm surface runoff [kg/m^2]
TCDCclm  0 71,200,0 ** atmos column Total cloud cover [%]
TCOLCclm  0 140,200,0 ** atmos column Total column condensate [kg/m/m]
TCOLIclm  0 137,200,0 ** atmos column Total column cloud ice [kg/m/m]
TCOLRclm  0 138,200,0 ** atmos column Total column rain [kg/m/m]
TCOLSclm  0 139,200,0 ** atmos column Total column snow [kg/m/m]
TCOLWclm  0 136,200,0 ** atmos column Total column cloud water [kg/m/m]
TMPsfc  0 11,1,0  ** surface Temp. [K]
TMPprs 25 11,100,0 ** (profile) Temp. [K]
TMP2m  0 11,105,2 ** 2 m above ground Temp. [K]
TMPhlev1  0 11,109,1 ** hybrid level 1 Temp. [K]
TMPhlev2  0 11,109,2 ** hybrid level 2 Temp. [K]
TMPclt  0 11,3,0 ** cloud top Temp. [K]
TSOIL_300cm  0 85,111,300 ** 300 cm underground Soil temp. [K]
TSOIL0_10cm  0 85,112,10 ** 0-10 cm underground Soil temp. [K]
TSOIL10_40cm  0 85,112,2600 ** 10-40 cm underground Soil temp. [K]
TSOIL40_100cm  0 85,112,10340 ** 40-100 cm underground Soil temp. [K]
TSOIL100_200cm  0 85,112,25800 ** 100-200 cm underground Soil temp. [K]
UGRDprs 25 33,100,0 ** (profile) u wind [m/s]
UGRD10m  0 33,105,10 ** 10 m above ground u wind [m/s]
UGRDhlev1  0 33,109,1 ** hybrid level 1 u wind [m/s]
UGRDhlev2  0 33,109,2 ** hybrid level 2 u wind [m/s]
UGRD30_0mb  0 33,116,7680 ** 30-0 mb above gnd u wind [m/s]
ULWRFsfc  0 212,1,0  ** surface Upward long wave flux [W/m^2]
USWRFsfc  0 211,1,0  ** surface Upward short wave flux [W/m^2]
VEGsfc  0 87,1,0  ** surface Vegetation [%]
VGRDprs 25 34,100,0 ** (profile) v wind [m/s]
VGRD10m  0 34,105,10 ** 10 m above ground v wind [m/s]
VGRDhlev1  0 34,109,1 ** hybrid level 1 v wind [m/s]
VGRDhlev2  0 34,109,2 ** hybrid level 2 v wind [m/s]
VGRD30_0mb  0 34,116,7680 ** 30-0 mb above gnd v wind [m/s]
VISsfc  0 20,1,0  ** surface Visibility [m]
VVELprs 25 39,100,0 ** (profile) Pressure vertical velocity [Pa/s]
WEASDsfc  0 65,1,0  ** surface Accum. snow [kg/m^2]
WTMPsfc  0 80,1,0  ** surface Water temp. [K]
ENDVARS