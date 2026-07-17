# E67.13 -- AUDIT of the root-of-unity realization: contamination + fabrication

**Date:** 2026-07-06.
**Script:** [E67_13_audit_qartifacts.py](E67_13_audit_qartifacts.py).
**Role:** audit WHY E67.12 failed, before building on top of it (solid-step discipline).

## Finding

At `q=e^{i pi/ell}` (z0=100-i, y=1, N=16), two independent pathologies:

1. **Contamination (artifact floor).** The BARE Shapovalov form (no prime data, no zeros) already has
   `ind_- > 0` for ell=11,17 (`bare=1`): pure `[m]_q<0` q-arithmetic, unrelated to RH.

2. **Fabrication (false positive for zeta).** Worse: at **ell=13**, `bare=0` but `zeta-twist=4`. The
   diagonal twist manufactures 4 negative directions for zeta, whose correct RH index is **0**. A
   faithful certificate must return exactly the floor for zeta; it returns floor+4. **Not faithful.**

Not even monotone: ell=7,c=0.5 gives `off-bare=+0` while `zeta-bare=+1` (off < zeta), the wrong order
for a detector.

## Verdict

The root-of-unity Shapovalov realization with a **diagonal** twist is NOT a faithful signed certificate.
It fails by contamination AND fabrication. This is structural, not knob-tuning.

## Audit of the whole Phase-67 signed arc

SOLID (classical, q=1):
- E67.9  : `ind_-(A_N - P_lambda) = 0  <=>  RH`, faithful detector. Correct, independent of q-issues.
- E67.11 : on-line zero = 0 negative squares, exact atom.

NOT SOLID (the quantum realization):
- E67.10/12/13 : root of unity as the canonical home -- the diagonal twist contaminates and fabricates.
  The q-realization does NOT turn the detector into a proof.

## Honest distance to Omega_7

We have the right OBJECT (signed index = faithful detector) but NOT the structural FORCING that would
make it a proof. The E67.9 detector COMPUTES `A_N - P_lambda` (which needs zeta); a proof of Omega_7
needs the index forced to 0 by structure, WITHOUT computing the zeros. The root-of-unity form was meant
to supply that forcing; it does not -- it contaminates and fabricates.

Two open constructions remain, both hard (not a script):
1. an OFF-DIAGONAL twist carrying the log-distance coherence (diagonal discards it: E67.8, E67.12);
2. a REGULARIZATION killing the root-of-unity artifacts (tilting / negligible quotient) so that zeta
   returns exactly 0.

Until both are built, Phase 67 has a correct certificate TYPE and a faithful detector, but no
structural forcing -- Omega_7 remains open exactly as in P52/P53. No regression, a sharper map.
