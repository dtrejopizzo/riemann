# E80.004 - Coherence and summability do not identify the limit

## 1. Purpose

The finite spectral-shift program observed three properties:

```text
1. all finite spectral atoms are real;
2. consecutive Poisson-transform differences are summable;
3. the cumulative spectral shift is sign coherent, making the Stieltjes bound
   equal to the signed transform difference.
```

This note determines what those properties can prove without an arithmetic
normalization.

## 2. A coherent real-spectral family

Let

```text
0<a_k<b_k,
epsilon_k>0,
```

and define the signed real measure

```text
mu_k
 = epsilon_k(-delta_{-b_k}+delta_{-a_k}
             +delta_{a_k}-delta_{b_k}).                (2.1)
```

Its cumulative function

```text
M_k(x)=mu_k((−infinity,x])                              (2.2)
```

satisfies

```text
M_k(x)x >= 0                                            (2.3)
```

for every real `x`: it equals `-epsilon_k` on `(-b_k,-a_k)`,
`epsilon_k` on `(a_k,b_k)`, and zero elsewhere.

For the Poisson kernel

```text
P_sigma(x)=2sigma/(x^2+sigma^2),                        (2.4)
```

one has

```text
integral P_sigma dmu_k
 = 2epsilon_k(P_sigma(a_k)-P_sigma(b_k)) > 0.           (2.5)
```

Integration by parts also gives

```text
integral P_sigma dmu_k
 = integral M_k(x) 4sigma x/(x^2+sigma^2)^2 dx,         (2.6)
```

and the integrand is nonnegative by (2.3).  Hence the absolute Stieltjes
bound is exactly tight.

## 3. Summability with arbitrary limit data

### Theorem 3.1

Assume

```text
sum_k epsilon_k(P_sigma0(a_k)-P_sigma0(b_k)) < infinity (3.1)
```

for one `sigma0>0`, with `a_k` bounded away from zero.  Then

```text
S_N(sigma)=sum_{k<=N} integral P_sigma dmu_k             (3.2)
```

converges locally uniformly for `sigma>0`.  Every increment is positive,
the cumulative shift is sign coherent, and the Stieltjes bound is tight.

Nevertheless the limiting function is not determined by these properties.

### Proof

On a compact interval `sigma in [alpha,beta]` with `alpha>0`, comparison of
the rational kernels gives a constant `C` such that

```text
0 <= P_sigma(a)-P_sigma(b)
 <= C(P_sigma0(a)-P_sigma0(b))                         (3.3)
```

for all `0<a<b` with `a` bounded away from zero.  The Weierstrass test and
(3.1) give local uniform convergence of (3.2).  Positivity of increments,
coherence and tightness were proved in (2.3)--(2.6).

Now replace `epsilon_1` by any other positive value.  Every qualitative
property remains true, but the limit changes by the nonzero function

```text
2 Delta epsilon_1(P_sigma(a_1)-P_sigma(b_1)).           (3.4)
```

Therefore the stated properties do not determine the limit. `QED`

## 4. Real-spectral interpretation

Each increment (2.1) is obtained by moving a symmetric pair of real atoms from
`+-b_k` to `+-a_k`.  Thus the theorem is already a difference-of-real-clouds
model.  It contains no complex spectral point and satisfies the same
single-signed cumulative geometry that makes the finite zeta bound tight.

The conclusion is exact:

```text
real spectra + GAP-type summability + single-signed cumulative shifts
do not identify an Euler--Gamma limit.                                 (4.1)
```

An additional arithmetic invariant is logically necessary.

## 5. Consequence for the discriminant

The proposed implication

```text
spectral coherence <=> SAFE-GAMMA-IDENT                               (5.1)
```

is false as a statement based only on coherence and convergence.  Coherence
may prove bounded variation or tightness, but the target value must enter
through RDI, an exact cell identity, or an equivalent arithmetic
normalization.

This does not refute coherence as a consequence of RDI or as an estimate used
inside a proof.  It refutes its use as the complete identification principle.

## 6. Status

```text
proved:
  an explicit family of real spectral clouds with sign-coherent cumulative
  shifts, tight Stieltjes bounds and locally uniform summable convergence;
  the limiting Poisson transform remains freely variable;

refuted:
  coherence plus GAP-type convergence as a sufficient arithmetic
  identification mechanism;

corrected:
  the load-bearing discriminant is RDI or an equivalent arithmetic identity;
  coherence is only an auxiliary geometric property;

next:
  express the RDI derivative defect in the closed Hilbert product-rule
  coordinates and isolate the exact arithmetic cocycle required to cancel it.
```

