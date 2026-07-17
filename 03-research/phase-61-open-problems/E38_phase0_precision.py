"""
FASE 0.1: estabilidad de precision de mu_0(zeta).
Recomputar a dps=40,60,80 y ver si mu_0~5.8e-21 y los ratios (k+1)^2 son ESTABLES.
Si mu_0 se mueve con dps -> era ruido de cuadratura, no espectro.
Criterio: mu_0 estable a >=10 digitos significativos.
"""
import mpmath as mp

def build_and_spec(dps, lam_str='7.0', N=14):
    mp.mp.dps = dps
    GAMMA=mp.euler; LOG4PI=mp.log(4*mp.pi); C=LOG4PI+GAMMA
    lam=mp.mpf(lam_str); L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1)); mx=int(lam*lam)
    # von Mangoldt zeta
    Lam=[mp.mpf(0)]*(mx+1); sv=[True]*(mx+1)
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pw=p
            while pw<=mx: Lam[pw]=lp; pw*=p
    def q_kernel(m,n):
        if m==n: return lambda u: 2*(1-u/L)*mp.cos(2*mp.pi*n*u/L)
        c=1/(mp.pi*(n-m)); return lambda u:(mp.sin(2*mp.pi*m*u/L)-mp.sin(2*mp.pi*n*u/L))*c
    half=mp.mpf('1')/2
    def entry(m,n):
        q=q_kernel(m,n); q0=q(mp.mpf(0))
        def ig(u):
            if u<mp.mpf('1e-15'):
                h=mp.mpf('1e-10'); return ((q(h)-q0)/h+half*q0)/2
            return (mp.e**(u/2)*q(u)-q0)/(2*mp.sinh(u))
        R=C*q0/2+mp.quad(ig,[0,L])+q0*mp.log(mp.tanh(L/2))/2
        Q=mp.mpf(0)
        for k in range(2,mx+1):
            if Lam[k]!=0: Q+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
        P=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L])
        return P-R-Q
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            v=entry(idx[a],idx[b]); M[a,b]=v; M[b,a]=v
    E,_=mp.eigsy(M); E=sorted([E[i] for i in range(dim)])
    return E

print("FASE 0.1 - estabilidad de mu_0(zeta) en dps:\n")
res={}
for dps in [40,60,80]:
    E=build_and_spec(dps)
    res[dps]=E
    print(f"dps={dps}:  mu_0={mp.nstr(E[0],14)}")
    print(f"          ratios mu_k/mu_0 = {[mp.nstr(E[k]/E[0],6) for k in range(5)]}")
# comparar mu_0 entre dps
print("\nComparacion mu_0:")
mp.mp.dps=90
for dps in [40,60,80]:
    print(f"  dps={dps}: mu_0 = {mp.nstr(res[dps][0],20)}")
d46=abs(res[40][0]-res[60][0])/abs(res[60][0])
d68=abs(res[60][0]-res[80][0])/abs(res[80][0])
print(f"\n  |mu_0(40)-mu_0(60)|/mu_0 = {mp.nstr(d46,3)}")
print(f"  |mu_0(60)-mu_0(80)|/mu_0 = {mp.nstr(d68,3)}")
print(f"  VEREDICTO: {'ESTABLE (espectro real)' if d68<mp.mpf('1e-8') else 'INESTABLE (ruido de cuadratura)'}")
