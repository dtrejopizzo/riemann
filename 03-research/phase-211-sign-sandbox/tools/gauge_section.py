"""Gauge sections and the c-margin of the tail form (ROUND_020_A).  NUMERICAL tool.
Admissible data in the log variable: f(y) = |y|^{-1/2} g(log|y|), g = sum_j a_j b_j, b_j C^inf bumps of half-width w;
window bumps centred in (-T, T), gauge bumps centred in (-T-R, -T) (supp < 1/lambda).  Phi_f(x) = sum_n n^{-1/2} g(x + log n);
Ef = Phi_f on (-T, T), Psi_f = Phi_f on (-T-L, -T).  Forms on tails (rung_gram_tail.py conventions):
  Ar (Levy, C_0 + K), Cb (sum over prime powers 2 Lambda(n) n^{-1/2} c^sym(log n)), Ta = A_i B_j + B_i A_j.
Constraints: Ff(0) = int g e^{u/2} = 0 (all data), A(Ef) = B(Ef) = 0 (P_T).  Gauge space G: gauge bumps with int g e^{u/2} = 0.
Leakage L(f) = int_lambda^inf |Ff|^2 = int_0^inf f^2 dy - int_0^lambda |Ff|^2 dxi.
Sections of the fibre Psi_f + G: 'ell' (min L), 'f2' (min int_0^{1/lambda} f^2), 'tail' (min ||Psi||^2), 'none' (no gauge part).
usage: python3 gauge_section.py T w R L h [nwin_shift]"""
import sys, math, time, numpy as np, mpmath as mp
from numpy.polynomial import legendre as LG
T, w, R, L, h = [float(a) for a in sys.argv[1:6]]
lam = math.exp(T); t0 = time.time()
def bump(r):
    out = np.zeros_like(r); m = np.abs(r) < 1; out[m] = np.exp(-1/(1 - r[m]**2)); return out
sp = w   # spacing = half-width (overlapping bumps)
cw = np.arange(-T + w, T - w + 1e-9, sp); cg = np.arange(-T - w, -T - R - 1e-9, -sp)
cen = np.r_[cw, cg]; nw, ng = len(cw), len(cg); nb = nw + ng
gx, gw_ = LG.leggauss(80)
def uquad(c):  # nodes/weights on [c-w, c+w]
    return c + w*gx, w*gw_
I = np.array([sum(wt*math.exp(u/2)*bump(np.array([(u-c)/w]))[0] for u, wt in zip(*uquad(c))) for c in cen])
# tails on grid
n = int(round(L/h)); xs = -T - L + (np.arange(n) + 0.5)*h
P = np.zeros((nb, n))
for j, c in enumerate(cen):
    nmax = int(math.exp(c + w + T + L)) + 1
    for m in range(1, nmax + 1):
        lm = math.log(m); lo = c - w - lm; hi = c + w - lm
        i0 = max(0, int(math.floor((lo - xs[0])/h))); i1 = min(n, int(math.ceil((hi - xs[0])/h)) + 1)
        if i0 >= n or i1 <= 0 or i1 <= i0: continue
        P[j, i0:i1] += bump((xs[i0:i1] + lm - c)/w)/math.sqrt(m)
print(f"tails {time.time()-t0:.0f}s  nw={nw} ng={ng} grid={n}", flush=True)
# window Ef on Gauss panels, A, B, window Gram
pan = np.linspace(-T, T, 161); Ew = []; Wt = []
for a_, b_ in zip(pan[:-1], pan[1:]):
    x = a_ + (b_-a_)*(gx+1)/2; Ew.append(x); Wt.append(gw_*(b_-a_)/2)
xw = np.concatenate(Ew); ww = np.concatenate(Wt)
Ef = np.zeros((nb, len(xw)))
for j, c in enumerate(cen):
    for m in range(1, int(math.exp(2*T)) + 2): Ef[j] += bump((xw + math.log(m) - c)/w)/math.sqrt(m)
Aw = Ef @ (ww*np.exp(xw/2)); Bw = Ef @ (ww*np.exp(-xw/2)); Mw = (Ef*ww) @ Ef.T
# tail forms
At = h*(P @ np.exp(xs/2)); Bt = h*(P @ np.exp(-xs/2))
C0 = float(mp.digamma(mp.mpf(1)/4) - mp.log(mp.pi))
Kf = lambda u: 1/(2*np.sinh(u/2)) + 1/(2*np.cosh(u/2)); Ktail = lambda q: -math.log(math.tanh(q/4)) + math.pi - 2*math.atan(math.exp(q/2))
def Lam(m):
    for p in range(2, int(math.isqrt(m)) + 1):
        if m % p == 0:
            r = m
            while r % p == 0: r //= p
            return p if r == 1 else 0
    return m
pps = [(m, Lam(m)) for m in range(2, int(math.exp(L)) + 1) if Lam(m)]
NF = 1 << int(math.ceil(math.log2(2*n))); FT = np.fft.rfft(P, NF, axis=1)
uu = np.arange(1, n)*h; Ku = Kf(uu)
lagk = np.array([math.log(m)/h for m, p in pps]); kk = lagk.astype(int); fr = lagk - kk; wt = np.array([2*math.log(p)/math.sqrt(m) for m, p in pps])
ok = kk + 1 < n; kk, fr, wt = kk[ok], fr[ok], wt[ok]
Ar = np.zeros((nb, nb)); Cb = np.zeros((nb, nb)); G0 = np.zeros((nb, nb))
for i in range(nb):
    cr = np.fft.irfft(np.conj(FT[i])[None, :]*FT[i:], NF, axis=1)*h
    for jj, j in enumerate(range(i, nb)):
        cp = cr[jj, :n]; cm = np.r_[cr[jj, 0], cr[jj, NF-1:NF-n:-1]]; cs = 0.5*(cp + cm); c0 = cp[0]
        g = (c0 - cs[1:])*Ku; g0 = 2*g[0] - g[1]
        Ar[i, j] = Ar[j, i] = C0*c0 + h*(0.5*g0 + g[:-1].sum() + 0.5*g[-1]) + c0*Ktail(n*h)
        Cb[i, j] = Cb[j, i] = np.sum(wt*((1-fr)*cs[kk] + fr*cs[kk+1])); G0[i, j] = G0[j, i] = c0
Ta = np.outer(At, Bt) + np.outer(Bt, At)
print(f"forms {time.time()-t0:.0f}s, {len(pps)} prime powers", flush=True)
# leakage Gram and small-y L2 Gram
Y2 = np.zeros((nb, nb)); Fq = []
xq, wq = LG.leggauss(200); xiq = lam*(xq+1)/2; wxi = wq*lam/2
for c in cen:
    u, wu = uquad(c); fu = np.exp(u/2)*bump((u-c)/w)*wu          # int f(y) cos(2 pi xi y) dy = int e^{u/2} b cos(2pi xi e^u) du
    Fq.append(2*np.cos(2*np.pi*np.outer(xiq, np.exp(u))) @ fu)
Fq = np.array(Fq); BL = (Fq*wxi) @ Fq.T
for i in range(nb):
    for j in range(nb):
        if abs(cen[i]-cen[j]) < 2*w:
            u = np.linspace(max(cen[i], cen[j]) - w, min(cen[i], cen[j]) + w, 801)
            v = np.exp(u)*bump((u-cen[i])/w)*bump((u-cen[j])/w); Y2[i, j] = np.trapz(v, u)   # int f_i f_j dy (y>0)
Lg = Y2 - BL
np.savez(f'cache/gsec_T{T}_w{w}_R{R}_L{L}_h{h}.npz', Ar=Ar, Cb=Cb, Ta=Ta, G0=G0, At=At, Bt=Bt, Aw=Aw, Bw=Bw, Mw=Mw, I=I, Lg=Lg, Y2=Y2, nw=nw, ng=ng, cen=cen)
print(f"saved {time.time()-t0:.0f}s")
