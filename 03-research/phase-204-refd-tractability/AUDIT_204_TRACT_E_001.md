# AUDIT_204_TRACT_E_001 — audit of the tractability inventory, part E (phase 204, step 2)

Everything is stated D-only: window form 𝔞_T on P_T, λ_A(T), λ combs and their floor b_T(λ), and the
spectral side only as the side of the window explicit formula (thm:Z).
**Only file written: this one.**

**Read:** TRACT_E_PHASES_001 complete; TRACT_001 (criterion); TRACT_D_README_001 §0–§2 (groups G1–G17); L2_INTERLACE_001
§0, §1, §3, §7–§8; POLAR_CAP_001 §0–§1, §5–§6; AUDIT_203_001 §1; N_BUILD_011 §1–§2, N_BUILD_012 complete, N_BUILD_013
§3–§5, N_BUILD_014 §2–§4, N_BUILD_015 §3–§4 (phase 188, source of K12); `06_` R2–R6 and the residue table (l.192–206);
`04_` l.127–206, 389, 522, 560, 588, 604, 649, 661, 814; `03_` (full grep); R157_002 row 27.

## Summary (≤300 words)

1. **The 4 YESes do not survive.**
   - **K10:** dead as a route via L2_INTERLACE_001. The premise "k jumps at contacts" is false, and T13.1 falls into 𝒦_W ∪ 𝒦_H.
     Lemma E.1 is Hellmann–Feynman at the crossing (𝒦_H, PROOF_L_SHARP_H_001). Moreover, its "input for D" is empty: lem:monoT
     already gives λ_A non-increasing in T, so reducing the ∀T to a discrete sequence contributes nothing.
   - **K11:** agrees with POLAR_CAP_001. 𝔤_par is defined by inverting 𝔞|𝒬^par. It becomes TRANSFER as a goal and NO-GO as a route.
   - **K12:** the comb λ_t = (1−t)ρ_κ + tΛ is not the global factor cΛ. The endpoint t = 0 has uniform margin η_κ > 0, so
     AUDIT_203 does not apply. But:
     - "strictly weaker (PROVED)" is mislabeled: only D ⇒ (Ω_{t₀}) is PROVED; the separation is OPEN;
     - Lemma E.2 is, by N_013 Thm 3, equivalent to (E_γ) (K37);
     - concavity in t only gives lower bounds on [0, t*] (this is INVENT's Theorem 2.3), so t_∞ > 0 does not push t → 1.
     Moves to TRANSFER.
   - **K26:** is not REF-D (the index says so explicitly). Moreover, the "Sylvester in a few lines" proof is false if
     Q₂ = W⊗W: n₋ = 2pn = ∞ with p = ∞. It leaves the inventory.
2. **NOs not mis-closed:** K7b (Problem B: OPEN-RESIDUE; two candidates died, branch E3 is still alive), K9 (the part =D_T is
   not closed by any falsifier) and K36 (only the linearized version died). All three move to TRANSFER. No NO or TRANSFER rises
   to YES: 9 debatable cases were reviewed.
3. **K × G:** 33 of the 38 Ks have a G pair or are covered. Groups G3, G8, G11, G13 and G16 have no K. There are **43
   distinct reformulations** in README + 04_ + 06_.
4. **Omissions:** 13 lines without "REF-D" in 04_/06_, all already covered by some K. `03_` has 1 REF-D line and 28 "CIRCULAR"
   lines: they fail by omission in the inventory. Only one is new, Nyman–Beurling, and it has no D-only form.
5. **Corrected inventory E:** **0 YES / 20 TRANSFER / 18 NO** (38 K). No active first lemma remains in E.

Row D: OPEN. L′♯: OPEN.

---

## 1. Task 1 — the 21 NOs and the 14 TRANSFERs, K by K

Criterion applied (TRACT_001's, unchanged): **NO** requires a class theorem or a falsifier covering *the
reformulation exactly as written*, not a stronger variant nor a pair of candidates. **TRANSFER** requires the available
general theory to consume the sign. **YES** requires a class of theorems 𝒯 and a remaining hypothesis distinct from the sign.

### 1.1 Verification table

| K | E verdict | does the citation cover the D-only form? | audited verdict |
|---|---|---|---|
| K1 Herglotz/dB | TRANSFER | yes: Nevanlinna/de Branges take the positive measure as data | TRANSFER |
| K2 Kreĭn | TRANSFER | yes (R3 ⇒ D; the converse OPEN; Kreĭn theory consumes a positive measure) | TRANSFER |
| K3 Li/finite order | TRANSFER | yes; each finite order holds, uniformity is the content | TRANSFER |
| K4 Douglas/… | TRANSFER (924 NO) | yes; l.924 closed by σ_T(0) < 0 PROVED | TRANSFER |
| K5 A_T/Schur | TRANSFER | yes (=D_T, Szegő consumes the symbol) | TRANSFER |
| K6 objects | NO | W10 + R173 + T5 cover *postulated carriers*; "alive as a construction" correct | NO (reformulation); construction outside E |
| K7 thm:Z/cone | TRANSFER | yes (cone duality) | TRANSFER |
| **K7b Problem B** | NO | **no**: "M1 killed both candidates", "surviving branch E3" (04_ l.389, 604); 06_ l.192 OPEN-RESIDUE | **TRANSFER (OPEN)** — §1.2(a) |
| K8 uniformity | TRANSFER | yes; κ>0 is weaker but the hypothesis is a new band | TRANSFER — §1.2(b) |
| **K9 Sonin** | NO (dominant) | **only partially**: 1007 falsifies (L-Son) uniform (>D); the form =D_T ρ*(T) < 1 is not closed | **TRANSFER** — §1.2(c) |
| K13 exact chains | NO | yes: W12, W5, W-det are class (sign-free identities) | NO |
| K14 estimates | NO | yes for estimates (lem:shape-est, PROVED); GAP-157.A only "EXCL as instantiated" | NO, with the caveat §1.2(d) |
| K15 function fields | NO | yes (W8, F3) | NO |
| K16 spectral realization | NO | yes: W-identification (R168 Thm 1.1–2.3) covers the class | NO |
| K17 witnesses | NO | yes (W-jet Thm 1.3 PROVED; W5) | NO |
| K18 monotone functionals | NO | mostly yes; flat CD(0,∞) and "local maximum" are instance falsifiers | NO — §1.2(e) |
| K19 algebraic Euler | NO | yes (W7, prime-by-prime split cocycle) | NO |
| K20 integrality | NO | yes (W3′ Thm O, Lemma U) | NO |
| K21 local Laguerre | NO | yes: the equivalence is false (PROVED), it is not a reformulation | NO (and redundant in the inventory) |
| K22 commutators | NO | yes (W6, Thm N) | NO |
| K23 polar/Frobenius | NO | yes (W11; refutation D.0) | NO |
| K24 SOS | NO | yes for T ≥ ½log3 (thm:sos) | NO |
| K25 tensor | NO | yes (σ₀ = 0, W2) | NO |
| K27 signed combs | NO | yes (W4; G_p indefinite PROVED) | NO |
| K28 Thm A at large T | TRANSFER | yes (Prop 5 of phase 153) | TRANSFER |
| K29 angular bound | NO | yes (‖K‖² ≳ e^{…} PROVED) | NO |
| K30 uniform in L | NO | yes (T1; (Q*) false in Type I) | NO |
| K31 R-C.a | TRANSFER | yes | TRANSFER |
| K32 Bagchi/LP-112 | TRANSFER | **not audited D-only** (the memo itself admits it); LP-112 is "DEAD as a route; statement OPEN" (06_ l.201) | TRANSFER (no D-only form written; see §4) |
| K33 deficit/MW-7 | NO | yes (MW-7 is a class barrier) | NO |
| K34 (N_loc) | TRANSFER | yes | TRANSFER |
| K35 (Ω₀) | TRANSFER (∀T) | yes; in bounded T it is proved with known technology, which contributes nothing to D | TRANSFER |
| **K36 (Ω_Φ)** | NO | **no**: N_010 closes only perturbative/linearized 𝒦_T; 06_ R4 leaves the non-perturbative 𝒦_T OPEN | **TRANSFER (OPEN, no 𝒯)** — §1.2(f) |
| K37 (E_γ) | TRANSFER | yes (critical; N_013 §4: Hadamard, MV and Selberg do not give the sign, CITED) | TRANSFER — §1.2(g) |
| K38 lower half | TRANSFER | yes; also, with lem:monoT, "λ_A ≥ −o(1)" ⟹ λ_A ≥ 0 is immediate | TRANSFER |

### 1.2 Debatable cases (nine), argued

**(a) K7b Problem B — NO → TRANSFER.** The index literally says "M1 (R160) killed both candidates" and "surviving branch
E3" (04_ l.389, l.604), and 06_ l.192 lists it as OPEN-RESIDUE. Killing two candidates is not a class theorem. Does it rise to
YES? No: the statement is >D and constructive, and the only general theory at hand (LP synthesis of certificates) takes the
positivity of the dual cone (thm:Z/thm:O) as data. TRANSFER, OPEN.

**(b) K8, branch κ > 0 (gradual law λ_A ≥ −Ce^{κT}).** It is the most serious candidate to rise: it is strictly weaker and the
trivial bound already gives some κ. The reason not to raise it:
- the gradual converse PROVED turns each κ < κ_triv into a band of width O(κ) on the spectral side of thm:Z, which is a
  problem of uniform bounds in T;
- W-fam (P46 thm:famblind) excludes bounded-rank functionals;
- lem:shape-est closes the shape estimates.

There is no 𝒯 whose hypothesis is anything other than a savings bound on the fluctuation of Λ in the window. TRANSFER
confirmed.

**(c) K9 Sonin — NO → TRANSFER.** The equivalence ρ*(T) < 1 ⟺ D_T is PROVED (all-or-nothing Müntz). What each theorem closes:
- the low-band falsifier (l.1007) closes **uniform (L-Son)**, which is stronger;
- W-Sonin (l.1003) and W11′ (l.1013/1029) close proof routes;
- none closes the statement ρ*(T) < 1.

Classifying all of K9 as NO because of its "dominant part" is exactly the omission that instruction (a) forbids. Does it rise
to YES? No: the spectral radius of a semilocal Sonin operator has no general theory bounding it below 1 without the sign
datum (ρ* is invariant, phase 183–186, "semilocal Sonin chain PROVED, no sign").

**(d) K14 / GAP-157.A.** TRACT_E gives it as NO "by cor:void/F1 (R157_002 #27)", but what each source actually says is:
- R157_002 row 27: "EXCL (**as instantiated**)", and the exclusion holds only for *positions-only inputs* (cor:void over
  C_supp);
- 06_ l.202: "condition C1 neither known nor excluded".

The correct conclusion has two parts:
- NO for any argument whose input is positions only (LI of log p): cor:void, PROVED;
- OPEN for a non-local Tauberian argument that uses **values** of Λ in addition to LI.

It does not rise to YES: it is not a reformulation but an input search, and C1 is not written D-only in the record. It is
recommended to note the nuance in row K14 and not count it separately.

**(e) K18 monotone functionals.** What each falsifier closes:
- "flat CD(0,∞): no gap" closes the Bakry–Émery route;
- "monotone laws hold for DH/finmod" is a class falsifier via thm:noimport(i);
- "local maximum at b = 0" closes the minimization.

All three cover the form as written. NO confirmed.

**(f) K36 (Ω_Φ) — NO → TRANSFER (OPEN, no 𝒯).** TRACT_E identifies it with R8/Φ.1 branch 2. But 06_ R4 says: "Perturbative or
Lipschitz 𝒦_T linearized at Λ is tautological" (NO-GO) and "Admissible directions: Only a non-perturbative, non-local 𝒦_T".
Φ.1 covers the linearization, not the global residue. It does not rise to YES because no quantitative candidate exists
(06_: "No quantitative candidate"): there is no 𝒯 to apply.

**(g) K37 (E_γ).** Does it rise to YES for being "a single frequency"? No. N_013 §1 and §3 show that the packet limit is
*exactly* m♯(γ), so (E_γ) is critical at each γ, and (E_γ, C) ⟺ (E_γ) for every C (CONDITIONAL on Hardy–Riesz summability).
A critical inequality admits no estimation 𝒯 (lem:shape-est). TRANSFER confirmed.

**(h) K35 (Ω₀) at bounded T.** That it is "YES in a finite range" is true but irrelevant: it is boundary technology (½log15)
and gives no uniform statement. The correct label is TRANSFER, not counted as YES. Agrees with TRACT_E.

**(i) K21.** TRACT_E counts it as NO, but the equivalence with (★_cell) is FALSE (PROVED) and degree 2 is derived from D, not
the other way around. **It is not a reformulation of D**; it should leave the inventory like K26. It is not removed here to
avoid moving the count unnecessarily, but it is noted.

**Task 1 result.** There are three NOs mis-closed by omission (K7b, K9, K36), which move to TRANSFER. No NO or TRANSFER rises
to YES: in the nine debatable cases the remaining hypothesis is the sign, or there is no 𝒯.

---

## 2. Task 2 — the four YESes

### 2.1 K10 / Lemma E.1 — **NO-GO as a route; TRANSFER as a goal**

L2_INTERLACE_001 (§1, §3, §7) already killed the TRACT_001 form:
- k is the number of blocks, not of contacts; S_{T,k} is continuous and of fixed size on T_n (U0);
- T13.1 (non-vanishing of det S between contacts) is Hellmann–Feynman at the crossing, a functional of h* (𝒦_W ∪ 𝒦_H);
- T13.2 has no rank-one edge.

The question is whether Lemma E.1 of TRACT_E §3.1 (EL + Hadamard boundary trace at the crossing) survives as "exact
rigidity". **It does not survive**, for three independent reasons.

1. **(b) is 𝒦_H.** The Hadamard condition ∂_T𝔞_T(F*)|_{T*} = 0 is the T-derivative of the form evaluated at the minimizer.
   It is literally a coefficient "evaluated at the minimizer", which is the definition of 𝒦_H (PROOF_L_SHARP_H_001), and its
   value is the pairing Σ v_n c_{h*}(log n), which BARRIER_W_001 identifies as *the only* crossing datum specific to Λ.
   POLAR_CAP_001 T6.1 says the same for the polar floor: the Hadamard derivative is a boundary trace of the residue, a
   functional of the resolvent, NO-GO (𝒦_H). That E.1 asks for a *qualitative* consequence ("forces F* ∈ 𝒢̄") does not remove
   it from the class: the datum that enters is still the same functional of h*. An exact rigidity would only dodge 𝒦_H if it
   used information about Λ that does not pass through h*, and E.1 does not name one.
2. **E.1's "input for D" is empty.** TRACT_E says that, if E.1 goes through, "it reduces D to the contact instants (discrete
   set {½log n})". But lem:monoT (P46; N_012 §1(a) reuses it for general combs) already gives that T ↦ λ_A(T) is
   **non-increasing** by extension by zero. Then D (∀T) is equivalent, without any lemma, to λ_A(T_n) ≥ 0 over *any*
   sequence T_n → ∞. Reducing to a discrete set gains nothing.
3. **Cor 2′ and the margin scale.** In the first interval (½log5, ½log7) the margin is already tiny: CA_R4_001 shows
   four-copy cancellation at 1.6·10⁻⁶. L2_INTERLACE §3 gives |dλ_A/dT| ≲ 10⁻⁷⁰ in the direction of h* at the relevant scale.
   The "falsifiability in the first interval" proposed by TRACT_E discriminates nothing.

**K10 verdict:** YES → **TRANSFER** (goal (L2) alive and OPEN in 06_ R1). The crossing rigidity route is NO-GO (𝒦_H) and
**is not retried** without a datum of Λ that is not a functional of h*. Lemma E.1 is withdrawn.

### 2.2 K11 — **agrees with POLAR_CAP_001: TRANSFER (goal) / NO-GO (route)**

Verified against the definition (thm:parityschur(a) and prop:polarcap, P46 l.4176/4316):
- 𝔤_par = 𝔞_T(H₀) − ⟨𝔞_T(H₀,·), (𝔞_T|𝒬^par)^{-1}𝔞_T(H₀,·)⟩ + 2ε_par is a bordered Schur complement: it inverts the primitive
  part;
- the definition only consumes non-degeneracy, but every property connecting 𝔤 with W_T ≥ 0 consumes λ_A^par > 0 ((a3),
  (a4), lem:gmono).

By Lemma T3 of L2_INTERLACE, In(W) = In(𝔞|𝒱_k) + In(S_{T,k}) + In(𝔊_T): K11 is *the upper floor* of K10's tower, not a
separate object. The verdict is shared. Nuance: "TRANSFER/NO" should read "TRANSFER as a reformulation; NO-GO as a dynamic
route (Hadamard + no-crossing)". The ceiling PC-2 (𝔤_ev ≲ 9·10⁻⁸, NUMERICAL) reinforces that there is no margin here either.

### 2.3 K12 (Ω_{t₀}), t_∞ > 0 — **TRANSFER**

**(i) Exact definition (N_BUILD_011 §2 and N_BUILD_012 §1).** The pieces are:
- ρ_κ := 2κe^{u/2}du on (0,∞);
- the comb of the form 𝔞_T^{(ρ_κ)}(F) = (1/2π)∫g_κ|F̂|², with g_κ = m + κ/(¼+τ²);
- ρ_κ ∈ Pos ⟺ κ ≥ κ* (≥ 1.343);
- for κ > κ*, b_T(ρ_κ) ≥ η_κ > 0 **uniformly in T** (PROVED).

With λ_t = (1−t)ρ_κ + tΛ, define t*(T) = sup{t : b_T(λ_t) ≥ 0} and t_∞ = lim t*(T), which exists by monotonicity.

**(ii) A global factor cΛ? No.** It is an interpolation between Λ and a *continuous* comb ρ_κ with a uniformly positive
floor, not the line c ↦ cΛ. The endpoint t = 0 is ρ_κ, not the null comb. AUDIT_203's observation (λ_A(0·Λ) = λ_{∞,P}(T) < 0
for T ≥ 0.60; interior maximum; ≈ 0 at c = 1) is about a = 0 (Arch + Pol) and **does not apply** here. Here b_T(0) ≥ η_κ > 0,
and "t*(T) > 0 ∀T" is PROVED with the crude bound t*(T) ≥ η_κ/(η_κ + A_T + 4 + |C₀+4|) ≍ e^{−T} (N_012 §4). The "∀T" is not
false. What is open is whether t_∞ > 0.

**(iii) "Strictly weaker than D (PROVED)" is mislabeled.** What is PROVED is:
- t_∞ = 1 ⟺ D (N_012 §1(c));
- D ⇒ t_∞ > 0 (trivial);
- if D fails, t_∞ ≤ t₁ < 1, with t₁ depending on the witness.

What is **not** proved is that t_∞ > 0 is *strictly* weaker, i.e. that (Ω_{t₀}) does not imply D. N_012 says "not equivalent
to the target **by any argument in the record**", which is an absence of proof, not a separation. There are also indications
to the contrary:
- **N_013 §5 (ARGUED):** (Ω_{t₀}) and (N) coincide on every family whose spectral measures converge weakly. Any separation
  would have to come from families with non-convergent spectral measure.
- **N_014 Thm A (PROVED) + N_015 §4:**
  - if the spectral side of the window explicit formula has an uncancelled singularity at σ₀ > 0, then limsup Ξ = +∞
    (Landau-type argument, CITED), and by Thm A, t_∞ = 0;
  - in the other direction, in the absence of such singularities row D holds (by thm:Z);
  - the trichotomy {0} ∪ (0,1) ∪ {1} tends to collapse to the dichotomy {0, 1}. This is ARGUED: uniformity over the
    profiles F₀ and control of the cancellation of C(ρ−½) are missing.

**Correct label:** "D ⇒ (Ω_{t₀}) PROVED; separation OPEN; collapse to dichotomy ARGUED". The summary of TRACT_E and the line
in 06_ R3 ("strictly weaker") must be corrected to "weaker; strictness OPEN".

**(iv) Lemma E.2 is not new: it is (E_γ).** E.2 asks, for packets concentrating at γ, limsup 𝔞^{λ_t}_T(F_T) ≥ (1−t)c(κ,γ).
On packets, 𝔞^{λ_t} = (1−t)G_κ(F_T) + t𝔞_T(F_T), with G_κ(F_T) → g_κ(γ) ≥ η_κ. By N_013 §2–§3 there are two cases:
- either 𝔞_T(F_T) converges to its critical value (the one fixed by m♯(γ)), and then E.2 holds outright with c = g_κ(γ);
- or it diverges to the bad side, and then E.2 fails for every t > 0.

That is, E.2 ⟺ (E_γ) (CONDITIONAL, same as N_013 Thm 3). This is what N_013 records: "**NO-GO for (Ω_{t₀}) via single
frequencies: packets cannot separate t_∞ > 0 from t_∞ = 1**". TRACT_E confuses the *criticality* of the packet with a
collapse that could loosen for t < 1. It does not loosen, because the factor (1−t) multiplies only G_κ, which is harmless,
and the Λ term enters with weight t > 0 unchanged. Lemma E.2 retries N_013 and is forbidden by the index rule.

**(v) Is the input for D real?** No. b_T(t) is concave in t (infimum of affine functions). Concavity bounds from below
**only with chords between points of known value** (INVENT's Theorem 2.3, CONFIRMED in AUDIT_203 §1.2):
- with b_T(0) ≥ η_κ and b_T(t*) = 0, the chord gives b_T(t) ≥ (1 − t/t*)η_κ on [0, t*];
- beyond t* it gives nothing.

t_∞ > 0 would be an independent theorem ("a fixed fraction of the fluctuation is harmless"), but it provides no bound at
t = 1. The phrase "turns D into an interpolation problem t₀ → 1 with non-degenerate margin" is rhetorical: interpolating
from t_∞ > 0 to t_∞ = 1 is *the entire* problem, and concavity only gives upper bounds over that stretch (Danskin's tangent
at t*: b_T′(t*) = −G_κ(h)/t* < 0, N_012 §2(iii)).

**(vi) "Escapes W2 by construction".** True for t < t*(T), but trivial: any comb strictly inside Pos has margin. It is not a
feature of the reformulation that helps reach t = 1, where thm:margin still holds.

**K12 verdict:** YES → **TRANSFER**. On packets it is (E_γ) (K37, critical); on two-copy families it is (Ξ), with the
direction PROVED t_∞ = 0 ⇐ Ξ unbounded and the converse OPEN; on non-convergent spectral families it is OPEN and without 𝒯
(it is the "admissible direction" 06_ R3 already records, so it is not new). First lemma: none new. Any attempt resuming R3
must start from families that are neither packets nor translation/modulation (SYNTHESIS_188 §4.2), with a written reason.

### 2.4 K26 Lemma 108 — **leaves the inventory**

- **What it is.** It is the sieve→index bridge bound of doc 108 (phase 36, P36-5 in 03_ l.151; 04_ l.661; 06_ l.204):
  κ_W(Q₂) ≤ C·n_W, the negative index of the bivariate Weil form Q₂ bounded by the index of the univariate one.
- **Not REF-D.** 04_ l.661 says "**Explicitly not [REF-D]**; never attacked" and 06_ l.204 says "not REF-D". The lemma is not
  a reformulation of D. Its route died because "sup κ_W restates the target at k=2" (i.e. the *uniform bound* would be the
  reformulation, not the lemma). Putting it in a REF-D reformulations inventory is a scope error.
- **"Likely PROVED in a few lines by Sylvester" is false on the natural reading.** If Q₂ = W⊗W, then, by the formula itself
  sig(W⊗W) = (p²+n², 2pn) (04_ l.814), n₋(Q₂) = 2·p_W·n_W. For the Weil form p_W = ∞, so n_W ≥ 1 ⇒ κ_W(Q₂) = ∞, and the
  bound κ ≤ C·n_W **fails** except in the trivial case n_W = 0. If Q₂ is the *diagonal* bivariate kernel W₂
  (06_ l.198, P36-4 OPEN, pair-correlation wall) and not the tensor product, the lemma is not inertia linear algebra and
  TRACT_E gave no argument.
- **Input:** none, as TRACT_E admits.

**K26 verdict:** out of the REF-D inventory. As a lemma: OPEN if Q₂ = W₂; FALSE if Q₂ = W⊗W and n_W ≥ 1. Not a YES.

---

## 3. Task 3 — K × G cross-reference

| G (TRACT_D) | equivalent K (TRACT_E) | comment |
|---|---|---|
| G1 dual certificate / ν̂ ≥ 0 / LP / Herglotz / Gram | **K7**, **K1** (Herglotz), K24 (Gram/SOS partial) | same reformulation (R7); TRACT_D counts it 15 times |
| G2 (★★) / 𝒲_ext / Sonin ring / moments | **K9** (Sonin), K17 partial (Γ-moments) | R1 |
| G3 gauge-minimized L′♯ | — | no K (R2; its Fredholm route → K10 died with K10) |
| G4 polar capacity / boundary triple / KVB / Kreĭn | **K11**, **K2** (Kreĭn) | R3 + R6 |
| G5 Schur in block A_⊥⊥ / C_RR / N3 / V6 | **K5** | R4 |
| G6 Hodge / Horn / Big♯ / Restatement 19.29 | **K6** | R5 |
| G7 "the mass is in the zeros" / Stokes | K29, K33, K21 (partial) | spectral side; NO |
| G8 Arch ≥ Near / (S) / T*₃(η) | — (only note R9 in TRACT_E) | **no K**; TRANSFER (TRACT_E note) |
| G9 exterior field C*_A / Lemma S / central cell | K17 (first-contact witness), K21 ((★_cell)) | same object (minimizer at the contact) |
| G10 induction by contacts L*_j / B8 / (L2) | **K10** | R13; dies with K10 (§2.1) |
| G11 concavity in c / Danskin / D_∃c / 𝖯⋆ | — | **no K**; **K12 is G11 along another line** (same concave machinery, same Theorem 2.3) |
| G12 quantitative REF-D⁺ | K38, K20 (quantitative Hamburger) | |
| G13 (Π_L) Green energy | — | **no K** |
| G14 spectral flow / Maslov / Floer | K13 (spectral flow, Kreĭn shift) | TRACT_D used it as an R6/R13 tool: **falls with K10/K11** (BARRIER_W_001's 𝒦_W explicitly includes spectral flow and Maslov) |
| G15 sign-free identities | K13, K19, K22 | NO |
| G16 Lemma F (convexity in ε) | — | **no K** (phases 200+, outside E) |
| G17 theorems producing "branch 2" | K36 (Φ.1), K24 | meta: not a reformulation |

**Cross-reference audit observations:**
- **G14 can no longer stand as YES in TRACT_D.** BARRIER_W_001 closes 𝒦_W = index / spectral flow / Kreĭn / Maslov over the
  structural class 𝒮. TRACT_D said G14 was "the general theorem R6/R13 was missing". With K10 and K11 in TRANSFER/NO-GO,
  **G14 falls with them.** Noted for the coordinator since it touches part D.
- **K12 ⊂ G11.** Both are "concavity of the floor in an affine comb parameter". AUDIT_203 confirmed for G11 that there are
  only upper bounds except for chords, and that same fact kills K12's input (§2.3(v)). They are the same method class
  applied to two different lines.
- K8 (uniformity in T) touches G11 via "D_∃c", but it is not counted as the same reformulation.

**Count of distinct reformulations across the whole index (README + 04_ + 06_):**
- Valid Ks: 39 − 1 (K26, out) = **38**. K21 is noted as "not a reformulation", but it is kept.
- G without K: G3, G8, G11, G13, G16 = **5**. G17 is meta and does not count.
- **Total: 43 distinct reformulations.** If K21 and G16 are also removed (Lemma F is a tool lemma, not a reformulation
  of D), 41 remain. **43** is given as the inventory figure and 41 as the honest lower bound.

---

## 4. Task 4 — omissions

### 4.1 04_ and 06_: reformulation-type lines without "REF-D"

grep `rama 2|restatement|tautolog|equivalente a|reescritura|mismo objeto|restates|rewrit|same object` without "REF-D":

| line | entry | K | treatment |
|---|---|---|---|
| 04_ l.18 | W6 linear completions, "tautological" | K22 | NO (W6) |
| 04_ l.127 | R186-1mode, AL-k alignment, "rewrite of W≥0" | K5/K17 | NO (FALSIFIED) |
| 04_ l.131 | R186-Gram G_k(T), (L2_k), "rewrite of W≥0" | **K10** (exact alias) | TRANSFER |
| 04_ l.142 | R186-phase, phase alignment, tautological | K4 (Wiener–Hopf) | NO (FALSIFIED) |
| 04_ l.176 | N_009/010 Poisson–Euler, linearized tautological | K36 | TRANSFER (global OPEN; §1.2(f)) |
| 04_ l.206 | P158 MW-5, "restatement; Lemma T" | K6 | NO |
| 04_ l.407 | G2_B3 Hermitian squares; "Landau converse restatement" | K24 | NO (F2) |
| 04_ l.496 | Berkovich, "Restatement within A+; energies outside A+ not excluded" | K6 | **TRANSFER**, not NO: the part outside A+ is not closed (PARTIAL) |
| 04_ l.741 | (PC-ren), linear tautology | K22 | NO |
| 04_ l.824 | ledger D_a ≡ 0, "rewriting of weights" | K20 | NO |
| 04_ l.898 | Euler gate (G), "restatement: … ⟺ D on window" via Lemma U | K20 | NO (Lemma U) |
| 06_ l.40 | segment-by-segment resummation / prime-by-prime Euler, tautological | K14 | NO |
| 06_ l.90 | linearized 𝒦_T tautological | K36 | (covered) |

None contributes a new reformulation. There are two effects: l.131 confirms that K10 already had in the index a "NO-GO as
route (rewrite of W≥0)" verdict that TRACT_E did not cite, and l.496 nuances K6, whose Berkovich subpart outside A+ is
TRANSFER/OPEN, not NO.

### 4.2 03_PHASES_000-099.md (not reviewed by TRACT_E)

- **REF-D: 1 line** (l.256). It is a cross note on boundary triples → K11. Covered.
- **The vocabulary of phases 0–99 is "CIRCULAR" ("proved restatement"), not REF-D: 28 lines.** TRACT_E omitted them wholesale.
  They are assigned here with a quick verdict:

| 03_ entries | K | quick treatment |
|---|---|---|
| MW-6 (uniform spectral gap), NG-E2 (scalar λ_min) | K8 / K5 | TRANSFER |
| MW-7 (Hadamard barrier) | K33 | NO |
| NG-A5/CIR-6, NG-B6/CIR-4 (Turán), ES-17 (Hurwitz), ES-27, P33-10 (Jensen) | K3 | TRANSFER |
| NG-A8 (spectral-side Gram PSD by construction) | K7 | NO (tautology) |
| CIR-1/2/5/7/8, P33-5, P49-3 (Tauberian) | K14 | NO / TRANSFER (Tauberian: K14 local-frequency) |
| NG-D3 (Euler + FE) | K27/K19 | NO |
| ES-13 (Fejér–Riesz), ES-19 (GLT/passivity) | K4 / K1 | TRANSFER |
| ES-16 (de Branges / Hermite–Biehler) | K1 | TRANSFER / FALSIFIED (Conrey–Li) |
| P32-2 (PCN), P32-3 (CTP), P81 (bordered secular) | K13 | NO / TRANSFER |
| P33-2 (pointwise |ζ|²), P33-9 (measure difference) | K29 / K2 | TRANSFER |
| P33-11 (entropy/KL), P33-12 and P70 (dBN flow, Lee–Yang) | K18 | NO |
| P34-2 (Pontryagin space κ = 0, seven routes) | K2 / K10 (index) | TRANSFER |
| P40-3 (Hodge index), P42-1 (Forni/EKZ) | K6 | NO |
| P73 (cell residue, tautological rowspace version) | K5 | TRANSFER (PARTIAL) |
| P36-5 Lemma 108 | K26 | out (§2.4) |
| **NG-B4/CIR-3, P33-8 (Nyman–Beurling)** | **none** | **outside D-only** (below) |

**Only absent reformulation: Nyman–Beurling.** It is a distance criterion in L²(0,1) stated over ζ. The record has no
window form (𝔞_T, λ_A, thm:Z) for it, so it is not a D-only reformulation and is not counted among the 43. If someone
wanted to bring it to D, it would first have to be written as a statement over 𝔞_T; until then the index keeps it as
CIRCULAR (phase 33) and it is not retried.

**Omissions by default (instruction (a)).** None of the 28 CIRCULAR entries hides a route of its own: all fall into
already-classified Ks. The CIRCULAR entries that should be TRANSFER rather than NO are those of K3, K1 and K2, consistent
with the table in §1.

---

## 5. Final verdict of the corrected inventory E

### 5.1 Reclassifications

| K | E | audited | reason |
|---|---|---|---|
| K10 | YES | TRANSFER (NO-GO route) | L2_INTERLACE; Lemma E.1 ∈ 𝒦_H; input empty by lem:monoT |
| K11 | YES | TRANSFER (NO-GO route) | POLAR_CAP_001 (bordered Schur; 𝒦_H) |
| K12 | YES | TRANSFER | E.2 ⟺ (E_γ) (N_013); concavity gives no input at t = 1; separation OPEN |
| K26 | YES | **out** | not REF-D; Sylvester fails (2pn = ∞) |
| K7b | NO | TRANSFER (OPEN) | dead candidates ≠ class; branch E3 alive |
| K9 | NO | TRANSFER | the falsifier covers (L-Son) >D, not ρ* < 1 |
| K36 | NO | TRANSFER (OPEN, no 𝒯) | only the linearization died |

### 5.2 Count

| class | n | which |
|---|---|---|
| K reformulations (without K26) | **38** | |
| **YES** | **0** | — |
| **TRANSFER** | **20** | K1, K2, K3, K4, K5, K7, K7b, K8, K9, K10, K11, K12, K28, K31, K32, K34, K35, K36, K37, K38 |
| **NO** | **18** | K6, K13, K14, K15, K16, K17, K18, K19, K20, K21, K22, K23, K24, K25, K27, K29, K30, K33 |
| distinct across the whole index | **43** (lower bound 41) | 38 K + G3, G8, G11, G13, G16 |

### 5.3 Definitive list of YESes with first lemma

**Empty in part E.** What part E proposed:
- E.1 (crossing rigidity): withdrawn, it is 𝒦_H;
- E.2 (packet with fraction): withdrawn, it is (E_γ) and retries N_013;
- Lemma 108: out of scope.

Outside E, and not audited here, the only residual YES in the program is G16 / R10 (Lemma F), which TRACT_D already
downgraded to "weak conditional YES". It is recommended not to resume K10, K11 or K12 without a new written reason naming
**a datum of Λ that is not a functional of the minimizer h*** (for K10/K11) or **a family of tests with non-convergent
spectral measure that is neither packets nor translation/modulation** (for K12).

### 5.4 Corrections to the TRACT_E text

1. Summary and §3.2(b): "strictly weaker (PROVED)" → "D ⇒ (Ω_{t₀}) PROVED; separation OPEN; collapse to dichotomy ARGUED
   (N_013 §5, N_014 Thm A, N_015 §4)". Same in 06_ R3.
2. §3.1: the input "reduces D to contact instants" is empty by lem:monoT.
3. §3.3: "likely PROVED by Sylvester" is false for Q₂ = W⊗W.
4. §5: K12 stops being #1 in the ranking. TRACT_E has no positive ranking.
5. §6: the correction to TRACT_001 §5 (continuation barriers in T: Cor 2′, L2_003, L2_016) is **correct and stands**. It is
   TRACT_E's best contribution. 𝒦_H (PROOF_L_SHARP_H_001) and 𝒦_W (BARRIER_W_001) should be added to it, as these are what
   actually close the "non-perturbative" version.

### 5.5 Index entry (for the coordinator; this memo does not edit the index)

"Phase 204 part E audited (AUDIT_204_TRACT_E_001): of 39 K, K26 leaves (not REF-D; Sylvester fails, 2pn = ∞); 38 remain →
0 YES / 20 TRANSFER / 18 NO. K10 and K11 → TRANSFER (Lemma E.1 ∈ 𝒦_H; input empty by lem:monoT). K12 (Ω_{t₀}) → TRANSFER:
Lemma E.2 ⟺ (E_γ) (N_013); concavity gives no input at t = 1; "strictly weaker" is OPEN, not PROVED. K7b, K9 and K36: NO →
TRANSFER (closures only of candidates or variants). 43 distinct reformulations in README + 04_ + 06_; 03_ uses "CIRCULAR"
(28 lines, all in K except Nyman–Beurling, no D-only form). G14 of TRACT_D falls with K10/K11 (𝒦_W). Row D: OPEN."
