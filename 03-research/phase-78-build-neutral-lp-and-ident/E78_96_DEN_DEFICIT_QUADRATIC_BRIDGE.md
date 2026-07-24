# E78.96 - The denominator deficit is exactly a normalized quadratic margin

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.95 reduced the live modulus-growth burden to the one-sided comparison

```text
DENOMINATOR-RADIAL-DEFICIT_N > NUMERATOR-LOSS_N.        (DQB-1)
```

The denominator side was already known to equal radial contraction of
`d_N := 1-theta_N` (E78.47). This note rebuilds the denominator quadratic law
directly on the same Phase-77 `old/new` shell pairing used by E78.94-E78.95, so
there is no ambiguity about indexing or transport.

## 2. Exact bridge

Using the current shell pairing, define

```text
q_b,N := d_N+2 / d_N,                                    (DQB-2)
w_b,N := q_b,N - 1.                                      (DQB-3)
```

Then

```text
q_b,N = 1 + w_b,N,                                       (DQB-4)
```

so

```text
DENOMINATOR-RADIAL-DEFICIT_N
 = 1 - |q_b,N|
 = 1 - |1+w_b,N|.                                        (DQB-5)
```

Multiply numerator and denominator by `1+|1+w_b,N|`:

```text
1 - |1+w_b,N|
 = [1 - |1+w_b,N|^2] / [1 + |1+w_b,N|].                 (DQB-6)
```

Expanding the square gives

```text
|1+w_b,N|^2 - 1 = 2 Re(w_b,N) + |w_b,N|^2,              (DQB-7)
```

hence

```text
DENOMINATOR-RADIAL-DEFICIT_N
 = -(2 Re(w_b,N) + |w_b,N|^2) / (1 + |q_b,N|).         (DQB-8)
```

Equivalently, with

```text
NEGATIVE-QUADRATIC-MARGIN_N
 := -(2 Re(w_b,N) + |w_b,N|^2),                         (DQB-9)
```

we have the exact identity

```text
DENOMINATOR-RADIAL-DEFICIT_N
 = NEGATIVE-QUADRATIC-MARGIN_N / (1 + |q_b,N|).        (DQB-10)
```

So the denominator deficit is exactly a local quadratic margin divided by a
benign positive factor on the same quotient object that already drives the
current denominator chain.

## 3. Consequence for the live target

Substituting `(DQB-10)` into E78.95 yields the stronger sufficient condition

```text
NEGATIVE-QUADRATIC-MARGIN_N
 > (1 + |q_b,N|) NUMERATOR-LOSS_N.                      (DQB-11)
```

Indeed, `(DQB-11)` implies

```text
DENOMINATOR-RADIAL-DEFICIT_N > NUMERATOR-LOSS_N,        (DQB-12)
```

which by E78.95 forces `U-RADIAL-GAP_N > 0`.

This is an admissible upward implication:

```text
QUADRATIC-MARGIN-DOMINANCE
=> DENOMINATOR-DEFICIT-DOMINANCE
=> U-RADIAL-GAP-LOWER-BOUND
=> LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT.             (DQB-13)
```

## 4. Probe audit

Companion:

```text
E78_96_den_deficit_quadratic_bridge_probe.py
E78_96_den_deficit_quadratic_bridge_results.json
```

### Exactness

The reconstruction `(DQB-10)` matches the certified denominator deficit to
roundoff on both builds:

```text
max reconstruction error < 1e-15.                       (DQB-14)
```

### Zeta

Across the certified zeta ladder:

```text
1 + |q_b,N|                  in [1.125517, 1.694602],
NEGATIVE-QUADRATIC-MARGIN_N  in [0.983992, 1.266852].  (DQB-15)
```

Representative late row:

```text
sigma=1.0, N=20:
  negative quadratic margin    = 0.983992
  1+|q_b|                      = 1.126754
  denominator deficit          = 0.873246
  numerator loss               = 0.720711
  quadratic_minus_weighted_loss= 0.171768.             (DQB-16)
```

So the denominator mechanism itself is not merely healthy: on the current
audited zeta rows the stronger weighted dominance law `(DQB-11)` already holds.

### Planted build

The planted build breaks the mechanism at the denominator stage itself: the
normalizing factor stays positive, but the quadratic margin can turn strongly
negative because the shell quotient points outward.

## 5. Honest reading

This note does **not** prove the cofinal dominance law `(DQB-11)`.

What it proves is more structural:

```text
DENOMINATOR-RADIAL-DEFICIT
 = normalized local quadratic margin of the shell quotient w_b,N. (DQB-17)
```

So the healthy half of the front is now fully local and algebraic. The only
remaining burden is to prove the weighted dominance law cofinally, or to reduce
the weighted numerator side to an even smaller exact scalar.

## 6. Status

```text
proved:
  the denominator radial deficit equals the negative quadratic residual of the
  shell denominator quotient, divided by the positive factor 1+|q_b,N|;

proved:
  this yields the admissible stronger target
  NEGATIVE-QUADRATIC-MARGIN > (1+|q_b|) NUMERATOR-LOSS;

observed:
  on the certified zeta ladder the stronger weighted dominance law already
  holds row-by-row, while the planted build fails at the denominator stage;

clarified:
  the denominator side is now completely reduced to a local shell quadratic
  margin, and the real live burden is to make that weighted dominance cofinal;

next:
  isolate a theorem-grade lower bound for the negative quadratic margin, or a
  theorem-grade upper bound for the weighted numerator loss.
```
