# E78.92 - The weighted modulus quotient is exactly a prefactor divided by `U-RADIAL-GAP`

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.91 identified the exact shell-growth source

```text
U-RADIAL-GAP_N
 := |q_a,N| - |q_b,N|,                                  (WGS-1)
```

with

```text
|u_N+2| - |u_N|
 = |u_N| (|q_a,N|-|q_b,N|) / |q_b,N|.                  (WGS-2)
```

This note substitutes that identity into the weighted modulus quotient and
removes the last unnamed modulus-difference scalar.

## 2. Exact split

From E78.88,

```text
W_N(sigma)
 := N * MODULUS-QUOTIENT_N(sigma)
 = N * (-SAFEDELTA_N(i sigma))
   / [2 (|u_N+2|-|u_N|) s_N+2],                         (WGS-3)
```

where

```text
s_N+2 = Im(u_N+2)/|u_N+2|.                              (WGS-4)
```

Using `(WGS-2)` gives the exact identity

```text
WEIGHTED-GAP-SPLIT:
W_N(sigma)
 = PREF_N(sigma) / U-RADIAL-GAP_N(sigma),               (WGS-5)
```

with

```text
PREF_N(sigma)
 := N * (-SAFEDELTA_N(i sigma)) * |q_b,N|
    / [2 |u_N| s_N+2].                                  (WGS-6)
```

So the entire weighted modulus front is now factored into:

```text
explicit numerator prefactor
/
explicit radial gap.                                    (WGS-7)
```

No hidden modulus-difference object remains.

## 3. Probe audit

Companion:

```text
E78_92_weighted_gap_split_probe.py
E78_92_weighted_gap_split_results.json
```

### Exactness

The split reconstructs to roundoff:

```text
max reconstruction error < 2e-15.                       (WGS-8)
```

### Zeta size on the certified ladder

Across the certified zeta rows:

```text
PREF_N
  min    = 0.017141,
  median = 0.077307,
  max    = 0.294841,                                    (WGS-9)

U-RADIAL-GAP_N
  min    = 0.152534,
  median = 0.371460,
  max    = 0.921090,                                    (WGS-10)

W_N
  min    = 1.935488,
  median = 2.361624,
  max    = 2.586236.                                    (WGS-11)
```

Representative rows:

```text
sigma=1.0, N= 8:
  prefactor   = 0.294841
  gap         = 0.921090
  W_N         = 2.560798

sigma=1.0, N=12:
  prefactor   = 0.101795
  gap         = 0.472324
  W_N         = 2.586236

sigma=1.0, N=20:
  prefactor   = 0.017141
  gap         = 0.152534
  W_N         = 2.247475.                               (WGS-12)
```

So the endpoint weighted modulus quotient is literally the ratio of two
explicit positive shell quantities.

## 4. Consequence

This gives the sharpest current endpoint reduction:

```text
PREF-CONTROL
+ U-RADIAL-GAP-LOWER-BOUND
=> LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT.             (WGS-13)
```

More explicitly, any theorem-grade bounds

```text
PREF_N(1.0) <= A_*,                                     (WGS-14)
U-RADIAL-GAP_N(1.0) >= g_* > 0                          (WGS-15)
```

would imply

```text
W_N(1.0) <= A_* / g_*.                                  (WGS-16)
```

That is a genuine upward implication, so the reduction is admissible.

## 5. Candid reading

This note does **not** yet prove either `(WGS-14)` or `(WGS-15)` cofinally.

What it proves is that the left-endpoint weighted modulus quotient has now been
reduced to a quotient of two named positive shell objects, one of which
(`U-RADIAL-GAP`) already separates zeta from the planted falsifier exactly at
the source of the growth law.

That is strictly sharper than carrying `W_N(1.0)` as a black-box constant
envelope target.

## 6. Status

```text
proved:
  the weighted modulus quotient is exactly PREF_N / U-RADIAL-GAP_N;

proved:
  the split reconstructs to roundoff on the certified zeta ladder;

clarified:
  the endpoint weighted modulus burden is now localized to
  PREF-CONTROL plus a lower bound on U-RADIAL-GAP;

reduced:
  LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT to
  PREF-CONTROL + U-RADIAL-GAP-LOWER-BOUND;

next:
  decide which side is genuinely stiffest on the audited ladder, and attack it
  directly rather than carrying the quotient W_N as a monolith.
```
