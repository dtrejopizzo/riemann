"""
FASE 0.3: que cuenta kappa_lambda = #autovalores negativos.
Experimento: mover ceros on-line -> off-line (cuadruples) y contar kappa.
(i)  kappa salta exactamente +2 por cuadruple off-line DETECTABLE? (add 1,2,3 a baja altura)
(ii) altura de transicion a lambda=7 (donde kappa deja de saltar: alcance del radical)
(iii) escala la transicion con lambda?
Q_off_{nm}=int_0^L q_{nm}(u) 4 cosh(b u) cos(g0 u) du  (cuadruple off-line, conv. engine).
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
    dim=len(idx); Q=mp.zeros(dim)
    for a in range(dim):
        for bb in range(a,dim):
            q=q_kernel(idx[a],idx[bb],L)
            v=mp.quad(lambda u: q(u)*4*mp.cosh(b*u)*mp.cos(g0*u),[0,L])
            Q[a,bb]=v; Q[bb,a]=v
    return Q
def kappa(M):
    E,_=mp.eigsy(M); return sum(1 for i in range(M.rows) if E[i]<-mp.mpf('1e-18'))

bb=mp.mpf('0.2')
print("(i) kappa al agregar cuadruples off-line de baja altura (lambda=7,N=12,b=0.2):")
Mz,L,idx=zeta_engine('7.0',12)
print(f"   A_zeta solo:           kappa={kappa(Mz)}")
acc=Mz.copy()
for g0 in [mp.mpf(8),mp.mpf(14),mp.mpf(20)]:
    acc=acc+Qoff(bb,g0,L,idx)
    print(f"   + off-line en g0={int(g0)}:  kappa={kappa(acc)}")

print("\n(ii) altura de transicion a lambda=7 (un solo cuadruple, b=0.2):")
for g0 in [mp.mpf(5),mp.mpf(10),mp.mpf(20),mp.mpf(35),mp.mpf(55),mp.mpf(85)]:
    k=kappa(Mz+Qoff(bb,g0,L,idx))
    print(f"   g0={int(g0):2d}: kappa(A_zeta+Q_off)={k}  {'(detecta)' if k>0 else '(NO detecta)'}")

print("\n(iii) escala la transicion con lambda? (un cuadruple, b=0.2, g0 barrido):")
for lam,N in [('5.0',10),('7.0',12),('9.0',14)]:
    Mz2,L2,idx2=zeta_engine(lam,N)
    trans=None
    for g0 in [mp.mpf(g) for g in [5,10,15,20,25,30,40,50,65,85]]:
        if kappa(Mz2+Qoff(bb,g0,L2,idx2))==0:
            trans=int(g0); break
    print(f"   lambda={lam} (L={mp.nstr(L2,4)}, lam^4={float(lam)**4:.0f}): transicion ~ g0={trans} (primer g0 con kappa=0)")
