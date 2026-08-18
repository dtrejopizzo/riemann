# E101.064 - Projective falsifier for the Jacobi leakage

## 1. Question

E101.063 proves the exact transfer

```text
p_zH_Py
=p_z(D_r-zeta I)H_P(D_c-zeta I)^(-1)y
 -p_z[D,H_P](D_c-zeta I)^(-1)y.                    (1.1)
```

The commutator term is an explicit two-generator endpoint source.  The first
term is the shifted Jacobi leakage

```text
JLEAK_(N,z,zeta)
=p_z(D_r-zeta I)H_P(D_c-zeta I)^(-1)y.             (1.2)
```

The cheapest possible prime-only closure would be that (1.2), after division
by the boundary transform, is projectively constant in the safe variable.
Then it would disappear under bilateral base-point subtraction.  This
document tests and rejects that possibility before any asymptotic work.

## 2. Canonical finite construction

Let

```text
H_Z=the arithmetic finite CCM matrix,
H_A=the same matrix with the prime current removed,
H_P=H_A-H_Z.                                        (2.1)
```

For a symmetric row mesh `[-N,N]` and the right-bordered column mesh
`[-N,N+1]`, let `R_N` be the corresponding rectangular block of `H_Z`.
Construct

```text
R_Ny_N=0,
1^Ty_N=1,

p_(N,z)R_N=c_z-B_(y_N)(z)1^T                       (2.2)
```

by solving the square bordered systems.  No determinant or finite difference
is used.

Fix

```text
eta=1/4,
zeta=z+eta.                                         (2.3)
```

For `sigma>0`, define the bilateral leakage

```text
L_N(sigma)
=JLEAK_(N,i sigma,i sigma+eta)/B_(y_N)(i sigma)
 +JLEAK_(N,-i sigma,-i sigma+eta)/B_(y_N)(-i sigma). (2.4)
```

The projective-constancy test at `sigma_*=1` is

```text
L_N(sigma)-L_N(1)=0.                                (2.5)
```

## 3. Exact internal control

Before evaluating (2.5), the computation verifies (1.1) directly.  With

```text
g=(D_c-zeta I)^(-1)y,                               (3.1)
```

it compares

```text
p_zH_Py
```

with

```text
p_z(D_r-zeta I)H_Pg-p_z[D,H_P]g.                   (3.2)
```

The discrepancy is below `10^(-39)` in the largest section reported below
and below `10^(-52)` in the smallest section.  Thus failure of (2.5) is not a
failure of the transfer identity.

## 4. Falsifier result

The companion computation

```text
E101_064_jacobi_projective_probe.py                  (4.1)
```

rebuilds both matrices in multiprecision.  For `lambda=6`, it gives

```text
N    sigma     L_N(sigma)-L_N(1)
2    0.60       3.358039571e6
2    0.75       6.202128284e6
2    1.50      -4.922844079e7
2    2.00      -1.453524794e8

3    0.60       3.637226592e10
3    0.75       2.658898077e10
3    1.50      -7.330558626e10
3    2.00      -1.630432422e11

4    0.60       2.818444122e13
4    0.75       2.189877255e13
4    1.50      -5.219261379e13
4    2.00      -9.634566374e13.                    (4.2)
```

All displayed values are real because the two safe half-axis values are
paired.  They are many orders of magnitude away from zero and vary strongly
with `sigma`.  Projective constancy is false already in the smallest tested
section.

## 5. Consequence

The Jacobi rank-two collapse remains an exact and useful recombination of the
prime direction:

```text
physical boundary + compression shell
=explicit endpoint source.                          (5.1)
```

It does not, however, remove the projective leakage.  Equation (1.1) merely
moves the complete prime path current into

```text
explicit two-generator term - JLEAK.                (5.2)
```

The optimistic prime-only clause of `DX-LOG-EULER-JACOBI-MATCH` is therefore
rejected.

The moving-level chain direction is a scalar shared-block direction.  Its
commutator with `D` vanishes, so it is invisible in the Jacobi identity and
was not included in (2.1).  It could cancel part of (4.2) only after being
restored in the complete horizontal variation.  Such a cancellation would
be the full path-to-secant identity of E101.062, not a consequence of the
rank-two Jacobi collapse.

The only remaining possibility is to prove that `JLEAK` is exactly the
terminal matched leakage under the path-to-secant map of E101.062.  Such an
identity would be a valuable crosswalk, but it would not by itself reduce the
open scalar: the terminal matched leakage is already DIRECTIONAL-IDENT in its
shifted coordinate.

Hence no asymptotic norm program is opened around the prime-only expression
(1.2).  The Jacobi bypass is frozen at finite-identity grade unless an exact
source-adapted evaluation including the chain direction is found.

## 6. Status

```text
verified:
  shifted commutator transfer to multiprecision accuracy;

falsified:
  projective constancy of the prime Jacobi leakage;
  prime-only disappearance under bilateral base-point subtraction;

retained:
  the rank-two Jacobi identity as a finite recombination;
  a possible exact crosswalk to the already open matched leakage;

frozen:
  asymptotic estimates for prime JLEAK without the complete chain direction
  and a new source-adapted identity;

open:
  the terminal secant identification;
  MATCHED-CURRENT-IDENT and Omega7.
```
