# D.88 — conforming-spline audit at `T=log(5)/2`

This note records a selection experiment, not a certificate.

## Why the discontinuous space was rejected

The cellwise Legendre space used in the first `log(5)/2` experiment is not
preserved by the incommensurable translations `log 2`, `log 3`, and `log 4`.
Once the contact action is evaluated on the common refinement, translated
jumps give a very large `QCP` component (`HS^2` already exceeded `13.7` after
only 12 of 109 target cells).  Thus the old assertion that contacts map `P`
to `P` is false away from the commensurable `T=log 2` endpoint.

## Conforming replacement

`114_d_88_log5_conforming_spline_float.py` uses cardinal degree-five
B-splines supported inside the interval.  The mass, contact, and contact-image
Gram matrices are integrated on the common refinement.  The identity

`(QCP)^*(QCP)=(CP)^*(CP)-(PCP)^*G^{-1}(PCP)`

then measures the complement coupling without constructing `Q`.

For 120 intervals (dimension 115), numerical exact projection to both Tate
moment kernels gives the first truncated-gamma Ritz values

`-3.3113e-6, -3.1489e-6, +5.5819e-7, 1.5452e-4, ...`.

They are near-kernel selection data only; the omitted positive gamma tail is
of the relevant scale.  More importantly, the full contact coupling is

`beta_contact^2 = 0.7978326`, `beta_contact = 0.8932147`.

The large worst-case value is a boundary/partial-translation phenomenon, not
a polynomial-regularity defect.  Truncated translations are non-compact
partial isometries, so no finite-dimensional spline refinement is expected to
make their operator-norm complement coupling small uniformly.

## Consequence for the proof route

The generic Schur route that bounds contacts separately by `||QCP||` is not
viable at this endpoint.  A successful proof must either

1. treat the gamma and contact operators jointly on the complement (for
   example through their joint symbol/limit operators), or
2. use a mode-specific Feshbach/capacity argument that does not replace the
   contact cancellation by its global operator norm.

No row-(d) conclusion is asserted here.
