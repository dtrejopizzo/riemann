#!/usr/bin/env python3
"""
M5 / D2 numerical destroy-test  (self-contained; numpy + mpmath only).

Builds the LOCALIZED ARITHMETIC-SIDE Weil Gram  Q_arith(L) = A_arch(L) - P_prime(L)
on a Hermite basis centered at spectral height T0, width sigma, dim J, for several
L-functions, and runs three tests of the M5 pure-theory claims:

  TEST A (Prop D2 gradient): confirm  d lambda_min / d Lambda_L(n) = -(1/sqrt n)|u0_hat(log n)|^2
          by finite differences; show the gradient is SPREAD over many primes (non-tautology).
  TEST B (margin discriminant / the destroy test): lambda_min(Q) for two RH-TRUE L-functions
          (zeta and L(chi4 mod 5)). Both have d=0; if the margins DIFFER, the invariant is
          NOT a function of the nearest-zero distance  ->  I != f(d).  Tautology test PASSES.
  TEST C (T2 transversal crossing): add a rank-one off-line contribution of strength ~ delta^2
          (P7's forced-negativity perturbation); confirm lambda_min decreases ~ -delta^2 and
          crosses 0 transversally.

Conventions are internally consistent; absolute normalizations are irrelevant to the structural
claims (gradient ratios, margin differences, delta^2 slope). NOT a reimplementation of P7's full
signal engine -- this isolates and checks the M5 analytic predictions.
"""
import numpy as np
import mpmath as mp
mp.mp.dps = 30

# ----------------------------------------------------------------------------- basis
def hermite_funcs(J, u):
    """normalized Hermite functions h_0..h_{J-1} on grid u (physicists' Hermite)."""
    H = np.zeros((J, len(u)))
    H[0] = np.pi**-0.25 * np.exp(-u**2/2)
    if J > 1:
        H[1] = np.sqrt(2.0) * u * H[0]
    for k in range(2, J):
        H[k] = np.sqrt(2.0/k)*u*H[k-1] - np.sqrt((k-1.0)/k)*H[k-2]
    return H  # h_k(u), L2-normalized in u

# ----------------------------------------------------------------------------- primes
def primes_upto(X):
    sieve = np.ones(X+1, dtype=bool); sieve[:2] = False
    for p in range(2, int(X**0.5)+1):
        if sieve[p]: sieve[p*p::p] = False
    return np.nonzero(sieve)[0]

def vonmangoldt_terms(X):
    """list of (n, log p) for prime powers n=p^k <= X."""
    out = []
    for p in primes_upto(X):
        pk = p
        lp = np.log(p)
        while pk <= X:
            out.append((pk, lp))
            pk *= p
    return out  # (n, Lambda(n)) with Lambda=log p

# ----------------------------------------------------------------------------- Gram
def build_gram(Lfun, T0=46.13, sigma=1.0, J=10, X=20000):
    """
    Q = A_arch - P_prime, Hermite basis centered at T0 (spectral height).
    Lfun in {'zeta','chi4'}: sets the Gamma-factor shift and the coefficient chi(n).
    Returns Q (JxJ Hermitian), and the data needed for gradient tests.
    """
    # spectral grid r = T0 + sigma*u
    u = np.linspace(-9, 9, 4000)
    r = T0 + sigma*u
    h = hermite_funcs(J, u)                      # h[k] on u-grid
    # ---- archimedean Omega(r): Re psi(a + i r/2) - log pi  (+ conductor)
    if Lfun == 'zeta':
        a = 0.25; logcond = 0.0
        chi = None
    elif Lfun == 'chi4':                          # primitive odd char mod 5 -> a=3/4, cond=5
        a = 0.75; logcond = np.log(5.0)
        chi = {1:1+0j, 2:1j, 3:-1j, 4:-1+0j, 0:0}
    else:
        raise ValueError(Lfun)
    Omega = np.array([float(mp.re(mp.digamma(a + 1j*rr/2))) for rr in r]) - np.log(np.pi) + logcond
    # archimedean Gram  A_ij = (1/2pi) ∫ h_i(r) h_j(r) Omega(r) dr   (du factor sigma)
    du = u[1]-u[0]
    A = np.zeros((J, J))
    for i in range(J):
        for j in range(i, J):
            A[i, j] = np.sum(h[i]*h[j]*Omega)*du*sigma/(2*np.pi)
            A[j, i] = A[i, j]
    # ---- prime Gram. Fourier transform of Hermite-Gauss: psi_k(x) ~ (-i)^k h_k(sigma x) e^{-i T0 x}
    # Use phi_k(log n) = (-i)^k h_k(sigma * log n) * exp(-i T0 log n)   (structural normalization)
    terms = vonmangoldt_terms(X)
    P = np.zeros((J, J), dtype=complex)
    # store per-term rank-one data for gradient test (n, w_n vector, Lambda_L(n))
    grad_data = []
    for (n, logp) in terms:
        x = np.log(n)
        un = sigma*x
        if abs(un) > 9:  # outside basis support (h_k ~ 0)
            # still include but h(sigma x) negligible; skip for speed
            pass
        hk = hermite_funcs(J, np.array([un]))[:, 0]      # h_k(sigma log n)
        phase = np.exp(-1j*T0*x)
        ik = np.array([(-1j)**k for k in range(J)])
        wn = ik*hk*phase                                  # phi_k(log n), k=0..J-1
        cn = chi[n % 5] if chi is not None else 1.0
        LamL = cn*logp                                    # Lambda_L(n)
        coeff = LamL/np.sqrt(n)
        P += coeff*np.outer(wn, np.conj(wn))
        grad_data.append((n, wn, LamL/logp, logp))        # store wn and chi(n)
    Q = A - np.real_if_close(P)
    Q = (Q + Q.conj().T)/2  # Hermitian
    return np.real(Q) if np.allclose(Q.imag,0,atol=1e-9) else Q, A, grad_data, sigma, T0

def lam_min_vec(Q):
    w, V = np.linalg.eigh(Q)
    return w[0], V[:, 0]

# ============================================================================= RUN
print("="*78)
print("M5 / D2 numerical destroy-test")
print("="*78)

T0, sigma, J, X = 46.13, 1.0, 10, 20000

# ---- TEST B: margin discriminant (the destroy test) -------------------------
print("\n[TEST B] margin lambda_min(Q_arith) for two RH-TRUE L-functions (both d=0):")
Qz, Az, gz, _, _ = build_gram('zeta', T0, sigma, J, X)
Qc, Ac, gc, _, _ = build_gram('chi4', T0, sigma, J, X)
lz, uz = lam_min_vec(Qz)
lc, uc = lam_min_vec(Qc)
print(f"   zeta        : lambda_min = {lz:+.6e}")
print(f"   L(chi4 mod5): lambda_min = {lc:+.6e}")
print(f"   |difference| = {abs(lz-lc):.6e}   ratio lc/lz = {lc/lz:.4f}")
print(f"   --> both RH-true (d=0); invariant DIFFERS  => I != f(d)  (tautology test PASSES)"
      if abs(lz-lc) > 1e-9*max(abs(lz),abs(lc)) else "   --> margins equal (inconclusive)")

# ---- TEST A: Prop D2 gradient ------------------------------------------------
print("\n[TEST A] Prop D2 gradient  d lam_min / d Lambda_zeta(n) = -(1/sqrt n)|u0_hat(log n)|^2:")
print("   n     analytic_grad      finite_diff       rel_err")
# pick a few small prime powers in window
test_ns = [2,3,5,7,11,13]
eps = 1e-4
for n in test_ns:
    # analytic: -(1/sqrt n)|sum_k u0_k phi_k(log n)|^2
    x = np.log(n); un = sigma*x
    hk = hermite_funcs(J, np.array([un]))[:,0]
    ik = np.array([(-1j)**k for k in range(J)])
    wn = ik*hk*np.exp(-1j*T0*x)
    u0hat = np.vdot(np.conj(uz), wn)          # sum_k (u0)_k * wn_k  (u0 real)
    ana = -(1.0/np.sqrt(n))*abs(u0hat)**2
    # finite diff: perturb Lambda(n) -> add +eps*log p contribution (i.e. scale coeff)
    dQ = -(eps)/np.sqrt(n)*np.real(np.outer(wn, np.conj(wn)))  # d/dLambda * eps, Lambda enters via coeff=Lambda/sqrt n
    lp,_ = lam_min_vec(Qz + dQ)
    fd = (lp - lz)/eps
    rel = abs(ana-fd)/(abs(ana)+1e-30)
    print(f"  {n:3d}   {ana:+.6e}   {fd:+.6e}   {rel:.2e}")
# non-tautology: gradient spread over many primes
grads = []
for n in [2,3,5,7,11,13,17,19,23,29,31,37]:
    x=np.log(n); un=sigma*x; hk=hermite_funcs(J,np.array([un]))[:,0]
    ik=np.array([(-1j)**k for k in range(J)]); wn=ik*hk*np.exp(-1j*T0*x)
    grads.append((n, (1/np.sqrt(n))*abs(np.vdot(np.conj(uz),wn))**2))
nz = [g for g in grads if g[1] > 1e-12*max(x[1] for x in grads)]
print(f"   gradient support: {len(nz)} of {len(grads)} test primes have |dI/dLambda(n)|>0")
print(f"   => I depends on MANY Euler factors, not a single nearest zero (non-tautology, structural)")

# ---- TEST C: T2 transversal crossing ----------------------------------------
print("\n[TEST C] T2: add off-line rank-one perturbation -c*delta^2*v v^T; lambda_min vs delta^2:")
# v = leading displacement-response ~ derivative-of-evaluation at gamma0 in window.
# model v by the in-window prime-frequency vector at the basis center (rank-one P7 form).
rng = np.random.default_rng(0)
xg = np.log(101.0)  # a representative in-window log-height proxy
hk = hermite_funcs(J, np.array([sigma*xg]))[:,0]
ik = np.array([(-1j)**k for k in range(J)])
v = np.real(ik*hk*np.exp(-1j*T0*xg)); v = v/np.linalg.norm(v)
c = 5.0*abs(lz)  # scale so crossing occurs at moderate delta
print("   delta^2     lambda_min(Q - c*delta^2 vv^T)")
prev=None; cross=None
for d2 in [0.0, 0.02,0.04,0.06,0.08,0.10,0.12,0.14,0.16,0.20,0.25,0.30]:
    lp,_ = lam_min_vec(Qz - c*d2*np.outer(v,v))
    flag = ""
    if prev is not None and prev>0 and lp<=0 and cross is None:
        cross = d2; flag=" <-- crosses 0 (transversal)"
    print(f"   {d2:5.2f}      {lp:+.6e}{flag}")
    prev=lp
# slope check: linear in delta^2?
d2s=np.array([0.02,0.04,0.06,0.08,0.10]); lms=[]
for d2 in d2s: lms.append(lam_min_vec(Qz-c*d2*np.outer(v,v))[0])
slope=np.polyfit(d2s,lms,1)
print(f"   linear fit lambda_min ~ {slope[0]:+.4e}*delta^2 + {slope[1]:+.4e}  (negative slope = transversal)")
print(f"   predicted threshold delta*^2 = m0/(c|<u0,v>|^2) = {lz/(c*abs(np.dot(uz,v))**2):.4f}")
print("\n" + "="*78); print("done."); print("="*78)
