# double-precision look at g*(x): shape, zeros, correlation c_g(a) grid, Fourier energy distribution
import json,sys,os,numpy as np
from numpy.polynomial import legendre as Lg
D=os.environ['SP']+'/mori15'; p=int(sys.argv[1])
E=json.load(open(f'{D}/p{p}_eig.json')); v=np.array([float(x) for x in E['vectors'][0]])
N=1664; L=0.5*np.log(15); I=np.arange(p,N,2)
coef=np.zeros(N); coef[I]=v*np.sqrt((2*I+1)/(2*L))
x=np.linspace(-L,L,4001); g=Lg.legval(x/L,coef)
print('g(±L)=',g[0],g[-1],' g(0)=',g[2000],' max|g|=',abs(g).max(),' argmax x=',x[abs(g).argmax()])
sc=np.where(np.diff(np.sign(g))!=0)[0]; print('sign changes at x=',np.round(x[sc],4))
print('|v_j| by j (first 40):',np.round(np.abs(v[:40]),4))
print('energy fraction in first 10/20/40/80 modes:',[float((v[:k]**2).sum()) for k in (10,20,40,80)])
# correlation grid
dx=x[1]-x[0]; A=np.arange(0,2*L,0.002); cg=[]
for a in A:
    k=int(round(a/dx)); cg.append(np.sum(g[:len(g)-k]*g[k:])*dx)
cg=np.array(cg)
for a,cv in zip(A[::25],cg[::25]): print(f'c_g({a:.3f})={cv:+.5f}')
json.dump({'x':x[::10].tolist(),'g':g[::10].tolist(),'a':A.tolist(),'cg':cg.tolist()},open(f'{D}/p{p}_shape.json','w'))
