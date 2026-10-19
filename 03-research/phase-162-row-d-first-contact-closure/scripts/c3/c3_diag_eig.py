"""Diagnostic only (not part of the certificate): smallest eigenvalues of the midpoint of S at mu=0."""
import json, mpmath as mp, sys
mp.mp.dps = 50
for p in (0, 1):
    S = json.load(open(f'S_mid_log5_par{p}_tauN240.0.json'))
    M = mp.matrix([[mp.mpf(x) for x in row] for row in S])
    ev = mp.eigsy(M, eigvals_only=True)
    ev = sorted(ev)
    print(p, [mp.nstr(e, 6) for e in ev[:4]])
