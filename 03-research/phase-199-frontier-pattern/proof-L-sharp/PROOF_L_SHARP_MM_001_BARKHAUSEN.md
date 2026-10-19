# PROOF_L_SHARP_MM_001 — A Barkhausen / passivity criterion for the exterior feedback structure

Phase 199 memo (pen and paper; one NUMÉRICO check script on ζ-values only:
`PROOF_L_SHARP_MM_001_check.py`). Target: Lemma L′♯ (AUDIT_199) in the exterior form of PROOF_L_SHARP_A_001
Thm 1.1, W_T(g) = 𝒲_ext[Zr].

**Outcome in one line.** No sign. PROVED: (MM.1) each prime channel G_p(s) = (1−p^{−s})^{−1} is strictly positive-real on
Re s > 0 with Re G_p ≥ (1+p^{−σ})^{−1}; (MM.2) the closed loop on the *full line* is exactly **lossless**: the complete Weil
form vanishes identically on (full-line) Z-images, because the prime coupling (collapsed by Λ∗1 = log) cancels the
archimedean plant symbol exactly via ∂_σ|Γ_ℝ(s)ζ(s)|² = 0 on Re s = ½ — the loop sits exactly on the Barkhausen boundary;
(MM.3) the cascade Z = ∏_p G_p is not positive-real on Re s = ½ (Re ζ(½) < 0) nor on 1 < σ < σ₀ (CITED), and the plant
symbol Θ(t) = Re ψ(¼+it/2) − log π is negative for |t| < 6.29; hence (MM.4, NO-GO) every passivity / small-gain / Zames
theorem on the exterior needs an inner product in which plant ∘ loop is passive, and the only one compatible with
(MM.2) is a form ≥ 𝒲_ext itself: the passivity route is the target restated (= ES-19 "passivity returns to Herglotz", now
with the exact mechanism). (MM.5) NUMÉRICO small-gain reading of the μ = 15 data: measured off-diagonal/diagonal = 0.72
(< 1, margin 0.28), not < 0.6; a norm-type statement, so it falls under constraint 4. Row D OPEN; L′♯ OPEN.

## 0. Corpus / index check and new reason
- **Index read:** ROUTES-TRIED-INDEX README l.50–51 (walls W-lin, W-det, W-fam, W-pat, W-loc, W-mom, W-coh, flowdet,
  margin; Nyquist), l.503–504 (JJ_001, LL_001); 03_PHASES ES-19 ("GLT symbol / index / passivity in full limit —
  CIRCULAR, returns to global positivity/Herglotz"), P34-6 (dissipative Kreĭn: FALSIFIED), ES-14; 06_ l.29 (Nyquist form
  (N)); AUDIT_PHASE193 #57 (Birkhoff = Wiener–Hopf = W-det), #91 (Nyquist mesh); SURVEY_MODERN (de Branges/Kreĭn closed).
- **Sources read:** R186_117 §0–1 (Nyquist identity: sampled symbol s_T on the window, alias term), AUDIT_L_SHARP_16 §6,
  AUDIT_CONSTRAINTS_001, A_001 Thm 1.1, E_001 (E.1 pair expansion, E.2 prime collapse), II_001 (Gram of (g,Ψ̌) =
  W_T[[1,−1],[−1,1]]), EXTERIOR_DATUM_001 §3 table, TEST_BRIDGE_001 §5, JJ_001 Prop JJ.3. 06-grafico/barkhausen_*.py are
  illustrations (zeros as audio signal) and are not used.
- **New reason (why not a retry).** R186_051/117 treat the *window* form as a sampled multiplier (Fourier symbol on the
  half-circle, Kreĭn vs Bochner); ES-19 treats passivity of the full symbol. Here the system is the **exterior feedback**:
  the summation map Z = I + Σ_{n≥2}n^{−1/2}D_n acting on the leakage tail r, with the Weil kernel as plant, and the
  question is phase-sensitive (passivity), not a norm bound. The memo determines exactly why this fails (MM.2–MM.4) so
  the variant is closed with a mechanism, not by analogy.

## 1. The feedback model (PROVED as bookkeeping)
Exterior variable u > λ, r = r_f (A_001 §1), Zr(u) = u^{1/2}Σ_n r(nu). Mellin on L²(du/u):
 M[Zr](it) = ζ(½+it)·R(½+it),  R(s) := ∫_0^∞ r(u)u^{s−1}du,
so Z is the multiplier ζ(½+it) = ∏_p G_p(½+it), G_p(s) = 1/(1−p^{−s}): each prime is a **local recursive loop**
y = x + p^{−s}y (a delay of log p in the log variable with unit gain, scaled by p^{−1/2}). Its Barkhausen set (loop gain
p^{−s} = 1) is s ∈ 2πiℤ/log p; on the reflected side these are the points 1 + 2πik/log p found as sources in INV_L_001 L3.
The plant is 𝒦 = b_∞ + Lévy (ν) + primes (c_q translations) + pole (rank two, 2Re AB̄). The window form is the quadratic
form of the closed-loop output Zr restricted to (a,∞): W_T(g) = 𝒲_ext[Zr] (A_001 Thm 1.1, PROVED there).
Loop gains of the data: with X_{mn} := ⟨r̃(·+log m), K_W r̃(·+log n)⟩ (E_001 E.1), 𝒲_ext[Zr] = Σ_{m,n}(mn)^{−1/2}X_{mn}, and
γ_n := X_{1n}/X_{11} is the measured gain of channel n (−0.48, −0.30, −0.15 for n = 2, 3, 5 at μ = 15).

## 2. Results
**MM.1 (PROVED, elementary).** For σ = Re s > 0: Re G_p(s) = (1 − p^{−σ}cos(t log p))/|1−p^{−s}|² ≥ 1/(1+p^{−σ}) > ½.
(Write w = p^{−s}, |w| = ρ < 1: Re 1/(1−w) ≥ 1/(1+ρ), the image of |w| = ρ being the circle with real interval
[1/(1+ρ), 1/(1−ρ)].) Each prime channel is strictly passive, with uniform margin ½. NUMÉRICO check: min on σ = ½ equals
1/(1+p^{−½}) for p = 2, 3, 5 to 10⁻⁷.

**MM.2 (PROVED; full-line losslessness = exact Barkhausen marginality).** Let F(s) = Γ_ℝ(s)ζ(s). Since F(½+it) ∈ ℝ·e^{iθ}
with |F(σ+it)| = |F(1−σ+it)| (functional equation), ∂_σ|F|² = 0 at σ = ½ for every t (smooth function, even in σ−½).
Hence, on σ = ½,  ∂_σ|ζ|² = −|ζ|²·2Re(Γ_ℝ′/Γ_ℝ) = −|ζ|²Θ(t),  Θ(t) := Re ψ(¼+it/2) − log π  (Θ(0) = b_∞).
In Mellin, the archimedean plant (b_∞ + Lévy) acts on a full-line function Φ with multiplier Θ; the prime comb acts by
2Re(ζ′/ζ) and, on Z-images, by the prime collapse (E_001 E.2: Λ∗1 = log) as the cross term with Z_log, multiplier
2Re(ζ′ ζ̄)/|ζ|²·|ζ|² = ∂_σ|ζ|². For Φ = Zr on the full line:
 archimedean + primes = ∫|R|²(|ζ|²Θ + ∂_σ|ζ|²)dt/2π = 0,
so the full-line Weil form of a Z-image is the pole term alone, and the pole term is cancelled by the comb mean (II_001:
both grow ±A·M_μ(1)e^{x/2}). This is the Mellin proof of II_001's Gram identity W_full(g ⊕ Ψ̌) = W_T(1+1−2) = 0. Signals
reading: **the closed loop "plant ∘ (Σ_n dilations)" is lossless; the loop gain is exactly 1 at phase 0 on the whole
critical line** (Barkhausen identically satisfied). Positivity of W_T is then the sign of the energy left at the
truncation edge x = a (the window), i.e. a *boundary* quantity of a lossless system, not a dissipation inequality.
(Formal at the level of A_001's absolute convergence; growth handled as in II_001.)

**MM.3 (CITED + PROVED).** (a) Z is not positive-real on σ = ½: Re ζ(½) = −1.46 (NUMÉRICO, trivial); on 1 < σ < σ₀ ≈ 1.19,
inf_t Re ζ(σ+it) < 0 (van de Lune 1983, CITED; Bohr–Landau value distribution). The phase of a product of passive
loops adds; ∑_p arg G_p is unbounded, so the cascade leaves the right half-plane. (b) The plant is not passive: Θ(t) < 0
for |t| < t₀ = 6.2898 (NUMÉRICO root; Θ(0) = −5.372), = prop:archneg; the pole is rank-two indefinite (constraint 13);
only the Lévy part is PD.

**MM.4 (NO-GO for the passivity/small-gain class on the exterior).** Class 𝒫: arguments of the form "there is a Hilbert
inner product ⟨·,·⟩_H on exterior data in which the plant 𝒦 is passive (resp. has gain ≤ γ₁) and the feedback Z is passive
(resp. gain ≤ γ₂, γ₁γ₂ < 1); conclude 𝒲_ext[Zr] ≥ κ dist²". By MM.2 the closed loop on the full line has zero energy for
every r; any H-passivity inequality for the full-line loop must therefore hold with equality, i.e. gives 0 ≥ 0. A strict
inequality can come only from the truncation term, which by A_001 Thm 1.1 *is* W_T(g); so a passivity certificate for
the truncated loop is a lower bound for W_T by a form that dominates nothing but W_T itself — circular (this is the
exact mechanism behind ES-19). Small-gain versions are additionally norm bounds (constraint 4) and fail because
‖Z‖ = sup|ζ(½+it)| = ∞ (CITED, Hardy–Littlewood Ω-results; no zero data) and the plant gain is not < 1 at low t (MM.3b).
Falsifier test (constraint 5): MM.1 holds verbatim for any Beurling system and for a_P (delete the factor G_P: still a
product of passive loops); MM.2 needs the functional equation, hence fails for cΛ (c ≠ 1: the collapse gives c∂_σ|ζ|²,
residual (1−c)|ζ|²Θ of indefinite sign by MM.3b) — the one Λ-specific item is the *losslessness*, which carries no sign.

**MM.5 (NUMÉRICO, existing data only; TEST_BRIDGE_001 §5, EXTERIOR_DATUM_001 §3, μ = 15, ω_max = 48).** All measured
loop gains are real (symmetric forms): the Nyquist diagram is degenerate on the real axis; the dominant channels have
phase π (negative feedback): γ₂ = −0.479, γ₃ = −0.295, γ₄ = +0.062, γ₅ = −0.148, non-resonant ≈ 0 (v_glob). Closed-loop
reading: diagonal Σ X_nn/S = 0.761, off-diagonal −0.550, ratio 0.72 < 1 (stable), margin 0.28; the requested "< 0.6" is
NOT met. Normalised channel correlation X₁₂/√(X₁₁X₂₂) = −0.557 vs the JJ symbol bound 1/√3 = 0.577: within 3.5 %.
cΛ: no data (the form changes non-linearly, MM.4); a_P: no data. Since gains are relative to a lossless total, a margin
here is not an inequality one can prove from the gains (it is W_T/S itself).

## 3. Verdict
PROVED: MM.1, MM.2 (formal-to-rigorous at II_001's level), MM.3(b). CITED: MM.3(a), sup|ζ| = ∞. NO-GO: class 𝒫
(passivity / small-gain / Zames on the exterior loop), with mechanism "full-line loop lossless ⇒ strict passivity margin
= truncation energy = W_T". NUMÉRICO: MM.5. The single new structural fact is MM.2: the sign target is the stored energy
at the window edge of a lossless loop. Any future route must produce that boundary energy directly (e.g. a boundary-triple
/ Hamiltonian-flux realisation, 06_ l.212 "boundary triples for W_λ — never attempted"), not a dissipation bound.
**Do not retry:** passivity of G_p products, small gain over dilation channels, Nyquist/Barkhausen loop-gain criteria on the
exterior. L′♯ OPEN. **Row D OPEN.**
