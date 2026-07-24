# E78.65 - Naive transfer-ratio reanchoring of `PAIRNUM_N` fails on the current certified artifacts

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.64 showed that the real shell numerator

```text
PAIRNUM_N = -Re((A_N+B_N+C_N) conj(1-theta_N))           (TRP-1)
```

does **not** collapse to the sigma-derivative objects `Delta safe_u_N` or
`Q_theta,N`.

The next natural question is whether this shell numerator can be re-anchored in
the partition-invariant transfer language from E77.5k-E77.5l.

The exact shell identity from E77.5g is

```text
T_N = t0_N (1-theta_N).                                  (TRP-2)
```

So define the transfer ratio

```text
q_N := T_N/t0_N = 1-theta_N.                             (TRP-3)
```

The natural next attempt is to rewrite `PAIRNUM_N` directly in terms of the
consecutive transfer ratios `q_N, q_{N+2}` pulled from the certified
`E77.5ac` rows.

This note records what actually happens on the current artifacts.

## 2. Exact polarization identity

Formally, if the cocycle normalization and the stored `1-theta_N` rows were
aligned in the naive way, one would expect

```text
PAIRNUM_N
 ?= Re((q_N-q_{N+2}) conj(q_N)),                         (TRP-4)
```

and therefore the quadratic polarization

```text
2 Re((x-y) conj x) = |x|^2 - |y|^2 + |x-y|^2.           (TRP-5)
```

With `x=q_N`, `y=q_{N+2}`, this would give the candidate identity

```text
PAIRNUM_N
 ?= ( |q_N|^2 - |q_{N+2}|^2 + |q_N-q_{N+2}|^2 ) / 2.    (TRP-6)
```

The point of this note is that `(TRP-4)`-`(TRP-6)` do **not** match the current
certified Phase-78 numerator data.

## 3. Consequence

So this is **not** a genuine bridge yet. It is a failed shortcut audit.

```text
PAIRNUM-SIGN
 -/-> naive quadratic contraction law for q_N from the current E77.5ac rows.
                                                            (TRP-7)
```

What fails is not arithmetic precision. It is the identification itself.

## 4. Probe audit

Companion:

```text
E78_65_transfer_ratio_polarization_probe.py
E78_65_transfer_ratio_polarization_results.json
```

Using the certified common ladder and the stored `1-theta_N` values from
E77.5ac, the candidate reconstruction `(TRP-6)` fails badly:

```text
zeta:   max reconstruction error = 2.874e-2,
plant:  max reconstruction error = 2.173e2.              (TRP-8)
```

Representative zeta row (`sigma=1.0, N=10`):

```text
|q_10|         = 0.2746755110
|q_12|         = 0.1175228107
|q_10-q_12|    = 0.1571532110
PAIRNUM_10     = 0.0146442701
candidate value = 0.0431660785.                          (TRP-9)
```

The same mismatch persists across the whole common ladder and explodes on the
planted build.

## 5. Honest reading

This note is an autopsy, not a reduction.

It proves that the **naive** identification of the E78 numerator with the
quadratic polarization of the stored `q_N=1-theta_N` rows is not justified by
current evidence. So there is a missing normalization/alignment step between:

```text
the E77.5i cocycle normalization,
the E77.5ac stored shell rows,
the E78 pairnum numerator.                               (TRP-10)
```

So the admissible next step is narrower and more honest:

```text
TRANSFER-RATIO-ALIGNMENT:
  derive the exact relation between the cocycle normalization used in E77.5i
  and the stored shell-transfer ratio rows from E77.5ac/E77.5g before trying
  to rewrite PAIRNUM_N in transfer-ratio form.           (TRP-11)
```

## 6. Status

```text
proved:
  the naive transfer-ratio polarization candidate can be tested directly on the
  current certified artifacts;

observed:
  that candidate fails by order `1e-2` on zeta and catastrophically on the
  plant;

autopsied:
  PAIRNUM_N does not yet admit a justified direct rewrite through the stored
  `q_N=1-theta_N` rows without an additional alignment theorem;

reduced:
  the next legitimate target to TRANSFER-RATIO-ALIGNMENT.
```
