"""Stage 1 of the window certificate (Paper 47 prop:lowercert, frequency-truncated lower form).
Ball arithmetic (Arb via python-flint).  Builds, for both parities, the Gram data
   Gacc[i,l] = sum_q w_q g(tau_q) j_i(tau_q T) j_l(tau_q T)        (rows l < K2 of the parity)
   Dacc[l]   = sum_q w_q j_l(tau_q T)^2                             (trace data for S_c)
with g = s_inf - s_T on [0, tauN], plus a rigorous per-entry quadrature error (Gauss-Legendre,
Bernstein-ellipse bound, Trefethen ATAP Thm 19.3).  Spherical Bessel values by forward recurrence
in ball arithmetic at adaptive precision (radius checked), crude bound |j_l(x)| <= x^l/(2l+1)!! beyond
the cut.  usage: build_G.py T_expr tauN s_inf_num s_inf_den K2 [prec] ; T_expr e.g. '1' or 'log15/2+1/100'
"""
import sys, time, json, math, pickle
from flint import arb, acb, arb_mat, ctx

Texpr, tauN, sn, sd, K2 = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
PREC = int(sys.argv[6]) if len(sys.argv) > 6 else 320
ctx.prec = PREC
OUT = sys.argv[7] if len(sys.argv) > 7 else f'G_T{Texpr}_tau{tauN}_K{K2}.pkl'

def Tval():
    if Texpr == '1': return arb(1)
    if Texpr == 'log5h': return arb(5).log() / 2
    if Texpr == '1.2': return arb(6) / 5
    if Texpr == '1.035': return arb(207) / 200
    if Texpr == '1.098': return arb(549) / 500
    if Texpr == 'log15h+0.01': return arb(15).log() / 2 + arb(1) / 100
    raise ValueError
T = Tval()
Tf = float(T.mid())
PI = arb.pi(); LOGPI = PI.log()
# contact set: prime powers n with log n < 2T
def lam(n):
    p = min(q for q in range(2, n + 1) if n % q == 0)
    m = n
    while m % p == 0: m //= p
    return p if m == 1 else None
NT = [n for n in range(2, int(math.exp(2 * Tf)) + 2) if lam(n) and arb(n).log() < 2 * T]
assert all(not (arb(n).log() < 2 * T) for n in range(int(math.exp(2 * Tf)) + 2, int(math.exp(2 * Tf)) + 50))
V = [(2 * arb(lam(n)).log() / arb(n).sqrt(), arb(n).log()) for n in NT]
SV = sum((v for v, _ in V), arb(0))
s_inf = arb(sn) / sd

def m_of(tau):
    return acb(arb(1) / 4, tau / 2).digamma().real - LOGPI
def s_of(tau):
    return m_of(tau) - sum((v * (tau * lg).cos() for v, lg in V), arb(0))

import os
PART, NPART = int(os.environ.get('PART', 0)), int(os.environ.get('NPART', 1))
t0 = time.time()
# ---- (1) certify s_T >= s_inf on |tau| >= tauN: interval scan on [tauN, tauB], m increasing beyond
tauB = tauN
while not (m_of(arb(tauB)) - SV > s_inf): tauB += 1
step = arb(1) / 512
k = 0; nb = (tauB - tauN) * 512
smin = None
while k < nb and PART == 0:
    box = arb(tauN) + step * k + step / 2 + arb(0, float(step.mid()) / 2 * (1 + 1e-9))
    sb = s_of(box)
    if not sb > s_inf:
        raise SystemExit(f'scan fails at tau ~ {float(box.mid())}: {sb}')
    lo = float(sb.lower()); smin = lo if smin is None else min(smin, lo)
    k += 1
print(f'[scan] s_T > s_inf on [{tauN},{tauB}] (min lower {smin}); m(tauB)-A > s_inf; {time.time()-t0:.0f}s', flush=True)

C0 = m_of(arb(0)); mN = m_of(arb(tauN))
om_p = arb((s_inf - C0 + SV).upper()); om_m = arb((mN + SV - s_inf).upper())

# ---- (2) psi modulus bound on boxes (Binet, shift 10)
def psi_abs(wre_lo, wre_hi, wim_lo, wim_hi):
    # box w = [wre_lo,wre_hi] + i[wim_lo,wim_hi]; returns upper bound of |psi(w)|
    ure_lo = wre_lo + 10; ure_hi = wre_hi + 10
    assert ure_lo > 1
    ui = max(abs(wim_lo), abs(wim_hi))
    tot = (arb(ure_hi) ** 2 + arb(ui) ** 2).sqrt().log() + PI / 2 + 1 / (2 * arb(ure_lo)) + 1 / (12 * arb(ure_lo) ** 2)
    imin = 0 if wim_lo <= 0 <= wim_hi else min(abs(wim_lo), abs(wim_hi))
    for kk in range(10):
        rlo = wre_lo + kk
        d = max(rlo, imin) if rlo > 0 else imin
        assert d > 0, ('psi box too close to a pole', wre_lo, wim_lo, wim_hi)
        tot += 1 / arb(d)
    return arb(tot.upper())

# ---- (3) panels
panels = []   # (c0, L, rho, N)
for p in range(40): panels.append((0.5 * p + 0.25, 0.25, 3.2, 46))
c = 20.0
while c < tauN - 1e-9:
    panels.append((c + 4.0, 4.0, 2.0, 92)); c += 8.0
assert abs(c - tauN) < 1e-9, 'tauN must be 20 + 8k'
GLc = {}
def GL(N):
    if N not in GLc: GLc[N] = [arb.legendre_p_root(N, k, weight=True) for k in range(N)]
    return GLc[N]
qerr = arb(0); qerrD = arb(0); nodes = []
for (c0, L, rho, N) in panels:
    L_a = arb(L); rho_a = arb(rho)
    b = L_a * (rho_a - 1 / rho_a) / 2; a = L_a * (rho_a + 1 / rho_a) / 2
    bf, af = float(b.upper()) * (1 + 1e-12), float(a.upper()) * (1 + 1e-12)
    # w = 1/4 + i tau/2 with tau = X + iY, |Y| <= b, X in [c0-a, c0+a]: Re w = 1/4 - Y/2, Im w = X/2
    m1 = psi_abs(0.25 - bf / 2, 0.25 + bf / 2, (c0 - af) / 2, (c0 + af) / 2)
    m2 = psi_abs(0.25 - bf / 2, 0.25 + bf / 2, -(c0 + af) / 2, -(c0 - af) / 2)
    mabs = (m1 + m2) / 2 + LOGPI
    cabs = sum((v * (lg * arb(bf)).cosh() for v, lg in V), arb(0))
    jb = (2 * T * arb(bf)).exp()
    fac = L_a * arb(64) / 15 * rho_a ** (-2 * N) / (rho_a ** 2 - 1)
    qerr += arb(((abs(s_inf) + mabs + cabs) * jb * fac).upper())
    qerrD += arb((jb * fac).upper())
    for (x, w) in GL(N):
        nodes.append((arb(c0) + L_a * x, L_a * w))
print(f'[quad] {len(nodes)} nodes, err/entry (raw) {qerr.str(3)}, trace err {qerrD.str(3)}', flush=True)

# ---- (4) Bessel rows by forward recurrence
TWO = arb(2)
def bessel_rows(x, Lmax):
    xf = float(x.mid())
    # crude cut: first l with x^l/(2l+1)!! < 2^-330 (log estimate), certified below
    lc = None
    lg = 0.0
    for l in range(0, Lmax):
        lg = l * math.log(xf) - (math.lgamma(2 * l + 2) - math.lgamma(l + 1) - l * math.log(2))  # log(x^l/(2l+1)!!)
        if l > xf and lg < -330 * math.log(2): lc = l; break
    Lrec = Lmax if lc is None else lc
    if lc is not None:   # certify crude bound at lc (decreasing beyond since lc > x/2)
        dfa = (TWO ** (lc + 1)) * arb(lc + 1.5).gamma() / PI.sqrt()
        cb = x ** lc / dfa
        assert cb < TWO ** (-320), ('crude', xf, lc, cb)
    p = int(1.6 * xf) + 600
    while True:
        ctx.prec = p
        X = arb(x.mid()); s = X.sin(); co = X.cos(); ix = 1 / X
        j = [s * ix, s * ix * ix - co * ix]
        for l in range(1, Lrec - 1):
            j.append((2 * l + 1) * ix * j[l] - j[l - 1])
        j = j[:Lrec]
        ok = all(v.rad() < TWO ** (-330) for v in j)
        if ok: break
        p = int(p * 1.5)
        if p > 200000: raise SystemExit(f"bessel prec blowup x={xf} Lrec={Lrec} worst={max(v.rad() for v in j)}")
    ctx.prec = PREC
    xr = arb(0, float(x.rad().upper().str(6, radius=False)) * 1.0001 + 1e-300)  # |j_l'| <= 1
    j = [v * 1 + xr for v in j]
    tailball = arb(0, float((TWO ** (-320)).upper()))
    return j + [tailball] * (Lmax - Lrec)

rows = {par: list(range(par, K2, 2)) for par in (0, 1)}
Gacc = {par: arb_mat(len(rows[par]), len(rows[par])) for par in (0, 1)}
Dacc = [arb(0)] * K2
CH = 1200
nper = -(-len(nodes) // NPART)
nodes = nodes[PART * nper:(PART + 1) * nper]
OUT = OUT if NPART == 1 else OUT.replace('.pkl', f'_part{PART}of{NPART}.pkl')
for c0 in range(0, len(nodes), CH):
    chunk = nodes[c0:c0 + CH]
    Jm = {par: arb_mat(len(rows[par]), len(chunk)) for par in (0, 1)}
    Jw = {par: arb_mat(len(rows[par]), len(chunk)) for par in (0, 1)}
    for cc, (tau, w) in enumerate(chunk):
        jl = bessel_rows(tau * T, K2)
        wg = w * (s_inf - s_of(tau))
        for l in range(K2):
            par = l & 1; r = l >> 1
            Jm[par][r, cc] = jl[l]
            Jw[par][r, cc] = jl[l] * wg
            Dacc[l] += w * jl[l] * jl[l]
    for par in (0, 1):
        Gacc[par] += Jw[par] * Jm[par].transpose()
    print(f'  nodes {c0+len(chunk)}/{len(nodes)}  {time.time()-t0:.0f}s', flush=True)

def ser(v): return (v.mid().str(120, radius=False), float(v.rad().upper().str(6, radius=False)) * (1 + 1e-5))
data = dict(Texpr=Texpr, tauN=tauN, s_inf=(sn, sd), K2=K2, prec=PREC, NT=NT,
            qerr=qerr.str(30), qerrD=qerrD.str(30), om_p=om_p.str(40), om_m=om_m.str(40), mN=mN.str(40),
            tauB=tauB,
            G={par: [[ser(Gacc[par][a, b]) for b in range(len(rows[par]))] for a in range(len(rows[par]))] for par in (0, 1)},
            D=[ser(v) for v in Dacc], seconds=time.time() - t0)
pickle.dump(data, open(OUT, 'wb'))
print('saved', OUT, f'{time.time()-t0:.0f}s')
