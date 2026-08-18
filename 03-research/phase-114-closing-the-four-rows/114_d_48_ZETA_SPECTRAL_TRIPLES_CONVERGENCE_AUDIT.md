# D.48 — Audit of the Zeta Spectral Triples convergence gate

## 1. Primary sources and scope

This note audits the following primary preprints against D.32, D.42 and
D.47:

1. A. Connes, C. Consani and H. Moscovici, *Zeta Spectral Triples*,
   arXiv:2511.22755v1 (2025), abbreviated `CCM`;
2. A. Connes and W. D. van Suijlekom, *Quadratic Forms, Real Zeros and
   Echoes of the Spectral Action*, arXiv:2511.23257v1 (2025), abbreviated
   `CvS`.

The goal is to identify the exact convergence theorem that would imply RH,
list its missing estimates, and decide whether rows A--B--C supply any of
them.  No paper file is changed.

## 2. What the two preprints prove

Fix `lambda>1` and let `QW_lambda` be the lower-semicontinuous,
lower-bounded Weil form on

\[
 H_\lambda=L^2([\lambda^{-1},\lambda],d^*u).                  \tag{2.1}
\]

Let `E_N` be the span of the `2N+1` central Fourier modes and let
`QW_lambda^N` be the restriction.  If its smallest eigenvalue
`epsilon_(lambda,N)` is simple and the normalized eigenvector
`xi_(lambda,N)` is even, CCM constructs a rank-one perturbation

\[
 D_{\lambda,N}
 =D_{\log}^{(\lambda)}
  -|D_{\log}^{(\lambda)}\xi_{\lambda,N}\rangle
   \langle\delta_N|.                                          \tag{2.2}
\]

Their Theorem 1.1/5.10 proves:

1. `D_(lambda,N)` is self-adjoint for the inner product induced on
   `E_N/C xi_(lambda,N)` by `QW_lambda^N-epsilon_(lambda,N)`;
2. with a fixed spectral cut,
   \[
   \det_{\rm reg}(D_{\lambda,N}-z)
     =-i\lambda^{-iz}\widehat\xi_{\lambda,N}(z);              \tag{2.3}
   \]
3. every zero of `widehat xi_(lambda,N)` is real.

CvS supplies the finite/continuous zero-localization theorem used here
(finite theorem in Section 5; infinite-dimensional main theorem in Section
6).  In its continuous form, if a real even convolution distribution defines a
lower-bounded self-adjoint operator whose lowest spectral value is simple
and isolated with even eigenfunction `xi`, then all zeros of `widehat xi`
are real.  The hypotheses “simple”, “isolated” and “even” are assumptions,
not conclusions of lower boundedness.

CvS also explains why simplicity cannot be omitted: when the extremal
eigenspace has dimension greater than one, an individual eigenfunction can
have additional arbitrary nonreal zeros.  Only the common zero set of the
whole extremal space retains the corresponding localization statement.

Thus the preprints rigorously construct many finite real-zero entire
functions.  They do not prove that these functions converge to `Xi`.

## 3. The exact two-stage convergence theorem

The CCM strategy requires the following two limits.

### Stage I: Galerkin limit at fixed `lambda`

Let `xi_lambda` be the normalized ground-state eigenfunction of the closed
operator associated to `QW_lambda`.  One needs

\[
 c_{\lambda,N}\widehat\xi_{\lambda,N}(z)
   \longrightarrow\widehat\xi_\lambda(z)                      \tag{3.1}
\]

locally uniformly on `C`, for suitable nonzero normalizations.  It is enough
that the bottom eigenvalue of `QW_lambda` be simple, isolated and even, and
that the Galerkin spaces form a core.  Indeed, form convergence plus an
isolated spectral gap gives norm convergence of the Riesz projections;
compact support then upgrades `L2` convergence of eigenvectors to locally
uniform convergence of their Fourier transforms.

The core property and compact resolvent are proved in CCM.  Simplicity,
isolation from the next eigenvalue by a positive gap, and even parity of the
ground state are not.

### Stage II: expanding-window limit

One needs constants `a_lambda,b_lambda` such that

\[
 e^{a_\lambda+i b_\lambda z}\widehat\xi_\lambda(z)
   \longrightarrow\Xi(z)                                      \tag{3.2}
\]

uniformly on compact subsets, or uniformly on closed substrips, of

\[
 |\operatorname{Im}z|<\tfrac12.                               \tag{3.3}
\]

The exponential factor changes normalization and phase but has no zeros.

CCM constructs an explicit prolate candidate `k_lambda=E(h_lambda)` and
proves in Section 7, Lemma 7.3,

\[
 \widehat k_\lambda(z)\longrightarrow\Xi(z)                   \tag{3.4}
\]

uniformly on closed substrips of (3.3).  Their estimate uses

\[
 \|h_\lambda-h\|_{L^\infty[-\lambda,\lambda]}
   =O(\lambda^{-2}).                                           \tag{3.5}
\]

What is not proved is

\[
 \xi_\lambda\sim c_\lambda k_\lambda                         \tag{3.6}
\]

in a topology strong enough to transfer (3.4).  CCM Section 8 explicitly
lists (3.6), together with the simple-even ground-state condition, as the
two missing steps.

## 4. Why this convergence implies RH

> **Proposition 4.1 (Hurwitz gate).** Suppose `F_j` are nonzero entire
> functions with only real zeros and converge locally uniformly to the
> nonzero function `Xi` throughout (3.3).  Then every zero of `Xi` in that
> strip is real.

**Proof.** Let `z_0` be a nonreal zero of `Xi` in (3.3).  Choose a closed
disk centered at `z_0`, contained in the strip and disjoint from the real
axis, whose boundary contains no zero of `Xi`.  By local uniform convergence
and Rouche's theorem (equivalently Hurwitz), `F_j` has the same positive
number of zeros in that disk for all sufficiently large `j`.  This
contradicts real-rootedness of `F_j`.  QED.

Under the coordinate `Xi(z)=xi(1/2+iz)`, every nontrivial zeta zero lies in
(3.3), and `z` is real exactly on the critical line.  Hence (3.2) implies
RH.

The CCM-specific convergence is therefore at least as strong as RH.  It is
not proved to be logically equivalent to RH: RH alone does not imply that
these particular minimizers or determinants converge.

## 5. Quantitative estimate actually required

Put `L_lambda=log lambda` and use logarithmic coordinates, so the
eigenfunctions are supported in `[-L_lambda,L_lambda]`.  For a compact set
`K` contained in `|Im z|<=eta<1/2`, Cauchy--Schwarz gives

\[
 \begin{aligned}
 \sup_{z\in K}|\widehat\xi_\lambda(z)
       -c_\lambda\widehat k_\lambda(z)|
 &\le (2L_\lambda)^{1/2}e^{\eta L_\lambda}
       \|\xi_\lambda-c_\lambda k_\lambda\|_2\\
 &= (2\log\lambda)^{1/2}\lambda^\eta
       \|\xi_\lambda-c_\lambda k_\lambda\|_2.               \tag{5.1}
 \end{aligned}
\]

Thus a sufficient estimate on every closed substrip is

\[
 \boxed{
 \|\xi_\lambda-c_\lambda k_\lambda\|_2
 =o\!\left(\lambda^{-\eta}(\log\lambda)^{-1/2}\right)
 \quad\text{for every }\eta<\tfrac12.}                         \tag{5.2}
\]

Plain `L2` convergence with no rate is insufficient because the support is
expanding.  Closeness of a few low zeros, Rayleigh quotients, or plots of
the two functions also does not imply (5.2).

An endpoint normalization such as `xi_lambda(lambda)=1` additionally
requires that this boundary value be nonzero and controlled uniformly.
Point evaluation is not continuous on bare `L2`; it must be controlled in
the form/graph norm.

## 6. Residual-gap theorem: a noncircular sufficient route

There is a precise way to turn the prolate candidate into the true
minimizer without using zeta zeros.

Let `A_lambda` be the self-adjoint operator of `QW_lambda`, normalize
`v_lambda=k_lambda/||k_lambda||`, and set

\[
 q_\lambda=\langle A_\lambda v_\lambda,v_\lambda\rangle,
 \qquad
 r_\lambda=(A_\lambda-q_\lambda)v_\lambda.                    \tag{6.1}
\]

Assume there is an interval containing `q_lambda` which contains exactly
one eigenvalue `mu_lambda` of `A_lambda`, and let `g_lambda` be its distance
to the rest of the spectrum.  The spectral theorem gives

\[
 \|(I-P_\lambda)v_\lambda\|
 \le {\|r_\lambda\|\over g_\lambda},                          \tag{6.2}
\]

where `P_lambda` is the corresponding spectral projection.  Indeed, on the
orthogonal complement of `P_lambda`,
`|(A_lambda-q_lambda)|>=g_lambda`, and (6.2) follows by applying the spectral
measure of `v_lambda`.

If the eigenvalue is simple, choose its eigenvector `xi_lambda`; then after
a phase choice

\[
 \|v_\lambda-\xi_\lambda\|
 \le \sqrt2\,{\|r_\lambda\|\over g_\lambda}                   \tag{6.3}

when the right side is small.  Combining (5.1) and (6.3), a sufficient
source estimate is

\[
 \boxed{
 {\|r_\lambda\|\over g_\lambda}
 =o\!\left(\lambda^{-\eta}(\log\lambda)^{-1/2}\right)
 \quad(\eta<1/2).}                                            \tag{6.4}
\]

Parity can be handled without assuming it: since `A_lambda` commutes with
reflection, it decomposes into even and odd operators.  It suffices to prove

\[
 \mu_{\lambda,\mathrm{even}}
   <\mu_{\lambda,\mathrm{odd}}                                 \tag{6.5}
\]

and a positive gap above the even ground state.  Equations (6.4)--(6.5) are
fully source-defined.

## 7. Determinant/resolvent version

For fixed `lambda`, let `P_N` be the Fourier Galerkin projections.  A robust
route to (3.1) is norm-resolvent convergence near a contour `Gamma_lambda`
surrounding only the ground state:

\[
 \sup_{z\in\Gamma_\lambda}
 \|(P_NA_\lambda P_N-z)^{-1}P_N
      -(A_\lambda-z)^{-1}\|\longrightarrow0.                  \tag{7.1}
\]

Contour integration then gives convergence of Riesz projections.  For
determinants on expanding windows one needs more: after subtracting a
reference scaling operator, a sufficient hypothesis is local trace-norm
resolvent convergence

\[
 \|(D_{\lambda,N}-z)^{-1}-(D_{\rm ref,\lambda}-z)^{-1}
      -R_\lambda(z)\|_1\longrightarrow0                       \tag{7.2}
\]

uniformly on compact resolvent sets, together with locally uniform bounds
on the trace norms and control of the spectral-cut phase.  The standard
Fredholm determinant estimate

\[
 |\det(I+A)-\det(I+B)|
 \le \|A-B\|_1
   \exp(1+\|A\|_1+\|B\|_1)                                   \tag{7.3}
\]

then gives determinant convergence.

For the `lambda -> infinity` step, (7.2) must be uniform after the
normalizing exponential and strong enough on every closed substrip.  Merely
having compact resolvent for each `lambda`, or convergence of finitely many
eigenvalues, does not imply (7.2).

## 8. Comparison with D.32

D.32 gives an exact, zero-free formula for every prime power and the full
Gamma term:

\[
 B_{\rm nuc}(F,G)
 =\langle\mathbf S_TF,\mathbf S_TG\rangle
  -\langle\mathbf B_TF,\mathbf B_TG\rangle.                    \tag{8.1}
\]

On a fixed support window only finitely many prime-power translations
occur.  Therefore D.32 contributes two real facts to the CCM route:

1. it identifies the exact source operator `A_lambda`/form matrix, including
   all `p^k` and the Gamma finite part;
2. it provides a canonical Gamma operator plus bounded finite-place
   perturbation, suitable for writing the residual `r_lambda` in (6.1) and
   a Birman--Schwinger resolvent.

D.32 does **not** estimate `||r_lambda||`, prove the lower spectral gap
`g_lambda`, establish the parity inequality (6.5), or give the expanding
support rate (6.4).  Its signed factorization (8.1) cannot be converted into
those estimates by dropping either norm.

## 9. Comparison with D.42

D.42 proves the exact Frechet two-chart identification

\[
 \sigma_\zeta:\mathcal L_\gamma^0\xrightarrow{\sim}
 Z\mathcal H_\cap                                             \tag{9.1}
\]

and hence identifies the correct nuclear cokernel and all Gamma residue
conditions.  This contributes:

1. the correct topology for the limiting character;
2. exact control of the two primitive values and Gamma chart gluing;
3. a target against which a successful determinant limit can be compared.

It does not supply a positive Hilbert norm or resolvent convergence.  D.41
shows that the ordinary critical-line `L2` completion has dense relation
range and zero quotient.  Consequently (9.1) cannot be fed directly into
the Hilbert resolvent estimate (7.2) without constructing a new faithful
graph/reproducing norm; doing so is the row-D completion problem.

## 10. Comparison with D.47

D.47 rewrites the primitive Hodge theorem on each compact window as the
index-one/hyperbolic-boundary certificate

\[
 \operatorname{In}(A_T)=(1,\infty,0),
 \qquad \operatorname{In}(G_T)=(1,1,0),
 \qquad G_T=M_TA_T^{-1}M_T^*.                              \tag{10.1}
\]

The two ruling jets form a hyperbolic plane; they do not provide two
positive directions.

This does not imply the CCM ground state is simple or even.  The inertia
count in (10.1) concerns the number of positive directions of the
upper-bounded sign convention; the CCM theorem concerns simplicity and
parity of the lowest eigenvalue of the lower-bounded form.  An operator can
have the required inertia and a multiple or odd lowest eigenvalue.

Conversely, CCM simple-even ground states do not imply (10.1).  They
localize the zeros of one Fourier transform but do not bound the total
positive index of the primitive Weil form.

If the uniform D.47 index-one theorem and hyperbolic Green signature were proved,
row D and RH would already follow without CCM convergence.  Thus D.47 is a
parallel exact gate, not a presently available hypothesis for (3.2).

## 11. Birman--Schwinger subroute supplied by the exact ABC decomposition

Write on a fixed window

\[
 A_\lambda=G_\lambda+K_\lambda,                               \tag{11.1}
\]

where `G_lambda` is the explicit Gamma pseudodifferential operator and
`K_lambda` is the finite sum of prime-power translations from D.32.  For
`z` in the resolvent set of `G_lambda`, define

\[
 \mathcal B_\lambda(z)
 =\operatorname{sgn}(K_\lambda)|K_\lambda|^{1/2}
   (G_\lambda-z)^{-1}|K_\lambda|^{1/2}.                        \tag{11.2}
\]

The resolvent identity gives

\[
 (A_\lambda-z)^{-1}
 =(G_\lambda-z)^{-1}
 -(G_\lambda-z)^{-1}|K_\lambda|^{1/2}
  (I+\mathcal B_\lambda(z))^{-1}
  \operatorname{sgn}(K_\lambda)|K_\lambda|^{1/2}
  (G_\lambda-z)^{-1}.                                         \tag{11.3}
\]

This is a noncircular possible route because every term is source-defined.
It would suffice to prove:

1. uniform Schatten bounds for `B_lambda(z)` on contours surrounding the
   candidate ground state;
2. a uniform lower bound on
   `||(I+B_lambda(z))^{-1}||` away from one simple even pole;
3. the residual estimate (6.4) for `k_lambda`;
4. trace-norm convergence of the normalized resolvent difference needed in
   (7.2).

The prime sum grows with the window and is not a uniformly small operator
perturbation.  Therefore a Neumann-series estimate based only on
`||B_lambda||<1` is not presently available.  The viable refinement is to
separate the two ruling/low-rank boundary block by the Schur complement of
D.47 and estimate the Birman--Schwinger operator on the primitive
complement.  Proving that its crossing index is zero is again the substantive
uniform index/angle theorem; it is not furnished by ABC exactness.

## 12. Exact audit table

| Requirement | CCM/CvS | D.32 | D.42 | D.47 | Status |
|---|---|---|---|---|---|
| finite self-adjoint approximants | conditional on simple-even | exact matrix entries | no | no | conditional |
| all finite determinant zeros real | yes under simple-even | compatible | no | no | conditional |
| ground state exists | yes | compatible | no | compact-window form | proved |
| ground state simple and even | assumed/missing | no | no | not implied by inertia | open |
| fixed-window Galerkin convergence | follows from isolated simple ground state | core-compatible | no | no | conditional |
| `k_lambda -> Xi` | proved | compatible Gamma/primes | compatible target | no | proved |
| `xi_lambda ~ c_lambda k_lambda` with rate (5.2) | missing | defines residual only | no | no | open |
| uniform determinant/resolvent convergence | missing | exact input, no estimate | target topology only | possible Schur split | open |
| primitive sign/Hodge index one | not proved | exact signed form | no | exact reformulation | open |

## 13. Verdict

The primary CCM/CvS results are rigorous and important: subject to a
simple-even extremal eigenvector, each finite/truncated determinant has only
real zeros.  The RH-bearing theorem is the locally uniform convergence of
these real-zero determinants to `Xi` on `|Im z|<1/2`.

Two hypotheses remain essential:

1. the ground state of the Weil operator is simple, isolated and even;
2. the true minimizer approximates the prolate candidate at the weighted
   rate (5.2), or an equivalent uniform resolvent/determinant estimate.

ABC improves the typing of the route.  D.32 supplies the exact `p^k+Gamma`
operator needed to calculate residuals; D.42 supplies the correct Frechet
limit target; D.47 supplies a Schur/index decomposition.  None supplies the
gap, parity ordering, weighted eigenvector estimate, or uniform trace-norm
resolvent bound.  The limit therefore remains an RH-strong missing theorem,
not a consequence of completed rows A--B--C.

The most concrete noncircular continuation is (11.2)--(11.3): isolate the
two boundary directions by the D.47 Schur complement, then prove uniform
Birman--Schwinger resolvent bounds and the residual/gap estimate (6.4) on
the primitive complement.
