# Phase 85 closure - two parity Weyl defects

## 1. Exact reduction

The phase eliminates every unknown cross-cluster matrix element.  The reduced
error is exactly

```text
q^T C^(-1)QD Mg
 =alpha S_q Delta_P^E(lambda_q),  q odd,
 =beta  A_q Delta_P^O(lambda_q),  q even.              (1.1)
```

The functions `Delta_P^E` and `Delta_P^O` are normalized Weyl defects of the
two cluster spectral measures.

On the imaginary safe axis the odd response is real and the even response is
purely imaginary.  They must vanish separately.

## 2. Moving-pole theorem

Interlacing makes the shifted inner spectrum nonnegative.  For a cluster
measure supported in `[0,eta]` and a complementary pole `z>eta`,

```text
m_1/z^2<=-Delta_P(z)<=m_1/[z(z-eta)].                 (2.1)
```

This proves that weak cluster convergence alone is insufficient and exposes
the quadratic moving-pole scale.

## 3. Route decision

Finite exact diagnostics show that the pointwise moving-pole scales can remain
huge while the final safe scalar is already small.  Thus uniform control of
each defect is an over-strong replacement for the theorem.

Phase 85 closes with one irreducible pair:

```text
SIGNED-PW-E,
SIGNED-PW-O,                                          (3.1)
```

the two signed complementary spectral sums of E85.005.

## 4. Closure grade

```text
closed:
  cross-parity matrix elements;
  normalized Weyl representation;
  cross-parity cancellation;
  weak-convergence shortcut;
  uniform moving-pole route;

open and transferred:
  signed Abel cancellation in each parity sector;
  cofinal cluster schedule compatible with that cancellation;
  the outer arithmetic anchor and Omega7.
```

