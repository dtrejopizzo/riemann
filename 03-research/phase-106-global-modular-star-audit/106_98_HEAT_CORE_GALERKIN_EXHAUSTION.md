# 106.98 — Heat-core Galerkin exhaustion

## Purpose and conclusion

The cofinal inertia route requires a nested finite-dimensional form-core
exhaustion of the complete mean-periodic complement.  The canonical choice
made from zero orbits remains subject to the weighted spectral-synthesis
gate isolated in `106_70_WEIGHTED_MEAN_PERIODIC_SPECTRAL_SYNTHESIS.md`.
That gate is unnecessary for the closure theorem: the closure uses a form
core, not a prescribed basis.

This note constructs an unconditional heat-regularized Galerkin core.  It
proves four statements.

1. The complete positive prime--Gamma form is densely defined and closed;
   its restriction to the closed radical complement has a positive self-adjoint
   operator
   \[
   S=T_F+1\ge \frac12 I.
   \]
2. If `(g_j)` is any Hilbert-dense sequence in that complement, then
   \[
   \mathcal V_M^{\mathrm{heat}}
   =\mathrm{span}\,\{e^{-S/k}g_j:1\le j,k\le M\}
   \]
   is a nested form-core exhaustion.
3. On each fixed heat space, the omitted ordinary-prime bank tends to zero
   uniformly in normalized operator norm.  No zero-mode theta asymptotic is
   needed.
4. A block containing two distinct omitted primes has strictly positive
   Gram matrix on every finite centered heat-plus-radical space.  Therefore
   the radical short and the basis-free finite Gram, Schur, inertia, and
   bordered-determinant algebra remain well defined.  Estimates tied to a
   single prime channel do not transfer automatically.

Consequently the form-core hypothesis in the cofinal closure theorem can
be discharged by choosing the heat Galerkin exhaustion.  This result does
**not** prove the physical surplus.  If RH is false, the same heat core
approximates the negative mean-periodic state in form norm.  The theorem
removes a domain/exhaustion gap and leaves the signed surplus as the sole
force-bearing inequality.

## 1. Unconditional operator setup

Put

\[
 \mathscr H=L^2_{\mathrm{even}}(\mu_K),
 \qquad
 d\mu_K(x)=\frac{h(x)K(x)}{c_K}\,dx,
 \qquad h(x)=\cosh(x/2),\qquad c_K=\frac12,
\]

where `K` is strictly positive and smooth.  For `u > 0` define

\[
 \mathcal J_u(q,s)
 =\int_{\mathbb R}K(x)K(x-u)
   \overline{q(x)-q(x-u)}\{s(x)-s(x-u)\}\,dx,     \tag{C1}
\]

and put

\[
 g(u)=\frac{e^{-u/2}}{1-e^{-2u}},
 \qquad
 \mathscr E_\Gamma(q,s)
 =\int_0^\infty g(u)\mathcal J_u(q,s)\,du.        \tag{C2}
\]

The complete ordinary-prime--Gamma form is

\[
 \mathscr E_K(q,s)
 =\mathscr E_\Gamma(q,s)
 +\sum_{n=p^a\ge2}\frac{\Lambda(n)}{\sqrt n}
       \mathcal J_{\log n}(q,s).                  \tag{1}
\]

### Lemma 1 — The complete source form is closed

The form `E_K` is nonnegative, densely defined, and closed.  Consequently
there is a unique nonnegative self-adjoint operator `L` such that

\[
 D(\mathscr E_K)=D(L^{1/2}),\qquad
 \mathscr E_K(q,s)=\langle L^{1/2}q,L^{1/2}s\rangle_{\mu_K}.
                                                               \tag{2}
\]

#### Proof

For `u > 0` set

\[
 (D_uq)(x)
 =\sqrt{K(x)K(x-u)}\{q(x)-q(x-u)\}.              \tag{C3}
\]

Introduce the Hilbert space

\[
 \mathscr Y=
 L^2((0,\infty)\times\mathbb R,g(u)\,du\,dx)
 \oplus
 \bigoplus_{n=p^a\ge2}L^2(\mathbb R,dx)          \tag{C4}
\]

and the maximal difference operator

\[
 \mathcal Dq
 =\left((u,x)\mapsto D_uq(x),
 \left(\sqrt{\frac{\Lambda(n)}{\sqrt n}}
            D_{\log n}q\right)_{n=p^a}\right).  \tag{C5}
\]

Its maximal domain is

\[
 D(\mathcal D)
 :=\{q\in\mathscr H:\text{the vector in (C5) belongs to }\mathscr Y\}.
                                                               \tag{C5a}
\]

This operator is closed.  Indeed, suppose that `q_j -> q` in `H` and
`D q_j -> Y` in `Y`.  Because the density of `mu_K` is strictly positive,
a subsequence converges to `q` almost everywhere for Lebesgue measure.
The translated subsequence converges at `x-u` for almost every `(u,x)`;
this follows from Fubini after the change of variables `(u,x) -> (u,x-u)`.
Hence the Gamma coordinate in (C5) converges pointwise almost everywhere to
`D_u q(x)`.  The same statement holds in every discrete prime-power
coordinate.  Realize `Y` as `L^2` over the countable disjoint union of its
sigma-finite coordinate spaces.  Taking one further almost-everywhere
convergent subsequence of the assumed `Y`-norm convergence then identifies
simultaneously every coordinate of `Y` with the corresponding coordinate
of `Dq`.  Thus (qin D(\mathcal D)) and \(\mathcal Dq=Y\).

The maximal domain is dense.  In fact, the even part of
`C_c^infty(R)` is contained in it.
For `0<u<1`, the mean-value theorem and

\[
 g(u)=\frac1{2u}+O(1)                              \tag{C6}
\]

make the Gamma integrand `O(u)`.  For large `u`, compact support together
with the theta bound

\[
 K(x)\le A\exp(-a e^{2|x|})                       \tag{C7}
\]

gives, when `supp(q) subset [-R,R]`,

\[
 \mathcal J_u(q,q)
 \le C_{q,R}\exp\{-a_{q,R}e^{2(u-R)}\},
 \qquad u\ge2R+1.                                 \tag{C7a}
\]

This is Gamma-integrable and, at `u=log n`, gives

\[
 \sum_{n=p^a}\frac{\Lambda(n)}{\sqrt n}
 \mathcal J_{\log n}(q,q)
 \le C_{q,R}\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}e^{-a'_{q,R}n^2}
 <\infty.                                         \tag{C7b}
\]

Finally, `C^infty_{c,even}(R)` is dense in
`L^2_even(mu_K)` because `mu_K` has a positive locally bounded density.

Finally,

\[
 \mathscr E_K(q,q)=\|\mathcal Dq\|_{\mathscr Y}^2. \tag{C8}
\]

The graph norm of the closed operator `D` is therefore exactly
`(\|q\|^2+E_K(q,q))^{1/2}`.  This proves closedness and density of the
form.  The representation theorem for closed nonnegative forms yields
`L` and (2).  \(\square\)

Let `R` be the closed span of the centered complete Riemann-radical
vectors and put

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp.    \tag{3}
\]

The strong operator-domain identities proved in 106.41(10),

\[
 \mathbf1\in D(L),\qquad
 L\mathbf1=0,
 \qquad
 r_j-\mu_K(r_j)\in D(L),\qquad
 L\{r_j-\mu_K(r_j)\}
 =\frac12\{r_j-\mu_K(r_j)\}                      \tag{4}
\]

show that `1 direct-sum R` and `C` are reducing subspaces for `L`.  The
membership assertions in (4) are essential: Hilbert density of smooth
tests alone would not promote a merely formal weak identity to a reducing
eigenspace.  Here (4) is imported as the already established strong
identity obtained from the absolutely convergent full-generator formula.
Multiplication by

\[
 h(x)=\cosh(x/2),
 \qquad
 d\omega_K(x)=\frac{K(x)}{c_Kh(x)}\,dx
\]

defines the unitary map

\[
 W:\mathscr H\longrightarrow L^2_{\mathrm{even}}(\omega_K),
 \qquad Wq=hq.                                    \tag{5}
\]

The closed Hilbert realization of the mean-periodic complement is

\[
 \mathcal N_K:=W\mathscr C.                       \tag{6}
\]

On the analytic domain this is exactly the equation `F*K=0`, as proved in
106.43 and 106.64.  Definition (6), rather than an unsupported closedness
claim for convolution in the weighted topology, is used below.

Define

\[
 T_F=W(L-\tfrac12)W^{-1}\big|_{\mathcal N_K},
 \qquad
 S=T_F+1=W(L+\tfrac12)W^{-1}\big|_{\mathcal N_K}. \tag{7}
\]

### Proposition 2 — Closed positive form on the complement

The operator `S` is self-adjoint on `N_K` and satisfies

\[
 \boxed{S\ge\frac12 I.}                           \tag{8}
\]

Its closed form is

\[
 \mathfrak s(F,G)
 :=\langle S^{1/2}F,S^{1/2}G\rangle_{\omega_K}
 =\frac12\langle F,G\rangle_{\omega_K}
 +\mathscr E_K(F/h,G/h),                         \tag{9}
\]

on the exact domain

\[
 D(\mathfrak s)=W\{\mathscr C\cap D(L^{1/2})\}.  \tag{9a}
\]

with form norm

\[
 \|F\|_{\mathfrak s}:=\|S^{1/2}F\|_{\omega_K}.  \tag{10}
\]

Moreover, `N_K` is separable.

#### Proof

The nonnegative self-adjoint operator `L` reduces `C` by (4).  Indeed, the
closed span `R` lies in the `1/2` eigenspace, while the constants lie in
the zero eigenspace.  The orthogonal projection onto a closed subspace of
an eigenspace commutes with a self-adjoint operator.  Its
restriction to `C` is therefore self-adjoint and nonnegative.  Unitary
conjugation by `W`, followed by addition of `1/2`, proves self-adjointness
and (8).  The representation theorem for nonnegative self-adjoint
operators gives the closed form (9).  Finally, weighted `L^2` is separable
and `N_K=W C` is a closed subspace, hence is separable.  No zero-location
statement occurs in this argument.  \(\square\)

## 2. The abstract heat-core theorem

We first isolate the functional-analytic statement independently of the
Riemann realization.

### Theorem 3 — Heat regularization produces a form core

Let `H` be a separable Hilbert space and let `S` be self-adjoint with
`S >= cI` for some `c > 0`.  Let `(g_j)` be a sequence whose algebraic
span is dense in `H`, and define

\[
 V_M=\mathrm{span}
 \{e^{-S/k}g_j:1\le j,k\le M\}.                   \tag{11}
\]

Then

\[
 V_M\subset V_{M+1}\subset\bigcap_{m\in\mathbb N_0}D(S^m). \tag{12}
\]

and

\[
 \boxed{
 \overline{\bigcup_{M\ge1}V_M}^{\,\|S^{1/2}\cdot\|}
 =D(S^{1/2}).}                                    \tag{13}
\]

#### Proof

For `t > 0` and every integer `m >= 0`, the spectral calculus gives

\[
 \|S^me^{-tS}\|
 \le\sup_{\lambda\ge0}\lambda^me^{-t\lambda}
 \le\left(\frac{m}{et}\right)^m,                \tag{14}
\]

with the usual value `1` when `m=0`.  Thus every vector in (11) lies in
every power domain and (12) follows.

Let `F` belong to `D(S^{1/2})`.  Its spectral measure gives

\[
 \begin{aligned}
 \|S^{1/2}(e^{-tS}-I)F\|^2
 &=\int_{[c,\infty)}
   \lambda|e^{-t\lambda}-1|^2\,d\mu_F(\lambda)\\
 &\longrightarrow0
 \qquad(t\downarrow0),                           \tag{15}
 \end{aligned}
\]

by dominated convergence, since the integrand is bounded by `lambda` and
`F` lies in the form domain.

Fix `epsilon > 0`.  Choose an integer `k` so large that, for `t=1/k`,

\[
 \|S^{1/2}(e^{-tS}-I)F\|<\frac\epsilon2.          \tag{16}
\]

The elementary spectral bound

\[
 \boxed{
 \|S^{1/2}e^{-tS}\|
 \le(2et)^{-1/2}}                                 \tag{17}
\]

follows by maximizing `sqrt(lambda) exp(-t lambda)` on the positive
half-line.  Since the span of `(g_j)` is dense, choose
`g in span{g_1,...,g_m}` such that

\[
 \|F-g\|<\frac\epsilon2\sqrt{2et}.                \tag{18}
\]

Then `e^{-tS}g` belongs to `V_M` for
`M >= max(k,m)`, and

\[
 \begin{aligned}
 \|S^{1/2}(F-e^{-tS}g)\|
 &\le\|S^{1/2}(F-e^{-tS}F)\|\\
 &\quad+\|S^{1/2}e^{-tS}(F-g)\|\\
 &<\epsilon.                                      \tag{19}
 \end{aligned}
\]

This proves (13).  Since `S >= cI`,

\[
 \|S^{1/2}F\|
 \le(\|F\|^2+\|S^{1/2}F\|^2)^{1/2}
 \le\sqrt{1+c^{-1}}\|S^{1/2}F\|,                \tag{19a}
\]

so the homogeneous norm used in (13) is equivalent to the usual form
graph norm `(\|F\|^2+\|S^{1/2}F\|^2)^{1/2}` and is complete.
\(\square\)

### Remark 4 — Why this is not an RH input

The theorem regularizes with `S=T_F+1`, not with `T_F`.  Since

\[
 S=W(L+\tfrac12)W^{-1}\ge\tfrac12 I,              \tag{20}
\]

its positivity is the unconditional positivity of the complete
prime--Gamma Dirichlet generator `L`.  It does not assert `T_F >= 0`.
If `T_F` has a negative eigenvector, the heat core approximates that vector
in form norm by (13).

## 3. Heat Galerkin spaces for the Riemann complement

Choose a Hilbert-dense sequence `(g_j)` in `N_K` and put

\[
 \mathcal V_M^{\mathrm{heat}}
 =\mathrm{span}
 \{e^{-S/k}g_j:1\le j,k\le M\},                  \tag{21}
\]

\[
 E_M^{\mathrm{heat}}=W^{-1}\mathcal V_M^{\mathrm{heat}}
 \subset\mathscr C.                               \tag{22}
\]

### Corollary 5 — Unconditional prime--Gamma form core

The spaces in (22) are nested finite-dimensional subspaces of the
centered radical complement and satisfy

\[
 \boxed{
 \overline{\bigcup_ME_M^{\mathrm{heat}}}^{\,
  (\frac12\|\cdot\|_{\mu_K}^2+\mathscr E_K)^{1/2}}
 =\mathscr C\cap D(L^{1/2}).}                    \tag{23}
\]

#### Proof

Apply Theorem 3 to the operator in (7) and conjugate (13) by `W`.
Identity (9) converts its form norm exactly into the norm in (23).
\(\square\)

The canonical zero modes may be adjoined to every space in (22) without
affecting (23).  What is not asserted is that the zero modes alone form a
core; that stronger statement remains the separate weighted synthesis
problem of 106.70.

More explicitly, if `Z_M` is any nested finite span of zero modes and
multiplicity jets, then

\[
 E_M^{\mathrm{hyb}}=E_M^{\mathrm{heat}}+Z_M       \tag{23a}
\]

is also a form-core exhaustion.  This hybrid version retains the explicit
off-line-orbit test vectors without claiming that heat flow can repair a
failure of zero-mode synthesis.  Indeed, if `S=I` and the zero modes span a
proper closed subspace `Z`, then `e^{-tS}Z=Z`; heating that subspace alone
does not make it dense.

## 4. Uniform Euler-tail convergence on every heat space

For `X >= 2`, let

\[
 \mathcal T_X(q,s)
 =\sum_{\substack{n=p^a>X}}
   \frac{\Lambda(n)}{\sqrt n}\mathcal J_{\log n}(q,s).
                                                               \tag{24}
\]

The sum is a nonnegative tail of (1).  Hence, for every
`q in D(L^{1/2})`,

\[
 0\le\mathcal T_X(q,q)\downarrow0
 \qquad(X\to\infty).                              \tag{25}
\]

### Theorem 6 — Fixed-space operator-norm tail convergence

Let `E` be any finite-dimensional subspace of `D(L^{1/2})`, let
`N_E` be its Hilbert norm Gram matrix in an arbitrary basis, and let
`T_{E,X}` be the matrix of (24).  Then

\[
 \boxed{
 \|N_E^{-1/2}T_{E,X}N_E^{-1/2}\|\longrightarrow0.} \tag{26}
\]

The same conclusion holds on

\[
 E_M^{\mathrm{heat}}\oplus\mathfrak R_J           \tag{27}
\]

for every fixed pair `(M,J)`.

#### Proof

Choose a basis `e_1,...,e_d` of `E`.  Equation (25) gives

\[
 \mathcal T_X(e_i,e_i)\longrightarrow0.           \tag{28}
\]

The Cauchy--Schwarz inequality for the positive form `T_X` gives

\[
 |\mathcal T_X(e_i,e_j)|^2
 \le\mathcal T_X(e_i,e_i)\mathcal T_X(e_j,e_j)
 \longrightarrow0.                               \tag{29}
\]

Thus every entry of the finite matrix `T_{E,X}` tends to zero, hence so
does its operator norm.  Conjugation by the fixed invertible matrix
`N_E^{-1/2}` proves (26).  The finite exact radical vectors belong to the
operator domain by the eigenidentity (4), so the same proof applies to
(27).  \(\square\)

### Corollary 7 — Cofinal cutoff schedule without an explicit rate

For arbitrary finite dimensions `M,J` and arbitrary `epsilon > 0`, there
is a finite `X(M,J,epsilon)` such that

\[
 0\preceq
 N_{M,J}^{-1/2}T_{M,J,X}N_{M,J}^{-1/2}
 \preceq\epsilon I.                               \tag{30}
\]

Consequently, for any schedules `M -> infinity`, `J(M) -> infinity`, and
`epsilon_M downarrow 0`, one may choose an increasing cutoff schedule
`X(M) -> infinity` satisfying (30) row by row.

#### Proof

The first statement is Theorem 6.  Choose each cutoff after the finite
pair `(M,J(M))` is fixed, and enlarge it recursively to obtain an
increasing schedule.  Increasing `X` can only decrease the positive tail.
\(\square\)

This replaces the canonical zero-mode rate `C_M exp(-cX)` by a qualitative
row-wise modulus tending to zero.  The compensated cofinal closure uses
only the latter property.

## 5. Two-prime strict observability

For `u > 0`, recall

\[
 \mathcal J_u(q,q)
 =\int_{\mathbb R}K(x)K(x-u)
  |q(x)-q(x-u)|^2\,dx.                            \tag{31}
\]

The Riemann theta kernel satisfies `K(x) > 0` on the real line.

### Lemma 8 — Two incommensurable shifts have only the constant kernel

Let `a,b > 0` with `a/b` irrational.  If a locally square-integrable
function `q` satisfies

\[
 \mathcal J_a(q,q)=\mathcal J_b(q,q)=0,           \tag{32}
\]

then `q` is constant almost everywhere.

#### Proof

Positivity of `K` turns (32) into

\[
 q(\cdot-a)=q=q(\cdot-b)\quad\text{a.e.}          \tag{33}
\]

Thus every element of the dense additive subgroup

\[
 G=\{ma+nb:m,n\in\mathbb Z\}                    \tag{34}
\]

is an almost-everywhere period.  Translations are strongly continuous in
`L^2_loc`.  Approximating an arbitrary real `t` by elements of `G` shows
that every real number is a period in `L^2_loc`.  Convolution with a
compactly supported smooth approximate identity produces continuous
functions invariant under every real translation, hence constants.
Passing to the approximate-identity limit proves that `q` is constant
almost everywhere.  \(\square\)

### Theorem 9 — Strict finite block Gram

Let (E\subset\mathscr C\cap D(L^{1/2})) be finite dimensional, and let
\(\mathfrak R_J\subset\mathcal R\cap\mathcal H_0\) be a finite exact-radical
space.  Thus (E\cap\mathfrak R_J=\{0\}), and every vector of
\(E\oplus\mathfrak R_J\) is centered.  For every cutoff (X), choose two
distinct primes (p,r>X).  Then

\[
 \boxed{
 \frac{\log p}{\sqrt p}\mathcal J_{\log p}
 +\frac{\log r}{\sqrt r}\mathcal J_{\log r}
 \succ0
 \quad\text{on }E\oplus\mathfrak R_J.}           \tag{35}
\]

#### Proof

If the form in (35) vanishes, positivity of its two coefficients implies
that both displacement energies vanish.  Unique factorization gives

\[
 \frac{\log p}{\log r}\notin\mathbb Q;            \tag{36}
\]

otherwise `p^a=r^b` for nonzero integers `a,b`.  Lemma 8 makes the vector
constant almost everywhere.  Every vector of
`E direct-sum R_J` is centered, so that constant is zero.  The Gram form
has trivial kernel on a finite-dimensional space and is therefore
positive definite.  \(\square\)

### Corollary 10 — Strict radical short and finite determinants

On every fixed heat row `(M,J,X)`, any finite omitted block that contains
two distinct primes larger than `X` has a positive-definite Gram matrix on

\[
 E_M^{\mathrm{heat}}\oplus\mathfrak R_J.          \tag{37}
\]

Its radical block and its Schur short to `E_M^heat` are positive definite.
Every principal denominator and augmented bordered determinant used in
the radical-conditioned gain and Krylov hierarchy is therefore well
defined after such a finite extension.

#### Proof

The complete block dominates the two-prime form (35), so it is positive
definite.  Congruence by block Gaussian elimination writes its inertia as
the sum of the inertia of the radical block and its Schur short.  Both are
therefore positive definite.  The determinant and bordered-determinant
claims are the standard Gram and Schur formulas.  \(\square\)

## 6. Exact scope of the finite-dimensional transfer

The Haynsworth inertia identity, the maximal radical anti-short, and the
cofinal compensated-inertia criterion of 106.72 are basis-free
finite-dimensional statements.  They require:

1. a nested finite-dimensional subspace of the form domain contained in
   the closed radical complement;
2. convergence of the omitted positive bank on each fixed row;
3. strict positivity of a sufficiently large finite omitted block;
4. the exact radical identities
   \(\mathcal A_\infty(r,f)=0\) and
   \(E_M^{\mathrm{heat}}\cap\mathfrak R_J=\{0\}\).

Corollary 5, Theorem 6, and Corollary 10 supply these three inputs for the
heat spaces.  Hence the Gram, Schur-complement, Haynsworth-inertia, and
cofinal compensated-closure algebra of 106.72 transfers exactly.  Once a
finite two-prime block has been chosen, its ordinary bordered determinants
and block Krylov spaces are also well defined.

This does **not** make every local statement of 106.89--106.97 valid
verbatim.  The following canonical-mode refinements are not inherited:

- the explicit superexponential rate `C_M exp(-cX)`;
- strict observability of one individual prime channel through the
  exponential-polynomial zero-mode formula;
- local one-channel Christoffel detection and scalar rank-one update
  estimates;
- the large-prime asymptotic specific to an elementary mode `chi_z`.

The first two required structural inputs are replaced respectively by
Theorem 6 and the two-prime block of Theorem 9.  Any later quantitative
surplus theorem must nevertheless be restated and proved either for the
heat Galerkin rows or for the hybrid exhaustion (23a).  Proving it only on
the possibly non-exhaustive canonical zero-mode span would not close the
global argument.

## 7. Closure consequence and exact remaining theorem

### Theorem 11 — Form-core hypothesis removed

In the cofinal compensated-inertia theorem of 106.72 and Paper 40, choose
the spaces `V_M` to be `E_M^heat`.  Then the form-core assumption and the
fixed-row tail-convergence assumption are theorems, not hypotheses.

If there exist schedules

\[
 M\longmapsto(J(M),\widehat X(M),\varepsilon_M),
 \qquad
 J(M),\widehat X(M)\to\infty,
 \qquad
 \varepsilon_M\downarrow0                        \tag{38}
\]

for which the joint prime--Gamma matrices satisfy

\[
 \boxed{
 n_-\!\left[
  \mathbf A_{M,J(M),\widehat X(M)}
  +\varepsilon_M
   \begin{pmatrix}\mathbf N_M&0\\0&0\end{pmatrix}
 \right]=J(M),}                                   \tag{39}
\]

then the complete centered, equivalently constant-quotiented, Weil form is
nonnegative and RH follows.

#### Proof

Corollary 5 supplies the form-core hypothesis.  We first synchronize the
inertia cutoff with the cutoff supplied by Corollary 7.  If (39) initially
holds at \(\widehat X_M\), choose

\[
 X_M\ge\max\{\widehat X_M,
 X_{\mathrm{tail}}(M,J(M),\varepsilon_M)\}.       \tag{39a}
\]

The finite head increases in Loewner order when the cutoff increases, so
its negative index cannot increase.  It also cannot fall below `J(M)`:
on every nonzero `r in R_{J(M)}` the shifted form is

\[
 \mathcal A_{X_M}(r,r)
 =-\mathcal T_{X_M}(r,r)<0,                       \tag{39b}
\]

because the remaining tail contains two distinct primes and Theorem 9
applies.  Thus (39) persists at the synchronized cutoff (39a).

The finite Haynsworth equivalence now converts (39) into a lower bound for
the anti-short; adding back its nonnegative tail short gives

\[
 \mathcal A_\infty(q,q)
 \ge-\varepsilon_M\|q\|_{\mu_K}^2
 \qquad(q\in E_M^{\mathrm{heat}}).                \tag{40}
\]

Fix `M_0` and `q in E_{M_0}^heat`.  Nestedness permits (40) to be applied
for every `M >= M_0`; letting `M -> infinity` gives
\(\mathcal A_\infty(q,q)\ge0\).  For a general centered vector in the
complement form domain, use (23).  The form

\[
 \mathcal A_\infty(q,s)
 =\mathscr E_K(q,s)-\frac12\langle q,s\rangle_{\mu_K}
\]

is continuous in the norm of (23), so its nonnegativity passes to the
limit.  On the whole space the corresponding expression is

\[
 \mathscr E_K(q,q)-\frac12\mathrm{Var}_{\mu_K}(q),
                                                               \tag{40a}
\]

not `E_K(q,q)-\|q\|^2/2`; constants have value zero in (40a).  The exact
radical also has value zero.  Thus the centered/constant-quotiented Weil
form is nonnegative;
Weil's criterion gives RH.  \(\square\)

The only force-bearing input left in (39) is the joint physical surplus,
equivalently the compensated bordered-minor/Krylov inequality.  The heat
construction does not supply that sign and does not hide it in a density
assumption.

## 8. Circularity and falsification audit

The construction passes the following checks.

1. **No RH sign.**  It uses `S=T_F+1=L+1/2`, which is positive whether or
   not `T_F` has negative spectrum.
2. **Off-line test.**  If an off-line zero creates a negative form-domain
   vector, Theorem 3 approximates it.  The heat core therefore does not
   delete the counterexample.
3. **No weighted translation step.**  The proof never asserts that a
   nonzero translation is bounded on `L^2(omega_K)`; 106.70 proves it is
   not.
4. **No zero-mode synthesis.**  Neither the division identity
   `D_Xi=R_W` nor the deficiency-space condition of 106.70 is used.
5. **No hidden convolution regularity.**  Generic heat vectors are
   analytic for `S`, not necessarily analytic under spatial translation.
   The proof uses the closed space `N_K=W C`; it invokes `F*K=0` only on
   the previously established analytic domain.
6. **Literal arithmetic.**  Tail monotonicity and strict observability use
   the actual positive coefficients `Lambda(p^a)=log p` and the actual
   shifts `log p^a`.
7. **Finite determinant integrity.**  A single channel is not assumed
   injective on an arbitrary heat space; two distinct prime channels are
   used, which is the sharp basis-free replacement.

## Verdict

The heat Galerkin spaces give an unconditional, nested form-core
exhaustion of the complete mean-periodic complement and preserve the
cofinal finite determinant mechanism.  The canonical zero-orbit-only
form-core problem remains open but is no longer required.  After this
replacement, the remaining theorem in the branch-selection route is the
joint physical surplus (or its compensated version) on the heat-core
rows.
