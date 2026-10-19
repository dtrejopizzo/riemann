# R168_201: the degree-2 carrier (Euler products that see the quartet frequency)

Phase 168, lead rank 2 of R168_001. Pure mathematics, no numerics. Single pass.
Inputs: R168_001 (§ rank 2, walls E1/W4), R168_190, R167_101 ((WS*), Thm B, Prop W, Thm C), R167_102 (Thm B′),
R166_190 §0, R166_802, R163_401, phase 37 Doc 111 §3 (anti-Siegel). Labels: PROVED / PROVED-CITED / ARGUED / OPEN.
No label of record moves.

**Corpus check (rule ).**
- Doc 111 §3.2 already showed that the dlVP/Mertens product (3+4cos+cos2) for ζ is the Siegel mechanism transported, and that it yields only the classical zero-free region.
- Doc 111 §3.3(a) already showed that ζ·ζ = ζ² adds nothing.
- New here: the shifted pair L_γ = ζ(s+iγ)ζ(s−iγ) and the four-factor product ζ²L_γ, plus the exact statements D2-1 to D2-6 below. R168_001 calls this family "degree 2". Note that (b) has degree 4.

---

## 0. Outcome

**Status: CLOSED NEGATIVE.** Every route stops at a named wall. Nothing open with content survives.

| # | Statement | Label |
|---|---|---|
| D2-1 | Translation identity: the Weil functional of L_γ is ζ's Weil functional on the modulated test. The prime, archimedean and pole terms all match exactly. | PROVED (explicit formula PROVED-CITED) |
| D2-2 | GRH for L_γ ⟺ RH for ζ. Weil positivity of L_γ at type T follows from ζ's at type T (wall E1, exact). | PROVED |
| D2-3 | First contact: T₂(L_γ) ≥ T_c(ζ). Height 0 does not shorten the window. The on-line density at height 0 is (1/π)log(γ/2π), twice ζ's density at γ. | PROVED |
| D2-4 | The "real off-line zero" is the double zero of L_γ(σ) = \|ζ(σ+iγ)\|² ≥ 0. There is no sign change, so Landau/Pringsheim has no leverage. | PROVED |
| D2-5 | Positivity of (b) and of its relatives is the triangle inequality. The best one-sided bound from any non-negative cosine polynomial is Re S_γ ≤ c·S₀ (+ sums at kγ, k ≥ 2), with c ≥ 1/2 up to the Fejér constant. This is the trivial order X^{1/2}, while (WS*) needs B ≍ Y^δ/δ (wall W4 + R167 Prop W). | PROVED |
| D2-6 | Deuring–Heilbronn at β = ½+δ is vacuous: the repulsion needs (1−β)·log Q < 1, i.e. δ > ½ − O(1/log γ). That region is dlVP, already excluded. | PROVED-CITED (Linnik/DH form) + PROVED |
| (c) | ζ(s)ζ(s−2iγ) = L_γ(s−iγ) is a vertical translate of (a). It is the same functional. | PROVED |

---

## 1. Case (a): L_γ(s) = ζ(s+iγ)ζ(s−iγ), with γ = γ_q

**1.1 Coefficients (PROVED).**
- a(n) = Σ_{de=n} d^{−iγ} e^{iγ} = Σ_{d|n} (n/d²)^{iγ}. This is real, since the substitution d ↦ n/d conjugates each term.
- a(p) = 2cos(γ log p), and a(n) = n^{iγ}σ_{−2iγ}(n).
- −L_γ′/L_γ(s) = Σ Λ(n)·2cos(γ log n)·n^{−s}. The coefficients change sign.
- L_γ is the standard L-function of the Eisenstein series E(·, ½+iγ) on GL(2), shifted.
- It is **not** in the Selberg class: it has simple poles at 1 ± iγ, not at 1.

**1.2 Zeros (PROVED).**
- Each zero ρ of ζ gives zeros ρ ∓ iγ of L_γ.
- The quartet ½±δ±iγ_q therefore gives zeros at ½+δ and ½−δ. Each has multiplicity **2**: one copy comes from each factor (ρ = ½±δ+iγ via s+iγ = ρ, and ρ̄ via s−iγ = ρ̄).
- The quartet also gives zeros at ½±δ±2iγ.

**1.3 Theorem D2-1 (translation identity; PROVED).** Let Ψ be admissible for (1.1) of R167_101, with type ≤ T. Then
  Σ_{ρ(L_γ)} Ψ(t_ρ) = Σ_{ρ(ζ)} [Ψ(t_ρ−γ) + Ψ(t_ρ+γ)] = W_ζ[Ψ(·−γ) + Ψ(·+γ)].
- The prime side Λ(n)·2cos(γ log n)·Ψ̌(log n) is exactly the transform of the modulated test.
- The gamma factor Γ_R(s+iγ)Γ_R(s−iγ) gives Ω(t−γ) + Ω(t+γ).
- The poles at 1±iγ give Ψ(i/2 ∓ γ)-terms, which are ζ's pole term on the shifted tests.
- Modulation by 2cos(γu) does not change the u-support. *Proof:* term-by-term from the Hadamard products. ∎

**1.4 Theorem D2-2 (E1, exact; PROVED).**
- Translation by ±iγ maps the critical line to itself and off-line zeros to off-line zeros. Hence GRH(L_γ) ⟺ RH(ζ).
- At the level of forms: e^{iγu}(f∗f̃)(u) = (e_γ f)∗(e_γ f)~. Therefore
  W_{L_γ}(f∗f̃) = W_ζ(g₊∗g̃₊) + W_ζ(g₋∗g̃₋), where g_± = e_{±γ}f and the type is unchanged.
- So positivity of the degree-2 form at type T is a *consequence* of ζ's at type T. Certifying it up to T (which needs γ_q, and γ_q is unknown) is never weaker than certifying ζ. ∎

**1.5 Theorem D2-3 (no gain at height 0; PROVED).**
- If W_{L_γ}(f∗f̃) < 0 at type T, then by D2-2 one of W_ζ(g_±∗g̃_±) < 0 at type T. Hence T₂ ≥ T_c.
- The converse can fail. Pulling ζ's witness F back as f = e_{−γ}F gives W_ζ(F∗F̃) + W_ζ(e_{−2γ}F∗…), and the second term (a test centred at height 2γ) is an uncontrolled positive "sea" of size ≍ (L/π)·I. So T₂ > T_c is possible.
- The analytic conductor of L_γ at t = 0 is ≍ (γ/2π)². The density of zeros there is (1/2π)·2log(γ/2π): zeros of ζ near +γ arrive through one factor, their conjugates through the other. The Landau window is therefore at the same scale T_L ≈ log γ, with **double** the on-line mass.
- "Height 0" is a relabelling of height γ, not a new regime. ∎

**1.6 Proposition D2-4 (no Siegel configuration; PROVED).**
- For real σ, L_γ(σ) = ζ(σ+iγ)·conj(ζ(σ+iγ)) = |ζ(σ+iγ)|² ≥ 0.
- The zero at ½+δ is a tangential double zero of a non-negative function.
- Siegel/Landau arguments need a sign change of a real function forced against a positive Dirichlet series. Here the coefficients a(n) are not ≥ 0, and there is no sign change to exploit. ∎

## 2. Case (b): F(s) = ζ(s)²ζ(s+iγ)ζ(s−iγ)

This product has degree 4, not 2.

**2.1 Structure (PROVED).**
- log F = Σ Λ(n)(2+2cos(γ log n))/(n^s log n), with coefficients ≥ 0. Hence the Dirichlet coefficients satisfy b(n) ≥ 0.
- Poles: order 2 at s = 1, and simple poles at 1±iγ.
- Zeros: ½±δ (multiplicity 2, from L_γ), ½±δ±iγ (multiplicity 2, from ζ²), and ½±δ±2iγ.
- F(σ) = ζ(σ)²|ζ(σ+iγ)|² ≥ 0 on (½,1). Landau's lemma locates only the real singularity at σ_c = 1, and nothing below it.
- F is the Rankin–Selberg square of the Eisenstein series up to ζ(2s): L(E_{γ/2}⊗E_{γ/2}) = ζ²(s)ζ(s+iγ)ζ(s−iγ)/ζ(2s).

**2.2 The only output of positivity (PROVED-CITED; Doc 111 §3.2).**
- Take −Re F′/F(σ) ≥ 0 for σ > 1, with the Hadamard expansion.
- The zero at β = ½+δ contributes 2/(σ−β) ≤ 2/(½−δ) = O(1) when σ > 1.
- The archimedean and conductor terms are ≍ log γ, and the pole budget is 2/(σ−1).
- The inequality is violated only if 1−β ≪ 1/log γ, which is exactly dlVP.
- The real zero near ½ sits at distance ½−δ from the pole, deep inside the "ocean" of Doc 111 §3.4. Positivity buys nothing there. ∎

**2.3 Theorem D2-5 (W4, exact; PROVED).** Let w ≥ 0 on the prime side, and write S_k := Σ Λ(n)n^{−1/2}cos(kγ log n)w(log n), with S₀ > 0. For any cosine polynomial P(θ) = a₀ + Σ_{k≥1} a_k cos kθ ≥ 0 with a₁ ≠ 0, positivity gives Σ a_k S_k ≥ 0.
- (i) If a₁ > 0, this is a **lower** bound on S₁ (the dlVP/(b) orientation).
- (ii) If a₁ < 0, it gives S₁ ≤ (a₀S₀ + Σ_{k≥2} a_k S_k)/|a₁|.
- By Fejér–Egerváry, |a₁| ≤ 2a₀cos(π/(N+2)) < 2a₀. So the constant in front of S₀ is > 1/2. The S_k for k ≥ 2 are twisted sums at heights kγ, and nothing controls them.
- Hence the best upper bound has trivial order S₀ ≍ Y^{1/2}. The case P = 1−cos θ, i.e. (2−2cos) = |1−n^{iγ}|², is the triangle inequality.
- (WS*) needs Re S < B with B ≤ 2c_Θ Y^δ w(0)/δ (R167_101 Thm C). This is polylogarithmic in γ_q (Cor D), and requires Y^δ > 1.04·δX^{1/2} (Prop W).
- The deficit is a factor X^{1/2−δ}/polylog. **No positive-coefficient Euler product closes it.** This is the same blindness as R167_102 Thm B′: a coefficient-sign constraint cannot see the phase of n^{iγ_q}. ∎

**2.4 D2-6 (Deuring–Heilbronn; PROVED-CITED + PROVED).**
- The DH/Linnik repulsion from an exceptional real zero β of an L-function of conductor Q is quantified by λ = (1−β)log Q. For example, other zeros satisfy 1−β′ ≥ c·log(c′/λ)/log Q, and this is only non-trivial for λ < c′.
- Here Q ≍ γ², so λ ≍ 2(½−δ)log γ. That is < c′ only for δ > ½ − O(1/log γ), the dlVP zone (Doc 111 §3.2).
- This answers R168_001 summary: "witness-scale DH repulsion" from degree-2 positivity does not exist. The required (H-sep) stays unsupplied, as R163_603 says. ∎

## 3. Case (c)

ζ(s)ζ(s−2iγ) = L_γ(s−iγ), so D2-1 to D2-4 apply verbatim. Twisting by Dirichlet characters adds only (q-aspect) conductor and does not change any orientation.

## 4. Ledger and wall

- **E1** (D2-2): the degree-2 Weil positivity *is* RH for ζ at the same type. It is implied by ζ's positivity, never weaker. Identification is exact (D2-1: same functional, modulated test).
- **Window** (D2-3): at height 0, T₂ ≥ T_c, and the on-line mass is doubled.
- **W4** (D2-5): positivity of coefficients gives either a lower bound, or an upper bound of trivial order Y^{1/2}. (WS*) needs an upper bound at the scale Y^δ/δ.
- **Siegel/DH** (D2-4, D2-6): the real zero is tangential; the repulsion is vacuous outside dlVP. This confirms Doc 111 Prop 3.1.
- **Exact stop.** A carrier would need coefficients whose *sign* correlates with the phase of n^{iγ_q} beyond the cosine-polynomial class. Any such sign information is a statement about the twisted sum itself, i.e. (WS*) restated (R167_102 Thm B′).
- Lead rank 2 of R168_001: **CLOSED NEGATIVE.** Open items: none new.
