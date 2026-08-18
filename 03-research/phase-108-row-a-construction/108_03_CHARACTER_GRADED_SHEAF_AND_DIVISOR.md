# 108.03 -- The character-graded family of DC potentials, its divisor, and a global principal line

## 1. What is being built, and its relation to 107_237/107_240

108.02 classifies the character-covariant test data as the one-parameter
family \(f_s(r)=c\,r^s\), \(s\in\mathbb R\), \(c\in\mathbb R\). This note
builds the corresponding potentials, defines their divisor, and identifies
inside them a canonical nonzero **global principal line** -- the object
108.04 needs to decide whether 107_240 Theorem C's well-posedness complaint
is resolved.

The formula (2.1) of 107_237, \(U_f(x,y)=\int_A^B
f(\lambda)\max(y-\lambda x,0)\,d^*\lambda\), does **not** converge for
\(f=f_s\): \(f_s\) is not compactly supported, and \(\max(y-\lambda x,0)\)
does not decay, so the integral diverges at \(\lambda\to0\) or
\(\lambda\to\infty\) for every real \(s\). This is expected: 108.02
Theorem 4.1 shows character-covariance is incompatible with compact
support, so the superposition formula (2.1), built for compactly supported
\(f\), is simply not the right tool here.

What survives is 107_237's *defining* relation, not its superposition
formula: \(U_f\) is, primarily, the unique-mod-affine solution of
\(u_f''(r)=f(r)/r\) (107_237 (2.3), Theorem 2.1). That ODE has an elementary
closed-form solution for every \(s\), with no convergence issue anywhere on
\((0,\infty)\). Formula (2.1) is then understood as one *construction
method* for that solution, valid on the sub-locus of compactly supported
\(f\); it is not the definition. The graded family below is obtained by
solving the defining ODE directly.

## 2. The graded potentials

For \(s\notin\{0,-1\}\), define

\[
 U_s(x,y):=\frac{y^{s+1}x^{-s}}{s(s+1)}
 =x\cdot u_s(r),\qquad
 u_s(r):=\frac{r^{s+1}}{s(s+1)},\qquad r=\frac yx .
 \tag{2.1}
\]

For the two degenerate weights,

\[
 U_0(x,y):=y\log(y/x)-y,
 \qquad
 U_{-1}(x,y):=x\log(x/y).
 \tag{2.2}
\]

### Proposition 2.1 (these are exactly the potentials of \(f_s\))

For every \(s\in\mathbb R\), \(u_s''(r)=r^{s-1}=f_s(r)/r\) with \(f_s(r)=r^s\).

**Proof.** Direct differentiation. For \(s\notin\{0,-1\}\):
\(u_s'(r)=r^s/s\), \(u_s''(r)=r^{s-1}\). For \(s=0\): \(u_0(r)=r\log r-r\),
\(u_0'(r)=\log r\), \(u_0''(r)=1/r=r^{-1}\). For \(s=-1\):
\(u_{-1}(r)=-\log r\), \(u_{-1}'(r)=-1/r\), \(u_{-1}''(r)=1/r^2=r^{-2}\).
\(\square\)

By 107_237 Theorem 2.1, \(U_s\) so defined is *the* correspondence
potential of \(f_s\), unique modulo affine functions of \((x,y)\); (2.1)-(2.2)
simply pick one representative in each class.

## 3. Exact Frobenius/chart-change covariance

### Proposition 3.1

For \(m,n\in\mathbb N^\times\) (equally, \(\mathbb Q_+^\times\)) and
\(s\notin\{0,-1\}\),

\[
 U_s(mx,ny)=n^{1+s}m^{-s}\,U_s(x,y)
 \tag{3.1}
\]

**exactly**, with no affine correction. For \(s\in\{0,-1\}\),

\[
 U_0(mx,ny)=n\,U_0(x,y)+ny\log(n/m),
 \qquad
 U_{-1}(mx,ny)=m\,U_{-1}(x,y)+mx\log(m/n),
 \tag{3.2}
\]

i.e. (3.1) holds **modulo an affine (in fact linear) correction** in the
two degenerate weights.

**Proof.** Direct substitution into (2.1)-(2.2); carried out in full in the
verifier. For (2.1): \(U_s(mx,ny)=(ny)^{s+1}(mx)^{-s}/(s(s+1))
=n^{s+1}m^{-s}\,y^{s+1}x^{-s}/(s(s+1))=n^{1+s}m^{-s}U_s(x,y)\). For (2.2):
\(U_0(mx,ny)=ny\log(ny/(mx))-ny=ny[\log(n/m)+\log(y/x)]-ny
=n[y\log(y/x)-y]+ny\log(n/m)=nU_0(x,y)+ny\log(n/m)\), and symmetrically for
\(U_{-1}\). \(\square\)

The correction terms in (3.2) are linear in \((x,y)\), hence affine, hence
invisible to \(f=u''\) (107_240 Lemma B). So in every case -- exactly for
generic \(s\), modulo the same affine ambiguity 107_237/107_240 already
work with for \(s\in\{0,-1\}\) -- \(U_s\) transforms under the two-variable
chart map \(T_{m,n}\) by the scalar character

\[
 \chi_s(m,n):=n^{1+s}m^{-s} .
 \tag{3.3}
\]

This is precisely one weight-space of the representation
\(f\mapsto n\,\rho_{m,n}f\) that 107_240 SS4 (4.1) identified as the correct
home for \(D_f\) once literal scalar descent was closed (107_240 Theorem
2.1/3.1). Nothing here contradicts that no-go: 107_240 shows the *entire*
\(C_c\)-module cannot be compressed to one scalar line; here we exhibit,
for each fixed \(s\), an candid rank-one sub-line \(\mathcal L_s\) on which
the representation genuinely **is** scalar -- at the cost, per 108.02, of
leaving \(C_c\) entirely.

## 4. The graded family as an equivariant line for each weight

### Definition 4.1

\[
 \mathcal L_s:=\mathbb R\cdot U_s\subset\{\text{DC potentials on the
 universal positive chart}\}/\text{affine},
 \qquad
 \mathcal G:=\{\mathcal L_s\}_{s\in\mathbb R}.
\]

By 108.02 Theorem 4.1, \(\mathcal L_s\) is exactly the space of potentials
of character-covariant test data of weight \(s\): it is one-dimensional,
and (3.1)/(3.2) exhibit it as a representation of the chart-change monoid
\(\{T_{m,n}\}\) (equally \(\mathbb Q_+^\times\)-equivariant after 107_237
(4.1)-style extension) via the scalar character \(\chi_s\) of (3.3).

We do **not** claim \(\mathcal G\) satisfies the gluing axioms of a sheaf on
an open cover of the quotient topos in the technical sense; each
\(\mathcal L_s\) is verified here only as a global, chart-covariant object
on the single universal positive chart that 107_237-107_240 already work
on. Calling \(\mathcal G\) the "graded sheaf" (108_00 SS5's language) is
shorthand for this weaker, but explicit and nonzero, structure.

## 5. Divisor

### Definition 5.1

For \(c\,U_s\in\mathcal L_s\), \(c\neq0\), define

\[
 \mathrm{div}(cU_s):=c\cdot r^{s-1}\,\frac{dr}r
 \qquad\text{on }(0,\infty),
 \tag{5.1}
\]

the current with density \(c\,r^{s-1}\) with respect to \(d^*r\), i.e. the
distributional angular curvature of \(cU_s\) via 107_237 (2.3)/107_238
SS1's Hessian formula.

### Proposition 5.2 (div is injective on \(\mathcal G\), and every value is nonzero)

For every \(s\), \(\mathrm{div}:\mathcal L_s\to\{\text{currents on
}(0,\infty)\}\) is injective, and \(\mathrm{div}(cU_s)=0\) iff
\(c=0\).

**Proof.** \(r^{s-1}\) is a nowhere-vanishing continuous function on
\((0,\infty)\) for every \(s\), so \(c\,r^{s-1}\equiv0\) as a distribution
iff \(c=0\); linearity gives injectivity. \(\square\)

This is the graded-category analogue of 107_240 Theorem C (\(f\mapsto D_f\)
injective); it holds by the same mechanism (the second derivative
recovers \(f\) exactly), extended without incident to the non-compact
category.

Unlike the \(D_f\) of 107_237 (built from compactly supported \(f\), with
finite total curvature mass on the balanced Weil test space), the currents
(5.1) have infinite mass on \((0,\infty)\) for every \(s\) (\(\int_0^\infty
r^{s-1}\,d^*r=\infty\)) since the density never decays. They remain
perfectly well-defined as *distributions*: paired against any compactly
supported test form they give a finite number. What they cannot do is
represent a compactly-supported source current; this is the same
compact-support/character-covariance trade-off 108.02 already forces.

## 6. The global principal line

Classically, a principal divisor is the divisor of a global rational
function, i.e. a global section that is genuinely invariant (fixed, not
merely covariant, under the structure group). In \(\mathcal G\), "genuinely
invariant" is exactly weight \(s=0\), the trivial character \(\chi_0\equiv1\)
of (3.3).

### Definition 6.1

\[
 \boxed{
 \mathrm{Prin}(\mathcal G):=\mathrm{div}(\mathcal L_0)
 =\mathbb R\cdot\Big(\frac{dr}r\Big)
 \subset\{\text{currents on }(0,\infty)\}.}
 \tag{6.1}
\]

### Theorem 6.2

\(\mathrm{Prin}(\mathcal G)\) is a one-dimensional, nonzero subspace,
canonically and explicitly constructed, with generator the curvature current
of \(U_0(x,y)=y\log(y/x)-y\).

**Proof.** \(\mathcal L_0\) is one-dimensional (108.02 Theorem 4.1 at
\(s=0\)); \(\mathrm{div}\,\) is injective on it (Proposition 5.2) and
its image is spanned by the density \(r^{-1}\), which is nonzero.
\(\square\)

### 6.1 An explicit candor check: \(U_0\) is not a classical rational function

\(U_0(x,y)=y\log(y/x)-y\) is transcendental, not algebraic/rational in the
classical sense; this should not be read as a defect. 107_237's entire
program replaces finite-PL/rational Cartier divisors by DC potentials
precisely because continuous \(f\) cannot be represented rationally
(107_237 Theorem 2.1). "Principal" in \(\mathcal G\) is defined
*intrinsically*, as "divisor of a weight-\(0\) (Frobenius-invariant)
section," which is the correct transplant of the classical notion into this
category -- it is not claimed to coincide with, or resemble, a divisor of a
rational function on a scheme.

### 6.2 Scope of the claim

\(\mathrm{Prin}(\mathcal G)\) is a *witness*: an explicit, nonzero
candidate for a global principal subspace, constructed without reference to
any zero of \(\xi\), any Li coefficient, or the sign of the Weil form. It is
**not** claimed to be:

* the full space of global principal divisors on the quotient topos (larger
  categories of global sections, beyond the character-graded family
  \(\mathcal G\), are not ruled out or constructed here);
* contained in, or unrelated to, \(\mathrm{rad}\,I_\partial\) (107_240
  Theorem D) -- that question is 108.04's, and 108.04 explicitly declines to
  test it; 108.10 explains why the test is not currently even well posed.

## 7. Scope

Proved here:

* Proposition 2.1: \(U_s\) (2.1)-(2.2) solves the defining ODE for \(f_s\)
  exactly, for every \(s\in\mathbb R\);
* Proposition 3.1: exact scalar chart covariance for \(s\notin\{0,-1\}\),
  covariance modulo an explicit affine correction at \(s\in\{0,-1\}\);
* Proposition 5.2: div is injective on every weight space, extending
  107_240 Theorem C to the graded category;
* Theorem 6.2: an explicit nonzero one-dimensional global principal line.

Not claimed:

* full sheaf-theoretic gluing on the quotient topos;
* completeness of \(\mathcal G\) as "all" global sections;
* any relation between \(\mathrm{Prin}(\mathcal G)\) and
  \(I_\partial\) (108.04, 108.10).

## 8. Verifier

`108_03_character_graded_sheaf_and_divisor.py`:

1. confirms Proposition 2.1 (\(u_s''=r^{s-1}\)) numerically by finite
   differences, for a bank of \(s\) including \(0\) and \(-1\);
2. confirms Proposition 3.1's exact and mod-affine covariance laws by
   direct substitution, checking the correction term in the degenerate
   cases is exactly linear in \((x,y)\) (fits a plane with zero residual);
3. confirms Proposition 5.2 (injectivity: distinct \(c\) give
   distinguishable sampled densities; the density is nonvanishing);
4. confirms Theorem 6.2: constructs \(\mathrm{Prin}(\mathcal G)\)
   explicitly and checks it is nonzero and one-dimensional (spanned by
   \(1/r\)) by sampling;
5. prints `VERDICT: YES` for "an explicit nonzero global principal line is
   constructed in the graded category," with all claims above it labeled
   proved/verified as appropriate.
