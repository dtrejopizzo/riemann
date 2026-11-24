# R130.001 — Report, phase 130 (row A closure)

Status: `REPORT`.
Target edited: `04-papers/43-row-a-correspondence-algebra/main.md` (4547 → 4590 lines;
42 passages marked `[REBUILT, phase 130]`).  Every new statement carries a
complete proof in the paper; nothing is asserted "by the blueprint".

---

## 1. Theorems and definitions added

| number | content |
|---|---|
| Def. 3.7 | the chart system `X = ({C_S},{π_{TS}})`, `C_X(S)=D_A(S)`, `C_Y(S)=G(S)` |
| Thm. 3.8 | inflation `J_{ST}`, restriction `R_{TS}=(π_{TS})_*`, `R∘J=id`, the induced monoidal `†`-functors on presented complexes, and the colimit `D_A^∞` |
| Prop. 3.9 | restriction does **not** preserve the trace, with a counterexample and the structural reason |
| Def. 8A.2′ | the enlarged target `T_A := Pic_b(B_T)`, and the norm convention `‖1‖=|s|^{−1/2}` fixed once |
| Def. 8A.7b0 | the trace norm `‖F‖_tr = ‖F‖_{L¹} + ∫\|F̂\|(\|T̂\|+\|c\|)dχ` |
| Thm. 8A.7b | `𝓐_tr` is a Banach `†`-algebra (submultiplicative with constant **1**); `T` continuous; power estimate; germ `Δ_F(z)` holomorphic on `\|z\|<1/‖F‖_{L¹}`; exact multiplicativity; (O-A5-1a) |
| Rem. 8A.7b1 | the exp-type determinant vs the operator-cutoff germ; what P123.105 §4 / P123.107 §5 actually disclaim |
| Thm. 8A.7c | support window, stabilization, the colimit trace `T_∞` chart-invariant on the nose, `M∘J=M`, window comparison `I_∞ = I_A^S` |
| Def. 8A.7d | `c := 0`, with four reasons |
| Rem. 8A.7e | the attempt at `c_{cut}`, its failure, and the correction (8A.13) → (8A.13′) |
| Thm. 8A.9 | (O-A5-5) `Tr_A = exp` of the Haar-regularized Euler characteristic of the shadow `Sh`, formula (8A.24) |
| Rem. 8A.9a | what that does and does not say |
| Thm. 8A.10 | (O-A5-6) `F ↦ E_F` is injective, two proofs |
| Thm. 8A.11 | (O-A5-4) mis-posed: requirement (a) deleted with its reason, (b) unnecessary |
| Thm. 9.7b | Mittag–Leffler form of `Ŵ_p` and `Ŵ_∞`, universal residue `∓i` at `±i/2`, total residue `∓i(\|S_f\|+1)`, and the contour + Poisson identities (9.7b.4)–(9.7b.6) |
| Rem. 9.7c | what 9.7b says about A.8 |
| Lem. 9.14a0 | `N(G)=∫\|Ĝ\|(\|T̂\|+\|c\|)dχ` is bounded on bounded subsets of `D_A` |
| Thm. 9.14a | the rulings as explicit limits of spread Tate characters in `N_A^{dist}` |
| Thm. 9.14b | canonical `D_A`-module splitting `N_A^{dist} = N_A^{dist,prim} ⊕ σ(B_T)` |
| Thm. 9.14c | the rulings are `I_A`-null; `σ(B_T)` **is** P123.007 §4's boundary radical `R_∂` |
| Rem. 9.14d | why this does not contradict Thm. 9.13(a) |
| Thm. 10.3b | (O-A7-1) the effective cone is proper in `N_A^{dist}` |
| Thm. 10.3c | (O-A7-2) RR compatibility of the cone; `λ_per` contractive on it |
| Rem. 10.3d | two different cones; which one A.7 asks for |
| Thm. 10.6a | no functor through the Tate fibre can carry `Tr_A` — the round-4 "(A.8-I)" is unsatisfiable |
| Def. 10.6a/b/c | `λ_per`, `L_S`, and the vector-valued `λ_RR` |
| **Thm. 10.7** | **clause A.8**, parts (a)–(g), with the equality formula (10.10) |
| Thm. 10.8 | the scalar determinant is trivial on the rulings; the vector target is forced |
| Rem. 10.8a | three structural reasons the scalar line is blind |
| Thm. 10.9 | `Φ_det = −⊗_{D_A^+}B_T`: exact, strictly monoidal on free complexes, `†↦♯`, Euler class `M∘s`; `Tor_1 = I/I² ↠ C²`, so `M` is **not** a homological epimorphism |
| Rem. 10.9a | P123.008 §7's derived gate settled, and why its items 1–3 are not needed |
| §11bis item 5 | re-assessment of item 4 (bidegree supplied, normalized Frobenius, span present, index excluded, non-invertible objects still absent) |
| §13.8 | five withdrawals + the deliberately unclaimed `𝓝_∞ = 0` |
| §14, §14.0 | new verdict block and obstacle ledger |

---

## 2. Clause-by-clause

**A.1 — `PROVED` on the declared carrier, with a stated reading.**
Constructed: the chart system (3.7), the coefficient comparison maps
(P123.121 (11), `J_{ST}`, `R_{TS}`), the **restriction functor on objects**
(O-A1-2, Thm. 3.8(b),(c) — it exists because `π_{TS}` is a homomorphism with
compact kernel, the direction P123.018 §2's counterexample does not touch),
and the colimit `D_A^∞` with a chart-invariant trace.  **Honest caveat,
flagged in the paper and here:** "descent" is discharged as *this* datum — a
filtered chart system with a retraction and a chart-invariant global trace —
and not as effective descent along a covering of a stack.  Under a
stack-theoretic reading of the word, A.1 is `PARTIAL` and the missing
statement is: *an effective-descent datum for `C_X`, `C_Y` along a covering of
`X`, with the gluing equivalences*.  This is the one clause whose grade
depends on a reading, and I do not hide it.

**A.2 — `PROVED`.** Additive/stable (8A.1, 8A.3), topological, localized
(3.2(iii)), closed under the declared completions (`𝓐_tr`, `N_A^{dist}`),
and containing more than the two rulings (9.12 (T3), 3.2(iv)); the rulings
themselves are objects of the completion (9.14a).

**A.3, A.4 — `PROVED` on `G`** (unchanged by this phase).

**A.5 — `PROVED`.** All six obstacles disposed of: O-A5-1a (8A.7b(f)),
O-A5-1b (8A.7b(d)–(e)), O-A5-2 (8A.7c), O-A5-3 (`c := 0`, Def. 8A.7d),
O-A5-4 (corrected, 8A.11), O-A5-5 (8A.9), O-A5-6 (8A.10).  §8A.4's verdict
is rewritten.  Two limitations are stated, not hidden: cyclicity is weak
(commutative sector), and (8A.13′) carries one undetermined constant which no
statement uses.

**A.6 — `PROVED`** under the amended clause, and strengthened: 9.14a–c add
that the rulings are subobjects of the completion and that the completion
splits canonically.  §9.3.7's old `PARTIAL` is marked superseded.

**A.7 — `PROVED`.** O-A7-1 by Thm. 10.3b (proper in `N_A^{dist}`), O-A7-2 by
Thm. 10.3c.  **Scope statement (Rem. 10.3d):** P123.010's "lifting of local
positive factorizations" is a property of its `C*` sum-of-squares cone, which
Theorem 10.2(e) proves is a *different* cone from this paper's; it is **not**
a requirement of clause A.7 and it is **not** proved.  I record this rather
than carry it as a row-A obstacle, and an auditor is entitled to disagree with
that judgement — it is the second-weakest point of the closure after A.1.

**A.8 — `PROVED`, with the target enlarged and the round-4 formulation
withdrawn.** Thm. 10.7 (a)–(g): biextension laws, continuity on `𝓐_tr` and
`N_A^{dist}`, principal invariance (vacuous, as before), restriction
(strict in the Tate slot; chart-invariant on the colimit), extension of
`λ_per` on the ruling plane, the equality formula (10.10)
`λ_RR(F,G) = λ_RR(prim,prim) ⊗ λ_per(MF,MG)`, and no sign.  Beside it,
Thm. 10.8: the scalar line **is trivial** on the rulings, so the vector target
`T_A = Pic_b(B_T)` is forced, not chosen.

**A.9 — passed for the formalism** on the automorphism sector (unchanged).

**A.10 — `PROVED`.** §11 stands; §13.8 adds the one statement deliberately
*not* claimed (`𝓝_∞ = 0` for the colimit), because every proof I know uses
zeta zeros.

**Closure rule (spec §4).** A.1–A.10 are proved.  The rule also requires "an
adversarial audit confirms that none of A.2–A.8 is merely a renaming of the
scalar explicit formula".  **That is not mine to certify.**  The paper states:
`ROW A: A.1–A.10 PROVED on the declared carrier; WEIL-STRENGTH-COMPLETE
EARNED, PENDING THE ADVERSARIAL AUDIT REQUIRED BY THE CLOSURE RULE`, and names
the two places to press: (1) A.1 under the stack reading; (2) the renaming
test against Remark 9.7a, since `T̂` *is* the prime-power-plus-Gamma side of
the explicit formula.  I did not edit the specification file.

---

## 3. Blueprint claims I found false, or had to modify

1. **(O-A5-4)'s counterexample `E_{2F} ≅ E_F` — not verifiable, and the
   opposite is true on this carrier.**  The blueprint proposes deleting the
   requirement `E_F ≅ E_G ⟹ F=G` by exhibiting `E_{2F} ≅ E_F` "as (bi)modules
   (multiply by 2)".  On Paper 43's carrier `E_F` is a *section* of the Fell
   bundle (Cor. 3.4), and Theorem 8A.10 proves `F ↦ E_F` **injective**; so
   `E_{2F} ≠ E_F`, and no isomorphism `E_{2F} ≅ E_F` is exhibited anywhere in
   the corpus.  I therefore did **not** write that counterexample into the
   paper.  The correct closure, which I did write (Thm. 8A.11), is that the
   requirement is *classically wrong to demand*: `Tr(nΓ)=nTr(Γ)` while `nΓ`
   and `Γ` have the same underlying subscheme, so no trace of correspondences
   is an invariant of unbased objects, Weil's included.  The blueprint's
   conclusion stands; its justification does not.

2. **The `c := 0` uniqueness argument (ii) is false as stated.**  Blueprint:
   "`c = 0` is the unique choice for which the chart constants agree".  Any
   constant declared uniformly in `S` makes `c_T = c_S`; uniqueness fails.  I
   kept (ii) as "must be declared chart-independently, and `c:=0` does that",
   explicitly disclaimed uniqueness there, and put the uniqueness content in
   (iii) (`c=0` is the unique choice adding **no** global constant on top of
   the intrinsic Mittag–Leffler constants `−log p` and `log π + γ`).

3. **`L_S = L_tan` for `S={q}` is false; only the local factors agree.**
   Blueprint §1.3(f) asserts equality "exactly".  But `∞ ∈ S` always, so
   `L_S = L_S^{(∞)} ⊗ ⊗_p L_S^{(p)}` carries an archimedean factor that
   `A_MIXED_METRIC_WORK`'s one-place construction has not got.  Theorem 10.7(f)
   states and proves the correct thing: `L_S^{(q)} = L_tan`, including the
   norm-versus-squared-norm factor, with the honesty note attached.

4. **(O-A5-5) is not "Theorem 8.10 is the identification `Tr_A = Sh^ren`".**
   Blueprint says the shadow "is the divergent operator trace `Tr R(F)`" and
   that Thm. 8.10 identifies them.  Theorem 8.10 compares `T` with the
   *imported operator cutoff* functional `T_an`, not with the Hochschild
   shadow `Sh` of §7, and its constant is undetermined; it cannot serve as the
   O-A5-5 comparison.  I proved a different and exact statement (Thm. 8A.9):
   place by place, the **Haar-regularized rank** of the local shadow factor of
   §7/Appendix D **is** the local density `τ_v`, so `Tr_A = exp` of the
   Haar-regularized Euler characteristic of `Sh`.  This is internal to the
   paper, uses no import, and is what the obstacle asked for.

5. **`c_cut` does not come out.**  I attempted the computation from
   P123.046 §1 (the unitary `T_p`, `c_p = 1−p^{−1}`, the multiplicative
   regular representation) and P123.035 §3 (the folding factor `½`).  It
   reduces to the identity counterterm of import `C`, whose coefficient
   P123.004 §4 and P123.035 §6 forbid using.  Recorded as a failed attempt
   (Rem. 8A.7e).  **This forced a real correction the blueprint did not
   anticipate:** Theorem 8A.7's display (8A.13) is *not* unconditional once
   `c := 0` is declared; it becomes (8A.13′) with the factor `e^{c_cut F(1)}`.
   Nothing in the paper depends on it.

6. **`‖F⋆G‖_tr ≤ 2‖F‖_tr‖G‖_tr` — the constant is 1, not 2.**  Direct
   computation: `‖F⋆G‖_tr ≤ ‖G‖_{L¹}‖F‖_tr ≤ ‖F‖_tr‖G‖_tr`.  Improved in the
   paper.

7. **The decay of the spread Tate characters is exponential, not `O(1/n)`.**
   Because `supp ψ ⊆ [a,b]` with `a > 0`, `λ_−(f_n) = ∫ψ(s)e^{−ns}ds` and
   `sup|f̂_n| ≤ ‖ψ‖_{L¹}e^{−na/2}`.  The blueprint's `2‖ψ‖_∞/n` is weaker; the
   paper proves the exponential bound, which makes Theorem 9.14a(c) a
   one-line consequence of Lemma 9.14a0.

8. **Blueprint §3's properness argument: verified and tightened.**  Nets, not
   sequences (the strong dual of a nuclear LF space need not be metrizable);
   otherwise the argument is exactly right and is written as Thm. 10.3b,
   including the AM–GM step `‖F‖_{L¹} ≤ ½(λ_+ + λ_−)`.

9. **Blueprint §6's item on `E_q⋆E_q^† = Δ`.**  Correct, but the paper must
   say *why* it is not a trivialization: the `q^{−1/2}` is the half-density of
   §5.2, and P123.021's `Γ_F⋆Γ_F^t = q·Δ` is its unnormalized form.  Written
   as §11bis item 5(ii), together with the withdrawal of round 4's inference
   that "the dagger cannot be extended without a normalization that is not
   constructed".

**Verified numerically** (`scripts/R130_ml_check.py`, independent of the
the blueprint's scripts): the Mittag–Leffler sums reproduce `Ŵ_p` for `p=2,3,7` and
`Ŵ_∞` to truncation accuracy, and contour integration gives residues
`∓i` at `±i/2` for both `Ŵ_2` and `Ŵ_∞` to `10^{−32}`.  `max_τ Ŵ_∞(0,τ) =
5.372183…`, matching (14.2).  Numerics are a check, not a proof; the paper's
proofs are analytic.

---

## 4. What remains open, exactly

Nothing that any clause of A.1–A.10 requires.  Four residual items are listed
in §14.0 and repeated here so that no one has to hunt for them.

1. **The stack-theoretic reading of "descent" in A.1.**  Missing statement:
   *an effective-descent datum for the coefficient categories `C_X`, `C_Y`
   along a covering of `X`, with its gluing equivalences and cocycle.*  Under
   the clause's own words this is not asked; under a stricter reading it is,
   and then A.1 is `PARTIAL`.
2. **`c_cut`.**  Missing statement: *the identity-class coefficient of the
   imported semilocal cutoff trace theorem, in the half-density
   normalization.*  Blocked by P123.035 §6's stop rule.  Nothing depends on it.
3. **`𝓝_∞ = 0` for the colimit.**  Deliberately not claimed; `CLASSICAL`,
   belongs to row C, forbidden as an input to row A by A.10.
4. **Non-invertible correspondences as objects.**  Not constructed; not
   required by any clause; §11bis item 5(v).

The label the mathematics earns, in the specification's own words:

> `ROW A: A.1–A.10 PROVED on the declared carrier; WEIL-STRENGTH-COMPLETE
> EARNED, PENDING THE ADVERSARIAL AUDIT REQUIRED BY THE CLOSURE RULE.`

The label is not granted here, because §4 of the specification does not let
this round grant it.
