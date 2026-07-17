"""
FASE F: gas de polimeros / LGV. Expansion (idealmente positiva) de e_k(A_lambda).

Criterio EXACTO (A simetrica real -> autovalores reales):
   A >= 0  <=>  e_k(A) >= 0  para todo k.
e_k(A) = suma de los menores principales k x k = (-1)^k * coef de t^{n-k} en det(tI-A).

Estrategia gas de polimeros: A = D - Q, D=P-R (parte 'libre', sin primos),
Q=sum_p Q_p (interaccion de primos). Encender el acoplamiento con un parametro t:
   A(t) = D - t*Q,   t:0->1.
e_k(A(t)) es polinomio en t de grado <=k. Sus coeficientes son los 'pesos' del gas:
  e_k(D - tQ) = sum_{j} (-t)^j * c_{k,j},  donde c_{k,j} mezcla menores de D y Q.
Pregunta F: para zeta, todos los e_k(1)>=0 (RH); para DH, algun e_k(1)<0.
Y: rastrear t* donde e_k cruza cero (la 'actividad critica' del gas).
"""
import mpmath as mp
mp.mp.dps = 30
GAMMA=mp.euler; LOG4PI=mp.log(4*mp.pi); LOG5=mp.log(5)

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
def vm_DH(mx):
    kap=(mp.sqrt(10-2*mp.sqrt(5))-2)/(mp.sqrt(5)-1)
    a=lambda n:[mp.mpf(0),mp.mpf(1),kap,-kap,mp.mpf(-1)][n%5]
    c=[mp.mpf(0)]*(mx+1)
    for n in range(1,mx+1):
        s=mp.log(n)*a(n); d=2
        while d<=n:
            if n%d==0: s-=a(d)*c[n//d]
            d+=1
        c[n]=s
    return c

def DandQ(lam_str,N,kind):
    lam=mp.mpf(lam_str); L=2*mp.log(lam); dim=2*N+1; idx=list(range(-N,N+1)); mx=int(lam*lam)
    Lam=vm_zeta(mx) if kind=='zeta' else vm_DH(mx)
    even=(kind=='zeta'); C=LOG4PI+GAMMA+(0 if kind=='zeta' else LOG5); half=mp.mpf('1')/2
    w=(lambda u:mp.e**(u/2)) if even else (lambda u:mp.e**(-u/2))
    D=mp.zeros(dim)   # P_pole - R_arch
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); q0=q(mp.mpf(0))
            def ig(u):
                if u<mp.mpf('1e-12'):
                    h=mp.mpf('1e-8'); return ((q(h)-q0)/h+(half if even else -half)*q0)/2
                return (w(u)*q(u)-q0)/(2*mp.sinh(u))
            R=C*q0/2+mp.quad(ig,[0,L])+q0*mp.log(mp.tanh(L/2))/2
            P=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L]) if even else mp.mpf(0)
            D[a,b]=P-R; D[b,a]=P-R
    Q=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0)
            for k in range(2,mx+1):
                if Lam[k]!=0: s+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
            Q[a,b]=s; Q[b,a]=s
    return D,Q,L

def ek_from_eigs(M):
    # e_k(M) = elementales de autovalores; via coef del polinomio caracteristico (Newton)
    E,_=mp.eigsy(M); ev=[E[i] for i in range(M.rows)]
    n=len(ev); e=[mp.mpf(1)]+[mp.mpf(0)]*n
    for lam in ev:
        for k in range(n,0,-1): e[k]=e[k]+lam*e[k-1]
    return e  # e[0]=1, e[1]=trace, ..., e[n]=det

def report(name,lam,N,kind):
    D,Q,L=DandQ(lam,N,kind); A=D-Q; n=A.rows
    e=ek_from_eigs(A)
    negs=[k for k in range(1,n+1) if e[k]<-mp.mpf('1e-12')]
    print(f"\n=== {name} (lambda={lam}, N={N}, dim={n}) ===")
    print(f"  #e_k<0 : {len(negs)}  primeros k negativos: {negs[:6]}")
    print(f"  e_1(traza)={mp.nstr(e[1],4)}  e_n(det)={mp.nstr(e[n],4)}  sign(det)={mp.sign(e[n])}")
    # actividad critica: para cada k, menor t en [0,1] donde e_k(D-tQ) cruza 0
    print(f"  t* (actividad critica) por k: encender acoplamiento D - t Q")
    ts=[mp.mpf(i)/20 for i in range(21)]
    firstcross=None
    for k in range(1,n+1):
        vals=[]
        for t in ts:
            ek=ek_from_eigs(D-t*Q)[k]; vals.append(ek)
        # buscar cruce de signo (desde + en t=0)
        tc=None
        for i in range(len(ts)-1):
            if vals[i]>0 and vals[i+1]<=0:
                tc=ts[i+1]; break
        if tc is not None and firstcross is None:
            firstcross=(k,tc)
    if firstcross:
        print(f"  PRIMER cruce e_k=0: k={firstcross[0]} en t*={mp.nstr(firstcross[1],3)} (acoplamiento<1 => rompe)")
    else:
        print(f"  NINGUN e_k cruza 0 para t in [0,1]: gas POSITIVO (todos e_k>=0) => A>=0")
    return e

report("ZETA",'7.0',10,'zeta')
report("DH  ",'7.0',10,'DH')
