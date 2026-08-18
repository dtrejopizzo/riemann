#!/usr/bin/env python3
"""FFT atlas of exact-Galerkin Green capacity versus cutoff at T6.

The trial bands are the primitive orthogonal complements of V200 in VM,
constructed by the same two-by-two Tate Gram solve as D.222.  The complete
Gamma/contact multiplier is applied on a full-line FFT chart.  This is
binary64 numerical evidence only and selects the next directed cutoff.
"""
from __future__ import annotations

import os
import numpy as np
from flint import arb, ctx


ctx.dps = 80
T = .5*np.log(6.0)
N0 = 200


def digamma_complex(z: np.ndarray) -> np.ndarray:
    z = np.asarray(z, dtype=np.complex128)
    w = z+20
    out = (
        np.log(w)-1/(2*w)-1/(12*w**2)+1/(120*w**4)
        -1/(252*w**6)+1/(240*w**8)-5/(660*w**10)
        +691/(32760*w**12)-1/(12*w**14)
    )
    for j in range(20):
        out -= 1/(z+j)
    return out


def synthesize(u: np.ndarray, coeff: np.ndarray) -> np.ndarray:
    nmax = coeff.shape[0]
    p0 = np.ones_like(u)
    ans = np.sqrt(1/(2*T))*p0[:, None]*coeff[0]
    p1 = u.copy()
    ans += np.sqrt(3/(2*T))*p1[:, None]*coeff[1]
    for n in range(2, nmax):
        p = ((2*n-1)*u*p1-(n-1)*p0)/n
        ans += np.sqrt((2*n+1)/(2*T))*p[:, None]*coeff[n]
        p0, p1 = p1, p
    return ans


def shifted(values: np.ndarray, x: np.ndarray,
            targets: np.ndarray) -> np.ndarray:
    dx = x[1]-x[0]
    pos = (targets-x[0])/dx
    left = np.floor(pos).astype(np.int64)
    frac = pos-left
    valid = (left >= 0) & (left+1 < len(x))
    out = np.zeros((len(targets), values.shape[1]))
    idx = left[valid]
    out[valid] = ((1-frac[valid, None])*values[idx]
                  + frac[valid, None]*values[idx+1])
    return out


def tate(n: int, sign: int) -> float:
    tt = arb(6).log()/2
    k = tt/2
    value = (2*arb.pi()/k).sqrt()*k.bessel_i(arb(2*n+1)/2)
    if sign < 0 and n % 2:
        value = -value
    value *= (tt*arb(2*n+1)/2).sqrt()
    return float(value.mid())


maxcut = int(os.environ.get("D224_MAXCUT", "600"))
points = int(os.environ.get("D224_POINTS", str(2**16)))
box = float(os.environ.get("D224_BOX", "32"))
batch = int(os.environ.get("D224_BATCH", "12"))
src = np.load(os.environ.get(
    "D224_SOURCE", "/tmp/t6_finite_green_capacity_rho009_arb.npz"
))
S0 = np.asarray(src["safe_source_c"])
PB = np.asarray(src["old_whitener"])
S = np.zeros((maxcut, S0.shape[1]))
S[:S0.shape[0]] = S0
S = S@PB

gp = np.array([tate(n, 1) for n in range(maxcut)])
gm = np.array([tate(n, -1) for n in range(maxcut)])
G = np.array([[gp[:N0]@gp[:N0], gp[:N0]@gm[:N0]],
              [gm[:N0]@gp[:N0], gm[:N0]@gm[:N0]]])
W = np.zeros((maxcut, maxcut-N0))
for n in range(N0, maxcut):
    a, b = np.linalg.solve(G, -np.array([gp[n], gm[n]]))
    W[:N0, n-N0] = a*gp[:N0]+b*gm[:N0]
    W[n, n-N0] = 1
print("Tate residual norms", np.linalg.norm(gp@W), np.linalg.norm(gm@W))
print("source-band orthogonality", np.linalg.norm(S.T@W, ord=2))

dx = box/points
x = (np.arange(points)-points//2)*dx
inside = np.flatnonzero(np.abs(x) <= T)
xin = x[inside]
u = xin/T
freq = 2*np.pi*np.fft.rfftfreq(points, d=dx)
psi_q = digamma_complex(np.array([.25]))[0].real
symbol = digamma_complex(.25+.5j*freq).real-psi_q
m0 = np.log(np.pi)-psi_q
contacts = ((2, np.log(2.)), (3, np.log(3.)),
            (4, np.log(2.)), (5, np.log(5.)))


def apply(coeff: np.ndarray, name: str) -> tuple[np.ndarray, np.ndarray]:
    values = synthesize(u, coeff)
    acted_inside = np.empty_like(values)
    for start in range(0, coeff.shape[1], batch):
        stop = min(start+batch, coeff.shape[1])
        functions = np.zeros((points, stop-start))
        functions[inside] = values[:, start:stop]
        acted = np.fft.irfft(
            np.fft.rfft(functions, axis=0)*symbol[:, None],
            n=points, axis=0,
        )
        acted -= m0*functions
        for n, mangoldt in contacts:
            d = np.log(float(n))
            weight = mangoldt/np.sqrt(float(n))
            acted[inside] -= weight*(
                shifted(functions, x, xin+d)
                + shifted(functions, x, xin-d)
            )
        acted_inside[:, start:stop] = acted[inside]
        print(name, start, stop, flush=True)
    return values, acted_inside


Sv, AS = apply(S, "safe")
Wv, AW = apply(W, "band")
B = dx*(Sv.T@AS)
B = (B+B.T)/2
Eall = dx*(Wv.T@AW)
Eall = (Eall+Eall.T)/2
Call = dx*(Sv.T@AW)
be = np.linalg.eigvalsh(B)
print("measured safe block range", be[[0, -1]])
calibration = np.linalg.norm(B-np.eye(B.shape[0]), ord=2)
print("safe-block calibration error", calibration, flush=True)
if calibration > .05:
    np.savez(
        os.environ.get("D224_SAVE", "/tmp/t6_green_cutoff_atlas.npz"),
        safe_block=B, calibration_error=np.array(calibration),
        points=np.array(points), box=np.array(box), dx=np.array(dx),
    )
    print("D224 REJECTED: FFT calibration does not resolve the exact safe block")
    raise SystemExit(0)

cutoffs = [n for n in (260, 320, 400, 500, maxcut)
           if N0 < n <= maxcut]
tops = []
for cutoff in sorted(set(cutoffs)):
    k = cutoff-N0
    E = Eall[:k, :k]
    C = Call[:, :k]
    cap = C@np.linalg.solve(E, C.T)
    cap = (cap+cap.T)/2
    L = np.linalg.cholesky(B)
    M = np.linalg.solve(L, cap)
    M = np.linalg.solve(L, M.T).T
    top = np.linalg.eigvalsh((M+M.T)/2)[-1]
    tops.append(top)
    print("cutoff", cutoff, "finite Green capacity", top, flush=True)

np.savez(
    os.environ.get("D224_SAVE", "/tmp/t6_green_cutoff_atlas.npz"),
    cutoffs=np.array(sorted(set(cutoffs))), capacities=np.array(tops),
    safe_block=B, band_block=Eall, cross=Call,
    points=np.array(points), box=np.array(box), dx=np.array(dx),
)
print("D224 DIAGNOSTIC ONLY")
