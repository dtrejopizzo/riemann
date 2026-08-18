# E77.6 - Iterated-Limit IDENT

**Run:** 2026-07-18.

## 1. Purpose

The joint-rate program `E77.5d--E77.5ah` is retired from the proof chain.
Its exact identities remain available, but its sign and cone conditions are
falsifier diagnostics, not forcing mechanisms.  The admissible replacement is

```text
fixed-L Weyl convergence
+ safe arithmetic identification of the fixed-L limit
+ outer L-limit
+ a cofinal diagonal
=> SR-LOG-2SCALE => IDENT.
```

This formulation requires LP separately for each fixed `L`; no LP estimate
uniform in `L` is assumed.

## 2. Cofinal Diagonal Lemma

Let

```text
K_m = [1/2+1/m,m],  m>=3,
E_{L,N}(sigma) = finite safe derivative error,
E_L(sigma)     = the intrinsic fixed-L error.
```

Assume:

```text
(A) for every fixed L and compact K subset (1/2,infinity),
    sup_K |E_{L,N}-E_L| -> 0 as N->infinity;

(B) for every compact K subset (1/2,infinity),
    sup_K |E_L| -> 0 as L->infinity.
```

Then there are increasing sequences `L_m,N_m` such that

```text
L_m -> infinity,
N_m/L_m -> infinity,
sup_K |E_{L_m,N_m}| -> 0
```

for every compact `K subset (1/2,infinity)`.

### Proof

Choose `L_m>max(m,L_{m-1})` so that

```text
sup_{K_m}|E_{L_m}| < 1/(2m).
```

With this `L_m` fixed, choose

```text
N_m > max(N_{m-1},m L_m)
```

so that

```text
sup_{K_m}|E_{L_m,N_m}-E_{L_m}| < 1/(2m).
```

Therefore `N_m/L_m>=m` and

```text
sup_{K_m}|E_{L_m,N_m}| < 1/m.
```

Every compact safe `K` is contained in `K_m` for all sufficiently large
`m`, proving local uniform convergence.  This is an existence theorem; no
explicit rate for `N(L)` is required.  QED.

The same construction can satisfy finitely many additional errors at stage
`m`.  It will later absorb the PROLATE, WEIL-TAIL, and FOURIER-SHELL pairings
into one common diagonal.

## 3. Exact Obligations

### A. FIXED-L-WEYL

For every fixed `L` and safe compact `K`, prove

```text
T'_{L,N}(i sigma)/T_{L,N}(i sigma) -> m_L(i sigma)
```

locally uniformly on `K`.  The statement includes two distinct clauses:

```text
convergence:    LP contracts the finite Weyl disks;
identification: the limit is the intrinsic m-function of the complete
                fixed-L semi-infinite CCM system.
```

The identification clause must include the fixed-L Fourier endpoint from
`RFL-2`.  Convergence to an unidentified truncation limit is insufficient.

### B. SAFE-GAMMA-IDENT

Identify the intrinsic fixed-L function through the coupled Gamma-prime/cell
formula.  In derivative form the finite expression is

```text
G_{L,N}(sigma)
 = L coth(sigma L/2)
   + 2 Re(i T'_{L,N}(i sigma)/T_{L,N}(i sigma))
   - B_ext,L,N(sigma).
```

After `N->infinity`, the target `G_L` must be obtained as an identity of
holomorphic functions in `s=1/2+sigma>1`, with archimedean and prime terms
kept coupled until the logarithmic derivative is formed.

### C. OUTER-LIMIT

Prove locally uniformly on the safe axis that

```text
G_L(sigma) -> 2 Xi'(s)/Xi(s),  s=1/2+sigma.
```

In the absolute region the target has the exact expansion

```text
2 Xi'(s)/Xi(s)
 = 2/s + 2/(s-1) - log(pi) + digamma(s/2)
   - 2 sum_{n>=2} Lambda(n)n^(-s).
```

Integrating from the safe normalization point `sigma_0` then gives the
logarithmic form of IDENT without a branch or additive-constant ambiguity.

## 4. Derivative Probe

The finite derivative identity is exact wherever `T(i sigma) != 0`:

```text
d/dsigma [2 log sinh(sigma L/2)] = L coth(sigma L/2),
d/dsigma [2 log |T(i sigma)|]    = 2 Re(i T'(i sigma)/T(i sigma)).
```

Adding the two equalities proves the displayed `L coth` formula.  The probe
below verifies its implementation by differentiating the finite logarithm
independently.

Companion probe:

```text
E77_6_iterated_limit_ident_probe.py
```

Command:

```bash
python3 E77_6_iterated_limit_ident_probe.py \
  --lambda 6 --modes 18 --dps 70 --prime-cutoff 200000
```

The probe independently differentiates

```text
log(sinh(sigma L/2)^2 |T(i sigma)|^2)
```

and compares it with `L coth+2 Re(iT'/T)`.  It separately compares the
completed-zeta derivative with a truncated von Mangoldt expansion.

| build | max finite derivative identity error | max finite/Xi error |
|---|---:|---:|
| zeta | 2.85e-70 | 0.375658 |
| planted | 2.73e-71 | 50.4676 |

Euler truncation at `x=200000`:

| sigma | s | relative error |
|---:|---:|---:|
| 0.55 | 1.05 | 4.276e2 |
| 0.75 | 1.25 | 5.462 |
| 1.00 | 1.50 | 9.693e-2 |
| 1.50 | 2.00 | 7.239e-5 |
| 2.00 | 2.50 | 8.115e-8 |
| 3.00 | 3.50 | 1.635e-13 |

The slow convergence near `s=1` is expected and shows why OUTER-LIMIT must
be stated locally uniformly only after fixing a compact inside the open safe
region.  These numbers do not prove OUTER-LIMIT.

## 5. Falsifier Location Rule

Outcome A predicts:

```text
plant passes A: fixed-L LP/Weyl convergence;
plant passes C: the abstract diagonal lemma;
plant fails B: SAFE-GAMMA-IDENT / OUTER-LIMIT.
```

The planted finite derivative identity passes to roundoff, while its mismatch
with the zeta arithmetic target is `10.98--50.47` over the tested sigma grid.
This is consistent with the prediction, but E77.8 must audit the full limiting
chain.  If the planted build fails first in A or in the diagonal glue, or if it
passes B, the architecture is circular or one endpoint has been misidentified.

## 6. Admissibility Rule

Every future reduced target must include a proved implication to its immediate
predecessor.  A quantity that merely separates zeta from the planted build is
archived as a detector and is not pursued as a proof target.

## 7. Status

```text
proved:    cofinal diagonal lemma A+B => SR-LOG-2SCALE;
proved:    exact calculus identity producing L coth+2 Re(iT'/T);
observed:  zeta finite/Xi error 0.369--0.376 at L6,N18;
observed:  planted mismatch 10.98--50.47 at the arithmetic target;
open:      FIXED-L-WEYL, including intrinsic fixed-L identification;
open:      SAFE-GAMMA-IDENT and OUTER-LIMIT;
next:      E77.7 TRICOMI-LP setup at fixed L.
```
