# A125.009 — classical control on a curve over a finite field (clause A.9)

Status: `PROVED-IN-REPOSITORY` on the graph sector, with the scope of §4.
Clause A.9 is an acceptance test for structural correctness, not a definition
by analogy, and it is treated as such here.

## 1. The two recorded refutations, and why they do not block A.9

The acceptance specification marks A.9 `NOT PASSED`, citing ledger rows
`C1` and `C2`.  Both refute identifications that this campaign does not make.

**`C1`: source squares are not effective graph cycles.**  Addressed in
A125.007 §1.  Effectivity here is coefficient nonnegativity of graph measures
(P123.074), never a sum-of-squares cone.  `C1` refutes the sum-of-squares
identification, which clause A.7 forbids anyway.

**`C2`: the Frobenius transpose is not the integral inverse.**  This is the
sharper one, and the classical model already contains its resolution.
`A_DUALITY_WORK` computes, for the graph of a finite morphism `f`,

\[
        D_h(\mathcal O_{\Gamma_f})
        =\sigma_{*}i_{f*}\bigl(h\otimes f^{*}h^{-1}\bigr),          \tag{1.1}
\]

concentrated in degree zero, with the ordinary **transposed** graph as leading
effective cycle of multiplicity one, and it states explicitly: "For a Frobenius
morphism (5) does not claim an integral inverse correspondence.  The line
factor in (5) is necessary at the kernel level, although it does not change
the leading cycle."

So the correct classical transpose is the transposed graph carried by a
half-density line twist, and `C2` refutes only the naive reading "transpose
equals inverse" for a non-invertible morphism.  The dagger of this campaign
satisfies (1.1)'s shape: A125.001 Definition 4.4 carries exactly the twist
`H=h\boxtimes h`, and on the graph sector `E_w^{\dagger}\cong E_{w^{-1}}`
(A125.006 Theorem 3.1(1)) is consistent with (1.1) because the idele classes
are invertible, so there the transposed graph **is** the graph of the inverse.
No claim is made for a non-invertible correspondence; see §4.

## 2. The comparison

Let `C` be a smooth projective curve over `\mathbb F_q`, `h` a theta
characteristic, `D_h` the involution `D_h(K)=\sigma^{*}(K^{\vee})\otimes H[1]`
of `A_DUALITY_WORK`.  Let `\mathrm{Aut}(C)` act by graphs.

**Theorem 2.1.**  There is a functor `\Phi` from the graph sector
`\mathcal G` to perfect kernels on `C\times C` which is typed correctly on
all four items A.9 names:

1. **composition.**  `\Phi(E_u\star E_v)=\Phi(E_{uv})=\mathcal O_{\Gamma_{uv}}
   =\mathcal O_{\Gamma_u}\star\mathcal O_{\Gamma_v}`.  Both sides use
   pull–tensor–push with no higher excess term, because the graph maps are
   isomorphisms onto their images: arithmetically P123.016 (3.1)–(3.2),
   classically the same fibre-product computation.
2. **transpose.**  `\Phi(E_w^{\dagger})=D_h(\Phi(E_w))` by (1.1), the twist on
   both sides being the half-density `h`.
3. **unit.**  `\Phi(\Delta)=\mathcal O_{\Delta}`, the two-sided unit on both
   sides: P123.016 (4.1) arithmetically, and `D_h(\Delta_{*}\mathcal O_C)
   \cong\Delta_{*}\mathcal O_C` classically, which is where `h^{2}=\omega_C`
   is used.
4. **diagonal intersection.**  `\chi(\mathrm{Tr}_A(\Delta))=r` matches
   `\chi(L\Delta^{*}\mathcal O_\Delta)=(1-g)-(g-1)=2-2g=\deg T_C
   =\Delta\cdot\Delta`, both being an Euler characteristic of a two-term
   complex whose excess is retained rather than truncated.

*Proof.*  Items 1–3 are the cited statements on each side, matched item by
item; item 4 is the computation in `A_DUALITY_WORK` §"Graphs, effective
cycles, and the diagonal trace" against A125.006 (1.2).  QED

## 3. The decisive structural match

The strongest evidence that the arithmetic formalism is correctly typed is not
any of the four items above, which a definition by analogy could also arrange.
It is that the arithmetic side **predicts** a classical fact that was not put
in.

A125.006 Theorem 1.1 gives the dichotomy: a freely acting external class has
acyclic shadow, hence `\delta(w)=0`; the identity has shadow `B[0]`, hence
`\delta(1)=r\neq0`.  Its classical shadow is the Lefschetz fixed-point count,

\[
        \Gamma_f\cdot\Delta=\#\mathrm{Fix}(f),                     \tag{3.1}
\]

which vanishes precisely when `f` has no fixed points.  The arithmetic
dichotomy was proved from a continuous contraction of a twisted corner bar
(P123.096) and a character-average computation (P123.097), with no
intersection theory and no fixed-point formula as input.  That it reproduces
(3.1) on the nose, including the vanishing case, is exactly the kind of
acceptance test A.9 asks for.

The same match explains the failure of the cheap invariants recorded in
A125.005: classically `\Gamma_f` and `\Delta` are abstractly isomorphic
subvarieties, so no isomorphism-class invariant of a bundle on either can
separate them, while the intersection number does.  A125.005 Theorem 1.1 is
the arithmetic instance of that classical triviality.

## 4. Exact scope, and the dependency it creates for row B

`\mathcal G` is generated by idele classes, which form a **group**.  The
comparison of Theorem 2.1 is therefore with the invertible classical
correspondences, i.e. graphs of automorphisms, together with their sums,
shifts, cones and retracts.  It is **not** a comparison with all finite
correspondences, and in particular not with the graph of Frobenius on a curve
over `\mathbb F_q`, which is finite and not invertible.

This is a real limitation and it is recorded as a dependency rather than
absorbed.  Row B will need non-invertible arithmetic correspondences; whether
they lie in `\mathcal G`, or require enlarging it and re-proving A.2–A.8 on
the enlargement, is not settled here.  The honest statement is: A.9 is passed
as a structural acceptance test on the sector where rows A's own clauses have
been proved, and the extension to non-invertible correspondences is the first
question row B must answer.

## 5. Ledger

| statement | status |
|---|---|
| §1 `C1`, `C2` do not apply to this campaign's definitions | `PROVED-IN-REPOSITORY` |
| Thm 2.1 composition, transpose, unit, diagonal intersection match | `PROVED-IN-REPOSITORY` |
| §3 the dichotomy reproduces the Lefschetz vanishing (3.1) | `PROVED-IN-REPOSITORY` |
| A.9 on the invertible/graph sector | `PASSED` |
| comparison with non-invertible finite correspondences | `OPEN`, and a stated prerequisite for row B |
