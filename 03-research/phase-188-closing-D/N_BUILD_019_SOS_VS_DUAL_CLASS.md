# N_BUILD_019 — Divisor-lattice sums of squares vs the dual certificate class: pure-arithmetic SOS is dead at every window with a contact; mixed SOS is the dual class

Pen and paper. Window measure μ^{form}_T on (−2T, 2T): 𝔞_T(F) = ⟨μ^{form}_T, c_F⟩ (archimedean part in Lévy–Khintchine form
C₀δ₀ + (1−cos)-renormalized K, minus the comb Σ_{n∈N_T} v_n(δ_{log n}+δ_{−log n})/2·2). SOS certificate (N_BUILD_018 §3):
μ^{form}_T = Σ_i A_i^*A_i + Π + β₀cosh(u/2) + β₁u sinh(u/2) on (−2T, 2T), Π positive-definite.

## Corpus check
Paper 47 def:PD (primal (P) / dual (D): certificates are EXTERIOR measures ν, supp ν ⊂ {|u| ≥ 2T}, with σ_T + ν̂ + β·ĝ ≥ c pointwise),
prop:weak, thm:D1 (strong duality D_T = λ_P, finitely atomic exterior sequences), thm:Z (dual variable = explicit formula on flat-top
tests), prop:TK + thm:N/N′/R (lattice ceilings), Theorem C (½log3). Phase 155 (TK, N, N′, "lattice never the deficit" AL′), R186_052
Thm 3.3 (Kreĭn, CONDITIONAL). New: Prop 1 (SOS ⊂ dual class), Theorem 2 (pure-arithmetic SOS dead), §3 (the ½log3 check by hand).

## 1. Prop 1 (PROVED): every SOS certificate is a dual certificate of value ≥ 0
Let Π̃ := Σ_iA_i^*A_i + Π, a positive-definite measure on ℝ (each A_i^*A_i is p.d.; Π extends to a p.d. measure on ℝ by hypothesis). Put
ν := Π̃ − Π̃|_{(−2T,2T)} (supported in |u| ≥ 2T) up to the window-edge convention. On (−2T, 2T), μ^{form} = Π̃ + Tate terms, so
σ_T(τ) + ν̂(τ)·(−1) … precisely: the symbol of the window measure plus the exterior part equals Π̃^ ≥ 0 plus the Tate multipliers:
 σ_T + (−ν)^ + β₀ĝ₀ + β₁ĝ₁ = Π̃^ ≥ 0,
i.e. (−ν, β) is a certificate of value 0 in the sense of def:PD (σ_T is the transform of the window measure, the exterior-supported −ν is an
admissible dual variable). Conversely a certificate of value c ≥ 0 gives Π̃ := μ^{form} + exterior part with transform ≥ c ≥ 0 (p.d.), i.e. an
SOS certificate with one "square". ∎
So: **SOS certificates with a free p.d. part = the dual class (D) of Paper 47** (with Tate multipliers). By thm:D1 this class is lossless in the
limit (D_T = λ_P); no new content. Lattice ceilings (prop:TK, thm:N, N′) apply to the subclass whose exterior part is supported on a lattice
jd; arithmetic squares produce exterior atoms at |log(n/m)| ≥ 2T — only if the A_i extend beyond the window (n or m ≥ N); with A_i supported
on {log n : n < N} all lags |log(n/m)| < 2T are interior, the exterior part comes only from Π.

## 2. Theorem 2 (PROVED): pure-arithmetic SOS fails at every window with a contact
Call a certificate pure-arithmetic if all atoms of μ^{form} are produced by Σ A_i^*A_i with A_i = Σ_{n<N}x^{(i)}_nδ_{log n} (Dirichlet polynomials)
and Π is absolutely continuous (no atoms). Then the atomic parts must match: Σ_i A_i^*A_i = mδ₀ − Σ_n v_n(δ_{log n}+δ_{−log n})/… =: 𝔐 (all
atoms at log of non-prime-power rationals cancel), for some m ≥ 0 (the δ₀-mass taken from the archimedean renormalized atom).
(i) 𝔐 is p.d. (sum of squares), so its symbol m − P_T(τ), P_T(τ) := Σ v_n cos(τ log n), is ≥ 0 for all τ: **m ≥ sup_τ P_T = A_T** (attained by
Kronecker on the finitely many log p, lem:mbounds(iii)).
(ii) The remainder μ^{form} − 𝔐 = (archimedean measure) − mδ₀ must be (p.d. continuous) + Tate on the window, so the archimedean form minus
m‖F‖² is ≥ 0 on P_T: λ_{∞,P}(T) ≥ m ≥ A_T.
(iii) Hand bound. prop:arch(ii) (PROVED in Paper 47 without computation) gives λ_{∞,P}(T) ≤ C₀ + φ((3π/2T)²), φ(x) = Σ_{k≥0}
x/(a_k(x+4a_k²)), a_k = k + ¼. For T ≥ ½log 3: N_T ∋ 2, so A_T ≥ v₂ = 2log2/√2 = 0.980 (the contact 3 enters only for T > ½log3, then A_T ≥ 2.248), and (3π/log3)² = 73.6, φ(73.6) ≤ 5.70 (hand
summation: 3.99, 0.737, 0.349, 0.195, 0.119, 0.076, 0.052, 0.037, 0.027, 0.021, 0.016, tail ≤ 0.083), so λ_{∞,P}(½log3) ≤ 0.33 < 0.980 ≤ A_T.
For T ≥ ½log 3 the comparison only improves (λ_{∞,P} nonincreasing, A_T nondecreasing).
For ½log 2 < T < ½log 3 (A_T = v₂ = 0.980) no hand bound is attempted; this interval is left OPEN here.
Hence: **no pure-arithmetic SOS certificate exists at any window T ≥ ½log 3** (in particular not at ½log3, where positivity holds by
Theorem C), PROVED by hand. ∎
Meaning: the atoms of the comb cannot be "paid" by squares of Dirichlet polynomials alone; they must be paired against the archimedean part
inside a p.d. combination — which is the general dual class of §1.

## 3. What differs from the lattice classes, and the verdict
- Lattice certificates (prop:TK): exterior atoms on jd, free coefficients; ceilings proved; converge to λ_P (thm:R).
- Arithmetic SOS: interior atoms forced at log(n/m) by squares; Theorem 2 shows the pure version is empty for T ≥ ½log 3; the mixed version
  (Π free) is exactly the dual class (Prop 1), whose limit is lossless and whose content is D itself.
**Verdict: divisor-lattice SOS is DEAD as a new route (pure: empty; mixed: = dual class).** The ½log3 test is answered by Theorem 2 (no
pure-arithmetic certificate), without numerics.

## Self-review
1. Prop 1: the window-edge atom convention (|u| = 2T) is as in prop:weak (harmless since c_F(±2T) = 0). The identification requires that the
SOS identity hold on the open window only — correct; outside, Π̃ is free. Correct.
2. Theorem 2(i): a p.d. atomic measure Σ_k b_kδ_{log k} (symmetric) has symbol b₀ + Σ 2b_k cos(τ log k) ≥ 0; with b_k = −v_n/2·… at prime
powers, the symbol is m − P_T(τ); sup P_T = A_T by Kronecker (log p rationally independent; prime powers k log p follow) — lem:mbounds(iii)
CITED. Correct.
3. (ii): "remainder must be p.d. continuous + Tate" — the remainder may also be any measure whose pairing with c_F is ≥ 0 on P_T, not only p.d.;
with that relaxation the condition is exactly 𝔞_∞ − m‖·‖² ≥ 0 on P_T, i.e. λ_{∞,P} ≥ m. Same conclusion. Correct.
4. (iii) hand arithmetic: φ terms recomputed: k=0: 73.6/(0.25·73.85) = 3.987; k=1: 73.6/(1.25·79.85) = 0.737; k=2: 73.6/(2.25·93.85) = 0.349;
k=3: 73.6/(3.25·115.85) = 0.195; k=4: 73.6/(4.25·145.85) = 0.119; k=5: 73.6/(5.25·183.85) = 0.076; k=6: 73.6/(6.25·229.85)=0.051;
k=7..10 ≤ 0.037+0.027+0.021+0.016; tail Σ_{k≥11} x/(4a_k³) ≤ 18.4·Σ_{k≥11}k^{−3} ≤ 18.4·0.0045 = 0.083. Total ≤ 5.70. C₀ = −5.3722 (CITED).
So λ_{∞,P}(½log3) ≤ 0.33. These are pen-and-paper evaluations (no code). The interval (½log2, ½log3) is OPEN for this theorem.
No sign contact; no negative value certified.
