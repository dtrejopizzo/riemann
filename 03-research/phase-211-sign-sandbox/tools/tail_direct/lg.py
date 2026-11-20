import os; HERE=os.path.dirname(os.path.abspath(__file__))
import sys, numpy as np
src=open(''+HERE+'/adm.py').read().split('# tail')[0]
src=src.replace("exec(open(''+HERE+'/tail.py').read())","import scipy.linalg as sl, mpmath as mp")
exec(src)
import os; J=int(os.environ.get('JG','30'))
xg=np.linspace(lam,40,16001)
def tailF(g,yy):  # F g (xi) = 2 int_0 g cos(2 pi xi y) dy on xi grid, chunked
    out=np.zeros_like(xg)
    for i in range(0,len(xg),2000):
        q=xg[i:i+2000]; out[i:i+2000]=2*np.trapz(g[None,:]*np.cos(2*np.pi*np.outer(q,yy)),yy,axis=1)
    return out
yy=np.linspace(0,1/lam,601)
phis=[(1-(lam*yy)**2)**3*(lam*yy)**(2*j) for j in range(1,J+1)]
ints=np.array([np.trapz(p,yy) for p in phis])
Bc=sl.null_space(ints[None,:])    # combos with int phi = 0
Ph=np.array([tailF(p,yy) for p in phis]).T@Bc
uf=tailF(f,x)
w=np.sqrt(np.gradient(xg)*2)
Qg,_=np.linalg.qr(Ph*w[:,None]); r=uf*w; res=r-Qg@(Qg.T@r)
D_=r@r; L_=res@res
print(f"probe R={Rarg}: |f|^2={2*np.trapz(f**2,x):.4f} mass |y|<1/lam {2*np.trapz((f**2)[x<1/lam],x[x<1/lam]):.4f} |Ef|^2={c[0]:.5f} a_T={aT:.5f} | D={D_:.4f} l_g(J={J})={L_:.5f} | lam*a/D={lam*aT/D_:.4f} lam*a/l_g={lam*aT/L_:.4f}")
