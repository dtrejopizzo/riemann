# E72.311 -- Cauchy numerator divisibility and the analytic core of MC-NZ

**Purpose.** Replace the compact-root target `MC-NZ` of E72.310 by a finite numerator identity. This
removes the remaining matrix language from the compact branch and shows exactly what still has to be
proved analytically.

The point is deliberately modest and load-bearing:

```text
MC-NZ is not a numerical phenomenon. It is a statement about the finite Cauchy numerator evaluated at
the rotated nontrivial-zero parameters.
```

## 1. The finite Cauchy numerator

Let the pole-even mesh be symmetric:

```text
d_-m=-d_m,        xi_-m=xi_m.
```

Define the finite Cauchy transform

```text
C_x(w)=sum_m xi_m/(w-d_m).
```

Let

```text
D_x(w)=prod_m(w-d_m),
P_x(w)=D_x(w)C_x(w)=sum_m xi_m prod_{n != m}(w-d_n).
```

Then `P_x` is the finite Cauchy numerator. Away from the mesh,

```text
C_x(w)=P_x(w)/D_x(w).                                      (1)
```

The finite Weyl roots are precisely the real zeros of `P_x` which are not mesh poles:

```text
P_x(tau_j)=0.                                               (2)
```

This is the numerator version of the E72.310 statement `C_x(tau_j)=0`.

## 2. Even reduction

Because `C_x` is odd under the pole-even symmetry, the numerator has the corresponding parity after
the harmless mesh factor is removed. Equivalently, in the squared variable

```text
r=w^2,
```

there is a polynomial `p_x(r)` and a nonzero explicit mesh factor `E_x(w)` such that

```text
P_x(w)=E_x(w)p_x(w^2).                                      (3)
```

The active finite Weyl divisor is therefore

```text
p_x(tau_j^2)=0.                                             (4)
```

This is the clean height-plane divisor. It is the object which should replace any informal phrase
like "division by the Cauchy transform."

## 3. MC-NZ as a numerator statement

For a nontrivial zero `rho`, write

```text
z_rho=rho-1/2,        w_rho=i z_rho.
```

E72.310 says that compact-root annihilation follows from

```text
MC-NZ:
sup_{tau_j<=H}
|R_tau_j * sum_rho
  (1-e^(z_rho L))
  z_rho tau_j^2/(tau_j^2+z_rho^2)
  C_x(w_rho)|
<= C_H L^5.                                                 (5)
```

Using (1), this becomes the exact numerator form:

```text
NUM-MC:
sup_{tau_j<=H}
|R_tau_j * sum_rho
  (1-e^(z_rho L))
  z_rho tau_j^2/(tau_j^2+z_rho^2)
  P_x(w_rho)/D_x(w_rho)|
<= C_H L^5.                                                 (6)
```

After the even reduction (3), this is equivalently

```text
sup_{tau_j<=H}
|R_tau_j * sum_rho
  W_{tau_j,L}(rho)
  p_x(-z_rho^2) / Delta_x(z_rho)|
<= C_H L^5,                                                 (7)
```

where `W_{tau,L}` contains the explicit Mellin factor and `Delta_x` is the explicit nonvanishing mesh
denominator obtained from `D_x(i z)/E_x(i z)`.

This is now a scalar finite-divisor theorem.

## 4. What real-root divisibility does and does not give

The real-root divisor gives the factorization

```text
p_x(r)=a_x prod_j(r-tau_j^2) q_x(r),                         (8)
```

where `q_x` contains only the inactive finite roots outside the compact window and any fixed mesh
normalization.

Substituting `r=-z_rho^2` gives

```text
p_x(-z_rho^2)
= a_x prod_j(-z_rho^2-tau_j^2) q_x(-z_rho^2).                (9)
```

This identity is useful, but it is not by itself enough to prove (7). For an off-line zero with
`Re z_rho>0`, the multiplier `(1-e^(z_rho L))` is exponentially large. Real zeros of `p_x` do not force
`p_x(-z_rho^2)` to be exponentially small. Therefore:

```text
Finite real-root divisibility alone cannot prove MC-NZ.
```

The missing input must be a residue/normalization identity for the quotient

```text
Q_x(r):=p_x(r)/Delta_x(sqrt(-r)),
```

evaluated on the rotated spectral set `r=-z_rho^2`.

This is the analytic core. It is not a matrix estimate.

## 5. The minimum new theorem

The compact branch reduces to the following pure scalar statement.

### Theorem target: rotated numerator suppression

For every fixed height window `H`, there are constants `C_H,L_H` such that for all `L>=L_H` and every
finite Weyl root `tau_j<=H`,

```text
|R_tau_j * sum_rho
  W_{tau_j,L}(rho)
  p_x(-z_rho^2)/Delta_x(z_rho)|
<= C_H L^5,                                                  (RNS)
```

with

```text
z_rho=rho-1/2,
W_{tau,L}(rho)=(1-e^(z_rho L)) z_rho tau^2/(tau^2+z_rho^2),
```

and with no use of the limiting `Xi` divisor as input.

Then `RNS => MC-NZ => NZ-MSD => fixed-height compact-root HPAC decay`.

## 6. How to attack RNS analytically

The only plausible proof route left is not pointwise smallness of the numerator. The off-line packet
would demand exponential smallness, which is too strong unless it is forced by a hidden identity.

The analytic route has to be one of:

```text
A. quotient residue identity:
   show that the weighted zero sum in (RNS) is the residue sum of a rational function with no interior
   residues after the finite Weyl divisor is removed;

B. canonical-product cancellation:
   show that the exponentially growing factor (1-e^(zL)) is cancelled by the mesh quotient
   p_x(-z^2)/Delta_x(z) through an exact sine-type identity;

C. contour transport:
   move the zero sum to a contour where the numerator quotient has polynomial growth and all horizontal
   sides cancel by the pole-even endpoint identities.
```

Among these, (C) is the most analytic and the least likely to smuggle in the answer. It would prove
RNS from:

```text
1. a meromorphic function
   G_{tau,L}(s)=W_{tau,L}(s-1/2)p_x(-(s-1/2)^2)/Delta_x(s-1/2) * Xi'(s)/Xi(s);

2. polynomial vertical growth of the finite quotient away from the mesh;

3. cancellation of the finite-mesh residues by the Weyl numerator identity P_x(tau_j)=0;

4. explicit control of the pole/trivial-zero residues, already isolated in E72.305.
```

This is now a concrete analytic proof problem.

## 7. Status

```text
proved: C_x(w)=P_x(w)/D_x(w) and finite Weyl roots are zeros of P_x;
proved: MC-NZ is exactly NUM-MC, a finite Cauchy-numerator statement;
proved: real-root divisibility alone cannot supply the needed off-line suppression;
open:   prove RNS by quotient residues, sine-type cancellation, or contour transport.
```

The next useful lemma is therefore not another finite matrix experiment. It is a contour lemma for
`G_{tau,L}` with finite-mesh residue cancellation.
