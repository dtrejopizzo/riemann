# PROOF_L_SHARP_HH_001 — Möbius-kink tails as the rough correction: exact decomposition, scale test, verdict (pen and paper; NUMÉRICO only from stored data)

Phase 199, inventor-prover. , no zero
datum is used,
Notation: AA_001 (D.1)–(D.2), FF_001, EXTERIOR_DATUM_001, MORI15_EXTREMAL_001. μ = 15, λ = √15, h(v) = v^{-1/2}g(log v), H = h·1_{[1/λ,λ)}.

## 0. Index check / reason this is not a retry
Indexed: EXTERIOR Cor C′.2 (1/ω jump-line model, q-grouped form, ARGUED/HEURISTIC), AA_001 D(iii) NO-GO (|M̃| ≤ 1, PD kernel),
AUDIT_13 Constraint 25, AUDIT_12 (24c) (profile kink-dominated, not 1/ω), FF_001/GG_001 (translate comb, cancels). New element
claimed by the idea: split r = r_smooth + Σμ(m)K_m with K_m at leakage scale, so that no 33-digit cancellation is needed. This memo
tests exactly that claim (whether the split avoids Constraint 25); it is a test, not a reformulation of C′.2.

## 1. The exact decomposition (PROVED) — and why it is gauge-dependent
**Lemma HH.1 (PROVED).** Let h_e be any extension of h|_{[1/λ,λ]} to [1/λ,∞) (C^k or C^∞). Put
 F_s(u) := Σ_{1≤m<μ} μ(m) h_e(m|u|)·1_{m|u|≥1/λ} + φ₀(u),  k_e(v) := h_e(v)·1_{v≥λ}.
Then f = F_s − Σ_{m<μ} μ(m) k_e(m|·|), and for ω > λ
 r(ω) = r_s(ω) + Σ_{1≤m<μ} μ(m) K_m(ω),  r_s := F̂_s|_{(λ,∞)},  K_m(ω) := −m^{-1}·k̂_e(ω/m).        (HH.1)
*Proof.* H(v) = h_e(v)1_{v≥1/λ} − k_e(v); insert in (D.1), take transforms (F[φ(m·)] = m^{-1}φ̂(·/m)). □
F_s is as smooth as h_e on (1/λ,∞) (the interior jet jumps at u = λ/m are removed: D.2 is exactly the jet of k_e(m·) at u = λ/m);
the φ₀ gauge contributes only at |u| ≤ 1/λ (lower cut, the "K_0" line; AUDIT_13 C1: individually at 1/(mλ), in aggregate at 1/λ).
**The split is not canonical.** K_m depends on h_e beyond v = λ; only its asymptotic series is canonical:
 K_m(ω) ~ μ-free part −2Re Σ_k e^{−2πiλω/m}(−1)^k m^k h^{(k)}(λ)(2πiω)^{-k-1}  (the series above; D.2).

## 2. The scale test (NUMÉRICO from MORI15/EXTERIOR numbers) — the idea fails here
Data: g*(T) = −1.42·10⁻³⁴, g*(T−10⁻³) = −1.7·10⁻³³, g*(T−0.05) = −1.3·10⁻²³ (MORI15 l.65); p′(T)/p(T) = 5079 (EXTERIOR §2).
h(λ) = g(T)/√λ = −7.2·10⁻³⁵. d/dv log h at v = λ: (g′/g − ½)/λ = 1311 (p) / ≈ 640 (secant g*). Hence in line m the ratio of
consecutive asymptotic terms is m·1311/(2πω) = 209·m/ω, and the higher derivatives grow at least as fast (boundary layer of width
≈ 4·10⁻⁴ in log v; g rises 11 orders in 0.05).
**(a) The canonical (asymptotic) K_m is valid only for ω ≫ 209·m.** On the whole data window ω ∈ [1,48] the series diverges
for every m ≥ 1; the two-term "jump + kink" model is not an approximation there (this is AUDIT_12 (24c) made quantitative).
**(b) Every leakage-scale choice of h_e makes K_m negligible on [1,48].** If |h_e| ≲ |h(λ)| on [λ,∞), C^∞-matching the jet forces
h_e to turn over within Δv ≈ 1/1311 (else it grows like e^{1311Δv}); then |K_m| ≤ m^{-1}∫|k_e| ≈ |h(λ)|/1311 ≈ 5·10⁻³⁸, vs
rms Δr_out = 0.075–0.20·10⁻³⁵ (EXTERIOR §1). So Σμ(m)K_m is ≤ 3 % of Δr_out and cannot carry the (1,2) = −0.48 resonance.
**(c) Long extensions (h_e ≈ h(λ) slowly decaying, giving 1/ω lines of size h(λ)/(πω) ≈ 6·10⁻³⁶ at ω = 4) are exactly EXTERIOR's
naive jump model: corr(Δr_out, model) = −0.05** (EXTERIOR §2, AUDIT_12 §2). Falsified pointwise; its (1,2) = −0.31 is not a mechanism.
**(d) Where r_s lives.** In every gauge, r_s = Σ_m μ(m) m^{-1}F[h_e1_{≥1/λ}](ω/m) + φ̂₀ with ω/m < λ for m ≥ 2: the dilates m ≥ 2
are read **in band** (bulk O(10⁻³)), so r_s is itself a 33-digit Möbius cancellation. The split moves Constraint 25 from r into
r_s; it does not remove it. The only cancellation-free object is the whole r (equivalently the translate comb of FF.1, which also
cancels) — r_s is "the tail of a prolate-like part" only after the same cancellation.
**(e) What the kinks do reproduce.** The directional (1,n) coincidence with sign μ(n) and the ω-band localization c/m are
properties of *any* object built as Σμ(m)m^{-1}φ(·/m) (EXTERIOR Lemma E.1, PROVED there); they are not evidence for the jump
mechanism. The amplitude (≈½, window-dependent) and the ω ≥ 2 localization are not produced by K_m in any gauge of (b)–(c).
**Verdict (task (i)): the decomposition is PROVED but trivial and gauge-dependent; the claimed scale property ("each K_m is
O(h(λ)) with no cancellation, and Σμ K_m is Δr_out") is FALSE on the data window. The idea is dead as stated (NO-GO).**

## 3. The blocks (task (ii)) — formal, in the only regime where K_m is canonical
Restricting to ω ≫ 209m (where 𝒲_ext-contributions are O(|h(λ)|²/ω₀) ≲ 10⁻⁴ ℓ, ℓ ∈ [4.4,8.5]·10⁻⁷⁰):
- **kink–kink (PROVED as algebra, leading order):** with j = (h(λ), h′(λ)) and K_m(ω) ≈ μ(m)[h(λ)sin(2πλω/m)/(πω) +
  m h′(λ)cos(2πλω/m)/(2π²ω²)], the coherent pairs in Ψ̌ are (m@n, m′@n′) with n/m = n′/m′; grouping by q gives
  jᵀ 𝔎 j, 𝔎 = Σ_q [C_q²·𝔄_q − 2C_qD_q·𝔅_q], C_q, D_q the AA_001 (D.3)/(D.4) class sums and 𝔄_q, 𝔅_q explicit 2×2 moment
  matrices of the profiles (1/ω, m/ω²). This **is** EXTERIOR Cor C′.2 / AA_001 (D.5) with σ replaced by its two-term
  asymptotic profile: no new object. Its sign at μ = 15 is controlled by the integer class −2M̃(14)·D_b (M̃(14) = −89/15015,
  M̃(15) = +304/5005: sign flips with the cutoff) and by the classes a ≥ 2; AA_001 D(iii)(c) (a_P and cΛ transport, AUDIT_13 C5a/b)
  applies verbatim: no sign is carried by μ(m), v_n at this level. NO-GO (inherited).
- **smooth–kink:** the (1,n) prolate-line × K_n-dilated pairing lands at phase e^{−2πiωλ}; in the canonical regime it is
  O(|h(λ)|·|prolate tail|) at ω ≫ 209n, i.e. below 10⁻⁴ℓ. On [1,48] it is gauge-dependent (§2(b)/(c)). Not computable as a
  gauge-free block.
- **smooth–smooth:** Theorem C (Z_001/CC_001) covers only r_s's m = 1 Langer part; r_s's m ≥ 2 content is the in-band Möbius sum (§2(d)).

## 4. Sign (task (iii)) and honest statement (task (iv))
The proposed finite matrix "prolate block ⊕ edge-jet block ⊕ coupling" does not exist gauge-free on the scale where ℓ lives:
the edge-jet (2×2) block is canonical only where it is 10⁻⁴ℓ, and on [1,48] the jet is not a coordinate (series diverges; the
boundary layer of g at T has derivative scale 1311 ≫ 2πω). PROVED: Lemma HH.1 (exact split, any extension); scale facts
§2(a),(b) (elementary, from stored numbers). NUMÉRICO: magnitudes §2. NO-GO: "rough correction = Σμ(m)K_m without
cancellation" (fails (b)+(c)+(d)); edge-jet 2×2 Möbius form as a sign carrier (inherits AA D(iii)(c)). OPEN: L′♯.
**Constraint 26 (new).** The edge jet (g(T), g′(T), …) of an admissible extremal is not a usable coordinate below ω ≈ 209·m
(μ = 15): the window boundary layer (log-slope ≈ 10³) makes jump/kink expansions divergent on the data window; any
"kink-line" split of r is gauge-dependent there and either negligible (short extension) or the falsified 1/ω model (long).
No sign of row D claimed. L′♯ OPEN. Row D OPEN.
