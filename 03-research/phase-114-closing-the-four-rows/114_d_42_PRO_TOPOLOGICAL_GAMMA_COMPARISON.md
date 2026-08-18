# D.42 — Pro-topological comparison theorem for the Gamma line

## 1. Statement

Retain the two-chart interpretation of D.40--D.41.  Give `L_gamma^0` the
intrinsic graph topology consisting of:

1. the Schwartz seminorms of `u_+` on every compact vertical substrip of
   `Re(s)>=1/2`;
2. the Schwartz seminorms of `u_-` on every compact vertical substrip of
   `Re(s)<=1/2`.
The finite principal-part coordinates at `0,-2,...,-2N` and
`1,3,...,1+2N` are not additional seminorms.  They are continuous
consequences of the opposite-chart seminorms.  Indeed, if `a=-2n` and
`b=1+2n`, then

\[
 \operatorname{res}_{s=a}u_+
 =\bigl(\operatorname{res}_{s=a}\gamma\bigr)u_-(a),
 \qquad
 \operatorname{res}_{s=b}u_-
 =\bigl(\operatorname{res}_{s=b}\gamma^{-1}\bigr)u_+(b).           \tag{1.1}
\]

Evaluation on a fixed vertical line is continuous for the Schwartz
seminorms.  Thus every finite residue projection is continuous, and the
pro-residue system is already represented by the two-chart graph topology.
No inverse limit of arbitrary residue sequences occurs.

The right- and left-chart spaces are Frechet.  Choose
`0<epsilon<1/2`.  On the overlap
`1/2-epsilon<Re(s)<1/2+epsilon`, `gamma` and its inverse are holomorphic
vertical-Schwartz multipliers.  The opposite chart therefore supplies the
same seminorms on this overlap, and the gluing condition is closed there.
Analytic continuation then supplies the global meromorphic pair.  The
resulting graph space and its two primitive kernels are therefore Frechet.

Then the characteristic map of D.41 is a topological isomorphism of
Frechet spaces onto Meyer's closed range:

\[
 \boxed{
 \sigma_\zeta:\mathcal L_\gamma^0
   \xrightarrow{\sim}Z\mathcal H_\cap.}             \tag{1.2}
\]

The target carries Meyer's closed-range topology.  Consequently the same
map is an isomorphism after embedding both sides as constant objects in
the exact pro-category, and all finite residue projections commute with
it.  This is stronger than a merely levelwise pro-statement.  No infinite
sequence space of arbitrary residues is required.

## 2. Continuity from the Meyer range to the two charts

Meyer's closed-range theorem gives a continuous inverse

\[
 Z^{-1}:Z\mathcal H_\cap\longrightarrow\mathcal H_\cap.           \tag{2.1}
\]

For `h=Zf`, Mellin transformation gives on the initial convergence strip
and then meromorphically

\[
 u_+(s)=\frac{\widehat h(s)}{\zeta(s)}=\widehat f(s).               \tag{2.2}
\]

The Fourier--Mellin identity and the functional equation give

\[
 u_-(s)=\frac{\widehat h(s)}{\zeta(1-s)}
 =\gamma(s)^{-1}\widehat f(s)
 =\widehat{J\mathcal Ff}(s).                         \tag{2.3}
\]

Indeed,

\[
 \widehat{\mathcal Ff}(s)=\gamma(s)\widehat f(1-s),
 \qquad
 \widehat{Jg}(s)=\widehat g(1-s),
\]

so

\[
 \widehat{J\mathcal Ff}(s)
 =\gamma(1-s)\widehat f(s)
 =\gamma(s)^{-1}\widehat f(s).
\]

Both maps

\[
 f\longmapsto\widehat f|_{\operatorname{Re}s\ge1/2},
 \qquad
 f\longmapsto\widehat{J\mathcal Ff}|_{\operatorname{Re}s\le1/2} \tag{2.4}
\]

are continuous for the half-strip Schwartz seminorms.  This is precisely
the pair of estimates in Meyer's characterization of `H_+`; additive
Fourier transform is continuous on the Schwartz source and Tate inversion
exchanges the two weighted strips.

Taylor expansion at zero gives the exact residue formulas

\[
 \operatorname{res}_{s=-2n}\widehat f(s)
 =\frac{f^{(2n)}(0)}{(2n)!},
 \qquad
 \operatorname{res}_{s=1+2n}\widehat{J\mathcal Ff}(s)
 =-\frac{(\mathcal Ff)^{(2n)}(0)}{(2n)!}.            \tag{2.5}
\]

Every finite list is a continuous functional of the Schwartz topology.
Combining this fact with
(2.1)--(2.4) proves continuity of

\[
 h\longmapsto(u_+,u_-)                              \tag{2.6}
\]

for the intrinsic graph topology.  Formula (1.1) simultaneously shows that
all finite residue projections are continuous.

The primitive values can be computed without a finite-part convention.
Since all functions are even and Meyer's Fourier transform uses
`exp(2 pi ixy)`,

\[
 \begin{aligned}
 u_+(1)&=\widehat f(1)
       =\int_0^\infty f(x)\,dx
       =\tfrac12\mathcal Ff(0),\\
 u_-(0)&=\widehat{J\mathcal Ff}(0)
       =\widehat{\mathcal Ff}(1)
       =\int_0^\infty\mathcal Ff(x)\,dx
       =\tfrac12 f(0).
 \end{aligned}                                      \tag{2.7}
\]

Thus `f(0)=mathcal Ff(0)=0` is exactly
`u_-(0)=u_+(1)=0`, and (2.6) lands in `L_gamma^0`.  Equivalently, at zero
the condition kills the possible residue of `u_+`, while at one it kills
the possible residue of `u_-`, as in D.41.

## 3. Continuity of the inverse

Conversely, let `(u_+,u_-) in L_gamma^0`.  Mellin inversion of `u_+` on a
right vertical line produces a function `f` in the right weighted
Schwartz space.  Equation

\[
 u_-=\gamma^{-1}u_+                                 \tag{3.1}
\]

and the Fourier--Mellin formula say that `J mathcal Ff` belongs to every
required left weighted Schwartz space.  Meyer's intersection
characterization therefore gives

\[
 f\in\mathcal H_+.                                  \tag{3.2}
\]

The two value conditions in `L_gamma^0`, by (2.7), give
`f(0)=mathcal Ff(0)=0`, hence `f in H_cap`.  This proves algebraically that
(2.6) is bijective, with inverse

\[
 (u_+,u_-)\longmapsto Zf=\sigma_\zeta(u_+,u_-)      \tag{3.3}
\]

Both spaces are Frechet: the source by the closed graph construction in
Section 1, the target by Meyer's closed-range theorem.  The forward
bijection (2.6) is continuous by Section 2.  The Frechet open mapping
theorem therefore makes (3.3) continuous automatically.  This proves
(1.2).  The proof uses the two-chart graph topology directly; it does not
infer an isomorphism in a pro-category from unrelated levelwise
bijections.

## 4. Consequence

D.42 closes the topological comparison in the intrinsic two-chart Frechet
topology and hence also after passage to constant objects in the exact
pro-category.  It does not identify arbitrary residue sequences with one
independently chosen Frechet sequence space: the allowed residues are the
continuous opposite-chart evaluations (1.1), so no such identification is
needed for the range--cokernel triangle.

Together with D.41, the odd object is now source-defined as the cokernel of
a scaling-equivariant morphism of Frechet Gamma lines (and therefore of
their constant pro-objects), with reflection
carrying the weight-one Tate twist.  The ordinary critical-boundary Hilbert
completion still has zero cokernel.  The only remaining row-D construction
is therefore the faithful positive, centrally unitary and trace-compatible
completion of this **nuclear/pro cokernel**, not another correction of the
Gamma divisor or of the two primitive moments.
