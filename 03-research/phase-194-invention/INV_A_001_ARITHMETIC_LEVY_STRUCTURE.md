# INV_A_001 — The arithmetic Lévy structure: one object, atoms + Γ_ℝ density, coupled by reflection

Track A, phase 194. Labels: DEFINITION / PROVED / CITED / CONJECTURE / HEURISTIC / OPEN.
Pen and paper. **No negative value for ζ found or certified.** Notation of CA_I_001 §0 and P47 (μ_T = c_Tδ₀ + K du − Σ v_nδ_{log n},
v_n = 2Λ(n)n^{−½}, 𝒫_T = {∫F e^{±t/2} = 0}).

## 0. The observation that makes the two data one
Classical (CITED): for Re s > 1,
  −ζ′/ζ(s) = Σ_n Λ(n) n^{−s} = ∫_0^∞ e^{−su} dJ_f(u),  J_f := Σ_n Λ(n) δ_{log n};
  −½ψ(s/2) = γ/2 + ∫_0^∞ (e^{−su} − e^{−2u}) dJ_∞(u),  dJ_∞(u) := du/(1 − e^{−2u})   (from ψ(z) = −γ + ∫(e^{−t} − e^{−zt})/(1−e^{−t})dt, t = 2u).
Hence for Λ(s) := π^{−s/2}Γ(s/2)ζ(s), Re s > 1:
  **−Λ′/Λ(s) = C₀ + ∫_0^∞ (e^{−su} − e^{−2u}𝟙_{∞}) dJ(u),  J := J_f + J_∞**   (0.1)
(compensator only on the continuous part; C₀ = ½log π + γ/2). Integrating in s from σ₀ > 1:
  log [Λ(σ+it)/Λ(σ)] = ∫_0^∞ (e^{−itu} − 1) e^{−σu} dJ(u)/u.   (0.2)
**Consequence (PROVED from (0.2)).** For every σ > 1, φ_σ(t) := Λ(σ+it)/Λ(σ) is the characteristic function of an infinitely
divisible law (a compound/pure-jump law of −X, X ≥ 0) with Lévy measure
  **L_σ(du) = e^{−σu} u^{−1} [ Σ_n Λ(n)δ_{log n} + du/(1 − e^{−2u}) ]**   on (0,∞).   (0.3)
The finite atoms Λ(n)/log n (Khinchine's ζ-distribution) and the a.c. density 1/(u(1−e^{−2u})) (the log-Γ_ℝ law) are the jump
and the continuous jump intensity of ONE subordinator, the **arithmetic Lévy process** 𝕏^σ. (L_σ is a Lévy measure: ∫min(1,u)L_σ < ∞
since the density ~ 1/(2u²)·u = 1/(2u) near 0 — wait: density e^{−σu}/(u(1−e^{−2u})) ~ 1/(2u²) at 0, so ∫min(1,u)L_σ diverges
logarithmically: 𝕏^σ is NOT a subordinator of finite variation but needs the compensator in (0.1)/(0.2) — (0.2) is fine as written
because e^{−itu} − 1 = O(u) and ∫_0^1 u·u^{−2}du diverges only logarithmically… CORRECTION: ∫_0^1 |e^{−itu}−1| u^{−2}du ~ ∫|t|/u du
diverges. So (0.2) must be read with the drift compensator: log φ_σ(t) = −i t b_σ + ∫(e^{−itu} − 1 + itu𝟙_{u<1}) L_σ(du). PROVED in this
form (it is the Lévy–Khintchine form; ∫min(1,u²)L_σ < ∞).) The a.c. part is precisely the Γ_ℝ Lévy density of CA_I_001
(ν(u) = κe^{−u/2}/(1−e^{−2u}) is u·L_{1/2}-density restricted to the continuous part, i.e. σ = ½ is the window line).

## 1. DEFINITION (the class 𝔐 and the internal relation R)
A **pure arithmetic Lévy structure** is a positive measure J = Σ_{n≥2} a_n δ_{log n} + du/(1 − e^{−2u}) on (0,∞) with
 (M1) a_n ≥ 0, Σ a_n n^{−σ} < ∞ for σ > 1 (atoms on log ℕ, positive: the Lévy measure (0.3) is positive);
 (M2) a.c. part EXACTLY the Γ_ℝ density (purity);
 (M3) define Λ_J(s) := exp(∫ (e^{−su} … ) ) by (0.1)–(0.2) (Λ_J = π^{−s/2}Γ(s/2) f_J(s), f_J(s) := exp Σ a_n n^{−s}/log n, a Dirichlet
      series Σ b_n n^{−s}, b_1 = 1, since exp of a Dirichlet series without constant term is one);
 (R)  **internal relation:** s(s−1)Λ_J(s) continues to an entire function of finite order and **Λ_J(s) = Λ_J(1−s)**.
In Lévy language (R) says: the Lévy exponent Ψ_J(s) = log Λ_J(s) of 𝕏 (a function of the damping σ = Re s) continues from the
half-plane of infinite divisibility σ > 1 and is invariant under s ↦ 1 − s. Neither half of J can satisfy (R) alone: J_∞ alone gives
π^{−s/2}Γ(s/2) (not reflective), J_f alone gives ζ (not reflective). **(R) is the coupling: the reflection maps the jump comb onto
the continuous density** (theta inversion is its Mellin shadow).
𝔐 := {J satisfying (M1),(M2),(R)}.

## 2. Theorem 1 (ζ ∈ 𝔐; CITED classical) J_ζ = Σ Λ(n)δ_{log n} + du/(1−e^{−2u}): (M1)(M2) by §0, (R) Riemann.

## 3. Theorem 2 (rigidity: 𝔐 = {J_ζ}; PROVED modulo CITED Hamburger)
*Proof.* Let J ∈ 𝔐. f_J = Σ b_n n^{−s} converges absolutely for σ > 1 (exp of an absolutely convergent series). (R) gives
π^{−s/2}Γ(s/2)f_J(s) = π^{−(1−s)/2}Γ((1−s)/2)f_J(1−s) with (s−1)f_J entire of finite order. Hamburger's theorem (1921; Titchmarsh
§2.13, CITED) ⇒ f_J = b_1 ζ = ζ. Taking logarithms in σ > 1 and comparing Dirichlet coefficients: Σ a_n n^{−s}/log n = log ζ(s) =
Σ Λ(n)n^{−s}/log n ⇒ a_n = Λ(n). ∎
**Reading.** CA_I_001 Cor 6 was a separation (a property set); Thm 2 is a rigidity: the coupled object has exactly one point. The
"atoms ⇄ density" coupling is not a constraint among many — it determines the atoms from the density.
**Corollary 2.1 (falsifier classes excluded; PROVED unless marked).**
- Beurling systems (atoms on log of a Beurling set ≠ ℕ): violate (M1) by definition; also no FE in general.
- a_P perturbations / amplified combs (atoms on log ℕ, a_n ≠ Λ(n), a_n ≥ 0): violate (R) by Thm 2.
- Quartets / rational FE-symmetric twists E: Λ·E has Lévy exponent with an extra signed density Σ_j ±e^{α_j u}/u (from log(s−α) =
  −∫(e^{−(s−α)u} − e^{−u})du/u), so (M2) fails (purity lost) — PROVED for E with zeros/poles left of σ = 1 (Laplace rep valid for
  σ > max Re α_j); the general E: ARGUED.
- Epstein ζ_Q (Γ(s)(2π)^{−s}): a.c. density 1/(1−e^{−u}) ≠ 1/(1−e^{−2u}) — (M2) fails. PROVED.
- ζ_K, [K:ℚ] = d > 1: a.c. density (r₁ + r₂)/(1−e^{−2u}) + r₂e^{−u}/(1−e^{−2u}) ≠ Γ_ℝ density — (M2) fails. PROVED.
- Dirichlet L(s,χ), χ ≠ 1: atoms Λ(n)χ(n) not ≥ 0 — (M1) fails; Γ_ℝ(s+1) for odd χ also fails (M2). PROVED.

## 4. The positivity built into 𝔐
**Prop 4.1 (infinite divisibility off the strip; PROVED).** For σ > 1, t ↦ φ_σ(t) is positive definite (§0). By (R) and real
coefficients, Λ(σ'+it) = Λ(1−σ'−it) = conj Λ(1−σ'+it); so for σ' < 0, φ_{σ'}(t) = [Λ(1−σ')/Λ(σ')]·conj φ_{1−σ'}(t), and
Λ(σ') = Λ(1−σ') > 0: φ_{σ'} is again an infinitely divisible characteristic function. **(R) transports Lévy positivity from σ > 1 to
σ < 0.** The strip 0 ≤ σ ≤ 1 is the only place where 𝔐 does not hand positivity for free.
**Prop 4.2 (odd harmonic symbol; PROVED).** Let ξ(s) = ½s(s−1)Λ(s) and H(σ,τ) := Re ξ′/ξ(σ+iτ) (harmonic off the zeros).
(i) H(σ,τ) > 0 for σ > 1 (Hadamard: ξ′/ξ = Σ_ρ 1/(s−ρ) symmetrically summed, Re 1/(s−ρ) > 0 when σ > Re ρ, and Re ρ < 1; CITED classical).
(ii) (R) ⇒ ξ′/ξ(s) = −ξ′/ξ(1−s) ⇒ **H(1−σ,τ) = −H(σ,τ)**: H is odd about the window line; H(½,τ) = 0 away from ordinates. This is
CA_M_001 (m + 2Re ζ′/ζ = 0 on the line) re-derived as a parity statement: on the line the a.c. symbol is exactly cancelled
and the window form lives entirely on the singular (jump) part of H across σ = ½.
**Prop 4.3 (window form = jump of the Lévy symbol; PROVED as an identity, HEURISTIC as a reading).** Define the **Lévy-damped
window form** 𝔞_T^{(ε)}(F) := ∫ c_F(u) e^{−ε|u|} dμ_T(u) (all atoms n^{−½} → n^{−½−ε}, density K → Ke^{−ε|u|}; c_Tδ₀ unchanged).
Its Fourier symbol is the Poisson extension P_ε ∗ μ̂_T, i.e. the symbol of the explicit form on the line σ = ½ + ε; 𝔞_T^{(0)} = 𝔞_T.
Since P_ε = e^{−ε|D|} is the Cauchy semigroup (the ½-stable subordination of the heat semigroup), 𝔞^{(ε)} is the window form of
the **subordinated** structure: ε is subordination time.

## 5. Candidate theorem and attack
**CONJECTURE Θ (Lévy descent).** For J ∈ 𝔐 (i.e. ζ) and every T > 0, ε ↦ 𝔞_T^{(ε)}(F) is ≥ 0 on 𝒫_T for all ε ≥ 0; in particular
λ_A(T) ≥ 0. Stronger form Θ⁺: for F ∈ 𝒫_T, ε ↦ 𝔞_T^{(ε)}(F) is completely monotone on (0,∞) (a Laplace transform of a positive
measure in ε — a Bernstein/CM structure forced by subordination).
**Attack.**
Step 1 (PROVED-direction, large ε): for ε large the comb part is ≤ 2(−ζ′/ζ)(½+ε)‖F‖² → 0 while the damped arch form is
m(0)‖F‖² + ∫ν(u)e^{−εu}∫(F(t)−F(t+u))² ≥ m(0)‖F‖². Gap G1: m(0) sign/normalization with damping and the polar contribution
under damping (on 𝒫_T, F̂(±i/2) = 0, but P_ε∗(polar atoms) does not vanish on 𝒫_T for ε > 0: the polar term returns with weight
∝ Re 1/((ε∓½)... ) — must be computed). So "𝔞^{(ε)} ≥ 0 for ε ≥ ε₀" is OPEN as stated, PROVED for the unconstrained form after
adding back the polar term only for ε > ½ (Prop 4.2(i) via Hadamard, all ρ have Re ρ < 1 < ½ + ε).
Step 2 (the descent, the real content): show the set {ε : 𝔞^{(ε)} ≥ 0 on 𝒫_T} is an interval [0,∞) — i.e. no sign change as
subordination time decreases. Θ⁺ would give it at once (CM functions positive at ∞ in the limit are ≥ 0 everywhere). Tool: Lévy
side, 𝔞^{(ε)}(F) = ∫c_F e^{−εu}dJ-terms + arch — each atom contributes −2Λ(n)n^{−½}c_F(log n)e^{−ε log n}: an exponential in ε with
SIGNED coefficient c_F(log n). So 𝔞^{(ε)}(F) = A₀(F) + ∫_0^∞ e^{−εu} dρ_F(u) with ρ_F = signed measure (c_F·μ_T). Θ⁺ ⟺ ρ_F ≥ 0 —
FALSE in general (c_F(log n) has both signs, R165_202). **Θ⁺ is FALSE as stated for single F** (PROVED: choose F ∈ 𝒫_T with c_F(log 2)
large positive and c_F small elsewhere; then ρ_F has a negative atom at log 2 and the ε-derivative of order k has the wrong sign
for large k). Θ (plain positivity, not CM) survives.
Step 3 (where R must enter): by Prop 4.2(ii) the symbol of 𝔞^{(ε)} on line ½+ε equals −(symbol on ½−ε): **𝔞^{(ε)} + 𝔞^{(−ε)} = 0
up to the singular part** (𝔞^{(−ε)} = anti-damping, comb n^{−½+ε}). So the family ε ↦ 𝔞^{(ε)}(F) is odd modulo a singular
contribution S_F(ε) concentrated at the zero ordinates; 𝔞^{(0)}(F) = ½[S_F(0⁺) − S_F(0⁻)] = half the jump. Θ at ε = 0 ⟺ the jump
of the subordinated form across ε = 0 is ≥ 0 on 𝒫_T. Gap G2 (the exact gap): R fixes the ODD part of the ε-family; the sign lives in
the jump, which R does not constrain — R is a parity, positivity needs a monotonicity. The missing tool is a **one-sided maximum
principle for the harmonic H on the half-strip ½ < σ < 1 restricted to |F̂|²-averages with F ∈ 𝒫_T** (H > 0 on σ ≥ 1, H = 0 on
σ = ½ off ordinates: a harmonic function positive on the boundary of the half-strip is positive inside — exactly what is needed —
but the boundary σ = ½ carries the singular part, whose sign is the question). Gap G3: the window localisation (supp F ⊂ [−T,T])
is not preserved by the Poisson family in τ; the damped forms live on all of L² — need the restriction to 𝒫_T to commute with
subordination (OPEN; plausible via the semigroup property P_ε P_η = P_{ε+η} only on the spectral side).
Retry flag: Step 3 is the Lévy rewriting of P47 Theorem Z ("one-sided smoothing"); the new elements are Thm 2 (rigidity) and the
subordination/parity reading Prop 4.2–4.3.

## 6. Status
PROVED: (0.3) arithmetic Lévy measure; Thm 2 rigidity 𝔐 = {ζ} (Hamburger CITED); exclusions Cor 2.1 (quartets general: ARGUED);
Prop 4.1, 4.2; Θ⁺ false. CONJECTURE: Θ. OPEN: G1 (damped polar term), G2 (jump sign — one-sided maximum principle), G3
(window ↔ subordination). No negative value for ζ.

**Compliance.** to classify, rank or stop;
no "E1"; positivity assumed true; the obstruction G2 is recorded as a tool to invent, not as a stop. Θ has ζ as its only instance
in 𝔐 by Thm 2 — recorded as a feature of the object (rigidity), and the toolbox target is the one-sided maximum principle of G2.
