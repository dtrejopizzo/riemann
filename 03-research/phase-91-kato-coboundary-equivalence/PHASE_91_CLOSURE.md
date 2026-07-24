# Phase 91 closure - Coboundary localization of the line current

## 1. Closed mathematics

The resonant line derivative satisfies

```text
C_t dot v_t=Q_tH_P^inv_t.                             (1.1)
```

For every inverse-free candidate `u_t`, the exact decomposition is

```text
Q_tH_P^inv_t=C_tu_t+e_t,

dot v_t=u_t+C_t^(-1)e_t.                             (1.2)
```

After applying the base-point-subtracted Cauchy functional, (1.2) is the
exact split of the projective Kato current into an explicit term and a reduced
leakage term.

## 2. Euler gauge decision

For a general spectral vector,

```text
Av=Z^(-1)delta[(Z-I)v]-(I-Z^(-1))delta v.             (2.1)
```

The last term cannot be discarded.  In the physical interval module,
`ker X={0}`, so a nonzero resonant vector cannot satisfy the ground-vector
hypothesis.  The distributional endpoint mass repairs the algebraic source,
but it does not directly integrate the physical line.

## 3. Closure grade

```text
closed:
  exact line-response equation;
  equivalence with an inverse-free coboundary;
  derivation-defect formula;
  direct ground-vector gauge route;

open and transferred:
  LINE-EULER-COBOUNDARY reduced leakage;
  PROJECTIVE-KATO-EULER;
  RDI-ANCHOR and Omega7.
```

