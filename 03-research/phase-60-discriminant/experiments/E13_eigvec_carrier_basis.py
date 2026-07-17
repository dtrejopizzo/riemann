#!/usr/bin/env python3
# ======================================================================================
# IV.1 deep identification of A_inf via eigenVECTORS.
# Engine reused verbatim from E11/E12 (q_func, QW_entry, eigsy via mpmath).
# We build QW at several lambda, take eigenvectors v_0..v_6 (high precision),
# then analyze their real-space structure with numpy/scipy:
#   (1) FFT to find the TRUE carrier frequency omega_k of each eigenvector
#       (E12 used (-1)^j = omega=pi blindly; check if that is actually the carrier).
#   (2) De-modulate with the measured carrier, count envelope nodes.
#   (3) Overlap of de-modulated envelope vs Dirichlet modes AND Hermite functions
#       AND prolate spheroidal (PSWF) via the prolate ODE / DPSS proxy.
#   (4) Search for a diagonal/unitary D so that D^{-1} QW D has a nonnegative ground vector
#       (positivity-preserving / Perron-Frobenius representation): try D=diag((-1)^j),
#       D=diag(e^{i*omega0*j}), and the sign-flip that makes v_0 all positive.
# Output is plain numbers; honest.
# ======================================================================================
import mpmath as mp
import numpy as np
mp.mp.dps = 40
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi)

def q_func(m, n, L):
    if m == n:
        return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def QW_entry(m, n, L, lam):
    q = q_func(m, n, L); q0 = q(mp.mpf(0))
    W02 = mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
    def wr(y):
        if y < mp.mpf('1e-12'):
            h = mp.mpf('1e-8'); return ((q(h)-q0)/h+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WR = (LOG4PI+GAMMA)*q0/2 + mp.quad(wr, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    arith = mp.mpf(0); mx = int(lam*lam); sv = [True]*(mx+1)
    for i in range(2, int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i, mx+1, i): sv[j] = False
    for p in range(2, mx+1):
        if sv[p]:
            lp = mp.log(p); pm = p; me = 1
            while pm <= mx:
                arith += lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp); pm *= p; me += 1
    return W02-WR-arith

def build_QW(lam, N):
    L = 2*mp.log(lam); dim = 2*N+1; idx = list(range(-N, N+1))
    M = mp.zeros(dim)
    for a in range(dim):
        for b in range(a, dim):
            v = QW_entry(idx[a], idx[b], L, lam); M[a, b] = v; M[b, a] = v
    E, V = mp.eigsy(M)
    order = sorted(range(dim), key=lambda j: E[j])
    eig = [float(E[order[k]]) for k in range(dim)]
    vecs = []
    for k in range(dim):
        col = order[k]
        vecs.append(np.array([float(V[i, col]) for i in range(dim)]))
    return np.array(eig), vecs, dim

def carrier_freq(v):
    # find dominant FFT frequency of the eigenvector (the carrier).
    n = len(v)
    f = np.fft.rfft(v * np.hanning(n))
    k = np.argmax(np.abs(f))
    omega = 2*np.pi*k/n  # radians per sample
    return omega, k, np.abs(f)

def hermite_funcs(K, dim):
    # discrete Hermite functions sampled on a symmetric grid, scaled to fit support.
    x = np.linspace(-1, 1, dim)
    # choose scale so a few oscillations fit; use physicists' Hermite * gaussian
    from numpy.polynomial.hermite import hermval
    out = []
    a = 4.0  # gaussian width scale (tunable); we try a small sweep later
    for k in range(K):
        c = np.zeros(k+1); c[k] = 1.0
        h = hermval(a*x, c)*np.exp(-(a*x)**2/2)
        h = h/np.linalg.norm(h)
        out.append(h)
    return out, x

def dpss_modes(K, dim, NW):
    # prolate spheroidal (discrete prolate spheroidal sequences) as PSWF proxy
    try:
        from scipy.signal.windows import dpss
        seqs = dpss(dim, NW, K, return_ratios=False)
        return [s/np.linalg.norm(s) for s in seqs]
    except Exception as e:
        return None

def overlap(a, b):
    return abs(np.dot(a, b))/(np.linalg.norm(a)*np.linalg.norm(b))

def sign_changes(v, tol=1e-9):
    s = [x for x in v if abs(x) > tol]
    return sum(1 for i in range(1, len(s)) if s[i]*s[i-1] < 0)

for lam in [7.0, 9.0, 11.0]:
    N = 14 if lam < 10 else 16
    eig, vecs, dim = build_QW(mp.mpf(lam), N)
    e0 = eig[0]
    print("="*78)
    print(f"lambda={lam}  N={N}  dim={dim}")
    print(f"eps_k/eps_0 : " + "  ".join(f"{eig[k]/e0:.4f}" for k in range(7)))
    print(f"(k+1)^2     : " + "  ".join(f"{(k+1)**2:.4f}" for k in range(7)))
    print("-"*78)
    print(" k | raw_sgn | carrier omega/pi | env_nodes(true) | ov_Dir | ov_Herm_best | ov_DPSS")
    herm, xg = hermite_funcs(7, dim)
    dpss = dpss_modes(7, dim, NW=2.5)
    for k in range(7):
        v = vecs[k]
        rsg = sign_changes(v)
        omega, kbin, spec = carrier_freq(v)
        # de-modulate with measured carrier (use cos to keep real envelope magnitude)
        j = np.arange(dim)
        # complex demod then take magnitude-preserving real part via analytic signal
        from scipy.signal import hilbert
        analytic = hilbert(v)
        env = np.abs(analytic)            # true envelope (carrier removed)
        env_signed = np.real(analytic*np.exp(-1j*omega*(j-dim//2)))
        env_nodes = sign_changes(env_signed)
        # Dirichlet mode k (k+1 half-waves)
        D = np.sin((k+1)*np.pi*(np.arange(dim)+1)/(dim+1))
        ovDir = overlap(env_signed, D)
        # Hermite best over a small scale sweep
        ovH = 0.0
        for a in [2.0, 3.0, 4.0, 5.0, 6.0]:
            from numpy.polynomial.hermite import hermval
            c = np.zeros(k+1); c[k] = 1.0
            h = hermval(a*xg, c)*np.exp(-(a*xg)**2/2)
            ovH = max(ovH, overlap(v, h))   # compare RAW vec to Hermite (Hermite has its own sign structure)
        ovDP = overlap(v, dpss[k]) if dpss is not None else float('nan')
        print(f" {k} |  {rsg:>3}   |     {omega/np.pi:.3f}        |     {env_nodes:>3}        | {ovDir:.3f}  |   {ovH:.3f}     | {ovDP:.3f}")
    # ---- positivity-preserving representation probe ----
    v0 = vecs[0]
    print("-"*78)
    print(f" ground v0: raw sign changes = {sign_changes(v0)}")
    # is |v0| (all-positive) close to a smooth bump? compare with first DPSS / first Dirichlet
    av0 = np.abs(v0)
    print(f"   overlap(|v0|, Dirichlet_1) = {overlap(av0, np.sin(np.pi*(np.arange(dim)+1)/(dim+1))):.4f}")
    print(f"   overlap(|v0|, DPSS_0)      = {overlap(av0, dpss[0]) if dpss is not None else float('nan'):.4f}")
    # Does diag((-1)^j) v0 become (nearly) one-signed? (the omega=pi carrier hypothesis)
    flip = v0*((-1)**np.arange(dim))
    print(f"   diag((-1)^j) v0 sign changes = {sign_changes(flip)}")
    # Does diag(e^{i omega0 j}) demod via measured carrier make it one-signed?
    om0, _, _ = carrier_freq(v0)
    demod0 = np.real(hilbert(v0)*np.exp(-1j*om0*(np.arange(dim)-dim//2)))
    print(f"   carrier-demod v0 (omega0/pi={om0/np.pi:.3f}) sign changes = {sign_changes(demod0)}")
