# E67.12 Results — twisted root-of-unity Shapovalov (model twist): NEGATIVE, informative

**Date:** 2026-07-06.
**Script:** [E67_12_twisted_shapovalov.py](E67_12_twisted_shapovalov.py).

## Test

Twist the discrete-series Shapovalov norms by a MODEL prime weight-shift
`[j+2y-1] -> [j+2y-1 + c*tau_j]`, `tau_j = diag(A_N^{-1/2} P_lambda A_N^{-1/2})_j` (harness-derived
from Lambda(n), not fitted to zeros). At `q=e^{i pi/ell}`, ask: is `ind_-` STABLE in level and does it
separate zeta (0) from a planted off-line zero (>0)?

## Result

- Raw signal is strong: `tau_zeta in [-0.66, 1.0]` (marginal), `tau_off in [-233, 217]` (off-line blows up).
- But the q-form index does NOT regularize:
  - ell=7: zeta ind_-=1 (stable but nonzero), off = 0/2/1; separation inconsistent (-1,+1,0).
  - ell=11,c=1.0: zeta=0 stable, off=3 stable, sep=+3 -- clean, but 1 of 12 knob settings.
  - ell=13,17: zeta ind_- = 4 or 1 with drift.

For almost all `(ell,c)`, zeta's `ind_-` is nonzero and/or unstable, when it should be robustly 0
(RH true). The separation that appears is inherited from the raw magnitude of `tau_off` (+-233 vs +-1),
not created by the Jantzen structure. The q-form merely passes the raw jet through, mostly muddied.

## Verdict: NEGATIVE for the diagonal twist -- and the reason is E67.8

The design error is diagnostic: `tau_j = diag(whitened P_lambda)` uses only the DIAGONAL, which
discards the off-diagonal log-distance coherence that E67.8 identified as the RH content. A diagonal
weight-shift is the incoherent part; it cannot regularize.

Sharpened specification (what the model bought us):

```
The canonical twist CANNOT be a scalar per-level (diagonal) weight shift.
It must be a full OPERATOR deformation carrying the off-diagonal log-distance
coherence, realized inside the q-module.
```

This is E67.8 reappearing in the signed register: the signed certificate TYPE is right (E67.9-E67.11),
but the SAME coherence-transmission problem persists -- how does a canonical q-object carry the
off-diagonal log-distance coherence without fitting?

## Honest state of Phase 67 (signed register)

```
solid : signed index (Jantzen) is the right certificate type        [E67.9-E67.11]
solid : root-of-unity gives intrinsic signed index                  [E67.10]
solid : on-line zero = 0 negative squares (exact atom)              [E67.11]
NEG   : diagonal weight-twist does not regularize / separate         [E67.12 this file]
open  : a coherence-carrying (off-diagonal) OPERATOR twist, canonical
        from Euler, realized in the q-module -- the real heart
```

The recurring obstruction, stated at its sharpest: the RH content is off-diagonal phase coherence
(log-distance). Every canonical algebraic handle tried so far -- positive (Haar/CP) or signed
(diagonal Jantzen) -- either is incoherent (loses it) or would encode it only by fitting. The signed
register secured the right certificate type but not yet a canonical carrier of the coherence.
