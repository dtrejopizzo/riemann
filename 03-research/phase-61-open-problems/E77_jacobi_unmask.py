"""
MECANISMO CANDIDATO (exacto, sin residuo e^{-cL}): la perturbacion aritmetica CANCELA el termino
de escala 2*pi*lam^2*(8n+1) de la Jacobi prolata de Connes (Prop 3.5), EXPONIENDO el termino
cuadratico -8n^2 preexistente -> escalera (k+1)^2.
Connes Prop 3.5:  b_n = -8n^2 - 2n - 3/4 + 2*pi*lam^2*(8n+1);  a_n = (1/4)sqrt((4n+1)..(4n+4)).
Variantes:
  (V1) full b_n: escalera LINEAL 8n+1  (control, ya verificado E75).
  (V2) b_n sin el termino de escala = -8n^2-2n-3/4 : ¿cuadratica (k+1)^2?
  (V3) b_n = -8n^2 puro : ¿cuadratica?
  (V4) interpolar: b_n = -8n^2-2n-3/4 + s*2pi lam^2 (8n+1), s:1->0 (apagar escala) -> deformacion.
Si V2/V3 da (k+1)^2: MECANISMO IDENTIFICADO (arith desenmascara -8n^2). Falta probar que el
termino de Weil = -2pi lam^2 (8n+1) sobre el near-radical (la balanza).
"""
import mpmath as mp
mp.mp.dps = 40

def jac_spec(bfun, lam, M=60, nlow=6):
    L2=2*mp.pi*mp.mpf(lam)**2
    b=[bfun(n,L2) for n in range(M)]
    a=[ mp.mpf(1)/4*mp.sqrt((4*n+1)*(4*n+2)*(4*n+3)*(4*n+4)) for n in range(M-1)]
    J=mp.zeros(M)
    for n in range(M):
        J[n,n]=b[n]
        if n<M-1: J[n,n+1]=a[n]; J[n+1,n]=a[n]
    E,_=mp.eigsy(J); ev=sorted(float(E[i]) for i in range(M))
    base=ev[0]; gap=ev[1]-ev[0]
    return [(ev[k]-base)/gap for k in range(nlow)], [ev[k] for k in range(nlow)]

variants={
 'V1 full (escala+cuadr)': lambda n,L2: -8*n*n-2*n-mp.mpf(3)/4 + L2*(8*n+1),
 'V2 sin escala (-8n^2-2n-3/4)': lambda n,L2: -8*n*n-2*n-mp.mpf(3)/4,
 'V3 -8n^2 puro': lambda n,L2: -8*n*n,
 'V3b -8n^2-2n': lambda n,L2: -8*n*n-2*n,
}
print("target (k+1)^2 normalizado k(k+2)/(gap): 0,1,2.667,5,8,11.667  ; lineal 8n+1: 0,1,2,3,4,5\n")
for name,bf in variants.items():
    for lam in [7.0,20.0]:
        nl,_=jac_spec(bf,lam)
        print(f"  {name:>30} lam={lam:>4}: {[round(x,3) for x in nl]}")
    print()

print("V4 interpolacion: apagar escala s:1->0 (b_n=-8n^2-2n-3/4 + s*L2*(8n+1)):")
for s in [mp.mpf(x) for x in ['1.0','0.5','0.1','0.01','0.0']]:
    bf=lambda n,L2,s=s: -8*n*n-2*n-mp.mpf(3)/4 + s*L2*(8*n+1)
    nl,_=jac_spec(bf,20.0)
    print(f"  s={float(s):>5.2f}: {[round(x,3) for x in nl]}")
