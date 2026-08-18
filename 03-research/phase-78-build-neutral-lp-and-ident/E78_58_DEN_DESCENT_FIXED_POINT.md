# E78.58 - The denominator descent has a fixed point: the centered quadratic core

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

From E78.50 onward, the denominator front has been rewritten several times:

```text
E78.50  centered quadratic inequality in w_N,
E78.52  Euclidean increment lock,
E78.54  cone condition,
E78.55  size-vs-sine lock,
E78.56  scalar gap factorization,
E78.57  inward branch = Re(w_N)<0.                        (DFP-1)
```

This note records the structural fact that these are no longer a true descent.
They all reduce to the same centered quadratic core.

## 2. Fixed-point identity

The core denominator inequality from E78.50 is

```text
CORE_N:
  2 Re(w_N) + |w_N|^2 < 0,                               (DFP-2)
```

with

```text
w_N := Delta d_N / d_N,   d_N := 1-theta_N.              (DFP-3)
```

Every later formulation is exactly equivalent to `(DFP-2)`:

```text
CORE_N
<=> -2<Delta d_N,d_N> > |Delta d_N|^2                    (E78.52)
<=> r_N + 2 c_N < 0                                      (E78.54)
<=> [ c_N<0 and r_N < 2 sqrt(1-s_N^2) ]                  (E78.55)
<=> [ c_N<0 and GAP_N := 2 sqrt(1-s_N^2)-r_N > 0 ]       (E78.56)
<=> [ Re(w_N)<0 and GAP_N > 0 ].                         (DFP-4)
```

Moreover, on the inward branch `Re(w_N)<0`,

```text
GAP_N
 = 2 sqrt(1-s_N^2) - r_N
 = -2 Re(w_N)/|w_N| - |w_N|
 = ( -2 Re(w_N) - |w_N|^2 ) / |w_N|.                     (DFP-5)
```

Since `|w_N|>0`, the sign of `GAP_N` is exactly the sign of the E78.50 core
margin.

So the whole denominator chain after E78.50 has a fixed point:

```text
every later endpoint is the same inequality viewed in different coordinates.
                                                             (DFP-6)
```

## 3. What this means operationally

This is not bad news. It is a very useful stop condition.

It says that the denominator front has already been completely localized. There
is no smaller theorem-grade target to be obtained by reparameterizing

```text
Re(w_N), Im(w_N), r_N, c_N, s_N, GAP_N,
<Delta d_N,d_N>, |Delta d_N|, |d_N|.                     (DFP-7)
```

All of them carry the same remaining content once E78.50 is in hand.

Therefore the next admissible work is no longer “descend the target again”. It
must be one of:

```text
(a) prove a shell law directly for w_N,
(b) prove a shell law directly for Re(w_N),
(c) derive w_N from a previously proved operator/cell identity in a way that
    forces the core sign.                                 (DFP-8)
```

Anything else is a coordinate change, not progress.

## 4. Candid reading

This note is a theorem-grade autopsy, not a new reduction.

It proves that the denominator descent has terminated in a fixed point at
E78.50.

That is valuable because it prevents more budget from being spent on
equivalences that only rename the same burden.

## 5. Status

```text
proved:
  E78.52-E78.57 are all exactly equivalent to the E78.50 centered quadratic
  core 2 Re(w_N)+|w_N|^2<0;

proved:
  on the inward branch, GAP_N has the same sign as the E78.50 core margin;

autopsied:
  the denominator descent has reached a fixed point at E78.50; further descent
  by reparameterization is no longer a legitimate source of new targets;

consequence:
  the next real progress must come from a shell law for w_N or Re(w_N), not
  from another geometric rewrite of the same inequality.
```
