# BARRIER_EST_001 — the estimates component: lem:shape-est(iv) upgraded from ARGUED to PROVED for a declared class

Phase 197. Memo (logic + analysis), not yet reviewed. Supplies only the *estimates*
component of the unified barrier meta-theorem (BARRIER_001_*, a parallel memo); it does not restate the other parts.
the result is a closure *of a method class*,
not of the target.

## 0. Corpus / index check
- Source: SURVEY_MODERN_UNTRIED §B4 (proof mining / reverse mathematics, "6 as meta, 0 as sign").
  Not in the index as a tried route. New reason vs. the registered material: Paper 46 lem:shape-est(iii) and
  prop:wit-sens perturb by **scaling** (1+δ)Λ or by the integer weights, so they need κ_T ≠ 0 (CONDITIONAL). Here the
  perturbation is an **added atom at a point u ∈ (0,2T) of our choosing**, inside the comb class of def:comb (positive
  Borel measures). The first-order effect is Re c_F(u) → ‖F‖² = 1 as u → 0⁺, so no nonvanishing hypothesis is needed.
- Paper 46 objects used with their own definitions: def:comb (𝔞^ν_T(F) = m_T(F) − ∫_{(0,2T)} Re c_F dν, bottom b_T(ν)),
  subsec:shape-est (estimate (E_T,R_T), 𝓕^{(a)}_T, μ_T, "decides by the estimate"), def:shape-class, cor:margin1.
- Proof mining (Kohlenbach's monotone functional interpretation) turns out **not needed**: the metatheorem used is
  the elementary soundness + constants lemma, valid for any classical theory (RCA₀ … ZFC). No reverse-mathematics
  strength claim is made. This is recorded so that B4 is not reopened as "proof mining of the estimate class".

## 1. The class 𝓔 (precise definition)
Fix a background theory 𝕋 (any classical first-order theory, sound for the intended reals/measures: e.g. WKL₀ or
ACA₀ with analytic primitives, Kohlenbach's 𝒜^ω, or ZFC). Extend its language by one constant symbol **ν** (the comb)
of sort "positive Borel measure on (0,∞), finite on bounded sets" (def:comb).

**Definition 1 (estimate-based proof at T, radius r).** A proof P of WP_T(ν) :≡ b_T(ν) ≥ 0 is *𝓔(T,r)-based*
(r = r(T) > 0) if every axiom of P that mentions ν belongs to a set Prem(ν) of premises such that
 (E1) [TV-robustness] Prem is satisfied by every positive comb ν′ with ‖(ν′ − ν_Λ)|_{(0,2T)}‖_TV ≤ r and
      ν′ = ν_Λ off (0,2T)  — i.e. the premises, *as true statements about ν_Λ*, hold with additive slack ≥ r in TV;
 (E2) no other axiom mentions ν (comb-independent axioms of 𝕋 are unrestricted).
A proof of ∀T WP_T is *𝓔(r(·))-based* if for each T its comb premises at window T satisfy (E1) with radius r(T).

Canonical instances. (a) An estimate (E_T,R_T) of subsec:shape-est with slack s_T := R_T − sup_F|𝓕_T(F) − E_T(F)|:
since |𝓕^{(ν′)}_T(F) − 𝓕^{(ν)}_T(F)| ≤ ‖ν′−ν‖_TV for unit F (|c_F| ≤ ‖F‖²), it satisfies (E1) with r = s_T.
(b) A Chebyshev-type premise |ψ(x) − x| ≤ R(x) on [1,e^{2T}) with slack s(x): (E1) with r = inf_x s(x)·e^{−T}·2
(the ψ-mass of an atom of v-weight m at u is m e^{u/2}/2 ≤ m e^{T}/2). (c) Any finite list of premises X_j(ν) ∈ [α_j,β_j]
with X_j L_j-Lipschitz in TV and slacks s_j: r = min_j s_j/L_j.
Relative-precision form (task's wording): premises with relative slack ≥ e^{−cT} against the comb mass
A_T = (4+o(1))e^T (prop:env(iii)), resp. absolute slack ≥ C e^{−cT} or ≥ C T^{−k}.

*Excluded from 𝓔 by definition* (zero slack): exact identities ("ν is supported on log ℕ", "Σ_{d|N}Λ(d) = log N",
Euler product, explicit formula as an identity). These are the exact-identity class, handled by thm:shape (B″) and the
other barrier components, not here.

## 2. Metatheorem (PROVED)
**Lemma 2 (constants lemma; standard, CITED: Shoenfield §4.5).** If 𝕋 + Prem(ν) ⊢ WP_T(ν) with ν a new constant, then
𝕋 ⊢ ∀ν′ (Prem(ν′) → WP_T(ν′)). With soundness of 𝕋: every comb ν′ satisfying Prem has b_T(ν′) ≥ 0.

**Lemma 3 (atom perturbation; PROVED).** Let T > 0 and η > 0. There are a unit F ∈ P_T ∩ 𝒟_T and u ∈ (0,2T) with
𝔞_T(F) < λ_A(T) + η and Re c_F(u) ≥ 1 − η. For m > 0 put ν′ := ν_Λ + m δ_u. Then
  b_T(ν′) ≤ 𝔞^{ν′}_T(F) = 𝔞_T(F) − m Re c_F(u) < λ_A(T) + η − m(1−η).
*Proof.* F exists by definition of the bottom (λ_A = b_T(ν_Λ), def:comb). c_F(u) = ∫F(x+u)F̄(x)dx is continuous in u
with c_F(0) = ‖F‖² = 1 (continuity of translation in L²), so some u ∈ (0, min(2T,·)) has Re c_F(u) ≥ 1−η. The form
identity is def:comb, linear in ν. ∎
**Corollary.** For every m > λ_A(T) (take η small) the comb ν′ = ν_Λ + mδ_u is positive, differs from ν_Λ only on
(0,2T), has ‖ν′−ν_Λ‖_TV = m, and b_T(ν′) < 0. (If λ_A(T) < 0 this is trivial; we assume positivity, λ_A ≥ 0.)

**Theorem 4 (no estimate-based proof below the margin; PROVED).** If a proof of WP_T(ν_Λ) is 𝓔(T,r)-based, then
  r ≤ λ_A(T),  and for T ≥ 1:  r ≤ 4·10⁹ T e^{−15.449 T}  (cor:margin1).
*Proof.* If r > λ_A(T), pick m ∈ (λ_A(T), r]. ν′ of the Corollary satisfies Prem by (E1), so b_T(ν′) ≥ 0 by Lemma 2,
contradicting the Corollary. ∎
**Corollary 5 (all windows).** No 𝓔(r(·))-based proof of ∀T WP_T exists when, for some T ≥ 1,
r(T) > 4·10⁹Te^{−15.449T}. In particular none exists if r(T) ≥ C e^{−cT} with c < 15.449 (fails at every
T > T₀ with (15.449−c)T − log T > log(4·10⁹/C)), if r(T) ≥ C T^{−k}, or if the relative slack against A_T is
≥ e^{−cT} with c < 16.449 (since A_T e^{−cT} ≥ 3.9 e^{(1−c)T} for T ≥ 1 by A_T ≥ … — the constant is taken from
prop:env(iii); the o(1) makes this ARGUED-to-constant, the exponent statement is PROVED for T large).
**Required precision (exact statement).** A successful estimate-based proof must, at every window T, carry all its
comb premises with TV-slack ≤ λ_A(T); for T ≥ 1 this is ≤ 4·10⁹Te^{−15.449T} (relative to the comb mass:
≤ ~10⁹ T e^{−16.449T}). Combined with lem:shape-est(i): main term and remainder then agree to the same precision, so
"remainder" and "true error" coincide to within λ_A(T). Any improvement of the proved upper bound on λ_A (e.g. the
conjectural exp(−e^{(2−ε)T}) of rem:shape-est(a), NOT used) sharpens the requirement automatically.

## 3. Integer-supported variant 𝓔^ℕ (comb variable ranges over weight vectors on 𝒩_T only)
If the language forces supp ν ⊆ log ℕ (premises stated on a: ℕ → ℝ), the atom at u→0 is unavailable.
**Proposition 6 (PROVED, qualitative).** For 2T > log 2 and every η > 0, κ̂_T(η) := sup{Σ_n v_n|Re c_F(log n)| :
‖F‖=1, F ∈ P_T∩𝒟_T, 𝔞_T(F) < λ_A+η} > 0, and every 𝓔^ℕ-based proof (ℓ¹(v)-slack r) has r ≤ (λ_A+η)/κ̂_T(η).
*Proof.* Perturb a_n ↦ a_n + ε·sgn Re c_F(log n) (prop:wit-sens computation). κ̂ > 0: the near-minimizer set is open
in the form domain; F ↦ Re c_F(log 2) is a continuous quadratic form; if it vanished on an open set it would vanish
identically on P_T (polynomial in t along F+tG), but the shift-by-log 2 form has infinite rank on L²(−T,T) for
2T > log 2 while P_T has finite codimension, so its restriction is nonzero. ∎
**OPEN / CONDITIONAL:** a lower bound κ̂_T ≥ k₀(T) (numerically κ_{log 2} ≈ 0.09, rem:wit-sens, not certified). With
such a bound Theorem 4 holds for 𝓔^ℕ with r ≤ λ_A/k₀. Without it the 𝓔^ℕ statement is qualitative.
Note: Paper 46's own estimate notion (subsec:shape-est) takes the comb in def:comb (measures), so instance (a) falls
under the PROVED Theorem 4, not under §3.

## 4. Effect on lem:shape-est and thm:shape (B′)
- lem:shape-est(iv): **PROVED** for the class 𝓔 (Def. 1) — i.e. for every estimate (E_T,R_T) in the paper's own sense
  whose slack exceeds λ_A(T), and for every proof whose comb premises are TV-robust beyond λ_A(T). Replaces the
  κ_T ≠ 0 hypothesis of (iii) for the measure class. Remaining ARGUED part: that the classical estimates
  (PNT with Vinogradov–Korobov remainder, sieve, large sieve, BV) *are* used with slack ≥ e^{−cT}, c < 15.449. This is
  a reading of how they are proved (they hold for classes of sequences open in TV/Kolmogorov distance at scale
  ≥ the stated remainder) — ARGUED per estimate, PROVED for any estimate whose stated proof is uniform over a TV-ball.
- Proposed text for Paper 46: add "Theorem (estimate class; proved)" after lem:shape-est with Def. 1, Lemma 3, Thm 4;
  relabel (B′) "proved for 𝓔; the reading for named classical estimates argued". Editor must verify against def:comb
  and subsec:shape-est (rule ). Not integrated by this memo.

## 5. CIRC kills (AUDIT_PHASE193_CERTAINTY) that become non-circular
Upgraded (the (B′) leg is now PROVED for 𝓔, provided the seed's sign step is a premise robust in TV beyond λ_A):
- #2 P191 "T* cannot be an estimate" — non-circular for 𝓔 (measure combs); for integer-only premises qualitative (§3).
- #15 E8 Golden–Thompson/Gibbs — (B′) half non-circular (equality half was already THM).
- #16 E9 Kadison–Singer/MSS/Lee–Yang — (B′) leg non-circular (retry strength unchanged).
- #25 F7 Selberg/horocycle equidistribution — non-circular (equidistribution inputs are TV/discrepancy estimates).
- #26 C_006 Helson H²(𝔻^∞) — (B′) half non-circular; RD half unchanged.
- #23 M5 singular series — (B′) leg now PROVED (was already PROVED in decisive class via CA_M_001).
- #14 C_001 tolerance cells (O4^ε, O5): non-circular **iff** the cell's tolerance is stated on the comb measure
  (then the atom falsifier replaces O4^ε without κ_T); if stated on integer weights only, stays CONDITIONAL (§3).
NOT affected: #1 SPEC_A (rests on the unproved doubly exponential scale), O10/O11/O12/G1/H0(b) kills (#7–#13).
Audit table row "(B′)" should read: "(iv) PROVED for 𝓔 (BARRIER_EST_001 Thm 4); reading for named estimates ARGUED".

## 6. Labels
Lemma 2 CITED · Lemma 3, Thm 4, Cor 5 (exponent form) PROVED · Prop 6 PROVED (qualitative) · quantitative κ̂ bound OPEN ·
relative-slack constant ARGUED (o(1) in A_T) · "classical estimates are in 𝓔" ARGUED · no sign for row D (method-class NO-GO).
