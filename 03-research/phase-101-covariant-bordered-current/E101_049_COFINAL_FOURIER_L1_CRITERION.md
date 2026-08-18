# E101.049 - Cofinal Fourier l1 criterion

## 1. Finite Fourier coefficients with boundary mismatch

Let `f in W^(2,1)(0,L)` and define

```text
f_hat(n)=(1/L)integral_0^L
         f(x)exp(-2pi i n x/L)dx.                    (1.1)
```

Write

```text
Delta_0(f)=|f(L)-f(0)|,
Delta_1(f)=|f'(L)-f'(0)|.                            (1.2)
```

### Theorem 1.1

For every integer `N>=1`,

```text
sum_(|n|<=N)|f_hat(n)|
<=||f||_1/L
  +[Delta_0(f)/pi]H_N
  +(L/12)[Delta_1(f)+||f''||_1],                    (1.3)
```

where `H_N=sum_(n=1)^N 1/n`.

### Proof

The zero coefficient satisfies

```text
|f_hat(0)|<=||f||_1/L.                               (1.4)
```

For `n!=0`, integrate twice by parts.  Since
`exp(-2pi i n)=1`, one obtains

```text
|f_hat(n)|
<=Delta_0(f)/(2pi|n|)
  +L[Delta_1(f)+||f''||_1]/(4pi^2n^2).              (1.5)
```

Sum over positive and negative `n`, and use

```text
sum_(n=1)^infinity 1/n^2=pi^2/6.                    (1.6)
```

Equations (1.4)--(1.6) give (1.3). `QED`

The logarithm in (1.3) is necessary when the periodic boundary values do not
match.  Pointwise smallness of the boundary jump alone is therefore not a
uniform `l1` theorem.

## 2. Cofinal diagonal theorem

Let `L->infinity` and let `f_L in W^(2,1)(0,L)`.  Put

```text
A_L=||f_L||_1/L
    +(L/12)[Delta_1(f_L)+||f_L''||_1],
B_L=Delta_0(f_L).                                    (2.1)
```

### Theorem 2.1

Assume

```text
A_L->0,
B_L log(2+L)->0.                                     (2.2)
```

Then there is an integer diagonal `N(L)` such that

```text
N(L)/L->infinity,
B_L log N(L)->0,                                     (2.3)
```

and consequently

```text
sum_(|n|<=N(L))|f_hat_L(n)|->0.                     (2.4)
```

### Proof

Choose a positive function `omega_L->infinity` sufficiently slowly that

```text
B_L[log(2+L)+omega_L]->0.                            (2.5)
```

This is possible by the second hypothesis in (2.2).  Set

```text
N(L)=ceil[L exp(omega_L)].                            (2.6)
```

Then `N(L)/L->infinity`, while

```text
log N(L)<=log(2+L)+omega_L+1.                        (2.7)
```

Thus (2.3) follows from (2.5).  Since `H_N<=1+log N`, substitution in
Theorem 1.1 proves (2.4). `QED`

No convergence rate for `N/L` is imposed.  This is exactly the flexibility
of a cofinal directed limit.

## 3. Periodic improvement

If `f_L(L)=f_L(0)`, then `B_L=0` and the diagonal restriction disappears:

```text
sum_(|n|<=N)|f_hat_L(n)|
<=A_L                                                   (3.1)
```

for every `N`.  If the first derivative also matches, then

```text
A_L=||f_L||_1/L+(L/12)||f_L''||_1.                  (3.2)
```

Thus exact periodic localization is stronger than needed; a boundary jump
with `B_L log L->0` is sufficient.

## 4. Safe Cauchy observations and one derivative

Let

```text
c_z(n)=z/(z-d_n),
d_n=2pi n/L.                                         (4.1)
```

On a compact subset of the imaginary safe axis bounded away from zero,

```text
sup_(L,n,z)|c_z(n)|<infinity,
sup_(L,n,z)|partial_z c_z(n)|<infinity.              (4.2)
```

Indeed,

```text
partial_z c_z(n)=-d_n/(z-d_n)^2,                    (4.3)
```

whose modulus is uniformly bounded for real `d_n` and safe `z`.

Consequently (2.4) implies, locally uniformly with one safe derivative,

```text
sum_(|n|<=N(L))c_z(n)f_hat_L(n)->0.                 (4.4)
```

The same conclusion holds for the scalar normalization row `ell`, because

```text
|sum_(|n|<=N)f_hat_L(n)|
<=sum_(|n|<=N)|f_hat_L(n)|.                          (4.5)
```

## 5. Application to PROLATE-INBAND

In E101.047 take

```text
f_L=k_lambda-k.                                      (5.1)
```

The exact remaining source estimate is now the quantitative package

```text
PROLATE-W21:
  ||f_L||_1/L
  +L[Delta_1(f_L)+||f_L''||_1] ->0,
  Delta_0(f_L)log(2+L)->0.                           (5.2)
```

By Theorem 2.1, `PROLATE-W21` supplies a cofinal `N(L)` for which the `l1`
condition E101.047(4.4) holds.  Equations (4.4)--(4.5) then close the direct
source observation in both value and first-derivative topologies.

The double-exponential endpoint estimates recorded in P76.065 address the
two boundary terms in (5.2).  The remaining analytic input is the integrated
bulk estimate

```text
||k_lambda-k||_1/L
 +L||(k_lambda-k)''||_1 ->0.                         (5.3)
```

It must be proved for the precise prolate localization; transform convergence
alone does not imply (5.3).

## 6. Revised status of RT-0

The order-of-limits issue in `RT-0` is closed: once (5.2) holds, an admissible
cofinal Fourier diagonal exists and is explicit up to the slowly increasing
function `omega_L`.

The only open part of `RT-0` is `PROLATE-W21`, principally the bulk estimate
(5.3).  This is a source approximation theorem and no bordered inverse or
arithmetic discriminant occurs in it.

## 7. Status

```text
proved:
  sharp finite l1 bound with boundary mismatch;
  cofinal diagonal theorem compatible with N/L->infinity;
  locally uniform safe Cauchy convergence with one derivative;

closed:
  the Fourier-diagonal selection mechanism in RT-0;

open:
  PROLATE-W21 for the precise Connes localization;
  RT-2 and RT-3 from E101.048.
```
