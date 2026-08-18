# E101.044 - Sectorial heat stability

## 1. Relative squared determinant

Let `y` and `w` be two boundary vectors on the same real mesh `D`, with

```text
1^T y!=0,
1^T w!=0.                                           (1.1)
```

Assume their quotient operators `D_y,D_w` have real nonzero spectra
`{kappa_(y,j)}` and `{kappa_(w,j)}`.  Define

```text
mathcal R_(y,w)(zeta)
 ={det M_y(zeta)}/{det M_w(zeta)}                   (1.2)

 =prod_j{zeta-kappa_(y,j)^2}
        /{zeta-kappa_(w,j)^2}.                       (1.3)
```

The common forced zero and the common squared mesh cancel.  In particular,

```text
mathcal R_(y,w)(zeta)->1
as |zeta|->infinity.                                 (1.4)
```

## 2. Sector contour formula

Fix `0<theta<pi/2`.  Let `Gamma_theta` be the counterclockwise boundary of
the sector containing the positive real axis, with rays

```text
zeta=r exp(-i theta),
zeta=r exp(i theta),
r>0.                                                 (2.1)
```

Small circles around a zero at the origin are retained if needed.  Suppose
the two core spectra avoid zero.  Then a continuous logarithm of
`mathcal R_(y,w)` can be chosen on `Gamma_theta` with value tending to zero
at infinity.

### Theorem 2.1

For every `v>0`,

```text
H_y(v)-H_w(v)
 ={v/(2pi i)}integral_(Gamma_theta)
   exp(-v zeta)log mathcal R_(y,w)(zeta)d zeta.      (2.2)
```

### Proof

The argument principle and the decay of the exponential on the sector give

```text
H_y(v)-H_w(v)
 ={1/(2pi i)}integral_(Gamma_theta)
   exp(-v zeta)partial_zeta
   log mathcal R_(y,w)(zeta)d zeta.                 (2.3)
```

Both node sets have the same cardinality, so the relative determinant has
zero winding on a contour containing both spectra.  Integration by parts is
therefore legitimate.  The large arc vanishes by (1.4) and exponential
decay; the small arc vanishes when the core spectra avoid zero.  This gives
(2.2). `QED`

## 3. Weighted logarithmic bound

Parameterizing the two rays in (2.2) gives

```text
|H_y(v)-H_w(v)|
 <={v/(2pi)}integral_0^infinity
    exp(-vr cos theta)[
      |log mathcal R_(y,w)(r exp(i theta))|
     +|log mathcal R_(y,w)(r exp(-i theta))|
    ]dr.                                             (3.1)
```

Consequently, convergence of the relative logarithm in this weighted
`L^1` norm implies convergence of the heat traces on every compact heat
interval.

## 4. Projective Cauchy form

By E101.043(4.2),

```text
mathcal R_(y,w)(zeta)
 ={B_y(sqrt(zeta))B_y(-sqrt(zeta))}
  /{B_w(sqrt(zeta))B_w(-sqrt(zeta))}.               (4.1)
```

Thus the sector norm uses only projective Cauchy transforms at points whose
arguments are `plus or minus theta/2` away from the real mesh.  If

```text
epsilon_+(zeta)=B_y(sqrt(zeta))/B_w(sqrt(zeta))-1,
epsilon_-(zeta)=B_y(-sqrt(zeta))/B_w(-sqrt(zeta))-1 (4.2)
```

have modulus at most `1/2`, then

```text
|log mathcal R_(y,w)(zeta)|
 <=2|epsilon_+(zeta)|+2|epsilon_-(zeta)|.           (4.3)
```

This is a directional estimate.  It requires no ambient norm bound for
`y-w` and no inverse spectral gap.

## 5. What the lemma can close

Theorem 2.1 can prove:

```text
finite-section heat convergence;
heat convergence from a proved boundary-to-model projective bridge;
stability of Gaussian node statistics under a sectorial Cauchy estimate.
                                                               (5.1)
```

It cannot by itself compare the finite real spectra with `H_Xi`.  A model
whose relative determinant tends to the completed target must still be
identified arithmetically.

In particular, assigning a positive real squared spectrum to the target
before proving that identification would assume the Stieltjes discriminant
and hence `Omega7`.

## 6. Relation to the radical route

For a finite prolate model vector on the same mesh, (4.2) is the sectorial
version of `SAFE-PROLATE-BRIDGE`.  P76.063 supplies the correct coupled
radical-tail decomposition for its numerator.  The still missing assertion
is directional uniqueness of the normalized boundary solution; sectorial
heat stability does not supply that uniqueness.

## 7. Status

```text
proved:
  sector contour formula for relative finite heat traces;
  weighted logarithmic stability bound;
  reduction to projective Cauchy ratios without an inverse-gap norm;

closed as insufficient:
  using sectorial stability without an independently identified model;

open:
  the arithmetic boundary-to-model projective bridge.
```
