# TOOLS_204U_001: cota superior de n_-(m_T) via minorante escalon de m + conteo prolato (Landau 1993; Karnik-Romberg-Davenport 2021). Constantes NUMERICAS.
import mpmath as mp
mp.mp.dps=30
m=lambda t: mp.re(mp.digamma(mp.mpf(1)/4+1j*t/2))-mp.log(mp.pi)
t0=mp.findroot(m,6.29); C0=m(0)
print('t0',t0,'C0',C0)
for T in [0.5493,1,2,3,5,10,30,100,1000]:
    T=mp.mpf(T); h=1/T; t1=t0+h; mu=m(t1); d=mu/(mu-C0); c=T*t1
    plunge=2/mp.pi**2*mp.log(50*c/mp.pi+25)*mp.log(5/(d*(1-d)))+7
    lead=mp.ceil(2*c/mp.pi); base=mp.ceil(2*T*t0/mp.pi)
    print(float(T),'mu',mp.nstr(mu,4),'delta',mp.nstr(d,4),'ceil(2c/pi)',int(lead),'ceil(2Tt0/pi)',int(base),'bound',int(lead+mp.floor(plunge)),'excess',int(lead+mp.floor(plunge)-base))
# minimo del simbolo de B_P
for P in ([2],[2,3]):
    g=lambda tau: sum(2*mp.log(p)*mp.re(p**(-0.5-1j*tau)/(1-p**(-0.5-1j*tau))) for p in P)
    print(P,'gmin_bound',sum(-2*mp.log(p)*p**-0.5/(1+p**-0.5) for p in P),'gmax',sum(2*mp.log(p)*p**-0.5/(1-p**-0.5) for p in P))
