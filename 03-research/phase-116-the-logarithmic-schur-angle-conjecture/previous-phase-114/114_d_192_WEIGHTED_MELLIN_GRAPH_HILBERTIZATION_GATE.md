# D.192 — Weighted Mellin/graph Hilbertizations and the closed-range gate

## Verdict

Weighted Mellin Hilbertizations exhibit an exact trilemma.

1. If the centrally normalized scaling involution is required to be the
   Hilbert adjoint, the spectral measure must be supported on the critical
   line.
2. On that line the completed Poisson multiplier is nonzero almost
   everywhere, so every scalar weighted \(L^2\) realization has dense range
   and zero Hausdorff cokernel.
3. A nonzero closed quotient can survive in an **analytic strip** Hilbert
   space only after the outer part of the completed zeta multiplier is
   absorbed into a graph norm.  The surviving quotient is then the model
   space of the inner factor, hence is determined exactly by the zero
   divisor in the strip.  Its scaling action is continuous but cannot be
   contractive in both directions unless all those zeros lie on the
   critical line.

Thus a noncritical graph norm can retain Meyer's quotient, but it does not
produce the missing row-D contraction.  The sharp lower bound

\[
 \max\{\|U_u\|,\|U_{-u}\|\}
 \ge \exp\bigl(|u|\,|\mathrm{Re}\,\rho-\tfrac12|\bigr) \tag{0.1}
\]

holds for every zero \(\rho\) represented in the quotient.  Two-sided
contractivity is therefore equivalent to the desired critical-line
statement.

This proves a precise no-go for all scalar weighted Mellin and standard
Hardy/graph completions satisfying the four simultaneous requirements:
closed Poisson range with nonzero quotient, continuous scaling, central
involution as a positive adjoint, and trace compatibility.  No paper file is
modified.

## 1. Scalar weighted Mellin spaces

Let \(\Omega\subset\{0<\mathrm{Re}\,s<1\}\) carry a positive measure
\(d\mu\), invariant under \(s\mapsto1-\bar s\), and let

\[
 H_w=L^2(\Omega,w(s)d\mu(s)),\qquad 0<w(s)<\infty\quad\mu\text{-a.e.} \tag{1.1}
\]

The centrally normalized scaling representation is

\[
 (U_uh)(s)=e^{u(s-1/2)}h(s),\qquad u\in\mathbb R.           \tag{1.2}
\]

Assume that the Tate involution is realized by the Hilbert adjoint, so in
particular

\[
 U_u^*=U_{-u}.                                             \tag{1.3}
\]

Since adjoints of multiplication operators are multiplication by the
complex-conjugate symbol, (1.3) implies

\[
 e^{u(\bar s-1/2)}=e^{-u(s-1/2)}\quad\text{for all }u       \tag{1.4}
\]

at almost every point in the support of \(w\,d\mu\).  Differentiating at
\(u=0\) gives

\[
 \boxed{\mathrm{Re}\,s=\tfrac12\quad\mu\text{-a.e.}}  \tag{1.5}
\]

This condition is independent of the choice of positive scalar weight.
No weight spread across a nontrivial strip can make the central involution
a positive Hilbert adjoint.

## 2. Closed range on the critical line

Allow different scalar weights in source and target,

\[
 H_+=L^2(w_+d\tau),\qquad H_-=L^2(w_-d\tau),                \tag{2.1}
\]

and let the completed Poisson operator be

\[
 Z_c=M_\Xi:H_+\longrightarrow H_-.                         \tag{2.2}
\]

The multiplication operator is bounded exactly when

\[
 |\Xi(\tau)|^2w_-(\tau)\le Cw_+(\tau)\quad\text{a.e.}      \tag{2.3}
\]

Because \(\Xi\ne0\) almost everywhere, its range is closed exactly when it
is bounded below:

\[
 |\Xi(\tau)|^2w_-(\tau)\ge c w_+(\tau)\quad\text{a.e.}     \tag{2.4}
\]

Equivalently, on the essential support,

\[
 c\le {|\Xi|^2w_-\over w_+}\le C.                         \tag{2.5}
\]

Under (2.5), division by \(\Xi\) sends every \(g\in H_-\) to an element
of \(H_+\):

\[
 \int |g/\Xi|^2w_+
 \le c^{-1}\int|g|^2w_-.                                  \tag{2.6}
\]

Thus \(Z_c\) is surjective and

\[
 \boxed{H_-/\mathrm{Ran}\,Z_c=0.}                     \tag{2.7}
\]

If (2.4) fails, the range is nonclosed.  With equal weights this failure is
unavoidable because the completed Gamma factor makes \(|\Xi(\tau)|\to0\)
as \(|\tau|\to\infty\), and \(\Xi\) also vanishes at the critical zeros.

The isometric graph choice

\[
 w_+=|\Xi|^2w_-                                             \tag{2.8}
\]

is therefore exact but vacuous for the cokernel: it turns \(Z_c\) into an
onto isometry.  A scalar critical-line graph norm cannot retain Meyer's odd
object.

## 3. Why a surviving quotient must be analytic or singular

For a multiplication operator nonzero almost everywhere between full
scalar \(L^2\) spaces, the only possible Hilbert cokernel is supported on a
set where the multiplier vanishes with positive measure.  The zeros of
\(\Xi\) are discrete and hence have measure zero.  A nonzero quotient must
therefore add one of:

* atoms or distributional jets at the zeros;
* an analytic constraint which makes division by \(\Xi\) fail at its zero
  divisor.

The first option explicitly installs the zero locations.  The second is the
Hardy/model-space mechanism analyzed next.  This proves that ordinary
weights alone cannot solve the problem.

## 4. The best noncritical analytic graph construction

Fix \(0<a<1/2\) and the symmetric strip

\[
 S_a=\{s:|\mathrm{Re}\,s-\tfrac12|<a\}.                \tag{4.1}
\]

Let \(H^2(S_a)\) be the Hardy space with norm

\[
 \|h\|_a^2=\int_{\mathbb R}
 \bigl(|h(\tfrac12-a+i\tau)|^2+|h(\tfrac12+a+i\tau)|^2\bigr)d\tau. \tag{4.2}
\]

Use the entire completed function (including the elementary polar
polynomial) and factor it in the strip as

\[
 \Xi=B_aO_a,                                               \tag{4.3}
\]

where \(B_a\) is its inner Blaschke factor, with multiplicities, and
\(O_a\) is outer (a harmless singular-inner factor may be included in
\(B_a\)).  Absorb \(O_a\) into the source graph norm:

\[
 \|f\|_{+,a}:=\|O_af\|_{H^2(S_a)}.                         \tag{4.4}
\]

Then multiplication by \(\Xi\) is, after \(f\mapsto O_af\), the isometry

\[
 M_{B_a}:H^2(S_a)\longrightarrow H^2(S_a),                 \tag{4.5}
\]

with closed range.  Its quotient is the positive model space

\[
 \boxed{K_{B_a}=H^2(S_a)\ominus B_aH^2(S_a).}              \tag{4.6}
\]

This is a genuine nonzero Hilbert cokernel whenever \(\Xi\) has a zero in
\(S_a\).  It is also the unique standard way of removing the nonclosed
outer range while retaining the analytic divisibility obstruction.

But (4.6) makes the dependence precise: \(B_a\) is the canonical product of
the zeros of \(\Xi\) in \(S_a\).  Equivalently, \(K_{B_a}\) is spanned
densely by the reproducing-kernel jets attached to those zeros.  The graph
weight has removed the zero-free outer part; the entire surviving quotient
is the spectral divisor.

The construction (4.3)--(4.6) may be defined from \(\Xi\) without listing
its zeros, but using its positive model metric as the source of the Hodge
sign is still spectral: inner--outer factorization reveals that the metric
is built precisely from the zero divisor whose horizontal position row D
must constrain.

## 5. Scaling on the strip quotient

Multiplication by

\[
 E_u(s)=e^{u(s-1/2)}                                      \tag{5.1}
\]

is a bounded invertible multiplier of \(H^2(S_a)\), with

\[
 \|M_{E_u}\|\le e^{a|u|}.                                \tag{5.2}
\]

It commutes with \(M_{B_a}\), so it descends to the quotient (4.6).  Thus
the noncritical graph Hilbertization does preserve a continuous full
scaling group and the support filtration of integrated compact tests.

Let \(\rho\) be a zero of \(\Xi\) in \(S_a\), and let \(k_\rho\) denote
the quotient evaluation kernel (with the corresponding derivative kernels
for higher multiplicity).  The adjoint action satisfies

\[
 U_u^*k_\rho=\overline{E_u(\rho)}k_\rho.                   \tag{5.3}
\]

Therefore

\[
 \|U_u\|\ge |E_u(\rho)|
 =e^{u(\mathrm{Re}\,\rho-1/2)}.                       \tag{5.4}
\]

Applying (5.4) to \(u\) and \(-u\) proves (0.1).  In particular,

\[
 \boxed{
 \|U_u\|\le1\text{ and }\|U_{-u}\|\le1\ \forall u
 \quad\Longrightarrow\quad
 \mathrm{Re}\,\rho=\tfrac12\ \forall\rho\in S_a.} \tag{5.5}
\]

Conversely, two-sided contraction for an invertible group is unitarity.
Thus even this optimal model quotient does not furnish an unconditional
contraction; its failure is measured exactly by the horizontal displacement
of the zero divisor.

## 6. Central reflection is Krein, not Hilbert, off the line

The anti-linear reflection

\[
 (\mathcal Jh)(s)=\overline{h(1-\bar s)}                    \tag{6.1}
\]

swaps the two boundary lines in (4.2) and is antiunitary.  Algebraically,

\[
 \mathcal J U_u\mathcal J=U_{-u}.                          \tag{6.2}
\]

However \(U_u^*\ne U_{-u}\) unless \(U_u\) is unitary.  The boundary
moduli are \(e^{-au}\) and \(e^{au}\), so the Hilbert norm (4.2) sees an
expansion in one chart and a contraction in the other.  Functional-equation
reflection supplies a Krein/dual pairing between the charts; it does not
turn their sum norm into a positive invariant metric.

This is the analytic-strip version of the distinction in D.191 between the
Tate transpose and a \(C^*\)-adjoint.

## 7. Jets, trace, and the simultaneous no-go

The two Tate jets \(\widehat a(0),\widehat a(1)\) remain continuous on the
original test core and are preserved by convolution.  They can be added as
the two finite polar summands without affecting Sections 1--6.  They do not
change the odd model quotient or the bound (5.4).

The integrated scaling operators of compactly supported smooth tests have
rapidly decaying eigenvalue symbols on the quotient kernels, so their
formal spectral trace is the zero sum with multiplicities.  Identifying
this trace with Meyer's nuclear trace requires a trace-compatible comparison
of the model completion with the Fréchet quotient.  Even granting that
comparison, if the central transpose were the Hilbert adjoint then

\[
 B_{\rm nuc}(a,a)
 =-\mathrm{Tr}\,\bigl(\mathscr Q_-(a)
          \mathscr Q_-(a)^*\bigr)\le0                      \tag{7.1}
\]

for primitive \(a\), which is row D.  Hence trace compatibility does not
weaken the gate; it makes it exact.

Combining the preceding sections gives:

> **Theorem 7.1 (weighted Mellin/graph no-go).**  No scalar weighted Mellin
> \(L^2\) completion can simultaneously have a nonzero closed Meyer
> cokernel and realize central inversion as the positive Hilbert adjoint.
> The standard analytic graph repair has a nonzero closed model quotient,
> continuous scaling, support propagation and jets, but its quotient metric
> is the metric of the inner zero divisor and its two-sided contractivity is
> equivalent to critical-line location of that divisor.

This theorem does not say a nonspectral A--B geometric polarization is
impossible.  It says such a polarization cannot be obtained merely by
choosing a scalar Mellin weight or the canonical inner--outer graph norm.

## 8. Remaining admissible construction

The next construction must differ essentially from scalar spectral
weighting.  It would need a matrix- or category-valued positive metric
coming from the A--B periodic/Künneth geometry, transported to \(V\) before
inner--outer factorization, and it must satisfy an independent conservation
law forcing

\[
 U_u^*GU_u=G                                             \tag{8.1}
\]

without defining \(G\) from \(B_a\), \(|\Xi|^{-1}\), or reproducing kernels
at zeros.  If such \(G\) is trace-compatible, D.191 then turns it directly
into the row-D negative square.

## 9. Finite-section certificate

The companion script `114_d_192_weighted_mellin_graph_verify.py` verifies:

1. weighted adjoint equals inverse scaling only on \(\mathrm{Re}\,s=1/2\);
2. absorbing \(|\Xi|\) makes a diagonal multiplier an onto isometry and
   kills the quotient;
3. inverse norms diverge without that absorption;
4. a finite model quotient carrying spectral points \(\rho_j\) satisfies
   the lower bound (0.1), and two-sided contraction fails for every
   off-critical \(\rho_j\).

This tests the exact functional-analytic implications, not the location of
actual zeta zeros.
