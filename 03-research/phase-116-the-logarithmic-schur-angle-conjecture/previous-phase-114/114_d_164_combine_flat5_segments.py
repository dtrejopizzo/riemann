#!/usr/bin/env python3
"""Outward combination of the four D.162 frequency segments and D.159 tail."""
import glob,math,os
import numpy as np

files=sorted(glob.glob(os.environ.get('D164_GLOB','/tmp/d162_flat5_seg*.npz')),
             key=lambda f:int(np.load(f)['start']))
assert files
starts=[];ends=[];C=None;R=None
for f in files:
    z=np.load(f);c=z['C'];r=z['R'];starts.append(int(z['start']));ends.append(int(z['cutoff']))
    C=c.copy() if C is None else C+c
    R=r.copy() if R is None else R+r
assert starts[0]==0 and all(ends[i]==starts[i+1] for i in range(len(files)-1))
cutoff=ends[-1];source=np.load(os.environ.get('D164_FRAME','/tmp/d160_flat_arb_columns5_300.npz'))
dn=np.nextafter(np.asarray(source['derivative_norm2'],float),np.inf);T=.5*math.log(5);K=len(dn)
for p in range(1,5):
    a=40;ell=math.log(cutoff)+5
    series=sum(math.comb(p,j)*ell**(p-j)*math.factorial(j)/(a-1)**(j+1) for j in range(p+1))
    diag=2*T*dn/math.pi*cutoff**(1-a)*series
    for i in range(K):
        for j in range(K):R[p-1,i,j]+=math.sqrt(diag[i]*diag[j])

# Cover binary64 summation and enforce a common symmetric enclosure.
R=np.nextafter(R+np.abs(np.spacing(C))/2,np.inf)
for p in range(4):
    for i in range(K):
        for j in range(i):
            lo=min(C[p,i,j]-R[p,i,j],C[p,j,i]-R[p,j,i])
            hi=max(C[p,i,j]+R[p,i,j],C[p,j,i]+R[p,j,i])
            C[p,i,j]=C[p,j,i]=(lo+hi)/2;R[p,i,j]=R[p,j,i]=np.nextafter((hi-lo)/2,np.inf)
out=os.environ.get('D164_SAVE','/tmp/d162_matrix5_R2048_Q64.npz')
np.savez(out,C=C,R=R,start=0,cutoff=cutoff,order=int(np.load(files[0])['order']))
print('segments=',list(zip(starts,ends)))
print('max radii=',[R[p].max() for p in range(4)])
print('worst H4 diagonal tail=',max(2*T*dn/math.pi*cutoff**(-39)*sum(math.comb(4,j)*(math.log(cutoff)+5)**(4-j)*math.factorial(j)/39**(j+1) for j in range(5))))
print('saved',out)
