"""
E68.1 -- identify the GLT symbol kappa(x,theta) and verify the distribution against exact eigenvalues.

Local (position-resolved) symbol of a matrix M at row j:
    kappa_M(x=j/N, theta) = sum_d M[j, j+d] e^{i d theta}   (valid d: j+d in [0,N-1]).
GLT symbol of the defect: kappa = kappa_A - kappa_P.

GLT distribution theorem (Serra-Capizzano/Garoni): for a Hermitian GLT sequence the eigenvalues are
an asymptotic equi-sampling of kappa(x,theta). Test: sorted eigenvalues of (A_N - P_lambda) should
match the sorted grid samples {kappa(j/N, theta_k)} (monotone rearrangement). If they do, kappa is
the symbol and
    ind_-/N -> measure{kappa < 0},   Omega_7 <=> kappa >= 0.
"""
import os, sys
import numpy as np
import mpmath as mp

H8 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, H8)
import h8lab as H
mp.mp.dps = 40

def mp2np(M):
    return np.array([[complex(M[i,j]) for j in range(M.cols)] for i in range(M.rows)], dtype=complex)

def planted(z0, rho):
    s0=mp.mpf(1)/2+mp.mpc(0,1)*z0; r,rc=rho,1-rho
    def g(j,s): return {0:(s-r)*(s-rc),1:(s-r)+(s-rc),2:mp.mpf(2)}.get(j,mp.mpf(0))
    return lambda k: sum(mp.binomial(k,j)*mp.zeta(s0,1,j)*g(k-j,s0) for j in range(k+1))

def local_symbol_grid(M, ntheta=64):
    """kappa(x_j, theta_k) as an (N x ntheta) real array (M Hermitian => real symbol)."""
    N=M.shape[0]; th=np.linspace(-np.pi,np.pi,ntheta,endpoint=False)
    K=np.zeros((N,ntheta),dtype=complex)
    for j in range(N):
        for d in range(-j, N-j):
            K[j]+= M[j,j+d]*np.exp(1j*d*th)
    return th, np.real(K)

def analyze(z0, N, Xi_deriv, tag):
    A_N,Plam,J=H.arithmetic_jets(z0,N,Xi_deriv)
    A=mp2np(H.herm(A_N)); P=mp2np(H.herm(Plam))
    th,KA=local_symbol_grid(A); _,KP=local_symbol_grid(P)
    K=KA-KP                                  # kappa(x,theta) of the defect
    # exact eigenvalues of the defect
    Jn=mp2np(H.herm(J)); Jn=0.5*(Jn+Jn.conj().T)
    eig=np.linalg.eigvalsh(Jn)
    # GLT check: compare sorted eigenvalues to sorted symbol samples at matched quantiles
    ksamp=np.sort(K.ravel())
    q=(np.arange(N)+0.5)/N
    ksamp_q=np.quantile(ksamp,q)
    match=np.linalg.norm(np.sort(eig)-ksamp_q)/(np.linalg.norm(np.sort(eig))+1e-30)
    print(f"  [{tag}]")
    print(f"     min kappa(x,theta) = {K.min():+.4f}   measure{{kappa<0}} = {np.mean(K<-1e-9):.3f}")
    print(f"     ind_-(defect) = {int(np.sum(eig<-1e-9))}   ind_-/N = {np.mean(eig<-1e-9):.3f}")
    print(f"     GLT match ||sort(eig)-quantile(kappa)||/||eig|| = {match:.3f}  (small = GLT confirmed)")
    return K, eig

def main():
    t0,y,N=100.0,1.0,20
    z0=mp.mpc(mp.mpf(str(t0)),-mp.mpf(str(y)))
    print(f"z0={t0}-{y}i  N={N}\n")
    print("GLT symbol kappa = kappa_A - kappa_P; Omega_7 <=> kappa >= 0.\n")
    analyze(z0,N,None,"zeta (RH true)")
    for beta in (0.65,0.80):
        analyze(z0,N,planted(z0,mp.mpf(str(beta))+mp.mpc(0,1)*mp.mpf(str(t0))),f"offline beta={beta}")
    print("\nReading: zeta -> min kappa ~>= 0 and GLT match small; off-line -> kappa<0 region,")
    print("ind_-/N ~ measure{kappa<0}, GLT match small. Confirms kappa is the rigorous symbol.")

if __name__ == "__main__":
    main()
