# E101.073 - Exact binomial collapse of the quartet exterior kernel

## 1. Result

The rational exterior current of E101.071 has a stronger exact structure
than the absolute growth gate of E101.072 reveals.  For a general finite
shift family it splits into

```text
a separable rank-four Cauchy collar;
a shifted Hilbert correction.                       (1.1)
```

For the binomial coefficients of E101.067, the entire signed shift sum in
the correction can be evaluated:

```text
sum_(m=1)^K (-1)^(m+1)binom(K,m)m/(u+m)
=1/binom(u+K,K).                                    (1.2)
```

Consequently the exponential coefficient norm `2^K-1` disappears after the
complete signed recombination.  The correction is bounded by `1/(K+1)`
times the pole-adapted Cauchy product.  The current converges, at fixed finite
data and also under the displayed absolute summability condition, to one
separable scalar:

```text
Sep_N(x,phi)
=sum_(p in P_zeta)K_p Phi_(p,N)(phi)X_(p,N)(x).     (1.3)
```

This closes the shift-order algebra.  It does not close the discriminant:
the two factors in (1.3) are exactly the dual Cauchy coordinate of E101.051
and the exterior source collar of E101.050.  Their actual nonvanishing is the
previously named `RDC-4` burden.

## 2. Signed Cauchy coordinates

For a pole `p`, define

```text
Phi_(p,N)(phi)
=sum_(n in I_N)phi_n R_p(n),

X_(p,N)^sigma(x)
=sum_(j in T_N^sigma)x_j R_p(j),

X_(p,N)(x)=X_(p,N)^+(x)+X_(p,N)^-(x),              (2.1)

R_p(n)=1/(d_n-p).                                   (2.2)
```

These are signed quantities.  No absolute value is taken.

For `m>=1`, put

```text
H_(p,m)^sigma(x,phi)
=sum_(n in I_N)sum_(j in T_N^sigma)
 phi_n x_j R_p(n)R_p(j)
 /[d_n-d_j-sigma m h].                              (2.3)
```

The pole component of E101.071(5.5) obeys

```text
delta L_(m,p)^sigma(n,j)
=K_p R_p(n)R_p(j)
 {1+sigma m h/[d_n-d_j-sigma m h]}.                (2.4)
```

### Theorem 2.1 - General finite-shift split

Let

```text
eta_sum=sum_m eta_m.                                (2.5)
```

Then

```text
RQEC_(N,eta)(x,phi)
=eta_sum sum_(p in P_zeta)K_p
  Phi_(p,N)(phi)X_(p,N)(x)

 +h sum_(p in P_zeta)K_p sum_m m eta_m
   [H_(p,m)^+(x,phi)-H_(p,m)^-(x,phi)].             (2.6)
```

### Proof

Insert (2.4) in the two-face definition of `RQEC`.  The first term
factorizes into (2.1) and is independent of `m`, giving the first line of
(2.6).  In the second term the factor `sigma` produces the difference of the
two face kernels. `QED`

Equation (2.6) already identifies the only part which survives when the
shifted denominator correction is removed.

## 3. Right-bordered Hilbert form

On the positive face, write

```text
n=N-r,
j=N+q,
r>=0,
q>=2.                                               (3.1)
```

On the negative face, write

```text
n=r-N,
j=-N-q,
r>=0,
q>=1.                                               (3.2)
```

Then

```text
d_n-d_j-mh=-h(r+q+m)                               (3.3)
```

on the positive face, while

```text
d_n-d_j+mh=h(r+q+m)                                (3.4)
```

on the negative face.  Therefore the correction in (2.6) is

```text
-sum_(p in P_zeta)K_p sum_m m eta_m {

 sum_(r>=0,q>=2)
  phi_(N-r)x_(N+q)R_p(N-r)R_p(N+q)/(r+q+m)

 +sum_(r>=0,q>=1)
  phi_(r-N)x_(-N-q)R_p(r-N)R_p(-N-q)/(r+q+m)}.
                                                            (3.5)
```

Both faces have the same sign after their orientation is included.  The
asymmetry survives only in the lower limit `q>=2` versus `q>=1`.

Formula (3.5) is the quartet-pole specialization of the Hilbert--Hankel
kernel already present in E101.060--E101.067.

## 4. Exact binomial identity

Set

```text
gamma_(K,m)=(-1)^(m+1)binom(K,m),
1<=m<=K.                                            (4.1)
```

### Lemma 4.1 - Binomial beta collapse

For every `u>0`,

```text
sum_(m=1)^K gamma_(K,m)m/(u+m)
=K! Gamma(u+1)/Gamma(u+K+1).                        (4.2)
```

For integer `u>=1`, this is

```text
sum_(m=1)^K gamma_(K,m)m/(u+m)
=1/binom(u+K,K).                                    (4.3)
```

### Proof

The binomial polynomial is

```text
G_K(t)=sum_(m=1)^K gamma_(K,m)t^m
      =1-(1-t)^K.                                   (4.4)
```

Since `m/(u+m)=1-u/(u+m)` and `G_K(1)=1`,

```text
sum_m gamma_(K,m)m/(u+m)
=1-u integral_0^1 t^(u-1)G_K(t)dt

=u integral_0^1 t^(u-1)(1-t)^Kdt
=u B(u,K+1).                                       (4.5)
```

The beta-gamma identity gives (4.2), and the integer specialization gives
(4.3). `QED`

This identity includes the singular-mode sum of E101.067 as a special
partial-fraction consequence, but here it acts on every Hilbert index
`u=r+q` simultaneously.

## 5. Exact binomial current

Since

```text
sum_(m=1)^K gamma_(K,m)=1,                          (5.1)
```

Theorem 2.1, formula (3.5) and Lemma 4.1 give the following result.

### Theorem 5.1 - Separable collar plus beta kernel

For every finite source and row test,

```text
RQEC_(N,K)(x,phi)
=Sep_N(x,phi)-Corr_(N,K)(x,phi),                   (5.2)
```

where

```text
Sep_N(x,phi)
=sum_(p in P_zeta)K_p
  Phi_(p,N)(phi)X_(p,N)(x),                         (5.3)
```

and

```text
Corr_(N,K)
=sum_(p in P_zeta)K_p {

 sum_(r>=0,q>=2)
  phi_(N-r)x_(N+q)R_p(N-r)R_p(N+q)
  /binom(r+q+K,K)

 +sum_(r>=0,q>=1)
  phi_(r-N)x_(-N-q)R_p(r-N)R_p(-N-q)
  /binom(r+q+K,K)}.                                 (5.4)
```

The theorem is exact.  No limiting exchange and no estimate of individual
binomial coefficients occurs.

## 6. Uniform correction bound

For every integer `u>=1`,

```text
0<1/binom(u+K,K)<=1/(K+1).                          (6.1)
```

Define the absolute pole sizes of E101.072:

```text
Phi_abs_(p,N)(phi)
=sum_(n in I_N)|phi_n|/|d_n-p|,

X_abs_(p,N)(x)
=sum_(j in T_N^+ union T_N^-)|x_j|/|d_j-p|.        (6.2)
```

### Corollary 6.1

Whenever the right side is finite,

```text
|Corr_(N,K)(x,phi)|
<=1/(K+1) sum_(p in P_zeta)|K_p|
  Phi_abs_(p,N)(phi)X_abs_(p,N)(x).                 (6.3)
```

Hence, for fixed `N,x,phi`,

```text
RQEC_(N,K)(x,phi)->Sep_N(x,phi).                    (6.4)
```

The same convergence is uniform in any family for which the product on the
right side of (6.3) is uniformly bounded.

### Proof

Apply (6.1) termwise only after the signed binomial sum has been evaluated by
Lemma 4.1.  The remaining double sums factor into (6.2). `QED`

The order of operations matters.  Bounding the binomial coefficients before
Lemma 4.1 gives `2^K-1`; summing them first gives `1/(K+1)`.

## 7. Identification with existing coordinates

The test factor in (5.3) is

```text
Phi_(p,N)(phi)
=phi(D_N-pI)^(-1)1.                                (7.1)
```

For the terminal dual row, this is exactly the function `V_z(p)` of
E101.051, analytically continued from an external real column to the quartet
pole.

The source factor is the exterior part of the periodic Cauchy transform:

```text
X_(p,N)(x)
=sum_(j in T_N)x_j/(d_j-p)
=-sum_(j in T_N)x_j/(p-d_j).                       (7.2)
```

E101.050 gives the complete bilateral transform before the interior terms
are removed.  Thus `Sep_N` is a four-pole coupling of

```text
the old dual external-column coordinate;
the old source Cauchy collar.                        (7.3)
```

The correction (5.4) is the shifted Hilbert kernel studied by
E101.057--E101.061.  Therefore every component of (5.2) has a prior
coordinate in the program.

## 8. Circle audit against the controlled spectral defect

E101.056 and E101.059 identify the completed controlled-build defect as

```text
sum_(rho in Q)Xi(rho)Phi_phi(rho),                  (8.1)
```

and leave nonvanishing on the actual limiting test as `RDC-4`.  The four
Cauchy factors in (5.3) are the finite right-bordered representation of the
same quartet evaluation after the source is separated into interior and
exterior pieces.

Consequently,

```text
proving Sep_N has the required nonzero limit by assuming nonvanishing of
the completed quartet functional is circular;

proving only that one factor in (5.3) is not identically zero on the full
test space does not control the selected terminal row;

using the exact beta collapse to rename RDC-4 does not create new
mathematics.                                         (8.2)
```

The exact gain of this document is narrower but real: shift order and the
Hilbert correction are no longer primitive obstructions.  The remaining
burden is the separable quartet collar (5.3).

## 9. Decision on the shifted-moment route

The following work is now closed or frozen:

```text
searching for better finite shift coefficients;
estimating the binomial coefficient norm before signed summation;
treating the shifted Hilbert correction as the force-bearing term;
separating quartet and boundary before the reduction of E101.071;
claiming novelty for the product of E101.050 and E101.051.             (9.1)
```

The only unresolved scalar in this route is

```text
SEPARABLE-QUARTET-COLLAR:

sum_(p in P_zeta)K_p
 Phi_(p,N)(phi_N)X_(p,N)(kappa_Z),                 (9.2)
```

with the actual normalized terminal row.  By Section 8, its nonvanishing is
`RDC-4` unless an independent equation for the four values `Phi_(p,N)` is
derived from the horizontal dual system.

Thus the next admissible front is not another Abel or moment transform.  It
is the horizontal moving-level response of the rank-four perturbation,
where the characteristic tangent projection may impose an additional
finite relation unavailable to the fixed-level Cauchy collar.

## 10. Status

```text
proved:
  exact general split into separable collar and shifted Hilbert correction;
  exact binomial identity (4.2)--(4.3);
  exact beta-kernel formula for the complete two-face correction;
  uniform 1/(K+1) correction bound after signed summation;
  reduction of growing binomial order to the separable quartet collar;

identified as prior burden:
  the separable collar is the coupling of E101.050 and E101.051 and carries
  the same selected-test nonvanishing problem as RDC-4;

frozen:
  further finite-shift design and separate Hilbert-correction estimates;

open:
  an independent horizontal equation for the four pole coordinates,
  DIRECTIONAL-IDENT and Omega7.
```
