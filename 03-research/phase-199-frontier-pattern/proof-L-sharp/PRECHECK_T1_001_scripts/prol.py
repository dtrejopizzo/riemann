# PRECHECK_T1_001 part 1: even prolates at c=2πμ in mp (normalised Legendre tridiagonal), χ_k, μ_k, λ_k, ψ_k(0), ψ_k(1)
import mpmath as mp, numpy as np, json, sys
def prolates(mu, ks=(0,4,8,12)):
    dps=int(4*np.pi*mu/np.log(10))+70; mp.mp.dps=dps
    c=2*mp.pi*mu; n=int(1.3*float(c))+40
    diag=[];off=[]
    for t in range(n):
        j=2*t
        diag.append(mp.mpf(j*(j+1))+c*c*mp.mpf(2*j*(j+1)-1)/((2*j+3)*(2*j-1)))
        off.append(c*c*(j+2)*(j+1)/((2*j+3)*mp.sqrt((2*j+1)*(2*j+5))))
    Md=np.diag([float(x) for x in diag])+np.diag([float(x) for x in off[:-1]],1)+np.diag([float(x) for x in off[:-1]],-1)
    ev,evec=np.linalg.eigh(Md)
    def thomas(sig,rhs):
        b=[diag[t]-sig for t in range(n)]; cp=[0]*n; dp=[0]*n
        cp[0]=off[0]/b[0]; dp[0]=rhs[0]/b[0]
        for i in range(1,n):
            den=b[i]-off[i-1]*cp[i-1]; cp[i]=off[i]/den if i<n-1 else 0; dp[i]=(rhs[i]-off[i-1]*dp[i-1])/den
        x=[0]*n; x[n-1]=dp[n-1]
        for i in range(n-2,-1,-1): x[i]=dp[i]-cp[i]*x[i+1]
        return x
    P0=[]; p=mp.mpf(1)
    for t in range(n):
        P0.append(p); j=2*t; p=-p*(j+1)/(j+2)   # P_{j+2}(0) = -P_j(0)(j+1)/(j+2)
    out={}
    for k in ks:
        kk=k//2; x=[mp.mpf(evec[t,kk]) for t in range(n)]
        sig=mp.mpf(ev[kk])*(1+mp.mpf(10)**-12)
        chi=None
        for it in range(40):
            x=thomas(sig,x); nr=mp.sqrt(mp.fsum(a*a for a in x)); x=[a/nr for a in x]
            Tx=[diag[t]*x[t]+(off[t-1]*x[t-1] if t>0 else 0)+(off[t]*x[t+1] if t<n-1 else 0) for t in range(n)]
            chn=mp.fsum(a*b for a,b in zip(x,Tx))
            if chi is not None and abs(chn-chi)<mp.mpf(10)**(-dps+15): chi=chn; break
            chi=chn; sig=chn  # Rayleigh quotient iteration
        if x[0]<0: x=[-a for a in x]
        nf=[mp.sqrt(mp.mpf(4*t+1)/2) for t in range(n)]
        psi0=mp.fsum(x[t]*nf[t]*P0[t] for t in range(n)); psi1=mp.fsum(x[t]*nf[t] for t in range(n))
        muk=mp.sqrt(2)*x[0]/psi0; lam_k=mu*muk**2
        out[k]=dict(x=x,chi=chi,muk=muk,lam=lam_k,one_minus=1-lam_k,psi0=psi0,psi1=psi1,tail=abs(x[-1]))
    return out,c
if __name__=='__main__':
    mu=int(sys.argv[1]); o,c=prolates(mu)
    for k,v in o.items(): print(k, mp.nstr(v['chi'],20), mp.nstr(v['one_minus'],12), mp.nstr(v['psi0'],10), mp.nstr(v['psi1'],12), mp.nstr(v['tail'],3))
