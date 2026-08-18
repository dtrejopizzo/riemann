#!/usr/bin/env python3
"""Directed flat/boundary Schur decomposition of primitive V200 at T6.

Builds the exact endpoint-flat Tate kernel (dimension 78), constructs its
L2-orthogonal complement inside primitive V200 (dimension 120), loads the
native Gamma/contact operator, and certifies the flat block and the
flat-shorted boundary block by Arb congruences.
"""
from __future__ import annotations

from fractions import Fraction
import os
import numpy as np
from flint import arb, arb_mat, ctx


N = 200
M = 60
DF = N-2*M
NF = DF-2
NB = N-2-NF
DPS = int(os.environ.get("D225_DPS", "140"))
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


def add_scaled(out: list[Fraction], src: list[Fraction],
               scale: Fraction) -> None:
    for i, value in enumerate(src):
        out[i] += scale*value


def xmul(src: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(N)]
    for n, value in enumerate(src):
        if not value:
            continue
        if n+1 < N:
            out[n+1] += value*Fraction(n+1, 2*n+1)
        if n:
            out[n-1] += value*Fraction(n, 2*n+1)
    return out


def flat_columns() -> list[list[Fraction]]:
    zero = [Fraction(0) for _ in range(N)]
    c0 = zero.copy()
    c0[0] = 1
    c1 = zero.copy()
    c1[1] = 2*LAMBDA
    cols = [c0, c1]
    for n in range(1, DF-1):
        nxt = zero.copy()
        add_scaled(nxt, xmul(cols[-1]),
                   Fraction(2)*(n+LAMBDA)/(n+1))
        add_scaled(nxt, cols[-2],
                   -Fraction(n+2*LAMBDA-1, n+1))
        cols.append(nxt)
    for k in range(DF):
        for _ in range(M):
            xx = xmul(xmul(cols[k]))
            cols[k] = [a-b for a, b in zip(cols[k], xx)]
    return cols


def directed_gershgorin(X: arb_mat, name: str) -> list[arb]:
    margins = []
    for i in range(X.nrows()):
        off = sum((abs(X[i, j]) for j in range(X.ncols()) if i != j),
                  arb(0))
        margins.append(X[i, i]-off)
    worst = min(margins, key=lambda z: float(z.lower()))
    print(name, "directed Gershgorin", worst, flush=True)
    assert all(z.lower() > 0 for z in margins)
    return margins


def whitener(X: arb_mat) -> tuple[arb_mat, np.ndarray]:
    xc = center(X)
    xc = (xc+xc.T)/2
    L = np.linalg.cholesky(xc)
    p0 = np.linalg.inv(L.T)
    P = arb_mat([[arb(repr(float(p0[i, j])))
                  for j in range(p0.shape[1])]
                 for i in range(p0.shape[0])])
    return P, p0


def pivot_columns(A: np.ndarray, rank: int) -> list[int]:
    """Deterministic modified Gram--Schmidt column pivoting."""
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


gp = [tate(i, 1) for i in range(N)]
gm = [tate(i, -1) for i in range(N)]

# Old primitive frame selected from the same centre operator as D.219.
gs = np.load("/tmp/t6_gamma260_arb2100.npz")["C"][:N, :N]
cs = np.load("/tmp/t6_contacts260_arb.npz")["C"][:N, :N]
m0 = arb.pi().log()+arb.const_euler()+arb.pi()/2+3*arb(2).log()
Ac = gs+cs-float(m0.mid())*np.eye(N)
Ac = (Ac+Ac.T)/2
Jc = np.array([[float(x.mid()) for x in gp],
               [float(x.mid()) for x in gm]])
_, _, vh = np.linalg.svd(Jc, full_matrices=True)
Q0 = vh[2:].T
_, vec = np.linalg.eigh(Q0.T@Ac@Q0)
Xc = Q0@vec
head = arb_mat([[gp[0], gp[1]], [gm[0], gm[1]]])
X = arb_mat(N, N-2)
for col in range(N-2):
    tail = [arb(repr(float(Xc[i, col]))) for i in range(2, N)]
    rhs = arb_mat([
        [-sum((gp[i]*tail[i-2] for i in range(2, N)), arb(0))],
        [-sum((gm[i]*tail[i-2] for i in range(2, N)), arb(0))],
    ])
    sol = head.solve(rhs)
    X[0, col], X[1, col] = sol[0, 0], sol[1, 0]
    for i in range(2, N):
        X[i, col] = tail[i-2]
assert (arb_mat([gp, gm])*X).contains(arb_mat(2, N-2))

# Exact flat Tate kernel.
raw = flat_columns()
W0 = arb_mat(N, DF)
for k, col in enumerate(raw):
    norm2 = sum((Fraction(2, 2*n+1)*a*a
                 for n, a in enumerate(col)), Fraction(0))
    scale = (T*arb(norm2.numerator)/norm2.denominator).sqrt()
    for n, value in enumerate(col):
        if value:
            standard = arb(value.numerator)/value.denominator/scale
            W0[n, k] = standard/(arb(2*n+1)/(2*T)).sqrt()
mom = arb_mat([gp, gm])*W0
mc = center(mom)
_, _, vhf = np.linalg.svd(mc, full_matrices=True)
selector = vhf[2:].T
Y = arb_mat(DF, NF)
fhead = arb_mat([[mom[0, 0], mom[0, 1]],
                 [mom[1, 0], mom[1, 1]]])
for col in range(NF):
    for k in range(2, DF):
        Y[k, col] = arb(repr(float(selector[k, col])))
    rhs = arb_mat([
        [-sum((mom[0, k]*Y[k, col] for k in range(2, DF)), arb(0))],
        [-sum((mom[1, k]*Y[k, col] for k in range(2, DF)), arb(0))],
    ])
    sol = fhead.solve(rhs)
    Y[0, col], Y[1, col] = sol[0, 0], sol[1, 0]
F = W0*Y
assert (arb_mat([gp, gm])*F).contains(arb_mat(2, NF))
print("exact endpoint-flat Tate frame: PASS", flush=True)

# Kernel of F^*X, enforced by an Arb pivot solve.
H = F.transpose()*X
hc = center(H)
pivots = pivot_columns(hc, NF)
free = [j for j in range(N-2) if j not in set(pivots)]
assert len(free) == NB
Hp = arb_mat([[H[i, j] for j in pivots] for i in range(NF)])
Z = arb_mat(N-2, NB)
for col, j in enumerate(free):
    rhs = arb_mat([[-H[i, j]] for i in range(NF)])
    sol = Hp.solve(rhs)
    for i, p in enumerate(pivots):
        Z[p, col] = sol[i, 0]
    Z[j, col] = 1
D = X*Z
assert (arb_mat([gp, gm])*D).contains(arb_mat(2, NB))
assert (F.transpose()*D).contains(arb_mat(NF, NB))
print("exact flat/boundary orthogonal decomposition: PASS", flush=True)

# Native complete operator.
gn = np.load("/tmp/t6_gamma260_native250.npz", allow_pickle=False)["G"]
cn = np.load("/tmp/t6_contact260_native_strings.npz",
             allow_pickle=False)["C"]
A = arb_mat([[arb(str(gn[i, j]))+arb(str(cn[i, j]))
              for j in range(N)] for i in range(N)])
for i in range(N):
    A[i, i] -= m0
Bff = F.transpose()*A*F
Kdd = D.transpose()*A*D
Cdf = D.transpose()*A*F

PF, PF0 = whitener(Bff)
QF = PF.transpose()*Bff*PF
directed_gershgorin(QF, "flat78")
K = Kdd-Cdf*Bff.inv()*Cdf.transpose()
K = (K+K.transpose())/2
PK, PK0 = whitener(K)
QK = PK.transpose()*K*PK
kmarg = directed_gershgorin(QK, "flat-shorted boundary120")

# Exact graph, A-orthogonal to the flat safe channel.
Dgraph = D-F*(Bff.inv()*Cdf.transpose())
assert (F.transpose()*A*Dgraph).contains(arb_mat(NF, NB))
dc = center(Dgraph)
dr = np.array([[float(Dgraph[i, j].rad()) for j in range(NB)]
               for i in range(N)])
dr = np.nextafter(dr+np.abs(np.spacing(dc))/2, np.inf)

# Whiten the boundary graph for the cancellation-free continuum action
# certificate D.172.  This is a congruence of the already certified Schur
# block, not a new numerical approximation to the form.
Gboundary = Dgraph*PK
Kboundary = PK.transpose()*K*PK
gc = center(Gboundary)
gr = np.array([[float(Gboundary[i, j].rad()) for j in range(NB)]
               for i in range(N)])
gr = np.nextafter(gr+np.abs(np.spacing(gc))/2, np.inf)
kc = center(Kboundary)
kr = np.array([[float(Kboundary[i, j].rad()) for j in range(NB)]
               for i in range(NB)])
kr = np.nextafter(kr+np.abs(np.spacing(kc))/2, np.inf)
gnative = np.array([[str(Gboundary[i, j]) for j in range(NB)]
                    for i in range(N)], dtype=str)
knative = np.array([[str(Kboundary[i, j]) for j in range(NB)]
                    for i in range(NB)], dtype=str)
action_save = os.environ.get(
    "D225_ACTION_SAVE", "/tmp/t6_boundary120_action_graph.npz"
)
np.savez_compressed(
    action_save, C=gc, R=gr, K=kc, KR=kr,
    C_native=gnative, K_native=knative,
    endpoint=np.array(6), dimension=np.array(N),
    native_digits=np.array(DPS),
)
print("saved", action_save, flush=True)

save = os.environ.get("D225_SAVE",
                      "/tmp/t6_flat_boundary_native_schur.npz")
np.savez_compressed(
    save,
    flat_dimension=np.array(NF), boundary_dimension=np.array(NB),
    flat_whitener=PF0, boundary_whitener=PK0,
    boundary_gersh_lower=np.array([float(z.lower()) for z in kmarg]),
    boundary_graph_c=dc, boundary_graph_r=dr,
    digits=np.array(DPS),
)
print("saved", save, flush=True)
print("D225 DIRECTED FLAT/BOUNDARY V200 SCHUR: PASS", flush=True)
