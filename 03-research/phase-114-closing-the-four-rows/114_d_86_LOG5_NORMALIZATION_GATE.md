# D.86 — `log(5)/2` corrected assembly gate

The mesh has endpoints induced by the displacements `log 2`, `log 3`, and
`log 4`.  Its seven macrocells have lengths

`log(5/4), log(4/3), log(6/5), log(5/4), log(6/5), log(4/3), log(5/4)`.

## Invalidated first run

The first contact assembler recognized a translation only when the midpoint
of a source cell landed on the midpoint of a target cell.  That is false on
this mesh: translated cells overlap cells without being aligned with them.
In particular it incorrectly returned zero for the `n=3` correlation.  The
reported even value near `-0.158` was therefore an artifact and is withdrawn.

The corrected assembler integrates each translated overlap on the common
refinement of the original and translated endpoints.  Degree `DEG+1` Gauss
quadrature is exact for every resulting product of degree-`DEG` Legendre
polynomials.

## Corrected floating audit

With 109 cells, degree nine, and exact numerical projection to the Tate
moment kernels, the *moderate-kernel matrix* gives

* even: `-0.00187079779423`, second `-0.00183859685777`;
* odd: `-0.00193230764234`, second `-0.00178964249200`.

These are not negative values of the full Weil form.  On the corrected even
Ritz vector the independently integrated terms are

* translated contacts: `+0.12107035747200505`;
* truncated gamma Fourier integral: `-0.121070948842668`;
* their direct sum: `-5.91370663e-7`;
* full gamma integral through `|tau|=200`: `-0.12106998158145951`;
* corresponding direct full sum: `+3.75890546e-7` before the positive
  remaining Fourier tail.

The discrepancy between the matrix gamma value `-0.12294115526623421` and
the direct gamma value is the unresolved same-cell quadrature/projection
error in the floating matrix assembler; it is numerically the size of the
spurious moderate Ritz deficit.  Consequently this endpoint is a
near-kernel selection problem, not a normalization failure.

## Gate

No negative conclusion and no directed positivity claim is authorized from
this floating calculation.  The next proof obligation is an analytic/directed
same-cell gamma assembly, followed by a positive Fourier-tail capacity bound,
as in the certified `T=log 2` endpoint.  This note is an audit gate, not a
row-(d) conclusion.
