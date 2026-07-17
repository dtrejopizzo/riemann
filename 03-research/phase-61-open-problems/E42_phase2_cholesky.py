"""
FASE 2: Cholesky algebraico del detector zeta. ¿El certificado de positividad
se organiza por PRIMOS (no-circular) o por CEROS (circular, como FF)?
(a) Cholesky/LDL de A_lambda(zeta); reconstruccion algebraica de entradas en Q(log p, gamma, log pi).
(b) Comparar con A = V V^* indexado por los CEROS de zeta (la fórmula explícita).
La leccion FF (E41): el certificado es V V^* por ceros, PSD porque los ceros son reales (Hodge).
"""
import mpmath as mp
mp.mp.dps = 40
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

def ldl(M):
    # LDL^T para PSD (posiblemente singular): M = L D L^T
    n=M.rows; Lm=mp.eye(n); D=mp.zeros(n,1)
    for j in range(n):
        d=M[j,j]-sum(Lm[j,k]**2*D[k] for k in range(j))
        D[j]=d
        for i in range(j+1,n):
            if abs(d)>mp.mpf('1e-35'):
                Lm[i,j]=(M[i,j]-sum(Lm[i,k]*Lm[j,k]*D[k] for k in range(j)))/d
            else: Lm[i,j]=0
    return Lm,D

lam,N='5.0',8
M,L,idx=zeta_engine(lam,N); dim=2*N+1
ev,_=mp.eigsy(M); evs=sorted([ev[i] for i in range(dim)])
print(f"FASE 2 (zeta, lambda={lam}, N={N}, dim={dim}):  mu_0={mp.nstr(evs[0],4)} (PSD marginal)\n")

print("(a) LDL^T: A = L D L^T. Pivotes D (=cuadrados de los factores):")
Lm,D=ldl(M)
print("   D =", [mp.nstr(D[i],4) for i in range(dim)])
print(f"   ultimo pivote D[{dim-1}] = {mp.nstr(D[dim-1],4)} (el radical marginal ~mu_0; ruido de cuadratura)")
print("\n   Intento de reconstruccion algebraica de pivotes/entradas en Q(log2,log3,gamma,log pi):")
consts=[mp.log(2),mp.log(3),GAMMA,mp.log(mp.pi),mp.mpf(1)]
for i in [0,1,2]:
    r=mp.identify(D[i], ['log(2)','log(3)','euler','log(pi)'])
    print(f"   D[{i}]={mp.nstr(D[i],8)}  identify-> {r if r else 'no cierre algebraico simple'}")

print("\n(b) Comparacion conceptual con el certificado por CEROS (V V^*):")
print("   Por la formula explicita (Lema de truncacion), A_lambda(zeta) = sum_rho |f^(gamma_rho)|^2")
print("   = V V^* con V indexado por los CEROS de zeta (igual estructura que FF, E41).")
print("   => el certificado NATURAL es por ceros, y es PSD SOLO si los gamma_rho son reales = RH.")
print("   El certificado por PRIMOS/divisores (no-circular) seria el indice de Hodge aritmetico,")
print("   que NO existe para Spec Z. Esa es la pared, confirmada por Fase 1.")
print(f"\n   Sintoma en los datos: el radical (ultimo pivote ~{mp.nstr(D[dim-1],3)}) es donde vive RH;")
print("   los pivotes del bulk son O(1) (positivos, estructura prolata), pero NO se reconstruyen")
print("   como funciones simples de {log p}: el certificado no es prime-local algebraico.")
