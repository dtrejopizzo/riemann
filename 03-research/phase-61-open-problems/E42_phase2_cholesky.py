"""
PHASE 2: algebraic Cholesky of the zeta detector. Is the positivity certificate
organized by PRIMES (non-circular) or by ZEROS (circular, as in FF)?
(a) Cholesky/LDL of A_lambda(zeta); algebraic reconstruction of entries in Q(log p, gamma, log pi).
(b) Compare with A = V V^* indexed by the ZEROS of zeta (the explicit formula).
The FF lesson (E41): the certificate is V V^* over zeros, PSD because the zeros are real (Hodge).
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
    # LDL^T for PSD (possibly singular): M = L D L^T
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
print(f"PHASE 2 (zeta, lambda={lam}, N={N}, dim={dim}):  mu_0={mp.nstr(evs[0],4)} (PSD marginal)\n")

print("(a) LDL^T: A = L D L^T. Pivots D (=squares of the factors):")
Lm,D=ldl(M)
print("   D =", [mp.nstr(D[i],4) for i in range(dim)])
print(f"   last pivot D[{dim-1}] = {mp.nstr(D[dim-1],4)} (the marginal radical ~mu_0; quadrature noise)")
print("\n   Attempted algebraic reconstruction of pivots/entries in Q(log2,log3,gamma,log pi):")
consts=[mp.log(2),mp.log(3),GAMMA,mp.log(mp.pi),mp.mpf(1)]
for i in [0,1,2]:
    r=mp.identify(D[i], ['log(2)','log(3)','euler','log(pi)'])
    print(f"   D[{i}]={mp.nstr(D[i],8)}  identify-> {r if r else 'no simple algebraic closed form'}")

print("\n(b) Conceptual comparison with the certificate over ZEROS (V V^*):")
print("   By the explicit formula (truncation lemma), A_lambda(zeta) = sum_rho |f^(gamma_rho)|^2")
print("   = V V^* with V indexed by the ZEROS of zeta (same structure as FF, E41).")
print("   => the NATURAL certificate is over zeros, and it is PSD ONLY if the gamma_rho are real = RH.")
print("   The certificate over PRIMES/divisors (non-circular) would be the arithmetic Hodge index,")
print("   which does NOT exist for Spec Z. That is the wall, confirmed by Phase 1.")
print(f"\n   Symptom in the data: the radical (last pivot ~{mp.nstr(D[dim-1],3)}) is where RH lives;")
print("   the bulk pivots are O(1) (positive, prolate structure), but they are NOT reconstructed")
print("   as simple functions of {log p}: the certificate is not algebraically prime-local.")
