#!/usr/bin/env python3
"""Binary64 FFT atlas for the D.222 corrected residual.

This script is a falsifier/sizing tool only.  It applies the complete T6
multiplier to the exact-Green corrected source saved by D.222, removes the
measured V260 polynomial projection, and reports the residual Gram relative
to the old safe energy.  No output is an interval certificate.
"""
from __future__ import annotations

import os
import numpy as np


T = .5*np.log(6.0)


def digamma_complex(z: np.ndarray) -> np.ndarray:
    z = np.asarray(z, dtype=np.complex128)
    w = z + 20.0
    out = (
        np.log(w) - 1/(2*w) - 1/(12*w**2) + 1/(120*w**4)
        - 1/(252*w**6) + 1/(240*w**8) - 5/(660*w**10)
        + 691/(32760*w**12) - 1/(12*w**14)
    )
    for j in range(20):
        out -= 1/(z+j)
    return out


def synthesize(u: np.ndarray, coeff: np.ndarray) -> np.ndarray:
    nmax = coeff.shape[0]
    p0 = np.ones_like(u)
    ans = np.sqrt(1/(2*T))*p0[:, None]*coeff[0]
    if nmax == 1:
        return ans
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


points = int(os.environ.get("D223_POINTS", str(2**16)))
box = float(os.environ.get("D223_BOX", "32"))
batch = int(os.environ.get("D223_BATCH", "12"))
src = np.load(os.environ.get(
    "D223_SOURCE", "/tmp/t6_finite_green_capacity_rho009_arb.npz"
))
F = np.asarray(src["corrected_source_c"])
PB = np.asarray(src["old_whitener"])
F = F@PB
N, width = F.shape
assert (N, width) == (260, 196)
maxcut = int(os.environ.get("D223_MAXCUT", "600"))
assert maxcut >= N

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

acted_inside = np.empty((len(inside), width))
source_inside = synthesize(u, F)
for start in range(0, width, batch):
    stop = min(start+batch, width)
    functions = np.zeros((points, stop-start))
    functions[inside] = source_inside[:, start:stop]
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
    print("acted", start, stop, flush=True)

# Stable measured polynomial projections.  QR avoids the badly conditioned
# normal equations of the uniform-grid Legendre Gram.  These are diagnostics
# on the fixed W260-corrected source; enlarging the exact Green trial space
# can only be assessed by a subsequent directed rebuild.
basis = synthesize(u, np.eye(maxcut))
q, _ = np.linalg.qr(basis, mode="reduced")
cutoffs = sorted(set([N, 320, 400, maxcut]))
cutoffs = [n for n in cutoffs if n <= maxcut]
spectra = []
grams = []
for cutoff in cutoffs:
    qc = q[:, :cutoff]
    residual = acted_inside-qc@(qc.T@acted_inside)
    H = dx*(residual.T@residual)
    H = (H+H.T)/2
    eig = np.linalg.eigvalsh(H)
    spectra.append(eig)
    grams.append(H)
    print("cutoff", cutoff, "residual top", eig[-1],
          "target ratio", eig[-1]/.134139, flush=True)
print("grid points/inside/dx", points, len(inside), dx)

np.savez(
    os.environ.get("D223_SAVE", "/tmp/t6_corrected_residual_fft.npz"),
    residual_grams=np.array(grams),
    eigenvalues=np.array(spectra),
    cutoffs=np.array(cutoffs),
    points=np.array(points), box=np.array(box), dx=np.array(dx),
)
print("D223 DIAGNOSTIC ONLY")
