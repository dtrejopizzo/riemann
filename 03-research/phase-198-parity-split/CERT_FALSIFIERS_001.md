# CERT_FALSIFIERS_001 — interval certification of the BARRIER_Y_001 and AA_001 negative Rayleigh quotients

**Status: PROVED (rigorous interval arithmetic, mpmath.iv, 60 digits, outward rounding).** Script
`scripts/cert_falsifiers.py`, output `scripts/cert_falsifiers_out.txt`. Corpus check: index entries BARRIER_Y_001,
AA_001 (README of ROUTES-TRIED-INDEX); no prior interval certificate for deletions or odd-sector falsifiers (the
½log5 certificate of Paper 46 thm:log5A certifies a lower bound, not these witnesses). This memo builds no new route;
it upgrades labels of existing falsifiers.

## Statement
For each row below there is an explicit F ∈ P_T (both Tate moments exactly 0; odd F in the AA rows) with
𝔞_T^{(a)}(F)/‖F‖² inside the stated interval, hence < 0. Since λ_A ≤ 𝔞_T(F)/‖F‖² for every F ∈ P_T, the bottom of
the form with the comb a is negative at that window (for the AA rows, also μ_odd < 0).

| witness | T | comb a | sector, basis | enclosure of 𝔞_T(F)/‖F‖² |
|---|---|---|---|---|
| Y1 delete q=3 | 0.75 | Λ − δ_3 | full, deg ≤ 13 | [−0.232424631, −0.2324246066] |
| Y1 delete q=3 | ½log5+0.01 | Λ − δ_3 | full, deg ≤ 13 | [−0.3851829765, −0.3851829492] |
| Y1 top-layer q=7 | 1 | Λ − δ_7 | full, deg ≤ 13 | [−0.04016566175, −0.04016562122] |
| Y1 top-layer q=8 | log3 | Λ − δ_8 | full, deg ≤ 13 | [−0.01792785057, −0.01792784628] |
| AA zero comb | ½log5 | 0 | odd, x¹…x²³ | [−0.002665265111, −0.00266525746] |
| AA zero comb | 1 | 0 | odd | [−0.2224671275, −0.2224671214] |
| AA a_2 (p=2 deleted) | 1 | Λ·1_{p≠2} | odd | [−0.5227839785, −0.5227839763] |
| AA 2Λ | 1 | 2Λ | odd | [−1.046524616, −1.046524612] |
| AA a_3 (extra) | ½log5 | Λ·1_{p≠3} | odd | [−0.1587799643, −0.1587799518] |
| AA 1.15Λ (extra) | 1 | 1.15Λ | odd | [−0.1526059164, −0.1526059126] |

(Y1 row at log3 is at T = log3 exactly; n = 9 is not a contact since log 9 = 2T. The q=3, T=0.75 and
½log5+0.01 values agree to 10⁻⁸ with the independent 30-digit quadrature of `phase-197/scripts/y001_mp_check.py`.)

## Method (checked against P46 eq:Aform, thm:S(iii), C₀ as in P46 §log5)
𝔞_T(F) = C₀c(0) + ∫₀^{2T}(c(0)−c(u))K(u)du + c(0)∫_{2T}^∞K − Σ_{log n<2T} v_n c(log n), v_n = 2a(n)/√n,
c(u)=∫F(t)F(t−u)dt, K(u)=½/sinh(u/2)+½/cosh(u/2)=2Σ_k e^{−(2k+½)u}, C₀=−γ−π/2−3log2−logπ.
1. Test function: F(t)=G(t/T), G polynomial; G chosen as the (non-rigorous) Galerkin minimiser, coefficients
   rationalised to denominator 2⁴⁰ except the coefficients of x⁰,x¹ (full) or x¹ (odd).
2. Tate moments imposed exactly: those coefficients are the interval solution of ∫G e^{±Tx/2}=0 (resp.
   ∫G sinh(Tx/2)=0, which for odd G gives A=B=0); moments ∫x^j e^{cx} by Taylor series with remainder
   4|c|^{121}/121!. The enclosure therefore holds for the exact F ∈ P_T.
3. c(Ts)=TΣ g_j g_k ∫_{−1+s}^1 x^j(x−s)^k dx, exact rational polynomials in s ∈ [0,2].
4. ∫₀^{2T}u^rK = 2Σ_k γ(r+1,a_kL)/a_k^{r+1}: k<3000 exact (positive series with geometric remainder, or
   complement form), k≥3000 by integral comparison [∫_N^∞f, f(N)+∫_N^∞f] (f decreasing), exponentially small
   incomplete part (<e^{−4000}) absorbed in the enclosure.
5. ∫_{2T}^∞K = log coth(T/2) + 2 arctan e^{−T}, arctan by alternating series with remainder.
6. Comb: interval Horner at s=log n/T; contact set decided by interval comparison.
Labels: enclosures PROVED. Galerkin minima themselves (the bottoms λ_A, μ_odd) remain NUMÉRICO; only the
upper bounds λ_A ≤ (enclosure) < 0 are PROVED.

## Addendum (fase 200): testigo 11 — Epstein x²+5y²
| 11 | Epstein Z_Q, Q = x²+5y² (h=2; Γ_ℝ(s)Γ_ℝ(s+1), conductor 20, peine 2Λ_Q(n)/√n) | T = 159/100, G par grado 56, denominadores 2^280 | 𝔞_T^Q(F)/‖F‖² ∈ [−0.0599398587, −0.0599398456] | PROVED (intervalos) | 03-research/phase-200-sign-object/LEMMA_E_EPSTEIN_001.md + _data/ |
Propiedad separadora: defecto cuadrático de producto de Euler Λ_cosh (restricción C-E). Negatividad para todo T ≥ 1.59 por Lema M.
| 12 | Davenport–Heilbronn F_DH (χ mod 5 impar, χ(2)=i, κ=0.2840790; Γ_ℝ(s+1), conductor 5; sin Euler, sin polo) | T = 9/5, sector impar ⊥ sinh(t/2), Legendre grado ≤ 259, coef. diádicos 2^60, 7000 bits arb | 𝔞_T^{DH}(F)/‖F‖² ∈ [−7.05197470947908e−9 ± 4e−25]; completo −2.3799e−7; T=2 impar −0.7519368254 | PROVED (arb) | 03-research/phase-200-sign-object/CERT_DH_001.md + _data/ |
Reproduce a Ziad (−6.169e−9, mismo sector/ventana). Testigo concentrado en ξ ≈ 84.5 (cero fuera en t ≈ 85.7). Negativo ∀T ≥ 9/5 por Lema M. T_DH sin cota inferior (numérico [1.6,1.8]).
