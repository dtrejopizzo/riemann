import os; HERE=os.path.dirname(os.path.abspath(__file__))
# prolate Legendre coefficients (same convention as prolate_tailgram.py: D_0 > 0), T=0.8
import mpmath as mp, numpy as np, pickle
mp.mp.dps=60
T=mp.mpf('1.0'); lam=mp.exp(T); NN=lam**2; c=2*mp.pi*NN
K=int(float(c))+120+80; kl=list(range(0,K,2)); m=len(kl)
dg=[k*(k+1)+c**2*mp.mpf(2*k*(k+1)-1)/((2*k+3)*(2*k-1)) for k in kl]
of=[c**2*mp.mpf((k+2)*(k+1))/((2*k+3)*mp.sqrt(mp.mpf((2*k+1)*(2*k+5)))) for k in kl[:-1]]
Md=np.diag([float(x) for x in dg])+np.diag([float(x) for x in of],1)+np.diag([float(x) for x in of],-1)
ev=sorted(np.linalg.eigvalsh(Md))[:60]
def inviter(sh,its=30):
    x=[mp.mpf(1)/(i+1) for i in range(m)]
    for it in range(its):
        cp=[mp.mpf(0)]*m; dp=[mp.mpf(0)]*m
        a0=dg[0]-sh; cp[0]=of[0]/a0; dp[0]=x[0]/a0
        for i in range(1,m):
            den=dg[i]-sh-of[i-1]*cp[i-1]
            if i<m-1: cp[i]=of[i]/den
            dp[i]=(x[i]-of[i-1]*dp[i-1])/den
        y=[mp.mpf(0)]*m; y[-1]=dp[-1]
        for i in range(m-2,-1,-1): y[i]=dp[i]-cp[i]*y[i+1]
        nr=mp.sqrt(mp.fsum(t*t for t in y)); xn=[t/nr for t in y]
        if xn[0]<0: xn=[-t for t in xn]
        Ax=[dg[i]*xn[i]+(of[i]*xn[i+1] if i<m-1 else 0)+(of[i-1]*xn[i-1] if i>0 else 0) for i in range(m)]
        if it>=3: sh=mp.fsum(a*b for a,b in zip(Ax,xn))
        x=xn
    return x
De=np.array([[float(v) for v in inviter(mp.mpf(e0)-mp.mpf(10)**(-9)*(1+abs(e0)))] for e0 in ev])
pickle.dump(dict(De=De,kl=kl,lam=float(lam)),open('coef10.pkl','wb')); print(De.shape)
