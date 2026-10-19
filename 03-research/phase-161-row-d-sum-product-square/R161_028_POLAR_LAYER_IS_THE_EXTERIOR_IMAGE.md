# R161_028 — The Euler--Maclaurin polar layer is exactly the exterior image

## 0. Verdict

The reflected exterior copy introduced in `R161_027` is not an auxiliary construction. On a parity source it is
exactly the logarithmic derivative of the Euler--Maclaurin continuum counterterm in `(PC-ren)`, at the natural
cutoff

```
log N=2(T+delta).                                                 (0.1)
```

Moreover, the support of the polar layer is exactly the support interval of that exterior image. Thus the
Gamma-Hankel force and the finite Poisson defect live on the same moving polar boundary. This is the first literal
operator bridge between the Gamma-pole square and the finite sum--product construction.

## 1. Logarithmic polar family

Write `N=exp(a)` and denote the continuum counterterm of `R161_003` by `C_a`. Its multiplier is

```
C_a(s)=exp(a(1-s))/(1-s).                                       (1.1)
```

In physical logarithmic coordinates,

```
(C_aF)(t)
 =exp(-t/2) integral_(-infinity)^(t+a) exp(y/2)F(y)dy.            (1.2)
```

Let

```
(VF)(t)=exp(-t/2)integral_(-infinity)^t exp(y/2)F(y)dy.           (1.3)
```

Then

```
C_a=exp(a/2)tau_a V.                                             (1.4)
```

Since `(partial_t+1/2)V=I`, differentiation gives the exact strong-core identity

```
partial_a C_a=exp(a/2)tau_a.                                    (1.5)
```

This is the logarithmic form of `dC_x/dx=x^(-1/2)tau_(log x)` from `R161_003`.

## 2. Support of the primitive polar layer

Assume `supp F subset [-T,T]` and the positive Tate moment vanishes:

```
integral_(-T)^T exp(y/2)F(y)dy=0.                               (2.1)
```

Below `t=-T-a`, the integral in (1.2) is empty. Above `t=T-a`, it is the full moment (2.1). Hence

```
supp C_aF subset [-T-a,T-a].                                    (2.2)
```

For

```
a=2(T+delta),       delta>0,                                    (2.3)
```

this becomes

```
supp C_aF subset [-3T-2delta,-T-2delta],                         (2.4)
```

which is exactly the image interval in `R161_027`.

## 3. The image is the polar velocity

Let `J` be reflection and define the image operator

```
M_(T,delta)=tau_a J,       a=2(T+delta).                         (3.1)
```

Indeed,

```
(tau_a JF)(t)=F(-t-a)=F(-t-2(T+delta)),                          (3.2)
```

the image used in `R161_027`.

If `JF=epsilon F`, then (1.5) gives:

**Theorem 3.1 (polar-layer/image identity; PROVED).**

```
partial_a(C_aF)=epsilon exp(a/2)M_(T,delta)F.                    (3.3)
```

Equivalently, since `partial_delta a=2`,

```
M_(T,delta)F
 =(epsilon/2)exp(-a/2)partial_delta(C_aF).                       (3.4)
```

Thus moving the Euler--Maclaurin cutoff generates the separated reflected copy exactly; no limiting or asymptotic
argument is involved.

## 4. Gamma-Hankel energy as a polar-layer pairing

Let `K_Gamma^+=C_(k_Gamma^+)` be the one-sided Gamma-tail convolution from `R161_027`. Its image formula and (3.3)
give

```
B_(T,delta)^Gamma(F)
 =<F,K_Gamma^+ M_(T,delta)F>
 =epsilon exp(-a/2)
   <F,K_Gamma^+ partial_a(C_aF)>.                                (4.1)
```

Therefore the faithful pole energy is

```
D_(T,delta)^Gamma(F)
 =-(1/2)partial_delta
   {epsilon exp(-a/2)<F,K_Gamma^+ partial_a(C_aF)>}.              (4.2)
```

Formula (4.2) places the complete Gamma-pole detector inside the moving continuum piece of `(PC-ren)`.

## 5. The matching finite Poisson layer

Define the continuous-cutoff integer comb

```
S_a:=sum_(1<=n<=exp(a))n^(-1/2)tau_(log n),                      (5.1)
```

with either one-sided convention at integer endpoints, and its discrepancy

```
Z_a:=S_a-C_a.                                                     (5.2)
```

Between integer births, `S_a` is constant while `C_a` moves according to (1.5). At a birth `a=log n`, `S_a` has
the jump

```
Delta S_a=n^(-1/2)tau_(log n).                                  (5.3)
```

Thus the moving image has two exactly source-defined components:

```
continuous velocity: -exp(a/2)tau_a,
discrete jumps:       n^(-1/2)tau_(log n).                       (5.4)
```

The first is the polar image velocity; the second is the integer Poisson boundary. Their combination is precisely
the moving renormalized Muntz discrepancy, not a fitted deformation.

## 6. Revised same-sign target

The bridge (3.3)--(5.4) sharpens L161.10. The missing finite calculation is now:

> **L161.11 (moving-discrepancy square; OPEN).** Differentiate the finite quadratic `(PC-ren)` pairing with respect
> to `a` between births and add its exact jumps at `a=log n`. After the Chebyshev hyperbola terms are combined via
> `Lambda*1=log`, prove that on a first-contact state the result is
>
> ```
> 0=2D_(T,delta)^Gamma(F)+D_a^Poisson(F),
> D_a^Poisson(F)>=0,                                             (6.1)
> ```
>
> at `a=2(T+delta)` or after a positive average in `delta`.

Unlike the earlier image-force formulation, every term in L161.11 now belongs literally to the finite polar
renormalization: the exterior image is `partial_a C_a`, and the putative complementary square must come from the
jumps of `S_a-C_a`.

The sign is still not proved. The ordinary derivative of `||S_a-C_a||^2` contains an uncontrolled cross term;
`(PC-ren)` and the hyperbola terminal jumps must supply the additional orientation. Dropping those terms returns to
the nonmonotone defect measured by `161_02_poisson_defect_probe.py`.

## 7. Status

- logarithmic derivative of the polar counterterm: **PROVED**;
- exact support match with the reflected exterior image: **PROVED**;
- image as polar-layer velocity on a parity source: **PROVED**;
- Gamma-pole energy as a moving polar-layer pairing: **PROVED**;
- exact continuous velocities and integer jumps of `S_a-C_a`: **PROVED**;
- same-sign moving-discrepancy identity L161.11: **OPEN**;
- row D: **OPEN**.
