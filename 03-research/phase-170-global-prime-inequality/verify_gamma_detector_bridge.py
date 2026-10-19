#!/usr/bin/env python3
"""Floating consistency checks for R170_702; not a positivity certificate."""
import json
import math
from pathlib import Path
import numpy as np
from verify_coherent_paths import build, prime_powers


def run():
    T, delta, size, rows = 1.0, 0.3, 24, 8
    h = 2*T/size
    edges = np.linspace(-T, T, size+1)
    aa = 2*np.arange(1, rows+1)+0.5

    def moment(a, lo, hi):
        if hi <= lo:
            return 0.0
        return (math.exp(-a*(T+delta+lo)) *
                (-math.expm1(-a*(hi-lo))) / math.sqrt(a*h))

    obs = np.array([[moment(a, lo, hi) for lo, hi in
                     zip(edges[:-1], edges[1:])] for a in aa])

    def collars(cut):
        records = [x for x in prime_powers(math.log(cut+0.5)/2)
                   if x[0] <= cut]
        d = np.zeros(rows)
        exterior = np.zeros_like(obs)
        shifted = np.zeros_like(obs)
        for n, _, weight in records:
            u = math.log(n)
            for m, a in enumerate(aa):
                factor = weight*math.exp(-a*u)
                d[m] += factor
                for j, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
                    exterior[m, j] += factor*moment(a, max(lo, T-u), hi)
                    shifted[m, j] += factor*moment(a, lo, min(hi, T-u))
        return d, exterior, shifted

    d, exterior, shifted = collars(20)
    d2, exterior2, _ = collars(40)
    collar_error = float(np.max(np.abs(shifted-d[:, None]*obs+exterior)))
    outside_error = float(np.max(np.abs(exterior2-exterior-
                                        (d2-d)[:, None]*obs)))
    tail = 0.5*(math.exp(-(4*rows+5)*delta)/(-math.expm1(-4*delta))-
                math.exp(-(4*rows+5)*(delta+2*T))/
                (-math.expm1(-4*(delta+2*T))))
    summed = sum(0.5*math.exp(-2*(2*m+0.5)*delta)*
                 (-math.expm1(-4*(2*m+0.5)*T)) for m in range(rows+1, 1000))

    # Separate finite matrix algebra check. Here the collar is the matrix
    # defect D R - R U, not the continuum collar projected onto step cells.
    model = build(T, size)
    distance = (np.arange(size)[:, None]-np.arange(size)[None, :])*h
    U = sum(weight*np.maximum(0, 1-np.abs(distance-math.log(n))/h)
            for n, _, weight in prime_powers(T))
    c = 2*np.diff(np.sinh(edges/2))/math.sqrt(h)
    s = 2*np.diff(np.cosh(edges/2))/math.sqrt(h)
    polar = 2*np.outer(c, c)-2*np.outer(s, s)
    W = model['W']
    M = W+U+U.T-polar
    G = obs.T@obs
    S = G+G[::-1, ::-1]
    defect = d[:, None]*obs-obs@U
    parity_results = []
    for parity in (1, -1):
        basis = np.zeros((size, size//2))
        for j in range(size//2):
            basis[j, j] = 1/math.sqrt(2)
            basis[size-1-j, j] = parity/math.sqrt(2)
        vals, vecs = np.linalg.eigh(basis.T@W@basis)
        f = basis@vecs[:, 0]
        rf = obs@f
        forcing = -polar@f
        Q = (2*rf@(obs@U.T@f)-2*rf@(defect@f)-
             f@M@S@f+forcing@S@f)
        expected = -2*np.sum((d+vals[0])*rf**2)
        parity_results.append({'parity': parity,
                               'balance_error': float(abs(Q-expected)),
                               'polar_term': float(forcing@S@f)})
    result = {'status': 'floating algebra diagnostics, not continuum certification',
              'continuum_collar_error': collar_error,
              'exterior_cancellation_error': outside_error,
              'HS_tail': tail, 'HS_tail_series_error': abs(tail-summed),
              'finite_matrix_complete_balance': parity_results}
    assert collar_error < 1e-12 and outside_error < 1e-12
    assert abs(tail-summed) < 1e-14
    assert all(x['balance_error'] < 1e-11 for x in parity_results)
    return result


if __name__ == '__main__':
    result = run()
    Path(__file__).with_name('gamma_detector_bridge_diagnostics.json').write_text(
        json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
