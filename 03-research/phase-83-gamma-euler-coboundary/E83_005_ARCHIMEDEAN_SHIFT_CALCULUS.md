# E83.005 - Archimedean shift calculus and boundary commutator

## 1. Renormalized archimedean operator

Let `Q_y=S_y+S_y^*` and `Q_0=2I` as in E83.004.  The archimedean part of the
finite CCM functional is the operator whose Fourier matrix is

```text
H_L^A
 = integral_0^L {
     (exp(y/2)+exp(-y/2))Q_y
     -[exp(y/2)Q_y-Q_0]/(2sinh y)
   }dy
   -[(log(4pi)+EulerConstant)+log(tanh(L/2))]Q_0/2.     (1.1)
```

The integral is renormalized as displayed; its two terms may not be separated
near `y=0`.  Indeed `exp(y/2)Q_y-Q_0` vanishes to first order on the common
Fourier core, so the quotient has a finite weak limit.

### Proposition 1.1

For every finite Fourier section,

```text
<phi_m,H_L^A phi_n>
```

is exactly the archimedean entry used in the CCM matrix.

### Proof

Insert `<phi_m,Q_y phi_n>=q_mn(y)` from E83.004 into (1.1).  The first integral
is the polar term, the renormalized quotient is the Gamma term, and the last
multiple of `Q_0/2=I` gives the two boundary constants.  This is precisely the
finite entry functional. `QED`

Thus the complete unshifted CCM operator is

```text
H_L=H_L^A-(V_L+V_L^*),                                 (1.2)
```

with `V_L` the Euler connection of E83.004.

## 2. Exact boundary commutator of shifts

For nonnegative `y,z`, direct use of the definitions gives

```text
(S_y^*S_z f)(t)
 =1_[max(0,z-y),L-y](t) f(t+y-z),                      (2.1)

(S_zS_y^* f)(t)
 =1_[z,min(L,L-y+z)](t) f(t+y-z).                      (2.2)
```

Therefore

```text
[S_y^*,S_z]f
 ={1_[max(0,z-y),L-y]-1_[z,min(L,L-y+z)]}
   f(t+y-z).                                           (2.3)
```

The difference is supported on boundary intervals.  In contrast,

```text
[S_y,S_z]=0.                                           (2.4)
```

## 3. Gamma--Euler commutator localization

Write the nonconstant coefficient of `Q_y` in (1.1) as

```text
a_L(y)=exp(y/2)+exp(-y/2)-exp(y/2)/(2sinh y),           (3.1)
```

with the renormalization by `Q_0` retained at the origin.  Since the Euler
unit is a sum of one-sided shifts and `Q_0` commutes with it, one obtains on
the common core

```text
[H_L^A,Z_{L,epsilon}]
 =sum_{n<=exp(L)}n^(-1/2-epsilon)
   integral_0^L a_L(y)[S_y^*,S_{log n}]dy.             (3.2)
```

Every term in (3.2) is an explicit boundary operator by (2.3).  Hence the
failure of the archimedean CCM operator to commute with the Euler unit is
localized at the two physical endpoints.

This is an identity, not yet a smallness estimate.  The active boundary width
may grow with the shift parameters, so absolute summation of the boundary
pieces is not admissible.

## 4. Global intertwining is impossible

The position operator `X` on `L^2(0,L)` is bounded with norm at most `L`.
The fixed-`L` archimedean CCM operator has Fourier diagonal growing like
`log(1+|n|)` up to a bounded term.  Therefore

```text
H_L^A-X
```

is unbounded on the infinite Fourier space.  In particular, the identity map
cannot intertwine the two operators with a bounded global error.

This does not refute the one-vector criterion of E83.002.  It proves that the
restriction to the Euler-generated vector is essential, not merely economical.

## 5. Correct live boundary theorem

Combining E83.004 and (3.2), the new compatibility target can be stated
entirely on `L^2(0,L)`:

```text
BOUNDARY-GAMMA-EULER:
after applying the model vector, the Mobius gauge, the finite Fourier
projection and the safe Cauchy functional, the boundary commutator (3.2) plus
the Fourier compression defect tends to the correction required in GE-2 and
GE-3.                                                   (5.1)
```

The theorem must preserve the signed sum over `n` and `y`.  Estimating the
individual boundary operators before Mobius cancellation repeats the absolute
shell wall.

## 6. Status

```text
proved:
  exact one-sided-shift formula for H_L^A;
  exact boundary support formula for [S_y^*,S_z];
  localization of [H_L^A,Z] to boundary operators;
  impossibility of bounded global identity intertwining;

localized:
  GE-2 and GE-3 to BOUNDARY-GAMMA-EULER on one vector;

open:
  paired cancellation of the boundary commutator on the actual model vector;
  joint control of the Fourier compression defect;

next:
  use the exact Mobius-weighted kernel of E83.006 and the endpoint obstruction
  of E83.007 to formulate the smallest surviving scalar theorem.
```
