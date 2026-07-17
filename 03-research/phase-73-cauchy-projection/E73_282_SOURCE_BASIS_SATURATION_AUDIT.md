# E73.282 - Source basis saturation audit

Date: 2026-07-14.

## 1. Purpose

E73.281 corrected the coefficient interpretation: generated columns pair zero
with `xi_L` exactly, and nonzero generated pairings in canonical coordinates
come from representation error.  E73.282 asks whether this error can be removed
by simply enriching the canonical source basis.

## 2. Test

For the source family

```text
cauchy0_gamma(d)=DD_L(-gamma,d),
rat_{gamma,beta,r}(d)=DD_L(-gamma,d)/(d^2+beta^2)^r,
endpoint_{gamma,q}(d)=d^(2q)DD_L(-gamma,d),
```

increase:

```text
r <= rMax,
q <= eMax,
```

and measure:

```text
imageRel     = max relative error for E_LP_L represented in S_L,
genCoeffB    = exponent of the spurious coefficient pairing xi^*S_LA_L,
rhoFitRel    = relative error representing rho=qH(I-P),
rhoCoeffErrB = exponent of the difference between coefficient center and true center.
```

If the family were converging toward an exact symbolic closure, increasing
`rMax,eMax` would reduce these errors coherently.

## 3. Result

Increasing the basis does not improve the scalar representation.  It quickly
destabilizes the coordinate system:

```text
rank collapses as columns are added,
condition exponents remain huge,
imageRel worsens from 1e-6--1e-7 to 1e-1--1e0,
rhoCoeffErrB becomes much larger than the true APR center.
```

Representative pattern:

```text
rMax=3,eMax=2: imageRel about 1e-7--1e-5, but scalar error still ~ L^-7 to L^-12;
rMax>=5:      imageRel can jump to 1e-2--1e-1 or worse.
```

The enriched least-squares basis is not approaching an exact source complex.

## 4. Meaning

The obstruction is not simply that the source basis was too small.  The
problem is that the numerical source basis is highly redundant and
ill-conditioned.  Adding more rational powers creates near-dependencies and
amplifies scalar error.

Thus the next step cannot be:

```text
add more atoms and refit.
```

It must be:

```text
derive a minimal exact partial-fraction basis and exact coefficient map.
```

Only after this exact algebraic basis is built can one form the source complex

```text
P_L --E_L--> S_L --ell_L--> C
```

and use the identity `ell_L E_L=0` without numerical contamination.

## 5. Corrected finite target

The exact source-complex theorem should be stated as:

```text
EXACT-SRC:
There exists a minimal symbolic source basis S_L^ex and a primitive basis
P_L^ex such that

E_L P_L^ex = S_L^ex A_L^ex
```

entrywise as a partial-fraction identity, and

```text
rho_{j,w}=S_L^ex c_{j,w}^ex + e_{j,w},
e_{j,w}xi_L=O_M(L^(-M)).
```

Then `ell_L A_L^ex=0` is exact, not a fitted numerical property.

The remaining arithmetic theorem becomes:

```text
EXACT-QUOT-APR:
ell_L([c_{j,w}^ex])=O_M(L^(-M))
```

in the exact quotient by `Image A_L^ex`.

## 6. Status

```text
tested: saturation of the current canonical source family;
rejected: brute-force enrichment by higher rational/endpoint powers;
identified: need minimal exact partial-fraction basis;
open: derive S_L^ex and A_L^ex symbolically.
```
