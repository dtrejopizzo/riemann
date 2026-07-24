# E78.23 - Theta sign stability separates from theta dominance

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.22 reduced sign coherence of `Q_logT` to

```text
THETA-DOMINANCE:
  sign(Q_theta) fixed
  and |Q_theta| > |Q_t0|.                                 (TS-1)
```

The natural next question is whether the `u`-sector law from E77.5ad/E77.5ae
forces all of `(TS-1)` at once.

This note records the honest answer:

```text
no.
```

The `u`-sector law appears to control the **sign** of `Q_theta` much more
robustly than the **dominance ratio** `|Q_theta|/|Q_t0|`.

## 2. The exact split

The sign part and the size part of E78.22 are logically distinct:

```text
THETA-SIGN-STABILITY:
  sign(Q_theta) fixed and compatible with the sign of safe_u;

T0-SMALLNESS:
  |Q_theta| > |Q_t0|.                                     (TS-2)
```

Together these imply E78.22's target, but neither implies the other.

So the correct refinement of E78.22 is

```text
THETA-SIGN-STABILITY + T0-SMALLNESS
=> THETA-DOMINANCE
=> sign coherence of Q_logT.                              (TS-3)
```

## 3. Probe audit

Companion:

```text
E78_23_theta_sign_vs_dominance_probe.py
E78_23_theta_sign_vs_dominance_results.json
```

The probe compares, on the audited `sigma in {1,3}` rows:

```text
- sign compatibility between safe_u and Q_theta;
- dominance of |Q_theta| over |Q_t0|.
```

Recall from E77.5ac that `safe_u = 2 Re(iu)`, so on the zeta sector
`safe_u < 0` is the expected sign carrier for positive `Q_theta`.

## 4. Results

### Zeta

```text
theta-sign-from-u count      = 12
theta-sign-from-u fails      = 0
theta-dominance count        = 12
theta-dominance fails        = 0.                          (TS-4)
```

So on the audited zeta ladder both parts hold.  But their numerical behavior is
different:

```text
- sign compatibility is perfect;
- dominance ratios range widely, from 5.324 to 9.252.     (TS-5)
```

That is already a hint that sign stability is the more rigid object.

### Planted build

```text
theta-sign-from-u count      = 8
theta-sign-from-u fails      = 4
theta-dominance count        = 5
theta-dominance fails        = 7.                          (TS-6)
```

So the planted build breaks the two clauses differently:

```text
- it sometimes loses the sign relation between safe_u and Q_theta;
- it loses dominance even more often.                      (TS-7)
```

This is exactly what one would expect if the `u`-sector governs sign first,
while the size comparison against `Q_t0` is a separate burden.

## 5. Consequence

This gives a cleaner roadmap for the next theorem-grade work:

```text
1. derive THETA-SIGN-STABILITY from the exact u-sector law;
2. treat T0-SMALLNESS as the remaining quantitative comparison problem. (TS-8)
```

That is a real simplification.  It prevents us from over-asking the `u`-sector
certificate to prove more than it structurally carries.

## 6. Honest reading

This note is deliberately an autopsy-grade refinement, not a closure claim.

What it proves:

```text
the current E78.22 target naturally splits into a sign problem and a size
problem, and the available Phase-77 evidence supports that split strongly.
```

What it does **not** prove:

```text
that THETA-SIGN-STABILITY alone implies T0-SMALLNESS,
or that the u-sector law by itself yields the full dominance ratio.
```

That negative information is useful. It tells us where not to waste time.

## 7. Status

```text
proved:
  E78.22 decomposes naturally into THETA-SIGN-STABILITY plus T0-SMALLNESS;

observed:
  on audited zeta rows, both clauses hold;

observed:
  on the planted build, sign compatibility fails on fewer rows than dominance,
  indicating that the sign burden is genuinely easier/more rigid than the size
  burden;

reduced:
  the next front from full THETA-DOMINANCE to the pair
    THETA-SIGN-STABILITY
    T0-SMALLNESS;

next:
  derive THETA-SIGN-STABILITY from the exact u-sector/cell identities and keep
  T0-SMALLNESS as the separate quantitative target.
```
