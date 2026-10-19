# R161_026 — The Gamma-pole energy is a positive Hankel boundary derivative

## 0. Verdict

The positive residue energy of `R161_025` is not an artificial weighted moment sum. After introducing a positive
boundary displacement `delta`, it is exactly a Hankel form built from the differentiated positive-odd tail of the
Gamma Levy kernel. Equivalently, it is minus one half of the displacement derivative of a positive Gamma-Hankel
energy.

This identifies the discrete pole detector with a literal additive-reflection boundary object. It is therefore
compatible with the Poisson/Fourier side of `(PC-ren)` and supplies a canonical quadratic target for the
sum--product construction.

## 1. Positive-odd Gamma tail

For `v>0`, the Gamma Levy density used throughout the corpus is

```
c_Gamma(v)=exp(-v/2)/(1-exp(-2v))
          =sum_(m>=0) exp(-(2m+1/2)v).                            (1.1)
```

Remove the first Tate mode and put

```
k_Gamma^+(v):=c_Gamma(v)-exp(-v/2)
             =sum_(m>=1)exp(-a_m v),
a_m:=2m+1/2.                                                      (1.2)
```

Termwise differentiation is absolute on every `v>=v_0>0`, and gives

```
-(k_Gamma^+)'(v)=sum_(m>=1)a_m exp(-a_m v)>0.                    (1.3)
```

The scalar positivity in (1.3) is stronger: the associated Hankel kernel is positive definite because it is a sum
of positive rank-one kernels.

## 2. Shifted pole and Hankel energies

For `delta>0`, define

```
B_(T,delta)^Gamma(F)
 :=sum_(m>=1)exp(-2a_m(T+delta))|K_F(a_m)|^2,                    (2.1)

D_(T,delta)^Gamma(F)
 :=sum_(m>=1)a_m exp(-2a_m(T+delta))|K_F(a_m)|^2.                (2.2)
```

Cauchy--Schwarz and the compact support of `F` give

```
D_(T,delta)^Gamma(F)
 <=(1/2)||F||_2^2 sum_(m>=1)exp(-2a_m delta)<infinity,           (2.3)
```

and the same conclusion for `B`. Thus differentiation under the sum is valid and

```
boxed: D_(T,delta)^Gamma(F)
       =-(1/2) partial_delta B_(T,delta)^Gamma(F)>=0.             (2.4)
```

Every coefficient is strictly positive. By the moment-completeness theorem,

```
D_(T,delta)^Gamma(F)=0  if and only if  F=0.                     (2.5)
```

## 3. Exact Hankel kernel

Using

```
K_F(a_m)=integral_(-T)^T F(t)exp(-a_m t)dt,                      (3.1)
```

and Tonelli for the positive majorant supplied by (2.3), equations (1.2)--(1.3) give:

**Theorem 3.1 (Gamma-pole/Hankel identity; PROVED).**

```
B_(T,delta)^Gamma(F)
 =integral integral F(t)conj(F(u))
    k_Gamma^+(2T+2delta+t+u) dt du,                              (3.2)

D_(T,delta)^Gamma(F)
 =integral integral F(t)conj(F(u))
    [-(k_Gamma^+)'(2T+2delta+t+u)] dt du.                        (3.3)
```

Both integrals are over `(-T,T)^2`.

In left-endpoint coordinates `x=t+T`, `y=u+T`, the kernels are simply

```
k_Gamma^+(x+y+2delta),
-(k_Gamma^+)'(x+y+2delta),       0<x,y<2T.                       (3.4)
```

Thus they are genuine Hankel kernels: they depend on `x+y`, not `x-y`. Reflection is load-bearing.

*Proof.* Expand the absolute square in (2.1):

```
exp(-2a_m(T+delta))|K_F(a_m)|^2
 =integral integral F(t)conj(F(u))
    exp[-a_m(2T+2delta+t+u)]dtdu.
```

Sum and use (1.2) to obtain (3.2). Multiplication by `a_m` and (1.3) give (3.3). ∎

## 4. Relation with the residue energy of `R161_025`

Take

```
delta_0=(log 2)/4.                                                (4.1)
```

Then

```
exp(-2a_m delta_0)=2^(-m-1/4),                                  (4.2)
```

so the earlier normalized energy is exactly

```
D_T^pole(F)=2^(1/4) D_(T,delta_0)^Gamma(F).                      (4.3)
```

The arbitrary-looking factor `2^(-m)` was therefore a fixed positive displacement of the Gamma-Hankel boundary.
More canonically, one may retain the entire family `delta>0`.

## 5. Operator factorization

Define the bounded observation

```
(R_(T,delta)^Gamma F)_m
 :=sqrt(a_m)exp(-a_m(T+delta))K_F(a_m),       m>=1.              (5.1)
```

from `L2(-T,T)` to `ell2(N_(>=1))`. Then

```
D_(T,delta)^Gamma(F)=||R_(T,delta)^Gamma F||_(ell2)^2,           (5.2)
```

and the integral operator in (3.3) is `(R_(T,delta)^Gamma)*R_(T,delta)^Gamma`. This factorization is constructed
from the Gamma pole lattice and does not use a square root of the Weil form.

It is faithful by (2.5).

## 6. The revised equality-state target

The direct causal inequality is automatic from (2.4): the Gamma-Hankel energy `B_(T,delta)^Gamma` decreases as the
boundary is displaced outward. Closure requires the reverse statement on a first-contact state. It is enough to
prove, for one `delta>0`,

```
partial_delta B_(T,delta)^Gamma(F)>=0.                           (6.1)
```

Indeed (2.4) gives the opposite inequality for every source, hence equality, then
`D_(T,delta)^Gamma(F)=0`, and finally `F=0`.

The sharpened finite target is:

> **L161.9 (reverse Gamma-Hankel displacement; OPEN).** Derive (6.1), for a primitive first-contact state, from the
> finite mixed `(PC-ren)` identity with the reflection `J` and the continuum counterterm retained before taking the
> quadratic form.

This is more structured than L161.8: the desired residue square is now the derivative of an explicit source-defined
Hankel norm, and the additive Fourier reflection in `(PC)` is exactly what changes a difference kernel into the
sum kernel (3.4).

The theorem must still supply the reverse sign. Formula (2.4) alone gives only the already known causal direction;
asserting (6.1) from minimality or ordinary first variation would collide with the phase-121 shape-derivative
audit.

## 7. Status

- Gamma pole lattice as a positive Hankel kernel: **PROVED**;
- equality with the normalized residue energy: **PROVED**;
- bounded faithful observation factorization: **PROVED**;
- direct displacement monotonicity: **PROVED**;
- reverse displacement inequality from finite `(PC-ren)` and first contact: **OPEN L161.9**;
- row D: **OPEN**.
