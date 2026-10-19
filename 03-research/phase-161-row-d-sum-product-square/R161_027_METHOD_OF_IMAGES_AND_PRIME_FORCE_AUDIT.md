# R161_027 — Method of images for the Gamma-pole square and audit of the prime force

## 0. Verdict

The Gamma-Hankel energy of `R161_026` is exactly the interaction of the source with a translated reflected copy
placed beyond the left endpoint. Its pole energy is the attractive force obtained by changing the separating gap.

This supplies a geometric meaning for the reflection `J` in the sum--product identity. The corresponding prime
interaction can also be written exactly, but its gap derivative is an autocorrelation derivative with no fixed
sign. Therefore the method of images alone does not close D. A successful `(PC)` argument must use Poisson and
`Lambda*1=log` to convert the combined discrete force, not each raw prime contact, into the same-sign square.

## 1. Reflected exterior image

Put `L=T+delta`, `delta>0`, and define

```
(M_(T,delta)F)(x):=F(-x-2L).                                    (1.1)
```

If `F` is supported in `(-T,T)`, then its image is supported in

```
(-3T-2delta,-T-2delta).                                         (1.2)
```

Thus the original interval and its image are disjoint and separated by the gap `2delta`.

Let `C_k` be the one-sided convolution operator

```
(C_k h)(t)=integral_R k(t-x)h(x)dx,                              (1.3)
```

where `k(v)=0` for `v<=0`. For the image (1.1), every difference `t-x` in the cross interaction is positive.

## 2. Exact image formula

Take `k=k_Gamma^+` from `R161_026`. A change of variables `x=-u-2L` gives

```
<F,C_k M_(T,delta)F>
 =integral integral conj(F(t))F(u)
    k(2T+2delta+t+u)dtdu.                                      (2.1)
```

After interchanging the dummy variables and conjugating the real scalar, Theorem 3.1 of `R161_026` yields:

**Theorem 2.1 (Gamma method of images; PROVED).**

```
B_(T,delta)^Gamma(F)
 =<F,C_(k_Gamma^+)M_(T,delta)F>,                                (2.2)

D_(T,delta)^Gamma(F)
 =-(1/2)partial_delta
    <F,C_(k_Gamma^+)M_(T,delta)F>.                              (2.3)
```

Although (2.2) is written as an interaction of two disjoint copies, it is nonnegative because `k_Gamma^+` is the
Laplace sum of positive rank-one kernels. Equation (2.3) is strictly positive for every nonzero source.

## 3. A single prime contact

Let `a=log n` and let the one-sided atomic convolution be translation through distance `a`. Its image interaction is

```
I_(a,T,delta)(F)
 :=<F,tau_a M_(T,delta)F>.                                      (3.1)
```

With the convention `(tau_a h)(t)=h(t+a)`, direct substitution gives

```
I_(a,T,delta)(F)
 =integral_(-T)^T conj(F(t))
   F(-t-a-2T-2delta)dt,                                         (3.2)
```

where the second factor is understood as zero outside `(-T,T)`. Thus a contact is active only when the translated
reflection of the interval overlaps the original interval. Equivalently, `a` lies in the appropriate distance
range between the two copies.

For smooth `F` away from an activation seam,

```
partial_delta I_(a,T,delta)(F)
 =-2 integral conj(F(t))F'(-t-a-2T-2delta)dt.                    (3.3)
```

There is no fixed sign: changing the phase or sign oscillation of `F` reverses (3.3). At activation values, the
zero extension contributes the corresponding seam distribution; it also has no source-independent sign.

The reflected atomic orientation gives the conjugate contact. Their symmetric sum is real but remains indefinite.

## 4. Prime-power force

The raw arithmetic image interaction is

```
B_(T,delta)^prime(F)
 :=sum_(n>=2) Lambda(n)/sqrt(n)
   [I_(log n,T,delta)(F)+conj(I_(log n,T,delta)(F))].             (4.1)
```

Only finitely many contacts are active for fixed compact copies and a fixed gap. Positivity of `Lambda(n)` does not
give a sign to either (4.1) or its gap derivative, because the autocorrelations (3.2)--(3.3) are signed.

This is the image-coordinate version of the warning already present in `R161_001`: a positive coefficient sum of
translations is not a positive operator.

## 5. Where `(PC)` can still add information

The Gamma force is the faithful square

```
-partial_delta B_(T,delta)^Gamma=2D_(T,delta)^Gamma>0            (5.1)
```

for `F!=0`, whereas the raw prime force is indefinite. A conservation identity saying merely

```
partial_delta(B^Gamma-B^prime)=0                                (5.2)
```

would not kill the Gamma term; the prime term could balance it.

The only possible gain from the phase-161 construction is therefore stronger: multiplication by the finite Muntz
factor and the hyperbola identity `Lambda*1=log` must transform the **combined** prime image force into a Poisson
boundary square with the same orientation as (5.1). Only then could a zero total first-contact force imply that both
nonnegative pieces vanish.

This gives a concrete acceptance test for the next calculation:

> **L161.10 (image-force Poisson completion; OPEN).** Apply the finite `(PC-ren)` identity to the pair consisting
> of `F` and its separated image `M_(T,delta)F`, polarize before recombining orientations, and prove an identity
>
> ```
> 0=2D_(T,delta)^Gamma(F)+D_(M,N,T,delta)^Poisson(F)+o(1),       (5.3)
> ```
>
> on a first-contact state, with `D^Poisson>=0` constructed from the additive boundary defect.

The sign in (5.3) is binding. If the calculation instead gives
`2D^Gamma-D^Poisson=0`, it is only the ordinary indefinite Green conservation law and does not close D.

The image lies outside the first-contact window, so (5.3) cannot be inferred by treating the image as another
primitive test. It must come from the global finite `(PC-ren)` identity and its exterior boundary terms. This is
precisely why the construction is not covered by the tautological radical polarization of `R161_023`.

## 6. Collision audit

Abstract invariance of a Hankel or Volterra operator on the radical is not available. The phase-121
Tate--Volterra audit proves that such invariance contains the moving Tate jet and the exterior localization defect.
Likewise, first-contact minimality alone supplies no stationary shape derivative.

L161.10 survives those audits only if `(PC-ren)` proves the explicit same-sign completion (5.3). Without that
calculation, the method of images is a coordinate interpretation, not a proof.

## 7. Status

- Gamma pole square as image interaction force: **PROVED**;
- exact raw prime image contacts: **PROVED**;
- fixed sign of raw prime force: **FALSE**;
- abstract Hankel/Volterra radical invariance: **REJECTED by phase 121**;
- same-sign Poisson completion of the image force: **OPEN L161.10**;
- row D: **OPEN**.
