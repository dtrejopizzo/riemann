# 106.39 — The signed-flow and radical-isometry constraint

## Purpose

Document 106.38 rewrites the full ordinary-prime--Gamma energy as the
square norm of a complete gradient \(\mathcal G\), without discarding any
theta index or crossing interval.  The desired inequality is therefore

\[
 \|D_\mu r\|^2\leq \|\mathcal G r\|^2.                 \tag{1}
\]

This note determines the form that a direct source-side proof of (1) must
have.  The infinite Riemann-radical family forces the closing map to be an
isometry on an infinite-dimensional source subspace.  Consequently every
positive stochastic construction must pass simultaneous equality tests
for all those vectors; the lossy path constructions already present in the
project fail that test.  After removing the forced isometric block, the
remaining problem is one complementary flow equation.

No zero location is assumed below.

## 1. The two gradient spaces

Let

\[
 \mathscr H_\mu=L^2_{\rm a}(\mu_K\otimes\mu_K),
 \qquad
 (D_\mu r)(x,y)=\frac{r(x)-r(y)}2,                    \tag{2}
\]

where the subscript denotes the antisymmetric part.  Let

\[
 \mathscr H_{\rm src}
 =\mathscr H_\Gamma\oplus\mathscr H_{\rm div}
  \oplus\mathscr H_{\rm frac}\oplus\mathscr H_{\rm ctr}               \tag{3}
\]

be the four weighted edge spaces in 106.38, and let

\[
 \mathcal G r
 =G_\Gamma r\oplus G_{\rm div}r
  \oplus G_{\rm frac}r\oplus G_{\rm ctr}r.             \tag{4}
\]

Their normalizations give

\[
 \|D_\mu r\|^2=\frac12\operatorname {Var}_{\mu_K}(r),
 \qquad
 \|\mathcal G r\|^2
 =\mathscr E_\Gamma+\widetilde{\mathscr E}_p
  +\mathscr X_{\rm frac}+\mathscr X_{\rm ctr}.          \tag{5}
\]

The Gamma fibers are the pairs \((x,x-u)\), \(u>0\).  The divisor and
fractional fibers are \((x,x-\log n)\), and the central fibers are
\((x,\log n-x)\).  All their measures are the literal positive measures
displayed in 106.38.

## 2. The canonical flow equation

Put

\[
 \mathscr R_G=\overline{\operatorname {ran}\mathcal G}.
\]

Since the Gamma measure is positive for every displacement \(u>0\),
\(\mathcal G r=0\) implies that \(r\) is constant almost everywhere.
Consequently \(D_\mu r=0\).  The rule

\[
 C_0(\mathcal G r):=D_\mu r                              \tag{6}
\]

is therefore a well-defined densely defined linear map from
\(\mathscr R_G\) to \(\mathscr H_\mu\).  It is the unique map on
\(\operatorname {ran}\mathcal G\) which can close the diagram

\[
 \begin{CD}
  \mathcal D/\mathbb C @>{\mathcal G}>> \mathscr R_G\\
  @V{D_\mu}VV @VV{C_0}V\\
  \mathscr H_\mu @= \mathscr H_\mu.
 \end{CD}                                                  \tag{7}
\]

Thus the requested construction is not an arbitrary search for a map.
It is the problem of proving that the canonical signed flow (6) is
closable and contractive:

\[
 \boxed{\|C_0v\|\leq\|v\|
        \quad(v\in\operatorname {ran}\mathcal G).}       \tag{8}
\]

When (8) holds, \(C_0\) extends to a contraction \(C\) on
\(\mathscr R_G\), and (1) follows.  Conversely, (1) is exactly (8).

The weak form of (6) is the signed-flow equation

\[
 \boxed{
 \langle C_0\mathcal G r,\Phi\rangle_{\mathscr H_\mu}
 =\frac12\iint(r(x)-r(y))\overline{\Phi(x,y)}
             \,d\mu_K(x)d\mu_K(y).}                    \tag{9}
\]

Any explicit construction must rewrite the right side as one joint
pairing against the Gamma, divisible-theta, fractional-theta and central
gradients.  Formula (9), rather than four separate lower estimates, is the
coefficient equation for that construction.

## 3. Exact isometry forced by the Riemann radical

For \(j\geq0\), let

\[
 r_j=K^{(2j)}/K.                                         \tag{10}
\]

The full-kernel identity and
\(\widehat {K^{(2j)}}(z)=(-1)^jz^{2j}\Xi(z)\) give

\[
 \|D_\mu r_j\|=\|\mathcal G r_j\|.                      \tag{11}
\]

Polarizing the vanishing Weil form gives, for every finite linear
combination \(r=\sum_{j=0}^J a_jr_j\),

\[
 \|D_\mu r\|=\|\mathcal G r\|.                          \tag{12}
\]

Define the radical-gradient space

\[
 \mathscr M=\overline{\operatorname {span}}
 \{\mathcal G r_j:j\geq0\}\subset\mathscr R_G.          \tag{13}
\]

Equations (6) and (12) prove the following requirement.

### Theorem 1 — Radical isometry

If the canonical flow is contractive, then

\[
 \boxed{C_0^*C_0v=v\qquad(v\in\mathscr M).}             \tag{14}
\]

In particular, the closing contraction must be an isometry on the
infinite-dimensional space \(\mathscr M\).

#### Proof

Equation (12) says \(\|C_0v\|=\|v\|\) on a dense subspace of
\(\mathscr M\).  For a contraction,
\(I-C_0^*C_0\geq0\).  Its quadratic form vanishes on that dense
subspace, and hence its positive square root vanishes there.  Closure gives
(14). \(\square\)

## 4. Saturation test for positive path constructions

Consider a proposed construction in which each target pair \((x,y)\) is
represented by a probability distribution \(P_{x,y}\) of source paths,
and \(C\) is obtained by averaging the signed sum of the source edge
values along the path.  The unweighted sum of exact increments along any
path telescopes to \(r(x)-r(y)\); averaging the path sums itself therefore
causes no loss.  The possible loss enters when the path sum is bounded by
the weighted source-edge norm (or when several edge allocations are
averaged) by Cauchy--Schwarz/Jensen.

### Theorem 2 — Radical saturation test

A positive path construction can satisfy (6) and \(\|C\|\leq1\) only if
every Cauchy--Schwarz and Jensen defect in its norm proof vanishes on
\(\mathcal G r_j\), simultaneously for every \(j\geq0\).  In particular,
any proposed allocation which is strict on \(\mathcal G r_1\) cannot close
the inequality.

#### Proof

Write the norm proof as the exact identity

\[
 \|v\|^2-\|Cv\|^2=\mathfrak d(v),\qquad \mathfrak d(v)\geq0,             \tag{15}
\]

where \(\mathfrak d\) is the sum (or monotone limit) of the
Cauchy--Schwarz and Jensen defects introduced by the allocation.  If the
construction closes (6), Theorem 1 gives
\(\|C\mathcal G r_j\|=\|\mathcal G r_j\|\).  Substitution in (15) gives

\[
 \mathfrak d(\mathcal G r_j)=0\qquad(j\geq0).             \tag{16}
\]

Every summand in the defect is nonnegative, so each of them must vanish.
For \(j=1\), this is precisely the equality condition for the weighted
edge increments of \(r_1=K''/K\).  Therefore a single strictly positive
defect on that vector contradicts (16). \(\square\)

The theorem does not by itself exclude every positive path construction:
an exact electrical allocation could conceivably saturate all of (16).
It does exclude the lossy canonical-path, Efron--Stein and reduced-theta
allocations already tested in 106.32 and 106.36, because their displayed
positive remainders are strict on \(r_1\).  Any new positive construction
must first pass the simultaneous saturation conditions (16); otherwise
cross-tower signs must be introduced before the norm is estimated.

## 5. The remaining coefficient problem

Let \(U:\mathscr M\to\mathscr H_\mu\) be the isometry fixed by

\[
 U(\mathcal G r_j)=D_\mu r_j.                            \tag{17}
\]

Every admissible solution has the block form

\[
 C=U P_{\mathscr M}+C_\perp P_{\mathscr M^\perp},
 \qquad \|C_\perp\|\leq1,                               \tag{18}
\]

subject to the exact interpolation equations

\[
 C_\perp P_{\mathscr M^\perp}\mathcal G r
 =D_\mu r-U P_{\mathscr M}\mathcal G r.                 \tag{19}
\]

Thus all freedom is confined to the orthogonal complement of the complete
radical-gradient space.  Equation (19) is the precise signed compensation
problem.  A proof must construct its coefficients from the joint
von-Mangoldt--Gamma--theta source and establish

\[
 \boxed{
 \|D_\mu r-U P_{\mathscr M}\mathcal G r\|
 \leq\|P_{\mathscr M^\perp}\mathcal G r\|}              \tag{20}
\]

without using a zero-location statement.

The projection localizes the unknown block but does not weaken the
inequality.  Polarization of the radical identity gives, for every
\(v=\mathcal G r\) and \(m\in\mathscr M\),

\[
 \langle D_\mu r,Um\rangle=\langle v,m\rangle.           \tag{20a}
\]

Therefore

\[
 U^*D_\mu r=P_{\mathscr M}\mathcal G r.                 \tag{20b}
\]

The corresponding orthogonal decompositions are

\[
 \begin{aligned}
 \|D_\mu r\|^2
 &=\|P_{\mathscr M}\mathcal G r\|^2
   +\|D_\mu r-UP_{\mathscr M}\mathcal G r\|^2,\\
 \|\mathcal G r\|^2
 &=\|P_{\mathscr M}\mathcal G r\|^2
   +\|P_{\mathscr M^\perp}\mathcal G r\|^2.
 \end{aligned}                                           \tag{20c}
\]

Consequently

\[
 \boxed{\text{(20)}\quad\Longleftrightarrow\quad
        \|D_\mu r\|\leq\|\mathcal G r\|.}              \tag{20d}
\]

Shorting subtracts the same exact radical square from both sides.  It
identifies where the unknown contraction acts, but it does not reduce the
strength of the all-prime estimate.

## 6. The radical span is not complete

A tempting closure of (20) would be to prove that the centered functions
\(r_j\) are dense in \(L^2(\mu_K)\).  Then \(U\mathscr M\) would contain
the full polar gradient range and the right side of (19) would vanish.
This closure is false, and the obstruction can be written exactly.

Let \(z\) be any zero of \(\Xi\), in the frequency normalization
\(\widehat K=\Xi\), and put

\[
 e_z(x)=\frac{\cos(zx)}{h(x)},\qquad h(x)=\cosh(x/2).     \tag{21}
\]

The function \(e_z\) belongs to \(L^2(\mu_K)\): the possible exponential
growth of \(\cos(zx)\) is dominated by the double-exponential decay of
\(K\).  For every \(j\geq0\),

\[
 \begin{aligned}
 \langle e_z,r_j\rangle_{L^2(\mu_K)}
 &=\frac1{c_K}\int_{\mathbb R}
   \cos(\overline z x)K^{(2j)}(x)\,dx\\
 &=\frac{(-1)^j\overline z^{\,2j}}{c_K}
   \Xi(\overline z)=0.                                  \tag{22}
 \end{aligned}
\]

Here conjugation invariance of the zero divisor gives
\(\Xi(\overline z)=0\).  Thus:

### Proposition 3 — Explicit complement modes

For every zero \(z\) of \(\Xi\),

\[
 \boxed{0\ne e_z\perp
 \overline{\operatorname {span}}\{r_j:j\geq0\}
 \quad\text{in }L^2(\mu_K).}                            \tag{23}
\]

Consequently radical completeness cannot prove (20).  The unresolved
complement is not an abstract closure artifact: it contains an explicit
mode for every zero.  Real \(z\) gives a critical-line mode; a nonreal
\(z\) gives the off-line channel which the absorption estimate must
exclude.

## 7. Status

The source-side problem has now been localized to one non-overcounting
coefficient equation, (19), with the exact isometric block (17) fixed in
advance.  Theorems 1--2 exclude the previously tested lossy positive path
averages.  The unknown block acts only on \(\mathscr M^\perp\); it may be
an exact electrical allocation or a globally signed flow, but in either
case it must satisfy (20).  Identity (20d) records that this localization
is equivalent to the original all-prime inequality.

The construction and norm estimate for \(C_\perp\) are not proved here.
Proposition 3 shows why completing the radical span cannot supply them:
the missing block contains exactly the zero-evaluation modes.  Controlling
that block from the joint ordinary-prime source remains equivalent to the
absorption estimate.
