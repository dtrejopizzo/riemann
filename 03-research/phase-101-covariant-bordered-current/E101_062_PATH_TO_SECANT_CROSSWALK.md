# E101.062 - Path-to-secant crosswalk for the total current

## 1. Purpose

The deformation route E97--E100 and the terminal residual route
E101.045--E101.052 must represent the same projective boundary scalar if both
are correct.  This does not justify a termwise identification of their
internal decompositions.

This document proves the exact total-scalar crosswalk.  Its central identity
is

```text
integrated path current
=terminal projective secant.                         (1.1)
```

It recombines the bordered sandwich, moving-level chain term and compression
shell before any estimate.

## 2. Rectangular boundary chart

Let

```text
R_t=[M_t,b_t]                                       (2.1)
```

be an `r` by `r+1` continuously differentiable full-row-rank matrix.  Work
in a chart where

```text
Delta_t=det M_t!=0.                                 (2.2)
```

Define

```text
a_t=adj(M_t)b_t,
kappa_t=(a_t,-Delta_t)^T,
ell=(1^T,1),
C_t=Delta_t-1^Ta_t.                                 (2.3)
```

Assume `C_t!=0` and put

```text
y_t=-kappa_t/C_t.                                   (2.4)
```

Then

```text
R_ty_t=0,
ell y_t=1.                                          (2.5)
```

Indeed, `M_ta_t=Delta_tb_t`, while
`ell kappa_t=1^Ta_t-Delta_t=-C_t`.

## 3. Bordered numerator equals the boundary transform

Let the augmented mesh be

```text
D_tilde=diag(D,d_b),                                (3.1)
```

and define

```text
c_z=z1^T(zI-D_tilde)^(-1).                          (3.2)
```

On the first `r` columns put

```text
(h_z)_j=(z-d_b)/(z-d_j).                            (3.3)
```

Then

```text
(h_z,1)=(z-d_b)c_z/z.                               (3.4)
```

Define the old bordered numerator

```text
N_t(z)=det [ M_t  b_t ]
             [ h_z   1 ].                           (3.5)
```

### Theorem 3.1

The normalized boundary transform

```text
B_t(z)=c_zy_t                                      (3.6)
```

satisfies

```text
B_t(z)=z N_t(z)/[(z-d_b)C_t].                       (3.7)
```

### Proof

The block determinant formula and `a_t=adj(M_t)b_t` give

```text
N_t(z)=Delta_t-h_za_t.                              (3.8)
```

Equations (2.4) and (3.4) give

```text
c_zy_t
=1/C_t[-c_z^(old)a_t+c_z^(b)Delta_t]
=z/[(z-d_b)C_t][Delta_t-h_za_t].                   (3.9)
```

Substitute (3.8). `QED`

In every base-point subtraction in `z`, the factor `C_t` cancels.  The
remaining `z/(z-d_b)` factor is explicit mesh geometry and must be retained
in the base term.

## 4. Differential projective Jacobi identity

For every safe `z`, let `p_(t,z)` be the unique row satisfying

```text
p_(t,z)R_t=c_z-B_t(z)ell.                           (4.1)
```

### Theorem 4.1

For every matrix variation `delta R_t`, with `c_z` and `ell` fixed,

```text
delta B_t(z)=-p_(t,z)(delta R_t)y_t,                (4.2)

delta log B_t(z)
=-p_(t,z)(delta R_t)y_t/B_t(z).                    (4.3)
```

### Proof

Differentiate (2.5):

```text
(delta R_t)y_t+R_t(delta y_t)=0,
ell(delta y_t)=0.                                   (4.4)
```

Since `delta B_t=c_z delta y_t`, equation (4.1) gives

```text
delta B_t
=p_(t,z)R_t(delta y_t)
=-p_(t,z)(delta R_t)y_t.                            (4.5)
```

Division by `B_t(z)` proves (4.3). `QED`

Thus the complete cofactor sensitivity on rectangular directions is the
rank-one covector

```text
-y_t p_(t,z)/B_t(z).                                (4.6)
```

The bordered source sandwich, moving-level chain term and compression shell
are not three different sensitivities.  They are three contributions to the
single variation `dot R_t` in (4.3).

## 5. Path-to-secant theorem

### Theorem 5.1

For every continuously differentiable path satisfying the preceding
hypotheses and `B_t(z)!=0` on the path,

```text
exp integral_0^1
 [-p_(t,z)dot R_ty_t/B_t(z)]dt
=B_1(z)/B_0(z)                                      (5.1)

=1-p_(1,z)R_1y_0/B_0(z).                            (5.2)
```

### Proof

Equation (4.3) with `delta=partial_t` integrates to (5.1).  For (5.2), use
`ell y_0=1` as a comparison vector for the terminal block.  E101.046 gives

```text
B_1(z)-c_zy_0=-p_(1,z)R_1y_0.                      (5.3)
```

Since `c_zy_0=B_0(z)`, division by `B_0(z)` proves (5.2). `QED`

Equation (5.2) is a finite secant formula.  It contains no path integral,
ambient inverse or separate shell norm.

## 6. Bilateral projective form

For a nonvanishing scalar function `F`, write

```text
Pi_bil log F
=log F(iu)+log F(-iu)
 -log F(iu_*)-log F(-iu_*),                         (6.1)
```

with compatible logarithm branches.  Apply (5.1) at the four points in
(6.1).  The total finite deformation current becomes

```text
integral_0^1 Pi_bil{
 -p_(t,z)dot R_ty_t/B_t(z)
 }dt
=Pi_bil log[B_1(z)/B_0(z)].                         (6.2)
```

By (3.7), this is also the complete bordered numerator current of E97--E100,
including the explicit mesh factor.  In particular,

```text
bordered sandwich
+moving-level chain term
+compression shell                                 (6.3)
```

must be recombined into `dot R_t` before comparison with the independent
Euler current.

## 7. Terminal comparator and MATCHED-CURRENT-IDENT

Let `k` be any terminal comparison vector with

```text
ell k=1,
e=R_1k,
B_k(z)=c_zk.                                        (7.1)
```

The terminal secant identity is

```text
B_1(z)/B_k(z)
=1-p_(1,z)e/B_k(z).                                 (7.2)
```

The radical decomposition and endpoint transfer of E101.047--E101.052 have
the schematic exact form

```text
p_(1,z)e
=DIRECT_(N,z)
 +COLLAR_(N,z)
 +m_0z[1-B_1(z)]+J_(N,z).                          (7.3)
```

Here `COLLAR` means the complete recombined exterior current, not separate
near and far limits.  Substitution into (7.2) gives

```text
log[B_1(z)/B_k(z)]
=log{1-[DIRECT+COLLAR
        +m_0z(1-B_1)+J_N]/B_k(z)}.                 (7.4)
```

Let `E_L(z)` denote the independently normalized Euler--Gamma target,
including the explicit mesh factor in (3.7).  Then the exact total defect is

```text
Pi_bil log[B_1/E_L]
=Pi_bil log[B_k/E_L]
 +Pi_bil log{1-[DIRECT+COLLAR
        +m_0z(1-B_1)+J_N]/B_k}.                    (7.5)
```

Equation (7.5) is the correct dictionary between the two routes.  Once the
model match `B_k/E_L`, the direct in-band term and the complete exterior
infrastructure are handled, the remaining numerator is precisely the
matched endpoint current.

## 8. Invalid termwise identifications

The total equality (7.5) does not prove any of the following:

```text
Gamma_t dot mu_t = J_z;

the E98 compression shell = the E101 omitted-column collar;

one bordered source sandwich = one radical-tail component.              (8.1)
```

The moving-level term in E100 is the component of `dot R_t` caused by the
level variation.  The invariant `J_z` in E101.052 is a terminal recombination
under a shifted endpoint corrector.  They live in different decompositions
of the same total scalar.

Likewise, the E98 shell is a crossing term created by compression of the
Euler direction along the path, whereas the E101 collar consists of omitted
Fourier columns in the terminal radical residual.  Equality can be asserted
only after both are shown to arise from the same complete `dot R_t` or the
same terminal `e` under (5.1)--(5.2).

## 9. Exact remaining bridge gaps

Two definitions must be completed before the crosswalk becomes a theorem
between the named historical targets.

```text
BRIDGE-1:
  prove that the RT-2 collar in (7.3) is the terminal secant image of the
  same compression crossing included in dot R_t;

BRIDGE-2:
  define the independent Gamma-prime current in E101.052 with the division
  by B_k, bilateral logarithm and mesh factor appearing in (7.5).         (9.1)
```

Neither bridge is a new sign assertion, but neither follows from a shared
name such as `shell` or `endpoint`.

## 10. Novelty verdict

PATH-TO-SECANT is universal finite algebra.  It holds for the arithmetic and
inserted-quartet builds, so it cannot prove `Omega7`.  Its value is a strict
no-duplication rule:

```text
do not estimate sandwich, chain and shell separately;
replace their path integral by the terminal secant (5.2);
compare only the complete terminal numerator with (7.3).                (10.1)
```

A further path-current estimate that does not improve the terminal secant is
another coordinate for the same open scalar.

## 11. Status

```text
proved:
  equality of the bordered numerator and normalized boundary transform;
  differential projective Jacobi identity;
  exact path-to-secant formula;
  total-scalar crosswalk (7.5);

rejected:
  termwise identification of the E97--E100 and E101 decompositions;
  separate estimates on sandwich, chain and compression shell;

isolated:
  BRIDGE-1 and BRIDGE-2;

open:
  the complete terminal secant identification;
  MATCHED-CURRENT-IDENT and Omega7.
```
