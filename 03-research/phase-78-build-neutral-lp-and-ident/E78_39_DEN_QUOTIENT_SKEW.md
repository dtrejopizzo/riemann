# E78.39 - Denominator phase rigidity is a quotient-skew law

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.38 reduced the denominator front to

```text
DEN-PHASE-RIGIDITY:
  |Delta phi_b,N| small,                                  (DQS-1)
```

where `Delta phi_b,N` is the phase increment of the normalized denominator
direction.

This note removes the normalization and rewrites the same target directly in
terms of the raw shell quotient of `1-theta`.

## 2. Exact quotient-skew identity

Set

```text
q_b,N := (1-theta_N+2)/(1-theta_N).                       (DQS-2)
```

Its modulus carries the size drift, but its argument is exactly the denominator
phase step:

```text
Delta phi_b,N = arg(q_b,N).                               (DQS-3)
```

Whenever `Re(q_b,N) != 0`, we therefore have the exact identity

```text
tan(Delta phi_b,N) = Im(q_b,N) / Re(q_b,N).              (DQS-4)
```

Equivalently,

```text
DEN-QUOTIENT-SKEW:
Delta phi_b,N = arctan( Im(q_b,N) / Re(q_b,N) ).          (DQS-5)
```

So denominator phase rigidity is exactly a skew-smallness law for the raw shell
quotient of `1-theta`.

## 3. Probe audit

Companion:

```text
E78_39_den_quotient_skew_probe.py
E78_39_den_quotient_skew_results.json
```

The probe reconstructs `(DQS-5)` directly from the certified `E77.5ac` points.

### Exactness

For both builds:

```text
max phase reconstruction error < 1e-15.                  (DQS-6)
```

So the quotient-skew identity is exact to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0:
  N=10->12  q = 0.4942228848 + 0.0009740449 i
            |phase| = 0.0019708589
            |Im/Re| = 0.0019708615

sigma=3.0:
  N=10->12  q = 0.5150553008 + 0.0030512469 i
            |phase| = 0.0059240458
            |Im/Re| = 0.0059241151.                      (DQS-7)
```

So on the audited zeta ladder the denominator quotient has tiny skew:

```text
the imaginary part is a very small fraction of the real part. (DQS-8)
```

### Planted build

The planted build fails through large quotient skew at early steps:

```text
sigma=1.0:
  N=10->12  q = 7.4534770 + 2.2988077 i,   |Im/Re| = 0.3084...
  N=12->14  q = 0.5419279 + 0.2137902 i,   |Im/Re| = 0.3945...

sigma=3.0:
  N=10->12  q = 7.2386796 + 2.2817796 i,   |Im/Re| = 0.3152...
  N=12->14  q = 0.5187196 + 0.2603806 i,   |Im/Re| = 0.5019.... (DQS-9)
```

So the falsifier fails already at the quotient-skew level, before any further
repackaging.

## 4. Consequence

This gives the smallest denominator reduced target so far:

```text
DEN-QUOTIENT-SKEW-SMALLNESS:
  prove that Im(q_b,N) / Re(q_b,N) stays small cofinally on zeta. (DQS-10)
```

Then

```text
small quotient skew
=> small denominator phase step
=> tiny DIRDEF_b,N
=> small DENDIR_N.                                        (DQS-11)
```

So the denominator chain becomes

```text
DEN-QUOTIENT-SKEW-SMALLNESS
=> DEN-PHASE-RIGIDITY
=> DIRDEF-B-SMALLNESS
=> denominator-direction control.                         (DQS-12)
```

This is a genuine reduction because the live object is now a plain real ratio of
the raw shell quotient components.

## 5. Honest reading

This note does not yet prove quotient-skew smallness cofinally. What it proves
is that denominator phase rigidity is exactly equivalent to a quotient-skew
target for `(1-theta_N+2)/(1-theta_N)`.

That is the cleanest denominator endpoint named so far.

## 6. Status

```text
proved:
  denominator phase rigidity is exactly the smallness of Im(q_b,N)/Re(q_b,N)
  for q_b,N = (1-theta_N+2)/(1-theta_N);

proved:
  the reconstruction holds to roundoff for both builds;

observed:
  zeta has tiny quotient skew on the audited ladder;

observed:
  the planted build has order-10^-1 to order-1 quotient skew at the early
  failing steps;

reduced:
  DEN-PHASE-RIGIDITY to DEN-QUOTIENT-SKEW-SMALLNESS;

next:
  express q_b,N directly from the shell update of 1-theta_N and test whether
  its skew inherits a simpler finite law.
```
