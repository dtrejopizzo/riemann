import numpy as np, time, revlib as R
T=0.5*np.log(3.0)
gam=R.load_zeros(); print("zeros",len(gam),gam[-1])
tau=np.arange(0,20.0001,0.05)
# a smooth C^1 flat-top: w = 2e^{-2v} - e^{-4v}  (w(0)=1, w'(0)=-4+4=0)
sv=np.array([2.0,4.0]); x=np.array([2.0,-1.0])
t0=time.time(); Bz,Az=R.zero_side_matrix(tau,T,sv,gam); print("zero side",time.time()-t0)
fz=Bz+x@Az
ns,lam=R.vonmangoldt_table(10**6); print("primepowers",len(ns))
t0=time.time(); fp=R.f_prime_side(tau,T,sv,x,ns,lam); print("prime side",time.time()-t0)
d=fz-fp
print("max|diff|",np.abs(d).max(),"mean",d.mean(),"std",d.std())
for i in range(0,len(tau),80): print(f"{tau[i]:7.2f} {fz[i]:14.6f} {fp[i]:14.6f} {d[i]:12.3e}")
