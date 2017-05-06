import pandas as pd
import numpy as np
import sys
resfile=sys.argv[1]
dff=pd.read_csv(resfile)
names="ident, com, nplanets, massbudget, massefficiency, sigmag0, md, rc, ms, metal, taugas"
nlist=names.replace(',','').split()
mass=dff['emepla(i)/emet']+dff['emegas(i)']
dfter=dff[mass<10.]
rdata=np.zeros((len(np.unique(dfter.ident)),11))
kk=0
for i in np.unique(dfter.ident):    
    filter=dfter.ident==i
    dummy=dfter[filter]
    pmass=dummy['emepla(i)/emet']+dummy['emegas(i)']
    com=((pmass*dummy['a(i)']).sum())/pmass.sum()
    npl=len(dummy)
    mbud=pmass.sum()
    effm=mbud*3e-6/(dummy.emed.iloc[0])
    sigmag0=dummy.sigmag_0.iloc[0]
    md=dummy.emed.iloc[0]
    rc=dummy.rc.iloc[0]
    ms=dummy.emestar.iloc[0]
    metal=dummy.emetal.iloc[0]
    taugas=dummy.taugas.iloc[0]
    rdata[kk,:]=i,com,npl,mbud,effm,sigmag0,md,rc,ms,metal,taugas  
    kk=kk+1
pd.DataFrame(rdata,columns=nlist).to_csv('tr_%s.csv'%resfile[:-4])
dfgia=dff[mass>=10.]
rdatag=np.zeros((len(np.unique(dfgia.ident)),11))
kk=0
for i in np.unique(dfgia.ident):    
    filter=dfgia.ident==i
    dummy=dfgia[filter]
    pmass=dummy['emepla(i)/emet']+dummy['emegas(i)']
    com=((pmass*dummy['a(i)']).sum())/pmass.sum()
    npl=len(dummy)
    mbud=pmass.sum()
    effm=mbud*3e-6/(dummy.emed.iloc[0])
    sigmag0=dummy.sigmag_0.iloc[0]
    md=dummy.emed.iloc[0]
    rc=dummy.rc.iloc[0]
    ms=dummy.emestar.iloc[0]
    metal=dummy.emetal.iloc[0]
    taugas=dummy.taugas.iloc[0]
    rdatag[kk,:]=i,com,npl,mbud,effm,sigmag0,md,rc,ms,metal,taugas      
    kk=kk+1
pd.DataFrame(rdatag,columns=nlist).to_csv('gt_%s.csv'%resfile[:-4])
print("Total systems: "+str(len(np.unique(dff.ident))))
print("Systems with giant planets: "+str(kk-1))
print("%.1f percent of all planets are below 10 earth masses" %(100.*len(dfter)/len(dff)))
