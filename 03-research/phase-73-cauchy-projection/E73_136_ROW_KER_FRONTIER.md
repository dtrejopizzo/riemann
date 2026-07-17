# E73.136 - ROW-KER Frontier

Date: 2026-07-12.

This note consolidates the CSV/ROW-KER work after E73.124--E73.135.

## 1. What survived

The surviving target is:

```text
ROW-KER_17:
for each natural-height critical row gamma,

|<xi_L,e_gamma>| <= C L^{-17-p_gamma},

where

e_gamma = k_gamma/||k_gamma||,
k_gamma(d_n)=1/(-gamma-d_n),
||k_gamma|| <= C L^{p_gamma}.
```

Then:

```text
ROW-KER_17 => CSV_17
```

by E73.133, and:

```text
CSV_17 + elementary envelopes => Asymptotic Standard-Box Theorem
```

by E73.123.

## 2. What failed

Three plausible shortcuts failed or were degraded:

```text
1. Arch/free geometry:
   false.  The arch/free vector does not satisfy CSV.

2. Displacement-image projection:
   tautological.  <xi,(H-mu)Y>=0 for every Y, so it cannot explain
   <xi,k_gamma>.

3. First-order arch perturbation:
   false.  The prime perturbation reorients the ground vector
   non-perturbatively in the CSV channel.

4. Raw constrained evaluation gap:
   numerically ill-conditioned.  The low spectrum is too compressed for
   min_{v perp e}<v,Hv>-lambda_0(H) to resolve ROW-KER.
```

## 3. What the data says

E73.134 gives the right rowwise invariant:

```text
q_gamma-p_gamma >= 17
```

for all tested asymptotic rows `lambda>=20`, where

```text
p_gamma = log ||k_gamma|| / log L,
q_gamma = -log |<xi,e_gamma>| / log L.
```

This remains true even for near-pole rows where `p_gamma` is large.

## 4. The remaining proof route

The proof must attack the direct orthogonality

```text
<xi_L,e_gamma> ~= 0
```

from the full zeta-coupled cell equation.  The likely usable structure is
not the full matrix spectral gap but the explicit cell formula:

```text
H_L = W02_L - WR_L - Prime_L.
```

The desired identity should have the shape:

```text
<xi_L,e_gamma>
 =
 CellCancel_gamma(L) + EndpointResidual_gamma(L),
```

where:

```text
CellCancel_gamma(L) = 0
```

by an exact coupled arch/prime cancellation, and:

```text
|EndpointResidual_gamma(L)| <= C L^{-17-p_gamma}.
```

This is the next mathematical construction.  It is finite, explicit, and
does not use zeros as input.

