# E83.004 - Exact truncated-shift representation of the CCM cells

## 1. One-sided shift semigroup

Work on `L^2(0,L)` and define, for `0<=y<=L`,

```text
(S_y f)(t)=1_[y,L](t) f(t-y).                          (1.1)
```

Set `S_y=0` for `y>L`.  Then

```text
S_y S_z=S_{y+z}                                       (1.2)
```

for all nonnegative `y,z`, with the zero convention when `y+z>L`.

Let

```text
phi_n(t)=L^(-1/2) exp(i d_n t),
d_n=2 pi n/L.                                          (1.3)
```

### Theorem 1.1 - cell representation

The CCM cell matrix satisfies

```text
q_mn(y)=<phi_m,(S_y+S_y^*)phi_n>.                      (1.4)
```

### Proof

For `m=n`,

```text
<phi_n,S_y phi_n>=(1-y/L)exp(-i d_n y),
```

so its sum with the adjoint matrix element is

```text
2(1-y/L)cos(d_n y)=q_nn(y).                            (1.5)
```

For `m!=n`, direct integration gives

```text
<phi_m,S_y phi_n>
 =[exp(-i d_n y)-exp(-i d_m y)]/[2 pi i(n-m)].         (1.6)
```

Adding the conjugate-transposed element yields

```text
[sin(d_m y)-sin(d_n y)]/[pi(n-m)]=q_mn(y).             (1.7)
```

This proves (1.4). `QED`

The finite CCM cell is the Fourier compression

```text
Q_y^(N)=P_N(S_y+S_y^*)P_N.                             (1.8)
```

## 2. Why the symmetric cells are not a semigroup

The Hermitian cells themselves do not multiply according to the additive
parameter.  Already on the zero-frequency diagonal,

```text
(q_00(y)/2)(q_00(z)/2)-q_00(y+z)/2
 = yz/L^2.                                             (2.1)
```

For `y=z=L/2`, the defect is `1/4`.  Hence it is not uniformly negligible on
the full prime support.  Mobius inversion may not be transported by replacing
each multiplicative shift directly with the symmetric cell `Q_y`.

The one-sided dilation (1.1) is the required repair: it carries the exact
semigroup law, and symmetrization is postponed until after the Euler connection
has been formed.

## 3. Position derivation

Let `X` be multiplication by `t` on `L^2(0,L)`.  On its natural common domain,

```text
[X,S_y]=y S_y.                                         (3.1)
```

### Proof

For `t>=y`,

```text
(X S_y f)(t)=t f(t-y),
(S_y X f)(t)=(t-y)f(t-y).
```

Their difference is `y(S_yf)(t)`; both sides vanish for `t<y`. `QED`

Thus the scale derivation of the Euler semigroup is represented exactly by
the commutator with `X`.

## 4. Exact finite Euler unit

For `epsilon>=0`, define bounded finite sums

```text
Z_{L,epsilon}
 = sum_{n<=exp(L)} n^(-1/2-epsilon) S_{log n},

M_{L,epsilon}
 = sum_{n<=exp(L)} mu(n)n^(-1/2-epsilon) S_{log n}.     (4.1)
```

### Theorem 4.1

On `L^2(0,L)`,

```text
M_{L,epsilon}Z_{L,epsilon}
=Z_{L,epsilon}M_{L,epsilon}=I,                         (4.2)

M_{L,epsilon}[X,Z_{L,epsilon}]
 = sum_{n<=exp(L)} Lambda(n)n^(-1/2-epsilon)S_{log n}. (4.3)
```

### Proof

By (1.2), the coefficient of `S_{log N}` in either product in (4.2) is

```text
N^(-1/2-epsilon) sum_{d|N}mu(d),                       (4.4)
```

which is one for `N=1` and zero otherwise.  Products with `N>exp(L)` vanish
because their shift length exceeds `L`.  This proves (4.2).

By (3.1),

```text
[X,Z_{L,epsilon}]
 =sum_n (log n)n^(-1/2-epsilon)S_{log n}.               (4.5)
```

Multiplication by `M_{L,epsilon}` and the convolution identity
`mu*log=Lambda` give (4.3). `QED`

## 5. Recovery of the prime CCM matrix

Let

```text
V_{L,epsilon}
 =M_{L,epsilon}[X,Z_{L,epsilon}].                      (5.1)
```

Using Theorem 1.1,

```text
<phi_m,(V_{L,0}+V_{L,0}^*)phi_n>
 =sum_{r<=exp(L)}Lambda(r)r^(-1/2)q_mn(log r).          (5.2)
```

The right side is exactly the prime-power part of the finite CCM entry before
its inherited overall sign is applied.  Hence the Euler--Mobius connection is
now represented in the same interval and Fourier coordinates as the CCM
cells.

No zero information and no limiting argument is used.

## 6. Finite Fourier compression

The physical semigroup law holds before Fourier compression.  In general,

```text
P_N S_y P_N S_z P_N != P_N S_{y+z}P_N,                (6.1)
```

because modes outside the finite mesh intervene.  The defect is a Fourier
shell term.  Any finite-section coboundary must keep this compression defect
and control it through the already isolated `RDP-SHELL` mechanism.

## 7. Consequence for GE-1--GE-3

The theorem closes the representation half of `GE-1` for the prime current:

```text
Euler connection
 -> exact one-sided interval operator V_L
 -> prime CCM matrix V_L+V_L^*.                        (7.1)
```

The remaining Gamma--Euler compatibility is no longer the construction of a
map between unrelated spaces.  Both sides act on `L^2(0,L)`.  The live theorem
is to compare the archimedean CCM operator and the position derivation on the
single Euler-generated corrector, including the Fourier-shell defect.

## 8. Status

```text
proved:
  Q_y is the Fourier matrix of S_y+S_y^*;
  S_y is an exact truncated semigroup;
  [X,S_y]=yS_y;
  exact finite Mobius inversion and Euler connection on L^2(0,L);
  exact recovery of the prime CCM matrix;

refuted:
  direct use of the symmetric cells as a semigroup representation;

closed:
  canonical physical-space realization of the Euler prime current;

open:
  one-vector compatibility of the archimedean CCM part with X;
  the finite Fourier compression defect through RDP-SHELL;

next:
  express the archimedean CCM operator in the same one-sided shift calculus
  and compute its commutator with the Euler unit.
```

