"""
FASE 0.2: control NO-CONFUNDIDO. ¿El detector es fiel a un cero off-line con
presupuesto presente? Construyo la contribucion de Weil de un CUADRUPLE off-line
{1/2+-b+i*g0, 1/2+-b-i*g0} y miro:
  (A) signatura de Q_off(b): on-line (b=0) -> PSD (Gram, >=0); off-line (b>0) ->
      INDEFINIDA (adquiere negativos). [test limpio, invariante de escala]
  (B) mu_0 de A_zeta_engine + Q_off(b): el off-line crea negativo con presupuesto?
Regimen A: g0=14 (cero bajo, "fuerte"); regimen B: g0=85 (alto, sub-dominante, el de DH).
Contribucion: A_nm = sum_{rho en quad} V~_n(rho) V~_m(1-rho),  V~_n(s)=int_0^L e^{i k_n u} e^{su} du.
"""
import mpmath as mp
mp.mp.dps = 30
GAMMA=mp.euler; LOG4PI=mp.log(4*mp.pi)

def q_kernel(m,n,L):
    if m==n: return lambda u: 2*(1-u/L)*mp.cos(2*mp.pi*n*u/L)
    c=1/(mp.pi*(n-m)); return lambda u:(mp.sin(2*mp.pi*m*u/L)-mp.sin(2*mp.pi*n*u/L))*c
def vm_zeta(mx):
    L=[mp.mpf(0)]*(mx+1); sv=[True]*(mx+1)
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pw=p
            while pw<=mx: L[pw]=lp; pw*=p
    return L
def zeta_engine(lam_str,N):
    lam=mp.mpf(lam_str); L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1)); mx=int(lam*lam)
    Lam=vm_zeta(mx); C=LOG4PI+GAMMA; half=mp.mpf('1')/2
    M=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); q0=q(mp.mpf(0))
            def ig(u):
                if u<mp.mpf('1e-12'):
                    h=mp.mpf('1e-8'); return ((q(h)-q0)/h+half*q0)/2
                return (mp.e**(u/2)*q(u)-q0)/(2*mp.sinh(u))
            R=C*q0/2+mp.quad(ig,[0,L])+q0*mp.log(mp.tanh(L/2))/2
            Q=mp.mpf(0)
            for k in range(2,mx+1):
                if Lam[k]!=0: Q+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
            P=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L])
            v=P-R-Q; M[a,b]=v; M[b,a]=v
    return M,L,idx

def Qoff(b,g0,L,idx):
    # cuadruple rho=1/2 +- b +- i g0 contribuye, en la convencion del engine (q_func):
    #   Q_off_{nm} = int_0^L q_{nm}(u) * 4 cosh(b u) cos(g0 u) du
    # (suma del cuadruple e^{(+-b +- i g0)u} = 4 cosh(bu) cos(g0 u)). b=0 -> par on-line (PSD).
    dim=len(idx); Q=mp.zeros(dim)
    for a in range(dim):
        for bb in range(a,dim):
            q=q_kernel(idx[a],idx[bb],L)
            v=mp.quad(lambda u: q(u)*4*mp.cosh(b*u)*mp.cos(g0*u),[0,L])
            Q[a,bb]=v; Q[bb,a]=v
    return Q
def sig(M):
    E,_=mp.eigsy(M); ev=sorted([E[i] for i in range(M.rows)])
    neg=sum(1 for e in ev if e<-mp.mpf('1e-20'))
    return neg, mp.nstr(ev[0],4), mp.nstr(ev[-1],4)

lam,N='7.0',12
Mz,L,idx=zeta_engine(lam,N)
ez,_=mp.eigsy(Mz); muz=min(ez[i] for i in range(Mz.rows))
print(f"lambda={lam} N={N}  A_zeta: mu_0={mp.nstr(muz,4)} (>=0)\n")

for g0lbl,g0 in [("BAJO g0=14 (fuerte)",mp.mpf(14)),("ALTO g0=85 (sub-dominante, regimen DH)",mp.mpf(85))]:
    print(f"=== {g0lbl} ===")
    for b in [mp.mpf(0),mp.mpf('0.1'),mp.mpf('0.3')]:
        Qo=Qoff(b,g0,L,idx)
        ns,mn,mx_=sig(Qo)
        # mu_0 de A_zeta + Q_off (normalizar Q_off para que no domine: escala relativa)
        At=Mz+Qo
        eat,_=mp.eigsy(At); muat=min(eat[i] for i in range(At.rows))
        print(f"  b={mp.nstr(b,3)}: Q_off signatura neg={ns} (min {mn}, max {mx_}); "
              f"mu_0(A_zeta+Q_off)={mp.nstr(muat,4)} {'<0 DETECTA' if muat<0 else '>=0'}")
    print()
