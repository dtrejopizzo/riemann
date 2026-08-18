#!/usr/bin/env python3
"""Directed two-column Galerkin graph after eliminating V260 safe modes.

The binary centres select an eigenframe only.  Both Tate equations, Gamma,
the delicate contact action, the safe inverse, the final Schur block and
the graph coefficients are then evaluated in Arb.  The resulting graph is
the input for the total-action enclosure D.172.
"""
from __future__ import annotations

import importlib.util
import os
from pathlib import Path

import numpy as np
from flint import arb, arb_mat, ctx


HERE = Path(__file__).resolve().parent
N = int(os.environ.get("D219_N", "260"))
ND = 2
NS = N - 2 - ND
DPS = int(os.environ.get("D219_DPS", "2100"))
WORK_DPS = int(os.environ.get("D219_WORK_DPS", "250"))
ctx.dps = DPS
T = arb(6).log() / 2


def sub(X: arb_mat, r0: int, r1: int, c0: int, c1: int) -> arb_mat:
    return arb_mat([[X[i, j] for j in range(c0, c1)]
                    for i in range(r0, r1)])


def center(X: arb_mat) -> np.ndarray:
    return np.array([[float(X[i, j].mid()) for j in range(X.ncols())]
                     for i in range(X.nrows())])


def float_ball(c: float, r: float) -> arb:
    rr = np.nextafter(float(r), np.inf)
    rr += abs(np.spacing(float(c))) / 2 + np.nextafter(0.0, 1.0)
    return arb(repr(float(c)), repr(float(rr)))


def tate(n: int, sign: int) -> arb:
    k = T / 2
    value = (2 * arb.pi() / k).sqrt() * k.bessel_i(arb(2*n+1) / 2)
    if sign < 0 and n % 2:
        value = -value
    return (T * arb(2*n+1) / 2).sqrt() * value


def legvals(x: arb) -> list[arb]:
    out = [arb(1), x]
    for n in range(1, N - 1):
        out.append(((2*n+1)*x*out[-1] - n*out[-2]) / (n+1))
    return out


def native_contact_on_delicate(D: arb_mat) -> arb_mat:
    order = N + 4
    directed = [arb.legendre_p_root(order, k, weight=True)
                for k in range(order)]
    roots = [z[0] for z in directed]
    weights = [z[1] for z in directed]
    mass_error = abs(sum(weights, arb(0)) - 2)
    print("Gauss mass error", mass_error, flush=True)
    assert mass_error < arb("1e-100")
    norms = [(arb(2*i+1) / 2).sqrt() for i in range(N)]
    U = arb_mat(N, ND)
    for nn, lam in ((2, arb(2).log()), (3, arb(3).log()),
                    (4, arb(2).log()), (5, arb(5).log())):
        d = arb(nn).log() / T
        midpoint = -d / 2
        half = 1 - d / 2
        coefficient = lam / arb(nn).sqrt()
        for node, weight in zip(roots, weights):
            u = midpoint + half * node
            vx, vy = legvals(u), legvals(u + d)
            for i in range(N):
                vx[i] *= norms[i]
                vy[i] *= norms[i]
            dx = [sum((D[i, j] * vx[i] for i in range(N)), arb(0))
                  for j in range(ND)]
            dy = [sum((D[i, j] * vy[i] for i in range(N)), arb(0))
                  for j in range(ND)]
            scale = -coefficient * half * weight
            for i in range(N):
                for j in range(ND):
                    U[i, j] += scale * (vx[i]*dy[j] + vy[i]*dx[j])
        print("native delicate contact", nn, "complete", flush=True)
    return U


def directed_gershgorin(X: arb_mat, name: str) -> list[arb]:
    margins = []
    for i in range(X.nrows()):
        off = sum((abs(X[i, j]) for j in range(X.ncols()) if i != j),
                  arb(0))
        margins.append(X[i, i] - off)
    worst = min(margins, key=lambda z: float(z.lower()))
    print(name, "directed Gershgorin", worst, flush=True)
    assert all(z.lower() > 0 for z in margins)
    return margins


gamma_file = np.load(os.environ.get(
    "D219_GAMMA", "/tmp/t6_gamma260_arb2100.npz"
))
contact_file = np.load(os.environ.get(
    "D219_CONTACT", "/tmp/t6_contacts260_arb.npz"
))
assert gamma_file["C"].shape[0] >= N and gamma_file["C"].shape[1] >= N
assert contact_file["C"].shape[0] >= N and contact_file["C"].shape[1] >= N

m0 = arb.pi().log() + arb.const_euler() + arb.pi()/2 + 3*arb(2).log()
m0f = float(m0.mid())
A0 = (np.asarray(gamma_file["C"])[:N, :N]
      + np.asarray(contact_file["C"])[:N, :N])
A0 = A0 - m0f * np.eye(N)
A0 = (A0 + A0.T) / 2

gp = [tate(i, 1) for i in range(N)]
gm = [tate(i, -1) for i in range(N)]
J0 = np.array([[float(x.mid()) for x in gp],
               [float(x.mid()) for x in gm]])
_, _, vh = np.linalg.svd(J0, full_matrices=True)
Q0 = vh[2:].T
evals, vectors = np.linalg.eigh(Q0.T @ A0 @ Q0)
X0 = Q0 @ vectors
print("primitive centre eigenvalues", evals[:8], flush=True)

# Freeze tails and solve the two primitive equations in Arb.
head = arb_mat([[gp[0], gp[1]], [gm[0], gm[1]]])
X = arb_mat(N, N - 2)
for col in range(N - 2):
    tail = [arb(repr(float(X0[i, col]))) for i in range(2, N)]
    rhs = arb_mat([
        [-sum((gp[i]*tail[i-2] for i in range(2, N)), arb(0))],
        [-sum((gm[i]*tail[i-2] for i in range(2, N)), arb(0))],
    ])
    solved = head.solve(rhs)
    X[0, col], X[1, col] = solved[0, 0], solved[1, 0]
    for i in range(2, N):
        X[i, col] = tail[i-2]
assert (arb_mat([gp, gm]) * X).contains(arb_mat(2, N - 2))
print("exact two-Tate graph: PASS", flush=True)

D = sub(X, 0, N, 0, ND)
S = sub(X, 0, N, ND, N - 2)

# Native Gamma is required on the delicate columns at the 1e-16 scale.
spec = importlib.util.spec_from_file_location(
    "d147", HERE / "114_d_147_hurwitz_gamma_arb.py"
)
d147 = importlib.util.module_from_spec(spec)
assert spec.loader is not None
print("loading D147 Gamma generator", flush=True)
spec.loader.exec_module(d147)
print("D147 Gamma generator loaded", flush=True)
native_cache = Path(os.environ.get(
    "D219_NATIVE_GAMMA", "/tmp/t6_gamma260_native_strings.npz"
))
if native_cache.exists():
    print("opening native Gamma260", native_cache, flush=True)
    saved = np.load(native_cache, allow_pickle=False)
    assert saved["G"].shape[0] >= N and saved["G"].shape[1] >= N
    saved_digits = int(saved["digits"])
    source_digits = (int(saved["source_digits"])
                     if "source_digits" in saved.files else saved_digits)
    assert source_digits >= DPS and saved_digits >= WORK_DPS
    # Parse directly at the directed matrix precision.  The decimal balls
    # are rounded outward by Arb; retaining 2100 digits during parsing would
    # only slow the dense algebra which is intentionally done at WORK_DPS.
    ctx.dps = WORK_DPS
    print("parsing native Gamma260 balls", flush=True)
    gamma_strings = saved["G"][:N, :N]
    gamma = arb_mat([[arb(str(gamma_strings[i, j])) for j in range(N)]
                     for i in range(N)])
    print("loaded native Gamma260", native_cache, flush=True)
else:
    print("computing native Gamma260", flush=True)
    gamma = d147.exact_gamma_block(N, DPS, T)
    # Preserve Arb textual balls before lowering the working precision.
    # This is a cache, not an originating certificate; D.147 remains the
    # authoritative generator.
    strings = np.array([[str(gamma[i, j]) for j in range(N)]
                        for i in range(N)], dtype=str)
    np.savez_compressed(native_cache, G=strings, digits=np.array(DPS))
    print("saved native Gamma260", native_cache, flush=True)
# The factorial endpoint representation needs DPS digits to construct
# Gamma.  Once that cancellation is enclosed, all remaining pivots are at
# scales >=1e-16; WORK_DPS directed digits are ample and greatly reduce the
# dense-matrix cost.  Lowering ctx.dps only widens existing balls.
assert WORK_DPS >= 100
ctx.dps = WORK_DPS
print("post-Gamma directed matrix digits", WORK_DPS, flush=True)
Bbase = X.transpose()*gamma*X - m0*(X.transpose()*X)
print("native Gamma primitive projection complete", flush=True)

# Native contact balls remove the binary64 radius floor from the safe
# inverse.  The serialized enclosure remains a rigorous fallback.
native_contact = Path(os.environ.get(
    "D219_NATIVE_CONTACT", "/tmp/t6_contact260_native_strings.npz"
))
if native_contact.exists():
    saved_contact = np.load(native_contact, allow_pickle=False)
    assert (saved_contact["C"].shape[0] >= N
            and saved_contact["C"].shape[1] >= N)
    assert int(saved_contact["endpoint"]) == 6
    contact_strings = saved_contact["C"][:N, :N]
    Cball = arb_mat([[arb(str(contact_strings[i, j]))
                      for j in range(N)] for i in range(N)])
    contact_is_native = True
    print("loaded native contact260", native_contact, flush=True)
else:
    Cball = arb_mat(N, N)
    for i in range(N):
        for j in range(N):
            Cball[i, j] = float_ball(contact_file["C"][i, j],
                                     contact_file["R"][i, j])
    contact_is_native = False
    print("using serialized contact260 fallback", flush=True)
Bss = sub(Bbase, ND, N - 2, ND, N - 2) + S.transpose()*Cball*S

# Native contact action on D gives the delicate and mixed blocks without
# paying the serialized 1e-16 floor.
CD = Cball*D if contact_is_native else native_contact_on_delicate(D)
if contact_is_native:
    print("native delicate contact action from cached balls complete", flush=True)
Bdd = sub(Bbase, 0, ND, 0, ND) + D.transpose()*CD
Bds = sub(Bbase, 0, ND, ND, N - 2) + CD.transpose()*S

# Freeze a midpoint whitening; the congruence is exact decimal Arb data.
css = center(Bss)
css = (css + css.T) / 2
print("safe centre first eigenvalues", np.linalg.eigvalsh(css)[:5], flush=True)
L = np.linalg.cholesky(css)
P0 = np.linalg.inv(L.T)
P = arb_mat([[arb(repr(float(P0[i, j]))) for j in range(NS)]
             for i in range(NS)])
Qsafe = P.transpose()*Bss*P
directed_gershgorin(Qsafe, f"safe{NS}")

C = Bds*P
Qinv = Qsafe.inv()
K = Bdd - C*Qinv*C.transpose()
K = (K + K.transpose()) / 2
det = K.det()
print("directed delicate Schur", K, flush=True)
print("directed delicate determinant", det, flush=True)
assert K[0, 0].lower() > 0 and det.lower() > 0

# Bss^{-1} Bsd = P Qsafe^{-1} P^T Bsd.
safe_coeff = -(P*Qinv*(C.transpose()))
Xgraph = D + S*safe_coeff
assert (arb_mat([gp, gm]) * Xgraph).contains(arb_mat(2, ND))

XC = center(Xgraph)
XR = np.array([[float(Xgraph[i, j].rad()) for j in range(ND)]
               for i in range(N)])
XR = np.nextafter(XR + np.abs(np.spacing(XC))/2, np.inf)
KC = center(K)
KR = np.array([[float(K[i, j].rad()) for j in range(ND)]
               for i in range(ND)])
KR = np.nextafter(KR + np.abs(np.spacing(KC))/2, np.inf)
assert np.isfinite(XC).all() and np.isfinite(XR).all()
assert np.isfinite(KC).all() and np.isfinite(KR).all()

save = os.environ.get("D219_SAVE", "/tmp/t6_v260_directed_graph2.npz")
X_native = np.array([[str(Xgraph[i, j]) for j in range(ND)]
                     for i in range(N)], dtype=str)
K_native = np.array([[str(K[i, j]) for j in range(ND)]
                     for i in range(ND)], dtype=str)
np.savez_compressed(save, C=XC, R=XR, K=KC, KR=KR,
         C_native=X_native, K_native=K_native,
         native_digits=np.array(WORK_DPS),
         endpoint=np.array(6), dimension=np.array(N),
         gamma_digits=np.array(DPS),
         work_digits=np.array(WORK_DPS),
         primitive_eigenvalues=evals)
print("max graph coefficient radius", XR.max(), flush=True)
print("saved", save, flush=True)
print(f"D219 DIRECTED V{N} TWO-COLUMN GRAPH: PASS")
