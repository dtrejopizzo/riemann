# E78.64 - `PAIRNUM_N` is not the `Q_theta` / `safe_u` object: the shell-vs-sigma bridge remains open

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.62-E78.63 localized the denominator-side burden to

```text
PAIRNUM_N := -Re((A_N+B_N+C_N) conj(1-theta_N)).         (PNQ-1)
```

Phase 77 had already localized the theta-logderivative sign geometry to

```text
Q_theta,N
 = N^2 ( N Delta safe_u_N - (N+2) Delta safe_u_{N+2} ),  (PNQ-2)
```

with

```text
safe_u_N = 2 Re(iu_N),
u_N = -theta'_N/(1-theta_N).                              (PNQ-3)
```

Because both objects come from the same `theta/(1-theta)` front, it is natural
to ask whether `PAIRNUM_N` is secretly just `Delta safe_u_N`, or `Q_theta,N`,
or a harmless scalar multiple of one of them.

This note audits that shortcut.

## 2. What the exact identities do and do not say

The exact identities already proved are:

```text
PAIRNUM_N
 = |1-theta_N|^2 Re( -(A_N+B_N+C_N)/(1-theta_N) )        (E78.62)
 = -Re(Delta theta_N conj(1-theta_N)),                   (PNQ-4)
```

so `PAIRNUM_N` is a **shell-direction bilinear pairing**.

By contrast,

```text
Q_theta,N
 = N^2 ( N Delta safe_u_N - (N+2) Delta safe_u_{N+2} ),  (E78.24)
```

so `Q_theta,N` is a **sigma-derivative second drift** of the coupled object
`u=-theta'/(1-theta)`.

The current theorem-grade ledger contains no exact identity identifying these
two constructions.

## 3. Probe audit against the shortcut

Using the certified common ladder

```text
sigma in {1.0,3.0},   N in {8,10,12,14,16,18},           (PNQ-5)
```

the ratios

```text
PAIRNUM_N / Delta safe_u_N,
PAIRNUM_N / Q_theta,N                                     (PNQ-6)
```

were computed directly from the existing certified JSON artifacts.

### Zeta

The ratios vary substantially:

```text
PAIRNUM / Delta safe_u:
  min = 6.360e-2,  median = 2.219e-1,  max = 7.275e-1

PAIRNUM / Q_theta:
  min = 2.591e-4,  median = 1.049e-3,  max = 7.439e-3.   (PNQ-7)
```

Representative rows:

```text
sigma=1.0, N=8:
  PAIRNUM = 2.31659e-2
  Delta safe_u = 3.18414e-2
  PAIRNUM/Delta safe_u = 7.275e-1
  Q_theta = 3.11409
  PAIRNUM/Q_theta = 7.439e-3

sigma=1.0, N=16:
  PAIRNUM = 3.01658e-3
  Delta safe_u = 7.66827e-3
  PAIRNUM/Delta safe_u = 3.934e-1
  Q_theta = 3.74339
  PAIRNUM/Q_theta = 8.058e-4.                             (PNQ-8)
```

So even on zeta there is no constant proportionality and no exact reduction of
`PAIRNUM_N` to the existing `safe_u` or `Q_theta` objects.

### Planted build

The mismatch is even stronger:

```text
PAIRNUM / Delta safe_u:
  min = -1.378e5,  median = -1.103e4,  max = -3.795e1

PAIRNUM / Q_theta:
  min = -1.299e2,  median = -1.071,   max = -1.224e-1.   (PNQ-9)
```

So the shortcut fails completely on the falsifier as well.

## 4. Consequence

This is an honest autopsy:

```text
PAIRNUM_N  ≠  disguised Q_theta,N
PAIRNUM_N  ≠  harmless multiple of Delta safe_u_N.       (PNQ-10)
```

The shell object and the sigma-derivative object live on the same coupled
`theta/(1-theta)` front, but they are not the same theorem-grade target.

Therefore the admissible next object is not "prove `Q_theta` and inherit
`PAIRNUM` for free". The correct frontier is a genuinely mixed statement:

```text
MIXED-THETA-SHELL-LAW:
  identify the shell pairing
  -Re(Delta theta_N conj(1-theta_N))
  directly from the finite Schur/cell algebra, without replacing it by the
  sigma-derivative curvature object Q_theta.              (PNQ-11)
```

## 5. Honest reading

This note does not close the sign problem. It prevents a false closure.

`Q_theta` remains useful as the exact carrier of `safe_u` curvature and as a
phase-side detector. But the denominator-side shell sign now has its own exact
finite endpoint, `PAIRNUM_N`, and current evidence does not justify identifying
the two.

So the next genuine progress must derive `PAIRNUM_N` itself as one coupled
finite functional, not reroute it through the sigma-derivative front.

## 6. Status

```text
proved:
  the current exact ledger contains no identity reducing PAIRNUM_N to
  Delta safe_u_N or Q_theta,N;

observed:
  on the common certified ladder, the ratios PAIRNUM/Delta safe_u and
  PAIRNUM/Q_theta vary substantially even on zeta;

autopsied:
  the shortcut PAIRNUM -> Q_theta / safe_u is invalid;

reduced:
  further denominator/IDENT progress to MIXED-THETA-SHELL-LAW.
```
