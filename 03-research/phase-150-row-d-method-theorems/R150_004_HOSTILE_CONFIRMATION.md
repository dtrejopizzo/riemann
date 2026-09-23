# R150.004 — Hostile confirmation pass on the round-2 repairs

*Hostile confirmer: Opus 5 (1M), 2026-09-19. Targets: `R150_002_HOSTILE_AUDIT.md` §5 (nine repairs)
and `R150_003_BUILDER_ROUND2.md`. Posture: the repairs are assumed cosmetic until the text proves
otherwise. Rules obeyed: pure mathematics; no sign is claimed; row D keeps no label.*

---

## §0. Verdict table

### (a) The nine repairs

| # | repair ordered | where in R150_003 | verdict |
|---|---|---|---|
| 1 | Lemma 4.2 range → `|γ| ≤ N^{1/2−ε}` | §4.1, Lemma 4.2′ | **CONFIRMED** — implemented with a corrected proof, not paraphrased; the endpoint failure is printed and the old range explicitly withdrawn |
| 2 | Thm 4.8: drop C3, C5, C7 from the coefficient-blind list | §4.3, §4.5 | **CONFIRMED, exceeded** — the builder finds *six* of seven fail Def. 4.4 (only C4 survives), withdraws the round-1 proof entirely and re-proves as a finite case check; C1–C3 now go through Lemma 4.2′, not Thm 4.5 |
| 3 | Thm 4.7 + Cor. 4.7a withdrawn or restated with coupled ranges | §4.4 | **CONFIRMED** — withdrawn outright, with the coupling argument and the Friedlander–Iwaniec refutation both printed; C6 recorded `OPEN` (O-150.7) rather than patched |
| 4 | Cor. 5.5 exponent arithmetic | §5.3, Prop. 5.5′ | **CONFIRMED** — withdrawn; Prop. 5.5′ re-derived and verified here (Cauchy–Schwarz on a support of size `≤ kL` gives `E_{2k} ≥ L^{2k−1}/k`; `(|ℱ|+kL)E_{2k} ≥ L^{2k} > L^{k+o(1)}`, `k ≥ 1`) |
| 5 | Import 2.3's continuation inference deleted; Prop. 2.5 relabelled | §2.1 | **CONFIRMED** — inference deleted as false with the divergent-integral proof; Prop. 2.5 deleted, not relabelled, and absorbed into an explicit hypothesis |
| 6 | §2.5 rows demoted to non-implications; function-field counterexample printed | §2.4 | **CONFIRMED** — row 1's structural claim withdrawn, both counterexamples (function fields; the rational primes) printed, all six rows re-stated model-theoretically |
| 7 | "Triangle" and joint-necessity corollary dropped | §2.5, Prop. 2.10′ | **CONFIRMED** — Thm 2.10/Rmk 2.11 withdrawn; three separate non-implications, each naming the conclusion it kills |
| 8 | Out-of-`𝒞` table added; "smooth regime forbids cancellation" weakened | §3, §4.6, §4.7 | **CONFIRMED** — the sentence is withdrawn and replaced by a proof attempt (Thm 4.12/4.13); `𝒞`-completeness `REFUTED as a curated list`; the cusp-form contrast is printed |
| 9 | T5 scope = single-fibre extraction; 5.6/5.7 fixed; 5.8 → `ANALOGY` | §5.1, §5.4, §5.5 | **CONFIRMED as implemented** — but the *substance* of the 5.7 repair is wrong; see D-1 |

**No repair was paraphrased. All nine are in the text with proofs or withdrawals, and in three places
(2, 3, 5) the builder goes further than ordered.**

### (b)–(f) The new material and the standing requirements

| item | verdict | one-line reason |
|---|---|---|
| **Def. 4.11** | **STILL OPEN** (D-4) | `m(s)` and `θ` are declared and never used; the "polar" clause is never applied outside `−ζ'/ζ` and `1/ζ` |
| **Thm 4.12** — proof | **CONFIRMED** | both directions are correct; the Mellin identity `∫_1^∞(ψ(x)−x)x^{−s−1}dx = −(1/s)(ζ'/ζ)(s) − 1/(s−1)` checks, and the quantifier "for all `ε > 0`" is exactly what makes `σ > θ` absolute convergence work |
| **Thm 4.12** — "Landau" attribution | **NEW DEFECT (D-3)** | the (⇒) direction is plain absolute convergence + uniqueness of continuation; Landau's abscissa theorem needs *one-signed* coefficients and `ψ(x) − x` is not one-signed, so it is *not* what is used |
| **Thm 4.12** — uniformity | **CONFIRMED** | the stated uniformity ("all `x ≥ 2`, all `ε`") is genuine and necessary; dropping "all `ε`" breaks (⇒) |
| **Thm 4.12** — novelty | **classical** | von Koch (1901) / Landau; textbook (Ingham; Montgomery–Vaughan Thm 13.1). The builder's §7 label says so; **§0 and §3 contradict it** (D-5) |
| **Thm 4.13** — convolution trick | **CONFIRMED (proof correct)** | `P_{s_0}(s) = 1 − 2^{s_0}2^{−s}` has zeros exactly at `s_0 + 2πik/\log 2`; `B(x) = Σ_d c_d A(x/d) ≪ (Σ|c_d|d^{−θ−ε})x^{θ+ε}` — the power saving really is preserved, the constant really does depend only on `S, ε`, and `b_n ≪_S n^{ε}` so the class is not changed |
| **Thm 4.13** — "any prescribed zero configuration" | **NEW DEFECT (D-2)** | the construction can only **add** zeros, and it adds a whole vertical progression of spacing `2π/\log 2` around each planted point. It cannot remove a zero and cannot plant an isolated one. What is proved: *any finite `S` can be included in the zero set* |
| **Thm 4.13** — novelty | **folklore** | multiplying a Dirichlet series by a finite Dirichlet polynomial and tracking partial sums is routine; the *classification* it serves is what is new in this corpus, and only there |
| **Cor. 4.13a** | **STILL OPEN** (minor) | Thm 4.13 is about the auxiliary `b`, not about `λ_f`; the correct reading is "the bound *alone* implies nothing", which is what §18.3.2 says and what 4.13a does not |
| **Prop. 5.5′** | **CONFIRMED** | re-derived independently; correct, and strictly more conservative than the withdrawn Cor. 5.5 |
| **Prop. 5.7 (corrected)** | **NEW DEFECT (D-1)** | the "correction" repairs a non-existent error: `‖b*b‖_2² = E(b)` for **every** complex `b`, by Parseval |
| **Prop. 5.6, 5.8** | **CONFIRMED** | per-case normalisation stated; 5.8 demoted to `ANALOGY` with the reason given |
| **Prop. 2.6′** | **NEW DEFECT (D-6)** | labelled `PROVED`, but the ⟸ half is a completeness claim and no formal system is specified; BE1–BE8 are not first-order. T3 uses only soundness |
| **(d) (H-DMV) as hypothesis** | **CONFIRMED** | `HYPOTHESIS`, explicitly "not `IMPORTED`, not `PROVED`"; `grep` finds no surviving `IMPORTED` label in the document. One unlabelled sentence remains (D-7) |
| **(e) FATAL rule** | **CONFIRMED (not triggered)** | re-run independently: no zero-free region, no moment bound, no cancellation statement, no chain below trivial, no `ζ(½+it)` exponent. Thm 4.13 *constructs* a saving it inherits; Thm 4.12 bounds no `β_max` |
| **(f) Gates** | **CONFIRMED with one over-claim (D-8)** | the four-falsifier × four-theorem table is complete and field-uniformity is recorded; but two cells assert Thm 4.12 for `ζ_𝒫` and `Ξ_Q`, whose (⇐) half needs an explicit formula with zero-density control not available from BE1–BE8 |
| **No sign / row D** | **CONFIRMED** | no sign is claimed anywhere; row D takes no label |

---

## §1. The new defects, in order of damage

**D-1 (the only real error). Prop. 5.7's repair corrects a non-error, and the round-1 identification
was right.** Both the audit (§3.3) and the builder (§5.4) assert that `‖b*b‖_2²` and the additive
energy `E(b) = ‖b ⋆ \bar b‖_2²` differ for complex `b` and agree only for real `b`. **They are equal
for every finitely supported complex `b`.** Write `\hat b(α) = Σ_n b_n e(nα)`. Then `b*b` has
transform `\hat b(α)²` and `b ⋆ \bar b` has transform `|\hat b(−α)|²`; by Parseval both squared
`L²`-norms equal `∫_0^1|\hat b(α)|^4 dα`. So `‖b*b‖_2² = E(b)` identically, in particular for the
centered complex `b = Λ − M_Q` of D.59. The withdrawal in §5.4 ("the identification made in round 1
is unjustified and is withdrawn") should itself be withdrawn; the quantity the extraction needs is
the additive energy, as round 1 said. **The multiplicative half of §5.4 is untouched and correct:**
for `ψ_t(n) = n^{−it}` the convolution is Dirichlet, the invariant is a multiplicative-energy count,
and removing the archimedean row from the table is right. Net effect: Prop. 5.7 should read `PROVED`
for the additive family **with `E(b)` restored**, and the `OPEN` Hardy–Littlewood target is unchanged.

**D-2. Thm 4.13 over-states its conclusion.** "compatible with **any** prescribed zero configuration
of `D_a` in `Re s > θ`" is not what the proof gives. `P_{s_0}` vanishes on the full progression
`s_0 + 2πik/\log 2`, so every planted zero drags in infinitely many companions; and no zero of `D_a`
can be removed by multiplication. Repair (one line): *for any finite `S ⊂ \{Re s > θ\}` there is `b`
with the same power saving whose Dirichlet series vanishes on `S`.* That suffices for the intended
use — the implication "power saving ⟹ zero constraint" is false — and it is what §18.3.2 already
says correctly. The overstatement is in §4.6 only.

**D-3. "Landau's theorem on the abscissa" is the wrong name for the step actually used.** Landau's
theorem requires eventually-one-signed coefficients; `ψ(x) − x` changes sign infinitely often
(Littlewood). The step used is: absolute convergence of `∫_1^∞|ψ(x)−x|x^{−σ−1}dx` for `σ > θ` gives
holomorphy there, and uniqueness of continuation contradicts the pole at `ρ`. That argument is
correct. Only the attribution is wrong, and it matters because BE8 ("Landau's theorem") is an axiom
elsewhere in the same document, so the misnomer silently suggests a dependence that does not exist.

**D-4. Def. 4.11 carries dead parameters and Thm 4.12 does not prove the general polar case.** `m(s)`
is declared and never used; `θ ∈ [½,1)` is declared inside the definition but only the entire clause
uses it. Thm 4.12 is stated for `D_a = −ζ'/ζ` and Cor. 4.12a adds `1/ζ` — two instances, not the
class. The general statement (a pole of `D_a − m` at `ρ` obstructs `A(x) ≪ x^{θ+ε}`) is true by the
same argument, but it is not written, so "classification" currently means "two examples and a name".

**D-5. Internal inconsistency about novelty.** §0 and §3 call §4.6 "the one genuinely new item in
round 2" / "the only new mathematics in this round"; §1 and §7 correctly label Thm 4.12 "classical
von Koch/Landau; new *in this corpus* as a classification". The §7 wording is the defensible one and
the §0/§3 wording should be brought into line with it.

**D-6. Prop. 2.6′ is labelled `PROVED` and is not proved.** "`(ZFS_δ)` is derivable from BE1–BE8 iff
it holds in every model" is soundness (⟹) plus completeness (⟸). No deductive calculus is fixed, and
BE1–BE8 quantify over meromorphic continuation and growth, so they are not first-order and Gödel
completeness is unavailable. **Thm 2.8′ uses only the soundness half**, which is immediate. Repair:
state 2.6′ as soundness alone, `PROVED`; drop the "if and only if".

**D-7. One unlabelled claim about an unread source.** §2.1's first bullet ("the construction goes in
the direction zeta → system … the meromorphic continuation and the location of the zeros are part of
the construction") is asserted as "what I can defend" with no label, while the following bullet
labels everything else `CERTIFIED`. It is a structural claim about a paper the builder states he has
not read. It should carry `CERTIFIED` too, or be folded into (H-DMV). Nothing is labelled `IMPORTED`;
requirement (d) is otherwise met.

**D-8. Two gate cells assert Thm 4.12 beyond its proof.** §6.1 row "Thm 4.12/4.13": for `ζ_𝒫` and for
`Ξ_Q` the *equivalence* is asserted. The (⇒) half transfers (absolute convergence + a pole), but the
(⇐) half is the truncated explicit formula, which needs a zero-counting estimate and controlled
growth on a contour — available for `ζ` and `ζ_K`, **not** derivable from BE1–BE8 and not recorded
for `Z_Q`. Repair: in those two cells claim the (⇒) direction only.

**Minor, carried over unfixed from round 1.** Thm 5.4's displayed chain reads
"`|S_{f_0}| ≤ M_{2k}^{1/2k} ≤ L(k(|ℱ|+kL)/L)^{1/2k} ≥ L`" — a `≤ … ≥` chain that does not parse.
The intended statement (the bound is `≥ L`, hence never non-trivial) is correct; the display is not.

---

## §2. What stands

Lemma 4.2′, Cor. 4.3, Thm 4.5 (as a normalisation lemma), Thm 4.8′ as a finite case check over
`{C1,…,C5}` with C6/C7 `OPEN`, Thm 4.12 (with D-3's attribution fixed), Thm 4.13 (with D-2's
conclusion narrowed), Thm 5.3/5.4, Prop. 5.5′, Prop. 5.6, Prop. 5.7 (with `E(b)` **restored**, D-1),
Prop. 5.8 as `ANALOGY`, Prop. 2.10′, the §2.5 non-implication table, and T3 as a meta-theorem
conditional on (H-DMV) with O-150.1 blocking. The §9 paper text is defensible after D-1, D-2, D-3 are
applied; §18.3.2 is already worded correctly and needs only the attribution fix.

**No new FATAL. No sign is claimed in this document. Row D takes no label from phase 150.**

---

*End of `R150_004`. Nine repairs confirmed implemented; eight new defects, one of them a wrong
correction that should be reverted.*
