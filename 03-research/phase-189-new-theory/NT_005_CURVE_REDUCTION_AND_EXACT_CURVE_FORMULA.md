# NT_005 — Curve reduction of the height symbol and its exact formula: coprime counting × (archimedean + Euler) main term
# + integer-discreteness remainder

Phase 189, construction step 5 (P189.1). Notation of NT_001–004 (after the referee fixes).
Neutral names only.

## Corpus check
grep "ζ(2σ−1)", "coprime", "Euler–Maclaurin" + "Dirichlet", "|ζ(σ+iτ)|²" + "Weil", "curve θ_p = τ log p": hits — NT_002 Prop 2.3
(curve pairing stated, not evaluated); L2_028 §2(c), N_022 §4 (the one-parameter diagonal sees Arch and Near); L2_025 §3
("explicit Euler × FE spectral density on Re s > 1": a positive density D_σ paired with a profile — different: no height,
no coprime counting, no remainder); R160_PD_R1 Lemma 2.1 / phase-108 108_91 (FE on the line: Re(−ζ′/ζ)(½+iy) = ½m(y),
"ζ′/ζ(s) + ζ′/ζ(1−s) is prime-free"). **New:** Thm 5.1 (min over 𝕋^∞ = inf over the curve), Thm 5.2 (exact decomposition
Φ_σ∘ι = (ζ(2σ−1)/ζ(2σ))·Re[F̂₀(z)²(m(z) + 2ζ′/ζ(w))] + Re ℛ_σ), Prop 5.3 (remainder analytic for σ > 0), Cor 5.4 (meromorphic
continuation of the curve symbol to σ > 0).

## 1. Curve reduction (PROVED)
**Thm 5.1.** For σ > 3/2: m(σ) = min_{𝕋^∞}Φ_σ = inf_{τ₀∈ℝ}Φ_σ(ι(τ₀)). Hence D(σ) ⟺ Φ_σ(ι(τ₀)) ≥ 0 for all real τ₀.
*Proof.* ι(ℝ) is dense in 𝕋^∞ (the log p are ℚ-linearly independent: unique factorization; Kronecker, CITED) and Φ_σ is continuous
(NT_002 Prop 2.1). ∎
So in the continuous regime the whole torus collapses to ONE real variable; the Bohr characters that matter are the curve characters
χ(m) = m^{−iτ₀}, i.e. the tests are the modulated ζ-tests Σ_m m^{−σ−iτ₀}τ_{log m}F₀.

## 2. Exact curve formula (PROVED for σ > 3/2)
Put s := σ + iτ₀, w := s − ½, z := −τ₀ + i(σ − 1) (so that ∫f(u)e^{(1−s)u}du = f̂(z) with f̂(τ) = ∫f e^{iτu}).
Analytic continuations: F̂₀(z)² = ĉ₀(z) (entire; double zeros at ±i/2), m(z) := ½[ψ(w/2) + ψ((1−w)/2)] − log π (so m(z) = m(τ₀) at σ = 1).
**Thm 5.2.** For σ > 3/2 and τ₀ ∈ ℝ,
  Φ_σ(ι(τ₀)) = (ζ(2σ−1)/ζ(2σ))·Re{F̂₀(z)²[m(z) + 2(ζ′/ζ)(w)]} + Re ℛ_σ(τ₀),
  ζ(2σ)ℛ_σ(τ₀) := Σ_{k≥1}k^{−σ+iτ₀}[E_k^A(s) − Σ_{n≥2}v_nE_{kn}^c(s)],
where E_L^A(s) := Σ_{m≥1}m^{−s}A(log m − log L) − L^{1−s}Â(s) and E_L^c(s) := Σ_{m≥1}m^{−s}c₀(log m − log L) − L^{1−s}Ĉ(s) are the
integer-discreteness defects (sum over ℕ minus integral over (0, ∞)), Â(s) := ∫A(u)e^{(1−s)u}du = m(z)F̂₀(z)²,
Ĉ(s) := ∫c₀(u)e^{(1−s)u}du = F̂₀(z)².
*Proof.* By NT_002 Prop 2.3, ζ(2σ)Φ_σ(ι(τ₀)) = Σ_{m,k}m^{−s}k^{−s̄}B(log m − log k) (curve character χ(m) = m^{−iτ₀}; absolutely convergent).
Split B = A − comb, the comb written one-sidedly under Re (NT_004 Thm 4.1 proof). For fixed k (resp. k, n) write the m-sum as integral +
defect: ∫_0^∞x^{−s}A(log x − log k)dx = k^{1−s}Â(s) (substitution x = ke^u; A decays like e^{−5|u|/2} by L2_023 Lemma C, so the integral
converges for −3/2 < σ < 7/2… in particular here), and likewise for c₀ at L = kn. The main terms sum to Σ_k k^{−s̄}k^{1−s}[Â(s) −
Ĉ(s)Σ_nv_nn^{1−s}] = ζ(2σ−1)[Â(s) − Ĉ(s)·2(−ζ′/ζ)(w)] (k^{−s̄+1−s} = k^{1−2σ}; v_nn^{1−s} = 2Λ(n)n^{−w}), all absolutely convergent for
σ > 3/2. Â(s) = m(z)F̂₀(z)²: A has spectral symbol mF̂₀², continued to Im z = σ − 1 (|σ − 1| < 5/2; the poles of m at z = ±i/2 are cancelled
by the double zeros of F̂₀²); and ¼ ± iz/2 equal (1−w)/2, w/2. Φ_σ is real, so take real parts. ∎

## 3. The remainder (PROVED with routine Euler–Maclaurin bookkeeping)
**Prop 5.3.** For each fixed τ₀, σ ↦ ℛ_σ(τ₀) extends to a real-analytic function on σ > 0, with
|ζ(2σ)ℛ_σ(τ₀)| ≤ C(F₀)(1 + |s|)²[ζ(2σ+1) + ζ(2σ+1)·(−ζ′/ζ)(σ + 3/2)·…] (finite for σ > 0).
*Proof.* E^c_L: f(x) = x^{−s}c₀(log x − log L) is C² with support in [L/2, 2L] (L ≥ 2): Euler–Maclaurin of order 2 gives |E^c_L| ≤ (1/12)∫|f″|
≤ C(1 + |s|)²L^{−σ−1}. E^A_L: f(x) = x^{−s}A(log x − log L) on [1, ∞) plus ∫_0^1 (which is O(L^{−5/2}) for σ < 7/2): boundary terms O(L^{−5/2})
and ∫_1^∞|f″| ≤ C(1 + |s|)²L^{−σ−1}. Hence the k-, n-sums are dominated by Σ_k k^{−2σ−1}(1 + Σ_n v_nn^{−σ−1}) = ζ(2σ+1)(1 + 2(−ζ′/ζ)(σ + 3/2)),
locally uniformly in σ > 0 and in s in compacts; each term is analytic in s. ∎
**Cor 5.4 (continuation of the curve symbol).** The right side of Thm 5.2 defines a function Φ^{curve}_σ(τ₀), meromorphic in σ > 0 (fixed τ₀),
whose only possible singularities are: σ = 1 (pole of ζ(2σ−1)), and the points where (ζ′/ζ)(w) has poles (w = σ − ½ + iτ₀ a zero or the
pole of ζ; the pole at w = 1, i.e. σ = 3/2, τ₀ = 0, is cancelled by the double zero of F̂₀(z)² at z = i/2). For σ > 3/2 it equals Φ_σ∘ι.
**Prop 5.5 (D ⟹ the continuation is the symbol).** If D holds, then for σ > 1, Φ_σ := Q_σ ⋆ μ₀ is continuous and Φ_σ∘ι = Φ^{curve}_σ.
*Proof.* Under D, Φ_σ(ι(τ₀)) = ∫Q_σ(ι(τ₀) − φ)dμ₀(φ) is real-analytic in σ > 1 (Q_σ = Π_p local Poisson factors, analytic in σ, dominated);
two real-analytic functions agreeing on σ > 3/2 agree on σ > 1 away from the (discrete) singularities. ∎

## 4. What uses what (requirement check)
- **Integrality:** the factor ζ(2σ−1)/ζ(2σ) is the count of coprime pairs (k^{1−2σ} after the m-integral; ζ(2σ) from the common factor)
  and ℛ is the discreteness of ℕ (Euler–Maclaurin) — both exact.
- **Euler product:** (ζ′/ζ)(w) = −Σ Λ(n)n^{−w}, and the product structure of Q_σ.
- **FE:** not yet used — Thm 5.2 holds with m(z) + 2ζ′/ζ(w) for any comb (replace −ζ′/ζ by its Dirichlet series). NT_006 inserts the FE.
- **Class status:** Thm 5.1–5.2 and Prop 5.3 hold for every comb (formula with L_a in place of −ζ′/ζ). Λ-specificity enters in NT_006.

## 5. Review
- Thm 5.1: density of the curve needs ℚ-independence of {log p} — immediate from unique factorization; continuity from ℓ¹. ✓
- Thm 5.2: interchange of the m-integral main terms with the k-, n-sums requires absolute convergence of Σ_k k^{1−2σ} and Σ_nv_nn^{1−σ}:
  σ > 3/2 ✓. The real-part step: the double series is real (B even, Hermitian), the split into main + defect is not symmetric, so only the
  real part of each piece is asserted. ✓ Sign conventions for z checked against ∫c₀(u)e^{(1−s)u}du = ĉ₀(−i(1−s)) and −i(1−s) = z. ✓
- Prop 5.3: C² regularity of c₀ and A (ĉ₀ = O(τ^{−4}); Â = O(τ^{−4}log τ)) ✓. The bound grows like |τ₀|²: ℛ is NOT uniformly small in τ₀;
  for large |τ₀| it contains the diagonal a₀ and the Riemann–Siegel-type range m ≲ |τ₀|. Stated as such.
- Prop 5.5 is conditional on D (labelled); used only as an implication.
- No numerics; **no sign contact**.

## Erratum note (after NT_005_007_REVIEW)
(1) Thm 5.2, Prop 5.3, Cor 5.4 hold for 3/2 < σ < 7/2 (resp. 0 < σ < 7/2): Â(s) = ∫A(u)e^{(1−s)u}du converges only for |σ − 1| < 5/2.
(2) Prop 5.3: for σ > 3/2 the A-defect is O((1 + |s|)²L^{−min(σ+1, 5/2)}); the sums still converge.
(3) Prop 5.5 wording: under D every singularity of Φ^{curve}_σ in 1 < σ < 7/2 is removable and the continuation equals Φ_σ∘ι.
