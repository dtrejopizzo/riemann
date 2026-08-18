# 106.115 — Folded stochastic monotonicity and the prime-reflection gate

## 1. Purpose and verdict

Document 106.42 excludes the classical TP2/variation-diminishing route to
ordering the threshold state

\[
 r_1=K''/K,
 \qquad
 Lr_1=\frac12\bigl(r_1-\mu_K(r_1)\bigr).
 \tag{1}
\]

A strictly weaker possibility is that the folded Markov semigroup on
\([0,\infty)\) preserves the cone of increasing functions.  One might then
try to combine stochastic monotonicity with the one-crossing shape of
\(r_1-\mu_K(r_1)\) and conclude that it is the first centered mode.

That hypothesis is false for the literal Riemann generator.  The failure is
not caused by the Gamma minor of 106.42.  It is caused by each ordinary
prime-power atom after folding: a displacement \(u\) contains the reflected
branch

\[
 t\longmapsto |t-u|,
 \tag{2}
\]

which reverses order on \(0<t<u\).  The first atom \(u=\log2\) produces an
explicit downward jump in an upper-tail jump rate.  The Gamma continuum and
all remaining von Mangoldt atoms are continuous at that jump and therefore
cannot repair it.

Consequently neither the folded semigroup nor its full resolvent family
preserves the increasing cone.  Stochastic ordering cannot declare (1) the
first centered eigenfunction.  No zero-location statement is used.

## 2. Semantic nonduplication audit

The nearest project results are the following.

1. 106.42 finds a negative two-by-two minor of the Gamma translation kernel
   and excludes TP2 and variation diminution.
2. 104.21 finds a PF2 failure in a prime exponent fibre.
3. 103.64 excludes a Monge/convex-order closure in the cell--lobe
   coordinate.

None of those statements tests stochastic monotonicity of the **folded
physical Doob process**.  The upper-tail discontinuity proved below retains
the actual state-dependent Doob factors, every ordinary von Mangoldt atom,
and the Gamma continuum.  It is therefore a distinct, weaker order gate.

## 3. The folded jump kernel

Write

\[
 a_n=\frac{\Lambda(n)}{\sqrt n},
 \qquad
 g(u)=\frac{e^{-u/2}}{1-e^{-2u}},
 \qquad
 h(t)=\cosh(t/2),
 \qquad c_K=\frac12.
 \tag{3}
\]

Let \(\mathcal A=-L\) be the Markov-sign generator.  If
\(r(x)=\phi(|x|)\), then 106.41(7) gives, for \(t\geq0\),

\[
\begin{aligned}
 (\mathcal A^F\phi)(t)
 =\frac{c_K}{h(t)}\Bigg[&
 \int_0^\infty g(u)\Bigl{
 K(|t-u|)\bigl(\phi(|t-u|)-\phi(t)\bigr)\\
 &\hspace{31mm}+K(t+u)\bigl(\phi(t+u)-\phi(t)\bigr)
 \Bigr\}\,du\\
 &+\sum_{n\geq2}a_n\Bigl{
 K(|t-\log n|)\bigl(\phi(|t-\log n|)-\phi(t)\bigr)\\
 &\hspace{31mm}+K(t+\log n)
 \bigl(\phi(t+\log n)-\phi(t)\bigr)
 \Bigr\}\Bigg].
\end{aligned}
\tag{4}
\]

Here and below the sum is effectively over prime powers, because
\(a_n=0\) otherwise.  Thus the off-diagonal folded jump measure at \(t\)
has, for every \(u=\log n\), the two literal targets

\[
 |t-u|,
 \qquad t+u,
 \tag{5}
\]

with respective rates

\[
 \frac{c_Ka_n}{h(t)}K(|t-u|),
 \qquad
 \frac{c_Ka_n}{h(t)}K(t+u).
 \tag{6}
\]

The same two-target formula holds continuously with density \(g(u)du\).

For \(z>t\), define the finite upper-tail rate

\[
 Q_t(z):=q_t^F((z,\infty)).
 \tag{7}
\]

It is finite because displacements \(u<z-t\) do not enter the tail, while
the double-exponential decay of \(K(t\pm u)\) controls the opposite end.
Formula (4) gives

\[
\begin{aligned}
Q_t(z)=\frac{c_K}{h(t)}\Bigg[&
\int_0^\infty g(u)\bigl{
 K(|t-u|){\bf1}_{\{|t-u|>z\}}
 +K(t+u){\bf1}_{\{t+u>z\}}
\bigr}\,du\\
&+\sum_{n\ge2}a_n\bigl{
 K(|t-\log n|){\bf1}_{\{|t-\log n|>z\}}
 +K(t+\log n){\bf1}_{\{t+\log n>z\}}
\bigr}\Bigg].
\end{aligned}
\tag{8}
\]

## 4. A literal \(p=2\) violation

Put

\[
 u_0=\log2,
 \qquad
 t_0=\frac{u_0}{4},
 \qquad
 z=\frac{3u_0}{4}.
 \tag{9}
\]

In particular \(0<t_0<z\).  For \(t\) close to \(t_0\), the reflected
target of the \(n=2\) atom is \(u_0-t\), and

\[
 u_0-t>z
 \quad\Longleftrightarrow\quad
 t<t_0.
 \tag{10}
\]

Its forward target \(t+u_0\) lies above \(z\) on both sides and varies
continuously.  Therefore the reflected branch contributes to (8) the
one-sided jump

\[
 \boxed{
 \Delta_2
 =\frac{c_K}{h(t_0)}\frac{\Lambda(2)}{\sqrt2}K(z)>0.}
 \tag{11}
\]

### Lemma 1 — The complementary tail is continuous at \(t_0\)

After deleting only the reflected \(n=2\) term in (8), the resulting
function of \(t\) is continuous at \(t_0\).

#### Proof

For the Gamma integral, the two moving boundaries remain a positive
distance from \(u=0\).  On a fixed neighbourhood of \(t_0\), dominated
convergence applies: \(g\) is smooth away from zero and the theta-series
bound for \(K\) is integrable at infinity.

For a prime atom, an indicator in (8) can change at \(t_0\) only if

\[
 t_0+\log n=z
 \quad\hbox{or}\quad
 |t_0-\log n|=z.
 \tag{12}
\]

The first equation would require \(\log n=u_0/2=\log\sqrt2\), which is
impossible for an integer \(n\).  The second requires either
\(\log n=t_0+z=u_0\), hence \(n=2\), or
\(\log n=t_0-z=-u_0/2<0\), which is impossible for \(n\ge2\).
Thus every other prime indicator is locally constant.  Finally, the sum of
their continuous contributions converges locally uniformly: for large
\(n\), both relevant \(K\)-factors are bounded by the
double-exponentially decreasing theta tail at \(\log n+O(1)\), whereas
\(a_n\leq(\log n)/\sqrt n\).  This proves continuity. \(\square\)

Combining (10)--(11) with Lemma 1 gives

\[
 \lim_{\varepsilon\downarrow0}
 \bigl\{Q_{t_0-\varepsilon}(z)
       -Q_{t_0+\varepsilon}(z)\bigr\}
 =\Delta_2>0.
 \tag{13}
\]

Hence, for all sufficiently small \(\varepsilon>0\),

\[
 \boxed{
 t_0-\varepsilon<t_0+\varepsilon<z,
 \qquad
 Q_{t_0-\varepsilon}(z)>Q_{t_0+\varepsilon}(z).}
 \tag{14}
\]

This is the reverse of the necessary upper-tail ordering for a
stochastically monotone jump process.

## 5. Semigroup and resolvent consequences

### Theorem 2 — No increasing-cone invariance

The folded semigroup \(P_s^F=e^{s\mathcal A^F}\) does not preserve the
cone of bounded increasing functions.

#### Proof

Choose \(x=t_0-\varepsilon\) and \(y=t_0+\varepsilon\) as in (14).
Approximate \({\bf1}_{(z,\infty)}\) monotonically by smooth increasing
functions \(\phi_k\) which vanish on a neighbourhood of \([0,y]\) and are
one above \(z+1/k\).  The lifted even functions are smooth at the folded
origin.  Dominated convergence in (4) gives

\[
 (\mathcal A^F\phi_k)(t)\longrightarrow Q_t(z),
 \qquad t\in\{x,y\},
 \tag{15}
\]

after choosing the approximation so that neither of the two fixed jump
measures charges its transition endpoints.  By (14), for some \(k\),

\[
 \phi_k(x)=\phi_k(y)=0,
 \qquad
 (\mathcal A^F\phi_k)(x)>(\mathcal A^F\phi_k)(y).
 \tag{16}
\]

If \(P_s^F\) preserved increasing functions, then
\(P_s^F\phi_k(x)\leq P_s^F\phi_k(y)\) for every \(s>0\).  Subtract the
equality at \(s=0\), divide by \(s\), and let \(s\downarrow0\).  This
would give the opposite inequality to (16).  Hence cone invariance fails.
\(\square\)

The same test excludes a resolvent closure.  For a smooth graph-core
version of \(\phi_k\), the large-\(\alpha\) expansion

\[
 (\alpha-\mathcal A^F)^{-1}\phi_k
 =\alpha^{-1}\phi_k+\alpha^{-2}\mathcal A^F\phi_k
 +o(\alpha^{-2})
 \tag{17}
\]

shows, using (16), that the resolvent also reverses the order of its values
at \(x<y\) for all sufficiently large \(\alpha\).  Equivalently, one
cannot recover increasing-cone invariance by Laplace averaging the
semigroup.

## 6. What this decides about the threshold mode

The exact equation (1) still proves that \(1/2\) is an eigenvalue and gives
the upper bound

\[
 \inf\sigma(L|_{1^\perp})\leq\frac12.
 \tag{18}
\]

But the proposed weaker oscillation mechanism requires at minimum that the
folded evolution preserve the order cone used to distinguish the
one-crossing state.  Theorem 2 disproves that premise before any spectral
ordering is invoked.  In fact stochastic monotonicity alone would not be a
complete nodal theorem without an additional irreducibility/strictness
argument; here even the basic monotonicity is absent.

The obstruction is robust and arithmetic.  The construction works with
any isolated positive displacement atom \(u\): choose
\(0<t_0<u/2\), set \(z=u-t_0\), and avoid coincidences with the other
displacements.  The reflected branch then produces the same downward tail
jump.  For Riemann's source, \(u=\log2\) gives the canonical exact witness
(9)--(14).

Therefore a proof of the physical surplus on heat/hybrid rows cannot come
from stochastic monotonicity, an increasing invariant cone, or its
resolvent analogue.  The surviving target remains the globally signed,
radical-shorted contraction identified in 106.105 and 106.111--106.114.

