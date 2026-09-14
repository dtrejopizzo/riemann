# R134.005 — hostile audit of record, round 2 (Paper 46, row D opening)

Auditor: adversarial auditor of record (Opus 5), for the session lead.
Date: 2026-09-12.  Target: `04-papers/46-row-d-the-sign/main.md` (1641 lines)
and `README.md`, against `R134_002_AUDIT_ROUND1.md` (M1–M7, m1–m9, n1–n3),
`R134_003_LEAD_AUDIT_ROUND1.md` (LF1–LF3), `R134_004_BUILDER_ROUND2.md`, the
four `[phase 134]` notes in phase 124 and the one in phase 118, and both
scripts re-run.

**Headline.  The no-sign rule still holds, and every one of M1–M7, m1–m9 and
LF1–LF3 has been carried out — but the repair of `(M1)` overshot and
introduced the worst defect the campaign has produced: `Proposition 3.6a(iii)`
("`Π²W_{fin} ∉ S'(R)`", labelled `PROVED`) is not proved, and **it is false if
RH is true**.  Worse, combined with the paper's own Theorem 3.6 and
Theorem 3.7 it yields a proof of ¬RH inside Paper 46.  This is `FATAL` for
that one proposition and for the `PROVED` label on it; it costs nothing else —
Theorem 3.7 is *unaffected*, because the `D'` form of Bochner–Schwartz needs
no temperedness hypothesis at all, which is exactly why (M1)'s repair (i)+(ii)
was the right repair and (iii) was an unnecessary extra. One further `MAJOR`:
Definition 6.8's rebuilt requirement list is inconsistent unless the duality
`F ↦ F^∨` moves the primitive sector off itself, and no clause says so.
Everything else in round 2 is accepted.  Both scripts reproduce every printed
number.  Recommendation: the paper is **fit to stand as Paper 46's opening
state after one bounded erratum** (delete 3.6a(iii), repair (X11), §9.1(13),
§10's grade row and the README sentence); no label; D.3 retired as a programme
item.**

---

## 0. Reproduction performed (my own re-runs, not the builder's numbers)

* `d134_gram.py --model zeta --N 10 30 --eps 2.0 1.0 0.5 0.3 0.1 --check`
  (80 s): the `--check` validation table (`1.476009 / 1.470692 / 1.469943`
  against `K = 1.469694`; `0.944048 / 0.943006 / 0.942858` against
  `0.942809` with the atom `0.490129`; `1.213439 / 1.210805 / 1.210432`
  against `1.210307`) and the whole `ζ` inertia column — `(0,0,7)` and
  `(0,0,27)` at every `ε`, full `G` inertia `(1,0,8)` / `(1,0,28)` —
  reproduce **exactly**.
* `d134_sigma.py --model zeta --tmin 0.72 --tmax 2.2 --steps 8`:
  `𝔅_T = [[0.11264,0.0767],[0.0767,0.11264]]`, `Σ(0.72) =
  [[0.0764,0.05055],[0.05055,0.0764]]`, swap defects `7.08·10^{−15} …
  4.12·10^{−13}`, and the non-monotone `λ_{\min}Σ` sequence
  `2.58, 1.83, 2.75, 3.45, 3.02, 2.30, 2.43, 1.74` (`×10^{−2}`) —
  **exactly** the paper's Observation 4.7 and Theorem 4.2(iii) row
  `refine = 2`.  The script now prints "frak-B_T (the Tate BLOCK, not the
  ruling plane)", so (M7) reached the apparatus too.
* Docstring of `d134_gram.py` re-read: (m6) is discharged — Lemma 5.1a is
  named as what defines the entries, 8bis.1e is flagged "NOT satisfied at any
  `(N,eps)` of the reported tables", the stale `−\log(1/ε)+γ+\log 4π`
  reference is replaced by `(c_φ/ε)(−\log(1/ε)+C_φ)`, `GAMMA_E` is gone.

**No numerical claim in the paper changed in round 2, and none of them is
wrong.**  My entire quarrel with round 2 is in §3.

---

## 1. Findings of round 2, graded

### FATAL

**(F1) Proposition 3.6a(iii) is not proved, and is false under RH; as it
stands the paper proves ¬RH.**  *Location:* main.md ll. 385–391 (the
proposition), l. 1462 ((X11)), l. 1500 (§9.1(13)), l. 1613 (§10's grade
table), README "Proposition 3.6a proves that `W_{fin}` and `Π²W_{fin}` are
**not tempered**".

*(a) The proof is invalid.*  The argument is
`⟨Π²W_{fin},φ⟩ = ⟨W_{fin},Π²φ⟩ = ⟨W_{fin},ψ⟩ = ∞` with `φ := Π^{−2}ψ`.
`φ ∈ S(R)` — that part is right (`\hatφ = \hatψ/(¼+τ²)²`, and `(¼+τ²)^{−2}` is
a multiplier of `S`; equivalently `φ = e^{−|·|/2}∗e^{−|·|/2}∗ψ`, which decays
like `e^{−|t|^{1/2}}`, i.e. rapidly).  But `φ` is **not compactly supported**,
and transposition of a differential operator across the pairing
`⟨·,·⟩ : D'×D` is available only for test functions in `D(R)`.  Both sides of
the first equality presuppose that `Π²W_{fin}` is already tempered, which is
the thing being denied.  So the display is a formal manipulation with no
theorem under it.  The gap is not cosmetic: it is exactly where the argument
throws away a cancellation, because `Π²` **annihilates** the growth that makes
`⟨W_{fin},ψ⟩` diverge.

*(b) The proposition is false under RH.*  `Π²ϖ = 0` is the paper's own
Theorem 3.6.  Hence, with `ν := W_{fin} − ϖ\,dt`,

    Π²W_{fin} = Π²ν   exactly.

Let `M(t) := Σ_{2≤n≤e^{t}}Λ(n)n^{−1/2}` and `∫_0^tϖ = 4\sinh(t/2)
= 2e^{t/2}+O(1)`.  Under RH, `ψ(x) = x + O(\sqrt x\log²x)`, and partial
summation gives `M(t) = 2e^{t/2} + O(t³)`.  So the distribution function of
`ν` is **polynomially bounded**, hence `ν ∈ S'(R)` (a locally integrable
function of polynomial growth, differentiated once), hence
`Π²W_{fin} = Π²ν ∈ S'(R)`.  **RH ⟹ Proposition 3.6a(iii) is false.**
Contrapositively, proving 3.6a(iii) would prove ¬RH — and the paper labels it
`PROVED`.

*(c) The internal contradiction is explicit and two lines long.*
`ω_∞ = K(|t|)dt` with the (8.5∞) finite part is tempered (`K(t) ∼ 1/2t` at `0`
after finite part, `K(t) ∼ e^{−t/2}` at `∞`), so `Π²ω_∞ ∈ S'`.  Therefore
`𝔏 = −Π²W_{fin} − Π²ω_∞` is tempered **iff** `Π²W_{fin}` is.  By 3.6a(iii),
`𝔏 ∉ S'`.  By Theorem 3.7 (c) ⟹ (d), `𝔏` positive-definite on `D(R)` would
force `𝔏` tempered.  Hence `𝔏` is not positive-definite, hence ¬(b),
hence ¬(a): **¬RH, proved in §3 of Paper 46.**  The paper half-sees this and
writes the opposite: §9.1(13) says "whether `𝔏` itself (as opposed to its
finite half `Π²W_{fin}`) fails to be tempered is not decided here".  Given
3.6a(iii) it *is* decided, immediately.  §9.1(13) and Prop 3.6a(iii) cannot
both stand.

*Repair (bounded, and it improves the paper).*  Keep 3.6a(i) and (ii) —
`ϖ ∉ S'` and `W_{fin} ∉ S'` are **correct and rigorous** (both are pairings of
a positive object against a nonnegative Schwartz `ψ`, and the compactly
supported truncations `ψ_j ↑ ψ` are bounded in every `S`-seminorm while
`⟨W_{fin},ψ_j⟩ → ∞` by monotone convergence — that is a real
non-temperedness proof, and it is all that is needed to refute round 1's
justification).  **Delete (iii)** and replace it by the true remark:

> `Π²` annihilates `ϖ`, so `Π²W_{fin} = Π²(W_{fin} − ϖ\,dt)`, and the
> temperedness of `𝔏` is *not* refutable by growth: under RH it holds
> (`M(t) = 2e^{t/2}+O(t³)`), and by Theorem 3.7 (c)⇒(d) it is implied by the
> target.  **No a priori temperedness is available and none may be denied**;
> that is exactly why the `D'(R)` form of Bochner–Schwartz is the import.

That remark is *better* motivation for (X3) than the false one, and it is the
kind of statement the rest of the paper is good at.  Then fix (X11)
("the non-temperedness of `W_{fin}` and of `Π²W_{fin}`" → `W_{fin}` only),
§9.1(13) (now correct as written, and becomes informative: the temperedness of
`𝔏` is implied by the target and is not decidable here in either direction),
§10's grade row, and the README sentence.

*What does **not** change.*  Theorem 3.6, `Πϖ = 0`, `𝔏 ∈ D'(R)`, the typing,
(m1)'s `c = 0` paragraph, Theorem 3.7 in all five clauses, (X3), the
uniqueness line for (d)⇒(e), and the `RESTATEMENT` grade.  **Nothing else in
the paper touches Proposition 3.6a.**  The cost of this finding is one
proposition and four cross-references.

### MAJOR

**(R2-1) Definition 6.8's rebuilt list is inconsistent unless `∨` moves the
primitive sector, and no clause says so.**  *Location:* ll. 1290–1305.
(R4) is `h(F) = 0` for **every** primitive `F`; (R3) is
`h(F) − h(F^∨) = ½I_∞(F,F) + ℓ(M(F)) + χ`.  If the duality `F ↦ F^∨` preserves
primitivity — and `†`, the only duality actually available on `Corr_A^{tr}` in
Papers 43–44, does preserve it (`λ_∓(Γ_h^†) = λ_±(Γ_h)`) — then `h(F^∨) = 0`
too, and (6.1) reads `0 = ½I_∞(F,F) + χ` for every primitive `F`: `I_∞(F,F)`
constant on the primitive sector.  That is false by homogeneity
(`F ↦ λF` scales `I_∞` by `λ²`) unless `I_∞ ≡ 0` there, which Theorem 14.1
forbids.  **So (R1)–(R4) as printed are satisfied by no `h` whatever, for the
one duality the corpus supplies** — the requirement list is vacuous, not
merely unfulfilled.  *Repair:* add **(R5)**: *the duality must carry the
primitive sector off itself* (in Weil's own argument it does: `F ↦ K − F`),
and say which duality is intended; or weaken (R4) to a *sub*class of primitive
classes on which the vanishing is asserted, with `∨` mapping it out.  The
direction of (6.2) is **correct** as repaired by (M3) — I re-derived it:
`M(F) = 0`, `h(F) = 0` ⟹ `I_∞(F,F) = −2h(F^∨) − 2χ ≤ −2χ ≤ 0` for `χ ≥ 0` ✓ —
and the disclaimer under it is adequate.  It is the *consistency* of the list,
not its direction, that is now the defect.

### MINOR

**(r1) Remark 6.8a's `h⁰_{eff}` row is right in substance, wrong in two
words.**  `h⁰_{eff}(F) = 1` if `F ∈ Eff_A^{tr}`, else `0`.  On a **nonzero**
primitive `F` it is `0` ✓ — but `F = 0` is primitive and `0 ∈ Eff_A^{tr}`, so
`h⁰_{eff}(0) = 1 ≠ 0` and (R4) fails at the origin.  And the vanishing is not
"vacuous": it is a *value*, forced by Theorem 6.1.  Say "`h⁰_{eff}` vanishes on
every nonzero primitive class, by Theorem 6.1, and fails (R3)".  The
sharpening the builder is proud of — *the one candidate that satisfies the
vanishing theorem has no Riemann–Roch identity at all* — **survives** and is
correctly the best line in Remark 6.8a.

**(r2) (1.13) misdirects the one cross-reference that matters.**  l. 161:
"inside D.1's classical equivalence (**Theorem 3.6**), where the equivalence
*is* with RH".  Theorem 3.6 is the distribution identity and contains no
statement about zeros; the equivalence with RH is **Theorem 3.7**.  In the
clause that defines this paper's compliance with the zeros rule, the wrong
theorem number is cited.

**(r3) README's file table still calls the Tate block `B_T`**
("`d134_sigma.py` … swap law, `B_T`, monotonicity"), the one surviving
instance of the (M7) collision outside main.md.  main.md itself is clean: bare
`B_T` occurs at ll. 128, 129, 584, 587, 606 only, every one of them the ruling
plane or §4.2's statement of the conflation — (M7) is **discharged in the
paper**.

**(r4) `R134_004`'s grep evidence is inflated in two places**
(`grep -c '𝔅_T'` → `19`, not `24`; the bare-`B_T` list is 5 lines, as the
report says).  The paper is right, the report is loose — the same `(m9)` habit
as round 1, one round later.

**(r5) `d134_gram.py`'s repaired docstring has a broken indent** at the
`Paper 44 Thm 8bis.1e` line (flush left inside an indented block).  Cosmetic.

**(r6) The phase-124 note omits the quadrature caveat the phase-118 note
carries.**  P124.014's `[phase 134]` note says the refined values "are
certificates"; the phase-118 note says "a certificate (**up to quadrature
error**)".  The weaker, correct phrasing should be in both.

### NOTE

**(n4)** `Π^{−2}` *is* well defined on `S(R)` and preserves it, and the
convolution `e^{−|t|/2}∗e^{−|t|/2}∗ψ` of a Schwartz function is Schwartz —
the lead's question is answered in the affirmative, and Proposition 3.6a gets
that part right.  The defect (F1) is **not** there; it is in the transposition
and in the conclusion drawn from it.

**(n5)** Warning 4.5a is adequate and closes (n1) of round 1, as round 1 asked.
Its carve-out for Theorem 4.2(iii) is stated honestly (the builder's own press
point 3 concedes the determinant's stability is empirical over five
resolutions and is not a bound) and I concur with the concession: (iii) keeps
its `COMPUTATIONAL-ILLUSTRATION` label and is used only in the falsifying
direction, which is permitted.

---

## 2. Disposition of every round-1 item

| item | disposition | verdict |
|---|---|---|
| **(M1)** = **LF1** | repair (i) `Πϖ = 0` and the typing `𝔏 ∈ D'(R)`: **carried out, correct, and it shortens the object**.  Repair (ii) the `D'` form of (X3): **carried out, correct** — (c)⇒(d) now needs no hypothesis, (d)⇒(c) is stated as the elementary direction.  The *extra* Proposition 3.6a(iii): **overshoot, `FATAL` (F1)** | **partially discharged; (F1) open** |
| **(M2)** | re-attribution to Paper 45 **Lemma 5.1a** with `c = 0`, plus polarization, plus 8bis.1e demoted to "interpretation only" in the regime `ε = O(1/N)`, plus the two `W`/`S` regime columns, **all twelve rows `✗`**, plus the `ε = 2.0` (`\max|Δ| = \log15 = 2.71 < 4`) and `ε = 0.5` computations in words.  I checked the polarization: `Q(f) = T_∞(Γ_{f⋆f^†})` is a real quadratic form because Lemma 5.1a is **linear in `h`** and `f ↦ f⋆g^†` is bilinear over `R`; all `h_n` are real, so `¼[Q(h_m+h_n)−Q(h_m−h_n)]` is the symmetric bilinear form, legitimately, at every `ε` ✓.  The claim that round 1's displayed entry diverges when `0 ∈ supp` is **correct** (`∫K(|t|)ψ_ε(t)dt = ∞` since `K ∼ 1/2t`), and the diagonal is finite only because the script works in `τ`-space against `\hat W_∞` — which is Lemma 5.1a's second term.  **The numbers are unchanged and I reproduced them.** | **discharged, exemplary** |
| **(M3)** | Def 6.8 rebuilt with (R2) on the dual and (R4) on the primitive side; (6.2) now gives `I_∞ ≤ −2χ ≤ 0` ✓ direction correct; the disclaimer under the display is explicit; Remark 6.8a re-tests all five negatives.  `h⁰_{eff}`'s status is **right in substance** (passes the vanishing, fails (R3)) and loose in two words (r1) | **discharged, with (R2-1) and (r1) newly open** |
| **(M4)** | Theorem 5.4 → **Remark 5.4**, keeping (i) dimension, (ii) non-membership of the concentration profiles, (iii) `OPEN` for the colimit; `grep "Theorem 5.4"` → one hit, inside the downgrade bracket; §5.2's `REFUTED` now reads "carried by Theorem 5.5"; §9.1 item 12 and §9.2's row record the withdrawal | **discharged** |
| **(M5)** | Finding 4.8 rebuilt in three parts with the inequality `λ_{\min}(C^{\mathsf T}ΣC) ≥ ‖C‖²λ_{\min}(Σ)` for `λ_{\min}(Σ) ≤ 0`; the withdrawal is explicit; (ii)'s witness `2.35·10^{−2}` vs `2.77·10^{−3}` at `T = 1.67`; (iii) Sylvester imported as (X12).  Recommendation unchanged in content, weaker in reason, and says so | **discharged** |
| **(M6)** | **Warning 4.5a**, with my `refine = 2…6` sweep reproduced to all printed digits, and the sentence "every positive value … certifies nothing" in bold; §4.3's verification paragraph, Theorem 4.2(iii) and §9.1(11) each carry their own scope sentence.  This is exactly what I asked for | **discharged** |
| **(M7)** | `𝔅_T` throughout (19 occurrences); bare `B_T` only at the five ruling-plane/collision lines; the convention announced in bold in (1.8) with the reason; §4.2's title rewritten; the **script** prints the disambiguation too.  One residue in README (r3) | **discharged in the paper** |
| **(m1)** | (3.2) now states the non-integrability, the `κδ_0` ambiguity, `⟨Π²(κδ_0),g⋆g^†⟩ = κ‖Πg‖²`, and that `c = 0` **is** the definition; repeated in Remark 3.8(2) | discharged |
| **(m2)** | the even/odd quantifier line is present and correct | discharged |
| **(m3)**, **(m4)** | Definition 5.1(d): `(C1)` off-diagonal, 8bis.2's exemption on the diagonal, purely archimedean constant in `2ε < \log 2` | discharged |
| **(m5)** | Theorem 5.2's clause rewritten; the proof now reads as a proof | discharged |
| **(m6)** | docstring rebuilt, `GAMMA_E` deleted, `verbose` reference corrected; (r5) is a typographical residue | discharged |
| **(m7)** | the mechanism is stated as I state it; the arithmetic matches | discharged |
| **(m8)** | Theorem 4.2(iii) prints the five-row sweep with "the *entries* may not be quoted as converged"; `\det 𝔅_T > 0` shown stable | discharged |
| **(m9)** | corrected to the paper's split | discharged |
| **(n1)–(n3)** | closed by Warning 4.5a as requested | discharged |
| **LF1** | = (M1); see above | partially discharged |
| **LF2** | Theorem 3.7 is now headed `RESTATEMENT (CLASSICAL + PROVED-IN-REPOSITORY)`, its `∎` line names the assembly (X2)–(X5)+(1.9)+(1.10)+Lemma 3.1+Theorem 3.6, Lemma 3.1 and Theorem 3.6 are carved out at `PROVED`, Remark 3.8(2)'s round-1 phrase is **withdrawn on evidence**, and §10's grade table agrees.  I re-searched for a proof that uses the modulus-group identification for anything but naming and again found **none**.  **LF2 is correctly graded and correctly evidenced** | discharged |
| **LF3** | all five notes read.  They are **accurate and scoped**: P124.013's note carries the *corrected* (M5), not round 1's claim, and its ledger row is updated; P124.014's note is explicitly "within the declared scope" of its own one-resolution disclaimer, gives both re-runs, and states that the qualitative conclusions (genuine first contact, Gate R fails, case 2 realized) are **unaffected** ✓; the phase-124 README's five-point note is a methodological note, not a retraction; the phase-118 note "retracts nothing", and **explicitly does not touch the interval-arithmetic `T = \log 2` endpoint certificate replayed in P123.036** ✓.  No qualitative conclusion of either phase is altered.  One omission: (r6) | discharged |

---

## 3. Final verdicts on D.1–D.5

| item | verdict | change from round 1 |
|---|---|---|
| **D.1** (§3) | **`RESTATEMENT`**, with Lemma 3.1 and Theorem 3.6 carved out at `PROVED`.  Theorem 3.7 is **correct as it now stands** and is stronger than round 1's version: the `D'` form of Bochner–Schwartz removes a hypothesis instead of asserting a false one, the uniqueness line for (d)⇒(e) (`D` dense in `S`, Fourier injective on `S'`) is present and correct, and (d)⇒(c) is the elementary direction.  **Proposition 3.6a must be cut back to (i)+(ii)**; at `PROVED` it is `FATAL` (F1) | grade unchanged; §3 otherwise improved; one proposition to withdraw |
| **D.2** (§4) | **`PROVED`** (Thm 4.3 swap law, Cor 4.4, Thm 4.2(i)(ii), Thm 4.6, Finding 4.8) **+ `COMPUTATIONAL-ILLUSTRATION`** (Thm 4.2(iii), Obs 4.7), all under **Warning 4.5a**; Thm 4.1 `PROVED-IN-REPOSITORY`, conditional on `T_q < ∞` | unchanged; (M5)(M6)(M7)(m8) all discharged |
| **D.3** (§5) | **`COMPUTATIONAL`**, with Theorem 5.8 the one genuine theorem, 5.2 and 5.5 structural at `PROVED`, 5.6 conditional on its own hypothesis, Remark 5.4(iii) `OPEN`, the tables `COMPUTATIONAL-ILLUSTRATION` with both regime columns `✗` in every row | unchanged; attribution now correct (M2), 5.4 correctly downgraded (M4) |
| **D.4** (§6) | **`PROVED`** negatives (6.1, 6.3–6.7); the synthesis **`OPEN`** and, as printed, **inconsistent** (R2-1) — (6.2)'s direction is right, the list needs (R5) | direction repaired; consistency newly at issue |
| **D.5** (§7) | **`PROVED`** (7.1, 7.4, 7.5(a)); 7.5(b),(c) declared unanswered.  Untouched by round 2 and still the best-aimed section in the paper | unchanged |

---

## 4. The no-sign check, re-run in full

I grepped and read in context every occurrence of `I_∂`, `q_T`, `Λ`, `𝔏`,
`G_N^{prim}`, `Σ(T)`, `α ± β`, `positive`, `nonnegative`, `≥ 0`, `≤ 0`,
`definite`, `sign`.  **Result: no violation.**  Each sign attached to a target
object is one of the five permitted kinds:

* **the boxed target, quoted**: §0.1, l. 431 (Thm 3.7(b)), §9.1(1), README;
* **a hypothesis**: l. 146 ((1.10), Paper 45 Thm 10.4), l. 171 (`PLAN` §8's
  common target), l. 457 (inside (b)⇒(a)), Theorem 5.6 ("Assume RH"),
  Theorem 4.1 (`T_q < ∞`);
* **an `OPEN` item**: §9.1(1),(4),(5),(6),(7),(12); Remark 5.7; Remark 6.9;
* **RH-conditional or an equivalence *with* RH**: Theorem 3.7, Theorem 5.6;
* **an explicit disclaimer**: Honest remark 4.5 ("No sign is claimed for
  `α ± β`"), Warning 4.5a, §5.4 reading item 4, Definition 6.8's disclaimer
  under (6.2), §10.

The sign statements the paper does **assert** are about other objects —
`\det 𝔅_T > 0` at one `T` and one family of resolutions, `G_N(ε) < 0` for
`ε < ε_1(N)` (unconditional, **for every model**, and presented as a
*deflation*), `λ_∓(F) > 0` on the effective cone — and none is offered as
evidence about the target.  The new display **(6.2)** is a direction check on
a requirement list, labelled as such in the sentence immediately following it.
**§10 reads `None.`**  Statements about the zeros occur only in (1.9),
Theorem 3.7, Theorem 5.6 under its hypothesis, and the explicitly-unused
bracket in §7.1 — the permitted set, though (1.13) misnames its own
cross-reference (r2).

**One caveat, and it is (F1) from the other side:** Proposition 3.6a(iii), if
it were true, *would* be a statement about the zeros — it implies ¬RH.  That
is the deepest reason it must go: the paper's own rule forbids it
independently of whether it is provable.

---

## 5. The builder's press points

1. **Retire D.3 as a programme item, keeping Theorem 5.8?  YES, and I so
   recommend.**  After (M2) the entries are Lemma 5.1a's values; the Frobenius
   reading holds in **no** computed regime (twelve rows, `W` and `S` both `✗`);
   Theorem 5.8 makes the small-`ε` end unconditionally definite for *every*
   model; and what is left — "the two models separate in a window of `ε` of
   order one" — has no theorem behind it and is, by Theorem 5.5, not
   answerable here in either direction.  Retire the **finite-inertia test** as
   a route; keep Theorem 5.8 as its result and Remark 5.9 as its epitaph.  I
   repeat round 1's recommendation not to spend cycles on press point P3
   (`N = 15,20,25`): a finer grid sharpens a statement with no theorem under
   it.
2. **Is the phase-119–123 Galerkin exposure a real open audit item?  Real, but
   narrower than feared — LOW priority.**  I searched: the shared assembly
   (`rowd_assembly`, `p124_lab`) is used in phases **118 and 124 only**;
   phases 119, 121, 122, 123 do not import it.  Phase 120 uses the *same
   piecewise-constant meshes* (`P3_PALEY_WIENER_JULIA_SHORT_CANDIDATE.md` §5,
   `FORCED_GREEN_AUDIT_OF_PHASE106.md` §5) but in the **safe direction**: its
   numbers are operator/Frobenius **residuals** establishing a *failure*, and
   an entrywise agreement check at `6.44·10^{−14}`, neither of which is a
   positive-eigenvalue certificate.  So the standing rule should be recorded
   once in the corpus methodology (as the phase-124 README note now does) and
   a full sweep of 119–123 is **not** worth a round.  I found no statement in
   Papers 43–46 resting on a positive double-precision Galerkin eigenvalue.
3. **Warning 4.5a vs Theorem 4.2(iii):** the builder's own concession is
   correct and adequate; see (n5).  No further action.
4. **Does Prop 3.6a leave a hole in (d)⇒(e)?**  No — the uniqueness line the
   builder added is correct and necessary, and I verified it.  Ironically it
   is the one part of the 3.6a story that improved the paper.

---

## 6. Consistency of §0, §9, §10 and README with the body

Checked line by line.  **Consistent, with three exceptions, all from (F1) and
(r2)/(r3):**

* §0.1 reproduces Paper 45 §14.4's box and the four travelling hypotheses
  verbatim; §0.2's five standing negatives match the body's uses; §0.3's
  D.1–D.5 summary matches §§3–7 **except** that D.1's summary is now honest
  about the grade ("The equivalence is classical … plus row A–C content").
* §8's import table is complete and each row names the clause it serves;
  **(X6)** is corrected to Gershgorin; **(X3)** is correctly restated;
  **(X11)** is **wrong** by (F1) and must lose "`and of Π²W_{fin}`";
  **(X12)**, **(X13)** are new and correctly used.  The two withdrawn imports
  do not occur.
* §9.1's thirteen items are accurate; **item 13 contradicts Prop 3.6a(iii)**
  (F1c) and becomes correct the moment (iii) is deleted.  §9.2's nine rows and
  §9.2a's ten-row repair ledger are faithful to what I verified.  §9.3's three
  corpus findings now match the phase-124/118 notes word for word.
* §10's `None.` and the grade table are consistent with the body, **except**
  the row grading Proposition 3.6a `PROVED`.
* README is consistent with the body **except** the `Π²W_{fin}` sentence (F1)
  and the `B_T` residue (r3).

---

## 7. Recommendation to the lead

**The paper is fit to stand as Paper 46's opening state, after one bounded
erratum — and not before.**  The erratum is five edits:

1. **Cut Proposition 3.6a to (i) and (ii)**, and replace (iii) with the
   correct remark of (F1) — that `Π²ϖ = 0` makes the growth argument
   unavailable, that RH *implies* temperedness of `Π²W_{fin}`, and that this
   is why (X3) is imported in its `D'` form.  Record the withdrawal in §9.2a
   as a **fourth refuted statement of the builder's own**, which is what it is.
2. **(X11)**, **§9.1(13)**, **§10's grade row**, **README** — the four
   cross-references.
3. **Add (R5) to Definition 6.8** (the duality must carry the primitive sector
   off itself), or say which duality is intended; otherwise the list is
   vacuous (R2-1).
4. **(r1)**, **(r2)**, **(r3)** — three words, one theorem number, one README
   cell.
5. **(r6)** — add "up to quadrature error" to the P124.014 note.

Nothing else.  In particular: **do not reopen §4, §5, §7, the scripts, the
numerics, or the phase-124/118 notes.**  They are in the best state this
campaign is going to produce, and round 2 discharged every finding against
them.

**What must be recorded when the campaign closes.**

* **No label for row D.**  None is warranted and none is claimed; §10 is
  correct.
* **D.1 is a `RESTATEMENT`** — the paper says so, on evidence, twice.
* **D.3 is retired as a programme item**, with Theorem 5.8 kept as its result
  and Remark 5.9(1)–(3) as the reason.
* **The standing methodological rule** (Galerkin eigenvalues are variational
  upper bounds; a negative one certifies, a positive one does not; the
  interval-arithmetic `T = \log 2` certificate is carved out) is now recorded
  in phases 118 and 124 and should be carried in the corpus methodology, not
  re-derived per phase.
* **Three of the builder's own round-1 statements were refuted in round 2**,
  and with (F1) a **fourth** is refuted in round 2's own repair.  That is the
  honest count, and it is the strongest evidence the process is working: every
  one of them was found by reading, not by luck, and none of them cost a
  result.
* **The campaign should close after the erratum.**  A third full round would
  buy nothing: the remaining open items are `OPEN` in the mathematics, not in
  the writing.

**Absolute rules, final check: no sign is claimed anywhere; no label is
claimed; no statement is made about the location of the zeros outside (1.9),
Theorem 3.7 and Theorem 5.6's hypothesis — once Proposition 3.6a(iii), which
is such a statement, is withdrawn.**
