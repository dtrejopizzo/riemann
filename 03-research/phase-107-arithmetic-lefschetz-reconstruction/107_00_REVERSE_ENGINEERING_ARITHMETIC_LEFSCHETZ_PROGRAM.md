# 107.00 — A reverse-engineering program for an arithmetic Lefschetz surface

## 1. Correction of the target

The arithmetic Hodge-index inequality is not missing inside classical
Arakelov geometry.  Faltings--Hriljac identifies the admissible
self-intersection of a degree-zero divisor on a regular proper arithmetic
surface with minus twice its Neron--Tate height.  Yuan--Zhang and related
work extend the arithmetic Hodge-index theorem to broad adelic settings.

This statement has a strict categorical scope.  A hypothetical
\(\mathrm{Spec}\,\mathbb Z\times_{\mathbb F_1}
\mathrm{Spec}\,\mathbb Z\), a scaling topos or a foliated dynamical
space is not automatically an arithmetic surface in that category.  For
such a new object the Hodge-index theorem must either be transported by a
comparison theorem or proved anew.

The missing structure precedes that theorem.  One needs:

1. an arithmetic surface or surface-like object carrying the relevant
   cycles;
2. a Frobenius/scaling correspondence on it;
3. an arithmetic Lefschetz formula whose fixed-point intersections are
   the prime, Gamma and polar terms of the explicit formula;
4. a comparison placing the resulting primitive metrized divisors in a
   category where an existing arithmetic Hodge-index theorem applies.

Thus the research direction is not to prove positivity directly.  It is
to construct the object to which known positivity applies.

There is an unavoidable dichotomy:

* **classical Arakelov branch:** the Hodge sign is available, but no known
  surface carries a Frobenius/Lefschetz intersection distribution equal
  to the zeta explicit formula;
* **absolute/dynamical branch:** prime orbits and a Lefschetz distribution
  may become geometrically meaningful, but the existing arithmetic Hodge
  theorem does not automatically apply.

The program must construct one side and a bridge to the other.  It may
not assume that both structures coexist.

## 2. Reverse engineering: discovery order versus proof order

The proposed discovery order is:

\[
 \text{intersection data}
 \longrightarrow
 \text{correspondences}
 \longrightarrow
 \text{global surface}.
 \tag{1}
\]

This is sensible engineering: the required output fixes the interfaces
that the correspondence and the surface must implement.  It is not the
logical proof order.  In the final theorem the surface must exist before
its intersection numbers are accepted as geometric numbers.

There is also a strict source rule:

> No definition may use a zero of \(\xi\), a Li coefficient, the sign of
> the Weil form, or a positive part extracted from that form.

The intersection distribution must be built from

\[
 \Lambda(p^k),\qquad \log p,\qquad p^{-k/2},
 \qquad \Gamma_{\mathbb R},\qquad s(s-1),
 \tag{2}
\]

and from geometric operations.  The zero side may enter only afterward,
through the already established explicit formula used as a comparison
theorem.

## 3. The final commuting diagram

The whole program is designed to construct the solid arrows in

\[
 \begin{CD}
 f @>{\text{source construction}}>> \overline D_f
    @>{\text{arithmetic intersection}}>>
       -\overline D_f^{\,2}\cdot\overline H_T\\
 @. @VV{\text{Lefschetz comparison}}V
    @VV{\text{explicit formula}}V\\
 @. Z_f @>>> \mathcal Q_W(f).
 \end{CD}
 \tag{3}
\]

The required identities are

\[
 D_f\cdot H_T=0,
 \qquad
 -\overline D_f^{\,2}\cdot\overline H_T=\mathcal Q_W(f).
 \tag{4}
\]

If \(\overline D_f\) lies in the dimension-two Yuan--Zhang domain,
then

\[
 \overline D_f^{\,2}\cdot\overline H_T\leq0
 \quad\Longrightarrow\quad
 \mathcal Q_W(f)\geq0.
 \tag{5}
\]

Weil positivity for every admissible \(f\) then gives RH.  The force of
the program is entirely in constructing (3)--(4), not in reproving (5).

## 4. Design principle: finite support on a proper global model

Every logarithmically compact test \(f\) sees only finitely many prime
powers.  The construction must exploit this without truncating the
arithmetic base:

\[
 \mathrm{supp}\,f\subset[-T,T]
 \quad\Longrightarrow\quad
 D_f\text{ has finite nonarchimedean support on a regular proper model }
 \mathcal X_T/\mathrm{Spec}\,\mathbb Z.
 \tag{6}
\]

Here \(\mathcal X_T\) is global over the whole base.  It is not
\(\mathrm{Spec}\,\mathbb Z\) with the places \(p>T\) deleted, and it
is not a nonproper truncation.  The word ``finite'' refers only to the
support of \(D_f\), or to a finite-type proper model carrying it.

The arithmetic Hodge-index theorem is applied separately to each such
global proper model.  No cofinal lower-semicontinuity of an indefinite
form is used.  A pro-object may organize compatibility, but the sign for
each compactly supported test is proved before, and independently of,
any limit.

This is the main defense against the signature-blindness obstructions
already established in the program.

# Part 0. Mandatory function-field calibration

## 4.1 Work package 0 — Recover Weil's proved case

Before constructing anything new over \(\mathbb Z\), the complete
interface must specialize to a smooth projective curve
\(C/\mathbb F_q\).  This is a positive control, not an analogy.

The calibration object is the genuine surface \(C\times C\), with its
vertical and horizontal rulings, diagonal \(\Delta\), and graphs
\(\Gamma_{F^n}\) of Frobenius.  The source package must recover, using
the same operations proposed over \(\mathbb Z\),

\[
 \deg_1\Gamma_{F^n}=1,
 \qquad
 \deg_2\Gamma_{F^n}=q^n,
 \tag{6a}
\]

\[
 \Gamma_{F^n}\cdot\Delta
 =\#C(\mathbb F_{q^n}),
 \tag{6b}
\]

and the closed-point Euler expansion

\[
 \log Z_C(u)
 =\sum_{x\in|C|}\sum_{k\geq1}
   \frac{u^{k\deg x}}{k}.
 \tag{6c}
\]

Critical balancing of a closed point of degree \(d\) must produce
\(q^{-kd/2}\), just as the proposed arithmetic row produces
\(p^{-k/2}\).  The connected Euler projector must retain primitive
closed points and their iterates.  Finally, primitive projection and the
classical Hodge index on \(C\times C\) must give

\[
 \left|q^n+1-\#C(\mathbb F_{q^n})\right|
 \leq2gq^{n/2}.
 \tag{6d}
\]

The required dictionary is:

| Source package | Function-field realization |
|---|---|
| polar rulings | \(C\times\{x_0\}\), \(\{x_0\}\times C\) |
| connected return symbol | primitive closed point of \(C\) |
| root-cover composition | composition of Frobenius graphs |
| balanced coefficient | \(q^{-kd/2}\) |
| connected Euler projector | logarithm of the Euler product |
| diagonal trace | fixed-point intersection (6b) |
| primitive negative form | Hodge index on \(C\times C\) |

### Stop rule 0

> If the definitions intended for \(\mathbb Z\) do not specialize to
> (6a)--(6d), the reverse-engineering program stops.  No exceptional
> construction is introduced only for \(\mathbb Z\).

### Deliverable

**Paper 0: Function-field calibration of the source correspondence
package.**  It must rederive the complete
Frobenius--Lefschetz--Hodge chain using the same categorical operations
proposed for the arithmetic case.  Merely citing Weil's theorem is not a
calibration.

### Scope limitation of the calibration

Paper 0 validates the interface

\[
 \text{correspondence}\longrightarrow\text{Lefschetz number}
 \longrightarrow\text{primitive Hodge sign}.
\]

It does **not** validate the finite-support mechanism of Section 4.
Weil's proof uses the complete proper surface \(C\times C\); truncating it
to closed points of degree at most \(T\) destroys properness and removes
the hypotheses of the classical Hodge-index theorem.  No artificial
function-field analogue of \(\mathcal X_T\) will be introduced merely to
make that part of the diagram commute.

# Part I. Reconstruct the intersection distribution

## 5. Work package I-A — The free arithmetic divisor module

### Objective

Construct a source-defined graded divisor module generated by

\[
 F_{\mathrm v},\quad F_{\mathrm h},\quad
 Z_{p,k},\quad Z_\infty,\quad \Delta,
 \tag{7}
\]

where \(F_{\mathrm v},F_{\mathrm h}\) are the two polar rulings,
\(Z_{p,k}\) is the connected \(k\)-fold return at \(p\),
\(Z_\infty\) is the archimedean fiber, and \(\Delta\) is the diagonal.

The module must retain the factorization decoration.  Categorical
composition and Euler disjoint union are different operations; the first
Eulerian idempotent acts only on the latter.

### Existing input

The following pieces are already proved:

* the hyperbolic polar plane;
* genuine CRT fiber products and multiplicative degrees;
* relative root torsion \(\log p\);
* the balanced incidence coefficient \(p^{-k/2}\);
* Eulerian extraction of connected prime-power returns;
* the Gamma determinant fiber, polar factor and matched finite part.

### Deliverable

A presentation by generators and relations of a finite-support module
\(\mathrm{Div}_{\mathrm{EF}}\), together with degree, transpose and
connected-trace maps.

### Stop tests

1. The relations must not identify connected and disconnected returns.
2. Transpose must be defined before connected extraction.
3. The construction must fail for Davenport--Heilbronn at the point where
   the Euler orbit structure is requested.

### Current branch state

The source rule of Section 2 remains the only admitted **legacy**
grammar inside Work Package I-A.  The local branch decision is now:

1. under the current local target retaining
   \((\text{Kodaira symbol},c_p,\text{reduction label})\), the legacy
   finite local row is closed by no-go;
2. the residue-sensitive `A5` packet
   \[
   (p,v(c_4),v(c_6),v(\Delta),v(j),\mathbf a_{\min}\bmod 32),
   \]
   is rejected: `107_144` gives integral admissible changes between
   minimal equations of the same real curve that change the packet;
3. because the same curve and its transformed equation have identical
   zeta/Euler data, the `A5` packet is not definable from zeta alone;
4. `107_144` upgrades the legacy obstruction from a target-table
   collision to a degree-zero Neron/Arakelov calculation: the same
   valuative/Euler packet supports different rational component
   correction functors on `20a1@2` and `36a4@2`.

Thus the current local state is:

\[
\text{legacy row (c): closed for the full degree-zero local target;}
\]
\[
\text{A5: rejected as noninvariant and non-source-defined.}
\]

Reopening I-A now requires a new invariant Galois-sensitive source
channel, or a theorem proving that every realized Phase 107 divisor is
component-trivial.  No current artifact supplies either one.

## 6. Work package I-B — Local derived intersection lines

### Objective

Replace scalar intersection guesses by determinant lines.  At each finite
place construct a local Deligne/determinant pairing

\[
 \langle Z_m,Z_n\rangle_p
 \tag{8}
\]

whose canonical section has norm controlled by the derived intersection
of the cyclotomic strata.

For distinct strata the local order must recover Apostol's resultant:

\[
 \frac1{\varphi(n)}\log
 |\mathrm{Res}(\Phi_m,\Phi_n)|
 =\begin{cases}
 \log p,&m/n=p^a,\\
 0,&\text{otherwise}.
 \end{cases}
 \tag{9}
\]

The output is a line with a section, not yet a signed real number.  This
leaves room for the archimedean metric to define the diagonal coherently.

### Deliverable

A finite-place determinant-line functor satisfying symmetry,
base-change, projection formula and compatibility with derived fiber
products.

### Stop tests

1. Mixed ratios must have trivial local line and prime-power ratios must
   have order exactly \(\log p\).
2. The diagonal must remain an excess-intersection line; it must not be
   filled with the cardinality value \(n\).
3. The functor must be compatible with transpose and composition on the
   decorated category.

### Operational consequence

At the current workspace state, both previously recorded local
continuations are closed:

1. the legacy determinant-line route attached to the Section 2 source
   grammar is closed for the full local degree-zero target by the exact
   component-correction no-go of `107_144`;
2. the `A5` branch is closed because its mod-32 minimal-equation residue
   does not descend under integral admissible coordinate changes and is
   not definable from zeta data.

Any future local continuation must therefore introduce a different,
coordinate-invariant source grammar and rerun the mandatory falsifiers
before it is admitted.

## 7. Work package I-C — The archimedean Green metric

### Objective

Use the already constructed Gamma--polar determinant to metrize the
global determinant line.  The metric must supply:

* the Gamma contribution;
* the pole and the two polar rulings;
* the diagonal self-intersection;
* cancellation of the common cutoff by a product formula.

The desired local-to-global object is

\[
 \overline{\langle D,E\rangle}
 =\left(\langle D,E\rangle_{\rm fin},
        \|\cdot\|_{\Gamma,\rm pol}\right).
 \tag{10}
\]

### Deliverable

An arithmetic Deligne pairing on finite-support divisors whose degree is
the complete prime--Gamma--polar distribution, with the diagonal obtained
from the same metrized line as the cross terms.

### Stop tests

1. Paired-cutoff independence must be exact.
2. Rescaling the metric may not leave an arbitrary additive constant.
3. The self-pairing must not be automatically negative for every possible
   divisor configuration; the divisor location must remain visible.
4. The scalar case \(s_a(z)=z-a\) must not make the metric independent of
   the moved divisor.

## 8. Milestone I — The intersection-number paper

The first paper is complete only when the following theorem is proved:

> **Finite-support intersection theorem.**  For every finite set of
> prime-power returns and every admissible finite-support coefficient
> vector, the source construction produces a metrized determinant line
> with a finite, symmetric intersection number.  Its finite local terms
> are (9), its archimedean term is the Gamma--polar determinant, and its
> diagonal is obtained from the same Green metric.

No Hodge sign is claimed in this paper.  Its value is the construction of
the numbers from one coherent theory.

# Part II. Reconstruct the Frobenius correspondence

## 9. Work package II-A — The decorated correspondence category

### Objective

Construct a category \(\mathrm{Corr}_{\mathrm{EF}}\) whose
morphisms are decorated spans of root/cyclotomic strata.  It must have:

\[
 \Gamma_u\circ\Gamma_v=\Gamma_{u+v},
 \qquad
 \Gamma_u^t\text{ defined},
 \qquad
 \deg(\Gamma_{k\log p})=p^k,
 \tag{11}
\]

where the first law is written in logarithmic time.  The decoration must
distinguish one \(k\)-fold primitive return from \(k\) disconnected
one-fold returns.

### Deliverable

Composition, transpose, degree, diagonal and connected cyclic trace,
proved compatible with the determinant pairing of Part I.

### Stop tests

1. Every composition square must be a genuine derived fiber product.
2. The Eulerian projector may act on cyclic traces but not on Rosati
   multiplication.
3. The category must retain divisor positions, not merely determinants or
   homotopy classes.

## 10. Work package II-B — Suspension to an arithmetic flow

### Objective

Construct a suspension/groupoid with a scaling flow \(\vartheta_t\) such
that the primitive closed orbits are

\[
 C_p=\mathbb R_+^\times/p^{\mathbb Z},
 \qquad \ell(C_p)=\log p.
 \tag{12}
\]

The newer Connes--Consani absolute arithmetic curve already supplies
these local periodic orbits and a common archimedean phase.  The task is
not to reconstruct the local circles, but to assemble them into the
global correspondence category while preserving their determinant
lines.

### Deliverable

A source-defined scaling action whose closed-orbit return category is
\(\mathrm{Corr}_{\mathrm{EF}}\).

### Stop tests

1. A disjoint union of prime circles is insufficient: it must possess a
   global degree-one cohomology and a diagonal class.
2. Averaging over continuous holonomies may not replace geometry by an
   absolutely continuous weight.
3. The zero-winding complement may not be used as though it were an ideal.

## 11. Work package II-C — The arithmetic Lefschetz formula

### Objective

For a compactly supported test \(f\), form a correspondence

\[
 Z_f=\int_{\mathbb R}\widehat f(t)\,[\Gamma_t],dt
      -c_f[\Delta].
 \tag{13}
\]

Prove from fixed-point intersections, not by definition, that

\[
 Z_f\cdot\Delta
 =\mathcal L_{\rm prime+Gamma+polar}(f).
 \tag{14}
\]

The classical explicit formula may then identify (14) with the spectral
zero distribution.  This is where the zeros enter the theorem, not the
construction.

### Deliverable

A Lefschetz/supertrace theorem for the constructed flow, including all
prime powers, Gamma and pole terms with the correct signs.

### Stop tests

1. If (14) is imposed as the definition of the trace, the package fails.
2. The formula must distinguish zeta from Davenport--Heilbronn before any
   appeal to zeros.
3. Prime, Gamma and pole terms must be obtained jointly; separate absolute
   estimates are not accepted.

## 12. Milestone II — The correspondence paper

The second paper is complete when the category and the flow exist and
the fixed-point calculation derives the arithmetic side of the explicit
formula.  At that point one has constructed the analogue of Frobenius and
its Lefschetz numbers without yet constructing the global surface.

# Part III. Reconstruct the global surface

## 13. Work package III-A — The universal finite models

### Objective

For each support bound \(T\), construct a regular proper arithmetic model
\(\mathcal Y_T/\mathrm{Spec}\,\mathbb Z\) of relative dimension two
containing all cycles with
\(k\log p\leq T\), together with two projections, a diagonal and the
correspondences of Part II.  The model remains proper over the complete
arithmetic base; only the divisor support is finite.

The models may form a compatible pro-system, but every divisor \(D_f\)
must already live on one global proper \(\mathcal Y_T\).  No sign may be
deduced from a limit of the models.

### Candidate construction directions

1. derived self-products of the Connes--Consani absolute arithmetic curve;
2. Gamma-ring/Segal-site charts glued from the cyclotomic derived
   intersections;
3. a moduli stack of rank-one groups with rigidification, using the
   Connes--Consani Jacobian as the Picard object;
4. finite classical arithmetic surfaces mapping to that stack and
   carrying the required finite-support divisors.

The fourth direction is especially important: it could place each test
divisor directly inside classical Arakelov geometry even if the universal
\(\mathbb F_1\) square remains a stack or a pro-object.

### Current foundational constraints

`107_147` closes one mass-functional branch for the first direction.
If the Euclidean projective tensor norm on the square is modeled by the
trace norm on \(M_2(\mathbb Z)\), primitive rank-one boundary matrices
force a superlogarithmic number of generators.  More precisely, for
\(n_k\) the product of \(k\) distinct primes congruent to \(1\pmod4\),
the absolute dimension is at least \(2^{k+1}\).  Thus this trace-norm
model is not compatible with linear Riemann--Roch growth under
\(n\simeq e^{\deg D}\).  `107_150` corrects the tensorial fork:
the projective tensor norm inherited from CC's \(\ell^1\) factors is
entrywise \(\ell^1\), so the linear-growth theorem of `107_146`
applies to it.  The trace no-go closes only the Euclidean branch.
Neither result alone constructs the square sheaf.

`107_151` supplies the missing formal middle-cohomology operation
for any three-term Cech complex realized in bounded submodules of
Eilenberg--MacLane modules.  It defines \(H^1\) as the cocycle module
with the image relation retained as a tolerance relation, proves
functoriality and isomorphism invariance, and recovers ordinary
cohomology when the image is a subgroup.  The remaining square problem
is therefore geometric rather than quotient-theoretic: construct the
Cech terms and differentials of the absolute square inside that
abelian ambient category.

`107_152` and `107_153` close the naive way of producing
that ambient category from the 2026 absolute stalk
\(\mathbb F_1[T^{\mathbb Z[1/p]_+}]\).  Its ordinary monoid-ring
linearization has infinite integer dimension already in radius one.
More strongly, every nonconstant additive submodule stable under the
invertible local Frobenius has infinite rank.  Therefore denominator
truncations cannot simultaneously retain Frobenius and finite CC
dimension; a viable Cech lift must be non-free/derived or encode
Frobenius between finite levels rather than internally at each level.

`107_154` constructs that finite-level alternative locally.
Writing every nonzero exponent uniquely as \(c p^j\), it gives bounded
levels cut by \(c\le A\) and \(|j|\le R\).  Frobenius and its inverse
act isometrically from level \(R\) to level \(R+1\); on the square the
two ruling actions commute, and the filtered colimit is the full
absolute stalk.  The next existence condition is stabilization of
divisor-controlled Cech cohomology under enlargement of these levels,
together with descent between primes.  This sentence describes the
finite coefficient-mass candidate only; 107_228 proves below that
stabilization is not an admissible condition for the full periodic
Scaling-Site \(H^0\).

`107_155` gives the exact stabilization criterion: for the
coefficient-mass modules of `107_154`, \(H^0(D)\) stabilizes if
and only if the union of monomial rays admitted by \(D\) is finite.
Thus finite admitted monomial support is the exact condition for that
candidate to stabilize.  It is a criterion, not yet a theorem that the
published divisor sheaf should satisfy; 107_228 eventually rejects
that universal requirement.

`107_156` separates the two support coordinates using the
published description of \(\Theta^*(\mathcal O)\).  Zariski geometry
already forces a section to vanish outside finitely many primes.  It
does not bound the local sequence \(p^{-k}\), all of which remains in a
bounded real interval and cannot be generated at finite denominator
depth.  At this stage this appeared to demand a divisor-derived
Frobenius-depth bound.  The published periodic RR normalization checked
in 107_228 shows instead that arbitrary depth is load-bearing.

`107_157` corrects the finite chart algebra used earlier in
`107_15` and `107_18`.  The visible orders form the
divisor lattice of \(L_T=\prod p^{\lfloor T/\log p\rfloor}\), not a
finite multiplicative monoid.  Its multiplication is partial and maps
outside products to larger levels.  This removes a hidden contradiction
and makes the rooted cyclotomic charts compatible with the pro-Frobenius
system of `107_154`.

Because \(L_T=\mathrm{lcm}(1,\ldots,\lfloor e^T\rfloor)\), its
logarithm is asymptotic to \(e^T\), and even its divisor set is
intractable from \(T=5\).  All later finite-level constructions must
therefore retain the exponent vector \((K_p(T))_p\) and must not
enumerate \(L_T\), its divisors, or its roots.

`107_158` records the resulting local stabilization corollary
for the rooted sector actually used by the candidate charts:
\[
 X_T^\vee=(1/L_T)\mathbb Z/\mathbb Z.
\]
It is finite of order \(L_T\), with exact \(p\)-depth
\(\lfloor T/\log p\rfloor\).  Thus the rooted/cyclotomic \(H^0\) sector
passes `107_155`; the remaining row-(a) problem is global descent
and representability, not local rooted-support growth.  This conclusion
applies only to the finite rooted coordinate, not to the full slope
sector of \(H^0(D)\).

`107_159` closes the remaining discrete descent for that
coordinate.  The finite rooted groups include canonically as \(T\)
grows, their frame duals project, and Chinese remainder glues the local
\(p\)-primary factors.  The limits recover
\(\mathbb Q/\mathbb Z\) and \(\widehat{\mathbb Z}\).  What remains is
representability and metric/intersection descent, not compatibility of
the finite rooted labels.

`107_160` proves representability of this discrete coordinate.
After correcting packet labels to exact order, the finite regular
arithmetic scheme
\[
 \mathcal R_T=\coprod_{n\mid L_T}\mathrm{Spec}\,\mathbb Z[\zeta_n]
\]
normalizes the visible root scheme and represents every primitive rooted
label once.  The missing representability is now confined to the
dynamical and archimedean coordinates needed to raise relative dimension
from zero to two.

`107_161` tests the cheapest remaining descent mechanism directly
against the published CC pullback sheaf.  Its generic stalk is zero,
its sections are finite-support prime families, and restriction deletes
coordinates.  Consequently distinct prime stalks carry no nonzero
transition and their values extend independently.  Prime-chart
restrictions alone therefore cannot supply cross-prime incidence or
intersection data.  An additional global adelic/archimedean gluing
morphism is necessary; the result does not obstruct such an extension.

`107_162` rejects the naive attempt to use the Abel--Jacobi fiber
product with only the inverse-image sheaf from the base curve.  Such
functions are fiber-saturated, so on
\(C_p\times C_p\) they cut neither the diagonal nor any Frobenius graph.
The topological pullback therefore needs the relative two-coordinate
sheaf already suggested by the Newton-polygon square of the Arithmetic
Site; base divisor modules alone cannot define intersections.

`107_163` gives an abelian finite-level lift of that published relative
correspondence.  At the stalk \(H_p=\mathbb Z[1/p]\), the CC map of
weight \((n,m)\) lifts to
\[
 \Lambda_{n,m}(X^aY^b)=T^{na+mb}.
\]
Its full kernel is generated by all Frobenius roots
\(X^{m/p^k}-Y^{n/p^k}\), while at depth \(R\) the single deepest root
generates the exact kernel.  The ideals form a strict directed system,
and the maps are contractive for the CC \(\ell^1\) mass.  Thus diagonal
and rational correspondences now live in the abelian ambient category
required by `107_151`; their global Cech descent remains open.

`107_164` closes one tempting but invalid globalization.  No nonzero
additive map exists from an idempotent semimodule to an abelian group;
more sharply, imposing equality of formal supports with the same upper
Newton polygon kills every monomial basis vector.  Hence the lift of
`107_163` cannot descend additively to the reduced Newton square.  The
cohomological source must retain enriched unreduced support, while
Newton reduction is only a non-additive tropical shadow.  Applying the
2022 integer dimension directly to reduced polygons is forbidden.

`107_165` constructs the minimal such enrichment globally.  The free
semiring \(\mathbb N[M]\), \(M=\mathbb Z^2\), tropicalizes
equivariantly onto the unreduced and reduced squares, while its
Grothendieck completion \(\mathbb Z[M]\) carries the bounded
\(\mathbb S[\pm1]\)-modules and exact kernels of `107_163`.  Signed
cancellation changes the Newton shadow, as required by `107_164`.
This supplies a coefficient object, not yet a cohomology theory.

`107_166` rules out taking ordinary derived invariants of the raw
monoid-action topos.  For \(r\) visible primes, its two rulings give the
polynomial ring on \(2r\) generators, and the constant module has
\[
 \mathrm{Ext}^k\cong\bigwedge^k\mathbb Z^{2r}.
\]
The amplitude is therefore \([0,2r]\), unbounded with \(T\), rather
than the surface amplitude \([0,2]\).  A genuine geometric three-term
complex is required; manual truncation is not admissible.

`107_167` identifies where the correct amplitude does occur.  The
published compact mapping torus \(\Gamma(p)\) has the de Rham
cohomology of a circle, and Kunneth gives
\[
 \dim H^\bullet(\Gamma(p)\times\Gamma(q))=(1,2,1).
\]
Thus the periodic complex lift has genuine surface amplitude, obtained
by contraction of nonzero Fourier orbits rather than truncation.

`107_168` then embeds the support enrichment into that geometry:
\(\mathbb Z[H_p]\hookrightarrow\mathbb C[\mathbb Q]\),
\(T^q\mapsto e_q\).  Frobenius and every rational
\(\Lambda_{n,m}\) are exactly intertwined.  The naive norm transport,
however, fails because the leafwise differential acts by
\(X(e_q)=2\pi i yq e_q\); its \(\ell^1\) norm is unbounded along the
pro-levels.  Hence the 2022 integer dimension cannot be applied directly
to the de Rham complex.  A mass-controlled cellular/difference model or
a proved graph norm is now required.

`107_169` constructs the cellular alternative.  At rooted order \(L_T\),
the torus complex over
\(R_L=\mathbb Z[x,y]/(x^L-1,y^L-1)\) has uniform \(\ell^1\)-bounded
differentials, homology \((1,2,1)\), and canonical symbolic subdivision
maps whenever \(L\mid L'\).  It is never necessary to enumerate
\(L_T^2\) cells.  This supplies a mass-controlled constant-coefficient
complex suitable for `107_151`.

`107_170` fixes its hard limit.  The cellular model has \(H^4=0\), so
ordinary cup products of divisor Chern classes all vanish.  On the fixed
Paper-0 curve, however, \(\Gamma_1\cdot\Delta=N_1=9\).  Therefore the
cellular complex can model additive cohomology but cannot be the
intersection theory.  Rows (c) and (d) require either a genuine complex
surface top class or the relative trace/fundamental class anticipated
in the 2018 strategy.

`107_171` supplies a positive calibration of the complex-surface branch.
The fixed Paper-0 curve is the reduction at \(5\) of the rational CM curve
with \(j=-32768\).  For
\(\alpha=(-3+\sqrt{-11})/2\), the graphs of \(\alpha^n\) on the abelian
surface \(E_{\rm CM}\times E_{\rm CM}\) satisfy
\[
 \Gamma_{\alpha^n}\cdot\Delta
 =N(\alpha^n-1)=\#E(\mathbb F_{5^n}),
\]
and their centered intersection matrices are exactly those of Paper 0.
This proves that a genuine complex top class preserves the complete Weil
chain for the fixed CM control.  It does not construct the universal
space over \(\mathrm{Spec}\,\mathbb Z\), nor does it evade the
finite-place source no-go.

`107_172` places the finite-field and complex fibres in one arithmetic
family.  Over
\(U=\mathrm{Spec}\,\mathcal O_{\mathbb Q(\sqrt{-11})}[1/11]\),
the CM curve is an abelian scheme and
\[
 \Gamma_{\alpha^n}\cap\Delta=\ker(\alpha^n-1)
\]
is finite flat of rank \(N_n\).  The prime \((\alpha)\) over 5 is fixed
before calculation and is exactly the prime where \(\alpha\) reduces to
the Paper-0 Frobenius.

`107_173` removes the remaining bad place after an explicit quadratic
extension.  If \(w^2=2\alpha+3\), then
\[
 y^2+w y=x^3+\alpha x^2-(\alpha+1)x
\]
has discriminant 1 over the quartic field \(L=\mathbb Q(\alpha,w)\).
Hence \(\mathcal E_L\times_{\mathcal O_L}\mathcal E_L\) is a proper
smooth relative surface over the entire arithmetic base
\(\mathrm{Spec}\,\mathcal O_L\), carrying all Paper-0 graphs and
intersections.  This proves the architecture for one CM control after
base extension; it is not the universal space over
\(\mathrm{Spec}\,\mathbb Z\).

The obvious descent of this calibration is closed by `107_174`.
Conjugation exchanges \(\Gamma_\alpha\) and
\(\Gamma_{\bar\alpha}\), and the two graphs have mutual intersection
11, so the oriented Frobenius graph does not descend to \(\mathbb Q\).
The invariant average recovers each scalar \(N_n\), but its composition
contains mixed graphs and fails \(A_mA_n=A_{m+n}\).  Therefore the CM
calibration cannot supply the universal correspondence by Galois
averaging.  The surviving absolute route is the idele-translation and
arithmetic-linking channel of the 2026 arithmetic Jacobian, which is not
covered by this no-go.

`107_175` tests that new channel against the forcing component pair.
Universal arithmetic linking at \(p=2\) contains characters with both
Frobenius signs, so it is genuinely Galois-sensitive.  Nevertheless its
source object is the same \(\mathrm{lk}_2\) for 20a1 and 36a4,
while their \(IV^*\) component groups require opposite actions.  A
target-independent selector cannot choose both.  Thus rooted/linking
capacity alone does not reopen \(S3\); a quotient character must be
derived canonically from the zeta source, or component-triviality must
remove the need for one.

`107_176` closes the smooth-group interpretation of the published
idele translations.  For every group scheme,
\(\Gamma_{\tau_a}\cap\Delta\) is empty for \(a\neq0\) and is the whole
diagonal for \(a=0\).  This is verified on five real finite-field
groups, including the Paper-0 curve, a supersingular curve, and a
genus-2 Jacobian.  It cannot produce the nonzero local factor
\(1/|1-u|_v\).  That factor comes instead from the normal scaling
representation at a fixed stratum of the adelic monoid boundary.

`107_177` shows that this transverse representation is still not an
ordinary intersection.  For \(x\mapsto ux\) on \(\mathbb A^1_{\mathbb
Q_p}\), the graph--diagonal multiplicity is always 1 when \(u\neq1\),
whereas the trace weight is \(1/|1-u|_p\).  For \(u=1+p^k\), integral
closures coincide along the special transverse line and create an
excess vertical component rather than multiplicity \(p^k\).  An
equivariant derived excess class is therefore mandatory.

That local class is constructed in `107_178`.  The graph--diagonal
Koszul differential has forced Euler class \(e_u=1-u\); fixed-point
localization gives \(e_u^{-1}\), whose normalized local absolute value
is exactly \(1/|1-u|_v\).  It is coordinate invariant and multiplicative
under direct sums.  This closes the local distributional factor, but
only in localized equivariant coefficients; no global bilinear or Hodge
pairing is yet obtained.

`107_179` proves that the standard forgetful map cannot bridge this
local class to ordinary Arakelov theory.  On
\(R(\mathbb G_m)=\mathbb Z[t,t^{-1}]\), forgetting equivariance is the
augmentation \(t\mapsto1\), but localization has made \(1-t\)
invertible.  An extension would send an invertible element to zero and
force \(0=1\).  The remaining fork is therefore global denominator
cancellation or a genuinely equivariant arithmetic Hodge theorem.

The cancellation fork is closed for finite-type coherent geometry in
`107_180`.  On the proper transverse compactification \(\mathbb P^1\),
\[
 {1\over1-t}+{1\over1-t^{-1}}=1,
\]
and the analogous formula for \(\mathcal O(n)\) is the regular character
\(1+t+\cdots+t^n\).  Proper equivariant coherent Euler characteristics
cancel all fixed-point denominators.  They can be forgotten to ordinary
theory only after the uncancelled local explicit factor has disappeared.
The surviving row-(c)/(d) interface must therefore be renormalized and
equivariant, not an ordinary proper coherent compactification.

`107_181` checks that numerical evaluation itself does not destroy the
Hodge sign.  On the actual surface
\(\mathbb P^1_{\mathbb Z}\times\mathbb P^1_{\mathbb Z}\), the primitive
class \(D=A-B\) has \(D^2=-2\), and every evaluated local class
\(w_v(u)D\), \(w_v(u)=|1-u|_v^{-1}>0\), has square
\(-2w_v(u)^2\).  Finite signed combinations in that primitive direction
remain nonpositive.  The remaining issue is global realization, not a
local sign incompatibility.

`107_182` supplies the first global convergent assembly of the boundary
classes.  At \(t_p(s)=p^{-s}\), subtracting the identity term gives
\[
 \mathscr B_p(s)={t_p(s)\over1-t_p(s)}
 =\sum_{k\ge1}p^{-ks}.
\]
Weighting by the Deninger orbit length and summing yields
\[
 \sum_p\log p\,\mathscr B_p(s)=-{\zeta'(s)\over\zeta(s)}
 \qquad(\Re s>1).
\]
This constructs the finite-prime scalar Green channel directly from the
localized normal classes and excludes Davenport--Heilbronn automatically
because no Euler-indexed family exists there.

`107_183` adds the forced Gamma and pole terms.  The completed channel is
\[
 \mathscr G_{\rm comp}(s)=-{\xi'(s)\over\xi(s)}
 =-{\zeta'(s)\over\zeta(s)}-{1\over s}-{1\over s-1}
 +{1\over2}\log\pi-{1\over2}\psi(s/2).
\]
It is odd under \(s\mapsto1-s\), with the apparent endpoint poles
cancelling.  This fixes the complete scalar source channel; the next
operation is its Mellin pairing with Weil tests and geometric
realization as a Green current.

`107_184` performs that Mellin pairing.  For
\(F_g(s)=\int g(x)e^{sx}dx\), absolute convergence gives
\[
 {1\over2\pi i}\int_{\Re s=c}F_g(s)
 \left(-{\zeta'(s)\over\zeta(s)}\right)ds
 =\sum_{p,k}\log p\,g(k\log p).
\]
Replacing the finite channel by \(-\xi'/\xi\) defines the completed
test distribution, including Gamma and pole terms.  The scalar
distribution is now constructed; its realization as a geometric Green
current remains the next interface.

`107_185` realizes the finite local class on the actual periodic orbits
of row (b).  On \(C_p=\mathbb R/(\log p)\mathbb Z\), the twisted operator
\(D_{p,s}=d/dx+s\) has monodromy \(p^{-s}\), cellular determinant
\(1-p^{-s}\), and periodic Green kernel
\[
 G_{p,s}(x)={e^{-sx}\over1-p^{-s}}.
\]
Its return value is \(p^{-s}/(1-p^{-s})\); multiplication by the orbit
length and summation recovers \(-\zeta'/\zeta\).  The finite row-(b)/(c)
Green bridge is therefore constructed on Deninger's existing geometry.

`107_186` supplies the archimedean analogue.  For the number operator
\(Ne_n=ne_n\),
\[
 \mathrm{FP}_{M\to\infty}left(
 \sum_{n=0}^M{1\over n+a}-\log M\right)=-\psi(a).
\]
At \(a=s/2\), one half of this regularized resolvent trace plus
\(\frac12\log\pi\) is the Gamma Green term.  Together with the orbit
kernels and degree-zero/two poles it gives \(-\xi'/\xi\).  Every scalar
local summand now has an operator Green realization.

`107_187` assembles their determinants.  Prime holonomy gives
\(\prod_p(1-p^{-s})^{-1}=\zeta(s)\), while
\[
 \det_\zeta(N+s/2)={\sqrt{2\pi}\over\Gamma(s/2)}.
\]
After the \(\pi^{-s/2}\) and degree-zero/two factors, the completed
determinant is exactly \(\xi(s)\), and its negative logarithmic
derivative is the Green trace of `107_183`.  This is a global analytic
determinant object, not yet a determinant-line sheaf on the arithmetic
space.

`107_188` places this determinant on the finite semilocal indexing
category used by Connes--Consani.  For finite \(S\ni\infty\),
\[
 \Lambda_S=\Lambda_\infty\otimes
 \bigotimes_{p\in S_f}\det C_p^\bullet(s)^{-1},
\]
and inclusion \(S\subset T\) tensors by
\(\prod_{p\in T\setminus S}(1-p^{-s})^{-1}\).  The transitions satisfy
the exact cocycle, and the cofinal canonical section converges to
\(\xi(s)\).  This is a directed semilocal determinant-line system;
descent to a sheaf and then to the absolute square remain separate.

Sheaf descent on the arithmetic curve is proved in `107_189`.  On
\(U_S=\mathrm{Spec}\,\mathbb Z\setminus S\), set
\(\mathscr L(U_S)=\mathcal O(\Re s>1)e_S\), with restrictions multiplied
by the missing local inverse Euler factors.  The frame change dividing
by \(g_S=\prod_{p\in S}(1-p^{-s})^{-1}\) identifies this presheaf with a
constant rank-one sheaf, proving every Cech equalizer.  Its compatible
canonical section has completed generic value \(\xi(s)\).  This is a
line sheaf on the arithmetic curve, not yet a line bundle or pairing on
the absolute square.

The external product is constructed in `107_190` on the actual product
of semilocal sites.  On \(U_S\boxtimes U_T\),
\[
 \mathscr L^\square=
 \mathrm{pr}_1^*\mathscr L\otimes
 \mathrm{pr}_2^*\mathscr L,
\]
and division by
\(g_S(s_1)g_T(s_2)\) proves all two-coordinate Cech equalizers.  Its
generic section is \(\xi(s_1)\xi(s_2)\), and diagonal pullback is
\(\mathscr L^{\otimes2}\) with section \(\xi(s)^2\).  This is a genuine
square-level sheaf result, but not a construction of the missing proper
absolute surface.  Moreover the Frobenius spectral specialization gives
\(z_p(ns)z_p(ms)\), not \(z_p((n+m)s)\); hence it cannot replace the
algebraic correspondence of `107_163`.  The next required object is a
top-degree/Deligne pairing retaining the local inverse-Euler classes.

`107_191` proves that no **unmetrized** ordinary-Picard pairing can
supply that class.  The transition cocycle is the explicit coboundary
\(g_T/g_S\), so \(\mathscr L\), \(\mathscr L^\square\), and its diagonal
pullback all have zero ordinary first Chern class.  In the same gauge
the canonical section is \(Z_\infty\), which has empty divisor on
\(\Re s>1\).  Hence ordinary tensor operations or an isomorphism-invariant
unmetrized Deligne pairing are forced to be trivial.  The remaining
route must use a nonconstant metric, Green current, meromorphic boundary
extension, or a renormalized secondary/equivariant class.

`107_192` closes the smooth determinant-metric subroute.  The completed
Green channel is exactly the logarithmic connection one-form
\(-d\log\xi\), constructed from the prime/Gamma determinant on
\(\Re s>1\), but this connection is flat and
\(\partial\bar\partial\log|\xi|=0\) there.  Hence its ordinary Chern
curvature cannot carry row (c).  A nonzero class can only arise after a
singular/relative extension or through analytic torsion and a
Bott--Chern/Bismut--Goette secondary current.  The published arithmetic
residue formula provides that kind of term only under geometric
hypotheses not yet furnished by the semilocal square.

`107_193` constructs the singular continuation that `107_192` leaves
open.  Poincare--Lelong applied to the source-derived entire determinant
gives \(dd^c\log|\xi|=[Z_\xi]\), and the logarithmic connection has
residue minus the zero multiplicity.  Hardy's theorem then proves a
finite-type no-go: no meromorphic section of a finite-degree line bundle
on a proper algebraic spectral curve can contain the infinite divisor
\(Z_\xi\).  The spectral current is genuine, but it lives on the
noncompact spectral plane rather than on the arithmetic square.  The
remaining bridge must therefore be relative/renormalized or use an
analytic-torsion secondary current on different proper geometry.

`107_194` proves that the published secondary current cannot be placed
directly on an isolated Deninger prime orbit.  The orbit is a real
one-dimensional circle, hence has no complex/Kahler structure.  Its
translation has empty fixed locus away from return times and the whole
circle with derivative one at a return.  Thus its tangent Euler class is
zero while the twisted holonomy determinant \(1-p^{-s}\) is nonzero.
The orbit Green kernel remains valid, but applying arithmetic
Lefschetz torsion requires an ambient complex transverse normal action
and a comparison theorem not supplied by the semilocal square.

`107_195` tests the minimal compact complex repair: the flat Tate torus
with \(q=p^{-s}\).  Kronecker's limit formula forces its determinant to
contain \(q^{1/6}\prod_{n\ge1}(1-q^n)^4\), not just the orbit mode
\(|1-q|^2\).  The ratio is nonconstant, so no universal normalization
identifies the two.  The standard flat compactification route is closed;
only a canonically derived virtual cancellation or relative determinant
can remove the extra Fourier tower.

`107_196` constructs that cancellation canonically.  For the number
operator tails \(\mathcal F_{\ge r}\), the exact sequence
\(0\to\mathcal F_{\ge2}\to\mathcal F_{\ge1}\to\mathbb C_{(1)}\to0\)
gives \(D_1(q)/D_2(q)=1-q\) by Fredholm determinant multiplicativity.
At \(q=p^{-s}\) this is exactly the orbit determinant, and its
logarithmic derivative recovers the finite Green connection.  Thus the
eta tail is removed by a source-defined virtual class rather than by
post-hoc truncation.  A secondary geometric realization of that exact
sequence remains open.

`107_197` shows that the standard metric supplies no such secondary
class.  Every finite number-tail sequence is isometrically and
equivariantly split, so its Bott--Chern secondary Chern character is
zero by normalization; any continuous compatible filtered limit is
also zero.  The nontrivial relative determinant belongs to the quotient
mode, not to a metric anomaly.  A surviving construction must derive a
non-orthogonal coupling or superconnection from the ambient dynamics.

`107_198` closes the simplest dynamic coupling.  The trace-class
weighted unilateral shift \(q^NS\) has zero trace in every positive
power, hence Fredholm determinant one; the same holds for the backward
shift.  It cannot generate \(1-q\) or a secondary anomaly.  A diagonal
rank-one mutation restores the target factor but merely reinstalls the
known quotient.  The next admissible local structure must contain a
bidirectional closed degree loop or a genuine boundary eta class.

`107_199` constructs the minimal bidirectional loop.  For
\(D(a,b)=\left(\begin{smallmatrix}0&a\\b&0\end{smallmatrix}\right)\),
the determinant is \(1-ab\).  Return weight plus transpose symmetry
forces \(a=b=p^{-s/2}\), yielding determinant \(1-p^{-s}\),
eigenvalues \(\pm p^{-s/2}\), and the exact local Green connection.
Asymmetric half-factorizations match the determinant but fail transpose,
so balance is a genuine independent gate.  Secondary current and global
gluing remain open.

`107_200` globalizes the balanced blocks in one operator
\(D_s=\bigoplus_p D_{p,s}\).  It is Hilbert--Schmidt exactly throughout
\(\Re s>1\), although not trace class for \(1<\Re s\le2\).  Paired
eigenvalues \(\pm p^{-s/2}\) cancel the order-two exponential
counterterms, proving
\(\det_2(1-D_s)=\prod_p(1-p^{-s})=\zeta(s)^{-1}\).  Its logarithmic
derivative is the global finite Green channel.  This is one genuine
global Schatten-class spectral realization, still without critical-strip
continuation, archimedean completion, square current, or Hodge form.

`107_201` proves that higher Schatten order does not provide a free
continuation.  One has \(D_s\in\mathcal S_m\) exactly for
\(\Re s>2/m\), so order five is minimal on the critical line.  Paired
blocks retain even exponential counterterms; in particular
\(\det_5(1-D_s)=\zeta(s)^{-1}\exp(P(s)+P(2s)/2)\) in the common Euler
domain.  Uncorrected higher determinants are not \(\zeta^{-1}\); a
global counterterm must be independently derived.

`107_202` proves that the existing Gamma/pole sector cannot provide
that counterterm.  Mobius continuation shows that
\(C_5=P(s)+P(2s)/2\) cancels its branch at \(s=1/2\), but retains
\(C_5(s)=\frac13\log(3s-1)+O(1)\) at \(s=1/3\).  Thus
\(e^{-C_5}\) has fractional monodromy, whereas the standard
archimedean factors are holomorphic and nonzero there.  Renormalization
must remain on the prime side or use a larger branched determinant line.

`107_203` constructs the canonical prime-side order-change correction
at every finite support:
\(\det_2=\det_5\exp(-\mathrm{Tr}\,D^2/2-\mathrm{Tr}\,D^4/4)\).
It then proves that ordinary cofinal convergence still fails on the
critical line.  At \(s=1/2\), the finite Euler determinants tend to
zero while \(\zeta(1/2)^{-1}\ne0\).  Thus analytic continuation cannot
be a norm/strong determinant limit; it requires a nonlocal summation,
branched relative line, or nuclear-space trace.

`107_204` identifies Meyer's published nuclear Frechet quotient as the
required continuation mechanism.  It is source-defined by
\(Zf(x)=\sum_{n\ge1}f(nx)\), and its nuclear virtual character is the
explicit formula.  The prime-orbit character specifically uses the
Euler factorization of \(Z\), so Davenport--Heilbronn still fails at the
correct pre-trace stage.  Meyer supplies continuation, not a polarized
intersection form or Hodge theorem.

`107_205` constructs the comparison map on the Euler half-plane.
Mellin diagonalizes \(Z\) with multiplier \(\zeta(s)\), while
`107_200` gives \(\det_2(1-D_s)^{-1}=\zeta(s)\).  Hence the global
balanced prime Dirac determinant and Meyer's nuclear quotient have the
same canonical Mellin symbol.  This closes the finite-prime
determinant-to-nuclear-trace interface; square-current realization and
positivity remain open.

`107_206` now carries that finite-prime trace character across
Morishita's map.  The anti-flow involution exchanges Meyer's two local
trace halves, making the balanced sum canonical on the
Connes--Consani orbit.  The pushforward simultaneously exposes its
exact limitation: normalized packet-orbit combinations with coefficient
sum zero vanish.  Therefore scalar base currents can carry the zeta
character, but any Galois-sensitive refinement required by legacy row
(c) must remain in a packet-enriched coefficient system.  No square
intersection or Hodge pairing follows from this transport alone.

`107_207` realizes the local relative determinant geometrically.  The
archimedean-local complex-point moduli of the 2026 absolute
Connes--Consani curve is \(\mathbb C\) with a scalar
\(W_\infty\)-action and a fixed trivial point.  Powers of its maximal
ideal complete to the Fock tails, and the exact quotient
\(\mathfrak m/\mathfrak m^2\) is the cotangent line with normal
determinant \(1-p^{-s}\).  This repairs the local geometric-realization gap left by
`107_196`, but the fixed point is absent from the proper Tate quotient;
a proper global fixed section and arithmetic pushforward remain open.

`107_208` closes the naive way of supplying that section.  Retaining
zero before quotienting by \(p^{\mathbb Z}\) makes the orbit of one
nonclosed, so the coarse quotient is not \(T_1\).  Starting from the
Tate curve does not help because it is already compact and admits no
strict Hausdorff compactification with dense image.  The next admissible
global route must therefore be stacky or relative, or must push the
cotangent class before taking the orbit quotient.

`107_209` constructs that pre-quotient local class.  The Koszul
self-intersection formula for the fixed trivial point gives
\(i^*i_*1=\lambda_{-1}(\mathfrak m/\mathfrak m^2)=1-\chi\), whose
prime-twist character is \(1-p^{-s}\).  Thus the local Euler factor is
now an actual equivariant derived intersection class, not a prescribed
number.  What remains is a legitimate proper/nuclear pushforward of
these local classes and their assembly on the arithmetic square.

`107_210` completes the nuclear part of that request on the Euler
half-plane.  The conormal direct sum
\(Q_s=\bigoplus_p p^{-s}\) is trace class exactly on \(\Re s>1\), and
\(\det_{\rm F}(1-Q_s)=\zeta(s)^{-1}\).  Thus the global finite Green
character is the trace of assembled local derived intersections.
Continuation still requires Meyer, while a proper pushforward from one
arithmetic square and its Hodge pairing remain unconstructed.

107_211 closes properness for each local graph--diagonal numerator.
The equivariant compactification \(\mathbb P^1\) has a proper square,
and the class supported at the canonical trivial point pushes to
\(1-\chi\) without an infinity term.  This does not preserve the
localized inverse pole as a coherent class: inversion occurs only in
the later global determinant, and augmentation kills \(1-\chi\).
Therefore the remaining gap is specifically the realization of the
countable nuclear assembly by one global arithmetic square and a
renormalized Hodge pushforward.

107_212 supplies the missing finite-support arithmetic degree.  The
actual arithmetic prime divisor has degree \(\log p\), and tensoring it
with the logarithmic return character
\(\chi_p/(1-\chi_p)\) yields exactly the local finite Green term.
This class is canonically obtained by logarithmically differentiating
the proper Euler numerator of 107_211.  Hence finite supports now have
both a proper equivariant numerator and an arithmetic-degree
realization; the remaining obstruction is the infinite/nuclear
direct image and its primitive Hodge pairing.

107_213 fixes the published-theorem boundary.  Tang's finite-cyclic
arithmetic Lefschetz--RR cannot specialize or converge to \(p^{-s}\).
Koehler--Roessler's torus residue formula does cover the underlying
infinitesimal equivariant arithmetic geometry, but the equality with
analytic torsion is established for unitary torus elements.  Evaluating
its rational side inside the unit disk is not yet a proved arithmetic
direct image.  The next required calculation is the nonunitary
continuation of the immersion anomaly \(R_g\) for the normal line.

107_214 performs that calculation and closes the unlifted branch.  The
reciprocal polylogarithm in \(R_g\) has discontinuity
\(2\pi i/(s\log p)\) at the nonunitary prime character.  Arithmetic
weighting removes the prime dependence, so the surviving object must
live over the logarithmic cover \(s\log p\) and cancel its universal
\(1/s\) monodromy against a generic-point term before nuclear
summation.  No such relative cancellation or lifted arithmetic direct
image is currently constructed.

107_215 constructs the unique minimal scalar correction of that cut:
adding \(\log(1-x)/\log x\) to the reciprocal polylogarithmic order
derivative cancels its two lateral boundary values.  The resulting
log-lifted relative anomaly is real on the positive prime-character
ray.  It is not the Gamma channel prime by prime: at fixed \(s\), its
arithmetic weighting varies with \(p\), whereas the digamma term does
not.  Therefore Gamma can arise only after a global generic-point or
white-light subtraction.  This is a scalar boundary construction, not
a nonunitary arithmetic direct-image theorem.

107_216 closes the remaining ordinary scalar globalization.  An exact
Jonquiere inversion formula yields
\(R^{\mathrm{rel}}(p^{-s})=\log\log(p^s)+\gamma-1+o(1)\), so its
arithmetic prime weighting grows like \(\log p\log\log p\).  The terms
of the proposed prime sum do not approach zero.  Consequently the
generic-point subtraction cannot be appended after placewise scalar
evaluation: it must already be part of the global virtual operator whose
nuclear trace produces Meyer's finite and archimedean distributions.
The comparison of the relative anomaly with that operator-level term is
the next open bridge.

107_217 constructs an integral middle-cohomology sector on the rooted
cellular square.  Twisting by a cyclotomic character gives a Koszul
complex with \(H^0=O/I\), \(H^1=I^{-1}/O\), and \(H^2=0\) away from the
trivial character.  The two finite groups have order \(N(I)\), and are
nonzero precisely for prime-power effective character order.  Thus the
complex Fourier contraction loses arithmetic torsion.  Compatibility
under rooted-level transition and identification with divisor sheaves
remain open and are now the next row-(a) gate.

107_218 runs that transition gate and closes the naive descent.  The
rooted inclusion preserves \(\zeta\), while the cellular subdivision
map restricts it to \(\zeta^d\); generic character labels therefore
move, and replacing the power map by the identity is not well-defined on
the quotient rings.  The finite twisted cohomology remains valid, but it
cannot be promoted through the transition maps of 107_169.  A
restriction/transfer correspondence or a componentwise complex on the
cyclotomic normalization is now required.

107_219 constructs the second option.  Each finite pair of rooted labels
is placed on its unchanged open-and-closed cyclotomic component, where
the integral Koszul complex and its \(H^1\) persist identically under
level enlargement.  Finite-support direct sums therefore have strict
cohomological stabilization.  This closes descent for character local
systems, not yet for the divisor modules \(O(D)\); producing and testing
that comparison is the next row-(a) step.

107_220 closes the direct version of that comparison.  The underlying
adele group in the published tolerant \(H^1(D)\) is divisible, so every
additive map to the finite cyclotomic middle groups is zero.  A viable
interface must first apply Pontryagin duality or use a derived functor.

107_221 constructs the resulting componentwise duality: after twisting
by the codifferent, the trace pairs \(O/I\) perfectly with
\(I^{-1}\mathfrak D^{-1}/\mathfrak D^{-1}\).  Equal cardinalities in the
untwisted complex were not enough; the codifferent is the forced
dualizing module.

107_222 assembles these codifferents over the normalized rooted levels.
The base divisor \(-2\{2\}\) cannot supply them by pullback because
cyclotomic components have relative ramification at odd primes.  The
finite relative dualizer is now constructed and stable.  What remains
is to combine it with the tolerant base dualizer and prove absolute
Serre duality/RR on a genuine square.

107_223 proves that the stabilized cyclotomic complexes still cannot be
the divisor complexes.  They are flat and have identically zero Euler
class, while the CC Euler characteristic varies with the degree of
\(D\).  Therefore further character decoration with ordinary
rank/length Euler characteristic cannot close row (a).  The surviving
construction must introduce a divisor-dependent nonflat transition,
\(c_1(D)\), or bounded/tolerance structure whose integer index reduces
to the published RR formula on the base.

107_224 eliminates the integral-\(c_1\) option for the archimedean real
direction.  Divisibility forces every additive map
\(\mathbb R\{\infty\}\to\mathrm{NS}(X)\) to vanish when
\(\mathrm{NS}(X)\) is finitely generated, while the CC integer
Euler characteristic varies along the same direction.  Hence the next
construction must keep the algebraic class fixed and place the real
variation in the metric/Green or bounded tolerance data, exactly as
predicted in Section 20.

107_225 eliminates the finite torsion subgroup as the tolerance carrier.
Its Minkowski-metric dimension freezes below the minimum nonzero
distance, while the CC \(H^1\) dimension grows without bound as the
tolerance shrinks.  The finite middle groups remain arithmetic strata,
but the ambient compact torus is indispensable.

107_226 supplies the first theorem on that ambient torus.  Volume alone
forces tolerant dimension growth with slope at least \(d/\log3\) in
cyclotomic degree \(d\), and specializes to the exact CC lower bound for
\(\mathbb R/\mathbb Z\).  The remaining metric task is now precise: a
basis-independent balanced-digit covering giving the matching upper
bound and compatible with codifferent duality.

107_227 fixes the target before any further construction.  The
archimedean real divisor direction is killed by every finitely generated
algebraic Chern/Euler shadow, but survives additively in the real kernel
of a metrized Picard object.  Therefore tensor compatibility remains
possible only if integer or continuous dimension is applied
nonlinearly after retaining metric, Green, mass, or tolerance data.

107_228 corrects the local stabilization program.  On every periodic
orbit \(C_p\), the published theorem gives
\[
 p^{-n}\mathrm{tdim}\,H^0(D)^{p^n}\longrightarrow\deg D>0
\]
for positive-degree divisors.  The filtered dimensions are therefore
unbounded, so no finite set of rays and no eventual finite-depth
stabilization can realize the full periodic \(H^0\).  The finite levels
of 107_154 remain useful only as a pro-filtration.  The next admissible
row-(a) task is to construct a cofinality-independent renormalized
dimension on the two-ruling square and then apply the tolerant \(H^1\)
operation; proving another depth cutoff is no longer on the plan.

107_229 executes the first corrected pro-level construction. The old
rectangular levels grow only linearly in depth and therefore have zero
\(p^{-R}\)-density. The norm-adapted levels
\(N_p(A,R)=p^{-R}\mathbb Z\cap[0,A]\) have exact Frobenius covariance
and normalized density \(A\). On two independent rulings their
mass-one \(\mathbb S[\pm1]\)-dimension converges cofinally to \(AB\),
with no relation required between the two depth rates. Identifying the
appropriate divisor-cut polyhedron and its normalized covering
dimension is the next unresolved geometric step.

107_230 proves that this step cannot use the Cartesian product of the
two published section spaces. Its covering dimension is additive and
therefore has zero \(p^{-n}q^{-m}\)-normalized limit. A viable square
must construct \(\Theta(p^nq^m)\) genuinely mixed parameters through a
tensor or convolution section object. This is now the only active
finite-level \(H^0\) architecture; direct products are closed.

107_231 proves that the required mixed architecture is nonempty. The
published one-ruling generators have strict dominance intervals; their
external sums have product dominance rectangles. Independent
coefficient perturbations therefore give an embedded cell of dimension
\((N-p+1)(M-q+1)\), with normalized limit \(\alpha\beta\). This closes
the lower-capacity problem for special external divisors. The active
gate is now the matching upper bound and sheaf descent for the complete
external tensor section module.

107_232 closes that upper bound for special external divisors. The
published appendix proves that the one-ruling CC functions are the full
extremal generating set. Hence their intrinsic external tensor is
generated by the product rays, has exact dimension
\((N-p+1)(M-q+1)\), and normalized limit \(\alpha\beta\). The local
special-external \(H^0\) problem is complete. What remains is extension
to arbitrary divisors and cross-prime sheaf descent.

107_233 completes the extension to arbitrary external divisors. The
published squeeze maps are effective inclusions and principal
translations, hence remain embeddings after external tensor. The exact
special dimensions squeeze every general external module to
\(\max(\deg D,0)\max(\deg E,0)\), with no cofinal-path dependence.
The local external \(H^0\) row on periodic products is now closed. The
remaining local problem is intrinsically mixed divisors.

107_234 closes cross-prime tensor descent at the global divisor-module
level. The 2026 arithmetic Picard theorem supplies \(\mathcal O(\mathcal D)\);
flatness of rank-one subgroups of \(\mathbb Q\) and exact equality of the
projective rank-one norm with the product seminorm make this construction
strong monoidal. Hence the external divisor module on the product topos is
canonical and retains the rooted/Galois refinement. The remaining global
gate is now strictly narrower: prove that its restrictions are the periodic
tropical external modules computed in 107_233. No \(H^1\), square RR, or
proper arithmetic surface follows merely from this descent theorem.

107_235 proves that this narrower gate cannot be the direct restriction of
the unextended module. The arithmetic Gamma-module stalks are countable,
whereas every positive-degree periodic \(H^0\) contains a real cell and has
continuum cardinality. The comparison must first perform scalar extension to
\(\mathbb R_{\max}\), or use the analytic tropicalization constructed at
structure-sheaf level in arXiv:2606.06604v1. That paper explicitly leaves the
relevant periodic eigenspace descent open. Thus the next task is a single
base-change comparison, not another surface candidate.

107_236 carries out the correct base change. The published
\(H_{\max}\widehat\otimes_{\mathbb B}\mathbb R_{\max}\) Legendre theorem
tensorizes after functional reduction to the semiring of bivariate convex
piecewise-affine functions with slope pairs in \(H\times K\). This defines a
Frobenius-covariant structure sheaf on the product Scaling topos and places
the exact external modules of 107_232--107_233 inside that global sheaf.
Thus `SCALING_SQUARE_EXTERNAL_H0` is constructed. The next gate is no longer
base change: it is extending this sheaf/divisor formalism from external
divisors to the intrinsically mixed correspondence divisors \(D(f)\).

107_237 performs that extension in the minimal completed category. A
continuous superposition cannot be a finite-PL Cartier divisor because its
angular curvature has density \(f(r)/r\), whereas finite-PL curvature is
atomic. The homogeneous DC potential
\(U_f(x,y)=\int f(\lambda)\max(y-\lambda x,0)d^*\lambda\) realizes it
chartwise as a distributional correspondence current, retains both source
moments as ruling degrees, and is Frobenius-covariant. It is not yet a global
Cartier/Picard class.

107_238 proves that the ordinary local extension of tropical intersection is
identically zero on these currents. Homogeneity forces every Hessian to have
the same rank-one direction at a fixed angular coordinate, and distinct
Frobenius rays meet only at the compactification corner. Thus the Weil form
cannot be an interior mixed Monge--Ampere integral. All nonzero intersection
content is forced into a global corner/diagonal functional. This turns the
next gate into one normalization problem rather than an unspecified DC
intersection theory.

107_239 constructs that normalization as a relative semilocal trace. The
operator, Fourier/position cutoff, and subtraction of the generic regular
orbit are defined geometrically before evaluating the trace. The published
semilocal trace theorem then proves that the finite remainder is the sum of
Tate local fixed-point terms, hence
\(I_\partial(D_f,D_g)=N(f\star\widetilde g)\). This closes the numerical
corner pairing through a new full adelic/Schwartz channel. It does not yet
make that pairing an intersection form on divisor classes: the DC local
equations still need nonprincipal line-bundle descent and principal
invariance.

107_240 proves that this hoped-for scalar gluing cannot exist with finite-PL
rational transitions. The pullback law forces either \(f=nf\) on diagonal
Frobenius maps or, after degree normalization, invariance under
\(\mathbb Q_+^\times\); both kill every continuous compactly supported test.
Thus the continuous object is a correspondence representation, not a
rank-one Picard class, and classical arithmetic Hodge theorems do not apply
to this branch. Any continuation must be higher-rank/derived and requires a
new positivity theorem.

Morishita's Theorem 3.6 (arXiv:2508.15971v5) supplies a continuous map

\[
 \Psi_F:\mathfrak X_F\longrightarrow\mathscr X_F
\]

from Deninger's system to the Connes--Consani adelic space.  It is
Galois-equivariant and flow-anti-equivariant and sends closed prime
orbits to the corresponding adelic periodic orbit.  This is enough to
place the periodic support of Part II over the Connes--Consani point
space, but it is not a morphism of ringed topoi, a pullback theorem for
Picard/cohomology, or an intersection comparison.  Moreover every
circle \(\gamma_p\) in Deninger's packet over \(p\) maps onto the same
circle \(C_p\).  A Phase 107 realization using this bridge must therefore
either retain the packet label before applying \(\Psi_F\), or prove that
the collapsed packet directions lie in the exact permitted radical.

### Deliverable

A surface realization theorem for all finite-support correspondence
cycles and their determinant lines.

### Stop tests

1. The model must have nontrivial degree one; genus-zero models are
   rejected.
2. The two polar rulings must remain transverse.
3. The cyclotomic local intersections and the Gamma metric must agree with
   Part I under realization.
4. Point/resonance classes may not disappear in an absolutely continuous
   completion.
5. Deleting the places \(p>T\) from the base is not an admissible model.

## 14. Work package III-B — The Picard/Jacobian realization

### Objective

Map every primitive correspondence divisor to a degree-zero metrized line
bundle

\[
 D_f\longmapsto \overline M_f\in
 \widehat{\mathrm{Pic}}_{\rm int}(\mathcal Y_T),
 \qquad M_f\cdot H_T=0
 \tag{15}
\]

or to an integrable adelic line bundle in the precise Yuan--Zhang
category.  The Connes--Consani Jacobian supplies a natural target
candidate, but the map and its metric compatibility must be constructed.

`107_148` rules out the published Jacobian monoid itself, and its
ordinary Grothendieck group, as that codomain.  The Abel--Jacobi prime
class \(H_p=\mathbb Z[1/p]\) is idempotent and noninvertible.  Therefore
it cannot receive a generator of the signed group
\(\mathrm{Div}_{\mathrm{EF}}\) under an additive map; after group
completion it becomes zero.  The live target must be a non-idempotent
derived/spectral enhancement or a genuine group of metrized line bundles
on a regular proper arithmetic model of relative dimension two.

`107_149` fixes the dimensional convention: the generic target is a
surface \(Y_T/\mathbb Q\), the arithmetic model \(\mathcal Y_T\) has
total Krull dimension three, and the direct terminal pairing is
\(-\overline M_f^{\,2}\cdot\overline H_T\).  An unpolarized
Faltings--Hriljac formula would require a separate, pairing-preserving
reduction to a curve.

### Deliverable

A faithful Abel--Jacobi map carrying the source intersection pairing to
the Neron--Tate/adelic height pairing.

### Stop tests

1. Faithfulness on the divisor jets is mandatory.
2. The target metric may not be defined from the Weil form.
3. The map must preserve the scaling action with weight one.
4. A purely absolutely continuous Hilbert target is excluded by the
   point-versus-continuous spectrum theorem.
5. After realification, its kernel must be exactly the explicit Weil
   radical, not a larger finite-codimensional substitute.

### Current classical control

`107_145` adds one genuine target-side control for III-B on Jacobians
already present in Sage.  On five elliptic curves over \(\mathbf Q\),
torsion classes are exactly the visible real-kernel classes and the
free quotient has positive-definite canonical-height Gram matrix.  On
the fixed Paper 0 control \(E/\mathbf F_5: y^2=x^3+x+1\) and on the
genus-\(2\) control \(C/\mathbf F_5: y^2=x^5+x+1\), explicit
point-minus-infinity classes are nontrivial in the classical Jacobian
targets.

This does not build the Phase 107 realization map \(\mathcal A_T\), but
it does anchor the exact-kernel logic of III-B to genuine geometric
Picard/Jacobian objects rather than only to symbolic finite shadows.

## 15. Milestone III — The surface paper

The third paper is complete when the correspondence category and
intersection numbers are realized geometrically on finite regular proper
arithmetic models or in an adelic category with a proved comparison to
such models.

# Part IV. Use the existing Hodge theorem

## 16. Work package IV-A — Applicability audit

Before invoking an arithmetic Hodge theorem, verify every hypothesis:

* regularity/properness or the exact adelic substitute;
* integrability of the metrized line bundle;
* degree zero relative to a fixed ample polarization;
* admissibility/semipositivity conditions on the metrics;
* finiteness of the arithmetic intersection;
* compatibility of pullback and pushforward.

Faltings--Hriljac does not automatically apply to an
\(\mathbb F_1\)-topos.  There are exactly two admissible outcomes:

1. each \(D_f\) is faithfully realized on a classical arithmetic surface
   or in the Yuan--Zhang adelic category, so an existing theorem applies;
2. the new absolute/dynamical category carries its own independently
   proved Hodge--Rosati index theorem.

The first outcome requires a comparison preserving both the Lefschetz
intersection numbers and divisor-sensitive degree one.  The second is a
new index theorem, not an application of Faltings--Hriljac.  Neither
outcome is currently available.

## 17. Work package IV-B — The terminal identity

Prove, with the sign convention fixed before applying Hodge,

\[
 \boxed{
 -\overline M_f^{\,2}\cdot\overline H_T
 =\mathcal Q_W(f).}
 \tag{16}
\]

Then the existing arithmetic Hodge-index theorem yields

\[
 \mathcal Q_W(f)\geq0
 \tag{17}
\]

for every admissible \(f\), and Weil's criterion yields RH.

The terminal audit must verify that (16), rather than (17), contains all
new work.  If positivity was used in constructing \(\overline M_f\), the
argument is circular.

# Part V. Program management

## 18. Paper sequence

The program should be split into independently auditable papers.

### Paper 0 — Function-field calibration

* realization on \(C\times C\);
* Frobenius composition and fixed-point intersections;
* closed-orbit Euler expansion;
* recovery of the Weil square-root estimate from the primitive form.

### Paper A — Local arithmetic intersection lines

* cyclotomic derived intersections;
* determinant/resultant identities;
* Gamma--polar metric;
* coherent diagonal and product formula.
* local branch governance:
  legacy row (c) closed for the full degree-zero target, `A5` rejected
  as noninvariant and non-source-defined.

### Paper B — The decorated absolute Frobenius category

* derived fiber-product composition;
* transpose, degree and connected trace;
* suspension to prime orbits of length \(\log p\).

### Paper C — Arithmetic Lefschetz formula

* fixed-point calculation;
* full prime--Gamma--pole supertrace;
* comparison with the classical explicit formula.

### Paper D — Surface and Jacobian realization

* finite regular proper models;
* two rulings and diagonal;
* Abel--Jacobi map into the Connes--Consani/adelic Picard object.

### Paper E1 — Classical/adelic Hodge bridge

* applicability of Faltings--Hriljac/Yuan--Zhang;
* exact identity (16);
* deduction of Weil positivity.

### Paper E2 — Absolute Hodge index, only if E1 is impossible

* polarization and primitive decomposition in the new category;
* an independently proved Hodge--Rosati index theorem;
* compatibility with the Lefschetz intersection distribution.

Papers E1 and E2 are alternative terminal branches, not cumulative
assumptions.

Each paper remains meaningful if a later stage fails.

## 19. Mandatory falsifiers

Every stage is tested against the following list.

1. **Function-field positive control.**  The same definitions must recover
   (6a)--(6d) on \(C/\mathbb F_q\).
2. **Zero-free source audit.**  Delete every reference to the zeros.  The
   construction must remain defined.
3. **Davenport--Heilbronn audit.**  The construction must fail at the
   Euler/correspondence input, not at an assumed positivity theorem.
4. **Diagonal coherence.**  Cross terms and diagonal must arise from one
   metrized determinant theory.
5. **Divisor sensitivity.**  Moving a divisor must change the relevant
   intersection class or Green metric.
6. **Finite-support realization.**  Each compactly supported test must
   live on one finite model before a limit.
7. **Point-spectrum retention.**  Resonant divisor classes may not be
   erased by an absolutely continuous Hilbert completion.
8. **No prescribed trace.**  The explicit formula must be derived from
   fixed points, not installed as the definition of the trace.
9. **Hodge-category audit.**  Either the hypotheses of an existing theorem
   are checked line by line, or a new index theorem is proved in the new
   category.  Transfer by analogy is forbidden.
10. **Equality-case audit.**  The equality case of the arithmetic Hodge
    theorem must match the equality case of the Weil form.  If
    \(\mathfrak R_W\) denotes the explicit Weil radical, then, on the
    precisely stated real test space,
    \[
      \ker\bigl(f\longmapsto\overline M_f\bigr)=\mathfrak R_W.
      \tag{18a}
    \]
    In particular the known radical jets, represented in the existing
    coordinates by
    \[
      r_j=\frac{K^{(2j)}}K-4^{-j},
    \]
    must map to torsion (hence to zero after tensoring with \(\mathbb R\)),
    and no non-radical test may do so.  Failure in either direction stops
    the candidate before a surface is constructed.

Failure of any item stops the relevant construction before another layer
is added.

## 20. Where the infinite-dimensional information must live

The Neron--Severi group of a fixed proper arithmetic surface is of finite
rank, whereas the compactly supported Weil test space is
infinite-dimensional.  Therefore a successful map cannot store most of
its variation in algebraic divisor classes.  The expected load-bearing
component is the archimedean Green datum:

\[
 f\longmapsto
 \bigl(D_f^{\mathrm{alg}},g_{f,\infty}\bigr),
 \qquad
 \dim\mathrm{span}\,\{D_f^{\mathrm{alg}}\}<\infty,
 \quad
 \dim\mathrm{span}\,\{g_{f,\infty}\}=\infty.
 \tag{18b}
\]

This is a design prediction and an early diagnostic, not an assumption.
A candidate whose Green component has fixed finite rank cannot be
faithful modulo \(\mathfrak R_W\).

## 21. The first concrete project

The immediate next project is not over \(\mathbb Z\).  It is Paper 0 on
the fixed control

\[
 E/\mathbb F_5:\qquad y^2=x^3+x+1.
 \tag{19}
\]

The project must:

1. construct the rulings and \(\Gamma_{F^n}\) inside \(E\times E\);
2. calculate degrees, transpose, composition and diagonal intersections;
3. express the closed-point Euler product through the same connected
   projector used for the prime towers;
4. recover the balanced factor \(q^{-nd/2}\);
5. compute the primitive intersection matrix;
6. derive
   \(|q^n+1-\#E(\mathbb F_{q^n})|\leq2q^{n/2}\)
   from its Hodge sign.

Only after all six operations use definitions admitting a literal
arithmetic analogue does the program return to the finite-support
determinant-line prototype \(\{2,4,3,9\}\) over \(\mathbb Z\).

Paper 0 does not certify the proper-global finite-support construction of
Section 4; that question begins only in Paper A and is audited again in
Paper D.

## 22. Final assessment

The reverse-engineering order is viable, provided it is understood as an
interface-design strategy rather than as permission to postulate
intersection numbers.  The available arithmetic Hodge-index theorems
remove one major conjectural step only on the classical/adelic branch.
They do not automatically apply to the absolute/dynamical branch and do
not construct the cycles, the Frobenius correspondence, the Lefschetz
formula or the comparison with a classical/adelic Picard group.

The program therefore has one central objective:

\[
 \boxed{
 \text{construct a finite-support arithmetic Lefschetz divisor}
 \ \overline D_f\ \text{ satisfying (4), from primes and Gamma alone}.}
 \tag{18}
\]

If such divisors are realized in the domain of
Faltings--Hriljac/Yuan--Zhang, the sign is supplied by an existing theorem.
If they exist only in a new absolute category, a new Hodge--Rosati theorem
remains part of the construction.

## 23. Finite-target branch closed

`107_241` upgrades the design prediction (18b) to an unconditional no-go.
The polarized Weil convolution form has infinite rank, and imposing the two
balance moments changes rank by at most two. Hence the precise source
quotient by \(\mathfrak R_W\) is infinite-dimensional. No realization with
exact kernel \(\mathfrak R_W\) can factor through a finite-dimensional
realification, including a finite-rank Neron--Severi group or a finite list
of Chern/intersection coordinates.

The active branch is therefore fixed: row (a) must retain an
infinite-dimensional Green/distributional component, and row (d) requires
an index theorem in that category. Further finite-rank candidates are
stopped by theorem, not merely deprioritized.
