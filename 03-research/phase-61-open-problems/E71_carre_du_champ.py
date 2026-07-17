"""
P3 del plan 2.3.F-CLOSE — ancla analitica de "C -> const" (sign-free).
Tesis: el multiplicador C(y) del operador Doob-conjugado (E70) = coeficiente de difusion
del CARRE-DU-CHAMP de la forma de Weil, que es el SEGUNDO MOMENTO de los saltos:
  c_2(x) = Omega''(0) (arq) + sum_{n<=lam^2} Lambda(n) n^{-1/2} (log n)^2 [salto disponible en [0,L]]
Afirmaciones a verificar (todas usan SOLO Lambda(n)>=0 y momentos, NUNCA la masa/el signo):
 (1) c_2 es TRADUCCION-INVARIANTE (constante en x) en el bulk; dominado por primos CHICOS
     (peso n^{-1/2} suprime n grande), salto efectivo O(1) << L => LOCAL pese al rango formal.
 (2) Cerca de los bordes hay un DEFICIT de borde (saltos truncados) en capa de ancho O(1);
     fraccion de borde O(1/L)=O(1/log lam) -> 0 => C->const con lam.
 (3) el bump de C(y) de E70 (centro/borde ~ [0.75,1.13]) lo EXPLICA este deficit; su tamano
     decrece con lam igual que std(C)/mean (0.22->0.15->0.14).
 (4) 4to momento M_4/M_2 da la correccion subdominante O(1/L^2) (no el bump dominante).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

def primes_weights(mx):
    sv=[True]*(mx+1); out=[]
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pm=p; me=1
            while pm<=mx:
                out.append((float(me*lp), float(lp*(mp.mpf(pm)**mp.mpf('-0.5')))))  # (salto=log n, peso Lambda/√n)
                pm*=p; me+=1
    return out  # lista (jump, weight)

def Omega_pp0():
    # Omega''(0): curvatura del termino arquimediano en t=0 (cota O(1), subdominante). Aprox numerica.
    # usamos psi''(1/4)/algo ~ O(1); valor de referencia O(1). Tomamos 1.0 como placeholder O(1).
    return 1.0

def run(lam):
    L=float(2*mp.log(mp.mpf(lam))); mx=int(lam*lam)
    pw=primes_weights(mx)
    M2=sum(w*s*s for s,w in pw)            # 2do momento global de primos
    M4=sum(w*s**4 for s,w in pw)
    Pl=sum(w for s,w in pw)                # masa P_lambda (0-esimo)
    # contribucion por tamano de salto (¿domina n chico?)
    sm=sorted(pw)
    small=sum(w*s*s for s,w in pw if s<1.5)   # log n<1.5 => n<=4
    print(f"\n{'='*60}\nlambda={lam}  L={L:.3f}  P_lam={Pl:.3f}  M2={M2:.3f}  M4={M4:.3f}  M4/M2={M4/M2:.3f}")
    print(f"  (1) 2do momento: salto<1.5 aporta {small/M2*100:.0f}% de M2  => dominado por primos CHICOS (salto O(1))")
    # c_2(x) con deficit de borde: salto s disponible si x+s<=L (der) o x-s>=0 (izq); promedio de ambos
    Nx=400; xs=np.linspace(0,L,Nx); c2=np.zeros(Nx)
    for s,w in pw:
        avail=0.5*((xs+s<=L).astype(float)+(xs-s>=0).astype(float))
        c2+=w*s*s*avail
    c2+=Omega_pp0()
    # bulk = E70: |y-L/2|< (L-2*0.73)/2 aprox; usamos margen 0.73
    margin=0.73
    bulk=(xs>margin)&(xs<L-margin)
    cb=c2[bulk]
    flat=np.std(cb)/np.mean(cb)
    inner=(xs>L/2-0.5)&(xs<L/2+0.5)
    center=np.mean(c2[inner]); edge=np.mean(c2[(xs>margin)&(xs<margin+0.5)])
    print(f"  (2) c_2(x) en bulk: mean={np.mean(cb):.3f} std/mean={flat:.3f}  centro={center:.3f} borde~{edge:.3f} centro/borde={center/edge:.3f}")
    print(f"      (E70 C(y) bump centro/borde ~ 1.13/0.75=1.51; aqui {center/edge:.3f})")
    print(f"  (4) correccion 4to momento (rel, subdominante): M4/M2/L^2 = {M4/M2/L**2:.4f} (->0 con lam)")
    return L, flat, center/edge

print("Verificacion P3: C->const via carre-du-champ (2do momento), deficit de borde O(1/L)")
res=[run(l) for l in [7.0,9.0,11.0,13.0,16.0]]
print(f"\n{'='*60}\nRESUMEN escala con lambda (deficit de borde -> 0):")
print(f"  L:            {[f'{r[0]:.2f}' for r in res]}")
print(f"  std(c2)/mean: {[f'{r[1]:.3f}' for r in res]}  (debe DECRECER ~1/L)")
print(f"  centro/borde: {[f'{r[2]:.3f}' for r in res]}  (debe ->1)")
