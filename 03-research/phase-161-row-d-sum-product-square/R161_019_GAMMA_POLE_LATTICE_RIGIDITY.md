# R161_019 — Gamma-pole lattice rigidity for the product-port range

## 0. Verdict

The arithmetic range-intersection problem of `R161_011` becomes rigid once the exact product scattering is known.
Indeed, the scattering defect of `R161_017` contains

```
d_Gamma(s)K_F(s-1/2),
d_Gamma(s)=-chi'(s)/chi(s).                                      (0.1)
```

The multiplier `d_Gamma` has simple poles at

```
s=3,5,7,... .                                                    (0.2)
```

Every other term in the canonically corrected defect is holomorphic there. Thus vanishing of the scattering defect
forces

```
K_F(5/2)=K_F(9/2)=K_F(13/2)=...=0.                               (0.3)
```

These exponential moments form a complete system on every finite interval. Consequently `F=0`.

This closes the **range-rigidity half** of the phase-161 terminal problem: exact physical cosine scattering already
excludes first contact and, in particular, gives the Sonin--Gamma upper bound with equality. The only remaining
load-bearing statement is the physical scattering boundary passage itself. It cannot be obtained from the linear
completed `(PC-ren)` limit by `R161_018`; it must come from the finite quadratic/reverse-scattering construction.

## 1. Pole set of the Gamma logarithmic derivative

With

```
chi(s)=pi^(s-1/2) Gamma((1-s)/2)/Gamma(s/2),                       (1.1)
```

logarithmic differentiation gives

```
d_Gamma(s)
 =-log pi + (1/2)psi((1-s)/2)+(1/2)psi(s/2).                     (1.2)
```

The digamma function has simple poles at `0,-1,-2,...`, each with nonzero residue. Therefore `d_Gamma` has simple
poles at

```
s=0,-2,-4,...,
s=1,3,5,... .                                                    (1.3)
```

At `s=2m+1`, `m>=1`, only the first digamma term in (1.2) is singular, so no cancellation is possible.

## 2. Holomorphy of the remaining defect terms

The corrected defect of `R161_017` is

```
W_epsilon^0(s)
 =d_Gamma(s)K_F(s-1/2)
  -Q_+(s-1/2)-Q_-(s-1/2)
  -Theta_+(s)-Theta_-(s).                                       (2.1)
```

The two `Q` terms are bilateral Laplace transforms of compactly supported prehistories and are entire in `z=s-1/2`.

For the canonical Hardy gauge of `R161_015`, the right correction has the form

```
Theta_+(s)=c_+ exp(-T(s-1))/s,                                   (2.2)
```

and the reflected correction has its only possible finite pole at `s=1`. Hence both are holomorphic at every
`s=2m+1`, `m>=1`. The earlier compactly supported gauges are entire and satisfy the same conclusion.

Thus, if `W_epsilon^0` vanishes meromorphically, the residue at each positive odd pole in (1.3) is a nonzero constant
times `K_F(2m+1/2)`. This proves:

**Lemma 2.1 (Gamma-pole cancellations; PROVED).** Exact scattering implies

```
K_F(2m+1/2)=0,       m=1,2,3,... .                              (2.3)
```

## 3. Completeness of the pole lattice

**Theorem 3.1 (exponential-moment rigidity; PROVED).** Let `T<infinity` and `F in L2(-T,T)`. If

```
integral_(-T)^T F(t) exp(-(2m+1/2)t)dt=0,
m=1,2,3,...,                                                     (3.1)
```

then `F=0` almost everywhere.

*Proof.* Put

```
x=exp(-2t),
a=exp(-2T),
b=exp(2T).                                                       (3.2)
```

Then `0<a<b<infinity`, `dt=-dx/(2x)`, and (3.1) becomes

```
integral_a^b f(x)x^m dx=0,       m=1,2,3,...,                    (3.3)
```

where

```
f(x)=(1/2)F(-(1/2)log x)x^(-3/4).                               (3.4)
```

On the compact interval `[a,b]`, multiplication by the bounded positive weights arising in (3.4) is an isomorphism
between the corresponding `L2` spaces, so `f` is locally square integrable and defines the displayed moments.

The span of `{x^m:m>=1}` is dense in `L2(a,b)`: since `a>0`, the continuous function `1/x` can be uniformly
approximated by polynomials, hence `1` can be uniformly approximated by polynomials with zero constant term; the
same argument applied to `p(x)/x` puts every polynomial in the closure of that span. Weierstrass density of
polynomials, followed by the density of continuous functions in `L2`, proves the claim.

Equation (3.3) therefore makes `f` orthogonal to a dense subspace, so `f=0`; the change of variables gives `F=0`.
∎

No restriction such as `T<pi/2` occurs. Compactness away from `x=0` is what makes the positive powers complete.

## 4. Exact range-intersection theorem

Combine Lemma 2.1 and Theorem 3.1.

**Theorem 4.1 (product-range/Sonin rigidity; PROVED CONDITIONAL ON PHYSICAL SCATTERING).** Let `F` be a finite-window
parity first-contact state and let `G_+^0,G_-^0` be its canonical corrected product ports. If the physical boundary
passage gives

```
G_+^0(s)+chi(s)G_-^0(s)=0                                       (4.1)
```

as a common meromorphic germ, then `F=0`.

*Proof.* By `R161_017`, (4.1) is `zeta(s)W_epsilon^0(s)=0`. In the zero-free half-plane `Re s>1`, division by zeta
gives `W_epsilon^0=0`; meromorphic continuation gives the same identity globally. Lemma 2.1 and Theorem 3.1 then
give `F=0`. ∎

This theorem proves the intersection statement anticipated in `R161_011`: a generic Sonin space is nonzero, but a
Sonin port in this explicit product range cannot come from a nonzero compact-window source.

## 5. Consequence for the Sonin--Gamma upper bound

Under (4.1), Theorem 4.1 gives `F=0`, hence the canonical product port `g=0`. Therefore

```
E_T^PC(F)
 =<D_Gamma g,g>-2T||g||^2
 =0<=0.                                                           (5.1)
```

Thus exact physical scattering implies the missing upper bound of `R161_014`—in fact with equality—and excludes
first contact. There is no separate homogeneous zero mode after the product-range condition is retained.

This corrects the provisional conclusion in `R161_017` that scattering would leave homogeneous uniqueness open.
That conclusion ignored the positive odd Gamma-pole lattice in the explicit quotient (2.1).

## 6. Scope and remaining gate

The theorem does **not** derive (4.1). `R161_018` proves that the linear completed `(PC-ren)` graph gives only the
tautology `[Z,D_Gamma]=0`; it cannot set the separated port to zero. Hence using Theorem 4.1 requires an independently
proved quadratic reverse-scattering identity, or another physical boundary theorem that yields (4.1) without
discarding the incoming prehistory.

The terminal chain is now:

```
finite quadratic (PC) defect
 -> physical cosine scattering (4.1)          [OPEN]
 -> W_epsilon^0=0                             [PROVED]
 -> Gamma-pole moment lattice                 [PROVED]
 -> F=0                                       [PROVED]
 -> E_T^PC(F)=0<=0 and no first contact       [PROVED].
```

## 7. Status

- positive odd Gamma pole lattice: **PROVED**;
- holomorphy audit of all non-Gamma defect terms there: **PROVED**;
- completeness of the induced exponential moments for every finite `T`: **PROVED**;
- product-range/Sonin intersection: **PROVED conditional only on physical scattering**;
- Sonin--Gamma upper balance after physical scattering: **PROVED with equality**;
- derivation of physical scattering from the finite quadratic `(PC)` defect: **OPEN**;
- row D: **OPEN**.
