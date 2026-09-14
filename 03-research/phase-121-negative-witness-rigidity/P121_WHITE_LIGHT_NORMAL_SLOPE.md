# P121 -- the white-light normal slope and the nuclear graph norm

## Status

This note proves an exact radial coordinate for the domain gap.  The dyadic
radical bootstrap constructed later in phase 121 proves the radical slope
bound at the end.  A further audit corrects the former last implication:
finite slope gives graph-domain membership, but v94 still requires annular
gap transport (358)/(441) to exclude the radical.  Thus the Abel-slope gate
is now closed, while the global square is not.

The construction is nonlinear in the source and is used only to test a
hypothetical first-loss vector.  It is not a Hilbert factorization of the
Weil form, a contraction, or a positive primitive descent.

## 1. Normalized radial energy

Use the unitary Fourier transform in the logarithmic variable.  For a
compact-window source `F`, extended by zero, and `epsilon>0`, define the
extended nonnegative quantity

\[
 \mathscr W_\varepsilon(F)
 :=\frac{1}{\zeta(1+2\varepsilon)}
   \int_{\mathbb R}
   \left|\zeta\left(\frac12+\varepsilon+i\tau\right)\right|^2
   |\widehat F(\tau)|^2\,d\tau .                    \tag{1.1}
\]

The value `+infinity` is allowed.  The normalization is the diagonal
coherent Euler mass.  Since

\[
 \frac1{\zeta(1+2\varepsilon)}
   =2\varepsilon+O(\varepsilon^2),                  \tag{1.2}
\]

the energy collapses to zero at the critical white-light wall on every
smooth source.  Its first normal slope need not collapse.

## 2. The normal-slope theorem

### Theorem 2.1 -- exact slope on the smooth primitive core

If `F in C_c^infinity(-T,T)`, then

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}
   \frac{\mathscr W_\varepsilon(F)}{2\varepsilon}
  =\int_{\mathbb R}
    |\zeta(1/2+i\tau)|^2|\widehat F(\tau)|^2\,d\tau .} \tag{2.1}
\]

Equivalently, after setting `W_0(F)=0`,

\[
 \mathscr W'_{0+}(F)
 =2\|\zeta(1/2+i\,\cdot)\widehat F\|_2^2.           \tag{2.2}
\]

#### Proof

On every fixed strip `1/2<=Re s<=1/2+epsilon_0`, zeta has an
unconditional polynomial vertical bound.  The Fourier transform of a
compactly supported smooth function is Schwartz.  Hence the integrand in
(1.1), without the scalar normalization, is dominated by one integrable
function uniformly for small `epsilon`.  Dominated convergence gives

\[
 \int |\zeta(1/2+\varepsilon+i\tau)|^2|\widehat F|^2
 \longrightarrow
 \int |\zeta(1/2+i\tau)|^2|\widehat F|^2.
\]

Divide (1.2) by `2 epsilon` and multiply the two limits.  This proves
(2.1)--(2.2).  QED.

The theorem identifies the missing graph seminorm without defining it as a
square root of row (d): it is a one-sided radial derivative of a
source-defined Euler energy.

## 3. A sufficient graph-domain criterion for rough sources

### Theorem 3.1 -- finite slope forces nuclear-domain membership

Let `F in L2(-T,T)`.  If

\[
 \liminf_{\varepsilon\downarrow0}
   \frac{\mathscr W_\varepsilon(F)}{2\varepsilon}<\infty, \tag{3.1}
\]

then

\[
 \zeta(1/2+i\tau)\widehat F(\tau)\in L^2(\mathbb R),       \tag{3.2}
\]

and

\[
 \|\zeta(1/2+i\,\cdot)\widehat F\|_2^2
 \leq
 \liminf_{\varepsilon\downarrow0}
   \frac{\mathscr W_\varepsilon(F)}{2\varepsilon}.        \tag{3.3}
\]

#### Proof

Choose a sequence realizing the finite liminf.  By (1.2), along that
sequence

\[
 \frac{\mathscr W_\varepsilon(F)}{2\varepsilon}
 =(1+o(1))\int
   |\zeta(1/2+\varepsilon+i\tau)|^2|\widehat F(\tau)|^2d\tau.
\]

For almost every real `tau`, continuity of zeta gives convergence of the
integrand to
`|zeta(1/2+i tau) Fhat(tau)|^2`.  Fatou's lemma proves (3.3), and finiteness
of its right side proves (3.2).  QED.

### Corollary 3.2 -- the precise first-loss target

Let `F_*` be the first-loss radical of phase 116.  The bound

\[
 \boxed{
 \mathscr W_\varepsilon(F_*)=O(\varepsilon)
 \quad(\varepsilon\downarrow0)}                            \tag{3.4}
\]

puts `F_*` in the maximal co-Poisson graph domain.  The phase-121 dyadic
bootstrap proves this bound.  Contrary to the first version of this note,
v94 does not say that graph membership alone rules out the state.  It still
asks for equality-state annular vanishing (358)/(441).

This is strictly weaker in quantifier than a uniform graph estimate on the
whole primitive space.  The modulated-test obstruction to the global bound
(434) does not by itself refute (3.4).

### Corollary 3.3 -- escape is infinite normal slope

If `F` is outside the maximal co-Poisson graph domain, then

\[
 \liminf_{\varepsilon\downarrow0}
 \frac{\mathscr W_\varepsilon(F)}{2\varepsilon}=+\infty.  \tag{3.5}
\]

This is the contrapositive of Theorem 3.1.  Thus the domain dichotomy is a
literal finite-slope/infinite-slope dichotomy.  No choice of an
approximating core sequence enters (3.5).

## 4. Exact arithmetic expansion in the safe Euler region

For `sigma>1`, put `epsilon=sigma-1/2` and define

\[
 (Z_\sigma F)(t)=\sum_{n\geq1}n^{-\sigma}F(t-\log n).       \tag{4.1}
\]

The series converges as a bounded Fourier multiplier and

\[
 \widehat {Z_\sigma F}(\tau)
 =\zeta(\sigma+i\tau)\widehat F(\tau).                     \tag{4.2}
\]

Let

\[
 C_F(u)=\langle F,S_uF\rangle.                              \tag{4.3}
\]

### Theorem 4.1 -- common-divisor removal

For `sigma>1`,

\[
 \boxed{
 \frac{\|Z_\sigma F\|_2^2}{\zeta(2\sigma)}
 =\sum_{\substack{a,b\geq1\\(a,b)=1}}
   \frac{C_F(\log(a/b))}{(ab)^\sigma}.}                    \tag{4.4}
\]

The left side is exactly `W_(sigma-1/2)(F)`.

#### Proof

Absolute convergence for `sigma>1` permits expansion and Plancherel:

\[
 \|Z_\sigma F\|_2^2
 =\sum_{m,n\geq1}(mn)^{-\sigma}C_F(\log(m/n)).              \tag{4.5}
\]

Write `m=da`, `n=db`, with `(a,b)=1`.  The correlation in (4.5) depends
only on `a/b`, while the common divisor contributes

\[
 \sum_{d\geq1}d^{-2\sigma}=\zeta(2\sigma).
\]

Dividing gives (4.4).  QED.

Formula (4.4) retains every cross-prime phase.  It also explains the
normalization in (1.1): `zeta(2 sigma)` is precisely the redundant common
divisor orbit, not a fitted scalar.

## 5. Exact centered Euler flow in the safe region

For `sigma>1`, define the bounded causal von Mangoldt multiplier

\[
 B_\sigma
 :=\sum_{n\geq2}\frac{\Lambda(n)}{n^\sigma}S_{\log n},
 \qquad
 c_\sigma:=-\frac{\zeta'}{\zeta}(2\sigma)>0.        \tag{5.1}
\]

### Theorem 5.1 -- source-specific radial flow

Let

\[
 h_\sigma=Z_\sigma F,
 \qquad
 \mathscr W(\sigma;F)=\frac{\|h_\sigma\|_2^2}{\zeta(2\sigma)}.
\]

Then

\[
 \boxed{
 \partial_\sigma\mathscr W(\sigma;F)
 =\frac{2}{\zeta(2\sigma)}
   \left\langle
    \bigl(c_\sigma I-\operatorname{Re}B_\sigma\bigr)h_\sigma,
    h_\sigma
   \right\rangle.}                                  \tag{5.2}
\]

#### Proof

Absolute convergence gives the multiplier identity

\[
 \partial_\sigma Z_\sigma=-B_\sigma Z_\sigma,       \tag{5.3}
\]

because `-zeta'/zeta` is the Dirichlet series of `Lambda`.  Hence

\[
 \partial_\sigma\|h_\sigma\|^2
 =-2\operatorname{Re}\langle B_\sigma h_\sigma,h_\sigma\rangle.
\]

Also

\[
 \partial_\sigma\log\zeta(2\sigma)
 =2\frac{\zeta'}\zeta(2\sigma)=-2c_\sigma.
\]

The quotient rule proves (5.2).  QED.

Equation (5.2) is signed; no monotonicity is claimed.  Its advantage is
typing.  The same normalized energy which has nuclear graph norm as its
critical slope has, in the Euler region, an exact flux containing every
`Lambda(n)n^(-sigma)` and the full observed vector `h_sigma`.  The scalar
size-bias identity of paper 36 contains the same logarithmic derivative,
and its channel formalism also has source-weighted quadratic data.  What is
not used there is (5.2) as a radical-only finite-slope criterion.  This is
the nearest semantic neighbour and must remain attached to every future use
of the flow.

## 6. Why this is not the coherent-root construction of phase 106

Phase 106 constructed the positive overlap

\[
 \frac{\zeta(2\sigma+i(u-t))}{\zeta(2\sigma)}
\]

of two source-independent coherent root states and proved its white-light
orthogonality at `sigma=1/2`.  Equations (1.1)--(4.4) instead evaluate the
norm of one compact-window physical source after the full zeta multiplier.
The new statement is (2.1): the first normal derivative of its collapsed
energy is the source-dependent nuclear graph norm.

The common denominator and the phrase "white light" are shared; the
derivative theorem and the radical-only finite-slope criterion are not the
positive root-module polarization or its forbidden Hilbert descent.

## 7. The pole crossing and the correct radial germ

Formula (4.4) is valid directly only for `sigma>1`.  Transporting its
Dirichlet series through `sigma=1` without modification is illegal: zeta
has a pole at `s=1`, and the physical co-Poisson sum acquires its continuum
tail.  This is the safe-region/boundary error which paper 36 repeatedly
exposed.

For a source with a defined value `Fhat(0)`, the pole can be shorted before
transport by the explicit germ

\[
 \mathcal R_\sigma F(\tau)
 :=\zeta(\sigma+i\tau)\widehat F(\tau)
   -\frac{\widehat F(0)}{\sigma-1+i\tau}.                   \tag{6.1}
\]

For each fixed radial line the pole is removed; on the smooth core the
remaining two-parameter germ is locally bounded in `L2_tau` across
`sigma=1`.  Pointwise joint removability is not asserted: the quotient
`(Fhat(tau)-Fhat(0))/(sigma-1+i tau)` can have path-dependent pointwise
limits, although its local `L2_tau` norm stays bounded.  Unlike a
logarithmic derivative, (6.1) does not acquire residues at zeros of zeta:
zeros are harmless for the zeta multiplier itself.  Thus (6.1) is the
correct pole-shorted object for any attempt to connect the safe expansion
(4.4) to the critical slope (2.1).

The subtraction changes the central graph norm by an explicit rank-one
pole term and its cross term.  Those terms must be retained; dropping them
would repeat the sign error and unpaired-divergence errors recorded in
paper 36.

## 8. The corona measure is only a projectivized tangent

For a smooth core approximant `F_j`, let `M_j` and `mu_j` be as in
`P121_RADICAL_DOMAIN_IDEAL_AND_CORONA.md`.  Theorem 2.1 gives

\[
 \mathscr W'_{0+}(F_j)=2M_j.                         \tag{8.1}
\]

More generally, insert any bounded continuous Euler-phase observable
`a((e^{-i tau log p})_p)` in the integral (1.1).  The same dominated
convergence proof shows that its normal derivative at zero, divided by
(8.1), is

\[
 \int a\,d\mu_j.                                    \tag{8.2}
\]

Thus `mu_j` is the **projectivized direction** of the radial tangent; it
forgets the tangent magnitude `M_j`.  In an escaping sequence that magnitude
diverges.  This proves internally, without invoking a comparison model, why
the weak-star corona measure alone cannot encode the finite-slope question.

## 9. The radical Abel-slope lemma

The fractional regularity theorem in
`P121_DYADIC_RADICAL_BOOTSTRAP.md` proves more than the finite-slope
hypothesis needed here.

### Theorem 9.1 -- exact radical Abel-slope lemma

Let `F_*` be a parity first-loss vector, let

\[
 h=\mathcal Z_{T_*,+}F_*,
\]

and assume the exact observed Gamma--Tate equation (445).  Then the
pole-shorted radial germ (6.1), with both functional-equation pole terms
kept in the completed coordinate, satisfies the exact asymptotic

\[
 \boxed{
 \mathscr W_\varepsilon(F_*)
 =2\varepsilon
   \|\zeta(1/2+i\,\cdot)\widehat F_*\|_2^2
   +o(\varepsilon).}                                      \tag{9.1}
\]

#### Proof

The dyadic radical bootstrap gives `F_* in H^s(R)` for every `s<1/2`.
Fix `s` with `1/4<s<1/2`, and choose `eta>0` with
`1/4+eta<s`.  Fix `0<epsilon_0<1/2`; the convexity estimate is uniform on
the pole-free compact strip `1/2<=Re z<=1/2+epsilon_0`:

\[
 |\zeta(1/2+\varepsilon+i\tau)|
 \le C_{\eta,\varepsilon_0}(1+|\tau|)^{1/4+\eta}.
\]

Consequently the integrands converge pointwise and are dominated by the
integrable function on the right:

\[
 |\zeta(1/2+\varepsilon+i\tau)|^2
 |\widehat F_*(\tau)|^2
 \le C(1+\tau^2)^s|\widehat F_*(\tau)|^2\in L^1.  \tag{9.2}
\]

Dominated convergence gives

\[
 \int |\zeta(1/2+\varepsilon+i\tau)|^2|\widehat F_*|^2d\tau
 \longrightarrow
 \|\zeta(1/2+i\,\cdot)\widehat F_*\|_2^2.           \tag{9.3}
\]

Since `1/zeta(1+2 epsilon)=2 epsilon+O(epsilon^2)`, equations
(9.2)--(9.3) prove (9.1).  QED.

### Corollary 9.2 -- zero-slope rigidity is exactly first-contact exclusion

For a first-loss radical the following are equivalent:

\[
\begin{array}{ll}
\text{(i)}&\mathscr W_\varepsilon(F_*)=o(\varepsilon),\\
\text{(ii)}&\zeta(1/2+i\tau)\widehat F_*(\tau)=0
             \quad\text{for a.e. }\tau,\\
\text{(iii)}&F_*=0.
\end{array}                                             \tag{9.4}
\]

#### Proof

Theorem 9.1 gives `(i) iff (ii)`.  The real zeros of zeta have measure
zero, so (ii) gives `Fhat_*=0` almost everywhere.  Fourier injectivity gives
(iii), and the reverse implications are immediate.  QED.

Thus the remaining Abel statement is no longer a finiteness or boundary
continuity problem.  It is the strict equality-state improvement

\[
 \boxed{
 P_TA_TF=0\quad\Longrightarrow\quad
 \mathscr W_\varepsilon(F)=o(\varepsilon).}         \tag{9.5}
\]

By (9.4), proving (9.5) is already first-contact exclusion.  It may not be
obtained merely by renaming the exact coefficient in (9.1).

### Corollary 9.3 -- the Abel coefficient sees the annular amplitude

Let `H=U mathfrak S_T^max F_*` be the global logarithmic co-Poisson
observation.  Its natural causal gap gives `H=0` on `(-infinity,-T)`, while
v94 (437) gives

\[
 H|_{I_T}=h=\mathcal Z_{T,+}F_* .                  \tag{9.6}
\]

Therefore

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}
 {\mathscr W_\varepsilon(F_*)\over\varepsilon}
 =2\|\zeta(1/2+i\,\cdot)\widehat F_*\|_2^2
 \ge4\pi\|h\|_{L^2(I_T)}^2.}                      \tag{9.7}
\]

In particular, on a first-loss state,

\[
 \mathscr W_\varepsilon(F_*)=o(\varepsilon)
 \Longleftrightarrow h=0
 \Longleftrightarrow F_*=0 .                       \tag{9.8}
\]

#### Proof

Equation (431) of v94 and unitarity of the logarithmic coordinate give

\[
 \|\zeta(1/2+i\,\cdot)\widehat F_*\|_2^2
 =2\pi\|H\|_2^2\ge2\pi\|h\|_{L^2(I_T)}^2.
\]

Combine this with Theorem 9.1.  If `h=0`, the finite nilpotent inverse v94
(439) gives `F_*=0`; the remaining implications are immediate.  QED.

Thus the exact Abel-slope lemma and maximal graph membership are proved.  They do
not by themselves exclude first loss: the remaining arrow is the annular
gap-transport theorem (358)/(441).

What has been gained is the proof of (9.1) and its radial type:

* it concerns one first-loss radical, not all sources;
* it is a finite boundary-slope estimate, not positivity of a boundary
  measure;
* it has the exact `|zeta|^2` scale missing from the Gamma-form equation;
* it retains cross-prime ratios through (4.4);
* it crosses `s=1` with an explicit pole shorting rather than an unnamed
  continuation;
* failure produces an infinite slope, the same corona defect already
  constructed in phase 121.

The global square may be promoted only after equality-state annular
transport is proved; finite Abel slope is no longer the missing theorem.
