"""
INDICE CCMT: testear los 3 candidatos de 'input geometrico' en paralelo, zeta vs DH.
Buscamos una firma de Hodge-aritmetica DEFINIDA para zeta (RH) y NO para DH (no-RH).
(I)  Polarizacion-EF: involucion u->L-u = n->-n; subespacios PAR/IMPAR; firma de A en cada.
(II) Cono amplio: primos interior(p<lam) vs exterior(p>lam); firma de presupuesto - primos-ext.
(III) Positividad de traza: A con peso cosh=E (positivo) vs sin E (simbolo desnudo, indefinido).
Firma = (n_pos, n_cero, n_neg).
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
def archmat(L,N,even,C):
    dim=2*N+1; idx=list(range(-N,N+1)); half=mp.mpf('1')/2
    w=(lambda u:mp.e**(u/2)) if even else (lambda u:mp.e**(-u/2))
    A=mp.zeros(dim)
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
def polemat(L,N):
    dim=2*N+1; idx=list(range(-N,N+1)); P=mp.zeros(dim)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L)
            v=mp.quad(lambda u:q(u)*(mp.e**(u/2)+mp.e**(-u/2)),[0,L]); P[a,b]=v; P[b,a]=v
    return P
def primemat(L,N,Lam,pred):
    dim=2*N+1; idx=list(range(-N,N+1)); Q=mp.zeros(dim); mx=int(mp.e**L)
    for a in range(dim):
        for b in range(a,dim):
            q=q_kernel(idx[a],idx[b],L); s=mp.mpf(0)
            for k in range(2,mx+1):
                if Lam[k]!=0 and pred(k): s+=Lam[k]*(mp.mpf(k)**mp.mpf('-0.5'))*q(mp.log(k))
            Q[a,b]=s; Q[b,a]=s
    return Q
def sig(M):
    if M.rows==0: return (0,0,0)
    E,_=mp.eigsy(M); ev=[E[i] for i in range(M.rows)]
    p=sum(1 for e in ev if e>mp.mpf('1e-16')); n=sum(1 for e in ev if e<-mp.mpf('1e-16'))
    return (p, M.rows-p-n, n)
def restrict(M,P):  # P: dim x k columnas ortonormales; devuelve P^T M P
    return P.T*M*P
def parity_proj(N,even):
    # base ortonormal del subespacio par (V_n+V_-n) o impar (V_n-V_-n)
    idx=list(range(-N,N+1)); dim=2*N+1; cols=[]
    if even:
        v=mp.zeros(dim,1); v[N]=1; cols.append(v)  # n=0
        for n in range(1,N+1):
            v=mp.zeros(dim,1); v[N+n]=1/mp.sqrt(2); v[N-n]=1/mp.sqrt(2); cols.append(v)
    else:
        for n in range(1,N+1):
            v=mp.zeros(dim,1); v[N+n]=1/mp.sqrt(2); v[N-n]=-1/mp.sqrt(2); cols.append(v)
    Pm=mp.zeros(dim,len(cols))
    for j,c in enumerate(cols):
        for i in range(dim): Pm[i,j]=c[i]
    return Pm

def run(name,lam_str,N,kind):
    lam=mp.mpf(lam_str); L=2*mp.log(lam); mx=int(lam*lam)
    Lam=vm_zeta(mx) if kind=='zeta' else vm_DH(mx)
    even=(kind=='zeta'); C=LOG4PI+GAMMA+(0 if kind=='zeta' else LOG5)
    R=archmat(L,N,even,C); P=polemat(L,N) if kind=='zeta' else mp.zeros(2*N+1)
    Qall=primemat(L,N,Lam,lambda k:True)
    A=P-R-Qall
    lamf=float(lam)
    Qout=primemat(L,N,Lam,lambda k: k>lamf)   # primos exterior p>lambda (log p>L/2)
    Qin =primemat(L,N,Lam,lambda k: k<=lamf)
    print(f"\n=== {name} (lambda={lam_str}, N={N}) ===")
    print(f"  baseline  A = P-R-Q : firma (pos,0,neg) = {sig(A)}")
    # (I) Polarizacion EF: subespacios par/impar
    Pe=parity_proj(N,True); Po=parity_proj(N,False)
    print(f"  (I) EF  A|PAR  : {sig(restrict(A,Pe))}    A|IMPAR : {sig(restrict(A,Po))}")
    # (II) cono amplio: presupuesto - primos exterior (ample) vs interior
    print(f"  (II) ample  P-R-Q_ext : {sig(P-R-Qout)}    P-R-Q_int : {sig(P-R-Qin)}")
    # (III) traza: A con E (peso cosh, =baseline) vs sin polo/sin E equivalente: simbolo desnudo
    #   sin E: usar arch con peso 1 (no cosh) -> aprox simbolo; comparamos solo el signo de inf
    print(f"  (III) traza  A(con E/cosh) inf<0? {sig(A)[2]>0}   (E-condicion da {'POS' if sig(A)[2]==0 else 'INDEF'})")

run("ZETA",'7.0',12,'zeta')
run("DH  ",'7.0',12,'DH')
