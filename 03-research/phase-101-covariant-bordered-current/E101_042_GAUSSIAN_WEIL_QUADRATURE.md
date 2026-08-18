# E101.042 - Gaussian Weil quadrature

## 1. Finite node functional

For the real secular roots of one core approximant, define

```text
Q_(L,N)(h)=sum_j h(kappa_(L,N,j)).                   (1.1)
```

Let `W_L` denote the centered Gamma-minus-prime functional with prime powers
restricted by `log m<=L`, in the normalization of E101.036.

For `v>0` and `j>=0`, put

```text
h_(j,v)(u)=u^(2j)exp(-vu^2).                         (1.2)
```

These are the Gaussian-monomial Weil tests of E101.038.

## 2. Exact quadrature identity

### Theorem 2.1

For every finite `L,N` and every `v>0`,

```text
Q_(L,N)(h_(0,v))=H_(L,N)(v),                        (2.1)

W_L(h_(0,v))=H_(E,L)(v),                            (2.2)

R_(L,N)(v)
 =Q_(L,N)(h_(0,v))-W_L(h_(0,v)).                    (2.3)
```

More generally,

```text
(-1)^j partial_v^j R_(L,N)(v)
 =Q_(L,N)(h_(j,v))-W_L(h_(j,v)).                    (2.4)
```

### Proof

Equation (2.1) is the spectral definition of the finite heat trace.  The
Fourier transform of `exp(-vu^2)` is a Gaussian in the dual variable.  In the
centered explicit formula, its prime-power value at `log m` is exactly

```text
{1/sqrt(pi v)}exp(-(log m)^2/(4v)),                 (2.5)
```

with the normalization already fixed by E101.036(1.5).  The pole and Gamma
part is `H_A(v)`.  Hence the truncated explicit formula is

```text
W_L(h_(0,v))=H_A(v)-P_L(v)=H_(E,L)(v),              (2.6)
```

which proves (2.2).  Equation (2.3) is E101.039(2.2).  Differentiation is
termwise on the finite node side and under the absolutely convergent Gaussian
integrals on the arithmetic side, giving (2.4). `QED`

Thus `R_(L,N)` is an equal-weight Gaussian quadrature error for the finite
Weil functional.

## 3. One heat interval is enough

### Lemma 3.1

Let

```text
F(z)=integral_[0,infinity)exp(-zt)d mu(t)            (3.1)
```

for a positive measure `mu`, initially convergent on `Re z>a`.  If `F`
extends holomorphically through the real point `a`, then the integral in
(3.1) converges on `Re z>a-epsilon` for some `epsilon>0`.

### Proof

Choose a real `x>a` inside a disk of holomorphy of radius `R>x-a`.  Cauchy's
estimate gives

```text
|F^(n)(x)|<=M n!/R^n.                               (3.2)
```

Positivity and differentiation in the original half-plane give

```text
|F^(n)(x)|
 =integral t^n exp(-xt)d mu(t).                     (3.3)
```

For `0<delta<R`, monotone convergence and (3.2)--(3.3) yield

```text
integral exp(-(x-delta)t)d mu(t)
 =sum_(n>=0){delta^n/n!}
   integral t^n exp(-xt)d mu(t)
 <=M sum_(n>=0)(delta/R)^n<infinity.                (3.4)
```

Take `delta>x-a`. `QED`

Consequently, the finite abscissa of convergence of a positive Laplace
transform is a real singularity.

### Theorem 3.2

Let `I` be any nonempty open interval compactly contained in `(0,infinity)`.
Assume, along one directed family,

```text
R_(L_alpha,N_alpha)(v)->0
for every v in I.                                   (3.5)
```

Then `Omega7` holds.

### Proof

By E101.041, `H_(E,L_alpha)(v)->H_Xi(v)` for each fixed `v>0`.  Hence (3.5)
gives

```text
H_alpha(v)->H_Xi(v)
for v in I.                                         (3.6)
```

Choose `a<b` inside `I`.  On the half-plane `Re z>=a`,

```text
|H_alpha(z)|<=H_alpha(a).                           (3.7)
```

Equation (3.6) at `a` bounds the right side of (3.7), so the finite heat
traces form a normal family on `Re z>a`.  Every analytic sublimit agrees with
`H_Xi` on `(a,b)`; the identity theorem makes the sublimit unique.  Hence
`H_Xi` is a pointwise limit of completely monotone functions on
`(a,infinity)` and is itself completely monotone there.

Bernstein's theorem supplies a positive measure whose Laplace transform is
`H_Xi` on that half-plane.  Let `sigma_c<=a` be its abscissa of convergence.
The arithmetic formulas E101.036(1.4)--(2.2) make `H_Xi` holomorphic
throughout `Re v>0`.  If `sigma_c>0`, the analytic continuation would be
holomorphic at `sigma_c`, and Lemma 3.1 would extend the positive Laplace
integral to the left of `sigma_c`, a contradiction.  Therefore
`sigma_c<=0`.  The representation converges for every `Re v>0`, so `H_Xi`
is completely monotone on `(0,infinity)`.  E101.036 gives `Omega7`. `QED`

## 4. One-point jet version

At a fixed `v_0>0`, local quadrature convergence is equivalently the complete
Gaussian jet

```text
Q_(L,N)(h_(j,v_0))-W_L(h_(j,v_0))->0
for every j>=0,                                     (4.1)
```

together with a uniform analytic bound in a neighborhood of `v_0`.  Equation
(2.4) then reconstructs `R_(L,N)` by its Taylor series.

E101.037 shows why no finite truncation of (4.1) can suffice.

## 5. What a proof must establish

The remaining theorem can be stated as

```text
GAUSSIAN-WEIL-QUADRATURE:
Q_(L_alpha,N_alpha)(h_(0,v))
 -W_(L_alpha)(h_(0,v))->0
on one nonempty heat interval.                      (5.1)
```

The finite nodes are real for both the zeta and planted constructions, so
real-rootedness alone cannot prove (5.1).  The proof must use the arithmetic
dependence of the node functional on the Gamma-prime cell matrix.

## 6. Status

```text
proved:
  exact equal-weight Gaussian quadrature identity;
  exact derivative identity for every Gaussian-monomial test;
  reduction from all heat times to one nonempty heat interval;
  one-point infinite-jet version;

open:
  GAUSSIAN-WEIL-QUADRATURE in (5.1).
```
