# PROOF_L_SHARP_Z_001 — Theorem C: the caustic layer ω ∈ (1,2) on a single prolate tail (diagonal + (1,n) resonances)

Phase 199, Pen and paper; three scratch checks of constants (not stored) are labelled NUMÉRICO and only
check the asymptotics against existing data (PRECHECK_T1_001_data, TEST_BRIDGE_001).

**Outcome.**
1. **Diagonal on the layer, closed form (PROVED given the Langer envelope).** With ω = sec θ the Langer mass is dθ and
   𝔴_μ = log 2μ − log sin 2θ on (1,2). Hence, per unit one-sided Langer mass m = (2/π)dθ,
   **D_layer(μ) = (2/3)·log 4μ − Cl₂(2π/3)/(2π) = (2/3)log 4μ − 0.107689**  (Cl₂(2π/3) = 0.676628).
   μ = 15: 2.6219 (full diagonal D(15) = 5.0513, the PRECHECK D₄). The (ω−1)^{−½} divergence of the Langer envelope is
   exactly the dθ measure: there is no divergence at all in θ, and no Beta function is needed.
2. **The turning point ω = 1 is not Airy.** It is a regular singular point of the prolate ODE (exponents 0,0): the uniform
   form is Bessel, ψ_k(ω) ≈ ψ_k(1)·J₀(c√(ω²−1)), transition zone ω − 1 ≲ c^{−2} (z = c√(ω²−1) ≲ 1), not c^{−2/3}. Its
   correction to the diagonal is O(log(μc)/c) relative (ARGUED). The Airy caustic of W_001 (t* ≈ 4πμ) lives in the other
   (dual) variable and is irrelevant here.
3. **Resonances: no compensation.** At s_n = √(1+n^{−2}) and T_n = n s_n = √(n²+1), the amplitude product is exactly
   n-free: s_n^{½}|a(s_n)|·T_n^{½}|a(T_n)| = C² (PROVED algebra: (s_n²−1)^{−¼} = n^{½}·… is cancelled by (T_n²−1)^{−¼} = n^{−½}·…).
   So the c^{−½} of stationary phase survives; s₂ has z = c/2 (= 47 at μ = 15), deep in the oscillatory zone.
   **R̂_n(k) = (4/π)·μ^{−½}·log(μ(1+n^{−2}))·n/((n²+1)√(n²−1))·cos(c(n²−1)/n − ((2k+1)/2)(π/2 − 2arctan(1/n)) + π/4)**
   per unit one-sided mass (note √(2π/c) = μ^{−½} exactly). ARGUED (stationary phase on the CITED uniform expansion).
4. **Assembly.** 𝔔_layer[r_k] = ((1−λ_k)/2)·[D_layer(μ) + Σ_n R̂_n(k)]·(1 + O(log c/c)) per side; worst case
   |ΣR̂_n| ≤ (4/π)μ^{−½}Σ_n w_n log(μ(1+n^{−2})) = 0.589, 0.573, 0.371 (μ = 4, 15, 100), while D_layer = 1.74, 2.62, 3.89.
   **The bracket is positive for every μ ≥ 4 at leading order, grows like (2/3)log 4μ, and bracket/log 2μ → 2/3.**
5. **The μ = 15 data are NOT a single-prolate-tail effect.** The formula gives |(1,2)|/X₁₁ ≤ 0.054 (with phase: +0.033) and
   |(1,3)|/X₁₁ ≤ 0.024, against the measured −0.48 and −0.30 on ρ_{v*} (TEST_BRIDGE §5): a factor 9–12 and the wrong
   sign-coherence. The pure ψ₄ tail (PRECHECK) has total cross-dilate −1.3 % of the diagonal, consistent with item 3. The
   TEST_BRIDGE deficit therefore sits in the non-prolate component of the even-window datum (parity / rough complement /
   jump datum, TEST_BRIDGE §2, §4; AUDIT_10), not in the caustic layer of a prolate tail. Theorem C does not explain W/(1−λ₄)
   = 4.08 nor the ladder 4.08/1.99/1.79 (leading order is ½D(μ) = 2.53, k-independent).
6. **κΛ.** On (1,2) H₁ = 0, so the layer diagonal is κ-free; the resonant weight is exactly
   log(μ(1+n^{−2})) + (1−κ)log n (PROVED algebra). The extra term is summable (Σw_n log n = 0.913), so the layer bracket stays
   positive at leading order for every κ near 1 (and for all κ once μ is large). **The layer is Λ-insensitive: by the
   semiring principle it is not a sign source.** The Λ-sensitivity is in cells ω ≥ 2 (Cor Y.9).
No sign of row D is claimed. L′♯ OPEN. Row D OPEN.

## 0. Corpus / index check, and why this is not a retry
- Read: TEST_BRIDGE_001 (§2, §4, §5), AUDIT_L_SHARP_10 entry, Y_001 (Lemma Y.2, §6, Prop Y.8, Cor Y.9), AUDIT_L_SHARP_9,
  W_001 (caustic t*, Langer form), SYNTHESIS §3.3 (M3), BRIDGE Lemma B.0, MORI15_EXTREMAL_001, PRECHECK_T1_001 (+ data
  res_mu15_psi4_fstar2.json). Index: ROUTES-TRIED-INDEX README l.470–476 (phase 199). grep "caustic layer / capa cáustica /
  Bessel J₀ / Clausen / turning point" in the index and proof-L-sharp/: no evaluation of the t → 1 layer exists; Y_001 §9.3 and
  AUDIT_9 record it as OPEN ("t → 1 layer OPEN").
- Why not a retry: Y_001 excludes (1,1+η) by hypothesis and gives only a van der Corput bound; this memo evaluates the layer
  itself, with the exact envelope at t → 1 (Bessel, not Airy) and the stationary-phase constant at s_n with the exact Langer
  amplitudes. Different object (actual tail on the layer) and different tool (closed-form diagonal + leading stationary phase).

## 1. Setting
- ψ_k: prolate of bandwidth c = 2πμ on [−1,1], k even, ‖ψ_k‖_{L²(ℝ)} = 1, so ∫_{|ω|>1}ψ_k² = 1 − λ_k. By the prolate
  eigen-equation the exterior datum r_k(ω) = ρ(ω) of f = λ^{−½}ψ_k(·/λ) is a constant multiple of ψ_k(ω), ω > 1 (BRIDGE §1);
  we work with ψ_k itself and one side ω > 1 (one-sided mass (1−λ_k)/2).
- Prolate ODE: ((ω²−1)ψ′)′ + (c²ω² − χ_k)ψ = 0, χ_k = c(2k+1) + O(k²) (CITED, Slepian; Osipov–Rokhlin–Xiao 2013).
- 𝔴_μ(ω) = H(ω)log(μω²/√(ω²−1)) − 2H₁(ω); on (1,2): H = 1, H₁ = 0, 𝔴_μ = log(μω²/√(ω²−1)).
- Exterior form and its dilate/pair decomposition: Y_001 Lemma Y.1 (PROVED); pair (1,n) after log-symbol replacement:
  2n^{−½}Re∫G_{1n}e^{iψ_{1n}}dy, G = [½log(τ(s)τ(ns)/(2π)²) − log n]A₁Ā_n (Y.5).

## 2. The envelope at t → 1: Bessel, not Airy
**Lemma Z.1 (local form; PROVED elementary + CITED uniformity).** ω = 1 is a regular singular point of the prolate ODE with
indicial exponents (0,0); the solution regular at ω = 1 (ψ_k is entire) is, with z := ∫_1^ω√((c²x²−χ)/(x²−1))dx,
 ψ_k(ω) = ψ_k(1)·[ (ζ-factor)·J₀(z) ]·(1 + O(c^{−1})) uniformly on ω ∈ [1, X],
where the prefactor is ((z²)/((ω²−1)(c²ω²−χ)))^{¼}·(c²−χ)^{¼}… → 1 at ω = 1 (Olver, *Asymptotics and Special Functions*,
Ch. 12 §§4–5, Bessel-type uniform expansions at a double pole/regular singular point; Dunster 1986 for prolates — CITED).
*Local check (PROVED):* with s = ω − 1 the ODE is 2sψ″ + 2ψ′ + (c² − χ)ψ = O(s)·(…), and J₀(√(2(c²−χ)s)) solves the
truncated equation (s w″ + w′ + (κ/2)w = 0 ⟺ w = J₀(√(2κ s))); √(2c²s) = c√(ω²−1) + O(s^{3/2}c).
- z = c√(ω²−1) − ((2k+1)/2)·arcsec ω + O(k²/c) (expand √(c²x²−χ) = cx − χ/(2cx) + …; ∫dx/(x√(x²−1)) = arcsec).
- Large z: J₀(z) = √(2/(πz))cos(z − π/4)(1 + O(1/z)) ⇒ the Langer form ψ_k ≈ C_c(ω²(ω²−1))^{−¼}cos(z − π/4) with
  C_c² = 2ψ_k(1)²/(πc).
**Lemma Z.2 (normalisation; ARGUED).** ψ_k(1)² = c(1−λ_k)(1 + O(log c/c)), equivalently C_c² = 2(1−λ_k)/π (W_001).
*Argument:* ∫_1^∞ψ_k² with cos² → ½ gives C_c²·(π/4); the Bessel zone changes the mass by O(ψ(1)²/c²)·O(log c). Set equal to
(1−λ_k)/2.
**Consequence (answers the Airy question).** The transition zone at ω = 1 has width ω − 1 ≍ c^{−2} (z ≍ 1). The resonant points
s_n lie at z_n = c√(s_n²−1) = c/n: **s₂ = 1.118 has z = c/2 = 47.1 at μ = 15**; s_n enters the Bessel zone only for n ≳ c.
So the (1,2), (1,3) resonances are ordinary Fresnel (stationary-phase) resonances, not Airy/Bessel-dominated. The
hypothesis "s₂ in an Airy zone of width c^{−2/3}" is false (no Airy point on ω ≥ 1; the c^{−2/3} zone belongs to the caustic
t* ≈ 4πμ in the dual variable, W_001).

## 3. (i) The diagonal on the layer — closed form
**Proposition Z.3 (PROVED, given the Langer envelope).** Let m(dω) = (2/π)dω/(ω√(ω²−1)) (unit one-sided Langer mass).
 ∫_1^2 𝔴_μ dm = (2/3)log 4μ − Cl₂(2π/3)/(2π),  Cl₂(2π/3) = Σ sin(2πk/3)/k² = 0.6766277376.
*Proof.* ω = sec θ, θ ∈ (0, π/3): dω/(ω√(ω²−1)) = dθ, log ω = −log cos θ, √(ω²−1) = tan θ, so
log(μω²/√(ω²−1)) = log μ − log(sin θ cos θ) = log 2μ − log sin 2θ. Then
∫_0^{π/3}(log 2μ − log sin 2θ)dθ = (π/3)log 2μ − ½∫_0^{2π/3}log sin φ dφ, and ∫_0^x log sin φ dφ = −x log 2 − ½Cl₂(2x);
with x = 2π/3, Cl₂(4π/3) = −Cl₂(2π/3). So the integral is (π/3)log 4μ − ¼Cl₂(2π/3). Multiply by 2/π. □
- This is Lemma B.0 in integrated form: the integrand log 2μ − log sin 2θ ≥ log 2μ, minimum at θ = π/4 (ω = √2).
- The layer carries 2/3 of the Langer mass; the (ω−1)^{−½} singularity of the envelope is the Jacobian dθ = dω/(ω√(ω²−1)),
  and −½log(ω²−1) = −log tan θ is integrable against dθ. No Beta integral appears.
- Full line (for comparison): ∫_1^∞𝔴_μ dm =: D(μ); without the H-cells it would be log 4μ exactly (∫_0^{π/2}−log sin 2θ =
  (π/2)log 2); with them D(15) = 5.0513 = PRECHECK's D₄ (NUMÉRICO reproduction).
**Proposition Z.4 (Bessel correction; ARGUED).** Replacing cos² by ½ and the Langer envelope by Lemma Z.1 changes the layer
diagonal by (ψ(1)²/c²)∫_0^{Z}(zJ₀(z)² − 1/π)(log(μc) − log z)dz + (oscillatory O(1/c)) = O((1−λ_k)·log(μc)/c).
(zJ₀² − 1/π = (1/π)sin 2z + O(z^{−2}) non-oscillatory part, so the integral is bounded by O(log(μc)).) Relative size
O(log c/c) — below the resonances. **D_diag has no Airy/Bessel contribution at leading order.**
So, two-sided and in the units requested: ∫_{layer}𝔴_μ|r_k|² = (1−λ_k)·[⅓log 4μ − Cl₂(2π/3)/(4π)](1 + O(log c/c)),
Cl₂(2π/3)/(4π) = 0.053844. **D_diag(k) = ⅓log 4μ − 0.053844, k-independent at leading order.**

## 4. (ii) The (1,n) resonances at leading order
**Lemma Z.5 (amplitudes at the resonance; PROVED algebra).** For the Langer envelope |a(ω)| = C(ω²(ω²−1))^{−¼} (C = C_c):
 s_n^{½}|a(s_n)|·T_n^{½}|a(T_n)| = C²  for every n ≥ 2  (s_n² − 1 = n^{−2}, T_n² − 1 = n², s_nT_n... cancel).
*Proof.* s_n^{½}|a(s_n)| = C s_n^{½}(s_n²n^{−2})^{−¼} = C n^{½}; T_n^{½}|a(T_n)| = C T_n^{½}(T_n²n²)^{−¼} = C n^{−½}. □
So the near-turning-point growth (s_n² − 1)^{−¼} = n^{½} of dilate 1 is **exactly compensated** by the decay n^{−½} of the
dilated copy at T_n. No compensation of the stationary-phase c^{−½} occurs.
**Proposition Z.6 (leading resonance; ARGUED = stationary phase, CITED, on the CITED uniform envelope).** For fixed n ≥ 2 and
real tail r = C(ω²(ω²−1))^{−¼}cos(z(ω) − π/4) (two conjugate chirps, each of amplitude C/2; cross-chirp sum phases are
non-stationary, O(1/c)):
 X_{1n} + X_{n1} = n^{−½}·L_n·C²·√(2π/|ψ″_{1n}(y_n)|)·cos(Ψ_n − π/4)·(1 + O(n²(cn³)^{−½}))
with L_n = log(μ(1+n^{−2})) (Y_001), |ψ″| = c(n⁴−1)(n²+1)/n³ (Lemma Y.2), and
 Ψ_n = z(s_n) − z(T_n) = −c(n²−1)/n + ((2k+1)/2)(π/2 − 2arctan(1/n)) + O(k²/c)
(arcsec s_n = arctan(1/n), arcsec T_n = arctan n). Since √(2π/c) = μ^{−½}:
 **X_{1n}+X_{n1} = C²·μ^{−½}·L_n·w_n·cos(Ψ_n − π/4),  w_n := n/((n²+1)√(n²−1))**,
and per unit one-sided mass (C²π/4): **R̂_n(k) = (4/π)μ^{−½}L_n w_n cos(Ψ_n − π/4)**.
- Constants: w₂ = 0.23094, w₃ = 0.10607, w₅ = 0.03928; Σ_{n≥2}w_n = 0.617383; Σw_n log n = 0.913203.
- Validity: the amplitude's log-derivative at s_n is ≍ n², the Fresnel width (cn³)^{−½}; SP needs n ≪ c. For n ≳ c the pairs sit
  in the Bessel zone; their total is ≤ (4/π)μ^{−½}log(2μ)Σ_{n≳c}w_n = O(μ^{−½}log μ/c) (ARGUED).
- Why ARGUED and not PROVED: SP with explicit remainder for the c-dependent amplitude near t = 1, and the uniform-in-n
  remainder, are not written; the Langer envelope is CITED (Dunster/Olver) with O(1/c) corrections.
**NUMÉRICO check (scratch, μ = 15, k = 4, WKB phase with χ = 9c, direct quadrature of n^{−½}∫L A₁A_n cos(Φ(s)−Φ(ns))dy):**
direct / SP = 0.1058 / 0.0951 (n = 2), −0.0775 / −0.0737 (n = 3), −0.0005 / −0.0039 (n = 5, phase-sensitive), C = 1.
Ψ_n from the formula agrees with the quadrature phase to 0.04–0.07 rad (O(k²/c)).

## 5. (iii) Assembly, sign and value
**Theorem C (caustic layer; leading order ARGUED, diagonal PROVED given the envelope).** For k even fixed, μ → ∞,
 𝔔_layer[r_k] := (layer diagonal) + Σ_{n≥2}(resonances with s_n in the layer)
 = (1−λ_k)·[ ⅓log 4μ − Cl₂(2π/3)/(4π) + ½Σ_{n≥2}R̂_n(k) ]·(1 + O(log c/c))   (two-sided),
and, worst case over the phases, ½Σ|R̂_n| ≤ (2/π)μ^{−½}Σ_n w_n log(μ(1+n^{−2})) ≤ (2/π)·0.6174·μ^{−½}log(1.25μ).
- Values of the per-side bracket D_layer ± Σ|R̂_n|: μ = 4: 1.741 ± 0.589; μ = 15: 2.622 ± 0.573; μ = 100: 3.887 ± 0.371;
  μ = 1000: 5.422 ± 0.175. **Positive at every μ ≥ 4 even with all cosines adversarial; the bracket grows as (2/3)log 4μ
  (per side); bracket/log 2μ → 2/3. It does not tend to a constant; it tends to a constant multiple of log μ.**
- Resonances are relatively O(μ^{−½}): ≤ 22 % of D_layer at μ = 15, ≤ 34 % at μ = 4.
**Comparison with data (NUMÉRICO, existing files only).**
- Pure ψ₄ tail, μ = 15 (PRECHECK res_mu15_psi4_fstar2.json): W/one-sided = 4.9608 vs diagonal with actual mass 5.0279:
  total cross −0.067 = −1.3 % of the diagonal, within Theorem C's resonance window (formula: n = 2: +0.135, n = 3: −0.099 per
  unit mass, rest small; non-resonant pairs O(1/c)). Consistent.
- Even-sector extremal ρ_{v*} (TEST_BRIDGE §5): X₁₁ for a Langer tail is log 4μ = 4.094 per unit mass, so Theorem C predicts
  |(1,2)/X₁₁| ≤ 0.054 (phase value +0.033) and |(1,3)/X₁₁| ≤ 0.024, vs measured **−0.48, −0.30**. **Not reproduced: a factor
  9–12.** The large plain overlap ⟨φ₁,φ₂⟩ = −0.084X₁₁ measured there is impossible for a Langer tail (its dilates are
  oscillation-decoupled except in the Fresnel windows). Hence the measured caustic-layer deficit is carried by the
  non-prolate part of the even-window datum (parity image / rough complement / jump datum: TEST_BRIDGE §2, §4; AUDIT_10),
  i.e. by data that are not regular on the Fresnel scale — the Prop Y.8 regime, now located.
- W/(1−λ₄) = 4.08 and the ladder 4.08/1.99/1.79: Theorem C (all ω) gives ½D(15) = 2.53 for every k at leading order (k
  enters only through Ψ_n and O(k²/c)). The ladder is not a single-tail layer effect. (Same 1.6× gap as SYNTHESIS.)

## 6. (iv) κΛ in the layer
**Proposition Z.7 (PROVED algebra + ARGUED leading order).** With the comb multiplied by κ:
- layer diagonal: H₁ ≡ 0 on (1,2) ⇒ κ-free (dilate 1 has log 1 = 0). D_layer unchanged.
- resonant weight at (s_n, T_n): ½log(τ_n²/(2π)²) − κ(log 1 + log n) = **log μ + (1−κ)log n + log(1+n^{−2})**.
- Leading order: ½Σ|R̂^κ_n| ≤ (2/π)μ^{−½}[0.6174·log(1.25μ) + |1−κ|·0.9132]. Positivity of the layer bracket is NOT lost for
  any κ with |1−κ| ≲ μ^{½}·D_layer, in particular for every fixed κ once μ is large.
- Reading: the comb's cancellation of log n is Λ-specific but irrelevant at leading order (Σn^{−2}log n < ∞). **The layer is
  comb-generic; under the semiring principle it cannot carry the sign.** The κ-sensitivity of the exterior form is in the
  cells ω ≥ 2 (−2κH₁ on the diagonal; Cor Y.9).

## 7. What remains (honest)
1. Theorem C is about one prolate tail. The extremal's caustic-layer deficit (−0.55 S) is outside its scope; the open object is
   the non-prolate component of the even window datum (OPEN; first task: its Fresnel-scale profile near s₂, s₃).
2. PROVED-ness: Prop Z.3 and Lemma Z.5 are exact; Z.1 needs the CITED uniform Bessel expansion; Z.2, Z.4, Z.6 are ARGUED
   (explicit remainders not written; uniformity in n ≲ c not written).
3. Edge f(λ) ≠ 0 and gauge Π: not addressed. P3b is OPEN (AUDIT_10).
No sign of row D claimed. L′♯ OPEN; row D OPEN.

## 8. Labels
- **PROVED:** Prop Z.3 (closed-form layer diagonal (2/3)log 4μ − Cl₂(2π/3)/(2π), given the envelope); Lemma Z.5 (n-free
  amplitude product C²); local Bessel form at ω = 1 (indicial exponents 0,0); κ-weight algebra (Z.7).
- **CITED:** uniform Bessel/Langer expansion at a regular singular point (Olver Ch. 12; Dunster 1986); χ_k asymptotics
  (Slepian; Osipov–Rokhlin–Xiao); stationary phase (Stein 1993 VIII); Clausen integral.
- **ARGUED:** normalisation C_c² = 2(1−λ_k)/π (Z.2); Bessel correction O(log c/c) (Z.4); leading resonance R̂_n (Z.6); n ≳ c tail;
  Theorem C as an asymptotic statement.
- **NUMÉRICO (check only):** D_layer, D(μ) = 5.0513 at 15 (= PRECHECK D₄); Σw_n, Σw_n log n; SP vs quadrature (n = 2, 3, 5);
  PRECHECK ψ₄ cross total −1.3 %.
- **Corrections recorded:** "s₂ in an Airy zone" — false (Bessel zone ω−1 ≍ c^{−2}, s₂ at z = c/2). "Langer divergence needs
  Beta/Airy regularisation at leading order" — false (it is the dθ Jacobian). "TEST_BRIDGE (1,2) = −0.48 is the prolate
  caustic layer" — false for prolate tails (Theorem C gives ≤ 0.054).
- **Do not retry:** explaining the μ = 15 resonant deficit by single-prolate (Langer) tails or by an Airy/Bessel turning-point
  mechanism; seeking the sign in the layer (1,2) (κ-free diagonal, κ-generic leading order).
