# 106.66 — The ideal-cosh reference and compensated-measure gate

## Purpose and verdict

The full-kernel quotient form has so far been written as a prime--Gamma
jump energy minus one half of the polar variance.  For even multipliers,
both terms can be folded to the positive half-line and put in exactly the
same displacement coordinate.  The reference displacement density is

\[
\boxed{w_0(u)=2\cosh(u/2).}                          \tag{1}
\]

This note verifies the constant in (1), derives the resulting signed
measure, and tests whether one or two cumulative integrations of that
measure supply the missing sign.

The folding is exact and useful.  The primitive-sign closure is not.  The
Gamma singularity makes the first primitive meaningful only as a finite
part, hence only modulo an additive constant; the second is defined only
modulo an affine function.  Those ambiguities disappear in the final
pairing because every admissible displacement profile has two vanishing
jets at zero.  But the same profile necessarily has derivatives of both
signs: it is a positive bump which starts at zero and returns to zero at
infinity.  Thus a sign of either primitive alone cannot determine the
defect.  A diagnostic on an exact four-zero complement vector exhibits
large opposite contributions at both the one- and two-primitive levels.

## 1. Folding an even jump form

Let \(K,r\) be even and put

\[
J_u(r)=\int_{\mathbb R}K(x)K(x-u)
 |r(x)-r(x-u)|^2\,dx,qquad u>0.                    \tag{2}
\]

For a positive density \(w(u)\,du\), define

\[
\mathscr E_w(r)=\int_0^\infty J_u(r)w(u)\,du.       \tag{3}
\]

The same formulas hold for atoms by interpreting the kernels below as
pushforwards of the displacement measure.

### Theorem 1 — Exact same-side/crossing fold

For every even multiplier in the form domain,

\[
\boxed{
\begin{aligned}
\mathscr E_w(r)
=\int_0^\infty\!\int_0^\infty
 K(x)K(y)|r(x)-r(y)|^2
 \{w(|x-y|)+w(x+y)\}\,dx\,dy .
\end{aligned}}                                      \tag{4}
\]

Equivalently,

\[
\boxed{
\begin{aligned}
J_u(r)
={}&2\int_0^\infty K(y+u)K(y)
 |r(y+u)-r(y)|^2\,dy\\
&+\int_0^u K(x)K(u-x)
 |r(x)-r(u-x)|^2\,dx .
\end{aligned}}                                      \tag{5}
\]

#### Proof

In (2), write \(y=x-u\), so \(x>y\).  The regions \(x>y\ge0\) and
\(0\ge x>y\) give equal same-side terms by evenness; together they give
the first line of (5).  In the crossing region \(x\ge0\ge y\), put
\(x=a\), \(-y=b\), so \(a+b=u\).  This gives the second line of (5).
Finally integrate (5) in \(u\).  The same-side part covers the two
orientations of \(|x-y|\), and the crossing part is the level set
\(x+y=u\), proving (4).  \(\square\)

## 2. The exact ideal density for the polar variance

Recall

\[
d\mu_K(x)=\frac{h(x)K(x)}{c_K}\,dx,qquad
h(x)=\cosh(x/2),\qquad c_K=\frac12.                 \tag{6}
\]

For even \(r\), folding both variables in the usual identity

\[
\operatorname {Var}_{\mu_K}(r)
=\frac12\iint|r(x)-r(y)|^2\,d\mu_K(x)d\mu_K(y)     \tag{7}
\]

gives

\[
\frac12\operatorname {Var}_{\mu_K}(r)
=\frac1{c_K^2}\int_0^\infty\!\int_0^\infty
 K(x)K(y)h(x)h(y)|r(x)-r(y)|^2\,dx\,dy.            \tag{8}
\]

Since \(c_K=1/2\), the scalar kernel in (8) is \(4h(x)h(y)\).  The
addition formula gives

\[
\boxed{
4h(x)h(y)
=2\cosh\!\left(\frac{|x-y|}{2}\right)
 +2\cosh\!\left(\frac{x+y}{2}\right).}            \tag{9}
\]

Comparing (9) with (4) proves:

### Corollary 2 — Exact displacement representation of the threshold

\[
\boxed{
\frac12\operatorname {Var}_{\mu_K}(r)
=\int_0^\infty J_u(r)\,2\cosh(u/2)\,du.}           \tag{10}
\]

Thus the proposed reference density (1) has the correct factor exactly.

## 3. The compensated ordinary-prime--Gamma measure

Let

\[
g(u)=\frac{e^{-u/2}}{1-e^{-2u}},                    \tag{11}
\]

and define the signed measure

\[
\boxed{
d\sigma(u)=
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \delta_{\log n}(du)
 +\{g(u)-2\cosh(u/2)\}\,du.}                       \tag{12}
\]

Theorem 1 and Corollary 2 give the exact quotient identity

\[
\boxed{
\mathscr E_K(r)-\frac12\operatorname {Var}_{\mu_K}(r)
=\int_0^\infty J_u(r)\,d\sigma(u).}                \tag{13}
\]

No centering or asymptotic approximation occurs in (13).  The measure has
the useful alternative form

\[
\boxed{
d\sigma(u)
=e^{-u/2}d\{\psi(e^u)-e^u\}
 +\frac{e^{-5u/2}}{1-e^{-2u}}\,du.}                 \tag{14}
\]

Indeed, the prime atoms are \(e^{-u/2}d\psi(e^u)\), while

\[
g(u)-e^{-u/2}
=\frac{e^{-5u/2}}{1-e^{-2u}}.                       \tag{15}
\]

Equation (14) is the variance-coordinate analogue of the exact PNT
compensation in 106.18.  It keeps the actual signed PNT discrepancy and a
strictly positive, exponentially decreasing Gamma remainder.

## 4. Canonical finite-part primitives

The literal cumulative mass of \(g(u)du\) at zero is infinite.  Therefore
\(\sigma((0,U])\) is not a finite number.  The canonical Hadamard
finite-part primitive is

\[
\begin{aligned}
S_1(U)
:={}&\sum_{n\le e^U}\frac{\Lambda(n)}{\sqrt n}
 +G_1(U)-4\sinh(U/2),                               \tag{16}\\
G_1(U)
:={}&\operatorname {FP}\int_0^U g(u)\,du\\
={}&-\frac12\log\frac{1+e^{-U/2}}{1-e^{-U/2}}
 -\arctan(e^{-U/2})+\log2+\frac\pi4.              \tag{17}
\end{aligned}

Here the finite part subtracts the divergence
\(-\frac12\log\varepsilon\) at the lower endpoint.  A second primitive,
normalized by \(S_2(0)=0\), is

\[
\boxed{
\begin{aligned}
S_2(U)
={}&\sum_{n\le e^U}\frac{\Lambda(n)}{\sqrt n}
 (U-\log n)\\
&+G_2(U)-8\{\cosh(U/2)-1\},                       \tag{18}\\
G_2(U)
={}&\left(\log2+\frac\pi4\right)U
 -\sum_{k=0}^\infty
 \frac{1-e^{-(2k+1/2)U}}{(2k+1/2)^2}.
\end{aligned}}                                      \tag{19}
\]

The series follows from

\[
G_1(U)=\log2+\frac\pi4
 -\sum_{k=0}^\infty\frac{e^{-(2k+1/2)U}}{2k+1/2}.  \tag{20}
\]

Changing the finite-part convention adds a constant to \(S_1\) and an
affine function to \(S_2\).  This observation is essential: the pointwise
sign of a primitive is not convention invariant.

## 5. Integration by parts and the exact sign obstruction

For every smooth multiplier of at most exponential growth, the
double-exponential decay of \(K\) gives

\[
J_u(r),J_u'(r)\longrightarrow0\qquad(u\to\infty).  \tag{21}
\]

At zero, Taylor expansion gives

\[
\boxed{
J_u(r)=u^2\int_{\mathbb R}K(x)^2|r'(x)|^2\,dx
 +O(u^3),}                                          \tag{22}
\]

and hence \(J_0=J_0'=0\).  Finite-part integration by parts is therefore
independent of the constant/affine ambiguities and gives

\[
\boxed{
\int_0^\infty J_u\,d\sigma(u)
=-\int_0^\infty J_u'S_1(u)\,du
=\int_0^\infty J_u''S_2(u)\,du.}                   \tag{23}
\]

### Theorem 3 — One- and two-primitive signs are not sufficient

Let \(r\) be a nonconstant analytic multiplier for which (21) holds.
Then each of \(J_u'\) and \(J_u''\) assumes both positive and negative
values.  Consequently a pointwise sign statement for \(S_1\), or for
\(S_2\), cannot by itself determine the sign of (23).

#### Proof

Equation (22) gives \(J_u>0\) for all sufficiently small positive \(u\).
The positive kernel in (2) shows that \(J_u\ge0\), while (21) makes it
return to zero at infinity.  It must therefore rise somewhere and fall
somewhere, so \(J'\) has both signs.

If \(J''\ge0\) everywhere, then \(J'\) is increasing from \(J'(0)=0\),
which is incompatible with the fall to zero.  If \(J''\le0\) everywhere,
then \(J'\le0\) from the origin, incompatible with positivity of \(J\).
Thus \(J''\) also has both signs.  The two products in (23) consequently
have no sign from a sign of the primitive alone.  \(\square\)

This theorem does not rule out a stronger *alignment* identity between the
actual functions \(S_j\) and the constrained profiles \(J_u\).  It proves
that cumulative positivity/negativity without such an alignment is not a
closure mechanism.

## 6. Diagnostic on an exact complement vector

Use the exact mean-periodic vector from 106.62,

\[
r_4(x)=\frac{
 \cos(\gamma_1x)-2\cos(\gamma_2x)
 +2\cos(\gamma_3x)-\cos(\gamma_4x)}{\cosh(x/2)}.    \tag{24}
\]

Because every \(\gamma_j\) is a zero ordinate, \((hr_4)*K=0\) exactly.
The diagnostic script described below gives, with prime powers through the
last displacement on which the numerical theta kernel is active,

\[
\begin{array}{c|r}
\text{piece}&\text{value}\\ \hline
\displaystyle\int J_u\{g(u)-2\cosh(u/2)\}\,du
 &-0.0097790\\
\displaystyle\sum_n\Lambda(n)n^{-1/2}J_{\log n}
 &+0.0991174\\ \hline
\displaystyle\int J_u\,d\sigma(u)&+0.0893384
\end{array}                                         \tag{25}
\]

At the first-primitive level the rising and falling pieces contribute

\[
+0.622949\qquad\text{and}\qquad-0.533749,           \tag{26}
\]

while at the second-primitive level the two curvature signs contribute

\[
-5.69792\qquad\text{and}\qquad+5.78749.             \tag{27}
\]

Thus the positive answer in (25) results from substantial signed
interference, not from a sign-definite integrand after one or two
integrations.

For a separate arithmetic diagnostic, using all prime powers up to
\(2\cdot10^6\) gives on
\(10^{-5}\le U\le\log(2\cdot10^6)\)

\[
\begin{array}{c|cc}
&\min&\max\\ \hline
S_1(U)&-5.756480&-0.497246\\
S_2(U)&-17.576250&-0.0000626.
\end{array}                                         \tag{28}
\]

The finite-range signs in (28) are not interval certificates and are not
used as theorems.  Even if they held globally in this finite-part
normalization, Theorem 3 and (26)--(27) show why they would not prove
(13).

## 7. Reproduction and status

Run

```bash
cd 03-research/phase-106-global-modular-star-audit
python3 tools/signed_measure_primitive_gate.py \
  --limit 2000000 --points 40000 --dx 0.0005 --du 0.001
```

The script uses NumPy only and is diagnostic, not interval-certified.

The exact advance is the common-displacement formula (13) with the verified
reference density (1), together with the compensated arithmetic form (14).
The direct one- and two-primitive attacks do not close it.  A surviving
argument must prove a nonlocal alignment property of the complete
mean-periodic displacement profiles against \(\sigma\); primitive signs
alone discard precisely the oscillatory information that remains
force-bearing.
