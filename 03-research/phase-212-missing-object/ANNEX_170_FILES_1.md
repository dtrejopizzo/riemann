# Annex 170 — files, stretch 1 (R170_000 to R170_822)

File-by-file reading of `03-research/phase-170-global-prime-inequality/`, from R170_000 to
R170_822 inclusive (30 memos). The folder **contains no README.md** (checked with `ls`). Cross-check
against the terrain not excluded by round 1 of phase 212:
(T1) continuous squares with the arithmetic in the index or in the dilation weights;
(T2) factorization of type [log gcd(i,j)] = E diag(Λ) Eᵀ as a Gram model;
(T3) total identification of Λ by Σ_{d|n}Λ(d) = log n converted into a quadratic bound;
(T4) common residue: converting the mixed pairings of the finite Poisson–Chebyshev identity
(H_{M,N}, E_N) into Σ_{k>N} h(k)|ℓ_k(F)|² with h ≥ 0.

Common notation of phase 170: W_T(F) = (1/2π)∫m|F̂|² + 2Re(A(F)B̄(F)) − Σ_{2≤n<e^{2T}} (2Λ(n)/√n) Re c_F(log n),
m(τ) = Re ψ(1/4+iτ/2) − log π, A(F)=∫F e^{t/2}, B(F)=∫F e^{−t/2}; c(t)=cosh(t/2), s(t)=sinh(t/2);
m₀ = m(0) = −γ_E − π/2 − 3log2 − logπ < 0; k(u) = e^{−u/2}/(1−e^{−2u}). Several memos use the
Poisson–Chebyshev (PC) operator of P46: S_N A_M 𝓕 = {X,E_N} − L_M*E_N − JH_{M,N} − H_{M,N}𝓕, with
H_{M,N} = Σ_{k>N} h_{M,N}(k) k^{−1/2} τ_{log k}, h_{M,N}(k) = Σ_{dm=k, d≤M, m≤N} Λ(d) ≥ 0.

General remark: the memos are written in English; several use an external equivalence (R163_401
Thm 1.2; P45 Theorem F); it is recorded neutrally and not developed.

---

## Non-.md files in the folder (no analysis)

- `archimedean_transfer_diagnostics.json` — numerical output of the cross-check of the archimedean transfer (R170_807/808).
- `coherent_paths_diagnostics.json` — Galerkin diagnostics of the path series (R170_301).
- `contact_response_diagnostics.json` — central differences and artificial contact (R170_401).
- `gamma_detector_bridge_diagnostics.json` — diagnostic of the Gamma moment detector (R170_702).
- `multiplicative_compensation_diagnostics.json` — checks of the compensation by modulation (R170_501).
- `nonlocal_storage_diagnostics.json` — checks of the Stein equation / nonlocal storage (R170_601).

There are no `.py` scripts in the folder: the `verify_*.py` cited by the memos (301, 401, 501, 601, 805, 807,
810, 812) are not present.

---

## 1. Entries by file

### R170_000 — Global target and effective dependencies
- **Object.** Self-contained statement of W_T(F) ≥ 0 on 𝒟_T = {F ∈ L²(−T,T): ∫log(2+|τ|)|F̂|² < ∞}; outside
  𝒟_T the archimedean term equals +∞. Lists dependencies: certified range T ≤ ½log5 (P46 thm:log5W,
  imported); "first contact" T_c as contact with zero, not a strict counterexample; Theorem M (P48
  thm:M(b)) as an asymptotic upper bound on normalized infima, not as an equivalence; "twisted"
  reduction (R167_101 Thm B) conditional on (Dom_θ), small regime and (WS*).
- **Labels.** Declared OPEN. Uses an external equivalence (R163_401 Thm 1.2). Sustained: it is a
  statement and an inventory; there is no proof of its own.
- **Stops.** Contributes no sign and does not extend the range; the twisted-sum route remains conditional.
- **Corrected by.** Not indicated.
- **T1–T4.** Touches none (mentions Eratosthenes as an exact identity without sign, R169_101/190).

### R170_101 — Domain, real tests, and scale quantifier
- **Object.** (§1) Extended form well defined: |c_F| ≤ ‖F‖², c_F(u)=0 for |u|≥2T, |2Re(AB̄)| ≤ 4 sinh T ‖F‖²,
  m(τ) − log(2+|τ|) bounded (DLMF 5.11.2). (§2) W_T(f+ig) = W_T(f)+W_T(g). (§3) W_S(F)=W_T(F) for S ≥ T;
  a sequence T_j → ∞ suffices. (§4) Σ_{n≤Y}Λ(n)a(n) = Σ_{dm≤Y} μ(d) log m a(dm).
- **Labels.** Declared PROVED (elementary). Sustained: yes, the four pieces are correct and elementary.
- **Stops.** §4: Möbius inversion is not a sum of squares; μ and the real part of the weights have no
  sign. Coincides with R169_101.
- **T1–T4.** Touches T3: yes, weakly — writes Λ = μ∗log as an exact identity and records that it gives no sign;
  does not convert it into a quadratic bound.

### R170_201 — Prime channel construction
- **Object.** In L²(ℝ), U_p translation by log p, r_p = p^{−1/2}, V_p = Σ_{k≥1} log p · r_p^k U_p^k,
  C_p = 2ℓ_p r_p/(1−r_p), b_p = ℓ_p r_p(1+r_p)/(1−r_p), D_p = √b_p (I−U_p)(I−r_pU_p)^{−1}.
  Prop. 1: D_p*D_p = C_p I − (V_p+V_p*). Assembly ⊕_p: ‖𝒟_P F‖² = C_P‖F‖² − 2Σ_p Σ_k (log p/p^{k/2}) Re c_F(k log p),
  and W_T = ‖𝒟_P F‖² + R_P(F), R_P = 𝔞_∞ + 2Re(AB̄) − C_P‖F‖². Theorem 2: the constant C_P is optimal
  (symbol q_P(0)=C_P). Truncated version (4): C_N^min‖F‖² − 2Re⟨V_N F,F⟩ = Σ_{n≤N} (Λ(n)/√n)‖F−U_nF‖².
  (5) R_P(F) → −∞ as P grows (Σ1/p diverges).
- **Labels.** "Construction and obstruction proved". Sustained: yes. Theorem 2 covers factorizations of the
  same operator with constant compensation, not τ-dependent or compressed compensations.
- **Stops.** The remainder R_P has no sign and diverges to −∞; the construction works for arbitrary
  dilations a_j > 1 and weights ℓ_j > 0, hence does not use the factorization of ℤ (implicit falsifier: any
  system of positive weights).
- **Corrected by.** No; R170_301 replaces it with the common coupling.
- **T1–T4.** Touches T1: yes — continuous squares ‖D_pF‖² with arithmetic in the index (channel per prime) and weights
  log p·p^{−k/2} in the dilation; fails because of divergent diagonal compensation C_P and genericity in the weights.
  T2/T3/T4: no.

### R170_202 — Hidden network audit
- **Object.** Network energies E(y) = Σ c_ij|y_i−y_j|² + Σκ_i|y_i|², c_ij, κ_i ≥ 0, with variational elimination of
  hidden vertices. Inherited property E_eff(|x|) ≤ E_eff(x) ⇔ E_eff(f,g) ≤ 0 for f,g ≥ 0 of disjoint support.
  Counterexample: kernel h(u) = 2cosh(u/2) − e^{−u/2}/(1−e^{−2u}); h(log(3/2)) = (7/10)√(2/3) > 0; with two
  bumps in (−1/2,1/2) one has W_{1/2}(f,g) > 0.
- **Labels.** "Class obstruction proved; precedent 106.13". Sustained: yes (I verified h(u₀)).
- **Stops.** Class NO-GO: no scalar network with positive conductances (with hidden vertices)
  represents W in physical coordinates while preserving the modulus. Does not cover matrix channels with phases or
  signed couplings.
- **T1–T4.** No (it is a Dirichlet/Beurling–Deny type representation, not arithmetic in the index).

### R170_301 — Coherent archimedean paths
- **Object.** Γ_T(F) = (1/2π)∫(m−m₀)|F̂|² = ∫₀^∞ k(u)‖F−S_uF‖² du (1); Γ_T ≥ α_T I, α_T = 2[artanh(e^{−T})+arctan(e^{−T})].
  E_T = Γ_T + 2A_T I − J_T + 2|c⟩⟨c|, C_T = b_T I + 2|s⟩⟨s|, b_T = 2A_T − m₀, with A_T = Σ a_n, a_n = Λ(n)/√n;
  ⟨E_TF,F⟩ = Γ_T + Σ a_n‖F−S_{log n}F‖² + 2|⟨F,c⟩|² (5); W_T = ⟨E_TF,F⟩ − ⟨C_TF,F⟩ (6).
  Theorem 1: ‖R_T‖ ≤ r_T = 2A_T/(2A_T+α_T) < 1 and Neumann series for E_T^{−1} (7)–(8). Theorem 2:
  W_T ≥ 0 ⇔ K_T = C_T^{1/2}E_T^{−1}C_T^{1/2} ≤ I ⇔ ‖𝒯_T‖ ≤ 1 (11). (12) K_T = Σ_j L_j*L_j,
  L_j = (I+R_T)^{1/2}R_T^jY_T, with tail bound (13). Target rewritten (14): Σ_j‖L_jx‖² ≤ ‖x‖².
- **Labels.** "Unconditional construction; sign OPEN". Sustained: yes; (14) is an exact reformulation.
- **Stops.** The contraction (14) does not follow from the construction. Explicit falsifier: T=1,
  F = 1_{(−1,1)}/√2, a₂ = 100 gives W < 5+16−100 = −79 (I verified c_F(log2) = 1−log2/2 and Γ₁(F) < 5); the series converges
  all the same. r_T → 1 as T grows: there is no uniform margin.
- **T1–T4.** Touches T1: yes — (5) is a sum of continuous squares with arithmetic weights Λ(n)/√n in the
  translations; the sign stays in the subtracted term C_T. Fails because the form is "squares − constant"
  and everything is generic in the weights (large-a₂ falsifier).

### R170_401 — Contact response and divisor coordinates
- **Object.** Derivative of the generalized eigenvalue C f = κ E f: κ̇ = 2(1−κ)s_d‖f‖² + κ⟨H_d f,f⟩ (2); at contact
  κ̇ = 2Σ d_n Re c_f(log n) (4). Theorem 1 (second-order tangency): if PDP = 0 and QDP ≠ 0,
  W_ε(f+εg) = −ε²q − ε³⟨Dg,g⟩ (5), hence W−εD is not ≥ 0 for small ε of either sign; Cor.: two-sided
  robustness ⇔ DP = 0 (6). §4 divisor coordinates: e_m = Σ_{d|m}λ_d − log m, λ_n − Λ(n) = Σ_{d|n}μ(n/d)e_d (7);
  response (8)–(9) with Σ_k μ(k)k^{−1/2} H_{dk}.
- **Labels.** "Identities and local criterion proved; sign OPEN". Sustained: yes (Schur computation;
  §3 conditional on contact hypotheses). Numerical data (positive derivatives, q ≈ 15.46) are NUMERICAL.
- **Stops.** "Decisive limit": imposing e_m = 0 ∀m ≤ N determines λ = Λ uniquely; a curve that
  preserves all the identities at fixed T is constant. (8)–(9) measure the response to violating the identity, not the
  sign at the exact point.
- **T1–T4.** Touches T3: yes — it is exactly the total identification of Λ by Σ_{d|n}Λ(d) = log n, used
  linearly (perturbatively); records that it produces neither a nontrivial direction nor a quadratic bound. T2: no
  (the Möbius matrix appears, but not as a Gram matrix).

### R170_501 — Multiplicative compensation law
- **Object.** Twist χ_θ(n) = n^{iθ}: (Λχ_θ)∗(1χ_θ) = (log)χ_θ (1). Covariance W_θ(F) = W_T(e^{iθX}F) with expansion (2).
  H_θ = H + θV + θ²R + O(θ³), V = i[H,X], R = XHX − ½(HX²+X²H). Theorem 1: PRP = PVQH_Q^{−1}QVP (4).
  Physical formula (5) for R. (6) σ(H_θ) = σ(H). Theorem 2: v measurable unimodular with v(t+log p) = χ(p)v(t) ∀p ⇒
  v = e^{iφ}e^{iθt}, χ(p) = p^{iθ} (uses log2/log3 irrational).
- **Labels.** "Covariance and rigidity laws proved; positivity law not". Sustained: yes.
- **Stops.** Class NO-GO: modulation is unitary conjugation; it transports the kernel, does not create positive
  excess; (4) does not use (1) and holds for artificial weights with negative form. Rigidity: there are no
  independent local phases per prime.
- **T1–T4.** Does not touch T1–T4 directly (uses the divisor identity only to transport it, without a bound).

### R170_601 — Nonlocal storage attempt
- **Object.** Inequalities (L): Z − RZR ≥ I + R, Y*ZY ≤ I. Theorem 1: every such Z is Z = G + Σ_j R^jSR^j ≥ G,
  G = (I−R)^{−1} (Stein equation); (2) the second condition is K + O_S ≤ I with O_S ≥ 0. Möbius detector:
  M_d = Σ_{k≤N/d} μ(k)(dk)^{−1/2}H_{dk}, A_d = B^{−1/2}M_dB^{−1/2}, S₀ = [A₂,A₃]*[A₂,A₃].
- **Labels.** "Construction and cost theorem proved". Sustained: yes. The η chosen using the computed
  margin are NUMERICAL and circular by its own declaration.
- **Stops.** Class NO-GO: positive nonlocal compensation consumes margin I−K, does not create it; existence of Z
  ⇔ K ≤ I. Falsifier a₂ = 100 from R170_301.
- **Corrected by.** R170_701/702: the Möbius detector is replaced by the faithful Gamma detector of P46.
- **T1–T4.** No (the M_d come from T3 via R170_401, but there is no quadratic bound).

### R170_701 — Paper 46 comparison
- **Object.** Table of precedents in P46 for 301–601; list of missing pieces (faithful Gamma detector, exterior
  collars, complete polar terms, oriented integer identity, minimality). Errors in the text of P46:
  "(P) has no minimizer" contradicts the proof of O; "m ≥ 0" false (m(0) < 0); update to lem:contA; existential
  extension beyond ½log5 already derivable from thm:log5W + lem:contT.
- **Labels.** Structural comparison, no theorem label. Sustained: yes as an audit.
- **Stops.** No identity in 301–601 uses minimality or the oriented integer identity.
- **T1–T4.** Mentions T4 (PC section with Λ∗1 = log and orientations) as pending; does not walk it.

### R170_702 — Gamma detector and complete collars
- **Object.** Detector (𝓡F)_m = b_m∫e^{−a_m t}F, a_m = 2m+1/2, b_m = √a_m e^{−a_m(T+δ)}; HS and injective (P46);
  exact HS tail h_L. O_Γ = Σ_j Y*R^j 𝓡*𝓡 R^jY > 0 strictly. Complete collar identity:
  𝓡U_N = D_N𝓡 − 𝓔_N; for an eigenvector of definite parity, Q^W_{N,L}(F) = −2Σ_{m≤L}(d_{m,N}+λ)|(𝓡_LF)_m|².
- **Labels.** "Consequences proved". Sustained: yes.
- **Stops.** Faithfulness ≠ coercive bound: K + ηO_Γ ≤ I already excludes contact (circular). The identity does not use
  minimality; at λ = 0 it gives Q = −2c.
- **T1–T4.** Touches T4: partially — it is the collar balance of the finite identity (D_N, 𝓔_N), with the
  cancellation 𝓔_{N'} − 𝓔_N = (D_{N'}−D_N)𝓡; converts nothing into Σ h(k)|ℓ_k|².

### R170_703 — Explicit extension past log5
- **Object.** With T₀ = ½log5, L = 10^{24}, ε = (T₀/4)e^{−L}: W_T(F) ≥ ½·10^{−18}‖F‖² for 0 < T ≤ T₀+ε.
  Explicit constants: sup|τm'(τ)| < 10, prime weights < 200, control Q(F) ≤ W_{T₀}(F) + 20; dilation U_r unitary.
- **Labels.** "Theorem derived from the P46 certificate" = CONDITIONAL on the imported certificate (not rerun);
  the analytic deduction is complete. Sustained: yes, with that dependence.
- **Stops.** Width e^{−10^{24}}: not useful; iterating continuity does not exclude summable widths.
- **Note.** Notation conflict: here L = 10^{24}, in the rest of the phase L = 2T or number of moments.
- **T1–T4.** No.

### R170_704 — First contact dilation flux
- **Object.** 𝒥_h(F) = [W_T(F) − W_{(1−h)T}(U_{1−h}F)]/h ≤ 0 at contact; exact identity with
  [m(τ)−m(τ/r)] ≤ 0, prime and polar term without sign. Inversion Σ Λ(n)q_h(n) = Σ μ(d) log k q_h(dk).
- **Labels.** "Identity and sign restriction proved". Sustained: yes; the restriction J_h ≤ 0 only uses W_T ≥ 0,
  not minimality (it says so).
- **Stops.** J_h > 0 would be equivalent to W_{(1−h)T}(U_{1−h}F) < 0: writing it is not proving it; Möbius without sign.
- **T1–T4.** Touches T3: yes, weakly (Λ = μ∗log on q_h, without a bound).

### R170_801 — Three Gates audit (external source)
- **Object.** Schur identities reconstructed for A = M_a − β|1⟩⟨1|: ∫g/a = δθ, debit D = δ|θ|²/J; residual
  identity ⟨g,B^{−1}g⟩ = ⟨x₀,Bx₀⟩ + 2Re⟨x₀,r⟩ + ⟨r,B^{−1}r⟩.
- **Labels.** Partial audit; algebra correct (CITED+reconstructed). Example A_δ = δ shows that there is no
  uniform response bound as the gap closes. The transport of lemma 8.4 remains unverified (neither proved nor
  refuted).
- **T1–T4.** No.

### R170_802 — Selection transfer (external source)
- **Object.** For S = Σ a_p(q)Z_p with Haar phases: E exp(t Re S) ≤ exp(t²V/4); with a law ν of entropy H relative to
  Haar, E_ν Re S ≤ √(VH).
- **Labels.** PROVED (elementary). Sustained: yes.
- **Stops.** A pointwise selection is a Dirac (infinite entropy); independence of log p does not exclude
  pointwise resonances.
- **T1–T4.** No.

### R170_803 — Boundary repair and exact response (external source)
- **Object.** Counterexample K = diag(−1,1), R = (1,0): K + R*R ≥ 0 without K ≥ 0. Example ℓ²⊕ℂ with A = diag(n^{−2}),
  b = (n^{−1}): scalar repair with divergent cost (b ∉ Ran A^{1/2}). Identity (E): S = C − X₀*BX₀ − X₀*R₀
  − R₀*X₀ − R₀*B^{−1}R₀; target inequality (P); formula (F) of the hidden cost |η|²/(Jδ).
- **Labels.** Elementary, correct. Inference NO-GO (positive repair does not transport sign).
- **T1–T4.** No.

### R170_804 — Literature transfer review
- **Object.** Summary of 801–803, 805 and table of 27 external works with depth of reading. Cost of
  selection via the modulation operator: input norm ~X^{1/2+1/p}; linearization error |γ|H²/(2X²).
- **Labels.** Review; no new theorem except elementary bounds. There is no complete audit (it declares so).
- **T1–T4.** No.

### R170_805 — Common complement capacity
- **Object.** On (0,1), r[u] = ¼∬(1/|x−y|−1)|u(x)−u(y)|² + ∫[−½log(x(1−x)) − log2]|u|². For disjoint
  intervals of length ε: r[u] ≥ Σ_ν[log(1/(2ε)) − Δ_ν]‖f_{ν,0}‖², Δ_ν = ½Σ_{μ≠ν} d(D_{νμ}),
  d(D) = log(1+1/D) − 1/(D+1), Δ_ν ≤ 1−γ_E. Minimum of l₀ = β‖u‖² − ½|∫u|² (β = log2+½) over the common complement:
  β‖f‖² − β/(2log2+ℓ)|∫_S f|².
- **Labels.** Reconstruction PROVED. Sustained: yes; audited and confirmed in R170_807.
- **T1–T4.** No.

### R170_806 — Archimedean transfer
- **Object.** With L = 2T, f(x) = √L F(L(x−½)): A_T[F] = b[f] − a_L‖f‖² − ⟨H_Lf,f⟩, a_L = γ_E + log(2πL),
  h_L(v) = Lk(Lv) − 1/(2v), b[f] = ¼∬|f(x)−f(y)|²/|x−y| + ∫−½log(x(1−x))|f|² (1). Complete form (2):
  W_T = b − a_L − H_L − J_L + 2|⟨f,c_L⟩|² − 2|⟨f,s_L⟩|². Reformulation (4): sup spec(b^{−1/2}K_Lb^{−1/2}) ≤ 1.
- **Labels.** No explicit label; identity PROVED (confirmed in 807/808). (4) is a reformulation.
- **Stops.** The remainder K_L has no sign in the metric of b; discarding R_S would be illegitimate.
- **T1–T4.** No.

### R170_807 — Transfer independent audit
- **Object.** Verification of 805 and 806 (constants, factor ½, K(v) = 1/(2sinh(v/2)) + 1/(2cosh(v/2)) = 2k(v)).
  Counterexample to the relaxation: normalized sines on an interval J ⊂ S^c of width < log2/L give W_rel →
  β − a_L < 0 for L > e^{β−γ_E}/(2π) ≈ 0.2947.
- **Labels.** Audit; PROVED (1)–(4) of its list; NUMERICAL the diagnostics at 45 digits.
- **T1–T4.** No.

### R170_808 — Final transfer audit
- **Object.** Same transfer; statement (A): inf{W_rel[f] : f|_S = 0} = −∞ for L > L_*. Limit value ≈ −1.69783 at
  L = log5.
- **Labels.** PROVED (restriction of the construction). Sustained: yes.
- **Stops.** NO-GO for the relaxation that discards R_S.
- **T1–T4.** No.

### R170_809 — Sign construction with retained reserve
- **Object.** P projection onto indicators of M cells; b[y] ≥ λ_M‖y‖², λ_M = log M + γ_E − ½ (1); K_L ≤ κ_L I with
  κ_L explicit; M > exp(κ_L+g−γ_E+½) ⇒ B ≥ g_M I (2). Harmonic extension V = b^{−1}PD^{−1}, C = D^{−1} − V*K_LV,
  A = QK_LV: W[Vx+y] = ⟨x,Cx⟩ − 2Re⟨y,Ax⟩ + B[y] (3); W ≥ ⟨x,(C−A*A/g_M)x⟩ + g_M‖y−Ax/g_M‖² (4);
  exact (5) C − A*B^{−1}A; loss (6) A*(g_M^{−1} − B^{−1})A ≥ 0.
- **Labels.** "Form inequality proved at each scale". Sustained: yes.
- **Stops.** C − A*A/g_M ≥ 0 not proved for all L; the bounds hold for many altered weights (they do not
  break falsifiers).
- **Corrected/audited by.** R170_810.
- **T1–T4.** No.

### R170_810 — Sign audit
- **Object.** Validates (4) of 809. 2×2 counterexample: b = diag(1,3), K = [[½,1],[1,1]], W semidefinite with
  W(1,½) = 0; with g = 1, C − A²/g = −½ while C − A²/B = 0. Another: K = diag(2,0) ⇒ W = diag(−1,3).
- **Labels.** Operator-inference NO-GO (reserve + coercivity do not force sign).
- **T1–T4.** No.

### R170_811 — Uniform arithmetic law proposal (FIDC)
- **Object.** Oriented divisor–collar incidence flux: 𝔉^ε = Re⟨{X,E_N}F − L_M*E_NF − JH_{M,N}F − H_{M,N}𝓕F,
  χ_εS_LF⟩ − Re⟨S_N r_F, 𝓕(χ_εS_LF)⟩ (1); N = ⌈e^{2T}⌉, M = N². FIDC conjecture: (FIDC+) 𝔉 ≥ (1−q₀)‖R_LF‖²,
  q₀ = log2/4 + 1/16, and (FIDC−) 𝔉 ≤ 0 at primitive first contact; together they would give R_LF = 0 ⇒ F = 0.
  Reserve (6) R_L*(I−D_{N,L})R_L ≥ (1−q₀)R_L*R_L (cited from P46). Mechanism §5: saturated zone k ≤ N cancelled by
  Σ_{d|k}Λ(d) = log k; boundary k > N with weights Λ(d) ≥ 0.
- **Labels.** Declared a proposal / CONJECTURE (in the sense of OPEN). Uses an external equivalence (§3,
  steps 3–4). Sustained: the proposal has definition errors (see 812).
- **Stops.** Sign of the exterior flux not derived.
- **Corrected by.** R170_812 (wrong adjoint S_N instead of S_N*; empty regularization χ_ε) and R170_813.
- **T1–T4.** Touches T4: yes, fully — it is the attempt to give sign to the mixed pairings of PC (H_{M,N}, E_N,
  Tate port) using h_{M,N}(k) ≥ 0; it is not written as Σ h(k)|ℓ_k(F)|². Touches T3: yes (interior cancellation
  by Λ∗1 = log).

### R170_812 — FIDC audit
- **Object.** U = 𝓕: U* = U, U² = I, Uτ_a = τ_{−a}U, US_N* = S_NU, UA_M = A_MU (1). Original flux
  = Re⟨A_MF − r, S_NUg⟩ + Re⟨r,(S_N−S_N*)Ug⟩ (4): the second term is superfluous. χ_εg = g exactly (inoperative
  regularization). Counterexample A_± = [[0,±1],[±1,0]]: same interior block, opposite flux. h_{M,N} ≥ 0 gives no sign
  of oscillating pairings; ⟨JH_{M,N}F,g⟩ = 0 by support but H_{M,N}UF does not vanish.
- **Labels.** Audit; corrections PROVED; NO-GO of the inference "local equation ⇒ sign of the flux".
  §5 uses an external equivalence (P45 thm:sufficiency) for the primitive bridge.
- **T1–T4.** Touches T4: yes — records that the positivity of h_{M,N}(k) does not transfer to the form.

### R170_813 — FIDC revised
- **Object.** Definition without regularization in Q_log: g = S_LF, h = S_NUg, e_{M,F}(v) = a_M(F,v) − ⟨r,v⟩,
  Flux_corr = Re e_{M,F}(h) (A); e_{M,F}(v) = 0 for v supported in I_T (B); PC expansion (C) with port
  Re⟨S_N*r,Ug⟩; difference (D) with the original. Pointwise exterior formula for A_MF outside I_T for smooth F.
  Obligations (P+) Flux ≥ (1−q₀)‖R_LF‖², (P−) Flux ≤ 0.
- **Labels.** Definition and identities PROVED; (P±) OPEN. Uses an external equivalence (P45 Theorem F) in §3.
- **T1–T4.** Touches T4: yes (well-defined object of the exterior residue; without sign).

### R170_814 — Arithmetic Green proposal
- **Object.** ρ = 1 − 1/(2N²), h = 1−ρ; correctors p, q with bump η, C(p)=1, S(q)=1; G_ρF = D_ρF − C(D_ρF)p − S(D_ρF)q
  primitive supported in I_{ρT} (3); E_ρ(F) = a_{ρT}(G_ρF,G_ρF)/h ≥ 0 and hE_ρ = a_T(G_ρF−F, G_ρF−F) (5) [lemma
  proved]. Φ(F) = Re[a_M(F,z) − ⟨r_F,z⟩], z = S_NUS_LF. Proposal (G): (i) (1−q₀)‖R_LF‖² ≤ Φ, (ii) Φ + E_ρ ≤ 0.
  (6) Φ = Ω − Σ_{d≤M}Λ(d)ξ_d/√d; (7) = Σ_{km≤M}μ(k)log m ξ_{km}/√(km); required interval (8).
- **Labels.** Lemma PROVED (only uses a_T ≥ 0 on the contact window); (G) OPEN. Uses an external equivalence
  (P45 Theorem F) in §4.
- **Stops.** Writing (7) does not give (8): μ and ξ without sign.
- **T1–T4.** Touches T3: yes — Λ = μ∗log inserted into the flux, without a bound. Touches T4: yes (Φ is the PC exterior residue).

### R170_815 — Green sign attempt
- **Object.** Interior identity [a_T(F,F) − a_{ρT}(G_ρF,G_ρF)]/h = −E_ρ ≤ 0 (1); (G−) is equivalent to (7):
  Re e_{M,F}(S_N𝓕S_LF) ≤ −(1/h)a_T(G_ρF−F, G_ρF−F). ⟨JH_{M,N}F,S_LF⟩ = 0 (9a); what survives is −Re⟨H_{M,N}𝓕F,S_LF⟩ (9b).
  3×3 counterexample A_c = [[0,0,c],[0,1,0],[c,0,0]]: fixed interior data, Φ + E = c + 1/h ranges over ℝ.
  (13) Σ_{d≤M}(Λ(d)/√d)ξ_d ≥ Ω + E_ρ.
- **Labels.** Identities PROVED; NO-GO of the purely variational inference (semidefiniteness + radical +
  interior competitor). (G−) OPEN.
- **Corrected by.** R170_817 (withdraws the unjustified use of P_Tz; restricts the scope of the 3×3 model).
- **T1–T4.** Touches T4: yes — isolates (9b), the tail term H_{M,N}𝓕F, as the residue without sign. T3: yes (14).

### R170_816 — Divisor sign attempt
- **Object.** Φ = B − C, C = Re⟨H_{M,N}UF,g⟩ (3); H_{M,N} = Σ_{N<k≤MN} h_{M,N}(k)k^{−1/2}τ_{log k} (4); mass
  W_{M,N} = Σ h_{M,N}(k)/√k (5); |C| ≤ W_{M,N}‖F‖‖S_LF‖ (6); self-adjoint form K_{M,N,L} = (UH*S_L + S_LHU)/2 with
  −W‖S_L‖ ≤ K ≤ W‖S_L‖ (7); required (8) B − ⟨F,KF⟩ ≥ (1−q₀)‖R_LF‖². Lower bound on the mass (8a):
  W_{M,N} ≥ (log2/(2√2))√N (verified). Falsifier of the inference "h(k) ≥ 0 ⇒ pairing ≥ 0" (translated
  bumps). Oriented separation of the d=2 channel (14): the reflected family JF cancels by support; there remain
  two Fourier families (shifts log(m/2) and log(2m) on UF) without opposite terms.
- **Labels.** Identities and bounds PROVED; negative for (G)(i), which stays OPEN.
- **Stops.** Fourier tail H_{M,N}UF only with a two-sided estimate, loss ~√N; the reindexing m ↦ 4m
  changes weights and ranges.
- **Audited by.** R170_817.
- **T1–T4.** Touches T4: yes, it is the most direct attempt — the tail Σ_{k>N} h(k)k^{−1/2}τ_{log k} applied to UF is not
  converted into a sum of squared moduli; only two-sided bounds. Touches T3: yes (§4, Eratosthenes/Λ = μ∗log gives no
  sign).

### R170_817 — Round validation
- **Object.** Table of verdicts on 815–816; corrections (P_Tz withdrawn; scope of the 3×3 model and of the
  negative-correlation examples restricted; norm bound not called a "new arithmetic estimate").
  Confirms the shift structure of the d=2 channel.
- **Labels.** Audit. Sustained: yes.
- **T1–T4.** Touches T4: yes (confirms that the tail does not cancel term by term; does not exclude deeper cancellation).

### R170_818 — Puzzle map
- **Object.** Map: direct route (exact debit A*B^{−1}A) and flux route (two gaps: reserve ≤ Φ, Φ ≤ −E_ρ).
  Table of pieces and priorities 1–4 (exterior–interior compatibility; joint Poisson–Tate/tail comparison;
  transport; uniformity). Criterion for a discriminating piece (breaks falsifiers).
- **Labels.** Synthesis; no theorem. Uses an external equivalence (P46 + P45 Theorem F in the diagram).
- **T1–T4.** Touches T4 as a target (priority 2), does not walk it.

### R170_819 — Exterior–interior connection
- **Object.** 𝒬_{M,r}(v) = a_M(v,v) − 2Re⟨r,v⟩; 2Φ = 𝒬(F+z) − 𝒬(F) − a_M(z,z) (4); hE_ρ = 𝒬(G) − 𝒬(F) = a_M(δ,δ) (5);
  𝓡F = δ − hz (6); bridge (8): Φ + E_ρ = Re e_G(z) + h^{−1}Re a_M(δ, 𝓡F). Scale commutation A_MD_ρ = D_ρA_M^{(ρ)}
  (9b), defect (9d), decomposition (9e) of e_G(z) into four pieces. PC expansion (10), cancellation (11), collar
  (12), second remainder (13). Obligation (16).
- **Labels.** Identities (4), (5), (8), (9e) PROVED (validated in 822). (16) OPEN.
- **Error.** The text around (9e) and §5 suggests that a scale transformation that would break the hyperbola
  must be reconciled; R170_820 and R170_822 correct this: dilation does not destroy divisor multiplication.
  (There is also a misplaced prose fragment: "where the defect is…" after (9c').)
- **T1–T4.** Touches T4: yes (12) is the residual collar without sign. T1: no.

### R170_820 — Joint arithmetic comparison
- **Object.** Complete conjugation O^{(ρ)} = D_ρ*OD_ρ: X ↦ ρX, τ_a ↦ τ_{a/ρ}, 𝓕 ↦ 𝓕_ρ; (PC_ρ) exact; H^{(ρ)}_{M,N} with
  the same h_{M,N}(k) (6); exact subtraction (7); ΔH = Σ h(k)k^{−1/2}(τ_{log k/ρ} − τ_{log k}) (8); Tate corrector (9).
  Dichotomy: conjugating all the data gives a scalar tautology; fixing data leaves an uncontrolled remainder. Multiplier
  cos((log k)ξ/ρ) − cos((log k)ξ) without sign (11).
- **Labels.** Identities PROVED ("new only in bookkeeping"). No one-sided inequality.
- **T1–T4.** Touches T4: yes — the tail reappears at two scales with the same h ≥ 0 and oscillating multipliers; there is no
  conversion to Σ h|ℓ_k|². T3: the interior cancellation is preserved (no new sign).

### R170_821 — Uniformity of scale remainders
- **Object.** ‖τ_b − τ_a‖ = 2 for a ≠ b in L² and Q_log (5); strong convergence (6), rate with Df ∈ Q_log (7);
  ‖m(D/ρ) − m(D)‖ ≤ (8/7)C_m h, C_m = sup|xm'(x)| (12); corrector bounds (15)–(16); modulus ω_T via radical (17)
  without uniformity in T (18).
- **Labels.** PROVED (size/topology). Sustained: yes (822 warns not to extrapolate the norm 2 to sums nor the
  strong continuity of D_ρ in the absence of norm continuity of 𝓕_ρ).
- **T1–T4.** Touches T4: yes, indirectly (two-sided bound (9) of ΔH without a factor h).

### R170_822 — Sequential round audit
- **Object.** Validates 819 (4),(5),(8),(9e); corrects the reading of loss of factorization under scaling; validates (PC_ρ)
  and (7) of 820; corrects that e_F annihilates every admissible test supported in the window (not only primitive ones); validates
  ‖τ_{a/ρ} − τ_a‖ = 2 and the O(h) Gamma bound; forbids extrapolations.
- **Labels.** Audit. Sustained: yes.
- **T1–T4.** Touches T4: confirms that the round did not obtain the one-sided inequality.

---

## 2. Synthesis

### (a) Reusable PROVED pieces
1. Domain, reduction to real tests and to a sequence of windows — R170_101 §§1–3.
2. Explicit root via prime tower D_p*D_p = C_pI − (V_p+V_p*) and truncated version (4) Σ(Λ(n)/√n)‖F−U_nF‖² —
   R170_201 §§2–4; optimality of the constant (Theorem 2).
3. Lévy representation Γ_T = ∫k(u)‖F−S_uF‖²du, coercivity α_T, decomposition W = E_T − C_T, path
   series with tail (8), (13), criterion K_T ≤ I — R170_301 §§2–5.
4. Response formula κ̇ and second-order tangency / two-sided robustness ⇔ DP = 0 — R170_401 §§2–3;
   divisor error coordinates (7) — §4.
5. Local-phase rigidity theorem (v = e^{iφ}e^{iθt}) and compensation PRP = PVQH_Q^{−1}QVP — R170_501 §§3,5.
6. Minimum-cost theorem for the Stein equation Z = G + ΣR^jSR^j — R170_601 §2.
7. Exact HS tail of the Gamma detector and complete collar identity Q^W = −2Σ(d_{m,N}+λ)|(𝓡_LF)_m|² — R170_702.
8. Explicit extension to T₀ + (T₀/4)e^{−10^{24}} (conditional on the P46 certificate) and constants sup|τm'| < 10 —
   R170_703.
9. Entropy bound E_ν Re S ≤ √(VH) — R170_802.
10. Response identities (E), (F) with residue — R170_803 §§3–4.
11. Capacity with common complement Δ_ν ≤ 1−γ_E and minimum of l₀ — R170_805, audited R170_807 §1.
12. Exact transfer W_T = b − a_LI − H_L − J_L + 2|c_L⟩⟨c_L| − 2|s_L⟩⟨s_L| — R170_806 (2), R170_807 §§3–4, R170_808.
13. Harmonic extension with retained reserve, inequality (4) and exact loss (6) — R170_809 §§1–3.
14. Correct adjoint of the Tate port and flux Φ well defined in Q_log — R170_812 §1, R170_813 §§1–2.
15. Primitive contraction G_ρ and E_ρ = a_T(G_ρF−F)/h ≥ 0 — R170_814 §3, R170_815 §2.
16. Separation Φ = B − C, ⟨JH_{M,N}F,S_LF⟩ = 0, mass W_{M,N} ≥ (log2/(2√2))√N, oriented decomposition of the
    d=2 channel (14) — R170_816 §§2–3,6.
17. Bridge Φ + E_ρ = Re e_G(z) + h^{−1}Re a_M(δ, δ−hz) and scale decomposition (9e) — R170_819.
18. Conjugated PC (PC_ρ), invariance of h_{M,N} under dilation, subtraction (7) — R170_820.
19. ‖τ_{a/ρ}−τ_a‖ = 2; ‖m(D/ρ)−m(D)‖ ≤ (8/7)C_m h — R170_821 §§2–3.

### (b) Closures (class or inference NO-GO) with falsifier
- Orthogonal channels per prime with constant compensation: C_P minimal and R_P → −∞; generic in dilations and weights
  — R170_201 (no nominal falsifier, the proof holds for every system a_j>1, ℓ_j>0).
- Scalar networks with conductances ≥ 0 and hidden vertices: falsifier h(log(3/2)) = (7/10)√(2/3) > 0 at T = ½ —
  R170_202.
- Coherent coupling + convergence ⇏ contraction: falsifier a₂ = 100, T = 1, F = 1_{(−1,1)}/√2, W < −79 —
  R170_301 §6.
- Scalar first-variation cancellation at contact does not suffice: Theorem 1 of R170_401.
- Local multiplicative modulations only transport the kernel; local phases per prime are rigid — R170_501.
- Positive nonlocal compensation does not create margin; falsifier a₂ = 100 — R170_601.
- Detector faithfulness ≠ coercive bound — R170_702 §2.
- Positive repair K + R*DR ≥ 0 does not transport sign; falsifier diag(−1,1) and divergent-cost example —
  R170_803.
- Relaxation discarding R_S: infimum −∞ for L > 0.2947 — R170_807 §5, R170_808 (A).
- Reserve + complement gap do not force sign: 2×2 falsifier b = diag(1,3), K = [[½,1],[1,1]] — R170_810.
- Local equation ⇒ sign of the flux: falsifier A_± — R170_812 §3.
- Semidefiniteness + radical + interior competitor ⇒ (G−): 3×3 falsifier A_c — R170_815 §4.
- h(k) ≥ 0 (or Λ(d) ≥ 0) ⇒ pairing ≥ 0: translated-bumps falsifier — R170_812 §4, R170_816 §4.
- Uniformity in norm of translation differences: exact norm 2 — R170_821 §2.

### (c) Explicitly open, with exact obstacle
- (14) of R170_301: Σ_j‖L_{j,T}x‖² ≤ ‖x‖² ∀T — uses no identity exclusive to ℤ.
- (4) of R170_806: sup spec(b^{−1/2}K_Lb^{−1/2}) ≤ 1, with R_S retained in the inverse metric.
- C − A*B^{−1}A ≥ 0 (or C − A*A/g_M ≥ 0) for all L — R170_809 §3; the loss (6) may eat the zero margin.
- (P+) Flux_corr ≥ (1−q₀)‖R_LF‖² and (P−) Flux_corr ≤ 0 — R170_813 §3; equivalent to (G)(i),(ii) of R170_814.
- (8) of R170_816: B − ⟨F,K_{M,N,L}F⟩ ≥ (1−q₀)‖R_LF‖²; obstacle: tail H_{M,N}UF only two-sided, mass ~√N; channel d=2 leaves
  two Fourier families log(m/2), log(2m) without opposite pairs.
- (13) of R170_815: Σ(Λ(d)/√d)ξ_d ≥ Ω + E_ρ; μ and ξ change sign.
- (16) of R170_819 / (12) of R170_820 / (19) of R170_821: Re e_G(z) + h^{−1}Re a_M(δ,𝓡F) ≤ 0; obstacle: no identity
  correlates ΔE, ΔH, Δ𝓕, Δ_Tate and the alignment error δ − hz in the radical of the first contact; the remainders have no
  orientation and there is no uniformity in T.
- First-order sign law in divisor coordinates — R170_401 §6 (the curve preserving e_m = 0 is constant).
- Transport of lemma 8.4 of the external source — R170_801 (neither proved nor refuted).
- Use of the selection entropy — R170_802 (a phase law with controlled entropy is missing).

### (d) What in this stretch already walks T1–T4 and why it failed
- **T1** (continuous squares with arithmetic in the index/weights of the dilation):
  R170_201 (‖D_pF‖² per prime, weights log p·p^{−k/2}; Σ(Λ(n)/√n)‖F−U_nF‖²) — fails: the expression is "squares − C_P‖F‖²",
  C_P diverges, R_P → −∞, and the identity is generic in arbitrary positive dilations/weights (does not see ℤ).
  R170_301 (5) — same structure with Γ_T and pole; the contraction K_T ≤ I does not follow; falsifier a₂ = 100.
  Neither of the two puts the nonlinearity in V_T so that it breaks for cΛ: both are linear in the weights.
- **T2** (Gram by divisor incidence [log gcd] = E diag(Λ) Eᵀ): **does not appear** in this stretch. The closest is the
  Möbius matrix of R170_401 §4 and the M_d of R170_601, used as linear responses, not as a Gram model.
- **T3** (total identification by Σ_{d|n}Λ(d) = log n → quadratic bound):
  R170_101 §4, R170_704, R170_814 §5 (7)–(8), R170_815 (14), R170_816 §4 — the inversion Λ = μ∗log is exact but leaves μ and the
  correlations with free sign; it is not converted into a bound. R170_401 §4 — sharpest formulation: e_m = 0 ∀m ≤ N determines
  λ = Λ; the identification is rigid (constant curve), so there is no direction along which to propagate the sign and the response
  (8)–(9) only measures violations. R170_811 §5 — uses the identity to cancel the saturated zone k ≤ N of PC; leaves only the tail.
- **T4** (common residue):
  R170_811 (FIDC, conjecture), R170_812 (adjoint corrected; h ≥ 0 gives no sign), R170_813 (Flux_corr well defined),
  R170_814–815 (Φ as exterior residue; (9a) ⟨JH_{M,N}F,S_LF⟩ = 0 but (9b) −Re⟨H_{M,N}𝓕F,S_LF⟩ survives),
  R170_816 (direct attempt: C = Re⟨H_{M,N}UF,g⟩ = ⟨F,K_{M,N,L}F⟩ with K self-adjoint and only two-sided bounded;
  mass ≥ c√N; channel d=2 with two Fourier families without term-by-term cancellation), R170_819–821 (the collar
  survives at two scales with the same h_{M,N}(k) and multipliers cos((log k)ξ/ρ) − cos((log k)ξ) without sign).
  Recorded reason for failure: the tail pairings act on UF = 𝓕F, which is not supported in the
  window; h_{M,N}(k) ≥ 0 does not fix the sign of an oscillating pairing between different functions (F and S_LF, not a
  square |ℓ_k(F)|²); and the reindexing that would align scales changes weights and ranges. No memo in this stretch
  writes the tail as Σ_{k>N} h(k)|ℓ_k(F)|²: what is missing is exactly that the pair (F, S_LF) become a
  diagonal pair (ℓ_k(F), ℓ_k(F)).

### (e) Inconsistencies or errors between memos
1. R170_811: wrong adjoint of the Tate port (S_N instead of S_N*) and empty regularization χ_ε — corrected by
   R170_812 and R170_813.
2. R170_815 uses P_Tz without justifying that the indicator preserves Q_log — withdrawn in R170_817.
3. R170_819 suggests that scaling log d ↦ log d/ρ breaks the hyperbola — corrected by R170_820 §2 and R170_822 (divisor
   multiplication is preserved).
4. R170_819 §1 states the weak equation only for primitive tests; R170_822 corrects that e_F annihilates every admissible test
   supported in the window.
5. R170_701 points out errors in the text of P46 (minimizer of (P); "m ≥ 0"; reference to lem:contA; existential extension
   past ½log5).
6. R170_812 §5 warns that the reference "(11.3)" of P46 is ambiguous (equation label).
7. Kernel conventions: k (R170_301, 806) vs K = 2k (R170_807, 808); consistent once made explicit (checked).
8. Notation: L = 10^{24} in R170_703 versus L = 2T (806–809) and L = number of moments (702, 811–816).
9. R170_819 has a displaced prose fragment ("where the defect is…") after (9c').
10. R170_000, 811, 812, 813, 814, 818 use an external equivalence (R163_401 Thm 1.2; P45 Theorem F); recorded without
    developing it.

### (f) Files read (complete reading with Read)
README.md: does not exist in the folder. Read in full: R170_000, R170_101, R170_201, R170_202, R170_301, R170_401,
R170_501, R170_601, R170_701, R170_702, R170_703, R170_704, R170_801, R170_802, R170_803, R170_804, R170_805,
R170_806, R170_807, R170_808, R170_809, R170_810, R170_811, R170_812, R170_813, R170_814, R170_815, R170_816,
R170_817, R170_818, R170_819, R170_820, R170_821, R170_822 (34 .md files). Non-.md files: six JSON, listed
above without analysis.
