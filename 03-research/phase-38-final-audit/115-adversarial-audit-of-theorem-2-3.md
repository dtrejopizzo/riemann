# Doc 115 — Adversarial audit of Theorem 2.3 of Doc 112 (the conditional dichotomy)

**Program:** Riemann Hypothesis — Phase 38, final audit
**Object:** Doc 112, Theorem 2.3 (LP-112 ⟹ m∈{0,∞}) and Proposition 2.6 (zero density of witnesses);
Doc 113 (non-precedence); P44 (`06-papers/P44-two-lemma-architecture/main.tex`), which rests its
entire architecture on these two statements.
**Rule:** no numerics; absolute frankness; every claim about the literature is checkable
(Bagchi 1987, Laurinčikas 1996, Titchmarsh 1986 — the same sources Doc 112 cites).

---

## 0. One-line audit result

**Theorem 2.3 SURVIVES WITH CORRECTIONS.** The proof of the conditional is essentially
correct (Rouché, choice of constants, novelty of the replica, iteration: verified);
there is ONE real statement mismatch in the weak version LP-112⁻ (insufficient height
threshold, repairable in one line), a repeated conceptual imprecision about "unknown
emptiness" (under H(m) the emptiness of the witness set above the threshold is a THEOREM —
a corollary of Thm. 2.3 itself by contraposition — and that does NOT make the theorem
vacuous, but the language of D112/D113/P44 must be corrected), a quantifier mismatch
between Doc 112 (weak form ∀D∃sequence) and P44/D113-§0 (strong form ∃sequence∀D, not
trivially equivalent), and a systematic overclaim in the headline statements about
non-equivalence with RH (which is UNREFUTED, not PROVED — and in fact cannot be proved
in the material sense). None of these defects brings down P44's architecture;
all require text corrections.

---

## 1. Line 1 — The margin η and the order of the choices: VERIFIED

The proof (D112, §2.2) chooses, under H(m) and with ρ₀ = β+iγ₀ = ½+δ+iγ₀ a fixed
off-critical zero:

r := ½·min( δ, 1−β, dist(ρ₀, Z(ζ)∖{ρ₀}) ) > 0.

Audit of each piece:

1. **dist(ρ₀, Z(ζ)∖{ρ₀}) > 0.** The zeros of ζ form a discrete set with no
   accumulation points in ℂ (ζ ≢ 0, holomorphic except for the pole); the set is infinite but
   its elements escape to infinity in height, so the distance from ρ₀ to the rest is
   attained and positive. ✓. (Multiplicity: if ρ₀ is multiple, Rouché counts with
   multiplicity and yields ≥ 1 zero — no problem.)
2. **D = D̄(ρ₀,r) inside the open strip and away from the line.** Re s ∈ (β−r, β+r);
   r ≤ δ/2 gives Re s > ½+δ/2 > ½ (the disk does not touch Re = ½, where the on-line
   zeros live), and r ≤ (1−β)/2 gives Re s < (1+β)/2 < 1. ✓.
3. **No other zeros in D.** r is strictly smaller than the distance to the nearest
   zero other than ρ₀ (factor ½): D̄∖{ρ₀} contains no zeros, neither on-line (excluded by 2)
   nor off (excluded by distance). If two quadruples were very close together, the distance
   records it and r shrinks — finitely many, no degeneration. ✓.
4. **η = min_{∂D}|ζ| > 0.** ∂D is compact and zero-free by 3. ✓.
5. **Order of the choices, no circularity.** Under H(m) the configuration
   {(δ_j,γ_j)}_{j≤m} is a fixed datum of the hypothetical world; ρ₀, r, η are functions of
   that datum, chosen BEFORE invoking LP-112; LP-112 is universally quantified over
   disks, so applying it to the D depending on the configuration is legitimate. The point
   D112 underlines ("F1: frozen constants") is exactly right: finiteness turns
   δ_min, γ_max, r, η into numbers, not into parameters requiring uniformity. ✓.

**Verdict for line 1: no crack.** The arithmetic |Re s − ½| ≥ δ − r ≥ δ/2 > 0 is correct as
written.

## 2. Line 2 — Rouché and the off-critical replica: VERIFIED, with ONE statement flaw in LP-112⁻

**Rouché.** On ∂D: |ζ(s+iτ) − ζ(s)| < η/2 < η ≤ |ζ(s)| — a STRICT inequality on the
whole contour, as Rouché requires. Conclusion: ζ(·+iτ) and ζ have the same number of
zeros (with multiplicity) inside D; ζ has ≥ 1 (ρ₀); hence there exists an interior z*
with ζ(z*+iτ) = 0. ✓.

**Off-criticality.** Re(z*+iτ) = Re z* ∈ (β−r, β+r) ⊂ (½+δ/2, 1). ✓.

**Novelty.** Im(z*+iτ) > γ₀ + τ − r; with τ > γ_max + γ₀ + r + 1 this exceeds γ_max, so
the zero does not belong to the list of 4m and its quadruple is the (m+1)-th (a quadruple has
exactly ONE member with Re > ½ and Im > 0, so two distinct zeros of that type
generate distinct quadruples). ✓ — contradiction with "exactly m". ✓.

**THE FLAW (repairable): the threshold of LP-112⁻ does not reach far enough as stated.**
LP-112⁻ (D112, §2.2) says: "for every D and every ε > 0 there exists ONE τ > height(D)".
But the proof applies it "with τ > γ_max + γ₀ + r + 1". If height(D) = γ₀ + r and γ_max > γ₀ (the
chosen zero is not the highest one), the τ that LP-112⁻ guarantees could fall in
(γ₀+r, γ_max+γ₀+r+1] and the replica could land on an off-critical zero ALREADY listed:
no contradiction. As the two statements are written, the step "Apply LP-112⁻
... with τ > γ_max + γ₀ + r + 1" uses more than the hypothesis gives. Two one-line
repairs:

- **(R1) Repair the lemma:** LP-112⁻ should say "for every D, every ε > 0 and every T₀ there
  exists τ > T₀ with sup_D |ζ(s+iτ)−ζ(s)| < ε". This is the natural form, is still implied
  by full LP-112 (τ_k → ∞), and is what the proof actually uses.
- **(R2) Repair the proof:** choose ρ₀ with γ₀ = γ_max (the HIGHEST off-critical zero, which
  exists by finiteness). Then Im(z*+iτ) > γ₀ + τ − r > 2γ_max > γ_max for every
  τ > γ_max + r = height(D), and the current statement of LP-112⁻ literally suffices.

With full LP-112 (sequence τ_k → ∞) there is no flaw at all: the τ_k eventually exceed
any threshold. The flaw affects ONLY the weak variant as currently phrased. P44
(sketch, lines 158–165 of main.tex) uses full LP-112 and says "τ_k eventually exceeds
2γ_max" — correct given τ_k → ∞ (and in fact it suffices to exceed γ_max + γ₀ + r).

**Verdict for line 2: the mechanism is correct; either the statement of LP-112⁻ must be
corrected via (R1), or the proof via (R2).**

## 3. Line 3 — The iteration: VERIFIED

- **A single τ already contradicts.** H(m) says EXACTLY m; a new quadruple gives m+1 > m:
  immediate contradiction. The proof states this well (F4 of §1.2 and the body of Thm. 2.3);
  the iteration is only the direct form "m ≥ 1 ⟹ m = ∞".
- **Separation of replicas in the iterated form.** For the replicas to be distinct it
  suffices to have τ_{k+1} − τ_k > 2r; since τ_k → ∞, extracting the subsequence is trivial and the
  proof records it ("taking τ_k with separations > 2r"). ✓.
- Distinct replicas with Re > ½, Im > 0 generate distinct quadruples (one member of that
  type per quadruple). ✓.

**Verdict for line 3: no crack.**

## 4. Line 4 (the central one) — Prop. 2.6: zero density or EMPTINESS?

### 4.1. The proof of Prop. 2.6, line by line

1. **Bagchi's limit theorem.** Q_T(·) = T⁻¹·meas{τ∈[0,T] : ζ(·+iτ)|_{D′} ∈ ·} converges
   weakly in H(D′) (compact-open topology) to the law Q of the random Euler
   product. Unconditional; [Bag81], [Lau96, Ch. 5]. The pole of ζ is not touched: D′ ⊂ {Re < 1}.
   ✓ VERIFIED against the cited literature (consistent with Doc 102 §2.3 and the Matsumoto
   survey that D102 used as source).
2. **Support.** S = {f ∈ H(D′) : f ≠ 0 in D′} ∪ {0} ([Lau96, Ch. 6]; consequence of
   Hurwitz's theorem on limits of nonvanishing Euler products). ✓ standard.
3. **C_ε is closed.** f ↦ sup_{D̄(ρ₀,r)}|f − ζ| is continuous in the compact-open topology
   (the sup is over a compact set ⊂ D′) and C_ε = preimage of [0,ε]. ✓.
4. **C_ε ∩ S = ∅ for ε < η.** If f ∈ C_ε: on |s−ρ₀| = r, |f−ζ| ≤ ε < η = min|ζ|
   (strict inequality), Rouché gives f a zero in D(ρ₀,r) ⊂ D′, so f ∉ S unless f ≡ 0;
   and f ≡ 0 would give sup_{D̄}|ζ| ≤ ε < η ≤ sup_{∂D}|ζ|, absurd. ✓.
5. **Q(C_ε) = 0.** C_ε closed ⊂ (supp Q)^c, which is Q-null (definition of support on a
   Polish space; H(D′) is separable metrizable). ✓.
6. **Portmanteau.** For closed sets, limsup_T Q_T(C_ε) ≤ Q(C_ε) = 0; and
   meas(A_ε∩[0,T])/T = Q_T(C_ε) because τ ∈ A_ε ⟺ ζ(·+iτ)|_{D′} ∈ C_ε. ✓.

**Technical conclusion: Prop. 2.6 proves ZERO UPPER DENSITY and NOTHING MORE.** The reason is
structural, not laziness: weak convergence of measures is categorically unable to
detect emptiness — a set of null limiting measure can be visited by each Q_T on a
set of τ of positive-but-o(T) measure, or on a countable set, or on none; the
Bagchi+Portmanteau apparatus does not distinguish these cases. **Prop. 2.6 does NOT prove
emptiness, and no refinement of the same machinery could prove it.**

### 4.2. BUT: emptiness under H(m) is a theorem anyway — by Thm. 2.3 ITSELF

Here is the conceptual finding of this audit, and it must be stated with precision because
all three documents get it WRONG:

"LP-112⁻(D,ε,T₀) ⟹ ¬H(m)" is logically equivalent, by contraposition, to
"H(m) ⟹ A_ε ∩ (T₀,∞) = ∅" (with ε = η/2 and T₀ the height threshold). That is: **in the world
H(m), the set of witnesses above the threshold is not "of zero density and unknown
emptiness" — it is EMPTY, with certainty, by Theorem 2.3 itself.** Every element of it
would produce the quadruple m+1, and H(m) says exactly m.

Therefore:

- The table of D112 §6.1 ("under ¬RH that set is: density 0, emptiness UNKNOWN") and the
  sentence of D113 §0 ("its witnesses form a set of zero upper density whose emptiness
  is unknown") are **imprecise**: they conflate the two branches of ¬RH. Under 0 < m < ∞ the
  emptiness (above the threshold) is a THEOREM; what is unknown is the branch m = ∞, where
  Prop. 2.6 also gives zero density but nothing forces emptiness. The correct wording:
  "under H(m) the set is empty above the threshold (contraposition of Thm. 2.3); under m = ∞
  it has zero density and unknown emptiness; non-emptiness IN THE REAL WORLD is exactly what
  LP-112 demands".
- In particular, "exhibiting a τ ∈ A_ε" is not an intermediate step toward refuting H(m): **it
  IS refuting H(m)** — the same act, in another coordinate. Doc 112 half-knows this (it
  calls it "the master quantifier in almost-period coordinates") but the vocabulary of
  "zero density but perhaps not empty under the hypothesis to be refuted" suggests a logical
  space that does not exist.

### 4.3. Does this make Theorem 2.3 vacuous? NO — and the distinction is the key of the whole audit

The target question: if under 0 < m < ∞ hypothesis LP-112 is false, is the theorem
"false ⟹ anything", vacuous, and does P44 collapse?

**No.** Two kinds of emptiness must be distinguished:

- **Relative (harmless, universal) vacuity:** in the hypothetical world H(m), LP-112 is false.
  This is true — by contraposition of the theorem itself — and is the structure of EVERY
  proof by contradiction: if "A ∧ B ⟹ ⊥" is a theorem, then in every B-world, A is false.
  Bagchi's theorem has exactly the same property (under ¬RH strong recurrence
  is false) and nobody calls it vacuous. The usable conclusion is the contrapositive in the
  REAL world: whoever proves LP-112 unconditionally will have proved m ∈ {0,∞}.
- **Absolute (lethal, does NOT occur) vacuity:** LP-112 demonstrably false, period. That
  would kill the architecture. This is not the case: RH ⟹ LP-112 (Bagchi, hard half: under RH,
  ζ|_D does not vanish, belongs to the support, good τ have positive lower density),
  and RH is not refuted; moreover LP-112 is consistent with m = ∞ (the Rouché argument
  there only produces more zeros among the infinitely many already present — no contradiction, Prop. 2.7).
  LP-112 is exactly as refutable as RH: no more.

**ANSWER TO THE CENTRAL QUESTION OF THE ASSIGNMENT: zero density, not emptiness — as
far as Prop. 2.6 is concerned, whose proof is correct and structurally incapable of giving more.
Emptiness under H(m) (above the threshold) holds anyway, for free, by contraposition
of Thm. 2.3 — and it is harmless: emptiness relative to the hypothetical world, not emptiness of the
conditional. Theorem 2.3 is NOT vacuous. P44's architecture does not collapse here.**

What this finding DOES require: rewriting the "unknown emptiness" sentences (D112 §0.2,
§6.1 table, §7 gap; D113 §0 and §1.1) separating the branches, and acknowledging in P44 that the
real content of Prop. 2.6 lives in (i) the branch m = ∞ and (ii) the explanation of why no
averaging machinery can prove LP-112 — not in the branch 0 < m < ∞, where
the contraposition of the theorem trivially supersedes it.

## 5. Line 5 — Is the non-equivalence LP-112 ≠ RH PROVED or UNREFUTED?

**UNREFUTED. Not proved — and, in the material sense, UNLIKELY EVER TO BE PROVED.**

1. **The real argument of D112 §5.4(2):** LP-112 does not imply RH "via the density
   route" (its conclusion under ¬RH is m = ∞, consistent with Bohr–Landau; a sequence of zero
   density activates no amplifier against N(σ,T) = o(T)). This is correct and shows
   exactly what it says: that the ONLY known dictionary (density of replicas versus
   density theorems) does not turn LP-112 into RH. D112 itself states it: "an
   implication via an unknown route cannot be excluded — minor GAP declared". **That sentence
   is the whole truth.**
2. **An observation the documents do not make, and should:** as closed statements about ζ,
   if RH is true then LP-112 and RH are BOTH true and hence materially
   equivalent; "non-equivalence" can only mean "no known derivation of
   RH from LP-112 exists" — a META-mathematical statement about the state of the proofs, not a
   theorem about ζ. Proving material non-equivalence would require exhibiting consistency of
   LP-112 ∧ ¬RH (the branch m = ∞ with self-approximation), which is out of all reach.
   Moreover: nothing today excludes LP-112 being materially equivalent to RH — that in the branch
   m = ∞ the witnesses also fail (Prop. 2.6 applies verbatim there: zero density
   around any off-critical zero). The frank status is: **LP-112 is implied
   by RH, implies the dichotomy, and neither the reverse implication nor an obstruction to
   it is known.**
3. **Where each document overclaims:**
   - D112 §0.3: "the reason LP-112 remains alive as a non-RH-equivalent target" —
     overclaims (drops the "by known dictionaries").
   - D112 §7.3: "LP-112 remains alive, not RH-equivalent" and §7 "certificate of non-equivalence
     with RH" — **"certificate" is false**: what is certified is non-equivalence BY
     DENSITY METHODS, not non-equivalence outright.
   - D112 §5.4 body: correct and frank (explicit hedge + declared GAP). The body and the
     headlines of the same document do not say the same thing; the headlines must be brought down to the body.
   - D113: the body is frank ("does not ⟹ RH by known dictionaries", table §7); the
     summary §0.4 ("LP-113 is not RH-equivalent by known dictionaries, but...")
     keeps the hedge — acceptable.
   - **P44, §2.4 (line 196 of main.tex): the section title is "LP-112 is not
     RH-equivalent" — headline overclaim.** The body (lines 142–144, 197–203) does say
     "as far as every known dictionary reaches" and "no known dictionary upgrades it to RH" —
     frank. **Required correction: retitle** ("LP-112 is not known to be
     RH-equivalent" or "No known dictionary upgrades LP-112 to RH") and review line 104
     ("strictly weaker than every previously identified sufficient condition" — "strictly
     weaker" is only proved against strong recurrence AS A STATEMENT FORM, sequence
     vs. density; strict logical strength is not proved: if both turned out
     equivalent to RH, the "strictness" would collapse).
4. **Hidden circularity in the architecture?** There is no LOGICAL circularity: RH ⟸ L8 ∧
   LP-112 is a proved conditional, and using the architecture requires proving LP-112 without
   assuming anything about the zeros — a self-approximation statement, syntactically independent
   of the position of the zeros. The risk is STRATEGIC, not logical, and D113 documents it
   with brutal frankness: there is no precedent, no technique, all known machinery
   produces generics and the required witness is exceptional; in the worst world (which nobody
   can exclude) proving LP-112 is exactly as hard as RH. The architecture is
   frank IF AND ONLY IF it is presented as a bet: "the target is weaker as a statement;
   we do not know whether it is weaker as a problem". P44 must state that second half explicitly.

**ANSWER TO LINE 5: non-equivalence UNREFUTED, not proved; the language of the
headlines of D112 and of §2.4's title in P44 must be downgraded to that of the body of D112 §5.4,
which is already correct.**

## 6. Line 6 — Quantifiers: P44 states the STRONG form, Doc 112 the WEAK one

- **Doc 112, §2.2 (official):** "For every closed disk D ⊂ {½<σ<1} there exists a sequence
  τ_k → ∞ such that sup_D |ζ(s+iτ_k)−ζ(s)| → 0" — **∀D ∃sequence (weak).**
- **Doc 113, §0 (summary):** "there exists a sequence τ_k → ∞ such that ζ(s+iτ_k) → ζ(s)
  uniformly on every compact disk" — **∃sequence ∀D (strong).** (Its §1.1 then copies
  D112's weak form: an internal inconsistency within D113.)
- **P44, Definition def:lp112 (lines 133–137):** "There exists a sequence τ_k → ∞ such
  that ζ(s+iτ_k) → ζ(s) uniformly on every compact disk" — **strong.**

The two forms are NOT trivially equivalent. Strong ⟹ weak, obviously. Weak ⟹ strong
does NOT follow by direct diagonalization: the strip is not exhausted by an increasing chain of DISKS
(every disk in the strip has diameter smaller than the width of the strip), and the weak form gives
different sequences for different disks with no common witness — to produce a τ good
for D₁,…,D_n simultaneously would require the version with arbitrary compacts (rectangles)
or positive density, which is exactly what LP-112 avoids requiring. (Under RH both hold: Bagchi gives
positive density per compact with connected complement — growing rectangles — and the
diagonal argument closes. Unconditionally, weak and strong must be treated as
distinct statements.)

**Consequence for the correction:** the proof of Thm. 2.3 uses ONE single disk — the weak form
suffices. P44 assumes the strong form and so its theorem holds a fortiori (no logical error), but
states as its target hypothesis something stronger than necessary. **Correction in favor of
the program: P44 should state the weak form** ("for every compact disk D there exists a sequence…"),
which is (a) what the proof uses, (b) what D112 states, (c) the easier target. And D113 §0
must be aligned with its own §1.1.

## 7. Additional attacks by the auditor (beyond the minimum required)

1. **Does Bagchi's limit theorem hold on the chosen disk D′?** Yes: D′ compact-closed
   within the strip, not touching the pole (Re < 1); [Lau96] gives it for bounded regions with
   closure in the strip. No crack.
2. **Does Portmanteau require something about A_ε that is missing?** No: A_ε is exactly the preimage of
   C_ε under τ ↦ ζ(·+iτ)|_{D′}, measurable (continuous in τ), and the identity
   Q_T(C_ε) = meas(A_ε∩[0,T])/T holds by definition. No crack.
3. **Does Prop. 2.6 use η from Thm. 2.3 circularly?** No: η depends only on the
   configuration H(m), fixed beforehand; ε < η is a legitimate restriction of the statement.
4. **Is the case f ≡ 0 of the support properly excluded?** Yes (step 4 of §4.1 above); it is the only
   point where ζ needs to be non-tiny on the WHOLE disk, and the contour provides that.
5. **Does "m ≥ 1 ⟹ m = ∞" require anything extra when m = ∞ from the start?** No: vacuously true;
   the form with content is the contradiction under finite m, which is what is proved.
6. **D112↔P44 consistency in the sketch:** P44 says "new, since τ_k eventually exceeds
   2γ_max" — with γ₀ ≤ γ_max and r < ¼ one needs τ_k > γ_max + γ₀ + r, and 2γ_max covers it
   only if γ₀ + r ≤ γ_max, true except when γ₀ = γ_max, in which case the +r is missing; since
   τ_k → ∞, irrelevant — but the sketch would gain by writing the correct threshold
   γ_max + γ₀ + r from D112.

## 8. VERDICT

**SURVIVES WITH CORRECTIONS.** Theorem 2.3 of Doc 112 is correct in its mechanism
(choice of constants, Rouché, off-criticality, novelty, iteration: verified line
by line) and Proposition 2.6 is correct in its proof and in its stated scope
(zero upper density). The result is NOT refuted and P44's architecture does NOT
collapse. Required corrections, in order of importance:

1. **(Statement, real) LP-112⁻:** add the arbitrary threshold ("for every D, ε and T₀ there
   exists τ > T₀…") — repair (R1) — or change the proof to choose ρ₀ with γ₀ = γ_max —
   repair (R2). As it stands, the proof invokes a threshold that the weak lemma does not provide.
   (§2 above. With full LP-112 there is no flaw.)
2. **(Logical language, repeated) "Unknown emptiness":** under H(m) the emptiness of A_{η/2}
   above the threshold is a theorem (contraposition of Thm. 2.3 itself), not an unknown; what is
   unknown is the branch m = ∞ and non-emptiness in the real world. Correct D112 §0.2,
   §6.1 (table), §7; D113 §0 and §1.1. Clarify in P44 that "certifying a witness" and "refuting
   H(m)" are the same act. The theorem is NOT vacuous: the falsity of LP-112 is relative to the
   hypothetical world (the structure of every proof by contradiction), not absolute — RH ⟹ LP-112
   and LP-112 is consistent with m = ∞.
3. **(Overclaim) Non-equivalence with RH:** is UNREFUTED, not proved (and the material
   version is unprovable while RH remains open). Downgrade: D112 §0.3 and §7
   ("certificate of non-equivalence" → "non-equivalence by known dictionaries");
   P44 title of §2.4 ("is not RH-equivalent" → "is not known to be RH-equivalent") and
   line 104 ("strictly weaker" → qualify as statement strength, not problem strength).
4. **(Quantifier mismatch) P44 Definition def:lp112 and D113 §0** state the
   strong form (∃sequence ∀disk); D112 and the proof use the weak one (∀disk ∃sequence), which is not
   trivially equivalent (the strip is not exhausted by disks). State the weak form in P44 —
   correction in favor: easier target, and it is what the theorem needs.
5. **(Cosmetic) P44 sketch:** novelty threshold γ_max + γ₀ + r instead of "2γ_max".

**Answers to the two central questions of the assignment:** (line 4) Prop. 2.6 proves
zero density and only zero density — its machinery (weak convergence + Portmanteau) is
structurally incapable of proving emptiness; emptiness under H(m) holds equally by
contraposition of the theorem itself and is HARMLESS (relative, not absolute, emptiness): the
Theorem 2.3 is not vacuous and P44 does not collapse. (line 5) the non-equivalence LP-112/RH is
unrefuted, not proved; the body of D112 §5.4 already states this correctly and the headlines of D112 and
P44 must come down to that language.

---

## References

**Internal:** Doc 112 (§§0–7, object of the audit); Doc 113 (§§0–8); Doc 102 (Bagchi);
Doc 104 (anchored window); Doc 109 (identity RH = (m<∞) ∧ D-109); Doc 111 (cosh examples);
P43 (master quantifier); P44 (`06-papers/P44-two-lemma-architecture/main.tex`,
lines 95–203 verified against source for this audit).

**Literature (all already cited and verified in D112/D113; used here without addition):**
B. Bagchi, ISI thesis 1981; B. Bagchi, *Recurrence in topological dynamics and the Riemann
hypothesis*, Acta Math. Hungar. 50 (1987) 227–240; A. Laurinčikas, *Limit Theorems for the
Riemann Zeta-Function*, Kluwer 1996, Chaps. 5–6 (limit theorem and support); E. C. Titchmarsh,
*The Theory of the Riemann Zeta-Function*, 2nd ed. 1986 (Thm. 7.2, Chap. VIII); H. Bohr and
E. Landau, Rend. Circ. Mat. Palermo 37 (1914); H. Davenport and H. Heilbronn, J. London Math.
Soc. 11 (1936). For Portmanteau and support on Polish spaces: P. Billingsley, *Convergence
of Probability Measures*, 2nd ed., Wiley 1999, Thm. 2.1 (standard form of the Portmanteau
theorem for closed sets).

*End of Document 115.*
