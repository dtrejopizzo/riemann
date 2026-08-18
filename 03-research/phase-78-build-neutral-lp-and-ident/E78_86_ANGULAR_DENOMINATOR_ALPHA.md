# E78.86 - The angular denominator factor is exactly a one-scalar alpha law

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.85 split the endpoint quotient as

```text
Q_N(sigma)
 = MODULUS-QUOTIENT_N(sigma) * ANGULAR-DEN-FACTOR_N.    (ADA-1)
```

The remaining denominator object was

```text
ANGULAR-DEN-FACTOR_N
 = modulus_share_of_delta_N.                            (ADA-2)
```

This note removes the last geometric ambiguity. The denominator factor is not a
new two-variable mechanism: it is exactly the reciprocal of a single real
scalar built from the already isolated `eps_N` drift.

## 2. Exact alpha law

From E78.33 and E78.85,

```text
angular_term_N = 2 |u_N| (eps_N - eps_N+2),             (ADA-3)
Delta safe_u_N = modulus_term_N + angular_term_N.       (ADA-4)
```

Define

```text
alpha_N
 := angular_term_N / modulus_term_N
  = 2 |u_N| (eps_N - eps_N+2) / modulus_term_N.         (ADA-5)
```

Then

```text
Delta safe_u_N = modulus_term_N (1 + alpha_N),          (ADA-6)
```

so the denominator factor from E78.85 is exactly

```text
ANGULAR-DEN-FACTOR:
ANGULAR-DEN-FACTOR_N
 = 1 / (1 + alpha_N).                                   (ADA-7)
```

Equivalently,

```text
Q_N(sigma)
 = MODULUS-QUOTIENT_N(sigma) / (1 + alpha_N).           (ADA-8)
```

This is the cleanest current form of the quotient branch.

## 3. Immediate envelope

Whenever

```text
|alpha_N| < 1,                                           (ADA-9)
```

the exact reciprocal law gives

```text
1/(1 + |alpha_N|)
 <= ANGULAR-DEN-FACTOR_N
 <= 1/(1 - |alpha_N|).                                  (ADA-10)
```

So any theorem-grade control of `|alpha_N|` immediately yields a theorem-grade
control of the angular denominator factor, with no further geometry.

This sharpens the open target to:

```text
ALPHA-SMALLNESS:
  |alpha_N| <= eta < 1                                  (ADA-11)
```

which implies

```text
ANGULAR-DENOMINATOR-SMALLNESS.                          (ADA-12)
```

## 4. Probe audit

Companion:

```text
E78_86_angular_denominator_alpha_probe.py
E78_86_angular_denominator_alpha_results.json
```

The probe combines the exact `eps_N` data from E78.33 with the quotient split
from E78.85.

### Exactness

Both identities reconstruct to roundoff:

```text
alpha_N
 = 2 |u_N| (eps_N - eps_N+2) / modulus_term_N,          (ADA-13)

ANGULAR-DEN-FACTOR_N
 = 1/(1 + alpha_N).                                     (ADA-14)
```

Numerically:

```text
max alpha reconstruction error   < 3e-17,
max factor reconstruction error  < 3e-16.               (ADA-15)
```

### Zeta size on the certified ladder

Across the currently certified zeta rows:

```text
alpha_N
  min    = -3.7975e-3,
  median = 1.2726e-3,
  max    = 1.7364e-1,                                   (ADA-16)

|alpha_N|
  min    = 5.5662e-5,
  median = 2.6264e-3,
  max    = 1.7364e-1.                                   (ADA-17)
```

Representative rows:

```text
sigma=1.0, N= 8:
  alpha   = -7.3513e-4,
  factor  = 1.000736

sigma=1.0, N=20:
  alpha   =  1.7364e-1,
  factor  = 0.852049.                                   (ADA-18)
```

Every audited zeta row satisfies `|alpha_N| < 1`, so the envelope `(ADA-10)`
holds automatically on the full certified ladder.

## 5. Consequence

The quotient branch is now reduced to:

```text
MODULUS-QUOTIENT
+ ALPHA-SMALLNESS
=> ANGULAR-DENOMINATOR-SMALLNESS
+ MODULUS-QUOTIENT
=> SECTOR-SIZE-QUOTIENT.                                (ADA-19)
```

In other words, the open denominator side is no longer a "polar instability"
problem. It is a one-scalar reciprocal law whose live object is

```text
alpha_N = 2 |u_N| (eps_N - eps_N+2) / modulus_term_N.   (ADA-20)
```

That is a finite, explicit object entirely assembled from already certified
cell data.

## 6. Candid reading

This note does **not** prove a cofinal bound `|alpha_N| <= eta < 1`.

What it does prove is that such a bound would be exactly enough for the full
angular denominator front, and that no further hidden phase bookkeeping
remains.

That is a genuine reduction.

## 7. Status

```text
proved:
  the angular denominator factor is exactly 1/(1+alpha_N);

proved:
  alpha_N is exactly 2|u_N|(eps_N-eps_N+2)/modulus_term_N;

proved:
  the reciprocal reconstruction holds to roundoff on the certified zeta ladder;

observed:
  on the current zeta ladder |alpha_N| stays below 0.1737, with median
  about 2.63e-3;

reduced:
  ANGULAR-DENOMINATOR-SMALLNESS to ALPHA-SMALLNESS;

next:
  attack MODULUS-QUOTIENT and ALPHA-SMALLNESS separately, with the denominator
  side now localized to one explicit scalar ratio.
```
