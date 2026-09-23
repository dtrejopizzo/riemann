"""Spike areas of the Fourier transform of the finite-universe row D (zero measure) at log n.
Prediction (explicit formula, sum over gamma>0 with Gaussian cutoff w(gamma/Gamma)): area = -v_n/4 = -Lambda(n)/(2 sqrt n).
Run from scripts/reverse:  python3 dinf/spikes.py   (~5 s)"""
import numpy as np
from math import log,sqrt
z=np.loadtxt('zeros1.txt')
def Lam(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return log(p) if m==1 else 0.0
    return 0.0
def area(N,a,b):
    zz=z[:N]; G=zz[-1]; wt=np.exp(-2*(zz/G)**2)
    return ((np.sin(zz*b)-np.sin(zz*a))/zz*wt).sum()
if __name__=="__main__":
    print(" n    -v_n/4    A(Z_1000)   ratio    A(Z_100000)  ratio")
    for n in (2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,37,41):
        ln=log(n); pred=-2*Lam(n)/sqrt(n)/4
        a1=area(1000,ln-0.03,ln+0.03)-area(1000,ln+0.06,ln+0.12)
        a2=area(100000,ln-0.0008,ln+0.0008)-area(100000,ln+0.0016,ln+0.0032)
        print("%2d  %8.4f  %9.4f  %7.3f   %9.4f  %7.3f"%(n,pred,a1,a1/pred,a2,a2/pred))
