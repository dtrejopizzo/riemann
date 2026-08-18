# E101.053 - Prolate BV-moment transfer

## 1. Multiplicative coordinate

Let

```text
E(g)(u)=u^(1/2) sum_(n>=1) g(nu),
lambda=e^(L/2),
g_lambda=h_lambda-h.                                (1.1)
```

The prolate combination `h_lambda` and the Hermite combination `h` are
normalized in the same scale and both have vanishing integral.  Hence

```text
integral_0^infinity g_lambda(t)dt=0.                 (1.2)
```

On the logarithmic interval used by the finite Fourier model, put

```text
F_lambda(x)=E(g_lambda)(e^x/lambda),
0<=x<=L.                                             (1.3)
```

Thus `F_lambda` is precisely the physical error `k_lambda-k` in the
coordinate of E101.050.  The right endpoint `x=L` corresponds to
`u=lambda`; the left endpoint `x=0` corresponds to `u=lambda^(-1)`.

The purpose of this document is to convert the endpoint hypothesis of
E101.050 into explicit estimates on `g_lambda` before any Fourier
projection is taken.

## 2. Weighted additive moments

Fix a compact safe interval

```text
K=[sigma_0,sigma_1],
1/2<sigma_0<=sigma_1.                                (2.1)
```

For `sigma in K`, define

```text
M_sigma(g)
=integral_0^infinity t^(sigma-1/2)|g(t)|dt,

M_sigma^log(g)
=integral_0^infinity
  t^(sigma-1/2)|log t||g(t)|dt.                      (2.2)
```

Set

```text
A_K(g)=sup_(sigma in K)
       [M_sigma(g)+M_sigma^log(g)].                  (2.3)
```

The restriction `sigma_0>1/2` is the exact threshold at which the integer
sum appearing below is absolutely summable.

## 3. Right-endpoint transfer

### Theorem 3.1

Suppose `A_K(g)<infinity`.  Then

```text
sup_(sigma in K)
integral_0^L (1+L-x)|E(g)(e^x/lambda)|
               e^(-sigma(L-x))dx

<=C_K lambda^(-sigma_0)(1+log lambda)A_K(g),         (3.1)
```

where `C_K` depends only on the safe interval.

### Proof

Write `u=e^x/lambda`.  Then `dx=du/u` and

```text
L-x=log(lambda/u).                                   (3.2)
```

The left side at a fixed `sigma` is

```text
lambda^(-sigma)
integral_(lambda^(-1))^lambda
 (1+log(lambda/u))|E(g)(u)|u^sigma du/u.             (3.3)
```

Use the definition of `E`, apply the triangle inequality, and put `t=nu`
in the term indexed by `n`.  The power of `n` is

```text
n^(-sigma-1/2).                                      (3.4)
```

On the original integration domain,

```text
1+log(lambda/u)
<=1+log lambda+log n+|log t|.                        (3.5)
```

Extending the resulting nonnegative `t` integrals to `(0,infinity)` gives

```text
lambda^(-sigma)
{[(1+log lambda)zeta(p)-zeta'(p)]M_sigma(g)
  +zeta(p)M_sigma^log(g)},
p=sigma+1/2.                                         (3.6)
```

Since `p>=sigma_0+1/2>1`, both `zeta(p)` and `-zeta'(p)` are uniformly
bounded on `K`.  Also `lambda^(-sigma)<=lambda^(-sigma_0)`.  This proves
(3.1). `QED`

The proof uses only absolute summation on the physical function `g`.  It
does not invoke the Fourier transform of a prolate function extended by
zero.

## 4. Left-endpoint transfer by zero-mass cancellation

Let `Var(g)` denote total variation on `[0,infinity)`, including any jump
created by extension by zero.

### Lemma 4.1

If `g` is integrable, has finite total variation, and has integral zero,
then for every `u>0`,

```text
|E(g)(u)|<=u^(1/2)Var(g).                             (4.1)
```

### Proof

Partition `[0,infinity)` into the intervals `[(n-1)u,nu]`.  On each
interval,

```text
|u g(nu)-integral_((n-1)u)^(nu)g(t)dt|
<=u Var_[((n-1)u,nu)](g).                            (4.2)
```

Summing and using the zero integral gives

```text
|u sum_(n>=1)g(nu)|<=u Var(g).                       (4.3)
```

Multiplication by `u^(-1/2)` proves (4.1). `QED`

### Theorem 4.2

Under the hypotheses of Lemma 4.1,

```text
sup_(sigma in K)
integral_0^L (1+x)|E(g)(e^x/lambda)|e^(-sigma x)dx
<=C_K lambda^(-1/2)Var(g).                           (4.4)
```

### Proof

Use `u=e^x/lambda`, then put `t=lambda u`.  Lemma 4.1 gives

```text
lambda^(-sigma)
integral_(lambda^(-1))^lambda
 (1+log(lambda u))u^(1/2-sigma)du/u

=lambda^(-1/2)
  integral_1^(lambda^2)(1+log t)t^(-sigma-1/2)dt.    (4.5)
```

The last integral is uniformly bounded for `sigma>=sigma_0>1/2`.
Multiplication by `Var(g)` proves (4.4). `QED`

This is the main cancellation.  A direct absolute estimate of the many
terms sampled at `u=lambda^(-1)` would lose the zero integral.  The bounded
variation estimate retains it exactly.

## 5. Endpoint traces

Lemma 4.1 immediately yields

```text
|F_lambda(0)|
<=lambda^(-1/2)Var(g_lambda).                        (5.1)
```

At the opposite endpoint, the support of `h_lambda` in
`[-lambda,lambda]` gives

```text
|F_lambda(L)|
<=lambda^(1/2)|h_lambda(lambda)|
 +lambda^(1/2)sum_(n>=1)|h(nlambda)|.                (5.2)
```

The second term tends to zero faster than every inverse power because `h`
is a fixed Hermite combination.  The only prolate trace still requiring an
estimate is therefore

```text
lambda^(1/2)|h_lambda(lambda)|->0.                   (5.3)
```

The value at the endpoint is understood as the interior trace before
extension by zero.

## 6. Sufficient prolate package

Define `PROLATE-BV-MOMENT(K)` by the three conditions

```text
A_K(g_lambda)
 =o(lambda^(sigma_0)/(1+log lambda)),

Var(g_lambda)=o(lambda^(1/2)),

lambda^(1/2)|h_lambda(lambda)|->0.                   (6.1)
```

### Theorem 6.1

`PROLATE-BV-MOMENT(K)` implies `PROLATE-ENDPOINT` of E101.050 on `K`.
Consequently, it implies the complete cofinal in-band observation

```text
q_(N,z)P_N(k_lambda-k)->0                            (6.2)
```

bilaterally and locally uniformly with one safe derivative along a diagonal
with `N/L->infinity`.

### Proof

Apply Theorem 3.1 to the upper boundary layer and Theorem 4.2 to the lower
boundary layer.  Conditions (6.1) make both bounds tend to zero.  Equations
(5.1)--(5.3) give

```text
F_lambda(0)+F_lambda(L)->0.                          (6.3)
```

These are exactly the hypotheses in E101.050(6.2).  Its endpoint theorem and
fixed-`L` Fourier diagonal prove (6.2). `QED`

A convenient stronger package is

```text
sup_lambda A_K(g_lambda)<infinity,
sup_lambda Var(g_lambda)<infinity,
lambda^(1/2)|h_lambda(lambda)|->0.                   (6.4)
```

No convergence in a global second-derivative norm is required.

## 7. What the classical prolate asymptotic must supply

The construction of `h_lambda` uses the fixed even prolate modes of orders
zero and four, combined so that their integral vanishes.  The usual
fixed-order prolate-to-Hermite localization is stronger than pointwise
convergence on compact sets if it supplies all three estimates in (6.4):

```text
uniform polynomially weighted L1 localization;
uniform bounded variation after extension by zero;
decay of the boundary trace at t=lambda.             (7.1)
```

The first item controls `A_K`; the second controls the Riemann-sum defect;
the third controls the symmetric Fourier normalization row.  These are now
the exact norms that must be extracted from the fixed-order prolate
asymptotic.  Qualitative local convergence alone is insufficient.

The exponentially small angle defects `1-chi_0` and `1-chi_2` control the
failure of simultaneous time and frequency localization.  They do not, by
themselves, state the three norms in (7.1).  A proof of (7.1) must therefore
either be imported with its normalization and uniform remainders, or derived
directly from the fixed-order prolate differential equation.

## 8. Separation from the Fourier collar

Extending a nonzero prolate endpoint trace by zero creates a Fourier tail of
order `1/|xi|`.  Taking an absolute weighted moment of that transform would
therefore be invalid even when the endpoint trace is exponentially small.

The argument above avoids that false requirement:

```text
right endpoint: physical weighted moments of g_lambda;
left endpoint:  zero-mass Riemann-sum cancellation and variation;
Fourier collar: retained in RT-2, where its signed tail is recombined.     (8.1)
```

Thus RT-0 does not borrow the cancellation that belongs to RT-2.

## 9. Revised RT-0 ledger

```text
RT-0a  periodic Cauchy endpoint theorem;                    proved;
RT-0b  fixed-L Fourier diagonal and N/L compatibility;      proved;
RT-0c  additive endpoint transfer E101.053;                 proved;
RT-0d  PROLATE-BV-MOMENT for h_lambda-h;                    open.  (9.1)
```

The remaining point `RT-0d` is a precise fixed-order prolate estimate.  It
contains no zero set, prime sum, or positivity assertion.  It remains in
Phase 101 because it is part of the same covariant determinant reduction,
not a new mathematical regime.
