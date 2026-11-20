import mpmath as mp
mp.mp.dps=20
# smooth cutoff g(x)=bump on [1,K]
def g(x,K):
    if x<=1 or x>=K: return mp.mpf(0)
    t=(x-1)/(K-1); return mp.e**(-1/(t*(1-t)))
K=40; 
for fac in [1.2,1.6]:
    tau=2*mp.pi*K*fac; s=mp.mpf(0.5)+1j*tau
    S=mp.fsum(mp.log(k)*g(k,K)*k**(-s) for k in range(2,K))
    chi=mp.pi**(s-0.5)*mp.gamma((1-s)/2)/mp.gamma(s/2)
    D=0
    for j in range(1,int(tau)+1):
        x=tau/(2*mp.pi*j)
        if 1<x<K:
            # stationary phase of sum_j int log x g x^{-s} e(jx): leading term
            D+= chi*j**(s-1)*mp.log(x)*g(x,K)
    print(fac, mp.nstr(S,8), mp.nstr(D,8), mp.nstr(abs(S-D)/abs(S),3))
