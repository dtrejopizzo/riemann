# TEST_CG_001: tables of zeta-type special functions on Re s = 1/2 and Re s = c (mpmath, dps = 30).
# Usage: python3 TEST_CG_001_zeta_tables.py TMAX PPU OUT.npz   (GL panels [k,k+1], PPU nodes per unit)
import sys, numpy as np, mpmath as mp
from multiprocessing import Pool
TMAX=int(sys.argv[1]); PPU=int(sys.argv[2]); OUT=sys.argv[3]; C=1.5
gx,gw=np.polynomial.legendre.leggauss(PPU)
tau=np.concatenate([k+(gx+1)/2 for k in range(TMAX)]); wt=np.tile(gw/2,TMAX)
def row(t):
    mp.mp.dps=30
    out=[]
    for sig in (0.5,C):
        s=mp.mpc(sig,t)
        z=mp.zeta(s); zp=mp.zeta(s,derivative=1)
        cl=mp.log(mp.pi)-mp.digamma((1-s)/2)/2-mp.digamma(s/2)/2   # chi'/chi(s), zeta(s)=chi(s)zeta(1-s)
        out+= [complex(z),complex(zp),complex(cl)]
    th=float(mp.re(mp.digamma(mp.mpf(0.25)+0.5j*t))-mp.log(mp.pi))
    return out+[th]
if __name__=="__main__":
    with Pool(20) as p: R=np.array(p.map(row,tau,chunksize=200))
    np.savez(OUT,tau=tau,wt=wt,C=C,zl=R[:,0],zpl=R[:,1],cll=R[:,2],zc=R[:,3],zpc=R[:,4],clc=R[:,5],th=R[:,6].real)
    print("done",len(tau))
