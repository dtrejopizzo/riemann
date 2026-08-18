#!/usr/bin/env python3
"""Directed endpoint-flat Green band 200:400 at T6.

Both the old 78-dimensional source and the 200-dimensional trial band are
inside the order-60 endpoint-flat primitive space.  Hence the exact Galerkin
corrected source remains endpoint-flat and can be passed to the D.208
post-400 Plancherel certificate.
"""
from __future__ import annotations

from fractions import Fraction
import os
import numpy as np
from flint import arb, arb_mat, ctx


N0, N1, M = 200, 400, 60
D0, D1 = N0-2*M, N1-2*M
NF, NW = D0-2, D1-D0
DPS = int(os.environ.get("D226_DPS", "160"))
RHO = arb(os.environ.get("D226_RHO", ".2"))
ctx.dps = DPS
T = arb(6).log()/2
LAMBDA = Fraction(4*M+1, 2)


def center(X: arb_mat) -> np.ndarray:
    return np.array([[float(X[i, j].mid()) for j in range(X.ncols())]
                     for i in range(X.nrows())])


def tate(n: int, sign: int) -> arb:
    k = T/2
    value = (2*arb.pi()/k).sqrt()*k.bessel_i(arb(2*n+1)/2)
    if sign < 0 and n % 2:
        value = -value
    return (T*arb(2*n+1)/2).sqrt()*value


def xmul(src: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(N1)]
    for n, value in enumerate(src):
        if not value:
            continue
        if n+1 < N1:
            out[n+1] += value*Fraction(n+1, 2*n+1)
        if n:
            out[n-1] += value*Fraction(n, 2*n+1)
    return out


def raw_flat() -> list[list[Fraction]]:
    zero = [Fraction(0) for _ in range(N1)]
    c0 = zero.copy()
    c0[0] = 1
    c1 = zero.copy()
    c1[1] = 2*LAMBDA
    cols = [c0, c1]
    for n in range(1, D1-1):
        nxt = zero.copy()
        xx = xmul(cols[-1])
        a = Fraction(2)*(n+LAMBDA)/(n+1)
        b = -Fraction(n+2*LAMBDA-1, n+1)
        for i in range(N1):
            nxt[i] += a*xx[i]+b*cols[-2][i]
        cols.append(nxt)
    for k in range(D1):
        for _ in range(M):
            xx = xmul(xmul(cols[k]))
            cols[k] = [a-b for a, b in zip(cols[k], xx)]
    return cols


def pivot_columns(A: np.ndarray, rank: int) -> list[int]:
    residual = A.copy()
    pivots: list[int] = []
    for _ in range(rank):
        norms = np.sum(residual*residual, axis=0)
        norms[pivots] = -1
        j = int(np.argmax(norms))
        assert norms[j] > 1e-24
        q = residual[:, j]/np.sqrt(norms[j])
        residual -= q[:, None]*(q@residual)[None, :]
        pivots.append(j)
    return pivots


def whitener(X: arb_mat) -> tuple[arb_mat, np.ndarray]:
    xc = center(X)
    xc = (xc+xc.T)/2
    L = np.linalg.cholesky(xc)
    p0 = np.linalg.inv(L.T)
    return (arb_mat([[arb(repr(float(p0[i, j])))
                      for j in range(p0.shape[1])]
                     for i in range(p0.shape[0])]), p0)


def gersh(X: arb_mat, name: str) -> list[arb]:
    margins = []
    for i in range(X.nrows()):
        off = sum((abs(X[i, j]) for j in range(X.ncols()) if i != j),
                  arb(0))
        margins.append(X[i, i]-off)
    worst = min(margins, key=lambda z: float(z.lower()))
    print(name, "Gershgorin", worst, flush=True)
    assert all(z.lower() > 0 for z in margins)
    return margins


def binary_enclosure(X: arb_mat) -> tuple[np.ndarray, np.ndarray]:
    """Serialize an Arb matrix without losing its directed enclosure."""
    c = center(X)
    r = np.array([[float(X[i, j].rad()) for j in range(X.ncols())]
                  for i in range(X.nrows())])
    r = np.nextafter(r+np.abs(np.spacing(c))/2, np.inf)
    return c, r


gp = [tate(i, 1) for i in range(N1)]
gm = [tate(i, -1) for i in range(N1)]
raw = raw_flat()
R = arb_mat(N1, D1)
for k, col in enumerate(raw):
    norm2 = sum((Fraction(2, 2*n+1)*a*a
                 for n, a in enumerate(col)), Fraction(0))
    scale = (T*arb(norm2.numerator)/norm2.denominator).sqrt()
    for n, value in enumerate(col):
        if value:
            standard = arb(value.numerator)/value.denominator/scale
            R[n, k] = standard/(arb(2*n+1)/(2*T)).sqrt()
print("exact flat raw basis ready", flush=True)

# Old primitive flat source: kernel of the two Tate rows on the first D0
# raw columns.
mom0 = arb_mat([gp, gm])*arb_mat(
    [[R[i, j] for j in range(D0)] for i in range(N1)]
)
mc = center(mom0)
_, _, vh = np.linalg.svd(mc, full_matrices=True)
sel = vh[2:].T
Y = arb_mat(D0, NF)
head = arb_mat([[mom0[0, 0], mom0[0, 1]],
                [mom0[1, 0], mom0[1, 1]]])
for col in range(NF):
    for k in range(2, D0):
        Y[k, col] = arb(repr(float(sel[k, col])))
    rhs = arb_mat([
        [-sum((mom0[0, k]*Y[k, col] for k in range(2, D0)), arb(0))],
        [-sum((mom0[1, k]*Y[k, col] for k in range(2, D0)), arb(0))],
    ])
    sol = head.solve(rhs)
    Y[0, col], Y[1, col] = sol[0, 0], sol[1, 0]
R0 = arb_mat([[R[i, j] for j in range(D0)] for i in range(N1)])
F = R0*Y
assert (arb_mat([gp, gm])*F).contains(arb_mat(2, NF))

# Endpoint-flat primitive orthogonal band: kernel of the two Tate moments
# and all 78 old-source inner products on the full 280-column flat space.
constraints = arb_mat(2+NF, D1)
mom1 = arb_mat([gp, gm])*R
for j in range(D1):
    constraints[0, j], constraints[1, j] = mom1[0, j], mom1[1, j]
FR = F.transpose()*R
for i in range(NF):
    for j in range(D1):
        constraints[2+i, j] = FR[i, j]
hc = center(constraints)
pivots = pivot_columns(hc, 2+NF)
free = [j for j in range(D1) if j not in set(pivots)]
assert len(free) == NW
Hp = arb_mat([[constraints[i, j] for j in pivots]
              for i in range(2+NF)])
Hf = arb_mat([[constraints[i, j] for j in free]
              for i in range(2+NF)])
sol = Hp.solve(-Hf)
Z = arb_mat(D1, NW)
for i, p in enumerate(pivots):
    for j in range(NW):
        Z[p, j] = sol[i, j]
for j, f in enumerate(free):
    Z[f, j] = 1
W = R*Z
assert (arb_mat([gp, gm])*W).contains(arb_mat(2, NW))
assert (F.transpose()*W).contains(arb_mat(NF, NW))
print("exact flat primitive orthogonal band: PASS", flush=True)

# Native operator caches.
gn = np.load(os.environ.get(
    "D226_GAMMA", "/tmp/t6_gamma400_native250.npz"
), allow_pickle=False)["G"]
cn = np.load(os.environ.get(
    "D226_CONTACT", "/tmp/t6_contact400_native_strings.npz"
), allow_pickle=False)["C"]
assert gn.shape[0] >= N1 and cn.shape[0] >= N1
A = arb_mat([[arb(str(gn[i, j]))+arb(str(cn[i, j]))
              for j in range(N1)] for i in range(N1)])
m0 = arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log()
for i in range(N1):
    A[i, i] -= m0
B = F.transpose()*A*F
E = W.transpose()*A*W
C = F.transpose()*A*W
print("native flat Green blocks assembled", flush=True)

# Falsifier only: this centre calculation never enters a certificate.  It is
# printed before the interval Schur test so that a bad proposed budget is
# rejected transparently rather than hidden behind a failed Cholesky step.
bc, ec, cc = center(B), center(E), center(C)
lb = np.linalg.cholesky((bc+bc.T)/2)
le = np.linalg.cholesky((ec+ec.T)/2)
cw_centre = np.linalg.solve(lb, cc)
cw_centre = np.linalg.solve(le, cw_centre.T).T
rho_centre = float(np.linalg.svd(cw_centre, compute_uv=False)[0]**2)
print("HEURISTIC centre finite capacity =", rho_centre, flush=True)
print("interval target =", RHO, flush=True)

PB, PB0 = whitener(B)
PE, PE0 = whitener(E)
QB = PB.transpose()*B*PB
QE = PE.transpose()*E*PE
bmarg = gersh(QB, "flat source")
gersh(QE, "flat band")
CW = PB.transpose()*C*PE
schur = RHO*QB-CW*QE.inv()*CW.transpose()
schur = (schur+schur.transpose())/2
PS, PS0 = whitener(schur)
smarg = gersh(PS.transpose()*schur*PS, "flat finite capacity")

# The corrected source remains exactly endpoint-flat because both F and W
# lie in the same order-60 ideal.
green = E.inv()*C.transpose()
Fcorr = F-W*green
assert (W.transpose()*A*Fcorr).contains(arb_mat(NW, NF))
fc, fr = binary_enclosure(Fcorr)
wc, wr = binary_enclosure(W)
gc, gr = binary_enclosure(green)
Bcorr = B-C*green
Bcc, Bcr = binary_enclosure(Bcorr)

save = os.environ.get("D226_SAVE",
                      "/tmp/t6_flat_green400_arb.npz")
np.savez_compressed(
    save,
    frame_c=fc, frame_r=fr,
    band_c=wc, band_r=wr,
    green_c=gc, green_r=gr,
    source_schur_c=Bcc, source_schur_r=Bcr,
    whitener=PB0,
    gershgorin_margin=np.array(
        min(float(z.lower()) for z in bmarg)
    ),
    capacity_gersh_lower=np.array([float(z.lower()) for z in smarg]),
    rho=np.array(float(RHO.mid())),
    N=np.array(N1), M=np.array(M), dimension=np.array(NF),
    digits=np.array(DPS),
)
print("saved", save, flush=True)
print("D226 DIRECTED ENDPOINT-FLAT GREEN400: PASS", flush=True)
