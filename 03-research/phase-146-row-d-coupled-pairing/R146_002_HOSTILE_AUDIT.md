# R146.002 — Hostile audit, phase 146 round 1

*Auditor: Claude Opus 5. Date 2026-09-14. Target: `R146_001_BUILDER_ROUND1.md` (+ `README.md`,
`scripts/cosh_test_cmn.py`), against `R146_000_LEAD_BLUEPRINT.md`, `CORPUS_CHECK_R146.md`,
`CORPUS_CHECK_R146b.md`, `R145_001` §§D.41–D.42, `R145_005`, `R140_001` §§D.23.1/D.23.3bis,
`R142_001` §D.31, Paper 44 §§3ter, 5, 6bis, 8bis, §12 (K1), Paper 46 §§11, 14.
Method: every claim assumed false; every number recomputed; every dictionary re-derived from its source.*

**FATAL screen: PASSES.** No statement anywhere in round 1 proves, conjectures, or smuggles positivity of
any degree form. Both quantitative outputs are *failures* of positivity. W-a is honoured in substance.
**Script: no bugs found**; every printed number reproduces exactly (`--fast`), including
`margin(1,1) = −0.499829`, `Q(5·Frob_6−4·Frob_10) = −10`, `min Q = −2088` at `(1,60,−12,6)`, and the
Hasse column (`PASS` only at `ℓ = 2,3,5`; `ℓ=4` fails at `18.549 > 16`). The model side was re-derived
independently and is **correct**: `E/F_2 : y²+xy = x³+1` has `N_1 = 4`, `Δ ≠ 0`, `a = −1`; (146.10) checks
against `F_1,F_2,Γ_χ`; `[Γ_{1+π}]² = 0`; and `Γ_φ² = deg(φ)(2−2g)` follows from adjunction on `C×C`
(`Γ² = 2g−2 − (1+d)(2g−2)`), so (146.6) **is** true in the model.

Everything that fails, fails on the **arithmetic** side, in the transport, or in the labels.

---

## MAJOR findings

**M1 (the worst one). (146.6) / D.45.3(3) — "adjunction forces `δ_n = n(2−2g) = −∞`" — is contradicted by
the round's own cited source.** Paper 44 **Theorem 8bis.1b** (`44/main.md:3416ff.`) *computes* the
Frobenius diagonal. Its value is
`Σ_q W_q(Δ^{(n),[φ_ε,N]}) = −Σ_{r∈S_f∖P(n)}(\log r)[(r−2)/(r−1)+(N−1)]` (finite places, exact, linear in
`N`) plus `W_∞ = −\log(1/ε)+O(1)` (archimedean, **independent of `n`**). The `n`-dependence is **through
`P(n)` only** — not through `n`, and not proportional to anything. So `δ_n = n(2−2g)` is a model formula
transported by assertion; it is not adjunction on `Spec Z`, adjunction is not available there, and the
label `RESTATEMENT` on D.44.7 is wrong for (146.6)'s arithmetic half. *Answer to audit item 2(c): the
model's formula, transported, and contradicted by Paper 44.*

**M2. O-46.3 is mis-posed twice, and the phase-147 recommendation rests on it.**
(a) *Internal:* under the round's own (146.6), `δ_m − δ_n = (m−n)(2−2g) = ±∞` — trivially closed. The
round proposes as its one open door a question its own §D.45.3 answers.
(b) *Substantive, and worse:* **the difference-only form does not depend on `δ_m − δ_n`.** From (146.8),
`B_δ(e_m − e_n, e_m − e_n) = L(m,n) − (δ_m + δ_n)/2` — a **sum** of diagonals, not a difference. The
sentence "the difference-only form of Theorem D.45.1 needs nothing else" is false by the round's own
formula, and with it the premise of the phase-147 recommendation.
(c) *Constructive repair, available from the cited source and not used:* by M1's displays the **archimedean
divergence cancels identically in `δ_m − δ_n`** (it is `n`-independent), leaving
`δ_m − δ_n = Σ_{r∈P(m)∖P(n)}(\log r)[(r−2)/(r−1)+N−1] − Σ_{r∈P(n)∖P(m)}(\ldots)`, which is **exactly `0`
when `P(m) = P(n)`** — in particular on every single-prime tower `m,n ∈ {ℓ^a}`, which is the *only* regime
the model dictionary covers — and otherwise diverges linearly in `N` at the chart. So O-46.3 is a genuine
question with a partly computable answer, but it is not the question the round asked and not the parameter
the difference form uses.

**M3. D.44.6(ii) ("rigidity") is not proved; its stated proof is false.** "`L_S` is a rank-1 `Z`-module
inside `X_S`, so `End_Z(L_S) = Z`". Paper 44 defines `L_S = ∏_{p∈S_f} Z_p` (`44/main.md:405`). That is not
a rank-1 `Z`-module and its endomorphism ring is enormous — it contains `∏_p Z_p` acting by multiplication,
and therefore **does contain rank-2 orders** (any `Z[π]`, `π²−aπ+ℓ=0`, whose discriminant is a square in
each `Z_p`, `p∈S_f`). The only true content of (ii) is the tautology that `Sh_Z`, *as defined*, sends
`Frob_n ↦ n ∈ Z`, so its image is `Z`. "Rigidity" is a naming of a definition. Label `PROVED`: **withdraw**.

**M4. D.44.6(i) is false at a finite chart.** `deg_det Sh_Z(m+n·Frob_ℓ) = \log\#(L_S/(m+nℓ)L_S)` equals
`\log|m+nℓ|` only when every prime factor of `m+nℓ` lies in `S_f`; in general
`[L_S:kL_S] = ∏_{p∈S_f}|k|_p^{−1}`, i.e. the **`S`-part** of `|k|`. Since `S_f` is finite and `m+nℓ` ranges
over all integers, no chart makes the stated identity true. (This is a real obstruction the round missed,
and it is a better one than M5: the shadow's count is only a partial count.)

**M5. D.44.6(iii) is a non-sequitur, and contradicts D.44.3.** The obstruction to a rank-2 order is stated
as: "the only candidate trace is `Σ_p Λ(p)p^{−1/2}`, which diverges". The model's trace is the trace of a
**single** Frobenius (`a = q+1−N_1`), not a sum over all primes; and the round's own Theorem D.44.3
constructs a perfectly **finite** per-prime candidate `a_ℓ = ℓ+1−Λ(ℓ)`. Divergence of the total contact is
the divergence of a *different* quantity and proves nothing about the existence of `Z[π_ℓ]`. *Answer to
audit item 6: non-sequitur.*

**M6. D.44.3 is a definition on a rank-2 truncation, not a determination — and the full dictionary is
inconsistent.** Matching `q^{−|a−b|/2}N_{|a−b|}` (`R145_001` D.41.6) against
`Λ(\max/\min)(\min/\max)^{1/2}` forces **`N_k ↔ Λ(ℓ^k) = \log p` for every `k ≥ 1`**, not only `k = 1`.
But any genuine rank-2 order requires `N_k = ℓ^k+1−(α^k+β^k)` **determined by `a_ℓ`**. At `ℓ = 2`:
the order predicts `N_2 = 5 − (a_2²−4) = 3.678…`, the dictionary supplies `N_2 = \log 2 = 0.693`. The
system is **over-determined and has no solution at a single prime**, before any Hasse test is run.
D.44.3's "unique symmetric form on a rank-2 module" is the trivial observation that three numbers determine
a symmetric 2×2 form. `PROVED` → **`DEFINITION`/`RESTATEMENT`**.

**M7. D.44.4's quantitative content is an artifact of the chosen degree normalization.** The result depends
entirely on `d_n := n`. The round *itself* records a second, equally arithmetic degree (D.44.7:
`deg_det Sh_Z(Frob_n) = \log n`) and does not argue for the choice. With `d_n = \log n` one gets
`a_ℓ = 1+\log ℓ−Λ(ℓ) = 1` for every prime `ℓ`, and `a_ℓ² ≤ 4ℓ` holds for **every** prime. (The
un-normalization of the *`L`-block* is signature-neutral — it is conjugation by `diag(n^{1/2})` — so that
part of the transport is clean; it is the `d_n` term that carries the whole result.) Further:
`g_ℓ := a_ℓ/(2\sqrt ℓ)` is not a genus (a genus is an integer; `g_2 = 0.816` bounds nothing), it is a number
produced by forcing `|a| ≤ 2g\sqrt q` backwards on data that does not come from a curve (M6). And "the
**first finite, prime-by-prime form** of `Δ·Δ = −∞`" is an **overclaim**: nothing here is derived from
Theorem 8bis.2, nothing implies it, and the content of (146.5) is the elementary fact `\log p ≪ ℓ`.
*Answer to audit item 3:* **D.44.4 is a heuristic** — a dimensional-consistency observation, correctly
computed, correctly signed, with the interpretation over-sold in the box, in `P46-40` and in the README.

**M8. "`c_N(m,n) → 1` as `N → ∞` … it does not affect a single sign below" (D.44.0) is false.** By (8bis.0)
and the §12 correction K1, `c_N(m,n) = ∏_{s∈S_f∖(P(m)∩P(n))} vol(1+s^NZ_s) = ∏((s−1)s^{N−1})^{−1}`, which
**decays geometrically to `0`**; in the `♭` convention the factor is `∏_{s∉F}vol(\cdot)^{−1} → ∞`. Paper 44
§8bis.0 headlines **no rate** precisely because of this. The factor is `(m,n)`-dependent (through
`P(m)∩P(n)`), so it does not cancel out of the form. What survives untouched is the **vanishing** of the
entries (8bis.2 is `0` off prime-power ratios, convention-free), hence the `−10` witness survives; what does
**not** survive is any numerical statement about a nonzero `L(m,n)`, `G(m,n)`, `\deg c_{m,n}`, or the
`ℓ ≥ 7` threshold. O-46.2 ("a volume `≤ 1`") contradicts the main text ("`→ 1`") — the round disagrees with
itself about its own constant. **O-46.2 should be promoted from "presentational" to MAJOR.**

**M9. D.45.1's clause (i) — "agrees with `I_∞` on differences" — is not established.** By Paper 46 (11.6),
`I_∞(E,E) = 2ab − W(E)`. For `x = E_m − E_n` one has `a = Φ_x(1) = m−n`, `b = Φ_x(0) = 0`, so
`I_∞(x,x) = −W(x) ≤ 0` for real classes, whereas `B_0(x,x) = L(m,n) ≥ 0`. **Opposite sign.** What agrees
with Gram (A) is the *off-diagonal entry*, which is a different statement from the blueprint's (i). The
blueprint item is not discharged; the hedge "in the only sense available" concedes as much and should say so.

**M10. "Extends the `Λ(n)n^{−1/2}` weights exactly" is misleading, and the form carries no zero data at
all.** The entries of `B_δ` are `G(m,n) = ½(m+n−L(m,n))`, dominated by the degree term; `Λ` enters as an
`O(\log)` correction to an `O(m+n)` entry. Structurally,
`Q_0(x) = Φ_x(0)·Φ_x(1) − ½\,x^{\mathsf T}Lx` — i.e. **Paper 46's comparison identity `2ab − W` with the
zero sum `W` replaced by the finite Gram**. *Answer to audit item 1: the first term is the product of the
two bidegree/ruling pairings `Φ(0)Φ(1)`, and `δ` is the diagonal `L(n,n)` set to `0` by the `g=1` model
convention.* Three consequences the round should state and does not: (a) the form is **by construction**
free of zero data, which is a stronger and cleaner reason for D.45.7's non-detection than "the correction is
ruling-plane"; (b) **every statement in §§D.44–D.45 is therefore `Ξ_a`-uniform**, not only D.45.8 — Paper 46
`main.md:2274` says §11 (11.8 included) "carries no sign whatever" and holds verbatim for `Ξ_a`; (c) the
indefiniteness is immediate (M13).

**M11. Theorem D.45.8 is labelled `PROVED` and is asserted.** (i) "the classification of continuous
endomorphisms of the idele class group … the affine maps `x ↦ ℓx^k`" is stated as if it were a citation;
it is neither proved nor true as literally written (`C_Q ≅ R_{>0}×\hat Z^×` has a large continuous
endomorphism monoid, and even on the modulus line the continuous endomorphisms are `x ↦ λx`, `λ ∈ R`).
(iii) "a sum of translations is not a translation" is a tautology and does **not** establish the stated
conclusion, "there is no sum of correspondences realized as a single correspondence on `C_S`" — it excludes
only realizations *inside the translation family*. (ii) (Riemann–von Mangoldt density under `s ↦ ks`) is
correct and cheap. *Answer to audit item 5: the headline is **asserted**, not proved; what is proved is
(ii) plus a tautology.* The `Ξ_a`-verbatim check is right and is itself trivial once the proof is seen to
use only the group law of `R` — recording it as a *negative* separation result is the correct discipline.

**M12. `O-46.1`'s `EQUIVALENT-TO-RH` label is a mis-citation.** Proposition D.42.5 (`R145_001:823`) is the
statement that, for a **closed, `𝓝_∞`-saturated cone `𝔈 ⊇ 𝓔` with the degree gate (4b)**, clause (4) is
equivalent to RH. It does **not** say that `Q_δ ⪰ 0` on `Z⟨Frob_n⟩` is RH, and no such reduction is given
anywhere in the round. The prudential verdict (do not attempt) is right and the direction of error is safe —
this is why it is not FATAL — but the round closes its **only free parameter** on a citation that does not
cover it, and `P46-41`'s "fixing it positively is RH" must not go to a paper in that form.

**M13. D.45.2(ii)'s "explicit integral witness" is one line, and it is the same computation as D.44.4.**
`Q_0(x) = Φ_x(0)Φ_x(1)` before `L` enters — a **product of two independent linear functionals**, hence
signature `(1,1)` on any span where they are independent. Indefiniteness needs no witness, no scan, and no
`6/10` degeneracy. On a pair `{m,n}` the determinant is `mn − (m+n−L)²/4`, i.e. **exactly** D.44.4's Hasse
discriminant; the two results are not independent. Additionally, `(6,10)`, `(15,22)`, `(1,60)` all live in
the multi-prime region, where the model (a single `π`) supplies **no counterpart at all** — the witness is
drawn from the part of the lattice the dictionary never covered. *Answer to audit item 2(a): the count axiom
as stated (`deg(α−β)=0 ⟺ α=β`) is correct in the model, and the degeneracy is real, but it is a property of
`L`-extended-by-zero, i.e. of the round's own definition, not a discovered arithmetic fact.*

**M14. The one entry that does the work, `⟨Frob_ℓ, Δ⟩`, is a choice between two Paper-44 objects — and the
choice discards the archimedean block the round then declares missing.** Theorem 8bis.1 is stated for
`m,n ≥ 2`, `m ≠ n`; the entry `L(1,ℓ)` comes from Theorem 3ter.10, which computes the **trace** of
`Frob_ℓ` (`Λ(ℓ)ℓ^{−1/2}`, exact, convention-free — that much is sound). But the pairing against the
*diagonal* in the frame is `I_A(Frob_ℓ, Δ^{rad})`, and by Theorem 8bis.1e / `R140_001` D.23.12(B) the
unit-averaged family `Frob ⋆ Δ^{rad}` carries the **full** Weil kernel `W_{fin}+ω_∞`. So `a_ℓ`'s defining
entry differs between object (A) and object (B) by exactly an archimedean block — and object (B) is the one
the round's phase-147 recommendation goes looking for elsewhere.

---

## MINOR findings

* **m1.** "`deg`" carries three incompatible meanings within four pages: `\deg Γ_n^{un} = n+1` (146.1),
  `d_n := n` called "`\deg Frob_n`" (146.2), `\deg_{det} = \log n` (D.44.7). The object `d_n = Φ(1) = Γ·F_2`
  is the right one for the model relation, but it is not a degree.
* **m2.** P122.028 is a no-go on *citing a magnitude-only relation as the independent input*. The round
  escalates it to "the correction term is **incapable of carrying the sign**" and "**refutes**". Direction
  is standard corpus practice; the verb is too strong. Keep as a gate, not a refutation.
* **m3.** Theorem 11.8(i) is cited for "the rulings have `Φ ≡ 0` at the zeros". Verified: `Φ_K = ξ` and
  `Φ_{K_{odd}}(s) = \frac{\sinh((s−½)a_0)}{\sinh(a_0/2)}ξ(s)` (`R140_001` D.23.7, `R138_001` D.15.1b) both
  vanish at every zero, and `F_1 = K+K_{odd}`, `F_2 = K−K_{odd}`. *The citation is correct.* It should carry
  Paper 46 `main.md:2274` alongside it: §11 holds verbatim for `Ξ_a`.
* **m4.** Script: `s_of_theta` approximates a supremum on a grid, so it **under**-estimates `s`, which
  **enlarges** the printed margin — conservative in the detecting direction, therefore harmless. The
  diagonal convention `L(n,n)=0` is documented in the code. No other issues.
* **m5.** D.45.7(ii)'s hand proof contains a visible false start ("at `m=n=1`: `1.4976 > 2`? no —") left in
  the text. It is repaired two clauses later, but it should not ship.
* **m6.** `Γ_{1+π} ∉ 𝓔_C` is asserted from "two negative coefficients"; negativity of coordinates in a
  spanning set is not by itself exclusion from a cone. True here (`[X]` of `R145_001` D.42.1 is cited), but
  the one-line argument given does not establish it.

---

## Per-item verdicts

| item | builder's label | audit verdict |
|---|---|---|
| **D.44.0–D.44.2** (normalization; off-diagonals as counts) | `PROVED-IN-REPOSITORY` | **SUSTAINED as citation** (3ter.10 is exact and convention-free; 8bis.2's vanishing criterion is convention-free), **less M8** (the `c_N` claim is false and O-46.2 must be promoted) and **less M14** (which object is `Δ`). |
| **D.44.2a, D.44.7** (the diagonal is not a count; two degrees) | `RESTATEMENT` | **SUSTAINED** for the table and for `Δ·Δ = −∞`; **WITHDRAWN** for (146.6)'s arithmetic transport (**M1**). |
| **D.44.3** (the would-be norm form) | `PROVED` | **DOWNGRADE → `DEFINITION`/`RESTATEMENT`** (M6): three numbers determine a 2×2 form; the full dictionary they come from is over-determined and inconsistent at every single prime. |
| **D.44.4** (Hasse failure; `g_ℓ → ∞`) | `PROVED`, `CERTIFIED` | **Numbers CERTIFIED-CORRECT; status → `HEURISTIC`** (M6, M7, M8). Not a theorem, and *not* a restatement of `Δ·Δ=−∞` either — an independent dimensional observation (`\log p ≪ ℓ`) whose sign is normalization-dependent. **Overclaim in the box, in `P46-40` and in the README.** |
| **D.44.6 = D.44.2 rigidity** | `PROVED` | **NOT PROVED.** (i) false at a finite chart (M4); (ii) false proof, tautological content (M3); (iii) non-sequitur (M5). |
| **D.45.1** (existence of `B_δ`) | `PROVED` | **SUSTAINED but content-free** (a symmetric form is its Gram); clause (i) **not discharged** (M9); "extends the `Λ(n)n^{−1/2}` weights exactly" **misleading** (M10). |
| **D.45.2** (not a count: degeneracy + indefiniteness) | `PROVED` | **SUSTAINED** (all three numerics reproduce). **Content lower than advertised**: indefiniteness is one line (M13), is the same computation as D.44.4, and the witnesses live outside the dictionary's domain. |
| **D.45.3** (the sign is the counterterm; STOP) | `PROVED` (equivalence of problems) | **PARTIALLY WITHDRAWN.** Item 1 is fine. Item 2's equivalence is **not established** (M12). Item 3 rests on **M1** and falls with it. Item 4 (`g=1` hides it) is correct and is the round's best observation. |
| **D.45.4, D.45.5** (model: additive class map, `Γ_{1+π}`) | `PROVED` | **SUSTAINED** — re-derived independently, including `[Γ_{1+π}]² = 0` and `\deg(1+π)=2`. Best-verified section in the round. |
| **D.45.7** (cosh test passes; non-detecting) | `PROVED`/`NEW` | **SUSTAINED, and the reason should be strengthened** (M10): the class is `Φ`-identical to the effective `E_m+E_n` while carrying strictly more degree, so Lemma D.31.4 is a **tautology** on this family; and the form itself contains no zero data by construction. Non-detection is right; it is also `Ξ_a`-uniform, which the section does not say. |
| **D.45.8** (only the formal additive structure) | `PROVED` | **DOWNGRADE → `ASSERTED` / partially proved** (M11). The `Ξ_a`-verbatim check and its "A3 does not enter here" conclusion are **SUSTAINED**. |
| **D.45.9** (count on monomials and differences, never on sums) | `PROVED` | (i)–(ii) **SUSTAINED**; (iii) **conditional on D.45.8** (M11) and on the chosen `δ`; (iv) rhetorical. |
| **O-46.1** | `EQUIVALENT-TO-RH`, DO-NOT-ATTEMPT | **DO-NOT-ATTEMPT: correct and endorsed.** The *label* is unsupported (M12): re-label `OPEN, suspected RH-equivalent, not proved so`. |
| **O-46.2** | `OPEN` (presentational) | **PROMOTE to MAJOR** (M8). |
| **O-46.3** | `OPEN`, recommended for 147 | **RE-POSE** (M2): trivially closed by the round's own (146.6); not the parameter the difference form uses; genuinely open in the corrected form, with the archimedean cancellation and the `P(m)=P(n)` case already computable from Thm 8bis.1b. |
| **O-46.4, O-46.5** | `OPEN` | **SUSTAINED.** |
| **Labels / §Label** | no label proposed | **CORRECT** — and the discipline of proposing none is right. Six of the round's `PROVED`s require downgrade (D.44.3, D.44.4, D.44.6, D.45.8, and clauses of D.45.1 and D.45.3). |
| **Corpus check** | per-idea table | **SUSTAINED in placement**, with one correction: D.23.12(A) already records the pure Frobenius Gram as **proved unsigned at every finite chart** (Paper 44 Thm 8bis.4a), so D.45.2's indefiniteness is *less* new than the table implies. |
| **FATAL screen** | none raised | **CONFIRMED: none.** |
| **README** | — | Headline repeats D.44.4 without its normalization- and convention-dependence (M7, M8). Must be qualified. |
| **Script** | — | **CLEAN.** Reproduces every printed value; conservative where approximate. |

---

## Overall

Round 1 is **honest, well-disciplined, and substantially over-labelled**. It obeys W-a scrupulously and its
model-side work (D.45.4–D.45.5) is the most solid thing in phases 145–146. But the arithmetic side rests on
two choices the round makes and does not defend — the degree normalization `d_n = n` and the diagonal
convention `δ ≡ 0` — and **every negative headline is an artifact of one of them**: with `d_n = \log n` the
Hasse test passes at every prime; with the arithmetic diagonal the form does not exist; with the chart
constant restored the `ℓ ≥ 7` threshold moves. What remains after the artifacts are removed is small and
real: (a) the off-diagonal entries are counts and the diagonal is not (already Rem 8bis.1c); (b) `L`
extended by zero cannot be a difference-degree (definitional, but worth recording); (c) `g = 1` hides the
counterterm (the round's best new observation); (d) D.45.7's non-detection, which is stronger than stated.

The single most damaging finding is **M1+M2**: the round's terminal claim about *where the sign lives*, and
its phase-147 recommendation, both rest on `δ_n = n(2−2g)`, a model formula that Paper 44's own computation
of the Frobenius diagonal contradicts, together with a false statement about which parameter the
difference-only form consumes.

---

## Programme level: is the diagnosis right, and what is a defensible phase 147?

**"The sign lives in the diagonal counterterm of the additive structure that `Spec Z` lacks" is not yet a
defensible final diagnosis — it is half a location and half an artifact.** Three reasons. First, the
additive structure whose counterterm is being blamed was *imposed*, with two free normalizations, and the
round's evidence for the blame is exactly the negativity that those normalizations produce (M7, M13);
change either and the evidence changes sign. Second, and decisively, the form the round built is
`Q_0(x) = Φ_x(0)Φ_x(1) − ½x^{\mathsf T}Lx` — Paper 46's own `2ab − W` with the **zero sum deleted**. An
object with no zero data cannot have localized anything about `ξ`, and consistently with this **every
theorem of §§D.44–D.45 is `Ξ_a`-uniform**, which the round records for D.45.8 and should have recorded for
all of them. Third, the "additive vs multiplicative" framing is not what the computation shows; what it
shows is the older and narrower fact that the **diagonal** is the only non-count entry, which the corpus has
held since Rem 8bis.1c. Phase 145 named the missing ingredient (effective classes = graphs of sums);
phase 146 has shown that naming them formally buys nothing, and *that* is the honest deliverable: **a
negative, and one that does not separate `ξ` from the falsifier.**

The round's own phase-147 recommendation — an archimedean-bearing model, on the identification "`δ_n` and
Paper 46 item (21) are the same slot" — is **half right and should not be taken as offered**. Right,
because Theorem 8bis.2's divergence is explicitly archimedean in origin (`44/main.md:3782`: "the divergence
coming entirely from the archimedean symbol, the finite-place symbol being bounded at the fixed chart").
Wrong, because the *Frobenius* diagonal `δ_n` (Thm 8bis.1b) has, in addition, a **finite-place divergence
linear in the chart parameter `N`**, depending on `n` only through `P(n)` — so `δ_n` and item (21) are not
one slot, they are two, and the round conflated them. And wrong again because the object that actually
carries the archimedean block already exists in the corpus and was not used: the unit-averaged family
`Frob ⋆ Δ^{rad}` (Thm 8bis.1e, `R140_001` D.23.12(B)), whose Gram is the **full** Weil kernel `W_{fin}+ω_∞`.

**A defensible phase 147, in order of defensibility.**
1. *Compute, do not model.* Evaluate `δ_m − δ_n` exactly from Paper 44 Thm 8bis.1b in **both** conventions:
   establish (i) the archimedean cancellation, (ii) `δ_m − δ_n = 0` whenever `P(m) = P(n)` — in particular
   on every single-prime tower `{ℓ^a}`, the **only** regime the model dictionary covers — and (iii) the
   `(N−1)\log r` chart term off that regime. This is a finite, checkable computation inside a cited theorem,
   it replaces the transported adjunction formula that M1 refutes, and it is the one place phase 146 touched
   where the corpus's `−∞` verdict genuinely is not dispositive.
2. *Then, and only then*, ask what the single-prime-tower form (`m,n ∈ \{ℓ^a\}`, diagonal now finite and
   convention-free) contains — this is the exact analogue of the model's `\{π^a\}`, and it is the first
   arithmetic object in this line whose diagonal is not an assumption. Note in advance that M6 predicts it
   will fail to be an order, and that failure, stated as a theorem about the `ℓ`-tower Gram, would be a
   better `P46-40` than the present one.
3. *Use object (B), not a new model.* Any archimedean content the phase needs is in `Frob ⋆ Δ^{rad}`
   (Thm 8bis.1e), not in an imported archimedean-bearing model; importing one re-opens the `Ξ_a` problem
   from scratch, since everything built in phase 146 is `Ξ_a`-uniform.
4. **Do not** pursue a two-variable square on `C_S × C_S` (the round's own corollary and P122.028 leave it
   with no source of zero data), **do not** pursue `δ_m − δ_n` as the difference form's parameter (M2b, it
   is `δ_m + δ_n`), and **do not** attempt O-46.1 — while noting that its `EQUIVALENT-TO-RH` label is not
   currently supported by Prop. D.42.5 and should be re-labelled rather than relied on.

*Required repairs before round 2 closes: M1, M2, M3, M4, M5 (statement withdrawals); M6, M7, M8 (label
downgrades and the `c_N` correction, with README and `P46-40` re-worded); M9, M10, M11, M12 (claim
weakening and re-labelling); M13, M14 (framing). Nothing in the round needs to be deleted; the
`PROVED` stamps do.*
