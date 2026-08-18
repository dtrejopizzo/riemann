# E101.041 - Heat tail bounds

## 1. Prime Gaussian tail

Let the arithmetic heat source be

```text
P(v)
 ={1/sqrt(pi v)}sum_(m>=2)Lambda(m)m^(-1/2)
   exp(-(log m)^2/(4v)).                             (1.1)
```

For a cutoff `X>=2`, write `ell=log X` and let `P_X` retain `m<=X`.

### Proposition 1.1

If `ell` is beyond the decreasing range of

```text
f(t)=log(t)t^(-1/2)exp(-(log t)^2/(4v)),             (1.2)
```

then

```text
0<=P(v)-P_X(v)<=B_prime(v,ell),                      (1.3)
```

where

```text
B_prime(v,ell)
 ={ell exp(-ell/2-ell^2/(4v))}/{sqrt(pi v)}

 +exp(v/4)[
    {2sqrt(v)/sqrt(pi)}exp(-(ell-v)^2/(4v))
    +v erfc((ell-v)/(2sqrt(v)))
  ].                                                 (1.4)
```

### Proof

Use `Lambda(m)<=log m` and the integral test:

```text
sum_(m>X)f(m)<=f(X)+integral_X^infinity f(t)dt.      (1.5)
```

With `u=log t`, the integral becomes

```text
exp(v/4)integral_ell^infinity
 u exp(-(u-v)^2/(4v))du.                             (1.6)
```

Splitting `u=(u-v)+v` evaluates (1.6) as

```text
exp(v/4)[
  2v exp(-(ell-v)^2/(4v))
  +v sqrt(pi v)erfc((ell-v)/(2sqrt(v)))
].                                                   (1.7)
```

Divide (1.5)--(1.7) by `sqrt(pi v)` to obtain (1.4). `QED`

For every fixed `v>0`, the bound tends to zero with Gaussian decay in `ell`.
It is locally uniform for `v` in compact subintervals of `(0,infinity)`.

## 2. External mesh heat tail

Put

```text
rho_k=2pi k/L,
a=4pi^2v/L^2.                                       (2.1)
```

The residual raw external divisor of E101.025 has heat trace

```text
Q_ext(L,N,v)
 =2exp(-aN^2)+4sum_(k>N)exp(-ak^2).                 (2.2)
```

### Proposition 2.1

For `N>=1`,

```text
0<=Q_ext(L,N,v)
 <=2exp(-aN^2)[1+1/(aN)].                           (2.3)
```

### Proof

Monotonicity and the Gaussian tail estimate give

```text
sum_(k>N)exp(-ak^2)
 <=integral_N^infinity exp(-at^2)dt
 <=exp(-aN^2)/(2aN).                                (2.4)
```

Substitute (2.4) into (2.2). `QED`

Thus the raw external tail disappears whenever

```text
vN^2/L^2->infinity.                                 (2.5)
```

The core family removes it exactly and needs no such estimate.

## 3. Cofinal heat scaling

For a fixed heat time, the two explicit tails are controlled by

```text
prime side:  L->infinity;
mesh side:   N/L->infinity.                         (3.1)
```

Uniformly for `v` in a compact interval `[v_0,V]`, it is enough to send

```text
L->infinity,
N/L->infinity,                                      (3.2)
```

with constants in (1.4) evaluated at the endpoints of the interval.

The numerical behavior in E101.040 has the same two-scale interpretation:

```text
small v:  more secular modes are needed because the heat window is broad;
large v:  a longer prime cutoff is needed for the archimedean-prime
          cancellation.                             (3.3)
```

## 4. What remains after the tail estimates

Propositions 1.1 and 2.1 close the explicit truncation tails.  They do not
control the build-dependent term

```text
2v integral_R u exp(-vu^2)Xi_(L,N)(u)du             (4.1)
```

in E101.040.  The remaining theorem is a uniform comparison between this
spectral-shift integral and

```text
H_A(v)-P_L(v)-Tr exp(-vD_(L,N)^2).                  (4.2)
```

Any proof which estimates the positive terms separately loses the signed
cancellation in (4.2).

## 5. Status

```text
proved:
  explicit Gaussian bound for the omitted von-Mangoldt tail;
  explicit Gaussian bound for the residual external mesh tail;
  rigorous cofinal scaling for both explicit tails;

open:
  the coupled core spectral-shift comparison (4.1)--(4.2).
```
