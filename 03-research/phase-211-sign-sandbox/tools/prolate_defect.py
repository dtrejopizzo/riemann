import mpmath as mp, numpy as np
def prolate(c, K=None, dps=60, parity=0, nfun=6):
    """Lowest nfun prolates of given parity on [-1,1]: coefficients in normalised Legendre P̄_k = sqrt(k+1/2)P_k,
    by mp inverse iteration on the tridiagonal Legendre matrix of the prolate operator."""
    with mp.workdps(dps):
        c = mp.mpf(c)
        if K is None: K = int(float(c)) + 80
        ks = list(range(parity, K, 2)); m = len(ks)
        dg = [k*(k+1) + c**2*mp.mpf(2*k*(k+1)-1)/((2*k+3)*(2*k-1)) for k in ks]
        of = [c**2*mp.mpf((k+2)*(k+1))/((2*k+3)*mp.sqrt(mp.mpf((2*k+1)*(2*k+5)))) for k in ks[:-1]]
        Md = np.diag([float(x) for x in dg]) + np.diag([float(x) for x in of],1) + np.diag([float(x) for x in of],-1)
        ev = sorted(np.linalg.eigvalsh(Md))[:nfun]
        out=[]; vals=[]
        for e0 in ev:
            sh = mp.mpf(e0) - mp.mpf(10)**(-9)*(1+abs(e0))
            x = [mp.mpf(1)/(i+1) for i in range(m)]
            for it in range(5):
                cp=[mp.mpf(0)]*m; dp=[mp.mpf(0)]*m
                a0=dg[0]-sh; cp[0]=of[0]/a0; dp[0]=x[0]/a0
                for i in range(1,m):
                    den=dg[i]-sh-of[i-1]*cp[i-1]
                    if i<m-1: cp[i]=of[i]/den
                    dp[i]=(x[i]-of[i-1]*dp[i-1])/den
                y=[mp.mpf(0)]*m; y[-1]=dp[-1]
                for i in range(m-2,-1,-1): y[i]=dp[i]-cp[i]*y[i+1]
                nr=mp.sqrt(mp.fsum(t*t for t in y)); x=[t/nr for t in y]
            if x[0]<0: x=[-t for t in x]
            out.append(x)
        return ks, out
def evalP(ks, d, x):
    kmax = ks[-1]; vals=[mp.mpf(1), x]; a,b = vals
    for k in range(2, kmax+1):
        a, b = b, ((2*k-1)*x*b - (k-1)*a)/k; vals.append(b)
    return mp.fsum(dj*mp.sqrt(k+mp.mpf(1)/2)*vals[k] for dj,k in zip(d,ks))
def one_minus_chi0(c, dps=60, nodes=24):
    """1 - chi_0(c) from d log chi_0/dc = 2 psi_0(1)^2/c (psi_0 unit on [-1,1]); Gauss-Laguerre after s = c + x/2."""
    with mp.workdps(dps):
        c = mp.mpf(c); X, Wt = np.polynomial.laguerre.laggauss(nodes); tot = mp.mpf(0)
        for x, w in zip(X, Wt):
            s = c + mp.mpf(x)/2
            ks, D = prolate(s, dps=dps, nfun=1)
            p1 = evalP(ks, D[0], mp.mpf(1))
            tot += mp.mpf(w)*mp.exp(mp.mpf(x))*(2*p1**2/s)/2
        return -mp.expm1(-tot)
def asym(c): c=mp.mpf(c); return 4*mp.sqrt(mp.pi)*mp.sqrt(c)*mp.exp(-2*c)
if __name__=="__main__":
    import time
    for c in [2, 5, 10, 20, 40]:
        t=time.time(); v = one_minus_chi0(c, dps=50, nodes=20)
        print(c, mp.nstr(v,10), mp.nstr(v/asym(c),8), round(time.time()-t,1), flush=True)
