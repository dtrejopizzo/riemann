"""Phase 155 round 2, task (c): explicit a priori bound ||beta||_inf <= B(T) for every
dual certificate (Paper 47, Def. 3.1) of value c.

Construction (Lemma W route, Paper 47 Lemma 6.1).  Take F in the span of the polynomial
witnesses psi_k(t) = (T^2-t^2) t^k on I_T (so F in H^1_0(I_T), F extended by 0 lies in
H^1(R)).  Then mu_F = |Fhat|^2 dtau/2pi is an even probability measure with
check-mu_F = c_F supported in [-2T,2T]: it is feasible for the relaxation of (P) with the
two moment constraints dropped, so int nuh d mu_F = 0 for every certificate measure nu.
Its moment vector is w(F) = (Q0,Q1) = (AB, A'B-AB') and its value is
   int sigma_T d mu_F = a_T(F) <= C0 + A_T + int_0^inf (1-c_F(u)) K(u) du
                              <= C0 + A_T + [ (L^2/2) int_0^{u0} u^2 K + 2 int_{u0}^inf K ]_{u0 = 2/L}  (the exact minimiser)
with L = ||F'||/||F||, using 1-c_F(u) <= min(2, u^2 L^2/2).

Pairing f = sigma_T + nuh + beta.ghat >= c against mu_F gives  beta.w(F) >= c - V(F).
The moment image of the relaxed feasible set is convex (mixtures), so if the polygon
conv{w_1,...,w_N} contains the disc of radius r0 about 0 and all V_i <= V*, then
   beta.w >= c - V*  for all |w| <= r0,  i.e.  |beta| <= (V* - c)/r0   (Euclidean),
and in particular ||beta||_inf <= (V* - c)/r0.

Output: r0, V*, B for c >= 0 and c >= -1, at T = (1/2)log3 and T = 0.58.
"""
import json
import numpy as np
from scipy.linalg import eigh
from mpmath import mp, mpf, quad, exp, cosh, sinh, log, pi, atan, coth, digamma, sqrt

mp.dps = 30
KDIM = 4
NDIR = 48


def setup(T):
    T = mpf(T)
    psi = [(lambda t, k=k: (T*T - t*t) * t**k) for k in range(KDIM)]
    dps = [(lambda t, k=k: -2*t*t**k + (T*T - t*t)*(k*t**(k-1) if k else 0)) for k in range(KDIM)]
    I = lambda f: quad(f, [-T, 0, T])
    G = mp.matrix(KDIM, KDIM); H = mp.matrix(KDIM, KDIM)
    for i in range(KDIM):
        for j in range(KDIM):
            G[i, j] = I(lambda t, i=i, j=j: psi[i](t)*psi[j](t))
            H[i, j] = I(lambda t, i=i, j=j: dps[i](t)*dps[j](t))
    al  = mp.matrix([I(lambda t, k=k: psi[k](t)*exp(t/2))     for k in range(KDIM)])
    be  = mp.matrix([I(lambda t, k=k: psi[k](t)*exp(-t/2))    for k in range(KDIM)])
    al2 = mp.matrix([I(lambda t, k=k: t*psi[k](t)*exp(t/2))   for k in range(KDIM)])
    be2 = mp.matrix([I(lambda t, k=k: t*psi[k](t)*exp(-t/2))  for k in range(KDIM)])
    return T, G, H, al, be, al2, be2


def run(T0, AT):
    T, G, H, al, be, al2, be2 = setup(T0)
    Gn  = np.array(G.tolist(), dtype=float); Hn = np.array(H.tolist(), dtype=float)
    a_, b_, a2_, b2_ = (np.array(v.tolist(), dtype=float).ravel() for v in (al, be, al2, be2))
    S0 = 0.5*(np.outer(a_, b_) + np.outer(b_, a_))
    S1 = 0.5*(np.outer(a2_, b_) + np.outer(b_, a2_) - np.outer(a_, b2_) - np.outer(b2_, a_))
    C0 = digamma(mpf(1)/4) - log(pi)
    Kf = lambda u: 1/(2*sinh(u/2)) + 1/(2*cosh(u/2))
    tailK = lambda u0: log(coth(u0/2)) + pi - 2*atan(exp(u0))
    W, V, Ls = [], [], []
    for th in np.linspace(0, 2*np.pi, NDIR, endpoint=False):
        w, U = eigh(np.cos(th)*S0 + np.sin(th)*S1, Gn)
        x = mp.matrix([mpf(repr(z)) for z in U[:, -1]])
        nrm2 = (x.T*G*x)[0]
        x = x / sqrt(nrm2)
        A = (al.T*x)[0]; Bv = (be.T*x)[0]; A2 = (al2.T*x)[0]; B2 = (be2.T*x)[0]
        L2 = (x.T*H*x)[0]
        # the minimiser of (L^2/2) int_0^{u0} u^2 K + 2 int_{u0}^inf K is exactly u0 = 2/L
        L = sqrt(L2); u0 = 2/L
        best = L2/2*quad(lambda u: u*u*Kf(u), [0, u0]) + 2*tailK(u0)
        W.append((A*Bv, A2*Bv - A*B2)); V.append(C0 + AT + best); Ls.append(L)
    # inradius of the polygon conv{W} about 0 (convex hull, then min distance to an edge)
    P = np.array([[float(u), float(v)] for u, v in W])
    from scipy.spatial import ConvexHull
    hull = ConvexHull(P)
    r0 = np.inf; inside = True
    for eq in hull.equations:                     # eq = (n, c) with n.x + c <= 0 inside
        val = eq[-1]
        if val > 0: inside = False
        r0 = min(r0, -val)
    Vs = max(float(v) for v in V)
    return dict(T=float(T0), A_T=float(AT), C0=float(C0), r0=float(r0), Vstar=Vs,
                zero_inside=bool(inside),
                B_c_ge_0=Vs/float(r0), B_c_ge_m1=(Vs+1)/float(r0),
                moments=P.tolist(), values=[float(v) for v in V], L=[float(l) for l in Ls])


if __name__ == '__main__':
    out = {}
    for nm, T, AT in [("0.5log3", 0.5*np.log(3.0), 2*np.log(2)/np.sqrt(2.0)),
                      ("0.58", 0.58, 2*np.log(2)/np.sqrt(2.0) + 2*np.log(3)/np.sqrt(3.0))]:
        r = run(T, AT); out[nm] = r
        print(f"T = {nm}: A_T={r['A_T']:.8f}  C0={r['C0']:.7f}  0 interior: {r['zero_inside']}")
        print(f"   r0 = {r['r0']:.6e}   V* = {r['Vstar']:.6f}   max L = {max(r['L']):.3f}")
        print(f"   B (c>=0) = {r['B_c_ge_0']:.1f}      B (c>=-1) = {r['B_c_ge_m1']:.1f}")
    json.dump(out, open('r2_c_beta_bound.json', 'w'), indent=1)
