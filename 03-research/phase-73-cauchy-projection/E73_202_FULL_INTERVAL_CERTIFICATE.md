# E73.202 - Full interval certificate for TRANS-CELL

Date: 2026-07-14.

## 1. Purpose

E73.199 gives the finite-frequency certificate with a closed digamma WR tail.
E73.200--E73.201 show that the final value is a severe cancellation between
large archimedean and prime terms.  Therefore a rigorous certificate cannot
intervalize only the WR tail.  It must enclose the whole finite object.

This note states the complete interval theorem needed for the current route.

## 2. Exact finite data

Fix `(lambda,N)` and `L=2log lambda`.  Let

```text
d_m=2pi m/L,             -N<=m<=N,
H=H_model-Prime,
xi=normalized ground vector of H,
Q_w=(q_w,q_-w),
eta_w=(I-P_w)xi,
P_w=Q_w^*(Q_wQ_w^*)^(-1)Q_w.
```

For each row `a in {w,-w}` define the finite-frequency packet

```text
B_a(y)=q_a Q_L(y)eta_w
      =sum_omega c_omega(a,w)e^(iomega y)
       +y sum_omega l_omega(a,w)e^(iomega y).
```

The E73.199 certificate is

```text
C_a(lambda,N,w)
=A_L^digamma[{c_omega,l_omega}]
 -sum_{p^k<=lambda^2}(log p)p^(-k/2)B_a(klog p).
```

The desired transverse cell estimate is

```text
C_a(lambda,N,w)=O_R(L^-R)
```

uniformly in the admissible rows.

## 3. Interval objects

A full certificate consists of the following interval enclosures.

### I. Matrix entry intervals

An interval Hermitian matrix `[H]` enclosing the exact finite matrix, computed
from the same closed finite-frequency formulas used in E73.199:

```text
[H_model]_{mn}=A_L[Q_{mn}],
[Prime]_{mn}=sum_{p^k<=lambda^2}(log p)p^(-k/2)Q_{mn}(klog p).
```

No quadrature is allowed in the final certificate.  The archimedean entries use
finite WR head plus digamma tail.

### II. Eigenline enclosure

An interval vector `[xi]` and scalar interval `[mu]` with:

```text
||H xi_0-mu_0 xi_0|| <= eps_eig,
dist(mu_0, spec(H|xi_0^perp)) >= gap,
eps_eig < gap/4.
```

Then the true normalized ground line lies in the ball

```text
dist(xi,xi_0) <= 2 eps_eig/gap                         (1)
```

by the standard Riesz-projection/Davis-Kahan estimate.  This turns the
eigenvector from a floating input into a certified interval object.

### III. Cauchy projection enclosure

Using interval arithmetic on

```text
P_w=Q_w^*(Q_wQ_w^*)^(-1)Q_w,
eta_w=(I-P_w)xi,
```

produce `[eta_w]` satisfying

```text
Q_w eta_w = 0
```

as an interval inclusion.  Equivalently, the residual interval for
`Q_w eta_w` must contain only a ball of radius below the target budget after
transport through the finite-frequency formula.

### IV. Packet coefficient intervals

From `[eta_w]`, compute intervals `[c_omega]`, `[l_omega]` for the exact
finite packet.  The coefficient map is bilinear in `(q_a,eta_w)` and rational
in the Cauchy denominators, so it is an explicit interval operation.

### V. Full functional interval

Compute one interval `[C_a]` for

```text
C_a=A_L^digamma[{c,l}]-P_L[{c,l}],
```

where:

```text
A_L^digamma = elementary finite exponentials
              + finite WR head
              + D_1/D_2 digamma tail
              + exponential remainder bound,

P_L = finite prime-power sum with interval exponentials.
```

The non-elementary enclosures are only:

```text
psi(R+1/2),       psi(R+1/4-iomega/2),
psi_1(R+1/4-iomega/2).
```

These can be enclosed by Euler-Maclaurin with a certified remainder, or by ball
arithmetic special functions.

## 4. The certificate theorem

**Theorem 202.1 (finite interval TRANS-CELL certificate).**  Fix an admissible
window and a target exponent `R_*`.  Suppose the interval objects I--V are
constructed with outward rounding and satisfy, for every admissible Cauchy row
`a`,

```text
[C_a] subset {z: |z| <= M L^(-R_*)}.                  (2)
```

Then `TRANS-CELL` holds in that finite window with budget `M L^(-R_*)`.

*Proof.*  By I, the exact finite matrices lie in `[H_model]` and `[Prime]`.
By II, the exact ground line of `H=H_model-Prime` lies in `[xi]`.  By III, the
exact transverse vector `eta_w=(I-P_w)xi` lies in `[eta_w]` and satisfies the
Cauchy constraints up to the certified residual already included in the
coefficient intervals.  By IV, the exact packet coefficients of
`B_a(y)=q_aQ_L(y)eta_w` lie in `[c_omega]` and `[l_omega]`.

E73.199 proves the algebraic identity

```text
q_a(H_model-Prime)eta_w
=A_L^digamma[B_a]-P_L[B_a]
=C_a.
```

All operations in V are interval extensions of the exact right-hand side, with
the WR tail replaced by the equal digamma expression of E73.198 and the
exponential tail bounded outward.  Hence the exact scalar
`q_a(H_model-Prime)eta_w` belongs to `[C_a]`.  Inclusion (2) gives the desired
finite `TRANS-CELL` budget. `QED`

## 5. Uniform upgrade

The remaining analytic theorem is the uniform production of such certificates:

```text
UNIFORM-INTERVAL-FF:
For every compact height window and every target R, there are constants
M,R_*,N_0 such that all admissible finite windows with N>=N_0 admit
the interval certificate of Theorem 202.1.
```

Combined with the reductions E73.188--E73.199, this implies the scalar WRL
gate for the corresponding channel.

## 6. Relation to previous interval work

E73.108--E73.119 used interval boxes for the earlier FAR/Hermite branch.  The
present certificate is not that branch.  It uses the later transverse packet
and the digamma finite-frequency functional.  The transferable lesson is
methodological: selection/geometry intervals alone are insufficient; the
load-bearing scalar must be enclosed after all cancellations.

## 7. Status

```text
proved: finite interval certificate theorem;
identified: all interval inputs needed for a rigorous TRANS-CELL check;
open: implementation with outward-rounded complex ball arithmetic;
open: uniform analytic production of certificate widths.
```
