# E73.017 - Finite displacement reduction for LOCAL-FIN

## 1. Purpose

E73.016 replaced strict triangularity by the finite-width action certificate:

```text
LOCAL-FIN:
(C_E-mu I)P_{O,K} subset S_{O,K}^{fin} + R_72.
```

This note gives the analytic reduction that must be proved directly from the CCM cell formula.
It is narrower than the previous open problem: instead of controlling the eigenvector, it controls
the displacement rank of the kernel family on which the eigenvector is tested.

## 2. Cell formula

In the finite CCM basis indexed by `m,n`, the coupled cell is

```text
C_E(m,n)=W02(m,n)-WR(m,n)-Prime(m,n)-e_pole delta_mn.
```

The shared test cell is `q_mn(y)`.  In the implementation this is:

```text
m=n:
q_nn(y)=2(1-y/L)cos(d_n y)

m!=n:
q_mn(y)=(sin(d_m y)-sin(d_n y))/(pi(n-m)),
```

where `d_n=2pi n/L`.  Equivalently, for fixed `y`, `q_mn(y)` is a finite Loewner divided difference
of the function `sin(dy)` plus the diagonal endpoint correction.

Thus all three pieces `W02`, `WR`, and `Prime` are obtained by applying scalar distributions in `y`
to the same finite Loewner kernel.

## 3. Displacement operator

Let `D=diag(d_n)` and let `J=11^T`.  The finite Loewner identity from Phase 72 gives the schematic
form

```text
Q(y)=2 cos(yD) - (2/L) Lo_y,
Lo_y = Frechet_D[sin(yD)](J).
```

Therefore every coupled cell has the form

```text
C_E = A_0(D) + L_A(D,J),
```

where:

```text
A_0(D)       is diagonal/multiplicative in the pole mesh;
L_A(D,J)     is one finite Loewner displacement of a scalar function A.
```

The arithmetic distribution changes the scalar function `A`; it does not change the displacement
type.  This is why `W02`, `WR`, and `Prime` must remain coupled.

## 4. Local Cauchy closure identity

For

```text
Y(d)=DD_gamma(d)/(d^2+beta^2)^r,
```

the diagonal part obeys exact rational closure:

```text
A_0(d)Y(d)
= finite source terms + endpoint remainder,
```

because `A_0` is evaluated only on the finite pole mesh and its endpoint interpolant has the same
finite Fourier support.  The Loewner part is controlled by the elementary divided-difference
identity

```text
(F(d)-F(e))/(d-e) * 1/(e^2+beta^2)^r
= sum_{j=0}^{r+1} A_j(d)/(d^2+beta^2)^j
 + sum_{j=0}^{r+1} B_j(e)/(e^2+beta^2)^j
 + E_{F,r,beta}(d,e),
```

where `E_{F,r,beta}` is supported on endpoint Fourier modes.  After summing in `e`, the first two
terms belong to the rational source class and the endpoint part belongs to

```text
span{d^2 DD_gamma(d), d^4 DD_gamma(d)} + R_72.
```

The apparent increase beyond `r+1` in E73.016 occurs because the endpoint-reduced terms from the
lower rational blocks are not zero before Phase 72 tail absorption.  Keeping all orders `0..3`
absorbs this interaction uniformly.

## 5. Finite displacement lemma

The load-bearing analytic lemma is:

```text
FDL:
For every fixed compact off-line window O and critical window K, and for all large L,
the coupled CCM cell operator satisfies

(C_E-mu I)P_{O,K} subset S_{O,K}^{fin} + R_72

with
||R_72||_{Cauchy(K,O)} <= L^B exp(-sigma L)
after the Phase 72 natural-height normalization.
```

The proof decomposes into three explicit algebraic checks:

```text
FDL-1  finite Loewner identity for q_mn(y);
FDL-2  partial-fraction closure of one Loewner displacement on
       DD_gamma(d)/(d^2+beta^2)^r, r=0,1,2;
FDL-3  endpoint terms are exactly the parity-cancelled / zero-node-absorbed / natural-height
       residuals already isolated in Phase 72.
```

No zero of Xi enters these checks.  The only arithmetic input is the prime distribution inside the
coupled scalar function `A`; the displacement type is geometric.

## 6. Consequence

Assume `FDL`.  Then for every off-line node `b` in the natural-height window,

```text
S_b = J_b + R_b,
J_b in (C_E-mu I)P_{O,K},
```

with `R_b` in the Phase 72 residual class.  Pairing with the eigenvector `xi` gives

```text
<xi,J_b>=<xi,(C_E-mu I)Y_b>=0.
```

Therefore

```text
<xi,S_b>=<xi,R_b>.
```

By the Phase 72 residual estimates,

```text
e^(Re b L)|<xi,R_b>| <= L^B.
```

This is `NAT-SRC`, hence `NAT-PROJ`, hence off-line Schur suppression.

## 7. Status

```text
proved here: FDL implies NAT-SRC and hence NAT-PROJ;
validated: E73.016 finite-width source class captures the coupled action numerically;
open analytic core: prove FDL-2 with explicit endpoint bookkeeping.
```

The remaining work is now a finite rational divided-difference computation, not a global positivity
estimate.
