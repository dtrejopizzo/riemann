# E77.7ag - Anchor-blindness audit

**Run:** 2026-07-18.

## 1. Purpose

After E77.7af, the singular finite-section LP obstruction split into two
geometric factors:

```text
source factor:  v0^* g,
anchor factor:  r(z0) v0,
```

for the simple zero mode `v0` of the shifted inner block

```text
A = H_inner - mu I.
```

The source factor was reduced to exclusion of a full ground-state eigenvector
with both boundary entries equal to zero.  This note audits the remaining
anchor factor directly on the zeta ladder.

## 2. Probe

Companion:

```text
E77_7ag_anchor_blindness_probe.py
E77_7ag_anchor_blindness_results.json
```

Command:

```bash
python3 E77_7ag_anchor_blindness_probe.py \
  --lambda 6 --max-modes 14 --dps 70
```

For each nested zeta section the probe computes:

```text
1. the smallest inner eigenvalue |lambda0(A)|;
2. the anchor coupling |r(z0)v0| at z0 = i;
3. the complex anchor value itself.
```

## 3. Result

Across the whole critical ladder where the zero mode becomes extremely small,
the anchor factor stays macroscopic:

```text
N= 6: |lambda0| = 7.38e-21, |r(z0)v0| = 0.3976
N=10: |lambda0| = 1.84e-30, |r(z0)v0| = 0.3538
N=12: |lambda0| = 4.28e-35, |r(z0)v0| = 0.3419
N=14: |lambda0| = 2.25e-39, |r(z0)v0| = 0.3332.
```

So the anchor coupling does not merely avoid zero numerically; it remains of
order one while the inner singularity deepens by roughly nineteen orders of
magnitude.

## 4. Reading

This sharply localizes the singular finite-section obstruction.

```text
1. the anchor factor is not the delicate part of the zeta regime;
2. the almost-singular behavior is carried by the inner mode and by the
   characteristic derivative p'_A(0), not by loss of Cauchy normalization;
3. any remaining theorem-grade obstruction is concentrated in the source side
   (equivalently, exclusion of full boundary-zero ground states).
```

Combined with E77.7ae:

```text
det M(z0)
= -p'_A(0) (v0^* g)(r(z0)v0),
```

the audit shows that the zeta determinant collapse is entirely compatible with
healthy anchor normalization.

## 5. Consequence for the live object

The singular LP-interface target can now be sharpened again:

```text
SOURCE-BLINDNESS-EXCLUSION
=> v0^* g != 0
and the anchor audit strongly supports r(z0)v0 != 0.
```

So the only theorem-grade obstruction still not reduced away is:

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE.
```

If that exclusion is proved, then by E77.7af the source factor is nonzero,
and by the macroscopic anchor audit plus E77.7k's normalization gate the
singular fixed-section clause is effectively closed.

## 6. Status

```text
observed:  the anchor coupling |r(z0)v0| stays O(10^-1) throughout the zeta
           singular ladder;
observed:  anchor blindness is not the active obstruction;
refined:   the remaining singular theorem target is source-blindness
           exclusion / no full boundary-zero ground state;
next:      connect that exclusion explicitly to the simplicity/nonvanishing
           gate of E77.7k and decide whether a separate theorem is still
           needed or the obstruction has already been subsumed there.
```
