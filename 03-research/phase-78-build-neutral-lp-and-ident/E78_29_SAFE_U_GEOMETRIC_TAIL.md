# E78.29 - Geometric envelope gives a summable tail for `Delta safe_u`

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.28 named the strongest current one-dimensional sign target:

```text
SAFE-U-GEOMETRIC-ENVELOPE:
  0 < A_{N+2} <= rho_* A_N,                               (GT-1)
```

with

```text
A_N := N Delta safe_u_N,                                  (GT-2)
rho_* < 1.                                                (GT-3)
```

This note records the exact transfer that makes `(GT-1)` useful beyond the sign
front itself:

```text
it gives a geometric tail bound for Delta safe_u.         (GT-4)
```

## 2. Exact implication

From `(GT-2)`,

```text
Delta safe_u_N = A_N / N.                                 (GT-5)
```

If `(GT-1)` holds from some starting index onward, then iterating gives

```text
A_{N+2k} <= rho_*^k A_N.                                  (GT-6)
```

Hence

```text
|Delta safe_u_{N+2k}|
 <= rho_*^k A_N / (N+2k).                                 (GT-7)
```

In particular,

```text
sum_{k>=0} |Delta safe_u_{N+2k}|
 <= A_N sum_{k>=0} rho_*^k/(N+2k)
 < infinity.                                              (GT-8)
```

So the geometric envelope implies:

```text
SAFE-U-GEOMETRIC-TAIL:
  the safe-u update sequence is absolutely summable on each parity branch.
                                                             (GT-9)
```

This is exactly the kind of cofinal control that can feed later assembly.

## 3. Consequence for the chain

The sign-side branch therefore refines as

```text
SAFE-U-GEOMETRIC-ENVELOPE
=> SAFE-U-GEOMETRIC-TAIL
=> SAFE-U-CONTRACTION
=> SAFE-U-DECAY
=> THETA-SIGN-STABILITY.                                  (GT-10)
```

This is a real gain: the target is no longer just a sign law, but a summable
law.

## 4. Probe audit

Companion:

```text
E78_29_safe_u_geometric_tail_probe.py
E78_29_safe_u_geometric_tail_results.json
```

The probe does not prove `(GT-8)` theorem-grade, but it records the observed
`rho_*` from E78.28 together with the exact identity `(GT-5)` on the audited
rows.

For zeta, E78.28 gave:

```text
rho_* observed = 0.9122297392646584.                      (GT-11)
```

So the audited sign front is already compatible with a genuine geometric tail
law for `Delta safe_u`.

For the planted build, the envelope fails because positivity fails, so this
transfer is unavailable there.

## 5. Honest reading

This note does **not** prove the envelope itself.  What it proves is that once
the envelope is obtained, the payoff is stronger than before:

```text
not only sign stability, but summability of the safe-u updates. (GT-12)
```

That makes `SAFE-U-GEOMETRIC-ENVELOPE` a much more worthwhile target than a
mere detector: it pushes directly toward the kind of cofinal bounds the final
IDENT assembly will need.

## 6. Status

```text
proved:
  SAFE-U-GEOMETRIC-ENVELOPE implies a geometric tail bound and absolute
  summability for Delta safe_u on each parity branch;

clarified:
  the current sign-side target is strong enough to feed later cofinal assembly,
  not just to certify positivity of Q_theta;

observed:
  the audited zeta rows are compatible with this transfer through the observed
  rho_* from E78.28;

reduced:
  the value of the current target to the stronger transfer object
  SAFE-U-GEOMETRIC-TAIL;

next:
  derive SAFE-U-GEOMETRIC-ENVELOPE theorem-grade from the u-sector law plus the
  exact shell-update formulas for safe_u.
```
