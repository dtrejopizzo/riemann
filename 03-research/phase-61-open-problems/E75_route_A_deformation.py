"""
RUTA A (Connes): la perturbacion aritmetica deforma la escalera prolata LINEAL 8n+1 a la
CUADRATICA (k+1)^2. Objeto correcto (R5): no coeficiente local, sino la deformacion espectral.

Parte 1: Jacobi prolata DESNUDA W_lambda (Connes Prop 3.5, arXiv:2310.18423):
   b_n = -8n^2-2n-3/4 + 2*pi*lam^2*(8n+1)   (diagonal)
   a_n = (1/4) sqrt((4n+1)(4n+2)(4n+3)(4n+4))  (off-diagonal)
   -> verificar escalera LINEAL (normalizada 0,1,2,3,4) en modos bajos.

Parte 2: interpolar el engine QW(t) = ARCH - t*PRIME, t:0->1.
   t=0: ARCH sola (sin primos).  t=1: QW completo (k+1)^2.
   Observar ratios (eps_k-eps_0)/(eps_1-eps_0) vs t: deformacion lineal->cuadratica.
   (normalizado: lineal=0,1,2,3; cuadratico Doob k(k+2)/3=0,1,2.67,5)
"""
import numpy as np, mpmath as mp
mp.mp.dps = 40
exec(open('E70_doob_parter.py').read().split('# ---- ejecutar')[0])

def bare_prolate_ladder(lam, M=40, nlow=5):
    L2=2*mp.pi*mp.mpf(lam)**2
    b=[ -8*n*n-2*n-mp.mpf(3)/4 + L2*(8*n+1) for n in range(M)]
    a=[ mp.mpf(1)/4*mp.sqrt((4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)) for n in range(M-1)]
    J=mp.zeros(M)
    for n in range(M):
        J[n,n]=b[n]
        if n<M-1: J[n,n+1]=a[n]; J[n+1,n]=a[n]
    E,_=mp.eigsy(J); ev=sorted(float(E[i]) for i in range(M))
    base=ev[0]; gap=ev[1]-ev[0]
    norm=[(ev[k]-base)/gap for k in range(nlow)]
    return norm

def engine_interp_ladder(lam, N, ts):
    A,Larch,Lpr,L,idx=build(lam,N,'zeta'); dim=len(idx)
    out={}
    for t in ts:
        M=Larch - t*Lpr
        E,_=mp.eigsy(M); ev=sorted(float(E[i]) for i in range(dim))
        base=ev[0]; gap=ev[1]-ev[0]
        norm=[(ev[k]-base)/gap for k in range(5)]
        out[t]=(ev[0], norm)
    return out

print("="*64)
print("PARTE 1: Jacobi prolata DESNUDA W_lambda (Connes Prop 3.5) -> escalera LINEAL?")
for lam in [7.0,20.0,50.0]:
    nl=bare_prolate_ladder(lam)
    print(f"  lam={lam:>5}: normalizada(0..4) = {[round(x,3) for x in nl]}  (lineal=0,1,2,3,4 / 8n+1)")

print("\n"+"="*64)
print("PARTE 2: engine QW(t)=ARCH - t*PRIME, deformacion lineal->cuadratica")
print("  (normalizado: t=0 lineal 0,1,2,3 ; t=1 cuadratico Doob 0,1,2.67,5)")
ts=[mp.mpf(s) for s in ['0','0.5','0.9','0.99','0.999','0.9999','1.0','1.0001','1.001']]
for lam,N in [(7.0,14),(9.0,16)]:
    print(f"\n  lambda={lam} N={N}:  (transicion fina cerca de t=1 donde eps_0->0)")
    res=engine_interp_ladder(lam,N,ts)
    print(f"    {'t':>8} {'eps_0':>12}  normalizada(0..4)   [cuadr Doob: 0,1,2.67,5,8]")
    for t in ts:
        e0,norm=res[t]
        print(f"    {float(t):>8.4f} {e0:>12.3e}  {[round(x,3) for x in norm]}")
