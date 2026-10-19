# PROOF_L_SHARP_CC_001 — the uniform prolate envelope on t > 1 and the caustic-layer diagonal (thm:ext-layer(iii))

Phase 199, Pen and paper only (no numerics; constants are hand-derived and NOT numerically audited).
Notation of Paper 47 §22.4: c = 2πN, ψ = ψ_k real, ‖ψ‖_{L²(ℝ)} = 1, concentration χ_k (so ∫_1^∞ψ² = ½(1−χ_k)),
differential eigenvalue ϑ = ϑ_k; ODE ((t²−1)ψ′)′ + (c²t² − ϑ)ψ = 0 on t > 1 (ψ is entire; Slepian duality makes the exterior
datum a constant multiple of ψ|_{(1,∞)}: CITED, Slepian–Pollak 1961, used as in the paper).

## 0. Corpus / index check; why not a retry
Read: Z_001 (Lemma Z.1 CITED, Z.2/Z.4 ARGUED), AUDIT_L_SHARP_11 (§2: Z.1 "k fixed only", A2 Slepian identity route),
thm:ext-layer (main.tex l.10186–10221: (iii) assumes the expansion). Index README l.470–481 (phase 199): the envelope is
recorded only as an assumption (CITED Olver/Dunster); no proof of it, no explicit constant. Not a retry: the object is the same
but the tool is new for the corpus — a self-contained adiabatic-invariant (modified Prüfer) argument with an exact
integration-by-parts identity, which replaces the cited Olver Ch. 12 / Dunster 1986 uniform expansion (whose error-control
hypotheses at the regular singular point t = 1 would have to be checked and whose constants are not explicit in k). It needs no
Bessel-function asymptotics at all; the Bessel zone is handled by a monotone energy.

## 1. Standing hypothesis and notation
(H_ν) ν := ϑ/c² ≤ 1/4, and c ≥ 200 (N ≥ 32).
- For fixed k, ϑ_k = c(2k+1) + O(k²) (CITED: Slepian 1965; Osipov–Rokhlin–Xiao 2013 ch. 2), so (H_ν) holds for c ≥ c₀(k).
  Nothing below depends on k except through ν: every statement holds **uniformly for all k with ϑ_k ≤ c²/4**
  (=: k ≤ k₀(c); k₀(c) ≍ c/8 by the same CITED asymptotic). Parity of k is not used.
- p = t²−1, q = c²t²−ϑ, P = pq, Ω = √(q/p), ε = P′/(4P) = (t/2)(1/p + c²/q), ρ = ε/Ω, γ = (1−ν)^{−1/2} ≤ 2/√3.
  Elementary: c²t²/γ² ≤ q ≤ c²t² on t ≥ 1; hence √P ∈ [c t√p/γ, c t√p], 1/q ≤ γ²/(c²t²).
- θ = arcsec t: dt/(t√p) = dθ (Z_001 Prop Z.3).

## 2. The adiabatic invariant (exact identities; PROVED)
Put a = P^{1/4}ψ, b = P^{−1/4}pψ′, G = a²+b² = √P ψ² + (pψ′)²/√P, and write a = √G cos φ, b = −√G sin φ (t > 1). From the ODE:
 a′ = εa + Ωb,  b′ = −εb − Ωa  ⇒  **(log G)′ = 2ε cos 2φ,  φ′ = Ω − ε sin 2φ.**   (2.1)
Since (sin 2φ)′ = 2cos 2φ(Ω − ε sin 2φ):
 **2ε cos 2φ = ρ·(sin 2φ)′ + ερ sin 4φ,   cos 2φ = (sin 2φ)′/(2Ω) + ρ sin 2φ cos 2φ.**   (2.2)
Also E := ψ² + (pψ′)²/P = G/√P satisfies E′ = −(pψ′)²P′/P² ≤ 0, and E(1+) = ψ(1)² (pψ′ → 0, ψ entire). Hence
 **|ψ(t)| ≤ |ψ(1)| for all t ≥ 1** and ψ(t)² = (G(t)/√P(t)) cos²φ(t).   (2.3)

## 3. Size of ρ, ε (PROVED, elementary)
(i) ρ = (t/2)[P^{−1/2} + c²√p q^{−3/2}] ≤ (γ/(2c))(1/√p + γ²/2)  (using √p/t² ≤ ½).
(ii) t·P^{−1/2} is decreasing (its derivative is P^{−1/2}(1 − t²/p − c²t²/q) < 0); the second term is unimodal (its derivative
has the sign of c²t²(2−t²) − ϑ(2t²−1), decreasing in t) and ≤ γ³/(4c). Hence TV_{[t,∞)}ρ ≤ γ/(2c√p(t)) + γ³/(2c).
(iii) ε ≤ t/(2p) + γ²/(2t); with ∫_t^∞ s p^{−3/2} = p(t)^{−1/2}, ∫_1^∞ ds/(s√p) = π/2, ∫_1^∞ √p/s³ = π/4:
 ∫_t^∞ ερ ≤ (1/(2c))[γ/(2√p(t)) + γ³π/2 + γ⁵π/8].

## 4. Theorem CC.1 (uniform envelope, explicit; PROVED)
G_∞ := lim_{t→∞}G(t) exists, and for every t > 1, with σ(t) := (1.45/√(t²−1) + 2.77)/c,
 **G(t) = G_∞·exp(x(t)),  x(t) = ρ(t) sin 2φ(t) − R(t),  |x(t)| ≤ σ(t).**   (4.1)
*Proof.* Integrate (2.1) on [t,∞) and use the first identity of (2.2): log G_∞ − log G(t) = −ρ(t)sin 2φ(t) − ∫ρ′ sin 2φ + ∫ερ sin 4φ
(ρ → 0 at ∞; both integrals converge absolutely by §3, which also gives existence of G_∞). |R| ≤ TVρ + ∫ερ. Summing §3(i)–(iii):
|x| ≤ (1/(2c))[2.5γ/√p + γ³(3/2 + π/2) + γ⁵π/8] ≤ σ(t) for γ ≤ 2/√3. □
Set **C_c² := G_∞/c** and z := c√(t²−1). Consequences:
(a) **Langer envelope.** |ψ(t)| ≤ √γ·e^{σ(t)/2}·C_c·(t²(t²−1))^{−1/4} for all t > 1 (from ψ² ≤ E = G/√P). For z ≥ 2 and c ≥ 200:
 **|ψ(t)| ≤ 1.57·C_c·(t²(t²−1))^{−1/4}.**
(b) **Bessel zone (Lemma CC.2 below).** ψ(1)² ≤ 35·G_∞ = 35c·C_c². With (2.3): **for t ∈ [1,2], |ψ(t)| ≤ 10.3·C_c·√c·(1+z)^{−1/2}**,
 the J₀-shaped uniform form (width t−1 ≍ c^{−2}), matching ψ(1)J₀(z) ~ ψ(1)(2/(πz))^{1/2}.
(c) **Normalisation (upgrades Z.2; PROVED).** C_c² = (2/π)(1−χ_k)/(1+e₁), with e₁ as in §6.
(d) **Phase.** φ′ = Ω(1 − ρ sin 2φ), so the phase is z(t) + O(∫ε ρ) with the WKB z(t) = ∫_1^t Ω; the explicit form
 z = c√(t²−1) − ((2k+1)/2)arcsec t + O(k²/c) of the paper is not needed for (iii) and is not re-proved here.

**Lemma CC.2 (ψ(1) vs G_∞; PROVED).** Let ζ(t) = ∫_1^tΩ, A = √P, so (Aψ_ζ)_ζ + Aψ = 0, E = ψ² + ψ_ζ², dE/dζ = −2(A_ζ/A)ψ_ζ².
(1) Aψ_ζ = −∫_0^ζ Aψ, A increasing, |ψ| ≤ |ψ(1)| ⇒ |ψ_ζ| ≤ ζ|ψ(1)|.
(2) A_ζ/A = 2ρ and c√p/γ ≤ ζ ≤ c√p ⇒ ζA_ζ/A ≤ γ(1 + γ²√p/2) ≤ 1.156 =: κ on ζ ≤ 1.
(3) Hence E(ζ₁) ≥ ψ(1)²(1 − κζ₁²); at ζ₁ = 0.8: ≥ 0.260ψ(1)². A(t₁) ≥ c√p₁/γ ≥ ζ₁/γ ≥ 0.693, so G(t₁) ≥ 0.180ψ(1)².
(4) c√p₁ ≥ 0.8 ⇒ σ(t₁) ≤ 1.8125 + 2.77/c; by (4.1), G(t₁) ≤ 6.13·1.014·G_∞. So ψ(1)² ≤ 34.5·G_∞. □

## 5. Lemma CC.3 (oscillation averaging; PROVED)
For W ≥ 0 of bounded variation on [t_B,b] (t_B: z(t_B) = Z_B := 2), with m := W/√P and the second identity of (2.2)
(note m/Ω = W/q):
 J_W := ∫_{t_B}^b m cos 2φ dt = [W sin 2φ/(2q)]_{t_B}^b − ∫(W/(2q))′ sin 2φ + ∫ mρ sin 2φ cos 2φ,
 |J_W| ≤ W(t_B)/(2q(t_B)) + W(b)/(2q(b)) + ½TV(W/q) + ½∫Wρ/√P.
- W ≡ 1, b = ∞: |J₁| ≤ (γ²/c²)[1 + ¼log(c/Z_B) + 0.27]  (∫_{t_B}^∞dt/(tp) = log(t_B/√p_B)).
- W = 𝔴_N on (t_B,2) (𝔴_N = log(Nt²/√(t²−1)) ≥ log 2N, two monotone pieces, 1/q monotone):
 |J_𝔴| ≤ (γ²/c²)·sup𝔴·[2.77 + ¼log(c/Z_B)], sup_{[t_B,2]}𝔴 ≤ 2.01·log 2N.
So ∫W cos²φ/√P = ½∫W/√P + ½J_W, and J_W is O(log c/c) **relative** to ½∫W/√P ≍ (1/c)∫W dθ — this is the
"∫𝔴 cos²(phase) = ½∫𝔴 + O(1/c)" step, with the logarithm coming from the t → 1 end, controlled at z = Z_B.

## 6. Theorem CC.4 (thm:ext-layer(iii), PROVED with explicit constants under (H_ν))
Write ∫_{t_B}^bWψ² = G_∞[½∫m + ½J_W + ∫m cos²φ(e^{x}−1)] and ∫_1^{t_B}Wψ² ≤ ψ(1)²∫_1^{t_B}W ≤ 35G_∞∫_1^{t_B}W. Relative to the
model M_W := (G_∞/(2c))∫W dθ (over the whole range, θ from 0), the errors are, for c ≥ 200, ν ≤ 1/4:
| source | W = 1 (mass, b = ∞) | W = 𝔴_N (layer, b = 2) |
|---|---|---|
| ν-factor (1−ν/t²)^{−½} ∈ [1, 1+0.77ν] | 0.77ν | 0.77ν |
| missing θ < θ_B ≤ Z_B/c | 1.27/c | 4.93/c |
| e^{x}−1, \|·\| ≤ σe^{σ}, e^{σ(t_B)} ≤ 2.31, ∫σdθ via ∫cot θ | (4.93 log(c/2) + 14.8)/c | (15.5 log(c/2) + 31.1)/c |
| J_W (Lemma CC.3) | (0.21 log(c/2) + 1.08)/c | (0.64 log(c/2) + 7.1)/c |
| Bessel zone t−1 ≤ Z_B²/(2c²), K = 35 | 89.1/c | 374/c |
So (1−χ_k)/2 = M₁(1+e₁), ∫_1^2𝔴_Nψ² = M_𝔴(1+e₂) with
 |e₁| ≤ 0.77ν + (5.14 log(c/2) + 106.2)/c,  |e₂| ≤ 0.77ν + (16.2 log(c/2) + 417)/c.
Since ∫_0^{π/3}𝔴_N dθ = (π/2)D_lay(N) and ∫_0^{π/2}dθ = π/2 (Z_001 Prop Z.3, PROVED), M_𝔴/M₁ = D_lay(N), hence:
**Theorem CC.4.** Under (H_ν) (in particular for every fixed k and c ≥ max(200, c₀(k)), and uniformly in k ≤ k₀(c)):
 ∫_1^2 𝔴_N|ψ_k|² dt = ½(1−χ_k)·D_lay(N)·(1+η),  two-sided: **(1−χ_k)[(2/3)log 4N − 0.107689](1+η)**,
 **|η| ≤ (|e₁|+|e₂|)/(1−|e₁|) ≤ [21.4 log c + 1.54 νc + 523]/c · (1−|e₁|)^{−1}**,
i.e. η = O((log c + k)/c) with an explicit constant; for fixed k, η = O(c^{−1}log c). (At c = 200, |e₁| ≤ 0.65 + 0.77ν, so the
bound is meaningful but crude there; the constants are not optimised — e.g. K = 35 and Z_B = 2 are generous.)
**Leading-order mass law (PROVED).** ψ²dt = (C_c²/2)(1 + O(ν))dθ + (oscillating part, Lemma CC.3) + (error ≤ σ e^{σ}), i.e. the
one-sided exterior mass is distributed as (1−χ_k)/π·dθ up to the explicit errors above.

## 7. What changes in Paper 47 (do not edit; note only)
- thm:ext-layer(iii): label "(layer diagonal)" under "Assume the uniform Bessel–Langer expansion" can become **proved**, with the
  hypothesis replaced by (H_ν): ϑ_k ≤ c²/4, c ≥ 200, and "(1+o(1))" by "(1+η), |η| ≤ (21.4 log c + 1.54ϑ_k/c + 523)/(c(1−|e₁|))".
  The theorem title "conditional on the uniform prolate envelope" should drop "conditional" for (i)–(iii); (iv) stays not proved
  (stationary-phase remainder; CC does not address it, though CC.1(a),(d) supply rigorous amplitudes and phase-derivative control).
  The citations Olver1974/Dunster1986 become unnecessary for (iii); OsipovRokhlinXiao2013 remains for ϑ_k asymptotics (c₀(k)).
- The C_c² = (2/π)(1−χ_k) normalisation is now proved (CC.1(c)), not assumed. Editor must check against the paper's
  definitions: 𝔴_N as in l.10000 (log 2N − log sin 2θ on (1,2)), one-sided mass ½(1−χ_k), χ_k = concentration (not ϑ_k).

## 8. Labels
- PROVED: identities (2.1)–(2.3); §3 bounds; Thm CC.1 (envelope, explicit, uniform in k under H_ν); Lemma CC.2 (ψ(1)² ≤ 35G_∞);
  Lemma CC.3 (averaging); Thm CC.4 (layer diagonal with explicit η); normalisation C_c² (upgrades Z.2 from ARGUED); Bessel-zone
  correction (upgrades Z.4 from ARGUED, with the stated non-sharp constant).
- CITED: Slepian duality (exterior datum ∝ ψ_k), ψ_k ∈ L²(ℝ) entire; ϑ_k asymptotics for c₀(k), k₀(c).
- Not done / OPEN: sharp constants; N < 32; the resonances (iv) remainder; the explicit phase z(t) to O(k²/c).
- Constants are pen-and-paper and not numerically audited — an audit is recommended (especially the table in §6).
No sign of row D is claimed. L′♯ OPEN; row D OPEN.
