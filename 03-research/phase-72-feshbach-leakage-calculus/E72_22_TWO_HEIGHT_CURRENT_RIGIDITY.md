# E72.22 -- Two-height rigidity for Schur-free current convergence

**Date:** 2026-07-08.
**Role:** prove a non-boundary criterion that rules out hidden Blaschke defects. Boundary modulus is
blind; two interior heights are not.

## 0. Motivation

E72.21 proves that real-axis modulus convergence cannot identify the interior divisor because Blaschke
factors have unit boundary modulus. The next possible proof must control an interior current.

The finite CCM divisor currents are supported on the real axis. Their Cauchy transforms are logarithmic
derivatives of real-rooted spectral functions. A hidden off-real divisor in the limit is detected by
the Cauchy transform away from the real axis.

## 1. Cauchy current transform

For a locally finite divisor measure `mu` on the strip, define its Cauchy transform

```text
C_mu(z) := int (1/(z-w)) dmu(w),
```

with the usual symmetric genus subtraction when the divisor has Cartwright growth. For finite CCM
divisors this is simply

```text
C_x(z)=F_x'(z)/F_x(z).
```

For the target divisor,

```text
C_Xi(z)=Xi'(z)/Xi(z)
```

away from zeros.

## 2. Two-height rigidity theorem

### Theorem 72.22

Let `mu_x` be finite positive divisor measures supported on the real axis, with uniformly bounded local
mass and Cartwright tail control. Let `mu` be a locally finite divisor measure in the strip.

Fix an upper half-slab

```text
S_eta := { z=t+iv : eta_1 < v < eta_2 },     0<eta_1<eta_2<1/2.
```

Assume:

1. the finite transforms

```text
C_{mu_x}(z)
```

are holomorphic on `S_eta`;
2. they are locally normal in `S_eta`, for example uniformly bounded in `H^2` on every compact
sub-slab;
3. on the two boundary heights the Cauchy transforms converge distributionally in the real variable:

```text
C_{mu_x}(t+i eta_j) -> C_mu(t+i eta_j),     j=1,2.      (TH)
```

Then `mu` has no mass in the open upper half-slab `S_eta`.

The analogous statement holds in lower half-slabs. Taking a countable exhaustion of the upper and lower
half of the centered strip rules out all off-real mass.

### Proof

Let `nu` be the part of `mu` in `S_eta`. We prove `nu=0`.

For each `x`, since `mu_x` is supported on `R`, the function

```text
u_x(z)=C_{mu_x}(z)
```

is holomorphic in `S_eta`.

By the local normality assumption, every subsequence has a further subsequence converging locally
uniformly on `S_eta` to a holomorphic function `u`. By `(TH)`, the boundary traces of `u` on the two
horizontal lines are the traces of `C_mu`. Uniqueness for holomorphic functions in a slab with
Cartwright/Hardy control implies that this limit is the restriction of `C_mu` to `S_eta`.

Therefore `C_mu` is holomorphic in `S_eta`. Any atom `a delta_w` of `nu` would contribute a pole

```text
a/(z-w)
```

to `C_mu`, impossible.

For non-atomic locally finite divisor mass, apply the same argument after testing against a small
circle around a point of support: the residue of the limit Cauchy transform around that circle must be
zero because all finite `C_{mu_x}` are holomorphic there. Hence the mass is zero. Therefore `nu=0`.
`QED`

## 3. Consequence for CCM

To prove Schur-free current convergence it is enough to prove the following interior two-height
log-derivative convergence:

```text
F_x'(t+i eta)/F_x(t+i eta)
  -> Xi'(t+i eta)/Xi(t+i eta)
```

distributionally in `t`, for two fixed heights `eta=+eta_0` and `eta=-eta_0` inside the centered strip.

This is stronger than boundary modulus convergence but weaker than tracking zeros. The essential extra
ingredient is the normal-family/Hardy control in the open half-slabs; without it, boundary traces alone
can hide a boundary-loss defect.

## 4. Why this is not the old wall

The Phase 69 Nevanlinna endpoint asks for the sign of

```text
Im(-Xi'/Xi)
```

throughout the half-plane. That is RH-strength.

The two-height criterion asks instead for convergence of finite real-divisor Cauchy transforms on two
specific horizontal lines. If this can be obtained from the finite CCM Weyl formula, the absence of
off-real mass follows from support closure, not from proving a global positivity sign.

## 5. New target

### THLC -- Two-height log-current convergence

For a fixed `0<eta_0<1/2` and every compactly supported smooth test `varphi(t)`,

```text
int varphi(t)
  [ F_x'(t+i eta_0)/F_x(t+i eta_0)
    - Xi'(t+i eta_0)/Xi(t+i eta_0) ] dt -> 0,
```

and the same statement holds at `-eta_0`.

Together with uniform local Hardy/normal bounds for `F_x'/F_x`, E72.22 gives Schur-free current
convergence away from the real axis. A countable exhaustion of half-slabs covers the centered critical
strip.

## 6. Status

```text
proved: two-height Cauchy convergence plus local normal bounds rules out Blaschke/off-real divisor
        defects;
open:   prove THLC and the normal bounds from the finite CCM Weyl construction.
```

The next step is to express `F_x'/F_x` from the finite Weyl function `m_x=P_x/Q_x` without building
`P_x` explicitly, and compare it to the explicit formula for `Xi'/Xi` on the two interior lines.
