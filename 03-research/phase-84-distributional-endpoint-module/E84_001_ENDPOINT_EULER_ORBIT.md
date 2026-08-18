# E84.001 - Endpoint Euler orbit and Fourier symbols

## 1. Atomic endpoint module

Let `E_L` be the vector space of finite atomic distributions on `[0,L]`.
For `0<=y<=L`, define

```text
S_y delta_x=delta_{x+y},  x+y<=L,
S_y delta_x=0,            x+y>L,                       (1.1)

X delta_x=x delta_x.                                  (1.2)
```

Then

```text
S_yS_z=S_{y+z},
[X,S_y]=yS_y,
X delta_0=0.                                          (1.3)
```

All identities are algebraic on `E_L`.

## 2. Exact Euler orbit

For `sigma=1/2+epsilon`, set

```text
Z=sum_{n<=exp(L)}n^(-sigma)S_{log n},
M=sum_{d<=exp(L)}mu(d)d^(-sigma)S_{log d}.             (2.1)
```

The semigroup calculation of E83.004 remains valid on `E_L`, so

```text
MZ=ZM=I.                                              (2.2)
```

Applying the connection to the ground mass gives

```text
M[X,Z]delta_0
 =sum_{n<=exp(L)}Lambda(n)n^(-sigma)delta_{log n}
 =:nu_{L,sigma}^P.                                    (2.3)
```

Thus the von Mangoldt measure is the covariant derivative of the endpoint
Euler orbit.

## 3. Finite Fourier map

For the mesh `d_m=2pi m/L`, define

```text
F_N(T)_m=L^(-1/2)<T,exp(-i d_m t)>.                   (3.1)
```

Then

```text
F_N(delta_0)_m=L^(-1/2),                              (3.2)

F_N(nu_{L,sigma}^P)_m
 =L^(-1/2)sum_{n<=exp(L)}Lambda(n)n^(-sigma)
   exp(-i d_m log n).                                 (3.3)
```

Writing the last sum as `P_{L,sigma}(d_m)`, one obtains

```text
Re P_{L,sigma}(t)
 =sum_n Lambda(n)n^(-sigma)cos(t log n),               (3.4)

Im P_{L,sigma}(t)
 =-sum_n Lambda(n)n^(-sigma)sin(t log n).              (3.5)
```

At `sigma=1/2`, (3.4)--(3.5) are exactly the cosine and sine prime-power
symbols appearing in the finite Weil functional, with the inherited sign
chosen when the full Gamma-prime functional is assembled.

## 4. Boundary vector already present

Equation (3.2) proves that the constant mesh vector is not an auxiliary
algebraic generator.  It is the Fourier image of the endpoint ground mass:

```text
1=sqrt(L) F_N(delta_0).                                (4.1)
```

Likewise the prime contribution to the vector `s_N=(S_L(d_m))_m` is the
imaginary part of (3.3).  Hence both generators in

`alpha_b s_N+beta_b 1` have a canonical endpoint origin.

The remaining issue is the archimedean and polar contribution to `s_N`,
including its renormalized mass at the origin.

## 5. Status

```text
proved:
  exact distributional shift module;
  exact Euler orbit of delta_0;
  exact von Mangoldt current;
  exact Fourier recovery of the constant and prime sine generators;

open:
  the full archimedean endpoint distribution;
  exact recovery of the coupled source after boundary projection.
```

