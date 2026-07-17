# E73.010 - Image subspace certificate

## 1. Purpose

E73.009 shows that raw least-squares coefficients in the `RAT-DD` basis are not stable.  This note
replaces coefficient extraction by the canonical object: the image subspace

```text
Image((C_E-mu I) RAT-DD_p).
```

## 2. Certificate

For a source `S_b`, define

```text
dist_p(S_b)
= ||(I-P_p)S_b||/||S_b||,
```

where `P_p` is the orthogonal projector onto

```text
Image((C_E-mu I) RAT-DD_p).
```

If `dist_p(S_b)` is small and the only remaining component is the eigenline component
`<xi,S_b>`, the source has the desired structured coborder up to the actual `NAT-SRC` residual.

## 3. Results

The numerical results are in `E73_010_RESULTS.md`.

The key observation is:

```text
effective image rank: 8--9,
relative distance:    about 10^-6 or smaller,
coefficient basis:    highly ill-conditioned.
```

Thus the proof object should be a low-rank image identity, not raw coefficient formulas.

## 4. Updated target

The structured primitive theorem becomes:

```text
IMAGE-RANK:
S_b belongs to Image((C_E-mu I) RAT-DD_p) plus an eigenline residual and Phase 72 endpoint residuals,
with a canonical finite rank certificate.
```

Then:

```text
IMAGE-RANK + NAT-SRC residual bound => NAT-PROJ.
```

## 5. Status

```text
redirected: coefficient-law search -> low-rank image subspace certificate;
open: derive the rank 8--9 image identity symbolically.
```

