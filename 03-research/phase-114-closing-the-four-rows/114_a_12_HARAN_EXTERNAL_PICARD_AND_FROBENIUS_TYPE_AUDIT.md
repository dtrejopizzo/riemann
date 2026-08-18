# 114.a.12 — Haran H7–I7: external unit torsors; completed sector conditional

> **Refined correction (`a_63`--`a_66`).** Formula (2.1) requires the projection maps to
> extend from `O` to Haran's regular-denominator fraction sheaves `K`.
> Section 11 does not give this for arbitrary morphisms, so the completed
> lattice construction is conditional on H7-PB-REG. The earlier `Pic_qc`
> interpretation is retracted by the type audit `a_66`; `GL_1(O)`-torsors,
> their labels and tensor laws do pull back unconditionally.

```
+--------------------------------------------------------------------------+
| H7-PIC       The two projections construct an external-product map       |
|                                                                          |
|              e : Pic(X) x Pic(X) -> Pic(X x_F X).                       |
|                                                                          |
|              Each ruling is injective.  ker(e), if nontrivial, lies     |
|              entirely in the anti-diagonal (lambda,lambda^{-1}).        |
| H7-SECTIONS  External multiplication of sections exists functorially.   |
|              Injectivity, generation and a Kunneth theorem are OPEN.    |
| I7-FROB      Haran's F_n is an endomorphism of the Witt sheaf/group.     |
|              It is not a supplied pro-scheme map X->X; hence no graph   |
|              cycle Gamma_n on the square follows from it.               |
| VERDICT      H7-I7 is reduced to three explicit gates; it is not closed. |
+--------------------------------------------------------------------------+
```

## 1. Objects and source scope

Let

\[
 X=\overline{\mathrm{Spec}\,\mathbb Z}=\{X_N\}_{N\in I},\qquad
 Y=X\times_{\mathrm{Spec}\,\mathbb F\{\pm1\}}X
   =\{Y_{N,M}=X_N\times_S X_M\}_{(N,M)\in I^2}.
\]

Haran 2017 constructs `Y` in (10.1).  Section 11 applies to an arbitrary
pro-`CFR^t` scheme and defines:

- rank-`d` bundles `D_d(X_N)` by (11.3);
- their section sheaves by (11.7) and pro-sections by (11.13);
- bounded pro-bundles and their isomorphism classes by (11.11)--(11.16).

For the arithmetic curve, (11.19) computes

\[
 \mathrm{Pic}(X)\simeq\mathbb R_{>0}.               \tag{1.1}
\]

The later non-involutive formulation, arXiv:2209.08536, confirms two facts
that must not be conflated:

1. the commutative-bio pushout is noncollapsed;
2. its *totally* commutative quotient collapses back to `Z`.

Thus the desired square lives essentially in the commutative but not totally
commutative category.

## 2. External product of Haran line bundles

Write `p_1:Y->X`, `p_2:Y->X` for the projections.

### Proposition 2.0 (unconditional external product of unit torsors)

Mapping the `GL_1(O)` transition cocycles gives

\[
 e_{tor}:Pic_{tor}(X)\times Pic_{tor}(X)\longrightarrow Pic_{tor}(Y),
 \qquad (L,M)\longmapsto p_1^*L\otimes p_2^*M.             \tag{2.0}
\]

This is `a_66`, and uses no fraction denominator.

### Proposition 2.1 (conditional finite-stage construction)

Assume the projections send Haran-regular denominators to regular
denominators, so that `p_i^#:K_X->K_Y` exists.

For line bundles

\[
 D=\{U_\alpha,f_\alpha\}\in D_1(X_N),\qquad
 E=\{V_\beta,g_\beta\}\in D_1(X_M),
\]

the cover `U_alpha x_S V_beta` of `Y_{N,M}` and local multipliers

\[
 h_{\alpha\beta}=p_1^\#f_\alpha\circ p_2^\#g_\beta       \tag{2.1}
\]

define a line bundle `D boxtimes E` on `Y_{N,M}`.

### Proof

On a double overlap,

\[
 h_{\alpha\beta}^{-1}h_{\alpha'\beta'}
 =p_1^\#(f_\alpha^{-1}f_{\alpha'})
  \circ p_2^\#(g_\beta^{-1}g_{\beta'}).
\]

Both factors belong to the local structure sheaf by the defining transition
condition (11.3), hence so does their product.  Refinement and multiplication
by local units give exactly Haran's equivalence (11.4).  Therefore (2.1) is
well-defined on line-bundle classes.  QED.

The construction commutes with transition pullbacks `(pi_N^N')^*` and
`(pi_M^M')^*`.  Bounded systems remain bounded after applying both pullbacks
and multiplying their local representatives.  Consequently it passes to the
pro-object.

### Corollary 2.2 (conditional completed external Picard homomorphism)

There is a canonical homomorphism

\[
 e:\mathrm{Pic}(X)\times\mathrm{Pic}(X)
 \longrightarrow\mathrm{Pic}(Y),\qquad
 e(L,M)=p_1^*L\otimes p_2^*M.                            \tag{2.2}
\]

Here `Pic` means the Section-11 completed lattice category. No computation of
all of it is asserted. Its abstract `Pic_tor` analogue is unconditional by
Proposition 2.0.

## 3. Exact kernel reduction

The diagonal `Delta:X->Y` exists by the universal property of the fiber
product and satisfies `p_1 Delta=p_2 Delta=id_X`.

### Theorem 3.1 (two rulings and the anti-diagonal gate)

The theorem holds unconditionally in `Pic_tor`; it holds in `Pic_comp` under
H7-PB-REG.

Under (1.1):

1. `p_1^*` and `p_2^*` are separately injective;
2. diagonal pullback obeys
   \[
   \Delta^*e(\lambda,\mu)=\lambda\mu;                   \tag{3.1}
   \]
3. hence
   \[
   \ker e\subseteq\{(\lambda,\lambda^{-1}):
                      \lambda\in\mathbb R_{>0}\}.       \tag{3.2}
   \]

### Proof

Functoriality gives `Delta^* p_i^*=id`, proving (1).  Pullback commutes with
tensor product, so

\[
 \Delta^*(p_1^*\lambda\otimes p_2^*\mu)=\lambda\otimes\mu,
\]

which is multiplication in `Pic(X)=R_{>0}` and proves (2).  If `e(lambda,mu)`
is trivial, (3.1) gives `lambda mu=1`, proving (3).  QED.

### Definition 3.2 (the exact bidegree gate)

The external rank-two sector is genuinely bigraded precisely if

\[
 p_1^*\lambda\otimes p_2^*\lambda^{-1}\not\simeq\mathcal O_Y
 \quad\text{for every }\lambda\ne1.                     \tag{3.3}
\]

Thus “compute two degrees” is no longer an unstructured request: its first
unresolved statement is the vanishing of this anti-diagonal kernel.  The
diagonal cannot decide (3.3), because every class in (3.3) restricts trivially
to it.  A second independent slice, a pushforward/norm, or a direct cocycle
calculation on the finite stages is required.

### Proposition 3.3 (absolute-point slice criterion)

Let `pi:X->S` be any object over a base with `Pic(S)=0`. If `pi` has a section
`sigma:S->X`, then the external Picard map (2.2) is injective.

### Proof

The section produces two maps

\[
 j_1=(\mathrm{id}_X,\sigma\pi),\qquad
 j_2=(\sigma\pi,\mathrm{id}_X):X\longrightarrow X\times_SX.
\]

For `(L,M)` one has

\[
 j_1^*e(L,M)=L\otimes\pi^*\sigma^*M=L,
 \qquad
 j_2^*e(L,M)=M,                                          \tag{3.4}
\]

because `sigma^*L,sigma^*M` lie in `Pic(S)=0`. Hence
`(j_1^*,j_2^*)` is a left inverse of `e`. QED.

For `S=Spec(F{+-1})`, the base is the absolute affine point and has trivial
rank-one Picard group. Thus either of the following would close H7-Pic:

1. construct an `S`-point of the compactified `X` and apply Proposition 3.3;
2. prove (3.3) directly from the finite-stage cocycles.

The read Haran sources supply the structure map `X->S` and the diagonal, but
do not supply a section `S->X`. No such point is assumed here.

## 4. What exists for sections

### Proposition 4.1 (external section multiplication)

For scalar sections `s` of `D` and `t` of `E`,

\[
 (s,t)\longmapsto p_1^\#s\circ p_2^\#t                 \tag{4.1}
\]

is a section of `D boxtimes E`.  The same formula is compatible with the
pro-section condition (11.13).

### Proof

Locally write `s=f_alpha u_alpha` and `t=g_beta v_beta` with `u_alpha` and
`v_beta` in the respective structure sheaves, as in (11.7).  Their external
product is

\[
 h_{\alpha\beta}\,
 (p_1^\#u_\alpha\circ p_2^\#v_\beta),
\]

which lies in the section sheaf of (2.1).  Pullback compatibility gives the
pro-statement.  QED.

This proves existence only.  None of the following follows formally:

- injectivity of (4.1);
- generation of all sections by external products and the two additions;
- a norm or proper bounded ball on those sections;
- a Künneth count producing `Theta(m^2)` absolute dimension.

Those four assertions are the remaining H7 section/gauge gate.

`114_a_14` adds a necessary quantitative correction: even an injective map
of pure external sections has logarithmic cardinality only `O(m)` when each
factor does. Quadratic growth requires independently usable mixed sums, with
noncollision, mass and upper-count proofs; H7-K records the exact acceptance
test.

## 5. Frobenius is presently of the wrong geometric type

In arXiv:2209.08536 equations (12.4)--(12.6), Haran defines

\[
 F_n:\mathcal W(\mathcal P)\to\mathcal W(\mathcal P),
 \qquad F_n[p]=[p^n],                                    \tag{5.1}
\]

and then applies this functor to the structure prop/bio to obtain a Witt
sheaf with Frobenius endomorphisms.  Formula (5.1) is an endomorphism of an
abelian group (and, in the totally commutative case, of a ring).

It is **not** a morphism

\[
 F_n:X\longrightarrow X                                  \tag{5.2}
\]

in the pro-scheme category.  The source does not construct (5.2), and the
contravariant spectrum functor cannot be applied to (5.1) to get a map of `X`:
the ring being acted on is the derived Witt sheaf, not the structure object
whose spectrum is `X`.

### Corollary 5.1 (I7 typing condition)

A cycle called `Gamma_n` on `Y` cannot yet be defined as “the graph of
Haran's Frobenius” from (5.1).  Before asking whether `Gamma_n` is principal
or whether `Gamma_n.Delta=Lambda(n)`, one must supply either:

1. a genuine pro-scheme endomorphism (5.2); or
2. an independently defined correspondence/cycle object on `Y`, together
   with its divisor class.

This is a missing morphism, not a claim that such a morphism is impossible.

### Proposition 5.2 (no nontrivial Frobenius from the ordinary dense chart)

The embedding of ordinary schemes into Haran generalized schemes is fully
faithful.  Hence

\[
 \mathrm{End}_{\mathrm{GSch}}(\mathrm{Spec}\,\mathbb Z)
 =\mathrm{End}_{\mathrm{Sch}}(\mathrm{Spec}\,\mathbb Z)
 =\mathrm{End}_{\mathrm{CRing}}(\mathbb Z)^{\mathrm{op}}
 =\{\mathrm{id}\}.                                      \tag{5.3}
\]

Indeed, a unital ring endomorphism fixes `1`, hence every integer.  Therefore
any pro-scheme endomorphism of `X` whose restriction to the ordinary dense
chart is induced by a ring endomorphism has identity restriction there.  In
particular, the nontrivial Witt operations `F_n` cannot be obtained by simply
extending an ordinary Frobenius of `Spec Z`: no such Frobenius exists.

This does not rule out a correspondence supported on the square, nor a more
exotic pro-map not determined by that chart.  It proves that the function-field
phrase “take the graph of Frobenius” has no literal ordinary-chart analogue in
characteristic zero.

## 6. Updated H7–I7 gate

The surviving task has three sharply separated parts:

| gate | exact statement | status |
|---|---|---|
| H7 abstract Picard | `a_66`: external unit-torsor pullback exists; anti-diagonal still needs a slice/descent for the full continuous plane | PARTIAL POSITIVE |
| H7 completed Picard | prove H7-PB-REG, then the Section-11 formula (2.1) is typed | OPEN |
| H7 discrete bigrade | `a_19`/`a_66`: unconditional in `Pic_tor`; completed realization conditional | ABSTRACT HAVE / COMPLETED OPEN |
| H7 axis/grid sections | `a_20`: curve axis and abstract square grid exist; completed bounded interpretation requires H7-PB-REG | PARTIAL |
| H7 generic off-diagonal entropy | `a_21`: `2^N` block defects in one fold fiber | HAVE, wrong type |
| H7-sections | scalarize/bound that entropy and prove the `exp(Theta(mn))` upper/lower bounds | OPEN |
| I7 prime-incidence carrier | `a_17`: `Delta cap V_p=Spec F_p`, mass `log p` | HAVE |
| I7 nonprincipal prime lift | `a_66`: unconditional in `Pic_tor`; completed prime lattice requires H7-PRIME-REG | ABSTRACT HAVE / COMPLETED OPEN |
| I7-cycle | extend the carriers to a Frobenius/correspondence algebra and local/global intersection complex | OPEN |

What is closed unconditionally is the abstract unit-torsor Picard algebra,
including injectivity of each ruling and the discrete rank-two bypass. `a_63`
restricts only the stronger completed-lattice realization and its bounded
section formalism. Pure external
products and diagonal-detected families are closed negatively as
quadratic-growth mechanisms by `114_a_14` and `a_20`. The generic algebra has
the required entropy by `a_21`; its scalar bounded realization remains open.

## 7. Source-verification rule

`114_a_12_haran_source_and_picard_verify.py` checks the exact formula anchors
in the local primary sources and the group-theoretic kernel implication.  It
does not pretend to verify the three open constructions in §6.
