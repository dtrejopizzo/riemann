# R138.003 — Builder, round 2, phase 138: repairs

*Builder: Opus 5 (1M). Date 2026-09-13. Object: the findings of `R138_002_HOSTILE_AUDIT.md`
(verdict **CONFIRMED WITH REPAIRS**, no FATAL; MAJOR H1–H4, MINOR H5–H13). Method prescribed by the
coordinator and followed literally: **every repair is applied in place in `R138_001_BUILDER_ROUND1.md`,
each marked with a bracketed `[REPAIRED / CORRECTED / WITHDRAWN / DOWNGRADED / RELABELLED / RESTRICTED,
round 2, finding H<n> of `R138_002`]` note at the point of use. There are no silent edits.** This file
is the ledger, not a second copy of the mathematics.*

**Verdict accepted in full.** Every one of H1–H13 is correct. I contest nothing. Three of the four
MAJOR findings (H1, H4, H10) are defects I should have caught by applying my own definitions to my own
objects; H2 is a claim of record I had no right to make; H3 is a label I attached without a proof.

---

## 1. The repair ledger

| # | severity | what was wrong | repair applied, and where in `R138_001` | cost |
|---|---|---|---|---|
| **H1** | MAJOR | "`C_Pó` is a **detecting cone**" is a type error: Definition 0.1 is about cones of **classes `F ∈ D^W`**, `C_Pó` is a cone of **kernels `h`**, and by my own Theorem D.17.1b `C_Pó ∩ D^W = {0}` — so read through Definition 0.1, `C_Pó` is the zero cone. Same defect for `C_Pó^{sm}`, and "the Pólya cone viewed through its square roots" is not well posed since `{F : F⋆F^∨ ∈ C_Pó}` is not known to be convex. | §D.17.2 heading rewritten ("The triangle family detects; `E` and `C_c^∞` are detecting cones"); Theorem D.17.2's headline replaced by an explicit three-part statement — (1) the **family** `{h_T}` detects in the `h`-variable, (2) Lemma D.17.2c produces the classes `F_T^{(δ)}`, (3) hence `E` and `C_c^∞(R)` are detecting cones; Corollary D.17.2d restricted; the ledger paragraph, §5 item 4, §6bis row 13, the §8 label table and the README all rewritten. New `OPEN` **D.17-β** records the convexity question for `√C_Pó`. | **None mathematically.** Every downstream use — §5, D.17.3's no-go, the answer to **Q** — goes through verbatim with "`E` and `C_c^∞`" in place of "the Pólya/triangle cone", because what those uses need is *a detecting cone of classes*, which is exactly what D.17.2c+d supply. |
| **H2** | MAJOR | "`E` has empty interior in **every** topology in which `I_∞(·,F)` is continuous" is a non-sequitur (continuity of the functionals is a *lower* bound on the topology) and is false: the auditor's weighted sup-norm `‖E‖_ε = sup_t\|E(t)\|e^{(1+ε)\|t\|}` makes every `I_∞(·,F)` continuous and gives `E ∩ D^W_ε` interior. | The `REFUTED` box after Theorem D.15.2b and the "Topology, stated precisely" paragraph now carry a **`WITHDRAWN`** box quoting the counterexample; **D.15.2b(i) is claimed for `‖·‖₁` only**; the refutation of the blueprint now rests on **D.15.2b(ii)** ("`E` is not absorbing at `K`"), which is algebraic and holds in every topology. Blueprint correction **B-3** restricted accordingly. New `OPEN` **D.15-γ** records the residual question. | **None.** Theorem D.15.2(c) requires "absorbing at `K`", not "has interior", so the load-bearing half was always (ii). The withdrawal costs a rhetorical flourish and nothing else. |
| **H3** | MAJOR (label) | The comparison "D.11 ⇒ D.16.3 immediate; converse false" was labelled `PROVED` with no proof, and compares a section-count rate (which presupposes an `h⁰` the corpus does not have) with a support-reach statement, without a common normalization. | The comparison is **relabelled `HEURISTIC`** with a bracketed note explaining why neither direction is proved; **Corollary D.16.3 itself stays `PROVED`**, its proof being independent of the comparison. The §8 table now has two rows, D.16.3 (`PROVED`) and D.16.3′ (`HEURISTIC`); README updated. | A claim of a proved bridge to D.11 is lost. The phase-136 meta-theorem reading survives as a heuristic, which is what it is. |
| **H4** | MAJOR | Definition D.16.1 let `⋆k` be convolution by one **fixed** kernel; then Theorem D.16.1(d) is not proved and cannot be, since `\hat k` has infinitely many zeros and may vanish at the very `z_0` being detected, while "detecting" quantifies `∀ρ_0 ∃F ∈ C` with `C` fixed first. | Definition D.16.1's `⋆` now ranges over **convolution by members of `C` itself**; Theorem D.16.1(d) and its proof restated accordingly, with the note that Theorem F's Step 2 chooses `φ` *after* seeing `ρ_0`, which is exactly why the self-convolution closure is the right operation. | **None to B-5.** No translation occurs in the repaired construction either, so "translation is *the* operation" remains refuted. |
| **H5** | MINOR | `I_∞(F,K_odd) = −½μ(F)`, not `+½μ(F)`. | Sign corrected in the proof of Theorem D.15.1(ii), with the note that every downstream use is of `μ²` or of `μ = 0`. | None. |
| **H6** | MINOR | D.17.3(d)'s perturbation had relative size `e^{−√log u}`, **larger** than the classical (Vinogradov–Korobov) remainder permits (`3/5 > 1/2`). | Profile replaced by `exp(−c(log u)^{3/5}(loglog u)^{−1/5})`; the conclusion becomes `R̃(T) ≫ e^{T/2}e^{−cT^{3/5}}/T → ∞`, identical in force. Per the auditor's recommendation, "Finding" is **downgraded to "Remark"** and the `PROVED` label retained only for the displayed inequality. | None: clause (c) already shows every unconditional bound diverges; (d) only rules out assuming a cancellation. |
| **H7** | MINOR | D.16.0(β) omitted CC's **second** vanishing condition `\hat g(0) = 0`, i.e. `Φ_F(½) = 0`, which primitivity does **not** imply. | (β) restated with both conditions, and with the Theorem 6.11 alternative (`−c\|Φ_F(½)\|²`, `13<c<17`). | None: source (α), phase-118's certificate, is independent of CC and covers all of `C_W^{prim}`. |
| **H8** | MINOR | The README and §8 presented Theorem D.17.2 without the attribution caveat that `OPEN` D.17-α records. | Remark D.17.2e now states "**not** claimed as new" and names the exact literature question and the sources to check (Bombieri, *Remarks on Weil's quadratic functional*; Yoshida 1992; Riesz-mean / Báez-Duarte one-parameter criteria; `phase-14/ANCHOR-framework…`); D.17-α expanded; the caveat carried into the §8 table and the README row. | None mathematically; the theorem may turn out to be a restatement, which is why it is filed as `OPEN` (attribution). |
| **H9** | MINOR | "`Z` is onto a dense subspace in the sense of Theorem 11.10" — Theorem 11.10 describes `ker Z`, not the image. | Clause replaced by "`ker Z = (P^W)^{⊥_{I_∞}}` exactly (Theorem 11.10)", which is what D.16.2‴ uses. | None. |
| **H10** | MINOR | D.15.2c's ample cone is defined through `I_∞`, hence through the zero sum: it **fails clause (ii) of Q**, and neither the README nor P46-4 said so. | Caveat box added under (D.15.2c); P46-4 and the README row amended; `OPEN` D.15-β (a zero-free description of `A`) cross-referenced. | A criterion I presented as usable is demoted to a *statement* whose usability depends on D.15-β. This is the honest status. |
| **H11** | MINOR | P46-1 cited the transposed `M`-convention to §12.1/(S1); it actually occurs in the **proof** of Proposition 12.6. | Location corrected; the recommendation to Paper 46 is unchanged. | None. |
| **H12** | MINOR | D.15.4b(c)⇒(b) tacitly used `P ⊂ R`. | Prop. 12.6's hypothesis "a finite set `P ⊂ R` of simple poles with `P = 1−P`" now cited at the point of use, with the remark that for complex `P` the condition cuts out a circle and the normal form fails. | None: the hypothesis is in force. |
| **H13** | MINOR | "four times CC's prime-free window" — the factor against CC's `½log2` is **2** (the `4` is against the blueprint's `¼log2`). | Corrected in D.16.0; §6bis row 8 was already right. | None. |

---

## 2. What survives unchanged

The auditor's §0 lists it and I re-checked nothing there, by design (a builder who "re-verifies" a
hostile confirmation adds nothing). For the record, the statements that were re-derived from scratch by
the auditor and stand without amendment are: Theorem D.15.1 in full (including the novelty claim (α)
against `phase-15/M2`'s rank-one `2λ⊗λ` on even tests); Theorem D.15.2 (a)⇔(b)⇔(c), (d), (e) and the
`R^{1,2}` counterexample; Theorem D.15.2c's absorbing property; Theorem D.15.3; Theorems D.15.4,
D.15.4b, D.15.4c and the constraint D.15.4d; Theorem D.16.0/D.16.0a; Theorem D.16.1(a),(b),(c),(e);
Theorems D.16.2, D.16.2′ (crossing height `2πe·e^{2T}`), D.16.2″ (CC's line numbers), D.16.2‴(1)–(3);
Theorem D.17.1b; Lemma D.17.2a (the Laplace identity and the partial-fraction step); Theorem D.17.2
(both directions, including the observation that meromorphy on `C` makes the argument *immune* to the
supremum of `Re ρ` not being attained — the blueprint's own worry); Lemma D.17.2c; Proposition
D.17.3a(i)–(iv) and D.17.3b(a),(c),(e); Theorem D.17.4(i)–(iv); blueprint refutations B-1, B-2, B-4,
B-5, B-6, B-7, B-8; the paper-facing items P46-1…P46-4; and the §6bis corpus check (five rows spot-read
verbatim).

**In particular the two substantive contributions of the phase survive hostile re-derivation intact:**
the `I_∞`-orthogonal splitting `D^W = Λ ⊥ P^W` into a hyperbolic plane and the zero form — with the
consequence (Theorem D.16.2‴) that no ruling-side structure can detect — and the equimodularity
criterion (Theorem D.15.4b) with its effective `Ξ_a` witness (Theorem D.15.4) and its `ζ_K` ceiling
(D.15.4d). So does the negative answer to **Q**.

---

## 3. New and amended open items

| id | statement | label |
|---|---|---|
| D.15-γ | Does `E` have empty interior on all of `D^W` in a topology finer than `‖·‖₁`? Round 1's claim is withdrawn (H2); the question is not needed downstream. | `OPEN` |
| D.17-β | Is `√C_Pó := {F ∈ D^W : F⋆F^∨ ∈ C_Pó}` convex (hence a cone)? Only then is "the Pólya cone is detecting" a statement in the sense of Definition 0.1 (H1). | `OPEN` |
| D.17-α | *(expanded)* Attribution of Theorem D.17.2, with the named sources to check (H8). | `OPEN` |
| D.15-β | *(unchanged, now cross-referenced from D.15.2c and P46-4)* a description of the ample cone that does not quantify over `I_∞` (H10). | `OPEN` |

`OPEN` D.16-α, D.16-β, D.16-γ and D.15-α are unchanged.

---

## 4. Answer to **Q** after audit, and the recommendation

Written as **§7bis of `R138_001_BUILDER_ROUND1.md`**, per the coordinator's instruction, as one
labelled paragraph plus a recommendation. In summary: **Q is answered negatively**, and the obstruction
is located — detection and structural signature sit on complementary `I_∞`-orthogonal summands, the
polar block satisfies the Hodge index identically, the one structurally signed zero-free cone
(`Λ_ξ^+`) is maximally non-detecting, detection is cheap but carries the PNT error term, and the
separating invariant (equimodularity of `|p−½|`) has a proved ceiling at `ζ_K`. **In my judgement the
phase has reached its result**; what remains inside it is bookkeeping. My recommendation for phase 139,
for the lead to accept or reject, is in §7bis: (1) settle the shape of `OPEN` D.16-γ — a cone cut out
by the **zero datum** `Z(F)`, the one unexplored quadrant — as a theorem-or-refutation; (2) develop
equimodularity as a *classification* of admissible `Z`, never as a sign, respecting the `ζ_K` ceiling;
(3) do the cheap attribution search D.17-α; (4) do **not** reopen the Pólya cone, the `log 2` window,
the ample cone without D.15-β, or `h⁰` growth.

**Label: unchanged. No label change for row D.** No sign, no `h⁰`, no cone meeting all three clauses of
**Q**. The FATAL screen is clean, and the one place a FATAL could hide — deriving the sign from
equimodularity — remains flagged and blocked in D.15.4d.

*End of R138.003.*
