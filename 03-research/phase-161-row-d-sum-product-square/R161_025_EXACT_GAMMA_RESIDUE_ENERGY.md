# R161_025 — Exact Gamma-residue energy and the failure of the linear safe-half-plane shortcut

## 0. Verdict

At every positive odd Gamma pole the corrected scattering defect has an explicit residue with no unknown constant:

```
Res_(s=2m+1)[zeta(s)W_epsilon^0(s)]
 =zeta(2m+1)K_F(2m+1/2).                                       (0.1)
```

Therefore removability is exactly vanishing of a source moment, not a consequence of finite-approximant
holomorphy. A locally uniform passage across the pole would already contain the missing theorem.

The residues define a canonical faithful positive energy after harmless support normalization. There is no
non-Gamma residue with which they can cancel. This is the
smallest quadratic equality-state target presently available. Any successful use of the sum--product square may
prove that energy zero; a linear `(PC-ren)` graph limit cannot, by `R161_018`.

## 1. Exact residue constants

Put

```
s_m=2m+1,       a_m=s_m-1/2=2m+1/2,       m>=1.                 (1.1)
```

Near `s=s_m`, write `u=(1-s)/2`. Since `u=-m-(s-s_m)/2` and the residue of `psi` at `-m` is `-1`,

```
psi((1-s)/2)=2/(s-s_m)+O(1).                                   (1.2)
```

Consequently

```
Res_(s=s_m)d_Gamma(s)=1.                                       (1.3)
```

All other terms of `W_epsilon^0` are holomorphic at `s_m`, so

```
Res_(s=s_m)W_epsilon^0(s)=K_F(a_m),                              (1.4)
```

and, because `zeta(s_m)` is finite and nonzero, (0.1) follows.

The same constant can be checked from the reflected product port. The functional equation

```
zeta(s)=chi(s)zeta(1-s)                                         (1.5)
```

and the simple trivial zero at `1-s_m=-2m` give

```
Res_(s=s_m)chi(s)=-zeta(s_m)/zeta'(-2m).                         (1.6)
```

Moreover the correction and `Q_-` terms are multiplied by `zeta(-2m)=0`, hence

```
G_-^0(s_m)=-zeta'(-2m)K_F(a_m).                                 (1.7)
```

Multiplying (1.6) and (1.7) again gives (0.1), including its sign.

## 2. Why finite holomorphy is not enough

The finite Dirichlet polynomials and hyperbola remainders in `(PC)` are entire, but the Fourier scattering factor
`chi` has the fixed poles (1.6). A sequence of holomorphic or meromorphic finite germs can converge away from
`s_m` to a germ with residue (0.1). To conclude removability from the approximants one must prove local uniform
boundedness on a full circle around `s_m`; by Cauchy's formula that assertion already forces the right side of
(0.1) to vanish.

Thus “pass the finite identity to the safe half-plane” is not a proof unless its topology controls the polar
coefficient. That coefficient is precisely the target moment.

There is also a structural obstruction. `R161_018` proves that every linear completed `(PC-ren)` graph limit gives
only

```
Z A_infinity F=[Z,D_Gamma]F=0,                                  (2.1)
```

whose two oriented polar residues cancel in the completed current. Extracting (1.4) from one orientation requires
retaining a finite quadratic or mixed oriented defect before that recombination.

Accordingly L161.7 must be amended: linear residue cancellation is not a surviving route.

## 3. A faithful positive pole energy

For `F in L2(-T,T)`, Cauchy--Schwarz gives

```
|K_F(a)|^2
 <=||F||_2^2 integral_(-T)^T exp(-2at)dt
 =||F||_2^2 sinh(2aT)/a.                                       (3.1)
```

Define

```
D_T^pole(F)
 :=sum_(m>=1) 2^(-m) a_m exp(-2a_m T)
     |Res_(s=s_m)[zeta(s)W_epsilon^0(s)]/zeta(s_m)|^2.           (3.2)
```

By (0.1), this is

```
D_T^pole(F)
 =sum_(m>=1)2^(-m)a_m exp(-2a_mT)|K_F(a_m)|^2.                  (3.3)
```

Equation (3.1) shows

```
D_T^pole(F)<=||F||_2^2 sum_(m>=1)2^(-m)/2<infinity.              (3.4)
```

Every weight in (3.3) is strictly positive. Hence

**Theorem 3.1 (faithful residue energy; PROVED).**

```
D_T^pole(F)>=0,
D_T^pole(F)=0  if and only if  F=0.                              (3.5)
```

*Proof.* Finiteness and nonnegativity follow from (3.3)--(3.4). If the energy is zero, every `K_F(a_m)` vanishes;
the moment-completeness theorem of `R161_019` gives `F=0`. The converse is immediate. ∎

The particular summable weights are inessential. Their role is only to convert the complete residue family into a
single finite positive number without changing its zero set.

## 4. Revised quadratic target

The minimal admissible successor to L161.7 is:

> **L161.8 (Gamma-residue square; OPEN).** Construct from the finite two-orientation `(PC-ren)` mixed pairing a
> nonnegative finite quantity `D_(M,N,T)^pole(F)` such that
>
> ```
> lim D_(M,N,T)^pole(F)=D_T^pole(F),                              (4.1)
> ```
>
> while the first-contact equality law forces the finite quantity, or its limit superior, to be zero.

This target is not defeated by the generic sign-blindness of `||S_NA_MF||^2`: only its value on a hypothetical
first-contact radical matters. Nevertheless, the vanishing must come from a source identity; defining the finite
energy by sampling the limiting residues would be circular.

Binding requirements:

1. residues must be extracted before the two causal orientations are added;
2. the continuum polar counterterm must be retained at every finite level;
3. convergence must control the first Laurent coefficient on circles around `s_m`;
4. the finite equality-state vanishing must be proved from `(PC-ren)`, not assumed from physical scattering;
5. summation in `m` may occur only after a uniform bound such as (3.4).

## 5. Status

- exact Gamma residue and sign: **PROVED**;
- exact reflected-port residue check: **PROVED**;
- linear safe-half-plane passage: **REJECTED AS INSUFFICIENT / covered by `R161_018`**;
- finite faithful pole energy: **PROVED**;
- finite `(PC-ren)` realization and first-contact annihilation of that energy: **OPEN L161.8**;
- row D: **OPEN**.
