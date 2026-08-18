# D.169 — Stable contracted-coupling diagnostic

## Scope

The raw directed Hurwitz--Lerch formula used successfully for the finite
low/low Gamma block is numerically ill-conditioned in the rectangular
high/low block: enormous endpoint-derivative terms cancel to produce a small
answer.  Increasing precision on the already assembled rectangular matrix is
therefore not a reliable route to the remaining Feshbach enclosure.

`114_d_169_contracted_fft_diagnostic.py` instead synthesizes the five columns
of the finite Schur graph first, applies the complete Fourier multiplier

\[
 \Re\psi(1/4+i\tau/2)-\psi(1/4)
\]

together with the constant term and the contacts at (2,3,4), and only then
extracts the Legendre coefficients of orders (200\le n<800).  This order of
operations avoids the artificial cancellation.

For a box of length (32) and (2^{18}) grid points, the observed column
norms are

\[
 (2.49\,10^{-7},\ 4.51\,10^{-6},\ 4.76\,10^{-5},\
   7.83\,10^{-4},\ 4.12\,10^{-3}).
\]

In the most delicate first direction, the squared diagnostic norm divided by
the known complement gap is smaller than the directed finite eigenvalue by
about one order of magnitude.  Thus the exact directional Feshbach closure is
numerically plausible; the scalar trace bound failed because it discarded this
anisotropy.

The direct physical norms on the interval (not merely the displayed Legendre
rows) are

\[
 (2.71\,10^{-7},\ 4.87\,10^{-6},\ 7.71\,10^{-5},\
   8.50\,10^{-4},\ 4.96\,10^{-3}).
\]

They are unchanged to the printed digits when the periodization box is doubled
from (32) to (64) at fixed mesh.  If (\(H_{\mathrm{FFT}}\)) denotes their full
cross Gram and the rigorous complement gap is weakened to (0.218), the
diagnostic eigenvalues of the exact matrix target are

\[
 \lambda\left(K_{\rm final}-0.218^{-1}H_{\rm FFT}\right)
 =
 \begin{pmatrix}
 2.78\,10^{-12},&5.48\,10^{-10},&2.88\,10^{-7},&
 2.79\,10^{-5},&1.99\,10^{-3}
 \end{pmatrix}.
\]

Thus the remaining directed computation has a positive numerical margin in
all five directions and can be formulated without any infinite Legendre-tail
summation: D.150 gives the fifteen entries of the total Gram directly as
one-dimensional integrals.

## Logical status

This is **not** a certificate: FFT periodisation, discretisation, interpolation,
the tail (n\ge800), and the exact primitive projection are not enclosed.
The rigorous replacement must evaluate the already-contracted columns by the
pointwise formula of D.150, enclose their Legendre coefficients, and prove an
analytic tail bound.  No conclusion about the endpoint sign is drawn here.
