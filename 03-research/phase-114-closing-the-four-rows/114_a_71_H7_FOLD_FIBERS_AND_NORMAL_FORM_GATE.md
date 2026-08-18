# 114.a.71 — H7: fold fibers reduce prime regularity; bilateral purity remains

> **Progress (`a_72`).** H7-RF-FOLD is proved on the exponential block
> fibers `V_epsilon` of `a_21` and their one-output scalarizations
> `T_epsilon` from `a_22`, uniformly in arity.  The unresolved part is now
> extended by `a_73` to every alternating read-once tree of depth at most
> two.  `a_74` removes the depth bound by Hessian reconstruction.  The
> unresolved part is H7-RF-CUT: signed/repeated variables, contractions,
> two-sided graph data and cut-related tree separation.  `a_75` then removes
> signs in the read-once sector; H7-RF-BICUT retains repetitions,
> contractions and genuinely bilateral cuts.
>
> **Correction (`a_76`).** Haran does prove unique reductions for an
> individual positive oriented tree.  The missing normal form is only for
> bilateral data modulo cancellation and consistent commutativity; the exact
> residual condition is `(E_cancel:p)=E_cancel`.

```
+-------------------------------------------------------------------------+
| RETRACTION   On a diagonal-compatible chart, fold o p_1^# = id.         |
| EXACT TEST   p is regular iff it is injective on every fold fiber.      |
| RESIDUAL     Evaluations need only separate pairs with the same fold.   |
| LOCALIZE     Once proved on an affine chart, regularity survives central |
|              localization and sheafification.                           |
| SOURCE AUDIT Individual positive trees have unique reductions; no       |
|              bilateral cancellation-purity theorem is supplied.         |
| OPEN CORE    Prove fiberwise cancellation, or the stated normal-form     |
|              theorem, on an affine cover at every pro-level.            |
+-------------------------------------------------------------------------+
```

## 1. Typed setup: fibers, not an additive kernel

Fix a pro-level, an arity and a chart on which the first projection and the
diagonal give operation-set maps

\[
 B\mathop{\longrightarrow}^{i=p_1^\#}A
 \mathop{\longrightarrow}^{r=\Delta^\#}B,
 \qquad r i=\mathrm{id}_B.                                      \tag{1.1}
\]

Here `A` is the corresponding operation set on the arithmetic plane and `B`
is the operation set on the arithmetic curve.  Let `mu_A` and `mu_B` denote
multiplication by the first-ruling scalar `p`.  Functoriality gives

\[
 r\mu_A=\mu_Br,
 \qquad \mu_Ai=i\mu_B.                                                \tag{1.2}
\]

The objects in (1.1) are sets with generalized-ring operations; they are not
the abelian modules of Haran's Section 6.  Therefore the unconditional
formulation is in terms of the fibers

\[
 A_b=r^{-1}(b),\qquad
 \mu_{A,b}:A_b\longrightarrow A_{\mu_B(b)},                            \tag{1.3}
\]

not a claimed direct-sum decomposition `A=B+ker(r)`.

The curve scalar `p` is regular: on its ordinary charts the operation sets
sit in rational matrix/vector sets, where a nonzero integer cancels.  This
is also the input that makes the inverse-uniformizer bundle `L_p` on the
curve available before attempting its pullback to the plane.

## 2. Exact fold-fiber criterion

### Theorem 2.1

Assume `mu_B` is injective.  Then `mu_A` is injective if and only if every
map `mu_{A,b}` in (1.3) is injective.

### Proof

If `mu_A` is injective, each restriction is injective.  Conversely, suppose
`mu_A(F)=mu_A(G)`.  Applying `r` and using (1.2) gives

\[
 \mu_B(rF)=\mu_B(rG).
\]

Cancellation on `B` gives `rF=rG=b`.  Thus `F,G` belong to the same fiber
`A_b`, and injectivity of `mu_{A,b}` gives `F=G`.  QED.

This proves something stronger than the informal statement that an
obstruction is "invisible on the diagonal": **every possible collision is
forced to occur between two off-diagonal trees having exactly the same
diagonal fold**.

It also explains why the retraction alone is insufficient.  Take
`B={*}`, `A={0,1}`, let `i(*)=0`, let `r` be constant, let `mu_B=id`, and let
`mu_A` be the constant map to `0`.  Equations (1.1)--(1.2) hold and `mu_B` is
injective, while `mu_A(0)=mu_A(1)`.

## 3. A strictly smaller residual target

Let `epsilon_lambda:A->K_lambda` commute with multiplication by `p`, and
assume that `p` cancels on every target.  Replace the global joint
faithfulness demanded in `a_64` by

> **H7-RF-FOLD.** For every `b in B`, the restrictions
> `epsilon_lambda|A_b` are jointly faithful.

### Corollary 3.1

H7-RF-FOLD implies injectivity of `mu_A`.

### Proof

If `mu_A(F)=mu_A(G)`, Theorem 2.1 first puts `F,G` in the same fold fiber.
Targetwise cancellation gives `epsilon_lambda(F)=epsilon_lambda(G)` for all
`lambda`; H7-RF-FOLD then gives `F=G`.  QED.

This is genuinely weaker than global residual faithfulness.  On a product
`A=B times C`, evaluations that remember only `C` distinguish every pair in
one fiber but identify points lying in different `B`-fibers.  Such
identifications are harmless because injectivity of `mu_B` already prevents
a `p`-collision across different fibers.

The finite twisted bios of `a_49`--`a_51` therefore need not reconstruct the
diagonal coordinate a second time.  Their exact remaining burden is to
separate the off-diagonal data inside each fold fiber.

## 4. Localization does not create a new prime collision

### Lemma 4.1

Let `S` be a central multiplicative system in a generalized ring operation
set `A`.  If multiplication by `p` is injective on `A`, it is injective on
`S^{-1}A`.

### Proof

Suppose `p(a/s)=p(b/t)`.  By the localization equivalence there is `u in S`
with

\[
 u t p a=u s p b.
\]

Centrality rewrites this as `p(uta)=p(usb)`.  Cancel `p` in `A`; the result
`uta=usb` is exactly `a/s=b/t`.  QED.

Sheafification of sets is left exact, so a monomorphism on a localized
presheaf remains a monomorphism after sheafification.  Consequently the full
Section-11 quantifiers do not require a fresh proof on every basic
localization **once regularity has been proved on an affine chart from which
that localization is taken**.  They still require an affine cover at every
later pro-level; a diagonal retraction need not exist on an arbitrary
off-diagonal boundary chart.

## 5. Why the positive tree normal form is not yet a proof

Haran's long source, Section 13.2, proves unique `1`-reduced and
alternating-reduced representatives for each individual positive oriented
tree.  The bilateral operation data are then quotiented by leaf bijections,
cancellation and consistent commutativity.  The source does not supply a
terminating confluent rewriting system or a prime-purity theorem for that
full bilateral quotient.

Thus the tempting argument

\[
 \text{"multiply all coefficients by }p\text{ and cancel coefficientwise"}
\]

is circular until the following is proved.

> **H7-CANCEL-PURE.** In every arity of every affine chart in a cofinal
> pro-level cover, Haran's bilateral cancellation congruence satisfies
> `(E_cancel:p)=E_cancel` for every prime `p`, compatibly with substitutions,
> contractions, consistent commutativity and chart localizations.

H7-CANCEL-PURE is equivalent to H7-PRIME-REG on the presentation (`a_76`).
The positive tree normal forms do not imply it: a quotient of a uniquely
represented ambient object can still acquire prime torsion when its defining
congruence is not pure.  Consistent commutativity across arbitrary cuts is
part of the unresolved bilateral problem.

## 6. Exact status after the reduction

The diagonal-compatible part of PRIME-REG is now reduced exactly to the
fiber maps (1.3), and H7-RF-ALL of `a_64` is sharpened to H7-RF-FOLD there.
Central localization is no additional obstruction.  What remains is one of:

1. prove H7-RF-FOLD on an affine cover, uniformly in arity and pro-level;
2. prove H7-CANCEL-PURE directly on the bilateral presentation; or
3. find an explicit same-fold pair `F!=G` with `pF=pG`, which would kill the
   completed-lattice route.

`a_72` completes item 1 for every block-extractable family generated by the
two primitive additions.  It leaves the nested/cut-related part as
H7-RF-NEST.  `a_73` then closes all read-once trees of depth at most two by
reconstructing their leaf partition from Boolean pair probes.  Thus any
remaining obstruction first lay in H7-RF-DEEP.  `a_74` subsequently closes
all depths and arities in the unsigned read-once sector; the residual gate is
H7-RF-CUT.  `a_75` recovers leaf signs by unit-vector evaluation and reduces
the corresponding orthant to `a_74`, leaving H7-RF-BICUT.

No remaining item in this list is supplied by the source or by a bounded
computation.  See `a_76` for the corrected source audit and exact colon-
congruence criterion.
Accordingly H7-PRIME-REG, the completed square lattice and `a4-strong` remain
open.

## 7. Verification scope

`114_a_71_h7_fold_fiber_verify.py` checks the source wording, the exact
finite-set fold-fiber theorem, the strict weakening of residual
faithfulness, the split-map counterexample and localization cancellation.
It does not assert H7-RF-FOLD or H7-NF.

Primary source: [Haran, arXiv:1709.05831](https://arxiv.org/abs/1709.05831),
equations (10.6)--(10.22) and Section 11.
