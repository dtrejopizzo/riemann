# AUDIT_195_2: audit of INV_Q_001 and INV_R_001 (phase 195)

Audit. Checked against Paper 46 (eq:symbol/eq:form, λ_A, 𝒫_T),
INV_L_001 L1/L3 and AUDIT_195 (P2 holds only on ½<σ<1). Script: AUDIT_195_2_r1_check.py.

## (a) R1 (log-free Green identity): VERIFIED, plus NUMÉRICO
- Derivation: for holomorphic f, Δ|f|²=4|f′|², so ∫_{½}∂_σ|f|² = ∫_{σ_1}∂_σ|f|² − 4𝓓(f). On σ=½ we have |ρ_S|=e^{d_S}=1, so
  ∂_σ(|ρΦ|²−|Φ|²) = |F̂|²∂_σe^{2d_S} = 2|F̂|²∂_σd_S = 4|F̂|²∂_σu_S. The last step uses ∂_σd_S = u_σ(s)+u_σ(1−s̄) = 2u_σ on the line.
  With L1 (∫4∂_σu|F̂|² = 4π𝔞_T for S⊇S_N, verified in AUDIT_195 (a)), the constants 1/π and 1/4π are correct. The second (v_S) form
  also checks: Δv_S = 2|ρ′|², v_S=0 on the line, the outward normal is −∂_σ, and ½∂_σ|ρ|² = 2∂_σu.
- The "exact Taylor step" is the chain rule ∂_σe^{2d} = 2e^{2d}∂_σd evaluated at d=0. It is exact, and no expansion is involved.
- Domain: ρ_S is holomorphic on σ>0 (poles of ξ_S lie on σ≤0), and its zeros are at 1, 1+2πik/log p, 3, 5, …. Neither zeros nor P2 are
  used. **R1 therefore holds for every σ_1>½, not only σ_1<1.** The restriction σ_1<1 is harmless. It matters only for R3 (|γ_2^{−1}| bound).
- NUMÉRICO: T=0.6, S={2,3}=S_N, F=(1−(t/T)²)⁴, σ_1=0.85, |τ|≤80. LHS (L1) −0.47943144959477, RHS (R1) −0.47943144959460, agreement
  1.7e−13. This also matches the L3 value −0.4794314 of AUDIT_195. Label: R1 PROVED + NUMÉRICO.

## (b) Normalization lemma: the "only if" is FALSE as stated
- "If" is correct: when |hξ_S|=1 on σ=½, the flux equals 4π𝔞_T.
- "Only if" fails for two independent reasons. (i) Band-limited invisibility: |F̂|² has Fourier support in [−2T,2T]. Exact recovery for
  all F∈C_c^∞(I_T) therefore forces only (|hξ_S|²−1)∂_σu_S to have vanishing Fourier transform on (−2T,2T), not to vanish pointwise.
  This is the same mechanism as L1 (atoms n≥N are invisible). (ii) Free gauge: h=I/ξ_S^# with I any zero-free holomorphic function with
  |I|=1 on σ=½. For example, I=exp(iΣc_n(n^{s−½}+n^{½−s})) with c_n real can be indexed by arbitrary ℤ-data. The weight is
  |I|²(|ρ_S|²−1), and |I|≠1 off the line, so **the weight does not factor through ρ_S alone**. The interior identity is R1 applied to IΦ.
- Correct statement (PROVED): in the class h=I/ξ_S^#, every such identity equals R1 with Φ replaced by IΦ, and the arithmetic content of the
  weight is ρ_S modulo a gauge I that the line does not see. "Forced factorization through ρ_S" is PROVED only for I≡1 with pointwise
  flux matching. Otherwise it is FALSE.

## (c) R4 (Hermite–Biehler): VERIFIED
- Γ_R′/Γ_R(σ) = −½logπ + ½ψ(σ/2) < 0 on (0,1), since ψ(σ/2) < ψ(½) ≈ −1.96. Hence d_∞(σ)<0 on (½,1).
- d_p(σ) = log(1−p^{σ−1}) − log(1−p^{−σ}) < 0, because σ−1 > −σ. This is correct for every p and every Beurling q>1.
- Reverse-HB fails at large |τ|: d_∞ ~ (σ−½)log(|τ|/2π) while Σd_p is bounded for fixed S. PROVED.
- The τ_0 asymptotic remains ARGUED, because it uses the real point as the worst case heuristically.

## (d) Q1/Q2
- **Q1(a) is mis-stated.** ℓ_S(½+iτ) = 2i·arg ξ_S is not small, and x_S = ρ_S−1 runs over the circle |1+x|=1 on the line. NUMÉRICO
  (S = primes<30, τ≤50): max|x_S| = 1.999999 on σ=½. The mean-value bound controls Re ℓ = d_S, not x_S. Consequently "|x_S|≤½ on the layer
  σ−½≲e^{−T}" is FALSE. The conclusion "no linear regime" survives in a stronger form: the expansion fails already on the line.
  Q1(b) (d_{S_N}(σ) → −∞ on real (½,1)) is PROVED.
- Q2a: re-derived (both branches σ<1 and σ>1). Re-ran the 14-digit check: max error 3.3e−16 at p∈{2,3,7} and the four stated points.
  Q2b: ∫|ĝ_σ|²cos(uτ)dτ = 2πR_σ(u) holds. Since supp R_σ⊂[−2T,2T], only p^k≤e^{2T} enter, with weight 1/k = Λ/log. PROVED.
  Q2 is an identity that does not depend on P2, so the AUDIT_195 domain restriction does not affect it. The statement that the p≥N Jensen
  term cancels against its sources is ARGUED.
- Q3 (place-additive, therefore surviving Beurling and O_6) is PROVED as structure. The NO-GO for 𝒦_mix stands.

## (e) The combined claim: ARGUED, not PROVED
The claim reads: "any exact identity for 𝔞_T factors through ∏γ_v, hence is O_6-stable; ℤ-specific info enters only via an inequality."
- PROVED in the narrow class: weights |hξ_S|²−|hξ_S^#|² with h=1/ξ_S^# (I≡1) and pointwise flux matching (R1/R2), and log-weights d_S (Q2/Q3).
- FALSE as a general statement, by (b): the gauge I and the band-limited freedom allow exact identities whose weights carry arbitrary
  ℤ-indexed data. These are gauge-trivial on the line, as in the INV_H gauge collapse, but they do not "factor through ρ_S".
- The part "ℤ-specific only via an inequality" is a meta-claim with no theorem behind it: ARGUED.
- R3's inference that O_P(1) cannot distinguish a_P from ℤ is also ARGUED. The ratio bound is PROVED, but the WP sign change of a_P at
  T≥0.60 is itself an O(1) effect. Separately, R3 cites the D-side e^{cT} size as "CITED (AUDIT item 4)". The size is ARGUED
  (AUDIT_195 (b)3), not CITED.

## Net
R1 is a correct and new exact identity (PROVED + NUMÉRICO 1e−13), valid for all σ_1>½. R4 and Q2 are correct. Two corrections: the
normalization lemma "only if" is false (gauge I and band-limit), and Q1(a) is mis-stated (|x|≤2 on the line). Claim (e) is
PROVED only in 𝒦_R(I≡1) ∪ 𝒦_mix; in general it is ARGUED, and FALSE as worded. Live residue sharpened: a gauge I (unimodular on σ=½) carrying
ℤ-data, making 𝓓(IΦ)−𝓓(IρΦ) signed on 𝒫_T. Its positivity is REF-D unless the choice of I supplies the input. No sign. Row D: OPEN.
