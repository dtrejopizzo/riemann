# 106.111 — Local Hodge--Korn radical rigidity

## 1. Purpose and verdict

The theta--divisor normal form of 106.104 is already an orthogonal Hodge
decomposition on every finite divisor fibre: the divisor current is the
constant component and the cross-divisor dispersion is its orthogonal
component.  The character covariance of 106.108 gives a second, unitarily
equivalent, Hodge coordinate for the nonzero residue fibres.  This note
tests whether the signed Gamma--pole term can be added to those local
coordinates so that the completed form becomes a nonnegative local square.

There is an exact obstruction.  On any finite collection of spatial
vertices, the signatures

\[
 \bigl(K^{(2j)}(x)/K(x)\bigr)_{j\geq0}
\]

are linearly independent as the vertex \(x\) varies.  Consequently a
finite local linear combination of edge increments which vanishes on every
Riemann-radical multiplier is necessarily a divergence-free incidence
cycle.  Such a cycle vanishes on the gradient of *every* multiplier.  On
the star fibres occurring in 106.104 there are no cycles, so all its
coefficients vanish.

Therefore no nontrivial finite-local Hodge, Korn or sum-of-squares
completion can be both positive and sharp on the complete radical.  A
surviving square must first apply the exact radical anti-short.  That
operation is intrinsically global, and in the Hodge coordinates of
106.104/106.108 its remaining estimate is exactly the complementary Korn
contraction already isolated in 106.39.  A subthreshold mode violates that
contraction by the sharp factor \((2\alpha)^{-1/2}>1\).

The result is a rigidity theorem and a gate, not a proof of the physical
surplus.  No zero-location hypothesis is used.

## 2. Radical vertex signatures

Put

\[
 r_j(x)=\frac{K^{(2j)}(x)}{K(x)},\qquad j=0,1,2,\ldots,
 \tag{1}
\]

on the positive half-line.  For \(a\geq0\), define the analytic germ

\[
 \mathcal A_a(z)
 :=\sum_{j\geq0}\frac{r_j(a)z^{2j}}{(2j)!}
 =\frac{K(a+z)+K(a-z)}{2K(a)}.
 \tag{2}
\]

The theta series makes (2) analytic in the connected strip
\(|\mathrm{Im}\,z|<\pi/4\).

### Lemma 1 — Finite vertex independence

Let \(0\leq a_1<\cdots<a_m\).  If

\[
 \sum_{\nu=1}^m c_\nu r_j(a_\nu)=0
 \qquad\text{for every }j\geq0,
 \tag{3}
\]

then \(c_1=\cdots=c_m=0\).

#### Proof

Summing (3) against \(z^{2j}/(2j)!\) gives

\[
 \sum_{\nu=1}^m c_\nu\mathcal A_{a_\nu}(z)=0.
 \tag{4}
\]

The identity continues throughout the strip.  Along the positive real
axis the first theta atom gives, uniformly for fixed \(a\),

\[
 K(z-a)
 =C e^{9(z-a)/2}e^{-\pi e^{2(z-a)}}(1+o(1)),
 \qquad z\to+\infty,
 \tag{5}
\]

whereas \(K(z+a)\) is smaller.  Hence

\[
 \frac{\mathcal A_{a_\nu}(z)}
      {\mathcal A_{a_m}(z)}\longrightarrow0
 \qquad(\nu<m).
 \tag{6}
\]

Dividing (4) by \(\mathcal A_{a_m}(z)\) gives \(c_m=0\).
Descending induction proves the lemma.  \(\square\)

Lemma 1 is the vertex version of the edge-separation calculation in
106.65.  It is recorded here because Hodge rigidity needs arbitrary finite
incidence patterns, not only equality of two oriented edges.

## 3. Finite-incidence Hodge rigidity

Let \(V\subset[0,\infty)\) be finite and let \(E\) be a finite oriented
multigraph with endpoint maps \(s,t:E\to V\).  For a function \(r\) on
\(V\), write

\[
 (\nabla_Vr)_e=r(t(e))-r(s(e)).
 \tag{7}
\]

For coefficients \(c=(c_e)_{e\in E}\), use the incidence divergence

\[
 (\mathrm{div}\,c)_v
 =\sum_{e:t(e)=v}c_e-\sum_{e:s(e)=v}c_e.
 \tag{8}
\]

Then the discrete integration-by-parts identity is

\[
 \sum_{e\in E}c_e(\nabla_Vr)_e
 =\sum_{v\in V}(\mathrm{div}\,c)_v r(v).
 \tag{9}
\]

### Theorem 2 — Radical-sharp local amplitudes are null cycles

For \(c\in\mathbb C^E\), the following are equivalent:

1. \(\sum_ec_e(\nabla_Vr_j)_e=0\) for every \(j\geq0\);
2. \(\mathrm{div}\,c=0\);
3. \(\sum_ec_e(\nabla_Vr)_e=0\) for every function \(r:V\to\mathbb C\).

In particular, if the underlying unoriented graph is a forest, then all
coefficients on its nondegenerate edges vanish.

#### Proof

By (9), condition 1 is

\[
 \sum_{v\in V}(\mathrm{div}\,c)_v r_j(v)=0
 \qquad(j\geq0).
 \tag{10}
\]

Lemma 1 gives \(\mathrm{div}\,c=0\), proving 1 implies 2.  Equation
(9) gives 2 implies 3, and 3 implies 1 is immediate.  On a finite forest
the incidence kernel is the cycle space and is zero after degenerate edges
are removed.  \(\square\)

The matrix form is useful.  Let \(B:\mathbb C^E\to\mathbb C^q\) be any
linear map.  If

\[
 B\nabla_Vr_j=0\qquad(j\geq0),
 \tag{11}
\]

then every row of \(B\) is divergence free, and therefore

\[
 \boxed{B\nabla_Vr=0\quad\text{for every }r:V\to\mathbb C.}
 \tag{12}
\]

Thus a local amplitude can annihilate the complete radical only by
annihilating the entire gradient space.

## 4. Application to the theta--divisor fibres

Fix \(b\geq2\) and \(y\geq0\).  The same-side fibre of 106.104 has the
vertices

\[
 V_{b,y}^+=\{y\}\cup
 \{y+\log n:n\mid b,\ \Lambda(n)>0\}
 \tag{13}
\]

and one edge from \(y\) to each shifted vertex.  It is a star.  The
central fibre at \((b,x)\) has the vertices

\[
 V_{b,x}^-=\{x\}\cup
 \{\log n-x:n\mid b,\ \Lambda(n)>0,\ \log n\geq x\},
 \tag{14}
\]

after degenerate edges and repeated vertices are identified.  It is also
a star.

The weighted ANOVA transform in 106.104 is a unitary change of coordinates
on the edge vector of each star.  Its constant coordinate is the divisor
current and its orthogonal coordinates have squared norm equal to the
cross-divisor dispersion.  The finite character transform of 106.108 is
another unitary change of coordinates on the residue fibres.  Neither
transform changes the incidence graph.

### Corollary 3 — No fibrewise sharp Hodge square

Let \(B_{b,y}^+\) and \(B_{b,x}^-\) be arbitrary finite matrices acting on
the complete current-plus-dispersion coordinates of the fibres (13)--(14).
If their amplitudes vanish on every radical multiplier,

\[
 B_{b,y}^+\nabla r_j=0,
 \qquad
 B_{b,x}^-\nabla r_j=0
 \qquad(j\geq0),
 \tag{15}
\]

then both amplitudes vanish on every spatial multiplier.  In particular,
no nonzero fibrewise sum of squares formed from divisor currents,
cross-divisor dispersions or residue-character amplitudes can be a sharp
positive remainder of the completed Weil form.

#### Proof

Undo the unitary ANOVA/character coordinates.  Each row becomes a linear
combination of the increments on a finite star.  Apply Theorem 2.  \(\square\)

The conclusion remains true if finitely many Gamma or polar edges are
adjoined to a fibre: the resulting finite incidence pattern may acquire
cycles, but every surviving row is then a cycle and its value on every
gradient is identically zero.  This is the precise Hodge obstruction.  It
does not depend on the signs or sizes of the coefficients.

## 5. Consequence for integral sum-of-squares representations

Let \((\Omega,\eta)\) be a sigma-finite measure space.  Suppose an exact
representation of the completed form had the local shape

\[
 QW(Kr,Kr)
 =\int_\Omega
   \|B_\omega\nabla_{V_\omega}r\|^2\,d\eta(\omega),
 \tag{16}
\]

where \(V_\omega\) is finite for almost every \(\omega\), and all
ordinary-prime, Gamma and polar terms have first been assembled with a
common cutoff before the nonnegative limit (16) is taken.  Assume (16)
holds on the radical multipliers as well as the form core.

For every \(j\), radical equality gives

\[
 0=\int_\Omega
   \|B_\omega\nabla_{V_\omega}r_j\|^2d\eta(\omega).
 \tag{17}
\]

Taking the countable intersection of the corresponding full-measure sets,
Theorem 2 gives

\[
 B_\omega\nabla_{V_\omega}r=0
 \quad\text{for every }r
 \quad\text{for almost every }\omega.
 \tag{18}
\]

Thus the right side of (16) is identically zero.  Therefore any nontrivial
sharp square must violate at least one local hypothesis of (16): it must
be globally nonlocal, must be formed only after the complete radical has
been anti-shorted, or must retain a signed/Krein channel rather than a
positive local norm.

This statement is cutoff-safe.  It does not assert that the separately
divergent prime, Gamma and polar pieces have limits.  It starts only after
an exact common-cutoff assembly has produced the nonnegative expression
(16), and Tonelli is applied solely to that expression.

## 6. The exact nonlocal Korn remainder

Let \(\mathcal G_H=W\mathcal G\), where \(W\) is any one of the exact
unitary source gauges already constructed: either the farther-endpoint
ANOVA gauge of 106.104 (on both same-side and central fibres), or the
residue-character gauge of 106.108 with the identity on its remaining
fibres.  These are alternative coordinates on the same source, not two
additional orthogonal energies.  In either gauge,

\[
 \mathcal G_H^*\mathcal G_H=\mathcal G^*\mathcal G=A.
 \tag{19}
\]

Let

\[
 \mathscr M_H=
 \overline{\mathrm{span}}
 \{\mathcal G_Hr_j:j\geq0\}.
 \tag{20}
\]

Polarized radical equality defines the isometry

\[
 U_H(\mathcal G_Hr_j)=D_\mu r_j.
 \tag{21}
\]

For every form-core multiplier, put

\[
 \begin{aligned}
 G_\perp r&=P_{\mathscr M_H^\perp}\mathcal G_Hr,\\
 D_\perp r&=D_\mu r-U_HP_{\mathscr M_H}\mathcal G_Hr.
 \end{aligned}
 \tag{22}
\]

Polarization gives

\[
 U_H^*D_\mu r=P_{\mathscr M_H}\mathcal G_Hr,
 \tag{23}
\]

and hence the exact Hodge--Korn identity

\[
 \boxed{
 QW(Kr,Kr)=\|G_\perp r\|^2-\|D_\perp r\|^2.}
 \tag{24}
\]

All physical source channels are present in \(G_\perp\).  In the first
gauge they are displayed as currents and dispersions; in the second, the
fractional channel is displayed by its residue characters.  The pole is
\(D_\perp\).  Equation (24) is not a new positivity assertion.  It
identifies the only possible sharp Korn step:

\[
 \boxed{\|D_\perp r\|\leq\|G_\perp r\|.}
 \tag{25}
\]

By the Douglas factorization lemma, (25) is equivalent to the existence of
a contraction \(C_\perp\) satisfying

\[
 D_\perp=C_\perp G_\perp.
 \tag{26}
\]

Theorem 2 shows why \(C_\perp\) cannot be assembled from finite local
Hodge blocks: the radical projection in (22) is load-bearing and globally
nonlocal.

## 7. Heat and off-line stress tests

For a positive heat or hybrid state \(\Gamma_t\), (24) lifts by a common
form-core approximation to

\[
 \mathrm{Tr}\,\{(A-\tfrac12I)\Gamma_t\}
 =\|G_\perp\Gamma_t^{1/2}\|_{\mathfrak S_2}^2
  -\|D_\perp\Gamma_t^{1/2}\|_{\mathfrak S_2}^2.
 \tag{27}
\]

If a hypothetical radically shorted mode satisfies

\[
 Aq=\alpha q,\qquad0<\alpha<\tfrac12,
 \tag{28}
\]

then \(q\) is orthogonal to the threshold radical and

\[
 \|G_\perp q\|^2=\alpha\|q\|^2,
 \qquad
 \|D_\perp q\|^2=\tfrac12\|q\|^2.
 \tag{29}
\]

Thus

\[
 \boxed{
 \frac{\|D_\perp q\|}{\|G_\perp q\|}
 =(2\alpha)^{-1/2}>1.}
 \tag{30}
\]

The same violation occurs for the literal off-line mean-periodic vector of
106.93.  Hence (25) passes the required falsifier: it is not implied by the
local incidence algebra, by theta-character positivity or by heat
averaging.

## 8. Status

Proved here:

* finite linear independence of the radical vertex signatures;
* exact incidence/Hodge rigidity on every finite spatial graph;
* triviality of every finite-local positive square which is sharp on the
  complete Riemann radical;
* the specialization to the divisor-current, cross-divisor-dispersion and
  residue-character fibres;
* the cutoff-safe obstruction to an integral of finite-local squares;
* the exact globally nonlocal Hodge--Korn remainder (24);
* the sharp subthreshold amplification factor (30).

Not proved here:

\[
 \|D_\perp r\|\leq\|G_\perp r\|.
\]

The new obstruction says that this inequality cannot arise from a local
Hodge or Korn completion of the theta--divisor fibres.  It must use a
globally nonlocal arithmetic contraction after exact radical anti-shorting,
or equivalently a genuinely signed global absorption of the off-line
channel.
