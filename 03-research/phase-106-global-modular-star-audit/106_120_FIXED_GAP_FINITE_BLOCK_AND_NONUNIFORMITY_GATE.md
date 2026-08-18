# 106.120 — Fixed-gap finite reduction and the near-threshold nonuniformity gate

## 1. Question and verdict

Let

\[
 A=L|_{(\mathbf1\oplus\mathcal R)^\perp},
 \qquad \mathfrak a[q]=\langle q,Aq\rangle,
 \tag{1}
\]

and recall the proved facts

\[
 \sigma_{\rm ess}(A)\subset[1/2,\infty),
 \qquad
 m_\Gamma(\xi)=\frac12\log|\xi|+O(1).
 \tag{2}
\]

This note tests whether (2) reduces every hypothetical subthreshold state
to a finite central/low-frequency problem with an error smaller than its
deficit.

The answer has two parts.

* For every fixed deficit \(\delta>0\), the answer is yes.  There is a
  finite heat-core block which detects every eigenvalue at most
  \(1/2-\delta\), retaining at least half the deficit.  Its rows may be
  chosen as exact radical projections of finitely many compact-window
  Fourier modes.
* There is no uniform version as \(\delta\downarrow0\) from (2).  The
  logarithmic Gamma moment gives compactness in Hilbert norm, but not in
  form norm.  A frequency packet can have Hilbert mass tending to zero
  while carrying a fixed amount of Gamma energy.  Consequently no finite
  frequency cutoff has a form-tail error controlled by the two inputs in
  (2), and the finite blocks may diverge without bound near the threshold.

This is a precise nonuniformity result, not a no-go for a stronger signed
prime--Gamma estimate.

## 2. Semantic audit

Document 106.47 proves the essential threshold and local Hilbert
compactness.  Document 106.59 already shows that localized compactness does
not imply the sharp Birman--Schwinger norm.  Document 106.69 rejects a
support-only uncertainty argument, and 106.98 supplies a form-core heat
exhaustion.  Document 106.116 (PNT heat quadrature) computes the full
logarithmic Gamma multiplier.  The result below does not reopen any of
those routes.  It identifies exactly what their combination does prove at
a fixed spectral distance and why that statement is nonuniform at
\(1/2\).

## 3. A finite theorem for every fixed deficit

For \(0<\delta<1/2\), put

\[
 P_\delta=\mathbf1_{(0,1/2-\delta]}(A),
 \qquad \mathcal H_\delta=\operatorname {Ran}P_\delta.
 \tag{3}
\]

### Theorem 1 — Fixed-gap finite form reduction

The space \(\mathcal H_\delta\) is finite dimensional.  Moreover, there is
a finite-dimensional subspace \(V_\delta\) of the heat form core such that
every normalized eigenvector

\[
 Aq=\alpha q,qquad \alpha\leq\frac12-\delta,
 \tag{4}
\]

has a vector \(v\in V_\delta\) satisfying

\[
 \|q-v\|^2+\mathfrak a[q-v]
 <\min\left\{\frac1{16},\frac\delta4\right\}.
 \tag{5}
\]

Consequently

\[
 \boxed{
 \inf_{0\ne v\in V_\delta}
 \frac{\mathfrak a[v]}{\|v\|^2}
 <\frac12-\frac\delta2.}
 \tag{6}
\]

Thus a violation with fixed deficit is detected by one rigorously finite
compression with a strictly smaller error.

#### Proof

The essential-threshold theorem makes every spectral projection on a
compact subset of \((0,1/2)\) finite rank.  Zero is absent on the radical
complement; otherwise it would be essential or an eigenvalue, while the
Gamma form forces every zero-energy row to be constant.  Hence (3) has
finite rank.

The heat spaces of 106.98 are a form-core exhaustion.  Strong form-core
convergence is uniform on the unit sphere of the finite-dimensional space
\(\mathcal H_\delta\).  Choose one finite heat space \(V_\delta\) for
which (5) holds.

Write \(e=q-v\).  The weak eigen-equation gives

\[
 \mathfrak a[q,e]=\alpha\langle q,e\rangle.
 \tag{7}
\]

Expanding \(v=q-e\) therefore yields the exact identity

\[
 \mathfrak a[v]-\alpha\|v\|^2
 =\mathfrak a[e]-\alpha\|e\|^2
 \leq\mathfrak a[e].
 \tag{8}
\]

By (5), \(\|v\|\geq3/4\) and \(\mathfrak a[e]<\delta/4\).  Hence

\[
 \frac{\mathfrak a[v]}{\|v\|^2}
 \leq\alpha+\frac{16}{9}\frac\delta4
 <\frac12-\frac\delta2,
 \tag{9}
\]

which proves (6).  \(\square\)

The numerical constant in (5) can be reduced arbitrarily; it has no
spectral significance.

## 4. Central and low-frequency realization in Hilbert norm

Since \(\mathcal H_\delta\) is finite dimensional, for every \(\eta>0\)
there is \(R<\infty\) such that

\[
 \sup_{q\in\mathcal H_\delta,\ \|q\|=1}
 \|(1-\chi_R)q\|<\eta.
 \tag{10}
\]

For the central part, local logarithmic coercivity gives a constant
\(C_R\), independent of the normalized \(q\in\mathcal H_\delta\), with

\[
 \int_{\mathbb R}\log(2+|\xi|)
 |\widehat{\chi_Rq}(\xi)|^2d\xi\leq C_R.
 \tag{11}
\]

Therefore

\[
 \boxed{
 \int_{|\xi|>\Omega}|\widehat{\chi_Rq}(\xi)|^2d\xi
 \leq\frac{C_R}{\log(2+\Omega)}.}
 \tag{12}
\]

Choosing \(\Omega\) finite makes (10)--(12) smaller than any prescribed
Hilbert error.  A finite Fourier mesh on \([-R,R]\), followed by exact
projection to the radical complement, therefore gives a finite
central/low-frequency approximation in Hilbert norm.  The form-norm block
in Theorem 1 is obtained instead from the heat-core exhaustion.  The next
section explains why the logarithmic estimate alone does not identify the
two blocks quantitatively.  In either construction the radical projection
is global; hence the correct statement is a block *generated* by central
modes, not a compactly supported block after exact radical shorting.

## 5. Why the logarithmic estimate does not preserve the deficit

Rayleigh detection requires the form error \(\mathfrak a[q-v]\), not only
the Hilbert error in (12).  A bounded first logarithmic moment does not make
its own tail uniformly integrable.

### Theorem 2 — Sharp logarithmic nonuniformity

For every fixed frequency cutoff \(\Omega\) and every \(c>0\), there are
smooth compact hybrid packets \(f_N\), with \(N>\Omega\), such that

\[
 \|f_N\|_2^2\longrightarrow0,
 \qquad
 \int_0^\infty
 \|f_N-\tau_uf_N\|_2^2c_\infty(u)\,du\longrightarrow c.
 \tag{13}
\]

Thus no function \(\varepsilon(\Omega)\downarrow0\) can bound the Gamma
form tail above \(\Omega\) using only a uniform Gamma-form bound.

#### Proof

Fix nonzero \(\chi\in C_c^\infty(\mathbb R)\), put \(\phi=K\chi\), and let

\[
 f_N(x)=a_N\phi(x)\cos(Nx).
 \tag{14}
\]

The exact Gamma multiplier gives

\[
 \int_0^\infty
 \|f_N-\tau_uf_N\|_2^2c_\infty(u)\,du
 =\frac{a_N^2\|\phi\|_2^2}{2}\log N+O(a_N^2).
 \tag{15}
\]

Choose

\[
 a_N^2=\frac{2c}{\|\phi\|_2^2\log N}.
 \tag{16}
\]

Then (13) follows, while the Fourier mass of \(f_N\) lies in packets
centered at \(\pm N\), outside every fixed cutoff.  \(\square\)

For a target deficit \(\delta\), choose \(c=2\delta\).  The packet then
has vanishing Hilbert norm but form energy larger than the allowed error.
This proves that (12) cannot be promoted to the form estimate (5) from the
Gamma logarithmic moment alone.  One would need a uniformly integrable
higher Gamma moment, an eigen-equation estimate coupling high frequency to
the literal primes, or the missing signed physical surplus itself.

Even at the Hilbert level, (12) requires

\[
 \log(2+\Omega)\gtrsim C_R/\eta^2.
 \tag{17}
\]

Taking \(\eta^2\asymp\delta\) produces the unavoidable scale

\[
 \boxed{\Omega_\delta\gtrsim\exp(C_R/\delta).}
 \tag{18}
\]

This is an upper-bound requirement of this method, not a claimed optimal
law for the Riemann operator.

## 6. Near-threshold and off-line stress tests

The finite-rank spaces in Theorem 1 are nested as \(\delta\downarrow0\).
The essential-floor theorem permits infinitely many eigenvalues
accumulating at \(1/2\).  Therefore it supplies no uniform bound on
\(\dim V_\delta\), \(R_\delta\), or \(\Omega_\delta\).  If such a bound
were uniform, one fixed finite compression would contain the entire
subthreshold spectral projection, a conclusion strictly stronger than
essential discreteness and not implied by it.

The off-line channel has exactly the same vanishing-margin stress.  Let
\(s=\gamma+ib\) be a centered off-line sample and let \(F\) be real on the
real axis with \(F(\gamma)=0\), \(F'(\gamma)\ne0\).  Then

\[
 F(\gamma+ib)=ibF'(\gamma)+O(b^2),
 \tag{19}
\]

and its quartet contribution to the signed evaluation form is

\[
 \boxed{
 4m_s\{(\operatorname {Re}F(s))^2
       -(\operatorname {Im}F(s))^2\}
 =-4m_sb^2F'(\gamma)^2+O(b^4).}
 \tag{20}
\]

Thus the individual negative channel becomes quadratically weak as an
off-line orbit approaches the critical line.  Formula (20) does not assert
that the actual bottom deficit equals a fixed multiple of \(b^2\); it proves
that no positive margin independent of \(b\) can come from the orbit
evaluation formula.  The growth in (18) is therefore not removable by
assuming that every hypothetical off-line zero has a uniformly visible
negative channel.

## 7. Result

The essential floor and exact Gamma multiplier do give a useful theorem:
every violation separated from \(1/2\) by a fixed \(\delta\) is detected by
one finite radically shorted heat block, with at least half its deficit
left over.

They do not give a uniform finite reduction for all \(\delta>0\).  The
precise obstruction is the distinction

\[
 \boxed{
 \text{logarithmic form boundedness}
 \Longrightarrow \text{Hilbert compactness},
 \qquad
 \not\Longrightarrow \text{form-tail compactness}.}
 \tag{21}
\]

Closing the near-threshold regime requires an additional estimate which
makes the Gamma energy uniformly integrable after the actual prime phases
and exact radical anti-short are included.  That estimate is not supplied
by the essential threshold or by uncertainty alone.
