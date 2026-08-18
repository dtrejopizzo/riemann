# 106.113 — Infinite Hodge boundary-flux rigidity

## 1. Purpose and verdict

Document 106.111 excludes every **finite-local** Hodge completion which is
sharp on the complete Riemann radical.  There is one apparent way around a
finite incidence theorem: use an infinite divergence-free current whose
only nonzero action is a flux through the boundary at infinity.

That possibility does not exist in the physical source Hilbert space.  The
ordinary von Mangoldt weights and the theta decay imply that the
conductance of a spatial cut tends to zero superexponentially.  Hence every
square-integrable source current has zero flux at the end of the folded
half-line.  More
intrinsically, the compact smooth multipliers are a form core for the full
prime--Gamma difference form.  A bounded current which is divergence free
on compact tests is therefore orthogonal to **every** form-domain gradient,
including every heat and hybrid row.

There is also an infinite Hodge statement.  Every such current is the
Hilbert limit of circulations on finite quotient incidence graphs.  Thus
the infinite source has no additional bounded boundary-homology sector:
the only bounded divergence-free sector is the closure of finite cycles.

Consequently an infinite Hodge flow cannot supply the polar channel.  A
nonzero boundary realization would have to leave the source Hilbert space.
Quantitatively, a current carrying a fixed flux through a cut at distance
\(R\) must have squared source norm at least

\[
 \exp\{c e^{R}\}.
\]

Such an object is not a bounded Hilbert row.  Nor can it define a closable
boundary operator whose domain contains the physical gradient core and
whose adjoint rows satisfy the local incidence equation.  It therefore
cannot prove the heat-row contraction.  The globally nonlocal contraction
after radical anti-shorting remains the force-bearing step.

No zero-location statement is used.

## 2. The literal source network

It is enough to use the unmarked edge realization.  The marked theta,
divisor-current and residue-character realizations of 106.65, 106.104 and
106.108 are isometric refinements of the same source norm.

Put

\[
 a_n=\frac{\Lambda(n)}{\sqrt n},
 \qquad
 g(u)=\frac{e^{-u/2}}{1-e^{-2u}},
 \tag{1}
\]

where \(u>0\).  Since the physical multipliers are even, use the folded
endpoints

\[
 s(u,x)=\min\{|x-u|,|x|\},
 \qquad
 t(u,x)=\max\{|x-u|,|x|\}
 \tag{1a}
\]

in \([0,\infty)\), oriented from \(s\) to \(t\).  The Gamma and
ordinary-prime conductance measures before this endpoint pushforward are

\[
\begin{aligned}
 d\Omega_\Gamma(u,x)
   &=g(u)K(x)K(x-u)\,du\,dx,\\
 d\Omega_p(n,x)
   &=a_nK(x)K(x-\log n)\,dx,
   \qquad n=p^k\ge2.
\end{aligned}
\tag{2}
\]

Let

\[
 \mathscr H_{\rm src}
 =L^2(\Omega_\Gamma)\oplus
   \bigoplus_{n=p^k}L^2(\Omega_p(n))
 \tag{3}
\]

and define the closed gradient

\[
 (\mathcal Gr)(u,x)=r(t(u,x))-r(s(u,x)).
 \tag{4}
\]

Thus

\[
 \|\mathcal Gr\|_{\rm src}^2=\mathscr E_K(r).
 \tag{5}
\]

Summing the latent theta marks in 106.65 gives exactly (2).  In particular,
all estimates below retain every theta atom and every literal weight
\(\Lambda(p^k)\); no PNT replacement is made.

For a current \(F=(F_\Gamma,F_p)\in\mathscr H_{\rm src}\), define local
divergence freeness by

\[
 \langle F,\mathcal G\varphi\rangle_{\rm src}=0
 \qquad
 \bigl(\varphi\in C_{c,\mathrm{even}}^\infty(\mathbb R)\bigr).
 \tag{6}
\]

This is the weak incidence equation.  It allows cancellation between the
Gamma channel, different prime powers and all theta fibres before any
absolute value is taken.

## 3. Vanishing conductance at spatial infinity

For \(R>0\), let

\[
 H_R=[0,R],
 \qquad \chi_R=\mathbf1_{H_R}
 \quad\text{on the folded half-line},
 \qquad
 \mathfrak c(R)=\|\mathcal G\chi_R\|_{\rm src}^2.
 \tag{7}
\]

The indicator belongs to the extended form domain.  Indeed, in the Gamma
channel only edges crossing \(R\) occur; their spatial interval has length
\(u\), which cancels the singularity \(g(u)\sim(2u)^{-1}\).

Use the theta bounds already proved in 106.67,

\[
 K(x)\le A e^{-a e^{2|x|}},
 \qquad
 Z(u):=\int_{\mathbb R}K(x)K(x-u)\,dx
       \le A e^{-a e^u}\quad(u\ge1).
 \tag{8}
\]

### Lemma 1 — Cut conductance tends to zero

There are constants \(A_0,a_0>0\) such that

\[
 \boxed{
 \mathfrak c(R)\le A_0\exp\{-a_0e^{R}\}
 \qquad(R\ge2).}
 \tag{9}
\]

#### Proof

In the unfolded coordinate, a folded edge crosses \(H_R\) only if it
crosses one of the two cuts at \(R\) and \(-R\).  Those two contributions
are equal by evenness.  For the positive cut put

\[
 I_R(u)=\int_R^{R+u}K(x)K(x-u)\,dx.
 \tag{10}
\]

For \(0<u\le1\),

\[
 I_R(u)\le
 \min\left\{uK(0)^2,
             K(0)\int_R^\infty K(x)\,dx\right\}.
 \tag{11}
\]

Since \(g(u)=1/(2u)+O(1)\), integration of (11) is bounded by a constant
times

\[
 T_R\{1+|\log T_R|\},
 \qquad T_R=\int_R^\infty K(x)\,dx,
 \tag{12}
\]

which is \(O(e^{-a'e^{2R}})\) after decreasing \(a'\).  For
\(1<u\le R\), use \(I_R(u)\le K(0)T_R\) and the integrability of \(g\)
on \([1,\infty)\).  For \(u>R\), use \(I_R(u)\le Z(u)\) and (8).  These
three ranges give

\[
 \|\mathcal G\chi_R\|_\Gamma^2
 \le A'e^{-a'e^R}.
 \tag{13}
\]

For a prime-power displacement \(u=\log n\), the crossing integral is

\[
 I_R(\log n)
 =\int_R^{R+\log n}K(x)K(x-\log n)\,dx.
 \tag{14}
\]

If \(n\le e^R\), (14) is at most \(K(0)T_R\).  The elementary bound
\(\Lambda(n)\le\log n\) gives

\[
 \sum_{n\le e^R}\frac{\Lambda(n)}{\sqrt n}
 \le CRe^{R/2}.
 \tag{15}
\]

If \(n>e^R\), (8) gives \(I_R(\log n)\le Ae^{-an}\).  Therefore

\[
\begin{aligned}
 \|\mathcal G\chi_R\|_p^2
 &\le CK(0)T_RRe^{R/2}
   +A\sum_{n>e^R}\frac{\log n}{\sqrt n}e^{-an}\\
 &\le A'e^{-a'e^R}.
\end{aligned}
\tag{16}
\]

Equations (13)--(16), with the harmless factor two for the two unfolded
cuts, prove (9).  In the marked theta realization, summing
the positive marks recovers (14) exactly, so the same estimate is literal
in the theta/divisor graph.  \(\square\)

## 4. The full compact form core

The maximal difference realization in 106.98 proves that \(\mathscr E_K\)
is closed.  We need the slightly stronger localization statement below.

### Lemma 2 — Smooth compact multipliers form a form core

The even part of \(C_c^\infty(\mathbb R)\) is dense in
\(D(\mathscr E_K)\) for the norm

\[
 \|r\|_{\mathscr E}^2
 =\|r\|_{L^2(\mu_K)}^2+\mathscr E_K(r).
 \tag{17}
\]

#### Proof

First apply a normal contraction to make \(r\) bounded.  If \(T_M\) is
radial truncation at height \(M\), both \(T_M\) and \(I-T_M\) are
Lipschitz with a universal constant.  Pointwise convergence and dominated
convergence in the difference representation (2)--(5) give
\(T_Mr\to r\) in the form norm.

For bounded \(r\), choose smooth cutoffs \(\eta_R\) which are one on
\([-R,R]\), zero off \([-R-1,R+1]\), and have uniformly bounded
derivative.  The product identity

\[
\begin{aligned}
 &(1-\eta_R(x))r(x)-(1-\eta_R(y))r(y)\\
 &\quad=(1-\eta_R(x))\{r(x)-r(y)\}
       +r(y)\{\eta_R(y)-\eta_R(x)\}
\end{aligned}
\tag{18}
\]

and \(|a+b|^2\le2|a|^2+2|b|^2\) show that

\[
 \mathscr E_K((1-\eta_R)r)
 \le o(1)+2\|r\|_\infty^2\mathscr E_K(\eta_R).
 \tag{19}
\]

The first term tends to zero by dominated convergence against the finite
energy density of \(r\).  The proof of Lemma 1, with a unit-width smooth
transition in place of a sharp cut, gives
\(\mathscr E_K(\eta_R)\to0\).  The weighted \(L^2\) tail also tends to
zero.  Hence compactly supported bounded form-domain functions are dense.

Finally mollify on a fixed compact interval.  Split the Gamma integral at
\(u=\varepsilon\), the prime sum at \(n=N\), and use ordinary translation
continuity on the resulting finite-measure part.  On \(0<u<\varepsilon\),
the difference quotient is controlled by the original Gamma energy; on
the omitted prime and large-\(u\) pieces, (8) gives a uniform summable
majorant.  Let the mollifier radius tend to zero, then
\(\varepsilon\downarrow0\) and \(N\to\infty\).  Symmetrizing the
mollified function preserves evenness.  This proves (17).  \(\square\)

## 5. No bounded boundary current

### Theorem 3 — Local divergence freeness has no boundary term

If \(F\in\mathscr H_{\rm src}\) satisfies (6), then

\[
 \boxed{
 \langle F,\mathcal Gr\rangle_{\rm src}=0
 \qquad\bigl(r\in D(\mathscr E_K)\bigr).}
 \tag{20}
\]

In particular it vanishes on every heat and hybrid row of 106.98.

#### Proof

The functional

\[
 r\longmapsto\langle F,\mathcal Gr\rangle_{\rm src}
 \tag{21}
\]

is continuous in the form norm, with norm at most \(\|F\|_{\rm src}\).
It vanishes on the core in Lemma 2, and therefore vanishes on its closure.
\(\square\)

There is a direct flux version.  Define the one-sided flux

\[
 \Phi_F(R)=\langle F,\mathcal G\chi_R\rangle_{\rm src}.
 \tag{22}
\]

For \(R_1<R_2\), the difference \(\chi_{R_2}-\chi_{R_1}\) is a compact
annulus indicator on the folded half-line; its even lift is obtained in
form norm from compact smooth even tests.  Thus (6) makes
\(\Phi_F(R)\) independent of \(R\).  On the other
hand, Lemma 1 and Cauchy--Schwarz give

\[
 |\Phi_F(R)|^2
 \le \|F\|_{\rm src}^2\mathfrak c(R)
 \longrightarrow0
 \qquad(R\to+\infty).
 \tag{23}
\]

Hence the constant flux is zero.  This explicitly excludes a hidden
finite-energy source at the folded end.

## 6. Finite-resolution cycle exhaustion

A *finite quotient cycle* is defined as follows.  Partition a compact
interval of the folded half-line into finitely many cells, retain finitely
many channel or mark cells, and aggregate every remaining edge block only at the final
cemetery vertex.  Push a current forward by its incidence endpoints.  A
finite quotient cycle is a circulation on this finite oriented
multigraph.  Every such circulation is an algebraic finite sum of ordinary
incidence cycles.  Its *conditional lift* is the block-constant current
having the prescribed integrated current on each edge block.

### Theorem 4 — Every bounded Hodge current is a limit of quotient cycles

For every \(F\in\mathscr H_{\rm src}\) satisfying (6), there is a cofinal
sequence of finite quotient circulations whose conditional lifts
\(F_N\) satisfy

\[
 \boxed{\|F_N-F\|_{\rm src}\longrightarrow0.}
 \tag{24}
\]

Moreover the norm of the part of a quotient circulation meeting its
cemetery vertex tends to zero.

#### Proof

Choose folded-half-line partitions whose mesh tends to zero and whose
bounded region tends to \([0,\infty)\).  Refine simultaneously the
displacement, prime-power and theta-mark coordinates.  For two distinct spatial cells
\(A,B\), every corresponding edge block has finite conductance.  This is
clear away from the diagonal; for adjacent cells the length of the
crossing interval cancels the \(1/u\) Gamma singularity exactly as in
(11).  Edges whose endpoints lie in one cell are loops in the quotient
and may be set to zero.  Their contribution to the \(L^2\) norm tends to
zero as the mesh tends to zero, because the diagonal itself has no edge
mass and \(|F|^2\) is integrable.

On each non-loop block \(E_{AB}\), set the lifted block coefficient equal
to its conditional mean,

\[
 F_{AB}
 =\frac{1}{\Omega(E_{AB})}
   \int_{E_{AB}}F\,d\Omega.
 \tag{25}
\]

Cauchy--Schwarz shows that this conditional averaging is contractive.
The martingale convergence theorem, applied to the increasing edge
partitions, gives convergence to \(F\) in \(\mathscr H_{\rm src}\).

For a vertex cell \(A\), the incidence sum of the finite pushed-forward
flow is

\[
 \sum_B\int_{E_{BA}}F\,d\Omega
 -\sum_B\int_{E_{AB}}F\,d\Omega
 =\langle F,\mathcal G\mathbf1_A\rangle.
 \tag{26}
\]

It is zero by Theorem 3.  The same is true at the cemetery vertex because
the total incidence sum of a finite graph is zero.  The pushed-forward
flow is therefore a finite circulation and decomposes into finite cycles.

Finally, the source norm on edges meeting the cemetery vertex tends to
zero by dominated convergence applied to \(|F|^2\).  Its scalar net flux
also tends to zero at the quantitative rate (23).  Thus the cemetery
cycles disappear in the cofinal limit, proving (24).  \(\square\)

The theorem is deliberately stated for finite **quotient** cycles.  Point
edges in the Gamma channel have measure zero, so literal delta-triangles
are not Hilbert vectors.  Quotient cycles are the correct finite-incidence
objects in the actual weighted source norm.  A conditional lift need not
be divergence free against tests which resolve the interior of one cell;
its exact assertion is that the current is a circulation at that finite
resolution.  Theorem 4 says that every bounded Hodge current is the
projective Hilbert limit of these exact finite-resolution circulations.  It
does not replace Theorem 3, which is the statement that the limiting
current has zero action on every form-domain gradient.

## 7. Exact cost of a nonzero boundary object

Suppose a possibly distributional current \(F\) carries a cofinal flux

\[
 |\Phi_F(R_k)|\ge\eta>0,
 \qquad R_k\to+\infty.
 \tag{27}
\]

Whenever its restriction to the cut is square integrable,
Cauchy--Schwarz and Lemma 1 force

\[
 \boxed{
 \|F\|_{L^2(\partial H_{R_k},\Omega)}^2
 \ge\frac{\eta^2}{\mathfrak c(R_k)}
 \ge c_0\eta^2\exp\{a_0e^{R_k}\}.}
 \tag{28}
\]

Thus a nonzero boundary channel must have super-double-exponentially
growing source density.  In particular it cannot define a bounded row of
an operator from \(\mathscr H_{\rm src}\).

In operator language, let \(B:\mathscr H_{\rm src}\to\mathscr Y\) be
bounded and assume every row \(B^*y\) is locally divergence free.  Theorem
3 gives

\[
 B\mathcal G=0.
 \tag{29}
\]

It follows that no such boundary operator can satisfy
\(B\mathcal G=D_\mu\), nor can it supply the nonzero complementary polar
map after radical anti-shorting.  An unbounded distribution satisfying
(28) would not repair this: contractivity on the heat rows requires a
bounded operator in precisely the norm which (29) destroys.

The same conclusion holds for a closable operator.  Suppose
\(B_0\) is densely defined on \(\mathscr H_{\rm src}\), its domain contains
\(\mathcal G C_c^\infty\), and \(B_0\) is closable.  If every adjoint row
\(B_0^*y\), \(y\in D(B_0^*)\), satisfies (6), then Theorem 3 gives

\[
 \langle B_0\mathcal Gr,y\rangle
 =\langle\mathcal Gr,B_0^*y\rangle=0
 \tag{30}
\]

on the compact gradient core.  Since \(D(B_0^*)\) is dense, one has
\(B_0\mathcal Gr=0\) there.  Thus a nonzero closable boundary map must
either fail the local divergence equation in an adjoint row or exclude
the physical gradient core from its domain.  Neither option realizes the
proposed Hodge boundary completion.

## 8. Consequence for the physical-surplus search

The infinite-boundary escape from 106.111 is closed:

* every bounded Hilbert current which is locally divergence free has zero
  boundary action on the complete form domain, and the same holds rowwise
  for a closable operator containing the physical gradient core;
* the bounded infinite Hodge sector is the closure of finite quotient
  cycles and contains no additional boundary class;
* the theta and von Mangoldt tails strengthen, rather than weaken, this
  conclusion because their cut conductance is superexponentially small;
* a nonzero boundary class would need the unbounded growth (28).

This does **not** prove the physical surplus.  It proves that the missing
contraction cannot be produced by an infinite divergence-free incidence
flow at infinity.  The surviving mechanism must fail local divergence
freeness in a controlled, globally signed way after exact radical
anti-shorting.  Equivalently, it must be the genuinely nonlocal
complementary contraction of 106.111(25), not a hidden Hodge boundary
term.
