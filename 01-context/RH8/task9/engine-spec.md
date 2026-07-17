# Validated Data — Localized Weil Detector (binding dataset) **Role.** Every number, definition, and target below is a validated reference value. Use these
directly: reproduce the zero lists from the stated generators and check them against the
validation gates, but do NOT rederive constants or re-discover function definitions. The
reference behavior in §4 is the expected output of a correct engine — use it to catch
implementation errors early. --- ## 1. Reference zeros (validation gate, mpmath dps=50)
- γ₁ = 14.134725141734693790…
- γ₂ = 21.022039638771554992…
- γ₃ = 25.010857580145688763…
Gate: `mpmath.zetazero(n)` imaginary parts must match to ≥9 digits. Fail ⇒ STOP. ## 2. The five controls — exact definitions **(1) ζ** — Riemann zeta. Zeros via `mpmath.zetazero`. Target list: 5000 zeros, dps=50. **(2) L(χ₄ mod 5)** — primitive complex Dirichlet character of order 4 mod 5:
χ(1)=1, χ(2)=i, χ(3)=−i, χ(4)=−1, χ(0)=0. Compute L(s,χ) via `mpmath` Hurwitz/L-series.
Target: 5000 zeros, dps=50. (validated against 129 LMFDB reference zeros, max diff 4.0×10⁻²⁸.) **(3) L_DH** — Davenport–Heilbronn. Construction (validated reference construction):
L_DH(s) = ((1−i)/2)·L(s,χ) + ((1+i)/2)·L(s,χ̄), with χ the primitive complex character mod 5
above (χ(2)=i) and κ ≈ 0.28407904384 the standard DH constant. **It is NOT multiplicative and
has no Euler product. It is the canonical RH-violator (off-line zeros).**
VALIDATION GATE (must hold to <10⁻⁶, three of four pass tightly; the (0.650786,114.163343)
point reads ≈4.0×10⁻⁵ — a documented transcription artifact, true zero at distance ≈4.4×10⁻⁵):
- (0.808517, 85.699348)
- (0.650786, 114.163343)
- (0.574355, 166.479306)
- (0.724258, 176.702461)
Newton-refined off-line zeros reach |L_DH|<10⁻⁴⁹ at Re(s)∈[0.574, 0.809]. Target: 5000 zeros. **(4) L(Δ,s)** — Ramanujan Δ L-function, weight-12 level-1 cusp form, LMFDB **1.12.a.a**.
L(Δ,s)=Σ τ(n) n^{−s}, analytically normalized so critical line is Re(s)=½. FROZEN — never
substitute. First zero (analytic norm): γ₁ = 9.2223793999211025 (matches LMFDB). Cost: PARI/GP
lfunzeros or mpmath, scales ~T⁴ — Target only 2000 zeros, dps=50 (N=5000 infeasible on 1 VM). **(5) ζ_δ deformation family** — ζ's zeros with the first m zeros shifted to Re(ρ)=½+δ
(imaginary parts unchanged). **Must shift the REAL part — imaginary-only shifts are invisible
(validated finding).** Parameters: δ∈{0, 10⁻³, 10⁻², 10⁻¹}, m∈{1, 5, 20}. The reference "strong"
control is δ=1.0 on the first 20 zeros; "small" is δ=0.1. ## 3. The localized Weil quadratic form Q (the central object)
Q = M_zeros − M_arith, the FULL explicit formula (zero side minus arithmetic side), NOT the
zero-side Gram matrix alone (that one is PSD by construction and carries no signal — a known error mode).
- Test functions: Hermite–Gauss, centered at T₀, width σ, basis dimension J.
- Arithmetic side MUST include: prime-power sum AND archimedean (gamma-factor) AND polar terms.
- Prime-power cutoff: use X=10⁵ (cutoff 10³ leaves a steep baseline α≈21 that swamps signal; 10⁵ + full archimedean suppresses GRH baseline ~2733 orders across J≤420 → 10²⁷ margin). ## 4. Engine reference behavior (reproduce these to validate the engine)
- At T₀=85.7, σ=2, J=10, dps=50: **L_DH λ_min ≈ −9.0×10⁴** (|λ_min|/tr(M_zeros) ≈ 1.7); ζ, L(χ), L(Δ) give |λ_min|/tr ≈ 10⁻⁸ to 10⁻¹⁰ (numerical floor, no false positives).
- **Locality:** away from T₀≈85.7, L_DH behaves like the controls. For ζ_δ, negativity appears only when T₀ lies within the shifted-zero window.
- **δ² scaling:** |λ_min| ∝ δ^α, α≈2.03 (R²=0.999) small-δ; at T₀=46.13, σ=1, J=12, dps=80 the asymptotic prefactor ≈610, so δ_min ≈ (|λ_min|/610)^{1/2}; reaches δ≈10⁻⁴.
- **J-amplification:** log|λ_min| ≈ 0.569·J·ln J; ~13 orders J=4→20 at δ=0.05; ~90 orders separation from control at J=20.
- **Optimal operating point:** T₀=46.13, σ=1, J=10. δ=0.05 detected for T₀∈[12.13, 82.13] at σ=1 (T₀∈[18.13, 80.13] at σ=2); detection fails outside the window or at over-broad σ. ## 5. ω-class moment fingerprint (side result, for reference)
ζ second-moment growth exponents (M_k ∝ (log N)^a): a≈5.9, 9.2, 11.3, 14.8, 19.3 for k=1..5 —
much larger than L(Δ) and L_DH (which cluster small). ζ fourth moment: 5.1% pure-class,
12.6% diagonal cross-class, **82.3% off-diagonal residual**; L(Δ) 56.5% diagonal-dominant,
L_DH 76.4%. Fractions do NOT converge in N (Erdős–Kac drift) — growth exponents are the robust
fingerprint, not fractions. ## 6. Environment
Preinstalled: mpmath 1.3.0, numpy 2.4.3, scipy 1.17.1, matplotlib 3.10.8, sympy 1.14.0.
Cost: ζ zeros dps=50 ≈ 22 ms/zero at small n, grows with index → 5000 ζ zeros ≈ 20–60 CPU-min.
L(Δ) zeros materially more expensive (~T⁴). Cache every zero list and Q matrix to disk. ## 7. Dead ends — do NOT revisit (established blind/negative by prior validated computation)
Jacobi inverse-spectral reconstruction (blind, ~10⁻¹⁰). Li coefficients (blind; λ₁…λ₂₀₀ stayed
positive despite 110 L_DH off-line zeros). Mercer/PSD-by-construction matrices (trivially
positive). TDA H0 persistence (δ²-insensitive; L_DH NOT an outlier at matched sample, p=0.50).
Zero-side-only Gram matrix (PSD by construction — a positive-by-construction artifact, no signal).
