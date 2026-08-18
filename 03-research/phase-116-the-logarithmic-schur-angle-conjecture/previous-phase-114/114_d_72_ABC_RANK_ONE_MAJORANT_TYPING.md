# D.72 — Typing the rank-one majorant in A--B--C

## Status

D.71 shows that row D is equivalent, parity by parity and for every `z>0`,
to a finite boundary majorant

\[
 B_\epsilon-zI\le C_{\epsilon,z}
       |u_\epsilon\rangle\langle u_\epsilon|.              \tag{0.1}
\]

This note tests whether (0.1) can be constructed directly from the current
A--B--C package, before identifying its trace with `B_nuc`.

The result is a typed obstruction and a minimal extension theorem.

* A constructs actual periodic sections, enriched Yoneda multiplication,
  cotangent frames and perfect determinant/contact objects.
* B constructs the dynamic Witt contact and its determinant degree.
* C constructs a nuclear supercharacter and the complete Gamma trace.
* None of the three categories currently contains a dagger, a cone of
  positive endomorphisms, or a contractive natural transformation gluing
  the periodic and Gamma feature maps.  The desired inequality is therefore
  not an intrinsic statement in the constructed categories.
* The minimal extra datum is an adelic contractive gluing in an ordered
  dagger enlargement, compatible with the cofinal cancellation of the
  neutral prime directions.  Its exact form is forced by the Douglas
  factorization lemma.

The obvious componentwise Yoneda construction fails: every local Poisson
block has expanding directions even after its two local jets are killed.
Thus any valid gluing must mix primes with Gamma globally.  No RH, zeta
zero, Weil positivity or screw positivity is used.  The paper is not
modified.

## 1. The exact analytic feature maps

For a finite prime cutoff `P`, D.32 constructs

\[
 \begin{aligned}
 \mathbf S_PF
 &=\bigl((\sqrt{\log p}\,A_pF)_{p\in P},\sqrt{m_0}F\bigr),\\
 \mathbf B_PF
 &=\bigl((\sqrt{\log p}\,F)_{p\in P},\partial_\infty F\bigr),
 \end{aligned}                                             \tag{1.1}
\]

with

\[
 B_{{\rm nuc},P}(F,G)
 =\langle\mathbf S_PF,\mathbf S_PG\rangle
  -\langle\mathbf B_PF,\mathbf B_PG\rangle.               \tag{1.2}
\]

The two Tate boundary maps are

\[
 MF=(M_-(F),M_+(F)).                                       \tag{1.3}
\]

For `z>0` and a positive boundary matrix `C`, set

\[
 X_{P,z,C}F=
 \mathbf B_PF\oplus\sqrt z,F\oplus C^{1/2}MF.             \tag{1.4}
\]

Then the rank-two version of (0.1) is exactly

\[
 \|\mathbf S_PF\|^2\le\|X_{P,z,C}F\|^2.                  \tag{1.5}
\]

Reflection diagonalizes `C` and reduces (1.5) to the two rank-one
majorants of D.71.

## 2. Douglas factorization gives the minimal datum

For bounded maps between Hilbert spaces, the Douglas lemma says

\[
 S^*S\le X^*X                                                \tag{2.1}
\]

if and only if there is a contraction `K` on the closure of `Ran(X)` such
that

\[
 S=KX,qquad\|K\|\le1.                                     \tag{2.2}
\]

Apply this with `S=mathbf S_P` and `X=X_(P,z,C)`.  We obtain:

> **Theorem 2.1 (minimal contractive gluing).**  At each finite cutoff, the
> D.71 boundary majorant is equivalent to a contraction
> \[
> \boxed{
> \mathfrak K_{P,z,C}:
> \overline{\mathrm{Ran}\,X_{P,z,C}}longrightarrow
> \overline{\mathrm{Ran}\,\mathbf S_P},qquad
> \mathbf S_P=\mathfrak K_{P,z,C}X_{P,z,C}.}               \tag{2.3}
> \]
> Consequently any source construction of (0.1) must supply either this
> contraction or an equivalent positive factorization of
> `X^*X-S^*S`.

The statement is minimal in a literal sense: if (1.5) holds, Douglas
constructs (2.3); if (2.3) is given, its contractivity proves (1.5).

To be a noncircular A--B--C proof, `mathfrak K` must be constructed from
periodic multiplication, Witt contact, Poisson/Fourier duality and support,
before using the sign or spectral decomposition of `B_nuc`.

## 3. What A supplies and what it does not

For each pair `(p,q)`, A constructs the enriched section category

\[
 \mathsf {Sec}_{p,q},                                      \tag{3.1}
\]

the enriched presheaf category

\[
 \mathsf A_{p,q}
 =\mathrm{PSh}_{\mathsf V_{p,q}}
   (\mathsf {Sec}_{p,q}^{\rm op},\mathsf V_{p,q}),         \tag{3.2}
\]

and the Yoneda lines `y_(p,q)(D,E)`.  Its universal property extends
enriched strong monoidal functors to cocontinuous lax monoidal functors.
This constructs multiplication and Kunneth maps.

The effective tropical section modules do have their pointwise idempotent
order.  But the next stages used by A are:

1. the real cotangent frame of the regular section locus;
2. stable idempotent completion to `Perf_per`;
3. scalar extension and homotopy pullback to `Perf_IDN`.

These stages retain exact sequences, tensor products, dualizable objects
and determinant lines.  They do **not** specify

\[
 f\longmapsto f^*,\qquad
 \mathrm{End}(H)_+,qquad
 \|f\|,\qquad
 f^*f\ge0.                                                 \tag{3.3}
\]

Categorical duality in a rigid symmetric monoidal category is not a Hilbert
adjoint: it has no conjugate-linear positivity axiom and does not compare
operator norms.  Likewise the enriched Yoneda adjunction is an adjunction
of mapping objects, not a dagger adjunction.  Its universal property cannot
produce the word ``contraction'' in (2.3) until a normed ordered target
functor is supplied.

## 4. What B and C supply and what they do not

B constructs from `F_n` the perfect dynamic contact

\[
 K_n^W\simeq[\mathbb Z\xrightarrow{\Phi_n(1)}\mathbb Z]   \tag{4.1}
\]

and compares its reduced determinant object with the prime contact of A.
This gives the exact scalar degree `Lambda(n)` and multiplicative
composition.  A determinant degree is additive, but it is not a positive
endomorphism of the periodic section object.

C realizes the correspondences by the scaling multipliers `U_n` and forms
the nuclear superobject

\[
 \mathbb L_{\rm comp}^{\bar0}\oplus
 \Pi\mathbb L_{\rm comp}^{\bar1}.                         \tag{4.2}
\]

Its supertrace gives all finite contacts and Gamma.  The category of nuclear
Frechet representations is not equipped here with a Hilbert norm making
the realization unitary, and a supertrace is a difference of traces rather
than a positive functional.  Hence it supplies the equality (1.2) after
analytic realization, but no cone in which (1.5) can be asserted before
that realization.

The resulting type table is

\[
 \begin{array}{c|c|c}
 \text{structure}&\text{constructed operation}&\text{missing for (2.3)}\\ \hline
 \mathsf A_{p,q}&\text{Yoneda/Day multiplication}&\text{dagger and norm}\\
 \mathrm{Perf}_{IDN}&\text{dual, tensor, cofiber}&\text{positive cone}\\
 K_n^W&\text{perfect contact/determinant}&\text{positive operator lift}\\
 \mathsf {NFRep}^{\rm sup}&\text{nuclear supertrace}&\text{Hilbert order}\\
 \text{Gamma Fourier block}&\text{analytic unitary/trace}&
       \text{gluing to periodic sections}.
 \end{array}                                               \tag{4.3}
\]

Therefore the inequality (0.1) is currently ill-typed inside A--B--C,
although its two scalar sides are correctly compared after passing to the
analytic form.

## 5. Cofinal cancellation is an additional typing obstruction

For compactly supported `F`, the paired difference in (1.2) stabilizes.
The two norms do not.  If `log p` is larger than the diameter of the support,
all nonzero translated correlations vanish and

\[
 \|A_pF\|=\|F\|.                                          \tag{5.1}
\]

Thus both sides contain the common neutral contribution

\[
 \sum_{p\in P}(\log p)\|F\|^2,                            \tag{5.2}
\]

which diverges as `P` exhausts the primes, while their difference remains
the stabilized form.

Consequently the finite-cutoff contractions (2.3), even if constructed,
do not automatically define a contraction between ordinary Hilbert direct
limits.  A cofinal construction must retain and cancel the common neutral
summand in a relative Hilbert, Krein, or support-compression object before
taking the limit.  The nuclear trace performs the scalar paired
renormalization, but no ordered Hilbert object realizing that cancellation
has been constructed in A--B--C.

## 6. The componentwise Yoneda candidate fails exactly

The simplest attempt is to construct `mathfrak K` independently at each
prime from Yoneda multiplication and then take its direct sum.  This would
require the local Poisson map

\[
 A_p=\sqrt{1-p^{-1}}(I-p^{-1/2}U_p)^{-1}                  \tag{6.1}
\]

to be contractive after removing its two local jet directions.

It is not.  In the Hardy model put `r=p^(-1/2)`,

\[
 h_r(z)={\sqrt{1-r^2}\over1-rz},qquad
 V_N(z)=z^2(1+z+\cdots+z^{N-1}),\quad N\ge2.              \tag{6.2}
\]

The constant and linear jets of `h_rV_N` vanish, but direct summation gives

\[
 \boxed{
 \|h_rV_N\|_{H^2}^2-\|V_N\|_{H^2}^2
 =2\sum_{d=1}^{N-1}(N-d)r^d>0.}                           \tag{6.3}
\]

Hence no contraction can map the unextended local boundary vector to the
local periodic Poisson section while preserving the matrix coefficient.
The obstruction occurs on the local two-jet kernel itself.

> **Theorem 6.1 (block-diagonal gluing no-go).**  The majorant (0.1) cannot
> be obtained as a direct sum of primewise Yoneda contractions, even after
> the two scalar jets are removed.  Any valid contraction must mix the
> finite places with the Gamma boundary before taking its norm.

This is an exact source-side obstruction, not a numerical failure of a
chosen discretization.  The necessity of Gamma is also global rather than
merely blockwise: the primitive family of D.67 has support chosen so that
every contact except `n=2` vanishes, while its positive arithmetic defect
grows two derivative orders faster than the continuum boundary energy.
Adding other finite-place summands cannot alter that family; the complete
Gamma multiplier is the term which restores the ultraviolet negative
order.

## 7. The minimal additional A--B--C datum

The preceding results force the following extension.

> **Definition 7.1 (ordered adelic gluing datum).**  An ordered adelic
> gluing consists of:
>
> 1. a dagger/ordered enlargement `HMix_ABC` of the common periodic--nuclear
>    realization, with a cone of positive adjointable endomorphisms;
> 2. relative feature objects `H_S` and `H_B` in which the common neutral
>    prime summand has a cofinal cancellation, rather than two divergent
>    Hilbert direct limits;
> 3. the two-ruling boundary morphism `M` induced by the Tate restrictions;
> 4. for every `z>0`, a positive finite boundary operator `C_z` and a
>    natural contraction
>    \[
>    \mathfrak K_z:
>    H_B\oplus\sqrt z,H_{\rm test}\oplus C_z^{1/2}\mathbb C^2
>       \longrightarrow H_S                              \tag{7.1}
>    \]
>    whose pullback on every finite cutoff is (2.3);
> 5. compatibility with Day multiplication, Witt composition, principal
>    descent, reflection and cofinal enlargement of the finite places.

> **Theorem 7.2 (sufficiency and minimality).**  If Definition 7.1 is
> constructed before comparison with the nuclear character, its
> contractivity proves
> \[
> B_{\rm nuc}(F,F)-z\|F\|^2
> \le\langle MF,C_zMF\rangle.                              \tag{7.2}
> \]
> Hence `B_nuc<=0` on the two-jet primitive space after letting `z` decrease
> to zero.  Conversely, at every finite cutoff (7.2) produces the
> contraction by Douglas, so the contractive gluing is the minimal Hilbert
> datum encoding the majorant.

### Proof

Apply the norm inequality for (7.1), use the trace-exact comparison (1.2),
and cancel the neutral relative summand.  On `MF=0`, (7.2) gives
`B_nuc(F,F)<=z||F||^2` for every positive `z`, hence the desired
nonpositivity.  The converse is Theorem 2.1, with the boundary matrix chosen
from the two parity capacities of D.71.

## 8. Attempted construction from the existing adjunctions

There are three canonical maps which might be mistaken for (7.1).

1. **Enriched Yoneda unit/counit.**  These maps are monoidal and universal,
   but no Hilbert norm is part of their target.  After choosing the ordered
   cotangent frame to be orthonormal, (6.3) shows that the induced local map
   is expansive.
2. **The geometric adjunction
   `Pi_per^* dashv R Pi_(per,*)`.**  It is an adjunction of presentable
   coefficient categories.  The right adjoint is lax monoidal, not the
   Hilbert adjoint of the left functor; no unit or counit norm estimate is
   defined.
3. **Perfect duality plus Gamma Fourier duality.**  Perfect duality gives
   evaluation/coevaluation and Fourier duality gives a unitary analytic
   block, but no natural transformation identifies the periodic Poisson
   range with the supported Gamma range.  Taking a polar decomposition of
   their already compared analytic operator would choose the positive part
   of `B_nuc` and be circular.

Thus none constructs Definition 7.1.  The missing datum is not another
determinant scalar: it is the ordered, norm-controlled *global gluing
morphism*.  A viable future construction would have to arise from an
independent adelic support theorem or a mixed-section effectivity theorem,
so that contractivity follows before the trace comparison.

## 9. Verdict

A--B--C determines every coefficient in (1.2), both Tate jets, all dynamic
contacts and the Gamma term.  It does not currently determine an order in
which every positive direction can be proved to factor through those jets.
The exact missing object is (7.1).

The local Yoneda route is ruled out by (6.3), and ordinary cofinal Hilbert
direct sums are ruled out by the neutral divergence (5.2).  The only
surviving source construction must simultaneously:

* mix all finite places with Gamma;
* implement relative cofinal cancellation;
* carry a dagger and positive cone;
* prove contractivity from support/effectivity rather than from `B_nuc`.

No such ordered adelic gluing is constructed here.  Therefore D.72 does not
close row D; it proves the precise typing obstruction and the minimal extra
datum needed to make the rank-one majorant an intrinsic A--B--C theorem.
