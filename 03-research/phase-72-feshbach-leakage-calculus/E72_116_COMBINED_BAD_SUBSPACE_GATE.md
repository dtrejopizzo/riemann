# E72.116 -- Combined bad-subspace gate

**Date:** 2026-07-09.
**Role:** unify the mass and energy alignment conditions into one finite orthogonality statement.

## 0. The bad subspace

Fix a physical band `H` and an integer `q`.  Let:

```text
m_x
```

be the mass row of E72.115, and let:

```text
v_1,...,v_q
```

be the first `q` right singular vectors of the shorted pushforward `R_x` from E72.114.  Define:

```text
B_{x,H,q}:=span{ m_x^*/||m_x||, v_1,...,v_q }.
```

Let:

```text
P_{B,x}
```

be the orthogonal projection onto `B_{x,H,q}` in the finite packet space of `Y_x(tau)`.

## 1. Combined gate

### Theorem 72.116

Assume, uniformly for finite root-height windows:

```text
(BNORM)
sup_{tau_j} ||m_x||||Y_x(tau_j)|| = O(1),
sup_{tau_j} sigma_1(R_x)||Y_x(tau_j)|| = O(1),
sup_{tau_j} sigma_{q+1}(R_x)||Y_x(tau_j)|| = O(1),
```

and:

```text
(BORTH)
sup_{tau_j} ||P_{B,x}Y_x(tau_j)||/||Y_x(tau_j)|| -> 0.
```

Then:

```text
MOP holds,
TOP-q holds with o(1),
TAIL-q holds with O(1).
```

Consequently, with `CCGD`, scalar WRL resonance annihilation follows.

### Proof

Mass:

```text
|m_xY_j|
 <= ||m_x||||P_{B,x}Y_j||
 <= ||m_x||||Y_j|| * ||P_{B,x}Y_j||/||Y_j|| -> 0.
```

Top singular energy:

```text
sum_{l<=q} sigma_l^2 |<Y_j,v_l>|^2
 <= sigma_1^2 ||P_{B,x}Y_j||^2
 <= (sigma_1||Y_j||)^2
    (||P_{B,x}Y_j||/||Y_j||)^2 -> 0.
```

Tail:

```text
sum_{l>q} sigma_l^2 |<Y_j,v_l>|^2
 <= sigma_{q+1}^2||Y_j||^2 = O(1).
```

Apply E72.114, E72.115 and E72.113. `QED`

## 2. Explicit discrepancy tests

Every vector `e` in the packet space defines a scalar test against the reflected Chebyshev discrepancy.
Writing:

```text
e=(a_n,b_n)_n
```

for the `sigma` and `dot_sigma` coordinates:

```text
<Y_x(tau),e>
 = int_0^L exp(-i tau r)
   [ sum_n A_n(e)sin(d_nr)+B_n(e)r cos(d_nr) ]
   dE_x^leftarrow(r).                                      (TEST-e)
```

The coefficients `A_n(e),B_n(e)` are the conjugate packet coefficients in the chosen Hilbert
convention.

Therefore `(BORTH)` is an explicit finite family of endpoint discrepancy cancellations:

```text
int_0^L exp(-i tau_j r)T_{x,H,q,a}(r)dE_x^leftarrow(r)
 = o(||Y_x(tau_j)||)
```

for an orthonormal basis `{e_a}` of `B_{x,H,q}`.  This is finite, constructive, and independent of
limiting zeta zeros.

## 3. Diagnostic

The companion script:

```text
E72_116_combined_bad_subspace_probe.py
```

forms:

```text
B_{x,H,3}=span{mass direction, first 3 right singular directions}
```

and reports the relative projection of `Y_x(tau_j)` onto that subspace.

Representative output:

```text
E72.116 combined bad-subspace probe q=3
 lam   N roots dimB  maxProjRatio  maxMassRatio  maxTopEnergy  tailBound
   6  18     3    4    1.568e-01     1.285e-01    3.010e-03  1.274e-02
   8  24     4    4    1.273e-01     8.404e-02    3.873e-03  2.630e-02
  10  28     3    4    9.242e-02     8.166e-02    1.535e-03  1.471e-02
  12  32     4    4    6.286e-02     3.939e-02    5.221e-04  1.822e-02
  14  36     4    4    5.847e-02     5.199e-02    5.336e-04  5.510e-03
```

The combined bad-subspace projection decreases in the tested windows.  The top energy is already
small; the remaining bounded contribution is the singular tail.

## 4. Current final finite statement

The Phase 72 route is now reduced to:

```text
CCGD,
BNORM,
BORTH.
```

All three are finite statements:

```text
CCGD  -> Cauchy-channel physical tail;
BNORM -> size of the mass row, singular values, and Fourier packet;
BORTH -> finitely many explicit endpoint discrepancy tests.
```

## 5. Status

```text
proved: BNORM + BORTH imply MOP and DQF;
proved: BORTH is a finite family of explicit Loewner-Feshbach discrepancy tests;
observed: q=3 bad-subspace projection decreases in tested windows;
open:   prove BNORM and BORTH uniformly, plus CCGD.
```
