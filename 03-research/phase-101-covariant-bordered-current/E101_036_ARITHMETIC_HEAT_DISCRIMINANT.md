# E101.036 - Arithmetic heat discriminant

## 1. Inverse Laplace coordinate

For `x>1/4`, put

```text
sigma=sqrt(x),
s=1/2+sigma.                                         (1.1)
```

The arithmetic target is

```text
g_Xi(x)
 =A(s)/(2sigma)
  -sum_(m>=2)Lambda(m)m^(-1/2)
     exp(-sigma log m)/sigma,                        (1.2)

A(s)=2/s+2/(s-1)-log pi+psi(s/2).                   (1.3)
```

Define

```text
H_Xi(v)=H_A(v)-P(v),
v>0,                                                 (1.4)
```

where

```text
P(v)
 ={1/sqrt(pi v)}sum_(m>=2)Lambda(m)m^(-1/2)
   exp(-(log m)^2/(4v)).                             (1.5)
```

For every fixed `v>0`, the Gaussian in `log m` makes (1.5) absolutely
convergent.

## 2. Explicit archimedean heat term

The pole and Gamma terms in (1.3) have inverse Laplace transform

```text
H_A(v)
 =2exp(v/4)-log(pi)/(2sqrt(pi v))+H_psi(v),          (2.1)
```

with

```text
H_psi(v)
 ={1/(2sqrt(pi v))}integral_0^infinity [
    exp(-u)/u
    -{exp(-u/4)/(1-exp(-u))}
       exp(-u^2/(16v))
   ]du.                                              (2.2)
```

The integrand in (2.2) is bounded at `u=0` after cancellation and is
integrable at infinity.

### Proposition 2.1

For `x>1/4`,

```text
integral_0^infinity exp(-xv)H_A(v)dv
 =A(1/2+sqrt(x))/(2sqrt(x)).                         (2.3)
```

### Proof

For any real `a` for which the Laplace integral converges,

```text
L^(-1){1/[sqrt(x)(sqrt(x)+a)]}(v)
 =exp(a^2v)erfc(a sqrt(v)).                          (2.4)
```

The terms `2/s` and `2/(s-1)` in (1.3), after division by `2sqrt(x)`,
correspond to `a=1/2` and `a=-1/2`.  Their inverse transforms add to

```text
exp(v/4)[erfc(sqrt(v)/2)+erfc(-sqrt(v)/2)]
 =2exp(v/4).                                         (2.5)
```

The constant `-log pi` gives the second term of (2.1).  Finally use the
convergent integral representation

```text
psi(z)=integral_0^infinity[
          exp(-u)/u-exp(-zu)/(1-exp(-u))
        ]du                                         (2.6)
```

with `z=1/4+sqrt(x)/2`, and the subordination formula

```text
L^(-1){exp(-b sqrt(x))/sqrt(x)}(v)
 ={1/sqrt(pi v)}exp(-b^2/(4v)).                     (2.7)
```

The cancellation at `u=0` permits the terms to remain paired.  Equations
(2.5)--(2.7) give (2.1)--(2.3). `QED`

## 3. Exact arithmetic heat identity

### Theorem 3.1

For every `x>1/4`,

```text
g_Xi(x)
 =integral_0^infinity exp(-xv)H_Xi(v)dv.            (3.1)
```

### Proof

Proposition 2.1 treats the archimedean part.  For `u>0`,

```text
integral_0^infinity
 exp(-xv-u^2/(4v))/sqrt(pi v)dv
 =exp(-u sqrt(x))/sqrt(x).                           (3.2)
```

Apply (3.2) with `u=log m`.  Positivity permits Tonelli's theorem, and the
resulting von-Mangoldt series converges for
`1/2+sqrt(x)>1`.  This gives the prime part of (1.2), with its sign, and proves
(3.1). `QED`

Equation (3.1) is constructed entirely from Gamma data and von-Mangoldt
weights.

## 4. Complete-monotonicity equivalence

### Theorem 4.1

The following are equivalent:

```text
(i)   Omega7;

(ii)  H_Xi is completely monotone on (0,infinity);

(iii) (-1)^j partial_v^j H_Xi(v)>=0
      for every j>=0 and every v>0.                 (4.1)
```

### Proof

If `Omega7` holds, E101.021 gives a positive Stieltjes measure `mu`, and

```text
H_Xi(v)=integral_[0,infinity)exp(-tv)d mu(t).        (4.2)
```

Indeed, the right side of (4.2) and the arithmetic function (1.4) have the
same Laplace transform by (3.1).  Uniqueness of the Laplace transform gives
equality almost everywhere, and smoothness on `v>0` gives pointwise equality.
Differentiation under the integral then gives (iii).

Conversely, (ii) and Bernstein's theorem give a positive measure `mu` for
which (4.2) holds.  Substitute (4.2) into (3.1) and apply Tonelli:

```text
g_Xi(x)=integral_[0,infinity)d mu(t)/(x+t).          (4.3)
```

Thus `g_Xi` is Stieltjes, and E101.021 gives `Omega7`.  The equivalence of
(ii) and (iii) is the defining complete-monotonicity theorem. `QED`

## 5. The force-bearing inequalities

The remaining theorem can now be written without a finite secular limit:

```text
(-1)^j partial_v^j [H_A(v)-P(v)]>=0
for all j>=0 and v>0.                               (5.1)
```

The case `j=0` is only the Gaussian prime inequality

```text
P(v)<=H_A(v).                                       (5.2)
```

It is necessary but is not the full discriminant.  All derivative orders in
(5.1) are required.  The positive Gaussian kernel in (1.5) does not by itself
control the signs after differentiation.

## 6. Relation to the integer current

For every finite core approximant,

```text
d lambda_alpha(v)
 =exp(-n_0v)H_alpha(v)dv.                           (6.1)
```

Accordingly, the beta-mixture condition of E101.033 is exactly the compact
image of complete monotonicity of the heat trace.  E101.034 tests its Laplace
moments simultaneously through the kernel

```text
exp(-n_0v)/(1-q exp(-v)).                            (6.2)
```

Thus the disk current and the arithmetic heat discriminant are two exact
coordinates for the same force-bearing assertion.

## 7. Status

```text
proved:
  explicit archimedean inverse Laplace kernel;
  explicit von-Mangoldt Gaussian heat source;
  exact arithmetic heat identity for g_Xi;
  complete monotonicity equivalent to Omega7;
  identification of the full derivative hierarchy as the remaining
  arithmetic inequality;

open:
  the complete-monotonicity inequalities in (5.1).
```
