# R148.004 — Confirmation pass, phase 148

Inputs re-read in full: `R148_003_ROUND2.md` (490 lines), the **Corrections of record** block
appended to `R148_001_ROUND1.md` (lines 613–641), `README.md`. Script
`scripts/certify_mixed_support.py --fast` re-run on the patched version; output reproduced below.
Cross-checks against `04-papers/47-intersection-frame-defect/archive/main.md` (Def. 11.1/(11.1), Lemma 11.2, Lemma 19.17,
Prop. 19.18, Thm 19.23) and `03-research/phase-41-build-G2/125-construction-of-the-intersection-form.md`
(lines 106–109, 149–160 verified verbatim).*

---

## VERDICT

**ACCEPT.**

All three findings (A-1, A-2, A-3), all eight repairs (R-1 … R-8) and both downgrades are discharged.
Nothing was contested, nothing was quietly narrowed, and no repair was implemented by deleting the
statement it was supposed to fix. Two of the repairs (R-1, R-3) leave the phase with a **stronger**
result than round 1 claimed. **Three residual defects remain, all cosmetic, all one-line; none blocks
acceptance and none touches a proof** (§7).

Outcome (i) confirmed: `s^{(M)}(γ₁,π/2) = s₁ = 0.99846016271880910923…`, `d₀ = 324.9598266…`,
no FATAL flag, Paper 47 Thms 19.21–19.25 untouched, **row D: no label, no sign.**

---

## §1 — Priority item: D.56.3′ / 3″ / 3‴ / 3⁗ and D.56.4′ / 4″

Each proof checked line by line against the text, not against the summary table.

**D.56.3′.** Adopted with the content I supplied and proved correctly.
(i) is exact: a supremum of nonnegative numbers is nonnegative — **no hypothesis**, which is the whole
point of the repair. (ii) is the definitional unwinding of `sup_u p_w(u) = −ε < 0 ⟺ p_w ≤ −ε` for
*every* `u`, and `∫|p_w| ≥ ∫ε\,du = +∞` is correct. (iii) three sufficient conditions, and the `L²` route
is via Cauchy–Schwarz `‖p_w‖₁ ≤ ‖φ‖₂‖ψ‖₂` — **this is the statement round 1 wanted and did not have**,
and it is now proved rather than asserted. **CONFIRMED.** The withdrawal in §R1.1 quotes the false clause
verbatim, names my counterexample (`φ = n` on intervals of width `n⁻³`), and identifies the three
dependent sentences by location. Nothing was left standing that rested on A-1.

**D.56.3″ (the C² plug).** Correct as stated and correctly proved: `Φ ∈ D^W ⊂ C²(R)` (Def. 11.1),
so `Φ(w₀) < 0` gives an open interval `I ∋ w₀` on which `Φ < 0`, and `Φ ≥ φ⊛ψ` then forces `I ⊆ W⁻`.
The contrapositive form — a bad set with empty interior cannot enlarge the shadow — is exactly what is
needed, since open intervals have positive measure. **CONFIRMED.**

**D.56.3‴ (the open-set argument / R-1a).** Correct. The chain is `W⁻` open (3″) → `χ_{φ,ψ} ≡ −∞` on `W⁻`
(3′(ii)) → `B(k_Φ, φ⊗ψ) = ∫Φχ` not finite for every `Φ` positive on a positive-measure subset of `W⁻`
(D.55.4). The conclusion drawn — *"Theorem D.56.4's conclusion holds on the entire domain of definition
of `B`"*, with **no intermediate carrier** — is the correct conclusion and is stated at exactly its
strength, neither more nor less. **CONFIRMED. This is the repair that converts the kill from a fact about
the Hilbert–Schmidt block into a fact about the `(T)×(R)` block, i.e. about the weaker block, which is
what closes the loophole the brief raised.**

**The loophole itself is recorded honestly.** §R1.2's note concedes that with `ψ ≍ e^{|w|/2}` and `φ`
decaying faster than `e^{−|u|/2}`, `χ_{φ,ψ}(w) = O(e^{|w|/2})` is integrable against
`Φ = O(e^{−(1+ε)|w|})` by (11.1), so `(T)×(R)` is finite while `(R)×(R)` is `+∞` — *"the loophole between
the two blocks is real, and it is empty as a route"*. That is the correct disposition: the gap between
the blocks exists; it is not a route, because for nonnegative data the collapse never used either block.
**CONFIRMED.**

**D.56.2′ / D.56.3⁗ / D.56.4″ (finite rank, A-2).** The coverage gap is closed. D.56.2′ is correct —
`n` genuinely plays no role, only the order of quantifiers. D.56.3⁗ is correct and its (i) is properly
weakened: we notice, correctly and without being told, that **at finite rank the sign
hypothesis is no longer available** (a general element of `(R)` has coefficients of both signs, so
`q_w = Σφ_iψ_i(·+w)` need not be nonnegative even for nonnegative generators), and falls back to
integrability. That is the right observation and it was not in my audit. (iii)'s converse — `(⊛P)(w) < 0`
forces `q_w ∉ L¹`, hence not every generator can have a finite `χ` — is correct by linearity.
D.56.4″ then runs `⊆` through 3⁗(i) + the C² plug and `⊇` through `P = 0`, and **the note that `⊇` is
content-free because it does not use the square at all** is recorded as I asked. **CONFIRMED.**

**D.56.4′ (both signs, R-3).** Correct, and correctly reduced rather than re-proved: `k_Φ + P = k_Φ − (−P)`
with `−P ∈ (R)` (legitimate — D.55.1 defines `(R)` as a real vector space) and `χ_{−φ,ψ} = −χ_{φ,ψ}`
finite exactly where `χ_{φ,ψ}` is. The explicit rank-one computation is also given and is right:
`inf_u φ(u)ψ(u+w) > 0` means `φ(u)ψ(u+w) ≥ ε` for **every** `u`, hence `χ = +∞`; and if the infimum
is `≤ 0` the constraint reads `Φ(w) ≥ −inf ≥ 0`. **CONFIRMED.**

**O-148.3.** §R3 withdraws **both** halves — the status and the degree-normalisation excuse — quotes the
round-1 sentence in full before deleting it, and states in terms why it was dangerous. This is the single
most important repair in the file and it is done without hedging. **CONFIRMED CLOSED.**

---

## §2 — D.55.5′ versus D.55.8′: is the reconciliation real?

Yes, and it is the right one. D.55.5′ no longer claims a unification: the three blocks are *"three traces
computed by **two inequivalent prescriptions**, glued along the direct-sum decomposition"*, and item (iv)
now carries the reason — *"because the sum is direct (Thm D.55.2), **and for no other reason**"*. D.55.8′
then measures the gap between the two prescriptions. **These are consistent: a well-defined form obtained
by a legitimate choice, plus a theorem that the choice is not forced by any limiting procedure.** The
round-1 self-contradiction (assert in D.55.5, refute in D.55.8) is gone.

The **Statement of record** in §R4 is the part I want to flag as correctly done rather than merely
adequate: the blueprint's priority (1) asked whether the `(T)×(R)` block is *consistent with* the
`(T)×(T)` regularisation, with the instruction *"this is the first thing that can fail: record it"*. The
answer given — *"consistent in the only sense available (they never meet), and in no stronger sense"* —
is the honest answer and it is now on the record as an answer, not buried as an aside. **CONFIRMED.**

D.55.8′ itself is now stated at its true (trivial) strength: `B(A_Λ(P), k_Φ) = ∫Φ·Σχ_i` **for every `Λ`**,
constant, with the `2Λ` divergence acknowledged as inserted by the normalisation chosen to make the
pointwise limit land on `k_χ`. The surviving sentence is mine, adopted: *the normalisation that makes
`(R)` converge to `(T)` pointwise is not the normalisation under which `B` converges.* **DOWNGRADE 1
applied**: the Connes–Consani identification is `ANALOGY`, and the README sentence *"exhibits, in two
lines, the 'delicate principal values' that Connes–Consani themselves name"* is withdrawn — verified
absent from the current README. **CONFIRMED.**

---

## §3 — D.55.7′(i) and D.55.6′

**D.55.7′(i).** The false clause is quoted, diagnosed ("as punctuated, the clause was read — and the
auditor reads it — as *no such linear map exists*") and replaced. The corrected statement says the right
three things: neither candidate is defined and nonzero on both summands; **the blockwise map does exist
by directness**; it is not an averaging limit and not continuous along D.55.8′. Part (ii) (no degree) is
correctly declared unaffected, and its positivity step `∫χ[2cosh(w/2) − 2K(w)]dw > 0` is untouched.
**CONFIRMED.**

**D.55.6′ (R-4).** Renamed to *non-existence of a common radial representation*, with the explicit
statement that **`B` is a single well-defined bilinear form** and that the two displays of (148.1) pair
different arguments through different representations, which could conflict only if some `k` admitted
both readings — excluded by D.55.2. The proof is unchanged and still correct (Thm 11.14(i); Lemma D.55.4;
`w_{2K} = 2cosh(w/2)` from (11.16) with `Φ_{2K}(0) = Φ_{2K}(1) = 1`, `Φ_{2K}(1−ρ) = 2ξ(1−ρ) = 0`). The
added final line — a common `R` would force `w_Φ = Φ`, which fails at `Φ = 2K` — is the correct way to
state it as a non-existence theorem rather than an "anomaly". **CONFIRMED.**

---

## §4 — D.56.8′ (DOWNGRADE 2)

§R11 quotes the overclaim, concedes it is *"quietly false for any **optimised** quantity"* for the right
reason (the admissibility constraint `Ψ ≥ ⊛P` couples the sectors; nothing forbids choosing `φ,ψ` as
functions of `ξ`-data), and replaces it with D.56.8′(i): *the integrand contains no zeta data*, with
**"No claim is made about suprema of that term over any cone"** stated explicitly rather than left to
inference. (ii) — non-`𝓝_∞`-invariance, the instrument that actually disqualifies the term via
D.31.2(iii) — is correctly identified as load-bearing and stands.

The consequential check is done and is correct: **the `Ξ_a` argument does not depend on the downgraded
claim.** D.56.10/D.56.11 are about the *definitions* of the new objects (the tropical condition, D.56.3′,
D.56.4″, D.56.4′, the two new blocks), none of which names a zeta function, verified by inspection of
each definition rather than by any statement about suprema. So conclusion (i) survives the downgrade
intact. **CONFIRMED** — this was the one place where DOWNGRADE 2 could have propagated into the outcome,
and it does not.

---

## §5 — The certificate: `CERTIFIED` restricted to part (a), and the asserted window

Re-run of the patched script (`--fast`, `mp.dps = 25`) reproduces part (a) exactly:

    s_1     = 0.9984601627188091092345474
    u*      = -0.1109915633705136940835335
    1 - s_1 = 0.001539837281190890765452603
    1 - s_1^2 = 0.003077303463529236176509683      d_0 = 324.9598266311831410805725
    tail enclosure for |u| > 1.6 : 1/cosh(0.8) = 0.747699918237  <  s_1   (scan window justified)

* **The enclosure is now asserted in the code** (`TAIL = 1/cosh(mpf("0.8"))`; `assert TAIL < s1`),
  printed, and no longer depends on a quoted digit. **R-7 first half: CONFIRMED.** I also confirm the
  the correction of *my* arithmetic: `1/cosh(0.8) = 0.7476999182374196157699898`, not the
  `0.748103…` I wrote in `R148_002` §4. My value was wrong; theirs is right; the enclosure holds either
  way, and the code now computes it rather than trusting either of us. Recorded so the corpus carries
  the right constant.
* **`CERTIFIED` is now scoped to part (a) in all three places** — the script's own banner, §R8's
  "Label of record", and the README's Reproduction section. Parts (b)–(e) are relabelled
  **"CONSISTENCY PRINT (not a certificate)"** in the script output itself, with the reason stated where
  a reader will hit it: *"Parts (b)-(e) below sample only Phi >= 0, which Lemma 19.17 bounds by s_1 A
  PRIORI, so their margins cannot be negative whatever the grid does."* The README adds the sentence
  that matters most — **"The kill is Theorem D.56.4′, a two-line proof; it is not numerical."**
  **R-7 second half: CONFIRMED.** The round-1 README line *"Every margin is ≥ 0"* is gone.

---

## §6 — The doc-125 row, the withdrawal, and O-148.2 as (α)–(δ)

**The corpus row (§R9).** Rewritten as I required and better sourced than I required: it carries line
cites into doc 125, which I have now verified verbatim — `f_1 = C_p×\{v_0\}`, `f_2 = \{u_0\}×C_p`,
`Δ = \{u=v\}` at `:106–108`, and at `:109` the flow correspondences *"`Δ_μ = \{v = u + \logμ\}`, una
**traslación de la diagonal**"*, identified there as *"el **análogo de los grafos de Frobenius**"*. The
identification **`(T)` = doc 125's `Δ_μ` smeared by `Φ`** is correct and is now on the record. The three
imported obstructions are also verified at their cited lines: G-125.A at `:151–158` (integer on the thin
lattice `𝓛_Z = ⟨f_1,f_2,Δ⟩ + \{Δ_{p^k}\}`, **real** on the continuous flow, and — the decisive sentence —
*"El generador infinitesimal del flujo … **NO está en `𝓛_Z`**"*, `:156`, so the object that encodes the
zeros is exactly the one outside the integral sublattice); G-125.B and NC3 at `:26–28`. **CONFIRMED.**

**The withdrawal.** *"Any reading of this document as 'the square admits no intersection theory' is
WITHDRAWN"* appears in three places — the Corrections of record (R-8 row), §R9, and the README under a
dedicated heading **"What this phase does NOT show"**. The replacement formulation is exact: *phase 148
proved its own form, on its own domain, trivial and zero-blind, no more.* §R14 repeats it in the closing
paragraph with the clause *"and this document does not say that it has"*. **CONFIRMED** — this is the
overreach I was most concerned would survive by inertia in the README headline, and it did not.

**O-148.2 as (α)–(δ) (§R10).** Now a precise question and not a gesture: (α) `𝒦' ⊇ (T)` with
`B'|_{(T)×(T)} = I_∞` (so zero data is carried); (β) the fibre classes with `B'(f_1,f_2)` finite and
nonzero; (γ) `T_a`-invariance, so the form is a property of the square and not of a chart; (δ) an
unambiguous degree. The three-way disposition is right and, importantly, **is bounded**:

*Phase 148 answers **no for `𝒦' = (T) ⊕ (R)` only**, on (β) and (δ) — *"a statement about one `𝒦'`, and
  about no other"*;
* doc 125 answers **yes on (β),(γ) for the compact toy**, `f_1·f_2 = 1` integral and `T_a`-invariant, and
  **no on (δ) in the regime that matters**;
* **the transfer to `C_Q × C_Q` is explicitly not available and not claimed** — doc 125 works on a
  compact torus of side `\log p` where `f_1` has finite measure, and on `X = R × R` the fibre classes
  have infinite measure and doc 125's stable-intersection normalisation is undefined. *"Whether (α) can
  be added to (β)–(γ) at all … is exactly what is open."*

That last bullet is the one I would have flagged had it been missing: without it, (α)–(δ) reads as an
invitation to port doc 125 to the non-compact square, which is precisely the move that does not work.
**CONFIRMED.** The recommendation is correspondingly re-based — *"Close the square on **D.56.4′ plus doc
125's obstructions**, not on the withdrawn premise that Hilbert–Schmidt finiteness forces the collapse"* —
which is the right basis, and the same sentence now appears in §R1.4, §R10 and the README.

---

## §7 — Residual defects (three; all cosmetic; none blocking)

1. **The script's docstring still carries my erroneous constant.** Lines 36–40 of
   `scripts/certify_mixed_support.py` read *"the a-priori enclosure … `≤ 1/cosh(0.8) = 0.748103...`"* —
   my transcription slip from `R148_002`, propagated into the comment — while the code six lines later
   computes and prints the correct `0.747699918237`. The assertion makes the enclosure rigorous
   regardless, so nothing is unsound; but a docstring that disagrees with its own program's output is
   exactly the kind of thing a later reader will spend an hour on. **Fix: one line.**
2. **"the `(T)×(R)` block is finite at `w`" is used as a synonym for `q_w ∈ L¹`** in D.56.4″'s hypothesis
   and in D.56.3‴. D.56.3⁗(i) is correctly stated with `q_w ∈ L¹` and its parenthetical correctly says
   *"if `φ_i(·)ψ_i(·+w) ∈ L¹` for each `i`"*; but a finite `χ_{φ,ψ}(w)` in the sense of a conditionally
   convergent integral would not license 3⁗(i). Within the phase this is harmless — Lemma D.55.4
   establishes the `(T)×(R)` block by Fubini under the **absolute** bound
   `‖Φ‖_∞‖φ‖_1‖ψ‖_1`, so absolute convergence is what "the block is defined" means throughout — but the
   two theorems should say *absolutely convergent* rather than *finite*. **Fix: two words, twice.**
3. **D.56.3⁗(iii)'s conclusion** — *"at least one generator has `χ_{φ_i,ψ_i}(w) = ±∞`"* — is slightly
   stronger than what the proof gives, which is that the generators cannot **all** have absolutely
   convergent `χ` at `w`. Same content for the use made of it; the wording should match the proof.

None of these three touches D.56.3′, D.56.3″, D.56.3‴, D.56.4″, D.56.4′, D.56.6, or any label. They are
recorded for that round, not as conditions on acceptance.

**Also confirmed clean:** no covert positivity assertion anywhere (W-a holds — I re-checked D.55.5′(iv),
D.56.4′ and §R10, the three places a repair could have introduced one); the `Ξ_a` epistemology is stated
correctly in both directions (blindness condemns a positive, is neutral for a negative, and here is the
proof that no A3 step was smuggled in); every withdrawal in §R0–§R12 quotes the withdrawn text verbatim
before deleting it, so the corpus keeps a record of what was wrong and not merely of what replaced it;
and the Corrections of record block in `R148_001` is dated, points forward to `R148_003`, and does **not**
rewrite round 1 — the document of record stays intact, which is the correct discipline.

---

## §8 — What phase 148 established

Phase 148 asked whether enlarging row D's carrier from the radial line to the square `C_Q × C_Q`, with an
effective cone generated by mixed classes `k_Φ − φ⊗ψ ≥ 0`, produces any constraint on `Φ_Φ(ρ)` that the
radial sector does not already give — concretely, whether the support function of that cone at the lowest
zero exceeds Paper 47's `s₁ = 0.99846016…`, which is what the frame defect theorem lives on. The answer,
after repair, is a clean and now correctly-proved **no**, and the proof is two lines with no numerics in
it: the effectivity condition on the square is the **tropical** inequality `Φ ≥ φ ⊛ ψ` with
`(φ⊛ψ)(w) = sup_u φ(u)ψ(u+w)` — genuinely the first appearance of the `(max,+)` structure of
Connes–Consani's arithmetic site inside row D, and genuinely new as a condition on a kernel — but it is a
**lower** bound by a function that cannot be negative. For nonnegative factors that is unconditional, a
supremum of nonnegative numbers, immune to every growth, decay or integrability hypothesis; for signed
factors, and for the `+` quadrant round 1 wrongly left open, a negative tropical bound on a set with
nonempty interior forces the product to be bounded away from zero on all of `R` and so sends the
**`(T)×(R)`** block — the weaker of the two blocks, the one that can survive when Hilbert–Schmidt fails —
to `∓∞` there. So the translation shadow of the mixed cone is exactly the frame's own effective cone `𝓔`,
on the entire domain where the form is defined, at every finite rank, for both signs: `s^{(M)} = s`,
`(b′)⁺_X ⟺ (b′)⁺`, outcome (i), no FATAL flag. **What the phase establishes positively is therefore a
negative of a rather sharp kind — the max-plus structure of the arithmetic site, reached through the
effective cone, cannot see the zeros of `ζ`, and the reason is that tropical effectivity is a
strengthening of ordinary effectivity and never a relaxation of it — together with two structural facts
about the square as a carrier: it has no degree and no radial projection, and any form on it must glue a
regularised trace to an honest one by fiat.** What the phase does **not** establish, and now says so in
four places, is that the square admits no intersection theory: it proved one form on one domain trivial
and zero-blind, and phase-41 doc 125 shows from the other side that the classes carrying the Hodge
signature — the fibre classes `f₁, f₂` with `f₁·f₂ = 1` — are precisely the ones this form cannot pair.
That residue is O-148.2, stated as (α)–(δ), and it is bounded independently by doc 125's own three
obstructions (intersection numbers generically real rather than integer on the continuous flow, with the
flow's infinitesimal generator — the object that encodes the zeros — outside the integral sublattice;
Babaee–Huh non-persistence of the signature at infinite rank; NC3 circularity), none of which phase 148
repairs and none of which it worsens. Closing the square is therefore the right recommendation, and it now
rests on `D.56.4′` plus those obstructions rather than on the withdrawn premise about Hilbert–Schmidt
finiteness — which is exactly the difference between a negative that will hold and a negative that would
have been reopened.
