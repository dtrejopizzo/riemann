# TEST_CG_001: explicit radical vector with Q(G,G) > 0 (radical span chi_j, ghat(0)=0); prints coefficients and stability in T.
import sys, os, numpy as np
src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'TEST_CG_001_analysis.py')).read().split('print("mu",mu')[0]
exec(src)
Ju=Juse[0]
Rc=np.zeros((nb,Ju)); Rc[K:K+Ju,:]=np.eye(Ju); Rc=gorth(Rc@null_of(d['g0'][K:K+Ju]),G)
QQ,QGG,S,QF,C0=forms(2000); e,v=np.linalg.eigh(sym(Rc.T@QGG@Rc)); x=Rc@v[:,-1]   # max Q(G,G)
x=x/np.abs(x[K:]).max()
print("coefficients on chi_j(t)=t^2(1-t^2)^MR P_2j(t), j<%d:"%Ju, np.array2string(x[K:K+Ju],precision=6,separator=','))
print("ghat(0) of combination: %.2e   ||rho||^2 = %.6e"%(x@d['g0'],x@G@x))
for T in (500,1000,2000):
    QQ,QGG,S,QF,C0=forms(T); n=x@G@x
    print("T=%d  Q(G,G)/||rho||^2=%.6f  QQ/||rho||^2=%.2e  (2Q(F,G)+2AB)/||rho||^2=%.6f  A=%.3e B=%.3e"%(T,x@QGG@x/n,x@QQ@x/n,x@S@x/n,x@A,x@B))
