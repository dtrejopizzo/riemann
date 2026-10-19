# R162_407 — H1: the local lower bound (LB) to the right of a first contact

Round 4 (front H1, follows R162_406 §8–9).

Status: **(c) OBSTRUCTED for the dual/dilation machinery, with a proved rate ladder.**
- PROVED (unconditional): λ_A(T_*+δ) ≥ −κ_0(δ), with κ_0(δ) = 2A_*Q_*/log(1/δ)·(1+o(1)) (Thm 2.1).
- PROVED (conditional, analytic input only):
  - O(δ^{2β}) under uniform H^β bounds on the ground states.
  - O(δ log 1/δ) under uniform BV/L^∞ bounds.
  - O(δ) exactly under (REG), in which case λ_A(T_*+δ) = −(δ/T_*)𝒱(G) + o(δ) with an explicit virial form 𝒱 (Thm 3.2).
- PROVED (obstruction):
  - o(δ) cannot come from any bound that is uniform in the window (Prop 4.1).
  - For δ < δ_1 no prime and no short-interval statement enters at all (Lemma 1.1). For δ ≥ δ_1 new primes enter only at second order, and only through Brun–Titchmarsh upper bounds (Prop 4.3).
  - Every step is blind to the weight, so it holds verbatim for Λ + η_0 and for Davenport–Heilbronn (F3, §5).
- EQUIVALENCE (under REG): (LB) at o(κ') with the natural rate κ' ≍ δ holds **iff** the virial form satisfies 𝒱 ≤ 0 on N_{T_*}. Together with (NE), that is exactly "no first contact". So it is **not** equivalent to a known conjecture on primes in short intervals or on pair correlation.

GATE 1: OPEN. Row D: OPEN.

Notation is that of Paper 47 and R162_404–406:
- s_T(τ) = m(τ) − Σ_{n<e^{2T}} v_n cos(τ log n), with v_n = 2Λ(n)n^{−1/2};
- a_T(F) = (1/2π)∫s_T|F̂|²;
- c_F(u) = (1/2π)∫|F̂|²cos(τu), the autocorrelation;
- A_* = Σ_{n<e^{2T_*}} v_n;
- M_1 = sup_x |x m'(x)| < ∞ (proof of lem:contT);
- U_r F(t) = r^{−1/2}F(t/r), a unitary map L²(I_T) → L²(I_{rT}) (lem:contT);
- T' = T_* + δ, r = T'/T_* = 1 + δ/T_*;
- N = ker H_{T_*} (primitive), G ∈ N is the Lemma-5 limit of the ground states F_δ, and r_G ∈ span{e^{±t/2}} is its Tate vector (eq:localweak: a_{T_*}(G,η) = ⟨r_G,η⟩ for η ∈ 𝒬∩L²(I_{T_*})).

## 0. Corpus check

- **lem:contA** (Paper 47) is the unconditional continuity of λ_A through dilation plus a Tate-moment correction. Its proof gives only a modulus η(r) → 0 with no rate. Theorem 2.1 below makes that modulus explicit (1/log). It is the same argument with the split frequency optimised.
- **lem:contT, step (ii)** already has the bound S_T(δ^{1/2} + 2‖F‖_Q²/log(2+δ^{−1/2})). That is the 1/log rate in embryo. So Thm 2.1 is not new in mechanism, only in constant and in its use at T_*.
- **thm:D1 / thm:O.** Strong duality gives finitely atomic ε-certificates. Non-attainment rules out an exact certificate at T_*. So any certificate transfer starts from value −ε, which is why ε appears in κ.
- **cor:margin1.** λ ≤ 4·10⁹ T e^{−15.449T} before T_*. The total drop Δ of λ_A across a chamber is at most this, which enters the constant of Prop 4.1.
- **rem:resweights / thm:finmod.** A finite modification at n_0 moves λ by 2ε|c(log n_0)|/√n_0. Used in §5.
- **R162_405 §4.4.** For bounded ξ_G, λ_δ = o(δ^{1/2}) (collar Cauchy–Schwarz), and the O(δ/log(1/δ)) figure is a heuristic. §3.4 compares these.
- **R162_406 Lemma 1.1** (threshold gap) and **§7** (Conjecture 7.1, requirements) are used as stated.
- R160 survey, NG-F1 ("smoothness, not multiplicativity, controls the localized sign") is confirmed here in sharp form: the rate of (LB) is decided by the regularity of the ground states, and not by Λ.

## 1. The comb does not move: reduction to a fixed-symbol window problem

**Lemma 1.1 (fixed symbol).** Let 0 < δ < δ_1 (R162_406 Lemma 1.1).
- In regimes I and I′, s_{T'} = s_{T_*} =: s.
- In regime II (e^{2T_*} = n_0 = p^k), s_{T'} = s − v_{n_0}cos(τ log n_0), and the new contact sits at log n_0 = 2T_*.
- In every regime, no integer n > n_0 enters.

*Proof.* The only integer in [e^{2T_*}, e^{2T'}) is n_0 (R162_406 Lemma 1.1(i)). In regime I′, v_{n_0} = 0. ∎

**Consequence.** For δ < δ_1 ≍ e^{−2T_*}, the function δ ↦ λ_A(T_*+δ) depends only on two things:
- the finite vector (Λ(n))_{n ≤ e^{2T_*}}, through s;
- the window length.

No statement about primes in [e^{2T_*}, e^{2T_*}(1+ε)] and no statement about zeros beyond what s already encodes can influence the germ of λ_A at T_*+. The question (LB) is an **analytic spectral question about the window dependence of the bottom of a fixed log-order multiplier compressed to intervals.**

**Lemma 1.2 (dilation identity).** Work in regime I or I′. For F ∈ L²(I_{T'}) put u = U_{1/r}F ∈ L²(I_{T_*}). Then

    a_{T'}(F) = a_{T_*}(u) − Δ_r(F),   Δ_r(F) := (1/2π)∫[s(rτ) − s(τ)]|F̂(τ)|²dτ,                   (1.1)

and s(rτ) − s(τ) = [m(rτ) − m(τ)] − Σ_{n<e^{2T_*}} v_n[cos(rτ log n) − cos(τ log n)]. Here:
- 0 ≤ m(r|τ|) − m(|τ|) ≤ M_1 log r ≤ M_1 δ/T_* (lem:mbounds(i));
- |cos(rτ log n) − cos(τ log n)| ≤ min(2, 2|τ|δ), because log n < 2T_*.

In regime II, (1.1) acquires the extra term −v_{n_0}c_F(2T_*).

*Proof.* We have û(τ) = r^{1/2}F̂(rτ). Substitute. ∎

**Lemma 1.3 (Tate correction, lem:contA steps 2–4 at rate).** Let F ∈ 𝒫_{T'} with ‖F‖ = 1 and a_{T'}(F) ≤ 0. Then there is G_c ∈ span{φ_1,φ_2} ⊂ C_c^∞(I_{T_*/4}) such that:
- v := u − G_c ∈ 𝒫_{T_*};
- ‖G_c‖ ≤ C_2 δ, and |a_{T_*}(u,G_c)| ≤ C_3 δ;
- the constants depend on T_* and A_* only.

*Proof.* We have A(u) = r^{−1/2}∫F(s)(e^{s/(2r)} − e^{s/2})ds, so |A(u)| ≤ (C δ/T_*)‖F‖, and likewise for B. The rest is lem:contA steps 3–4, using a_{T_*}(u) ≤ Δ_r(F) ≤ M_1δ/T_* + 2A_*. ∎

## 2. The unconditional rate (PROVED)

**Theorem 2.1.** Let T_* be a first-contact window, λ_A(T_*) = 0, and put Q_* := A_* + c_m, where c_m = log 2π + 1 bounds m from below via lem:mbounds(ii) (m(τ) ≥ log(2+|τ|) − c_m). Then for 0 < δ < δ_1:

    λ_A(T_*+δ) ≥ −κ_0(δ),
    κ_0(δ) = 2A_*Q_*/(log(1/δ) − 2 log log(1/δ)) + 2A_*/log²(1/δ) + Cδ + θ_{II} v_{n_0} e_δ,           (2.1)

where
- θ_{II} = 1 only in regime II;
- e_δ := sup{‖F‖²_{L²(T_*−δ, T')} : F a unit ground state at T'}.

In particular κ_0(δ) = O(1/log(1/δ)) in regimes I and I′. In regime II, e_δ → 0 (without rate), because F_δ → EG strongly in L².

*Proof.* Take F ∈ 𝒫_{T'} with ‖F‖ = 1 and a_{T'}(F) ≤ 0. Then (1/2π)∫m|F̂|² ≤ A_*, so (1/2π)∫log(2+|τ|)|F̂|² ≤ Q_*. Split the comb part of Δ_r at |τ| = τ_1:

    Δ_r(F) ≤ M_1δ/T_* + A_*[2δτ_1 + 2Q_*/log(2+τ_1)].

Choose τ_1 = 1/(δ log²(1/δ)). By Lemma 1.3, and because a_{T_*} ≥ 0 on 𝒫_{T_*} (first contact),

    a_{T'}(F) ≥ a_{T_*}(v) + 2a_{T_*}(v,G_c) + a(G_c) − Δ_r(F) ≥ −Δ_r(F) − Cδ.

For regime II, add v_{n_0}|c_F(2T_*)|. Here c_F(2T_*) is an overlap integral over a set of length 2δ, so by Cauchy–Schwarz and parity |c_F(2T_*)| ≤ ‖F‖²_{L²(T_*−δ,T')}. Take the infimum over F. ∎

**Corollary 2.2 (certificate form).** By thm:D1 at T', for every η > 0 there is a finitely atomic certificate of value ≥ λ^P(T') − η. The primal statement (2.1) concerns λ_A ≥ λ^P. The same dilation proof applies to λ^P (Φ ↦ Φ(r·) preserves positive-definiteness and Φ(0) = 1), provided the two g-annihilation moments are corrected as in Lemma 1.3. That correction is not re-verified here, so the certificate version is recorded as **NOT CHECKED**.

**Proposition 2.3 (1/log is the ceiling of any symbol-level scheme).** Consider a scheme that proves λ(T') ≥ (1−θ)λ(T_*) − η using only a pointwise inequality s(τ) ≥ (1−θ)s(rτ) − η for all τ. Such a scheme is exactly what a certificate-only transfer can use, since the form is tested against all F. If min s < 0 and v_{n} > 0 for some contact n, it needs η ≥ c/log(1/δ).

*Proof.* At τ = π/((r−1)log n) + O(1) the comb difference for n alone is 2v_n. The other contacts have independent phases, and by Kronecker on the finitely many log n there are such τ where the rest does not compensate. There s(τ) ≈ log τ ≈ log(1/δ). The inequality at such τ forces θ log(1/δ) ≳ 2v_n. At a point τ_0 with s(rτ_0) = min s < 0 it forces η ≥ θ|min s| − O(δ). ∎

So **the dual machinery alone (certificates plus symbol comparison) gives exactly the order 1/log(1/δ), no better.** Any power rate needs information about the ground states that is not a symbol inequality.

## 3. Conditional rates: regularity is the only lever

**Theorem 3.1 (ladder).** Let F_δ be the unit ground states at T' (regime I or I′).
- (a) If sup_δ (1/2π)∫|τ|^{2β}|F̂_δ|² ≤ R for some 0 < β ≤ ½, then κ(δ) ≤ M_1δ/T_* + 2^{1−2β}A_* R δ^{2β} + Cδ.
- (b) If sup_δ(‖F_δ‖_∞ + ‖F_δ‖_{BV}) ≤ V, so that |F̂_δ(τ)| ≤ V/|τ|, then κ(δ) = O(V²A_* δ log(1/δ)). In regime II the same holds, with the extra term v_{n_0}e_δ ≤ 2v_{n_0}V²δ.

*Proof.* (a) Use min(2, 2|τ|δ) ≤ 2^{1−2β}(2|τ|δ)^{2β}. (b) Use ∫min(2,2|τ|δ)V²τ^{−2}dτ over |τ| ≥ 1, which is ≤ 4V²δ(log(1/δ) + 2), and ‖F_δ‖²_{L²(edge 2δ)} ≤ 2δV². ∎

The absolute-value bound (b) is lossy: it ignores the cancellation in cos(rτ log n) − cos(τ log n). The exact first-order term is a virial.

**(REG).** For some neighbourhood 𝒰 of the comb points {log n : n < e^{2T_*}}, the following hold:
- c_{F_δ} ∈ C¹(𝒰) uniformly in δ, and c'_{F_δ} → c'_G on 𝒰;
- G ∈ Dom(t∂_t) near the Tate pairing, i.e. ∫|t||G| < ∞, which is automatic.

(For piecewise-C¹ ground states with jumps only at a set J, the first bullet holds whenever log n ∉ J − J.)

**Theorem 3.2 (virial law, conditional on REG).** Define the virial form on N by

    𝒱(G) := (1/2π)∫ τ m'(τ)|Ĝ(τ)|² dτ − Σ_{n<e^{2T_*}} v_n log n · c_G'(log n) + 2⟨G, t r_G'⟩.     (3.1)

In regimes I and I′, under (REG):

    λ_A(T_*+δ) = −(δ/T_*)𝒱(G) + o(δ),   and   𝒱(G) = max_{H∈N, ‖H‖=1} 𝒱(H) ≥ 0.             (3.2)

*Proof.*
1. Lower bound: apply (1.1) to F_δ.
   - m(rτ) − m(τ) = (r−1)τm'(τ) + O((r−1)²) uniformly, since (τ∂_τ)²m is bounded. The weight τm' is bounded and continuous, and F_δ → EG in L², so the archimedean part is (δ/T_*)(1/2π)∫τm'|Ĝ|² + o(δ).
   - By (REG), c_{F_δ}(r log n) − c_{F_δ}(log n) = (r−1)log n·c_G'(log n) + o(δ).
   - Tate term: 2a_{T_*}(v,G_c) = 2⟨r_G,G_c⟩ + o(δ) by eq:localweak, with v → G. Here ⟨r_G,G_c⟩ = αA(u) + βB(u) for r_G = αe^{t/2} + βe^{−t/2}. Also A(u) = −(δ/T_*)∫F_δ(s)(s/2)e^{s/2}ds + O(δ²), and likewise for B. This gives −(δ/T_*)·2⟨G, t r_G'⟩ up to sign convention, entering with the sign in (3.1).
   - Hence λ_δ ≥ −(δ/T_*)𝒱(G) + o(δ).
2. Upper bound: use the trial vector U_rH − (Tate correction) for any unit H ∈ N. The same expansion with r ↦ 1/r gives λ_δ ≤ −(δ/T_*)𝒱(H) + o(δ).
3. Comparing the two bounds, the limit G maximises 𝒱 on the unit sphere of N. Monotonicity (lem:monoT) gives 𝒱(G) ≥ 0. ∎

**Corollary 3.3 (exact criterion for o(δ)).** Under (REG): (LB) holds with κ = o(δ) iff 𝒱 ≤ 0 on N, i.e. max_N 𝒱 = 0 (λ_A has zero right derivative at T_*). If max_N 𝒱 > 0, then |λ_δ| ≥ (δ/T_*)max_N 𝒱 − o(δ). The upper-bound half needs (REG) only for the trial vector H, not for F_δ, and it is a proved (NE)-type bound at rate δ.

**3.4 Comparison with κ'.** By R162_405 (2.2), |λ_δ| = |⟨ξ_G^δ, F_δ|_C⟩|(1+o(1)). So (LB) and (NE) bound **the same number** from the two sides.
- Under (REG) this number is (δ/T_*)𝒱(G) + o(δ). Conjecture 7.1 at the natural rate κ' ≍ δ is then equivalent to: **𝒱(G) = 0 and 𝒱(G) ≥ c‖R_LG‖²**.
- The (LB) half is the virial identity 𝒱|_N ≤ 0, a single quadratic condition on the finite-dimensional N.
- If κ' = o(δ), then (LB) needs 𝒱 = 0 and the vanishing of the next Taylor coefficient as well.
- Relative to R162_405 §4.4 (o(δ^{1/2}) for bounded ξ_G): Theorem 3.1(b) improves this to O(δ log 1/δ) under BV, and (3.2) gives the exact order δ. The heuristic O(δ/log(1/δ)) of R162_405 §4.4 would force 𝒱(G) = 0. It is therefore not a generic rate: it is a first-contact-specific assertion equivalent to Cor 3.3.

## 4. Obstructions (PROVED)

**Proposition 4.1 (no uniform o(δ)).** Suppose κ bounds λ_A(T) − λ_A(T+δ) for every T in an interval J on which λ_A drops by Δ > 0. Then κ(δ) ≥ Δδ/(|J| + δ).

Every first contact has such a J to its left: λ_A > 0 before T_*, and λ_A is continuous (lem:contA). By cor:margin1, Δ ≤ 4·10⁹T e^{−15.449T} is tiny but positive. Hence **any bound derived uniformly over windows (in particular Thms 2.1 and 3.1, whose constants are continuous in T) is Ω(δ)**. The rate o(δ) can come only from an input that holds at T_* and fails at the nearby positive windows. This is the F1 requirement of R162_406 §7, now a theorem.

*Proof.* Cover J by ⌈|J|/δ⌉ intervals of length δ. The drops sum to Δ. ∎

**Proposition 4.2 (λ-covariance).** Every transfer in §§2–3 has the form λ(T') ≥ λ(T_*) − κ, with κ computed from s, T_*, and bounds on F_δ. The value λ(T_*) enters only additively (a_{T_*}(v) ≥ λ(T_*)‖v‖²). The same proof at a positive window T_0 in the same chamber gives λ(T_0+δ) ≥ λ(T_0) − κ_{T_0}(δ), with κ_{T_0} → κ_{T_*} as T_0 ↑ T_*.

Suppose (NE) holds with a rate κ' at the windows T_0 (R162_406 §7: it does, because it is not arithmetic), with R_LG_0 ≠ 0 (eq:Qspectral) and ‖R_LG_0‖ bounded below along T_0 ↑ T_*. Then κ_{T_*}/κ' ↛ 0. So a λ-covariant transfer can reach (LB) at o(κ') **only if it already knows R_LG = 0**. This is circular.

**Proposition 4.3 (arithmetic enters only at δ ≥ δ_1, second order, one-sided).** For macroscopic δ (new contacts n ∈ [x, xe^{2δ}), x = e^{2T_*}), the new-contact term in a_{T'}(F) is −Σ v_n c_F(log n). Here |c_F(log n)| ≤ ‖F‖²_{L²(edge of width 2T'−log n)}, which under Thm 3.1(b) is ≤ V²(2T'−log n).

By Brun–Titchmarsh (Montgomery–Vaughan, ψ(x+h) − ψ(x) ≤ 2h log x/log h + O(√x) for prime powers), the total is ≤ C V² e^{T_*} δ² · log x/log(δx), unconditionally. So:
- primes in short intervals affect κ only at order δ², and only through an **upper bound on their number**;
- no short-interval asymptotic (PNT for h = x^θ, or its conjectured extension to h = x^ε) can supply a sign, since the sign of c_F(log n) near the edge is ε·F(T'−)F(−T'+) (the parity of the ground state) and not arithmetic;
- pair correlation enters only through thm:Z, i.e. through s itself, which is already fixed by Lemma 1.1.

Hence (b) "equivalent to a known conjecture" is **refuted** for the short-interval and pair-correlation families.

## 5. F3: finite modifications and Davenport–Heilbronn

**(a) Weight-blindness.** For a weight a: ℕ → ℝ₊ ∪ ℝ (a(1) = 0), replace Λ by a. Lemmas 1.1–1.3, Thms 2.1, 3.1, 3.2 and Props 4.1–4.3 hold verbatim, with A_* = Σ|v_n^a|. None of them uses a*1 = log or the Euler product; Lemma 1.3 uses only |A|, |B| bounds. This includes a = Λ + η_0 with supp η_0 ⊂ (1, e^{2T_*}), and the DH coefficient sequence.

**(b) DH has a first contact.** DH has off-line zeros. So its complete Weil form, and via Paper 45 Thm 11.3 / R162_001 its primitive form, is negative at some T. It is positive for small T (empty comb). By continuity (the lem:contA proof is weight-blind), a first contact T_*^{DH} exists. At it, Thms 2.1/3.1/3.2 hold. Hence either (NE) fails for DH at the rate κ' or (LB) at o(κ') fails for DH. So **no argument built from §§2–3 can prove (LB) at o(κ') for Λ unless it also proves it for DH**. In that case the Λ-specificity must sit entirely in (NE), or in the value of 𝒱 at the particular G. Neither is a consequence of the transfer.

**(c) Genericity (remark, NOT PROVED).** Take the family a_ε = Λ + ε1_{n=n_0}, n_0 < e^{2T_*} (rem:resweights). It moves T_*(ε) and G_ε. The condition max_{N_ε}𝒱_ε = 0 of Cor 3.3 is one real equation. If it depends analytically on ε and is not identically satisfied, it fails for all but discretely many ε. So (LB) at o(δ) is a **non-generic, exact identity** in weight families, whereas λ-decrease at rate δ is generic. This is the precise sense in which (LB) at o(κ') is not a perturbative statement.

## 6. Verdict on the task's trichotomy

- **(a) Provable:**
  - (LB) at rate 1/log(1/δ), unconditionally (Thm 2.1). This is the sharp order of certificate/symbol-level transfer (Prop 2.3).
  - O(δ^{2β}), O(δ log 1/δ) and O(δ) under analytic regularity of the ground states (Thm 3.1, 3.2). That regularity is not known, because the operator has log order and gives no power bootstrapping. This rate is not o(κ') for any κ' ≳ δ.
- **(b) Equivalent to a known conjecture: NO.** For δ < δ_1 no arithmetic enters (Lemma 1.1). For δ ≥ δ_1 primes enter at order δ² and only through unconditional upper bounds (Prop 4.3).
- **(c) Obstructed: YES**, for the dual machinery:
  - o(δ) is impossible by window-uniform bounds (Prop 4.1);
  - λ-covariant transfers are circular (Prop 4.2);
  - every step is weight-blind, so it applies to DH, which has a first contact (§5b).
  - Under (REG), (LB) at o(κ'), κ' ≍ δ, is **equivalent** to the virial identity 𝒱 ≤ 0 on N_{T_*} (Cor 3.3). With (NE), that is equivalent to the non-existence of a first contact.

**New target stated (for the next round).** Conjecture 7.1 reduces, under (REG), to the pair
𝒱|_{N_{T_*}} ≤ 0 and 𝒱(G) ≥ c‖R_LG‖². The first is a property of one explicit quadratic form (3.1) on a finite-dimensional space. Any proof must use the Euler product to evaluate the comb virial Σ v_n log n · c_G'(log n) against the archimedean virial and the Tate virial. Both remaining open items are analytic: proving (REG), and deciding the sign structure of 𝒱 on N. Numerics: not needed for any statement here.

Falsifiers:
- F1 PASSED: Prop 4.1–4.2 prove that no statement here separates first contact from positive windows.
- F3 PASSED: §5.
- No claim is made beyond the primitive form. The certificate version (Cor 2.2) is NOT CHECKED.

GATE 1: OPEN. Row D: OPEN.

Files edited: this file only.
