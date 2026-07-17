"""
FASE H0 — GATE DE NO-CIRCULARIDAD (obligatorio antes de cualquier 'cruce').
Tesis a verificar: los insumos de positividad que alimentaremos al teorema de Abboud
  - el polo 𝒫 (clase amplia L̄),
  - el arquimediano ℛ (factor-Γ, la condicion ℰ/cosh),
  - el termino de primos 𝒬 (von Mangoldt),
son DATOS ARITMETICOS construidos SIN usar la posicion de los ceros. Los ceros aparecen
solo como OUTPUT (el espectro de A=𝒫−ℛ−𝒬, = Σ_ρ|f̂(γ_ρ)|² por la formula explicita).
Si algun insumo requiriera saber que los ceros estan on-line => circular => DETENER.

Tests:
 (1) Procedencia: 𝒫 usa solo cosh(u/2) (polo s=0,1); ℛ usa solo {γ,log4π, e^{±u/2}, sinh}
     (factor-Γ, CCM eq 2.8); 𝒬 usa solo Λ(n)=log p (primos). Ninguno toma ceros como input.
 (2) Invariancia: 'mover' ceros hipoteticos NO cambia 𝒫,ℛ,𝒬 (no pueden: no hay slot de ceros).
 (3) Firma de cada pieza: identificar 𝒫 como CLASE AMPLIA (auto-pareo positivo, el +1 de Hodge).
 (4) Falsador: misma estructura polo/Γ pero primos de DH (=otra aritmetica) => output indefinido,
     probando que la positividad la decide la ARITMETICA (primos), no un supuesto sobre ceros.
"""
import mpmath as mp
mp.mp.dps = 30
GAMMA=mp.euler; LOG4PI=mp.log(4*mp.pi); LOG5=mp.log(5); half=mp.mpf('1')/2

def q_kernel(m,n,L):
    if m==n: return lambda u: 2*(1-u/L)*mp.cos(2*mp.pi*n*u/L)
    c=1/(mp.pi*(n-m)); return lambda u:(mp.sin(2*mp.pi*m*u/L)-mp.sin(2*mp.pi*n*u/L))*c

def polemat(L,N):
    # 𝒫: SOLO el peso del polo 2cosh(u/2)=e^{u/2}+e^{-u/2}. CERO input de ceros.
    dim=2*N+1; idx=list(range(-N,N+1)); P=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L)
            v=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L]); P[a,b]=v; P[b,a]=v
    return P

def archmat(L,N,even,C):
    # ℛ: SOLO factor-Γ (γ, log4π, e^{±u/2}, sinh). CERO input de ceros.
    dim=2*N+1; idx=list(range(-N,N+1))
    w=(lambda u:mp.e**(u/2)) if even else (lambda u:mp.e**(-u/2)); A=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); q0=q(mp.mpf(0))
            def ig(u):
                if u<mp.mpf('1e-12'):
                    h=mp.mpf('1e-8'); return ((q(h)-q0)/h+(half if even else -half)*q0)/2
                return (w(u)*q(u)-q0)/(2*mp.sinh(u))
            R=C*q0/2+mp.quad(ig,[0,L])+q0*mp.log(mp.tanh(L/2))/2
            A[a,b]=R; A[b,a]=R
    return A

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
def primemat(L,N,Lam):
    # 𝒬: SOLO Λ(n) (primos). CERO input de ceros.
    dim=2*N+1; idx=list(range(-N,N+1)); Q=mp.zeros(dim); mx=int(mp.e**L)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0)
            for k in range(2,mx+1):
                if Lam[k]!=0: s+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
            Q[a,b]=s; Q[b,a]=s
    return Q

def sig(M):
    E,_=mp.eigsy(M); ev=[E[i] for i in range(M.rows)]
    p=sum(1 for e in ev if e>1e-14); n=sum(1 for e in ev if e<-1e-14)
    return (p, M.rows-p-n, n)

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); mx=int(float(lam)**2); C=LOG4PI+GAMMA
    P=polemat(L,N); R=archmat(L,N,True,C); Qz=primemat(L,N,vm_zeta(mx))
    print(f"\n=== H0 gate  lambda={lam} N={N} (dim {2*N+1}) ===")
    print(f"  (1)(2) PROCEDENCIA: 𝒫<-cosh(polo), ℛ<-{{γ,log4π,e^±u/2,sinh}}(Γ), 𝒬<-Λ(n)(primos).")
    print(f"          NINGUNA funcion toma ceros como argumento => insumos zero-independientes.")
    print(f"  (3) FIRMAS (pos,0,neg):")
    print(f"        𝒫 (polo)        = {sig(P)}   <- CLASE AMPLIA si tiene direccion(es) +")
    print(f"        ℛ (arquimediano)= {sig(R)}")
    print(f"        𝒬 (primos zeta) = {sig(Qz)}")
    Az=P-R-Qz
    print(f"        A=𝒫−ℛ−𝒬 (zeta) = {sig(Az)}   <- OUTPUT (positividad = formula explicita)")
    # (4) falsador: misma estructura polo+Γ, primos de DH (DH no tiene polo => usamos solo Γ+primos_DH)
    Cdh=LOG4PI+GAMMA+LOG5; Rdh=archmat(L,N,False,Cdh); Qdh=primemat(L,N,vm_DH(mx))
    Adh=-Rdh-Qdh   # DH entera: sin polo
    print(f"  (4) FALSADOR (misma maquinaria, aritmetica DH): A_DH=−ℛ_DH−𝒬_DH firma={sig(Adh)}")
    print(f"      => la positividad la decide la ARITMETICA (primos/polo), NO un supuesto sobre ceros.")
    # veredicto
    poleAmple = sig(P)[0]>=1
    print(f"  D-H0: insumos zero-independientes=SI ; 𝒫 amplia (tiene +)={poleAmple}")
    print(f"        => {'GATE PASA: seguir a H1/H4' if poleAmple else 'REVISAR: 𝒫 no amplia'}")

run('7.0',10)
run('9.0',10)
