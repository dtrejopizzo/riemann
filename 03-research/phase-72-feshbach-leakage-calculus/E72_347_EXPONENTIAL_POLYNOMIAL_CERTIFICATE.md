# E72.347 -- Exponential-polynomial CFIR certificate

**Purpose.** Make `CERT-CFIR` non-tautological.  The row-ideal condition

```text
R_T(L) in Row(C_E-mu I)
```

is equivalent to `R_T(L)xi=0`, so by itself it only renames the desired cancellation.  This note
replaces it by a coefficient certificate: expand the determinant/adjugate identities as finite
exponential-polynomials in `L` and require the explicit coefficients to vanish.

## 1. Finite determinant object

Let

```text
E(L):=C_E(L)-mu(L)I.
```

For each Hermite row `r_alpha(L)` of `R_T(L)` and each replacement index `i`, define

```text
D_{alpha,i}(L)
:= det ReplaceRow(E(L); i, r_alpha(L)).              (1)
```

Exact `CERT-CFIR` is equivalent to

```text
D_{alpha,i}(L)=0
```

for all `(alpha,i)`, with the standard rank-one-kernel convention.

### Proof of the determinant equivalence

Fix one row `r`. Since the pole-even ground eigenspace is simple, `E(L)` has rank `N-1`. A row belongs
to `Row(E)` if and only if adjoining it does not increase the row rank. That is equivalent to the
vanishing of every `N x N` minor obtained by replacing one row of `E` by `r`. These minors are exactly
the determinants in (1). Applying this criterion to each Hermite row of `R_T` gives

```text
R_T(L) in Row(E(L)) <=> D_{alpha,i}(L)=0 for all alpha,i.
```

The polynomial-residual version is equivalent to

```text
|D_{alpha,i}(L)| <= C_T L^B |AdjScale_i(L)|,          (2)
```

where `AdjScale_i` is the corresponding nonzero cofactor scale of `E(L)`.  The exact case is cleaner
and is the one expanded below.

## 2. Exponential-polynomial form

All entries involved in (1) are built from:

```text
1. finite sums over active mesh indices;
2. finite sums over primes n<=e^L appearing through the already assembled matrix C_E;
3. elementary factors E_L(lambda)=(e^(lambda L)-1)/lambda;
4. fixed zero-window parameters a_j;
5. Fourier mesh phases e^(i d_m L)=1.
```

After the finite active mesh is fixed, every `D_{alpha,i}(L)` is a finite sum of the form

```text
D_{alpha,i}(L)
= sum_{beta in B_T} e^(beta L) P_{alpha,i,beta}(L)
  + PrimeFinite_{alpha,i}(L).                         (3)
```

Here:

```text
B_T subset span_Z{ a_j, -a_j, zeta-window sums }
```

is finite, each `P_{alpha,i,beta}` is a polynomial/rational function in `L` with coefficients depending
only on the active mesh and fixed zero-window data, and `PrimeFinite` is the finite prime-power part
already present in `C_E`.

The point is that no outside zero sum or infinite Fourier tail remains.

## 3. Prime-expanded finite coefficient form

To make (3) completely finite, expand the prime part of `C_E` before taking the determinant.  Since
the active matrix is finite, multilinearity of the determinant gives

```text
D_{alpha,i}(L)
= sum_{word omega in Omega_{alpha,i}(L)}
   c_{alpha,i}(omega;L)
   prod_{r in omega} Lambda(r)r^(-1/2).               (4)
```

where each word uses only prime powers `r<=e^L` and has length at most the matrix size.  The coefficient
`c_{alpha,i}` is an explicit finite expression in the archimedean/Fourier kernels and the fixed
zero-window data.

Thus exact `CERT-CFIR` is equivalent to the finite family of identities

```text
sum_{word omega in Omega_{alpha,i}(L)}
   c_{alpha,i}(omega;L)
   prod_{r in omega} Lambda(r)r^(-1/2)
=0                                                     (5)
```

for all Hermite rows and replacement indices.

This is the fully expanded finite certificate.

### Proof of the coefficient expansion

The determinant is multilinear in its rows. Each row of `E(L)` and each replacement row `r_alpha(L)`
is a finite sum of an archimedean/model row and finitely many prime-power rows, because the cutoff
`r<=e^L` is finite. Expanding the determinant by multilinearity chooses one summand from each row.
Each such choice contributes one finite word `omega` of prime powers, multiplied by an explicit
coefficient from the archimedean/Fourier kernels and the selected row positions. Summing over all
choices gives (4). No limiting process is used.

## 4. Coefficient annihilation certificate

A stronger, purely structural certificate is:

```text
COEFF-CFIR:
c_{alpha,i}(omega;L)=0
for every alpha,i,omega.                              (6)
```

Then `CERT-CFIR` holds without using cancellation between different prime words.

If (6) is too strong, the next admissible level is grouped cancellation:

```text
GCOEFF-CFIR:
for each invariant displacement class Delta,
sum_{omega: Delta(omega)=Delta}
   c_{alpha,i}(omega;L)
   prod_{r in omega} Lambda(r)r^(-1/2)=0.             (7)
```

The displacement class is the same multiplicative/Fourier invariant used in earlier Green-word
audits: it groups words whose total logarithmic shift is equal.  This preserves coherent cancellation
but forbids taking absolute values term by term.

## 5. Why this is progress

Earlier determinant endpoints still hid analytic convergence in phrases like "prove determinant
identification" or "prove row membership".  Here the determinant is reduced to explicit finite
coefficient identities.  A failure of `COEFF-CFIR` or `GCOEFF-CFIR` can be localized to a concrete word
class; a proof can be checked by finite multilinearity and the explicit kernel formulas.

## 6. Minimal endpoint after E72.347

The proof chain can now be stated as:

```text
COEFF-CFIR or GCOEFF-CFIR
=> CERT-CFIR
=> FINITE-CFIR
=> UREM-POLY
=> Theorem 72.329
=> compact-root HPAC decay.
```

The remaining work is no longer to find the right functional.  It is to prove the finite coefficient
annihilation identities (6) or the grouped identities (7).

## 7. Status

```text
proved: CERT-CFIR is equivalent to finite determinant identities D_{alpha,i}=0;
reduced: exact row membership to finite word coefficient identities;
introduced: COEFF-CFIR and grouped GCOEFF-CFIR as the non-tautological proof targets;
open: prove the coefficient/grouped identities.
```
