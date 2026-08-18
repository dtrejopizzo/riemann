# D.165 — Directed flat-five ambient moments and the missing-projection no-go

## Verdict

At \(T=\frac12\log 5\), the four complete joint-multiplier moment
matrices on the five endpoint-flat dangerous columns have now been enclosed
with directed Arb arithmetic.  They contain the three active contacts
\(2,3,4\) and the full digamma/Gamma multiplier before taking powers.
The largest entry radii, including the frequency tail, are

\[
 2.89\,10^{-16},\quad 6.82\,10^{-16},\quad
 1.06\,10^{-15},\quad 3.65\,10^{-15}
\]

for \(H_1,H_2,H_3,H_4\), respectively.

These data do **not** equal powers of the primitive compressed operator
beyond the first moment.  If \(M_r\) is the ambient Fourier multiplier and
\(P_T\) is the time--Tate projection, then the primitive operator is
\(A=P_TM_rP_T\).  The calculation encloses \(S^*M_r^jS\), whereas the
Feshbach identities require \(S^*(P_TM_rP_T)^jS\).  For \(j\ge2\) the
missing intermediate projectors are essential.  Feeding the ambient
moments into the three-moment graph algebra produces a negative matrix
which must be read as a projection-mismatch diagnostic, not as a property
of the true graph.

No paper file is modified.

## 1. Directed source frame

The five columns lie in

\[
 (T^2-t^2)^{20}\mathbf R[t]_{\le129}
 \cap\ker M_+\cap\ker M_-.
\]

`114_d_160_endpoint_flat_arb_frame.py` constructs the Gegenbauer frame
over exact rationals, freezes only the numerical selector, and solves each
two-by-two Tate system with Arb.  At 300 decimal digits all ten Tate moments
are balls containing zero with radii below \(5\,10^{-299}\).  The directed
column Gram differs from the identity by less than \(8\,10^{-15}\) at its
centres.  Twenty endpoint jets vanish algebraically, rather than by
floating cancellation.

The serialized proof source is
`/tmp/d160_flat_arb_columns5_300.npz`; all binary64 radii and derivative
norm upper endpoints are widened outward.

## 2. Complete multiplier moments

For source columns \(F_a,F_b\), put

\[
 (H_j)_{ab}={1\over2\pi}\int_{\mathbf R}
 r_T(\tau)^j\widehat F_a(\tau)\widehat F_b(-\tau)\,d\tau,
 \qquad 1\le j\le4,
\]

where

\[
 r_T(\tau)=\Re\psi(1/4+i\tau/2)-\log\pi
 -2\sum_{n=2,3,4}{\Lambda(n)\over\sqrt n}
 \cos(\tau\log n).
\]

Each unit frequency cell is integrated with a certified Gauss--Legendre
rule.  The analytic quadrature remainder uses a Bernstein ellipse contained
in \(|\Im\tau|<1/2\).  Its Fourier majorant is the dependency-free bound

\[
 |\widehat F(x+iy)|\le\sqrt{2T}\,\|F\|_2e^{T|y|}.
\]

The directed bands are

\[
 [0,64],\ [64,512],\ [512,1024],\ [1024,1536],\ [1536,2048].
\]

The first three use order 64; the last two use order 40.  Each band carries
its own analytic quadrature error.  Mixed orders cause no logical issue,
because the interval additivity of the integral is exact.

Beyond \(R=2048\), repeated integration by parts and the twenty vanishing
jets give polarized tail bounds.  The worst \(H_4\) entry tail is

\[
 6.953\,10^{-21}.
\]

`114_d_163_aggregate_matrix_moments.py` adds the five band enclosures and
the tail once, checks the independently integrated symmetric entries
overlap, and writes
`/tmp/d163_flat5_complete_R2048_Q64.npz`.

## 3. Why the ambient moments cannot feed the Feshbach graph

Formally feeding the ambient moments into the three-moment algebra gives
midpoint eigenvalues

\[
 \lambda(\mathcal S_5)=
 (-12.82,-2.38,-1.06,-0.53,21.07),
\]

while the alleged residual Gram has largest midpoint eigenvalue about
\(1.33\,10^3\).  More decisively, the reconstructed matrix which would be
\(C^*DC\) is indefinite.  Since the independently certified complement
satisfies \(D>0\), a genuine matrix \(C^*DC\) cannot be indefinite.

The contradiction identifies the exact error: multiplication by \(r_T^j\)
in the ambient Fourier space omits the support and Tate projections between
successive applications.  Only \(H_1\) is automatically unchanged because
the source columns already lie in the primitive range.  The identities
recovering \(M_0,M_1,M_2\) remain valid when supplied with true compressed
moments, but formula (3.1) of D.155 does not supply those moments.

Thus the directed integrations remain valid certificates for the ambient
joint moments.  They cannot be cited as a Feshbach or residual certificate.
The true projected powers must be evaluated by applying the complete
spatial operator and reprojecting after every step, as in D.150/D.156, or
by an exactly equivalent projected-kernel construction.

## 4. Exact remaining endpoint gate

The rank-60 spatial audit reduces the safe part to two directed assertions:

1. positivity of its finite graph shorting \(\mathcal S_{ss}\);
2. the scalar trace bound
   \[
   \mathrm{Tr}
   (\mathcal S_{ss}^{-1/2}R_{ss}^*R_{ss}
    \mathcal S_{ss}^{-1/2})<\delta.
   \]

Indeed the normalized residual is positive, hence it is bounded above by
its trace times the identity.  The floating ratio of this trace to
\(\delta\) is about \(0.466\), leaving a coarse directed margin.  These two
claims still require directed rank-60 contractions formed with an actual
projection after every operator application; selector-only matrices and
ambient multiplier powers cannot be cited as proof.
