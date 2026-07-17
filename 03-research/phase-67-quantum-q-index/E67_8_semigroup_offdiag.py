"""
E67.8 -- semigroup-isometry off-diagonal test.

Question
--------
Does the multiplicative-semigroup (Cuntz N^x) coherent state reproduce the
off-diagonal *coherence* of the exact P52 whitened prime operator?

  s_n : dilation isometries, s_m s_n = s_{mn}, s_p^* s_p = 1.
  Coherent Mellin vector xi = sum_m w_m delta_m,  w_m = m^{-alpha} e^{-i t0 log m}.
  Then  omega(s_a^* s_b) = <s_a xi, s_b xi>
       = (a' b')^{-alpha} (b'/a')^{i t0} * zeta(2 alpha),
    with g=gcd(a,b), a'=a/g, b'=b/g.
  Normalized:  rho_mod[a,b] = (g^2/(a b))^{alpha} * (b/a)^{i t0}.   (zeta-free after norm)

Exact P52 side
--------------
Per-integer prime jet from h_P(z)=i*Lambda(n)*n^{-s}. Whitened contribution
  t_a = W * pick_jet(h_{P,a}) * W,  W = A_N^{-1/2}   (raw, no herm: keep phase).
  rho_exact[a,b] = <t_a, t_b>_F / (||t_a||_F ||t_b||_F).

Decision
--------
 - If rho_mod (divisibility-driven) matches rho_exact (archimedean-driven) on the
   off-diagonal, the semigroup coherence IS the coherence of P_lambda -> route alive.
 - If they disagree (esp. magnitude: gcd jumps vs smooth log-distance), the
   divisibility coherence is the WRONG coherence -> folds back to Mellin/Omega_7.
"""
import os, sys, math, itertools
import numpy as np
import mpmath as mp

H8 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, H8)
import h8lab as H

mp.mp.dps = 50

def vonmangoldt(n):
    # Lambda(n)=log p if n=p^k else 0
    m = n; p = 2; res = 0.0; base = None; ok = True
    f = {}
    d = 2
    x = n
    while d*d <= x:
        while x % d == 0:
            f[d] = f.get(d,0)+1; x//=d
        d += 1
    if x > 1:
        f[x] = f.get(x,0)+1
    if len(f) == 1:
        p = list(f.keys())[0]
        return math.log(p)
    return 0.0

def hP_n_taylor(z0, M, n):
    """Taylor coeffs (order 0..M) of h_{P,n}(z) = i * Lambda(n) * n^{-s}, s=1/2+iz.
       Matches hP_taylor convention: coeff order p = i^{p+1} * g_p,
       g(s)=Lambda(n) n^{-s}, g_p = Lambda(n)(-log n)^p n^{-s0}/p!."""
    s0 = mp.mpf(1)/2 + mp.mpc(0,1)*z0
    Lam = mp.mpf(vonmangoldt(n))
    if Lam == 0:
        return [mp.mpc(0)]*(M+1)
    logn = mp.log(n)
    nms0 = mp.e**(-s0*logn)
    out = []
    for p in range(M+1):
        g_p = Lam*((-logn)**p)*nms0/mp.factorial(p)
        out.append((mp.mpc(0,1)**(p+1))*g_p)
    return out

def mp2np(Mx):
    return np.array([[complex(Mx[i,j]) for j in range(Mx.cols)] for i in range(Mx.rows)], dtype=complex)

def run(t0=100.0, y=1.0, N=6, cutoff=33):
    z0 = mp.mpc(mp.mpf(str(t0)), -mp.mpf(str(y)))
    M = 2*N+2
    A_N = H.herm(H.pick_jet(H.hA_taylor(z0, M), z0, N))
    W = H.inv_sqrt(A_N)                      # A_N^{-1/2}
    Wn = mp2np(W)

    labels = [n for n in range(2, cutoff+1) if vonmangoldt(n) > 0]
    # exact whitened per-integer contribution (raw pick jet, keep phase)
    T = {}
    for a in labels:
        Pa = H.pick_jet(hP_n_taylor(z0, M, a), z0, N)
        ta = Wn @ mp2np(Pa) @ Wn
        T[a] = ta
    def fro(x,yv): return np.vdot(x.ravel(), yv.ravel())
    rho_ex = {}
    for a in labels:
        for b in labels:
            na = math.sqrt(abs(fro(T[a],T[a]).real)); nb = math.sqrt(abs(fro(T[b],T[b]).real))
            rho_ex[(a,b)] = fro(T[a],T[b])/(na*nb)

    def gcd(a,b):
        while b: a,b=b,a%b
        return a
    def rho_mod(a,b, alpha, sgn):
        g = gcd(a,b)
        mag = (g*g/(a*b))**alpha
        ph = math.exp(sgn*t0*(math.log(b)-math.log(a)))  # placeholder; complex below
        return mag*complex(math.cos(t0*(math.log(b)-math.log(a))), sgn*math.sin(t0*(math.log(b)-math.log(a))))

    # off-diagonal index set
    offpairs = [(a,b) for a in labels for b in labels if a<b]
    ex_vec = np.array([rho_ex[(a,b)] for (a,b) in offpairs])

    # optimize alpha and sign to match magnitudes+phase (complex Frobenius)
    best = None
    for sgn in (+1,-1):
        for alpha in np.linspace(0.05, 3.0, 120):
            mod_vec = np.array([rho_mod(a,b,alpha,sgn) for (a,b) in offpairs])
            # complex relative error
            err = np.linalg.norm(mod_vec-ex_vec)/np.linalg.norm(ex_vec)
            # separate magnitude-only error (phase-agnostic)
            magerr = np.linalg.norm(np.abs(mod_vec)-np.abs(ex_vec))/np.linalg.norm(np.abs(ex_vec))
            if best is None or err < best[0]:
                best = (err, magerr, alpha, sgn)
    # phase agreement: correlation of phases on pairs where |ex| not tiny
    # measure how well arg(ex) tracks t0*(log b-log a)
    ph_pred = np.array([t0*(math.log(b)-math.log(a)) for (a,b) in offpairs])
    ph_ex = np.angle(ex_vec)
    ph_pred_wrapped = np.angle(np.exp(1j*best[3]*ph_pred))
    phase_match = np.mean(np.cos(ph_ex - best[3]*ph_pred))  # 1 => perfect

    print(f"t0={t0} y={y} N={N} cutoff={cutoff}  #labels={len(labels)}  #offpairs={len(offpairs)}")
    print(f"labels = {labels}")
    print(f"best complex offdiag_error = {best[0]:.4f}   (alpha={best[2]:.3f}, sign={best[3]:+d})")
    print(f"magnitude-only offdiag_error = {best[1]:.4f}")
    print(f"phase tracking <cos(arg_ex - sign*t0*dlog)> = {phase_match:.4f}   (1=perfect, 0=random)")
    print()
    # diagnostic: divisibility vs log-distance for a few illustrative pairs
    print("pair   gcd  dlog=logb-loga   |rho_exact|   |rho_mod(alpha*)|")
    ill = [(2,4),(4,8),(4,9),(8,16),(3,9),(4,5),(2,3),(9,27),(16,32),(5,25),(2,32),(3,27)]
    ill = [(a,b) for (a,b) in ill if a in labels and b in labels]
    for (a,b) in ill:
        g=gcd(a,b); dl=math.log(b)-math.log(a)
        me = abs(rho_ex[(a,b)]); mm = abs(rho_mod(a,b,best[2],best[3]))
        print(f"({a:2d},{b:2d})  {g:3d}   {dl:8.4f}     {me:9.4f}     {mm:9.4f}")

if __name__ == "__main__":
    run()
