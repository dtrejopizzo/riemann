# Laguerre--Hardy nonduplication and stop gate

## Verdict

The degree generating function introduced in 103_70 is not a new
mechanism. It is exactly the fixed-cutoff prime transform already recorded
in Phase 102/233, up to the elementary factor and index shift forced by

\[
 L_N^{(1)}=\sum_{j=0}^N L_j.
\]

Its radial Parseval interpretation is the standard disk/half-plane
Laguerre--Laplace transform used in the Tricomi--Widder/Weeks method. Phase
101 had also already audited the relevant Hardy and short-window
Dirichlet-polynomial estimates.

The literal combination of Vaughan's identity with the Laguerre addition
formula was not found in the inspected literature or in Phases 0--103. That
combination is an exact decomposition, but it does not itself yield a new
estimate. The proposed continuation by separate degree-variable Hardy norms
loses the Moebius--divisor cross-cancellation and is discarded.

## 1. Exact duplication inside the project

For finite \(a=(a_m)\), 103_70 defines

\[
 A_j(a)=\sum_m {a_m\over m}L_j(\log m)
\]

and proves

\[
 \sum_{j\ge0}A_j(a)z^j
 ={1\over1-z}\sum_m a_m m^{-1/(1-z)}.                 \tag{1}
\]

For \(a_m=\Lambda(m){\bf1}_{m\le e^T}\), summing the degree coefficients
once gives

\[
 \sum_{N\ge0}\left(\sum_{j=0}^N A_j(a)\right)z^{N+1}
 ={z\over(1-z)^2}\sum_{m\le e^T}{\Lambda(m)\over
 m^{1/(1-z)}}.                                        \tag{2}
\]

The right side is exactly \(\mathcal S_T(z)\) in
233_SINGLE_TRANSFORM_FIXED_CUTOFF_GENERATOR.md, equation (2), and

\[
 \sum_{j=0}^N A_j(a)
 =\sum_{m\le e^T}{\Lambda(m)\over m}L_N^{(1)}(\log m).
\]

Thus (1) is not merely analogous to Phase 102/233: its cumulative
coefficient sequence is identical to the prime--Laguerre sequence there.
Phase 102/125 had already recorded the same Laguerre exponential generator
for the compact A1 core.

| proposed ingredient | earlier project location | result |
|---|---|---|
| disk/half-plane map \(s=(1-z)^{-1}\) | Phase 102/174, 233 | exact known coordinate |
| Hardy norm as a closure source | Phase 101/E101.057 | Hardy membership alone gives no progress; naive uniform norm rejected |
| short-window mean value for exponentially long Dirichlet polynomials | Phase 101/E101.090, Section 11 | reciprocal frequency spacing gives the obstructing length cost |
| linear Dirichlet square | Phase 70/E70.10 | creates an Euler ratio comb and divergent diagonal mass |
| global Hardy prime cancellation | Phase 70/E70.6--8 | the missing uniform estimate is RH-strength |

## 2. Public-literature provenance

The inspected public antecedents separate into three already-known pieces.

1. Bombieri--Lagarias and the later Li/Coffey literature give the arithmetic
   explicit formula for Li coefficients and its Laguerre kernel. See
   Bombieri--Lagarias, *Complements to Li's criterion for the Riemann
   hypothesis*, JNT 77 (1999), and Coffey,
   <https://arxiv.org/abs/math-ph/0505052>.
2. The passage from Laguerre coefficients to a Laplace transform composed
   with a bilinear map from a half-plane to the disk is classical
   Tricomi--Widder/Weeks theory. A modern account is Abate--Choudhury--Whitt,
   <https://doi.org/10.1287/ijoc.8.4.413>; the explicit Fourier/Laguerre
   basis and Moebius map are also displayed in
   <https://projecteuclid.org/journals/communications-in-mathematical-sciences/volume-3/issue-3/Application-of-Weeks-Method-for-the-Numerical-Inversion-of-the/cms/1128386014.pdf>.
3. Vaughan decomposition and Type I/II estimates are classical. Modern
   variants found in the search still rely on genuine oscillation in the
   arithmetic phase; see Granville,
   <https://arxiv.org/abs/2001.07777>, and Srivastav,
   <https://arxiv.org/abs/2505.07803>.

Searches through arXiv and public mathematical repositories, through
2026-07-25, found no paper proving the special ultra-long curved-contour
mean square needed in 103_70, nor a paper closing RH through this Vaughan--
Laguerre combination. Absence from a search is not a proof of novelty. In
any event, the identities are assembled from known pieces; only a successful
new bound could constitute mathematical progress.

## 3. Scale falsification of separate Hardy norms

The Cauchy step in 103_70 replaces

\[
 \sum_{j=0}^N A_j(\mu_D)A_{N-j}(b_{V,R})              \tag{3}
\]

by the product of two nonnegative norms. This deletes every relative sign
between the two degree sequences.

The loss is structural. Let a central logarithmic interval lie inside a
sign-consistent lobe of \(L_k\), with \(u\asymp k\asymp N\), and take primes
\(p>V\) in that interval. Since \(b_V(p)=\log p\), the prime number theorem
and the uniform interior Plancherel--Rotach formula give, on a fixed
subinterval of that lobe,

\[
 \sum_p {b_V(p)\over p}L_k(\log p)
 =\int L_k(u)\,du+o\!\left(\int |L_k(u)|\,du\right)
 =e^{u/2}N^{-O(1)}.                                   \tag{4}
\]

Hence the positive divisor-side Hardy norm is already exponential in a
central block. A product estimate at the \(O(N\log N)\) A1 budget would
therefore need the Moebius-side norm to compensate at exponential scale.
Neither Montgomery--Vaughan mean values, the classical zero-free region,
nor a coefficient-blind square-root model provides such a gain. The
cancellation required by A1 must remain coupled inside (3); applying
separate norms removes it.

Equation (4) is a stop-gate argument about this proof method, not a theorem
that no specially coupled bilinear estimate can exist.

## 4. Decision

    proved:
      exact identity with the Phase 102/233 transform;
      classical provenance of the Laguerre--Hardy coordinate;
      prior local coverage of Hardy and short-window mean-value obstructions;

    not claimed:
      novelty from the literal Vaughan--Laguerre bookkeeping combination;
      impossibility of every coupled bilinear estimate;

    discarded:
      separate Laguerre--Hardy Cauchy norms as an A1 closure mechanism;
      further work on generic curved-contour mean values for this route;

    only admissible successor in this family:
      a coupled signed Moebius--divisor theorem which retains cancellation
      in the degree convolution and passes the off-line A1 falsifier before
      any extended development.

## 5. Immediate successor audit: the Sturm--Liouville square

The next proposed use of the collective square in 103_67 also fails the
nonduplication gate. Put \(a=1+\varepsilon\), \(u=\log x\), and

\[
 \tau(x)=x^{-a}L_n(u).
\]

The Laguerre equation \(uL_n''+(1-u)L_n'+nL_n=0\) gives exactly

\[
 \tau''(x)=x^{-a-2}
 \left[
  \left(-2a-{1\over u}\right)L_n'(u)
  +\left(a^2+a-{n\over u}\right)L_n(u)
 \right].                                                \tag{5}
\]

The multiplier in (5) has no fixed sign and alternates on the same lobe
scale as the original A1 kernel. Integrating
\(-\frac12\int E(x)^2\tau''(x)\,dx\) by parts does not produce a positive
Sturm--Liouville energy: the distributional derivative of \(E^2\) contains
the prime-power jumps and reconstructs the first-moment/max-kernel terms
of 103_67. It is an exact return to the starting identity.

This route also fails by scale. Brent--Platt--Trudgian prove
unconditionally that, for all sufficiently large \(X\),

\[
 \int_X^{2X}(\psi(x)-x)^2\,dx\ge {X^2\over5374};
\]

see <https://arxiv.org/abs/2008.06140>. Thus the square has macroscopic
mass. Any useful estimate must exploit its signed correlation with
\(\tau''\), not absolute energy or ODE coercivity.

This successor is therefore discarded as already covered by the Laguerre
ODE audit 103_22 plus the exact reconstruction in 103_67. No separate
Sturm--Liouville branch is opened.
