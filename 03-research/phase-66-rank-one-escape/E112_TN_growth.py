"""
E112 (Phase 66) — the TRUE growth rate of ||T_N|| in N: extending the loglog border.

cor:loglog-effective bounds  lambda_max(T_N) <= c0 N^2 e^{beta N}/log(|t0|/2pi)  (crude sup-norm bound
on Laguerre functions), giving contractivity only for N <= loglog|t0|/beta. If the TRUE operator-norm
growth is polynomial N^a (not exponential), the border extends to N <= (log|t0|)^{1/a} -- a real gain.

We build T_N exactly from prop:laguerre-entries and MEASURE lambda_max(T_N) vs N at fixed large t0.

  (T_N)_{jk} = -1/log(t0/2pi) * sum_n Lambda(n)/sqrt(n) [ n^{-it0} m_{jk}(log n) + n^{it0} m_{kj}(log n) ]
  m_{jk}(lam) = e^{-y lam} * INT_0^inf L_j(x+a) L_k(x) e^{-x} dx,  a = 2 y lam   (Gauss-Laguerre)

Question answered: is log lambda_max(T_N) linear in N (exponential, crude bound tight) or linear in
log N (polynomial, border extends)?
"""
import numpy as np
from numpy.polynomial.laguerre import laggauss
from scipy.special import eval_laguerre

# ---- prime powers with von Mangoldt ----
def prime_powers(X):
    sieve=np.ones(X+1,bool); sieve[:2]=False
    for i in range(2,int(X**.5)+1):
        if sieve[i]: sieve[i*i::i]=False
    out=[]
    for p in np.nonzero(sieve)[0]:
        lp=np.log(p); q=p
        while q<=X:
            out.append((q, lp)); q*=p
    return out   # (n, Lambda(n)=log p)

# ---- Gauss-Laguerre nodes for the overlap integral ----
GLx, GLw = laggauss(64)   # int_0^inf f(x) e^{-x} dx ~ sum w_i f(x_i); exact for deg <= 127

def build_TN(N, t0, y, pp):
    Nmax=N
    # precompute L_k(x_i) for k=0..N-1 at nodes
    Lx = np.array([eval_laguerre(k, GLx) for k in range(Nmax)])   # (N, nodes)
    logt=np.log(t0/(2*np.pi))
    T=np.zeros((Nmax,Nmax),dtype=complex)
    for (n,lam) in pp:
        a=2*y*np.log(n)
        # L_j(x+a) at nodes for all j
        Lxa=np.array([eval_laguerre(j, GLx+a) for j in range(Nmax)])  # (N,nodes)
        # m_{jk}(log n) = e^{-y log n} sum_i w_i L_j(x_i+a) L_k(x_i)
        M = np.exp(-y*np.log(n)) * (Lxa*GLw) @ Lx.T          # (N,N), real
        phase = n**(-1j*t0)
        w = lam/np.sqrt(n)
        T += -(w/logt)*(phase*M + np.conj(phase)*M.T)
    T=(T+T.conj().T)/2
    return T

if __name__=="__main__":
    y=1.0; t0=1.0e6
    pp=prime_powers(200000)
    print(f"t0={t0:.0e}  y={y}  #prime-powers={len(pp)}  (log(t0/2pi)={np.log(t0/(2*np.pi)):.3f})")
    print(f"{'N':>4} {'lambda_max(T_N)':>18} {'log(lmax)':>12}")
    Ns=list(range(2,51,3))
    lmax=[]
    for N in Ns:
        T=build_TN(N,t0,y,pp)
        ev=np.linalg.eigvalsh(T)
        lm=np.max(np.abs(ev))
        lmax.append(lm)
        print(f"{N:>4} {lm:>18.6e} {np.log(lm):>12.4f}")
    lmax=np.array(lmax); Ns=np.array(Ns,float)
    # fit log(lmax) ~ beta N  (exponential)  vs  log(lmax) ~ a log N (polynomial)
    b_exp=np.polyfit(Ns, np.log(lmax),1)[0]
    a_pol=np.polyfit(np.log(Ns), np.log(lmax),1)[0]
    # residuals to decide which model fits
    r_exp=np.std(np.log(lmax)-np.polyval(np.polyfit(Ns,np.log(lmax),1),Ns))
    r_pol=np.std(np.log(lmax)-np.polyval(np.polyfit(np.log(Ns),np.log(lmax),1),np.log(Ns)))
    print(f"\nEXPONENTIAL fit  log(lmax) ~ beta*N   : beta={b_exp:.4f}   resid={r_exp:.4f}")
    print(f"POLYNOMIAL  fit  log(lmax) ~ a*log(N) : a   ={a_pol:.4f}   resid={r_pol:.4f}")
    # large-N-only fit (drop the small-N transient N<10)
    mask=Ns>=10
    a_pol_L=np.polyfit(np.log(Ns[mask]),np.log(lmax[mask]),1)[0]
    b_exp_L=np.polyfit(Ns[mask],np.log(lmax[mask]),1)[0]
    print(f"  large-N (N>=10): polynomial a={a_pol_L:.3f} | exponential beta={b_exp_L:.4f}")
    print("-> smaller residual = better model. If polynomial wins, the loglog border extends to (log t0)^{1/a}.")

    # ---- t0-scaling check: does lambda_max(T_N) ~ 1/log(t0/2pi) at fixed N? ----
    print("\n=== t0-scaling at fixed N (expect lambda_max * log(t0/2pi) ~ const if whitening is 1/log) ===")
    for Nfix in [10, 16, 22]:
        print(f"  N={Nfix}:")
        prod=[]
        for t0b in [1e3, 1e4, 1e5, 1e6, 1e8]:
            ppb=prime_powers(min(int(200000), max(2000,int(50/np.log(10)*np.log(t0b))*2000)))
            Tb=build_TN(Nfix,t0b,y,pp)  # use same wide prime set pp for consistency
            lmb=np.max(np.abs(np.linalg.eigvalsh(Tb)))
            lg=np.log(t0b/(2*np.pi))
            prod.append(lmb*lg)
            print(f"     t0={t0b:.0e}  lmax={lmb:.4e}  lmax*log(t0/2pi)={lmb*lg:.4f}")
        print(f"     -> product spread: {min(prod):.3f}..{max(prod):.3f}  (flat => 1/log scaling holds)")
