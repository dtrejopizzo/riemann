# 106.37 — The global signed quotient factorization

## Purpose

Document 106.36 showed that no proof obtained by leaving a positive local
edge remainder can be sharp: every derivative of Riemann's kernel is an
exact equality vector.  This note therefore tests the surviving proposal,
namely a factorization which

1. keeps the ordinary-prime, Gamma and polar contributions coupled;
2. annihilates the entire Riemann radical, not only its ground vector;
3. is globally signed rather than atomwise positive.

Such a factorization does exist.  On the even real Weil domain it is the
Krein factorization of the evaluation quotient by the divisor of
\(\Xi\).  It is exact and gives the requested cross-tower interference.
It also exposes a terminal obstruction: every off-line quartet produces
one accessible negative evaluation channel.  Hence the factorization by
itself does not prove the complement floor; eliminating its negative
channel is equivalent to excluding off-line zeros.

No statement below assumes RH.

## 1. Domain and zero orbits

Use the normalized zero coordinate

\[
 \rho=\frac12+is,
 \qquad
 \mathcal Z=\{s\in\mathbb C:\zeta(\tfrac12+is)=0\},
 \tag{1}
\]

with multiplicity.  The divisor is invariant under

\[
 s\mapsto-s,
 \qquad
 s\mapsto\overline s.
 \tag{2}
\]

Let \(\mathcal D_{\mathrm{ev}}\) be the real even, smooth compactly
supported Weil domain and put

\[
 F(z)=\widehat f(z)=\int_{\mathbb R}f(u)e^{-izu}\,du.
 \tag{3}
\]

Then

\[
 F(-z)=F(z),
 \qquad
 F(\overline z)=\overline{F(z)}.
 \tag{4}
\]

Split the zero divisor into two types.

* A critical pair is \(\{\gamma,-\gamma\}\subset\mathbb R\), with
  multiplicity \(m_\gamma\).
* An off-line orbit is
  \(\mathcal O_s=\{s,-s,\overline s,-\overline s\}\), where
  \(\Re s\,\Im s\ne0\), with common multiplicity \(m_s\).  Choose one
  representative from each such orbit.

The absence of nontrivial real zeros \(0<\rho<1\) ensures that these are
the only cases.

## 2. Exact Krein evaluation factorization

Define real evaluation maps by

\[
 \begin{aligned}
 (T_0f)_\gamma&=\sqrt{2m_\gamma}\,F(\gamma),\\
 (T_+f)_s&=2\sqrt{m_s}\,\Re F(s),\\
 (T_-f)_s&=2\sqrt{m_s}\,\Im F(s).
 \end{aligned}
 \tag{5}
\]

The target sequence spaces are real \(\ell^2\) spaces over the indicated
zero orbits.

### Theorem 1 — Global signed factorization

For every \(f,g\in\mathcal D_{\mathrm{ev}}\),

\[
 \boxed{
 QW(f,g)
 =\langle T_0f,T_0g\rangle
  +\langle T_+f,T_+g\rangle
  -\langle T_-f,T_-g\rangle.}
 \tag{6}
\]

In particular,

\[
 \boxed{
 QW(f,f)=\|T_0f\|^2+\|T_+f\|^2-\|T_-f\|^2.}
 \tag{7}
\]

All three norms in (7) are finite.

#### Proof

The polarized explicit formula on this domain is the absolutely convergent
identity

\[
 QW(f,g)=\sum_{s\in\mathcal Z}
   \overline{F(\overline s)}G(s).
 \tag{8}
\]

By (4), the summand is \(F(s)G(s)\).  A critical pair contributes

\[
 2m_\gamma F(\gamma)G(\gamma).
 \tag{9}
\]

For an off-line representative write

\[
 F(s)=a+ib,
 \qquad
 G(s)=c+id.
\]

The four points in its orbit contribute

\[
 4m_s\Re(F(s)G(s))=4m_s(ac-bd).
 \tag{10}
\]

Equations (9)--(10) are exactly the three terms in (6).  Absolute
convergence of (8) applied to a diagonal, together with
\(|F(s)^2|=|F(s)|^2\), gives the separate square summability in (5).
Polarization then gives the asserted cross-term convergence. \(\square\)

## 3. The factorization uses the complete arithmetic source

Document 106.19 proved on the same domain that the joint physical-side
form is

\[
 QW(f,f)=\mathcal E_*(f)-c_*\|f\|_2^2-\mathcal A_\Delta(f),
 \tag{11}
\]

where \(\mathcal E_*\) contains every literal von Mangoldt atom and the
Gamma jump measure, \(c_*\) is the exact completed centering constant, and
\(\mathcal A_\Delta\) is the polar contribution.  Combining (7) and
(11) gives the requested global prime--Gamma--pole factorization:

\[
 \boxed{
 \mathcal E_*(f)-c_*\|f\|_2^2-\mathcal A_\Delta(f)
 =\|T_0f\|^2+\|T_+f\|^2-\|T_-f\|^2.}
 \tag{12}
\]

Thus the arithmetic atoms are not estimated separately.  Their complete
signed interference is retained until after the explicit formula has
formed the three global evaluation channels.

## 4. Quotient by the full Riemann radical

Let

\[
 \mathcal R_{\Xi}
 =\{f\in\mathcal D_{\mathrm{ev}}:F(s)=0
                    \text{ for every }s\in\mathcal Z\}.
 \tag{13}
\]

### Corollary 2 — Radical compatibility

The three maps \(T_0,T_+,T_-\) vanish on \(\mathcal R_\Xi\), so (12)
descends to a signed evaluation form on

\[
 \mathcal D_{\mathrm{ev}}/\mathcal R_\Xi.
 \tag{14}
\]

In the natural enlarged Weil domain used in 106.31, if \(K\) is Riemann's
kernel with \(\widehat K=\Xi\), then

\[
 T_\bullet K^{(2j)}=0
 \qquad(j=0,1,2,\ldots; \bullet=0,+,-).
 \tag{15}
\]

#### Proof

The first assertion is immediate from (5) and (13).  Moreover,

\[
 \widehat{K^{(2j)}}(z)=(-1)^jz^{2j}\Xi(z),
\]

which vanishes at every point of \(\mathcal Z\). \(\square\)

Consequently (12) passes the saturation test of 106.36 exactly.  There is
no positive local surplus left on any member of the infinite radical
family.

## 5. The negative channel is accessible

One might hope to complete (12) by proving an arithmetic absorption
estimate

\[
 \|T_-f\|^2
 \leq \|T_0f\|^2+\|T_+f\|^2+o(1)\|f\|_2^2
 \tag{16}
\]

on the moving semilocal complement.  The next theorem identifies exactly
when such an estimate can hold.

### Theorem 3 — No absorption in the presence of an off-line orbit

If an off-line orbit exists, there is a fixed real even
\(f\in\mathcal D_{\mathrm{ev}}\) such that

\[
 QW(f,f)<0.
 \tag{17}
\]

More precisely, for any chosen off-line representative \(s_0\) and every
\(\varepsilon>0\), one can choose \(f\) so that

\[
 |F(s_0)-i|<\varepsilon
 \tag{18}
\]

while the total absolute contribution of the other zero orbits is smaller
than \(\varepsilon\).  Hence the selected orbit contributes
\(-4m_{s_0}+O(\varepsilon)\) to (7).

#### Proof

This is the even interpolation construction of 106.11.  A fixed
Paley--Wiener damping factor gives absolute zero-sum control; a real even
interpolation polynomial sets the value at \(s_0\) to \(i\); high powers
of the damping factor suppress all nonselected orbits.  Substitution in
(10) gives the stated negative contribution and proves (17). \(\square\)

Because every exact radical vector is polarized-orthogonal to all Weil
tests, subtracting any finite or complete radical component from this
\(f\) leaves its Weil value unchanged.  Thus radical projection cannot
remove the negative channel.

### Corollary 4 — Exact terminal dichotomy

On the complete real even Weil domain,

\[
 \boxed{
 QW\geq0
 \quad\Longleftrightarrow\quad
 T_-=0
 \quad\Longleftrightarrow\quad
 \mathrm{RH}.}
 \tag{19}
\]

The forward implication uses Theorem 3.  If RH holds there are no
off-line orbits, so (7) is a sum of squares.  The last equivalence is the
definition of the off-line channel in (5).

## 6. Logarithmic-derivative candidate

A second natural candidate is the divided-difference kernel of the
centered logarithmic derivative of \(\Xi\).  Its Mittag--Leffler expansion
splits into the same orbit blocks as (8): a real pole gives a positive
rank-one evaluation block, whereas a nonreal reflected orbit gives one
positive and one negative real channel.  Therefore its Krein--Langer
factorization is unitarily the factorization (6), after completion of the
evaluation range.

This candidate is not new in the project.  The Herglotz version was audited
in Phase 16, the per-zero Krein--Langer atom and finite Loewner jets in
Phase 67, and the de Branges/Clark versions in Phases 5, 17 and 64.  Their
positivity is precisely the assertion that the negative channel in (7) is
absent.  They do not provide an independent estimate for that channel.

## 7. Consequence for the semilocal complement floor

For the finite semilocal operator, (12) is approached after the already
proved residual limits.  If RH fails, Theorem 3 supplies a fixed compactly
supported negative even test.  For all sufficiently large support windows
it can be made orthogonal to the moving near-radical without changing its
limiting negative Weil value.  Hence

\[
 \liminf_{L\to\infty}\beta_L^+<0.
 \tag{20}
\]

Conversely, either \(\beta_L^+\ge-o(1)\) or the stronger desired joint
floor excludes (20) and proves RH by 106.25.  The signed factorization
therefore localizes the remaining estimate exactly as

\[
 \boxed{
 \|T_-f\|^2
 \leq\|T_0f\|^2+\|T_+f\|^2+\varepsilon_L\|f\|_2^2,
 \quad f\in(q_L^+)^\perp\cap\mathcal D_L,
 \quad\varepsilon_L\longrightarrow0.}
 \tag{21}
\]

Theorem 3 shows that (21) is false in every off-line divisor model.  A proof
for the literal ordinary-prime source would therefore already exclude all
off-line zeros.

## 8. Verdict

The canonical signed normal form underlying the factorization requested in
106.36 has now been constructed and proved: it is (12).  It is exact,
retains every prime, Gamma and polar term jointly, and annihilates the
complete Riemann radical.

It does **not** satisfy the lower-bound clause (21) of 106.36, and therefore
is not yet the requested closing factorization.  Its negative channel is
not a removable bookkeeping artifact: an off-line zero makes that channel
independently accessible by a compact Paley--Wiener test.  Consequently no
further square completion, radical projection, or logarithmic-derivative
factorization can turn (12) into a positive identity without supplying a
new arithmetic theorem that rules out the negative evaluation channel.

The corrected surviving problem is not to find another factorization of
the completed form.  It is to prove the literal-prime absorption estimate
(21), or an equivalent semilocal estimate, by an input which distinguishes
the ordinary von Mangoldt weights from an abstract divisor with an
off-line orbit.
