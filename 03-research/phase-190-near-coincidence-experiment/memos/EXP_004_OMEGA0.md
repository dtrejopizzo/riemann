# EXP_004 — (Ω₀): the clamped ground-state test on T ∈ [0.40, 1.10], with controls

Object (index R2; L2_BUILD_008 §1–§3, 009 §2): P_T = (¼ − ∂²)H²₀(I_T); G₀ = clamped ground mode minimising the archimedean form
𝔞_∞(F)/‖F‖² over F = (¼−∂²)G, G ∈ H²₀(I_T); φ₀ = (¼−∂²)G₀, ‖φ₀‖ = 1; μ₀(T) = 𝔞_∞(φ₀); h_T = c_{φ₀} (autocorrelation);
S_T(a) := Σ_n v_n^{(a)} h_T(log n), n < e^{2T}; margin 𝔞_T(φ₀) = μ₀ − S_T. (Ω₀) as stated in R2: S_T(Λ) < 0 for T > ½log5; the
sharper single-vector statement 𝒯₀: 𝔞_T(φ₀) ≥ 0.

## Method (scripts/omega0.py; NUMÉRICO)
Galerkin on G_j(t) = (1 − t²/T²)²P_j(t/T), j even, j < 2N (N = 14 and 20; the ground mode is even), F_j = (¼−∂²)G_j exact polynomials;
cross-correlations c_ij(u) by Gauss–Legendre exact for polynomials; 𝔞_∞ by the Lévy form C₀⟨F_i,F_j⟩ + ∫₀^{2T}(c_ij(0) − c_ij^{even}(u))K(u)du +
c_ij(0)·∫_{2T}^∞K (thm:S(iii)), 200 Gauss nodes on [0, 2T] (integrand smooth after cancellation of the 1/u singularity); Gram cutoff
10⁻¹³ (polynomial basis is ill-conditioned). Convergence: N = 14 vs 20 agree on μ₀ to 1.4·10⁻⁴ and on S_T(Λ) to 2.3·10⁻⁴ (absolute).
The full-form Galerkin bottom on the same space (last column of the log) is an upper bound for λ_A(T) and is NOT resolved below ≈ 10⁻⁴
(it reads −1.4·10⁻⁵ at T = 0.70, a basis artefact; the certified value there is positive, Paper 46 thm:log5A / Zhu to 0.8); it is quoted
only as a consistency check at T ≤ 0.6 (2.3·10⁻¹ at 0.40, 1.2·10⁻² at 0.50, 5.3·10⁻⁵ at 0.60). The (Ω₀) margins are 10²–10³ above this noise.

## Results (N = 20; S/margin = S_T(a) / 𝔞_T(φ₀))
| T | μ₀(T) | Λ | a₃ | a₅ | amp2(0.05) | amp2(0.5) | pert₂(+10⁻²) | pert₂(−10⁻²) | Poisson 0 | Poisson 1 | Poisson 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.40 | +0.403 | +0.135/+0.268 | 0/+0.403 | 0/+0.403 | +0.142/+0.261 | +0.204/+0.199 | +0.137/+0.266 | +0.134/+0.269 | +0.020/+0.383 | 0/+0.403 | 0/+0.403 |
| 0.45 | +0.284 | +0.204/+0.080 | 0/+0.284 | 0/+0.284 | +0.214/+0.070 | +0.308/**−0.024** | +0.206/+0.078 | +0.202/+0.082 | +0.207/+0.077 | +0.081/+0.203 | 0/+0.284 |
| 0.50 | +0.178 | +0.138/+0.040 | 0/+0.178 | 0/+0.178 | +0.145/+0.033 | +0.208/**−0.031** | +0.139/+0.038 | +0.137/+0.041 | +0.525/**−0.347** | +0.200/**−0.022** | +0.053/+0.125 |
| 0.55 | +0.081 | −0.010/+0.091 | +0.000/+0.081 | 0/+0.081 | −0.011/+0.092 | −0.016/+0.097 | −0.010/+0.091 | −0.010/+0.091 | +0.619/**−0.538** | +0.220/**−0.139** | +0.190/**−0.109** |
| 0.60 | −0.007 | −0.086/+0.079 | +0.095/**−0.102** | 0/**−0.007** | −0.095/+0.088 | −0.178/+0.171 | −0.088/+0.081 | −0.084/+0.077 | +0.432/**−0.439** | +0.139/**−0.146** | +0.364/**−0.371** |
| 0.65 | −0.089 | −0.130/+0.042 | +0.205/**−0.294** | 0/**−0.089** | −0.148/+0.059 | −0.302/+0.213 | −0.134/+0.045 | −0.127/+0.038 | +0.055/**−0.143** | +0.069/**−0.157** | +0.436/**−0.524** |
| 0.70 | −0.164 | −0.198/+0.033 | +0.258/**−0.422** | 0/**−0.164** | −0.221/+0.057 | −0.432/+0.267 | −0.203/+0.038 | −0.193/+0.029 | −0.353/+0.188 | +0.019/**−0.184** | +0.385/**−0.550** |
| 0.75 | −0.235 | −0.264/+0.028 | +0.236/**−0.471** | 0/**−0.235** | −0.292/+0.056 | −0.541/+0.306 | −0.269/+0.034 | −0.258/+0.023 | −0.694/+0.459 | −0.059/**−0.176** | +0.298/**−0.534** |
| 0.80 | −0.302 | −0.348/+0.046 | +0.153/**−0.455** | 0/**−0.302** | −0.378/+0.076 | −0.652/+0.350 | −0.354/+0.052 | −0.342/+0.040 | −0.998/+0.696 | −0.178/**−0.124** | +0.160/**−0.461** |
| 0.85 | −0.365 | −0.402/+0.038 | +0.088/**−0.453** | +0.056/**−0.420** | −0.434/+0.069 | −0.718/+0.354 | −0.409/+0.044 | −0.396/+0.031 | −1.274/+0.909 | −0.328/**−0.036** | +0.025/**−0.389** |
| 0.90 | −0.424 | −0.440/+0.016 | +0.041/**−0.465** | +0.147/**−0.571** | −0.472/+0.048 | −0.757/+0.333 | −0.447/+0.022 | −0.434/+0.010 | −1.523/+1.098 | −0.494/+0.070 | −0.145/**−0.279** |
| 0.95 | −0.481 | −0.498/+0.017 | −0.017/**−0.464** | +0.228/**−0.709** | −0.529/+0.048 | −0.806/+0.325 | −0.504/+0.023 | −0.492/+0.011 | −1.742/+1.261 | −0.617/+0.136 | −0.346/**−0.135** |
| 1.00 | −0.535 | −0.566/+0.030 | −0.078/**−0.457** | +0.297/**−0.832** | −0.595/+0.060 | −0.859/+0.323 | −0.571/+0.036 | −0.560/+0.025 | −1.925/+1.390 | −0.634/+0.099 | −0.534/**−0.002** |
| 1.05 | −0.587 | −0.613/+0.026 | −0.115/**−0.472** | +0.373/**−0.960** | −0.641/+0.053 | −0.887/+0.299 | −0.619/+0.031 | −0.608/+0.020 | −2.072/+1.484 | −0.611/+0.023 | −0.736/+0.149 |
| 1.10 | −0.637 | −0.657/+0.020 | −0.164/**−0.473** | +0.419/**−1.056** | −0.682/+0.045 | −0.908/+0.270 | −0.662/+0.025 | −0.652/+0.015 | −2.178/+1.541 | −0.592/**−0.046** | −0.962/+0.325 |

## Reading
* μ₀(T) crosses zero between T = 0.55 and 0.60 (consistent with Paper 46 thm:index/cor:Tarch: archimedean bottom positive on (0, 0.58], negative
  from 0.60). From T = 0.55 on, S_T(Λ) < 0: (Ω₀) HOLDS for Λ on [0.55, 1.10] (NUMÉRICO), with margin 𝔞_T(φ₀) ∈ [0.016, 0.091], minimum 0.016 at
  T = 0.90 and no monotone trend (0.079, 0.042, 0.033, 0.028, 0.046, 0.038, 0.016, 0.017, 0.030, 0.026, 0.020): the single-vector test is
  comfortably positive, 10²–10³ above its numerical noise, in sharp contrast with λ_A(T) itself (10⁻⁸ at log 2).
* Controls: a₃ fails from T = 0.60 (margin −0.10 → −0.47), a₅ from T = 0.60 (its comb is empty below ½log5 so its margin is μ₀ < 0 exactly
  as thm:finmod(i)); Poisson combs fail at various T (seed 0: 0.50–0.65; seed 1: 0.50–0.85 and 1.10; seed 2: 0.55–1.00). amp2(0.5) fails at
  T = 0.45, 0.50 and PASSES for T ≥ 0.55 with a margin larger than Λ's (because h_T(log 2) < 0 there, so extra mass at 2 helps this one test).
  **amp2(0.05) and the 10⁻² perturbations pass (Ω₀) at every T with margins within ±25 % of Λ's.**
* Classification: (Ω₀) separates Λ from the structural controls (a_P, Poisson) but not from amplification/perturbation controls that
  fail window positivity (amp2(0.05) is indefinite on A_M from M = 50, EXP_002); it is a necessary condition only, as R2 states (L2_007 §3,
  rem:bar-loc). It carries no ζ-specific content beyond what cor:void allows: its truth for Λ on [0.55, 1.10] is a NUMÉRICO fact at
  margin ≥ 0.016, not a structure.
* No new sub-route attempted on R2 (admissible direction "one explicit Weil sum per window using an individual property of Λ" untouched);
  the data say that any such proof must produce a margin of order 10⁻² at T ≈ 0.9 while being insensitive to 10⁻²-level changes of
  one weight — i.e. it must come from the bulk of the comb, not from the first atoms.
