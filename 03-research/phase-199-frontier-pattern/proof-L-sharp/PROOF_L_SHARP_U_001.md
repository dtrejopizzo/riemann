# PROOF_L_SHARP_U_001 — Strategy U: transfer of the sector formula from the Sonin class 𝒮 to the PW carrier

Phase 199, prover memo (pen and paper; no numerics). Target: Lemma L′♯ = (★★) (AUDIT_L_SHARP_4 §8, AUDIT_L_SHARP_5 §6,
constraints 1–17). , no zero location is used,

**Outcome in one line.** L′♯ NOT proved. Constraint 16 (𝒮-vs-PW gap) is resolved *as a statement of structure*: (U.1, PROVED,
unconditional) the sector formula holds on the carrier itself in bilinear "edge-mirror" form, with the two 𝔉_μ-sectors
f_± = (f ± 𝔉_μ f)/2 of every window datum, the radical lemma for f_± being *derived* from Guo's compact-class lemma (no (H1),
no (H2)); (U.2, PROVED in L²) the gauge-minimal representative of a carrier datum is its orthogonal projection onto the
**Sonin annulus 𝒱_μ = 𝒮(1,1)⁺ ⊖ 𝒮(1,μ)⁺**, so ℓ(g) = λ‖Πρ‖²; (U.3, CONDITIONAL) the transfer identity
𝔔[ρ] = 𝒲_refl[σ_+] − 𝒲_refl[σ_−] + (rank-one polar block), σ = Π_𝒮ρ. Verdict on (ii): **REF-D** (exact restatement; the
minus sector carries −SOS, sign burden stays on 𝒫 per sector). No sign is claimed. (★★) OPEN; row D OPEN.

## 0. Corpus / index check and why this is not a retry
- Index read: README l.453 (D_001: CC prolate–Sonin frame, Thm 2.1 Sonin decomposition of 𝔐, weight inversion), l.465
  (T_001 + AUDIT_17/AUDIT_L_SHARP_5), l.452 (A_001 half-line identity, gauge = radical), l.47 (Sonin/Connes/prolate cluster:
  no sign), 04_PHASES l.35 (W-Sonin NO-GO: Sonin positive part + bounded remainder), l.29 (W11′), R186 rows (semilocal Sonin
  chain, ρ*), P106 (co-Poisson/prolate frame NO-GO), G8D-106 (prolate leakage determines square not sign).
- Why new. (a) None of these identifies the **gauge quotient of the carrier** with a Sonin space: D_001 §1 rejects
  "constraints = Sonin conditions" (correctly: f(0) = f̂(0) = 0 are not Sonin conditions) and works with CC's trace on window
  vectors; here the Sonin space appears as the *orthogonal complement of the gauge* in the exterior L², a different object.
  (b) T_001 proved the sector formula on 𝒮 and AUDIT_5 declared it contentless for W_T; U.1 shows the sector formula holds on
  the carrier with a *scaled* Fourier transform 𝔉_μ (cut at the window edge), which neither memo considered. (c) W-Sonin /
  W11′ use Sonin positivity as a sign source; this memo uses no Sonin positivity and claims no sign.

## 1. Edge mirror on the carrier (U.1)
Notation as A_001 §1: λ = e^T, μ = λ², a = T, f admissible (even, C² on [−λ,λ], supp ⊂ [−λ,λ], f(0) = f̂(0) = 0, f(λ) = 0),
Φ_f(x) = e^{x/2}Σ_{n≥1}f(ne^x), g = Φ_f|_I, Ψ_f = Φ_f|_{(−∞,−a)}. Scaled Fourier transform 𝔉_μ h(ξ) := μ^{1/2}ĥ(μξ)
(unitary, 𝔉_μ² = id on even h, self-dual scale 1/λ).

**Lemma U.1.1 (edge intertwining; PROVED).** For even h with h(0) = ĥ(0) = 0 and enough decay: Φ_{𝔉_μ h}(x) = Φ_h(−2a − x).
*Proof.* T Lemma 1.1 gives Φ_h(−y) = Φ_ĥ(y). Put y = 2a + x: Φ_ĥ(x+2a) = e^{(x+2a)/2}Σĥ(μne^x) = Φ_{𝔉_μh}(x). □
So R_a: x ↦ −2a − x (reflection about the window edge −a) is intertwined with 𝔉_μ. (T_001 used the cut 0, i.e. 𝔉 = 𝔉_1 in
ρ-units; translation invariance of W makes the two equivalent, §2.)

**Lemma U.1.2 (radical for the sectors; PROVED from CITED Guo Lemma 4.4).** f_± := (f ± 𝔉_μ f)/2 satisfy 𝔉_μ f_± = ±f_±,
f_±(0) = 0, and WΦ_{f_±} = 0 a.e.
*Proof.* Φ_{f_±} = ½(Φ_f ± Φ_f∘R_a) by U.1.1 (f̂ = O(ξ^{−2}) by Guo Lemma 4.3, so Φ_{𝔉_μf} converges). W is a convolution
with even kernels (A_001 §1), so W(Φ∘R_a) = (WΦ)∘R_a; WΦ_f = 0 (Guo Lemma 4.4, CITED). □
This removes hypotheses (H1), (H2) of T_001/AUDIT_5 for this class: the sector data are explicit (f_± ≠ 0, and f_− = 0 is
impossible for f ≠ 0 since f = 𝔉_μ f would make f and f̂ both compactly supported).

**Theorem U.1.3 (sector formula on the carrier; PROVED).** With s = x + a, ǧ(s) := g(−a+s) (s ∈ (0,2a)), Ψ̌(s) := Ψ_f(−a−s)
(s > 0), u_± := ǧ ± Ψ̌ = 2Φ_{f_±}(−a+·)|_{(0,∞)}, and for u on (0,∞)
 𝒲_refl[u] := Σ_{j≥1}L_j(u)² + 𝒫[u] − A(u)²,  L_j(u) = ∫u e^{−(2j+½)s}ds, A(u) = ∫u e^{s/2}ds, 𝒫[u] = Σ_qΛ(q)q^{−½}(u∗u)(log q):
 **W_T(g) = Σ_{j≥1}L_j(ǧ)L_j(Ψ̌) + 𝒫(ǧ,Ψ̌) − A(ǧ)A(Ψ̌) = ¼𝒲_refl[u_+] − ¼𝒲_refl[u_−].**
*Proof.* A_001 Thm 1.1(c): W_T(g) = −𝒲(g,Ψ_f). In the variables s, t with x = −a+s, y = −a−t: ν(x−y) = ν(s+t) = Σ_{j≥0}e^{−(2j+½)(s+t)}
(Tonelli), Ψ_f(x+log q) = 0 for x > −a, Ψ_f(x − log q) = Ψ̌(log q − s), 2cosh((x−y)/2) = e^{(s+t)/2} + e^{−(s+t)/2}. Hence
−𝒲(g,Ψ_f) = Σ_{j≥0}L_jL_j + 𝒫(ǧ,Ψ̌) − A A − B B, and L_0 = B cancels the B-pole product exactly. Polarisation
(4xy = (x+y)² − (x−y)², 𝒫 symmetric bilinear) gives the second form. □
Consistency: equivalently W_T(g) = 𝒲_{(−a,∞)}[Φ_{f_+}] + 𝒲_{(−a,∞)}[Φ_{f_−}] with the sectors 𝔔-orthogonal (T Prop 3.3, now
unconditional by U.1.2) and 𝒲_{(−a,∞)}[Φ_{f_ε}] = ε𝒲_refl[u_ε/2] (T Thm 3.1 with R_a in place of R).
**Status.** PROVED; elementary restatement of Guo Thm 4.5 (the operator X written as a bilinear form with a completely monotone
Hankel kernel). The archimedean part is SOS on u_+ and **−SOS on u_−**; it is not manifestly positive on the carrier.

## 2. The exact relation PW ↔ Sonin: the gauge quotient is a Sonin annulus (U.2)
ρ-units (T_001): ρ(t) := r_f(λt) = f̂(λt) on |t| > 1 (even); ‖r_f‖² = λ‖ρ‖². By translation invariance of W,
𝒲_{(a,∞)}[Ψ̌(·)] = λ𝒲_{(0,∞)}[Φ_ρ] =: λ𝔔[ρ] (Ψ̌ = λ^{1/2}Φ_ρ(·−a), A_001 Rem 1.1(ii)); so W_T(g) = λ𝔔[ρ], T-free form.
Sonin spaces (CC Def 4.4): 𝒮(α,β) = {ρ ∈ L²_even: ρ = 0 on (−α,α), ρ̂ = 0 on (−β,β)}; 𝒮(α,β)⁺ := {ρ = 0 on (−α,α),
ρ̂ ≡ const on (−β,β)} (dim 𝒮(α,β)⁺/𝒮(α,β) ≤ 1, PROVED: the constant is a linear functional).

**Theorem U.2.1 (PROVED, L² level).** In L²_even(|t|>1):
 (a) 𝒢̄ (closure of rescaled gauge {(1−P_1)ψ̂ : ψ ∈ C², supp ψ ⊂ [−1,1], ψ(0) = ψ̂(0) = 0}) = (𝒮(1,1)⁺)^⊥;
 (b) the closure of the carrier set 𝒞_μ := {ρ_f : f admissible} is (𝒮(1,μ)⁺)^⊥;
 (c) 𝒮(1,μ)⁺ ⊂ 𝒮(1,1)⁺ (μ ≥ 1); hence ℓ(g) = λ‖Πρ‖², Π := orthogonal projection onto 𝒮(1,1)⁺, and Π𝒞_μ is dense in the
 **Sonin annulus 𝒱_μ := 𝒮(1,1)⁺ ⊖ 𝒮(1,μ)⁺**; 𝒱_μ ↑ 𝒮(1,1)⁺ as μ → ∞ (∩_μ𝒮(1,μ)⁺ = {0}).
*Proof.* (a) Rescaling ψ(y) = φ(y/λ)/λ (ψ̂(t) = φ̂(λt)) maps the gauge 𝒢₀ of A_001 §2 onto the stated set; its L²-closure on the
ψ side is V = {ψ ∈ L²(−1,1): ∫ψ = 0} (point conditions are not L²-closed). ρ supported in |t| ≥ 1 is ⊥ (1−P_1)𝔉ψ ⟺
⟨ρ̂, ψ⟩ = 0 ∀ψ ∈ V ⟺ ρ̂ ≡ const on (−1,1). (b) Fubini: ∫h(t)f̂(λt)dt = ∫f(x)ĥ(λx)dx (h, f real even), so h ⊥ 𝒞_μ ⟺ ĥ(λx) is ⊥ to
{f ∈ L²(−λ,λ): ∫f = 0} (C² with f(0) = f(λ) = 0 dense there) ⟺ ĥ ≡ const on (−μ,μ). (c) inclusion is immediate; ℓ =
dist²(r_f,𝒢̄) (A_001 Prop 2.1(c)) = λ‖Π_{𝒢̄^⊥}ρ‖²; density: ρ_f ⊥ 𝒮(1,μ)⁺ and Π maps (𝒮(1,μ)⁺)^⊥ onto a dense subset of
𝒮(1,1)⁺ ⊖ 𝒮(1,μ)⁺; the intersection: ρ̂ constant on ℝ and in L² ⇒ ρ = 0. □
**Answer to (i), exact relation.** The exterior datum r_f is *not* itself Sonin; its gauge class is represented canonically
(minimal leak) by Πρ ∈ 𝒱_μ, a Sonin vector at level (1,1) orthogonal to the Sonin space at level (1,μ). The aliasing tail
Zr is the E-image of that class (Prop 2.1(b)). This is Landau–Pollak "double orthogonality" in Sonin form. Note: 𝒮(1,1) is
𝔉-stable, 𝒮(1,μ) is not (𝔉𝒮(1,μ) = 𝒮(μ,1)), so 𝒱_μ is **not** 𝔉-stable: the 𝔉-sectors of a carrier class leave 𝒱_μ.

## 3. Transfer identity (U.3) and its status
**Proposition U.3.1 (CONDITIONAL).** Assume (C1) 𝔔 is gauge-invariant along the L²-closure (𝔔[ρ] = 𝔔[Πρ]; true for C²
gauge by A_001 Prop 2.1, extension needs closability of 𝔔 on the form domain — OPEN), (C2) the radical lemma on 𝒮(1,1)
(= (H1) of AUDIT_5; CONDITIONAL). Write Πρ = σ + βe₀, σ ∈ 𝒮(1,1), e₀ ∈ 𝒮(1,1)⁺ ⊖ 𝒮(1,1), σ_± = (σ ± σ̂)/2. Then
 **𝔔[ρ] = 𝒲_refl[Ψ_{σ_+}] − 𝒲_refl[Ψ_{σ_−}] + E(ρ),  E(ρ) = 2β𝔔(σ,e₀) + β²𝔔[e₀],  ℓ(g) = λ(‖σ‖² + β²).**
*Proof.* (C1), bilinearity, T Thm 3.1 + Prop 3.3 on σ_± (𝒮(1,1) is 𝔉-stable). □
E is explicit up to the polar vector e₀ (ρ̂₀ ≠ 0, the AUDIT_4 rank-two polar defect lives here). Ψ_{σ} = Ψ_ρ is the
"Ψ_ρ" asked for in (i): it is a *difference* of two sector forms, never a single SOS.
**(ii) Reduction or REF-D.** Under (C1)–(C2): (★★) ⟺ ∀μ ≥ 5, on Π𝒞_μ ⊂ 𝒱_μ:
 𝒲_refl[Ψ_{σ_+}] − 𝒲_refl[Ψ_{σ_−}] + E ≥ κμ^{−A}(‖σ‖² + β²).
This is an exact restatement (every step an identity) — **REF-D**. Neither 𝒫 nor E is controlled; the minus sector contributes
−Σ_{j≥1}L_j(σ_−)² so the archimedean SOS is cancelled, not gained. What *is* gained (PROVED/CONDITIONAL as marked):
- **Monotonicity (PROVED).** 𝒞_μ ⊂ 𝒞_{μ′} for μ < μ′ (k ↦ dilate, supp shrinks), so κ_μ := inf 𝔔/‖Πρ‖² over 𝒞_μ is
  non-increasing; (★★) is a rate statement for the exhaustion 𝒱_μ ↑ 𝒮(1,1)⁺.
- **Status of T's 𝒮_− prediction upgraded (CONDITIONAL on C1, C2 and form-core density).** (★★) for all μ gives 𝔔 > 0 on
  ∪_μΠ𝒞_μ, dense in 𝒮(1,1)⁺ in L²; if this union is a form core, then 𝔔 ≥ 0 on 𝒮(1,1)⁺ and T's predictions hold in non-strict
  form on 𝒮_±. So AUDIT_5 §3 ("not a row-D falsifier") is replaced by: *falsifier of (★★) modulo C1, C2, core property*. Still
  not hand-decidable (Sonin vectors not explicit).
- **Dichotomy (CONDITIONAL on closability + core).** If each Π𝒞_μ is a core of the closed form on 𝒮(1,1)⁺, then κ_μ is
  μ-independent; any genuine μ-decay of κ_μ (as suggested by phase-199 numerics, NUMÉRICO, not re-run) therefore means the
  carrier classes are *not* cores, i.e. (★★) lives on the non-closable/boundary part of 𝔔 — OPEN which.

## 4. Falsifiers and constraints
- **cΛ.** U.2 is pure Fourier analysis (Λ-blind: same annulus). U.1.2 fails at c ≠ 1 (W_cΦ_f = (1−c)Σc_q(S+S^{−1})Φ_f ≠ 0), so
  both Thm U.1.3 and C1 (gauge invariance, A_001 Prop 2.1 uses ζ) break with defect linear in (1−c): the transfer identity
  breaks as required. **a_P**: same (Guo Lemma 4.4 needs the Euler product), ARGUED. **Beurling**: no Poisson ⇒ no 𝔉_μ, no
  U.1.1; U.2 survives (Fourier only) but the gauge is no longer radical. F-M_m: identities are class-blind; no sign claimed.
- Constraints: 14 (forced coefficients) respected — u_± use the full E-image; 15 (self-duality is a mirror, not a reduction)
  — confirmed: U.1.3 is the mirror at the edge, REF-D; 16 — addressed: transfer = projection onto 𝒱_μ (exact in L², form-level
  CONDITIONAL); 17 — canonical gauge fixed (orthogonal projection = minimal-leak representative; 𝔔 itself gauge-invariant).
  1–13: no step uses per-harmonic signs, PW decoupling, Hankel-CM as coercivity (the CM SOS is cancelled by the minus sector),
  or Sonin positivity as a sign source (W-Sonin, W11′).

## 5. Labels
| item | label |
|---|---|
| U.1.1 edge intertwining (𝔉_μ ↔ R_a) | PROVED (classical co-Poisson, scaled) |
| U.1.2 radical for f_± from Guo | PROVED (given CITED Guo 4.3/4.4) |
| U.1.3 sector formula on the carrier, W_T = ¼𝒲_refl[u_+] − ¼𝒲_refl[u_−] | PROVED; restatement of Guo Thm 4.5 |
| U.2.1 gauge⊥ = 𝒮(1,1)⁺, carrier closure = 𝒮(1,μ)⁺⊥, ℓ = λ‖Πρ‖², Sonin annulus | PROVED (L²) |
| U.3.1 transfer identity with E = 2β𝔔(σ,e₀) + β²𝔔[e₀] | CONDITIONAL (C1 closability, C2 = H1) |
| (★★) ⟺ annulus inequality | REF-D |
| κ_μ non-increasing | PROVED |
| T 𝒮_− prediction as (★★)-falsifier | CONDITIONAL (C1, C2, core) |
| core dichotomy | CONDITIONAL / OPEN |
| cΛ, a_P breaking | PROVED algebra / ARGUED |
| (★★), L′♯ | OPEN |
**Do not retry:** sector formula on the carrier as a sign source (the minus sector −SOS is forced: f_− ≠ 0 by Paley–Wiener);
projection onto Sonin space as a "reduction" of (★★) (it is the canonical gauge, REF-D). **Residual:** (★★_U) annulus
inequality; (C1) closability of 𝔔 on 𝒮(1,1)⁺; whether 𝒮(1,1) ⊖ (𝒮(1,μ)+𝒮(μ,1)) ≠ {0} (pure 𝒮_− vectors in the carrier).
No sign is claimed. Row D OPEN.
