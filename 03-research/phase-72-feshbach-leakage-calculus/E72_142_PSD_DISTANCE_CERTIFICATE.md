# E72.142 -- PSD distance certificate for NHS

**Date:** 2026-07-09.
**Role:** turn the negative-Hilbert-Schmidt gate into an SDP-style finite certificate.

## 0. Identity

For a Hermitian matrix `K`, let `K^-` be its negative spectral part.  Then:

```text
||K^-||_HS = dist_HS(K, PSD),
```

where:

```text
dist_HS(K,PSD):=inf_{P>=0} ||K-P||_HS.
```

### Proof

Diagonalize:

```text
K=U diag(lambda_i)U^*.
```

The Frobenius norm and the PSD cone are unitarily invariant.  Thus the closest PSD matrix may be
taken diagonal in the same basis, and the scalar problem is:

```text
min_{p_i>=0} sum_i (lambda_i-p_i)^2.
```

The minimizer is:

```text
p_i=max(lambda_i,0).
```

The squared distance is:

```text
sum_{lambda_i<0} lambda_i^2 = ||K^-||_HS^2.
```

`QED`

## 1. Finite SDP certificate

Apply this to:

```text
K_rel=C_model^(-1/2)(C_actual-C_model)C_model^(-1/2).
```

Then `NHS` is equivalent to the existence of a positive semidefinite matrix `P_x` such that:

```text
P_x >= 0,
Tr((K_rel-P_x)^2) <= eta_H^2 < 1.                           (PSD-DIST)
```

This is a finite semialgebraic certificate.  If one wants to remove spectral language completely,
`P_x>=0` can be checked by principal minors and the trace-square inequality is polynomial in the
entries of `P_x` and `K_rel`.

## 2. Consequence

The current sharp route can now be written without spectral projections:

```text
CGE-K + ROP + GCOER + PSD-DIST + MSB
=> scalar WRL resonance annihilation.
```

This is the most explicit finite form so far:

```text
GCOER:    row-wise inequalities for C_model,
PSD-DIST: one finite PSD approximation inequality for the relative arithmetic perturbation,
MSB:      one finite norm product,
ROP:      one finite operator/packet product,
CGE-K:    one finite graph-energy tail inequality.
```

## 3. Diagnostic

The companion script:

```text
E72_142_sdp_distance_certificate_probe.py
```

constructs the closest PSD matrix by spectral projection and reports the distance.  The construction is
only for verification; the theorem above states the equivalent finite existence certificate.

Representative output:

```text
E72.142 SDP distance certificate probe
 lam   L  dim  distPSD  dist2  margin  minP  minK
```

## 4. Status

```text
proved: PSD-DIST is equivalent to NHS;
proved: CGE-K + ROP + GCOER + PSD-DIST + MSB imply scalar WRL;
open:   prove PSD-DIST uniformly, or exhibit an explicit algebraic P_x with bounded distance.
```
