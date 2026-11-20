# ROUND_001_B — The exterior form: is it a fused object, and does it carry a sign?

Object: Paper 47 §sec:ext (main.tex 9856–10677): summation map E, aliasing tail Ψ_f, gauge 𝒢_T, half-line
identity (thm:ext-half), Problem prob:ext-L, prop:ext-consol, prop:ext-univ, thm:ext-margin, prop:ext-latred,
rem:ext-latno, §ext-constraints. Starting point: DOSSIER_001 §6(d), §6(g), §7.1.
Notation as in Paper 47 §sec:ext: λ = e^T, N = λ², 𝓕f(ξ) = ∫f(x)e^{−2πixξ}dx, v_n = 2Λ(n)n^{−1/2}, 𝒲 the complete
form on the line with the full comb, Mellin–Laplace transform F̃(s) = ∫F(x)e^{(s−½)x}dx, Mf(s) = ∫_0^∞ f(u)u^{s−1}du.
The target throughout is (★) λ_A(T) ≥ 0 (and λ^W_T ≥ 0) as a statement about one quadratic form; no equivalence of it
with any other statement is used.

---------------------------------------------------------------------------------------------------------------------
## 0. Summary

1. The half-line identity is proved below with a self-contained, zero-free proof (Theorem 1.1, Corollary 1.2). Its
   three inputs are exactly: the Dirichlet series Σ n^{−s} with coefficients 1 on ℕ (I), the identity ζ·(ζ′/ζ) = ζ′,
   i.e. Λ∗1 = log (E), and the functional equation of ζ with Γ_ℝ at conductor 1 (F). PROVED.
2. For every other comb w (cΛ with c ≠ 1, a_P, finite modifications) the identity fails with an explicit defect
   (Proposition 1.3); for cΛ no nonzero function lies in the radical of both 𝒲 and 𝒲^c (Proposition 1.4, PROVED), and the
   c-exterior value is not gauge invariant (Proposition 1.5, ARGUED). So §ext-constraints item 2 over-claims, as
   DOSSIER §6(d) says. This is a re-derivation of results already in the corpus (PROOF_L_SHARP_C_001, R-Q6,
   AUDIT_200_PIMU_001); it is not new.
3. The failure carries no sign: the defect is −(c−1)·(archimedean+pole form)[Ef] + (c−1)·(same)[Ψ_f], indefinite in
   both slots. The "key cancellation" of cor:ext-cfals(ii) detects c > 1 only through comb monotonicity on a cone where
   the comb pairing has a fixed sign (Lemma 1.6), and therefore survives cΛ with c < 1, a_P and every downward finite
   modification: it fails the falsifier test. NO-GO as a sign step. PROVED.
4. The fused reading does not meet clause (5) of prop:spec. In Mellin coordinates the exterior datum is
   g̃·(ζM_N − 1) (SPEC_SIGN_OBJECT_002 T.1), so the exterior form is the factor ζ(½+iτ) with a Möbius mollifier,
   placed in the test-function slot; it is the mollifier case of the factor-ζ route. NO-GO for the reading of
   DOSSIER §6(d) "natural candidate for clause (5)" (identity PROVED; classification ARGUED, definitional).
5. Construction. (a) The never-attempted "layer edges κ_{T+log n}" residue is void: all per-dilate cuts sit at one
   point of the tail variable, where the tail is C¹-flat for core data by a Poisson relation (Lemma 2.1), and every
   edge term is archimedean, hence identical for all combs (Proposition 2.2). NO-GO, PROVED. (b) The "coupling of the
   non-integer classes to φ_0" (rem:ext-latno) has no freedom: φ_0 enters 𝒲 only through the forced polar
   compensator with scalar σ_g(0)·M̃_1(N) (Proposition 2.3, PROVED; this is the relocated pole of
   PROOF_L_SHARP_II_001). (c) DOSSIER §6(g) made quantitative: (ext-L) forces unit near-minimizers to lie within
   explicit distance of E applied to a prolate span of dimension 4N+O(log²N); with the measured margin law it forces
   concentration on a fixed, N-independent number of prolates (Proposition 2.4, CONDITIONAL). This locates the only
   place where a sign for (ext-L) could still sit: the second-order term of the Γ-limit of K3_GAMMA_001 on a finite
   prolate sector.

No sign is proved. Result: NO-GO with class (see the last section).

---------------------------------------------------------------------------------------------------------------------
## Corpus check

Searched: ROUTES-TRIED-INDEX/README.md (lines 448–535: phase 199 proof-L-sharp, phase 200 sign object, phase 202),
the grid, phase-199-frontier-pattern (AUDIT_199, MECH_001, PATTERN_001, proof-L-sharp/), phase-200-sign-object
(K1_OSG_001, K3_GAMMA_001, SPEC_SIGN_OBJECT_002, AUDIT_200_SPEC_002, PI_MU_001), phase-202-exterior-plank
(README, BUILD_R2_001, WORK_STATE).

What closed each prior attempt on this object, and why.

- **Lemma L′ / L′♯ (MECH_001, AUDIT_199).** L′ (leakage of a fixed representative) is false by the gauge: f supported
  in (−1/λ,1/λ) with f(0)=∫f=0 has Ef=0 and leak(f)>0. Repaired as L′♯ = prob:ext-L with gauge-minimised ℓ; OPEN.
  MECH_001 proved L′ ⇒ λ^W>0 ∀T (now thm:ext-margin).
- **MM_001 (Barkhausen / passivity of the exterior loop).** The prime channel is strictly positive-real, but the full
  loop on the line is lossless: archimedean part and collapsed comb cancel through ∂_σ|Γ_ℝζ|² = 0 on Re s = ½. Any
  passivity / small-gain / Nyquist margin is the truncation energy, which is W_T itself: circular. NO-GO.
  (NN_001: local factors are PR; (1−z)^{−c} PR iff c ≤ 1 — c-specific, not Λ-specific; dissipation inequality = L′♯.)
- **K1 OS-Γ reflection (K1_OSG_001).** The reflection identity at the edge x = T with a completely monotone kernel of
  Γ_ℝ poles is false: W_T is Toeplitz in Ψ̌ and window atoms pair translates by ratios N′/N; the reflected
  contribution is a Möbius correlation, comb-generic. Restriction R-K1: every Hankel form using the gap [2,μ) has
  NN′ product structure and cannot carry the sign. NO-GO PROVED.
- **K3 Γ-limit (K3_GAMMA_001).** Renormalising by leakage on the ψ_{4j} sector at c = 2πμ → ∞, the Γ-limit
  𝒩_μ/log 2μ = ‖b‖² is identical for cΛ (every c), Beurling and deleted primes; Λ enters only the O(1) term Q₁. The
  limit loses the sign. NO-GO as a route; Lemma K3.1 kept as a tool; Q₁ OPEN.
- **SQ (AUDIT_200_SPEC_002).** By SQ.0 every mollified exterior is −g modulo the radical at any level: the Selberg
  square yᵀ𝔅y equals 𝒲[g]. Tautological (REF-D). Q2 ladder likewise (Lemma R: levels, classes, divisor bands are
  coordinates inside the radical).
- **Phase 202.** Lemma M: every Möbius sum of archimedean pairings of tail dilates is ∫m|r̂̃|²D_N(½−iτ)dτ, the
  1/ζ channel (C6, closed). Residue left with no proposal: "layer edges κ_{T+log n}".

Is the fused-object reading a new reason? **No.** The statement "the exact Λ lives in the radical inclusion
𝒢̄_T ⊂ rad 𝒲 and in the intertwiner Z (Poisson over ℤ, a_n ≡ 1), nonexistent for Beurling/cΛ/DH" is
AUDIT_200_PIMU_001; "the identity requires L_a = ζ; with E_a adapted, W^{(cΛ)}(Φ) = −(c−1)(arch+pole)(Φ)" is
PROOF_L_SHARP_C_001; "a_P, cΛ, DH already fail in the quotient" is R-Q6 (AUDIT_200_SPEC_003). The fusion is
therefore known, and none of the closures above relied on comb-genericity of the half-line identity: MM_001 died of
circularity (lossless loop), K1 of NN′ product structure, K3 of a comb-generic leading order, SQ of tautology. The
fused reading touches none of these reasons. What this memo adds that is not in the index: a zero-free proof of the
radical lemma (§1.1), the sign analysis of the defect and of the cell cancellation (§1.3–1.6), the void status of the
layer-edge residue (§2.1–2.2), the explicit φ_0 reduction (§2.3) and the quantitative form of §6(g) (§2.4).
Overlaps to state: Lemma 2.1 refines FF.2 of PROOF_L_SHARP_FF_001 (edge jet = reflected window jet); Proposition 2.3
is the relocated pole of PROOF_L_SHARP_II_001; Proposition 2.4 is consistent with K3.1 (leak saturated by ψ₀, ψ₄).

---------------------------------------------------------------------------------------------------------------------
## 1. The half-line identity and its falsifiers

### 1.0 Setting
f admissible at T (even, supp ⊂ [−λ,λ], C² on [−λ,λ], f(0) = 𝓕f(0) = f(λ) = 0). Since f is even and C² with
f(0) = 0, f′(0) = 0 and f(u) = O(u²) at 0; hence Mf(s) is holomorphic on Re s > −2. One integration by parts
(f(λ) = 0) gives Mf(σ+it) = O_σ(1/|t|) on vertical strips. Mf(1) = ∫_0^∞ f = ½𝓕f(0) = 0.

Φ_f(x) = e^{x/2}Σ_{n≥1}f(ne^x). Each term is continuous on ℝ (f is continuous on ℝ, f(±λ) = 0), the sum is locally
finite on x > −∞, so Φ_f is continuous; Φ_f = 0 on [T,∞). By Poisson summation, Φ_f(x) = e^{−x/2}Σ_{k≥1}𝓕f(ke^{−x}),
and 𝓕f(ξ) = O(ξ^{−2}), so Φ_f(x) = O(e^{3x/2}) as x → −∞. Hence Φ̃_f(s) is holomorphic on Re s > −1, and for
Re s > 1, Φ̃_f(s) = Σ_n ∫ f(ne^x)e^{sx}dx = ζ(s)Mf(s). By uniqueness of continuation, Φ̃_f = ζ·Mf on Re s > −1 (the pole
of ζ at 1 is cancelled by Mf(1) = 0).

Bilinear complete form (real functions, polarisation of def:ext):
  𝒲(F,G) = (1/2π)∫ m F̂ Ĝ̄ − Σ_{n≥2} Λ(n)n^{−½}[⟨F,G(·−log n)⟩ + ⟨F,G(·+log n)⟩] + A(F)B(G) + B(F)A(G),
A(F) = F̃(1), B(F) = F̃(0).

### Theorem 1.1 (radical lemma, zero-free proof). PROVED.
For f admissible at T and G ∈ C_c^∞(ℝ), 𝒲(Φ_f, G) = 0. The same holds for G = Φ_{f′} or G = Ψ_{f′} with f′ admissible.

*Proof.* Write F = Φ_f. Parseval in Mellin form: ⟨F, G(·−a)⟩ = (1/2πi)∫_{(σ)} F̃(s)G̃(1−s)e^{−(s−½)a}ds for every σ in
the common strip (here −1 < σ; G̃ is entire and decays faster than any power of |Im s| on vertical strips).
Comb, first half: summing over n with a = log n requires σ > 1, and Σ_n Λ(n)n^{−s} = −ζ′/ζ(s):
  C₁ = (1/2πi)∫_{(σ₁)}(−ζ′/ζ)(s)ζ(s)Mf(s)G̃(1−s)ds = (1/2πi)∫_{(σ₁)}(−ζ′(s))Mf(s)G̃(1−s)ds,   σ₁ ∈ (1,2).
Comb, second half (a = −log n): Σ_n Λ(n)n^{−½}n^{s−½} = −ζ′/ζ(1−s) needs σ < 0; by the functional equation
ζ(s) = χ(s)ζ(1−s), (ζ′/ζ)(1−s)ζ(s) = χ(s)ζ′(1−s), so
  C₂ = (1/2πi)∫_{(σ₂)}(−χ(s)ζ′(1−s))Mf(s)G̃(1−s)ds,   σ₂ ∈ (−1,0).
(Absolute convergence of the comb sums at these abscissae: F = O(e^{3x/2}) at −∞ and G compact.)
Both integrands are holomorphic in −1 < Re s < 2 except at s = 1 (first) and s = 0 (second): ζ′ has only the double
pole at 1; χ(s)ζ′(1−s) has a pole only where ζ′(1−s) does, s = 0 (χ is holomorphic on Re s < 1). No other singularity
is crossed; in particular nothing depends on where ζ vanishes. Polynomial growth of ζ′, χ on vertical strips,
Mf = O(1/|t|) and the rapid decay of G̃ justify moving both lines to Re s = ½.
Residue at s = 1: −ζ′(s) = (s−1)^{−2} + O(1), Mf(s) = Mf′(1)(s−1) + O((s−1)²), so the residue is Mf′(1)G̃(0). Since
F̃(1) = lim_{s→1}ζ(s)Mf(s) = Mf′(1) = A(F) and G̃(0) = B(G), moving left gives C₁ = L₁ + A(F)B(G).
Residue at s = 0: χ(s) = s/2 + O(s²) (from χ(s) = ζ(s)/ζ(1−s), ζ(0) = −½, ζ(1−s) = −1/s + O(1)) and
ζ′(1−s) = −s^{−2} + O(1), so −χ(s)ζ′(1−s) = 1/(2s) + O(1), residue ½Mf(0)G̃(1). Since B(F) = F̃(0) = ζ(0)Mf(0) = −½Mf(0) and
A(G) = G̃(1), moving right gives C₂ = L₂ − (−B(F)A(G)) = L₂ + B(F)A(G).
On the line: L₁ + L₂ = (1/2πi)∫_{(½)}[−ζ′(s) − χ(s)ζ′(1−s)]Mf(s)G̃(1−s)ds. Differentiating ζ(s) = χ(s)ζ(1−s):
ζ′(s) + χ(s)ζ′(1−s) = χ′(s)ζ(1−s) = (χ′/χ)(s)ζ(s). With χ(s) = π^{s−½}Γ((1−s)/2)/Γ(s/2),
(χ′/χ)(½+iτ) = log π − ½ψ(¼−iτ/2) − ½ψ(¼+iτ/2) = −m(τ). Hence L₁ + L₂ = (1/2πi)∫_{(½)} m F̃(s)G̃(1−s)ds, which is the
archimedean term. Therefore 𝒲(F,G) = Arch − (L₁+L₂) − A(F)B(G) − B(F)A(G) + A(F)B(G) + B(F)A(G) = 0.
For G = Φ_{f′} or Ψ_{f′}: G̃ is holomorphic on Re s > −1 (decay e^{3x/2} at −∞, G = 0 on [T,∞)) and O(1/|t|) on vertical
lines (G bounded with one jump at most); the integrands are then O(|t|^{A−2}) with A < 1 on the lines used
(|ζ′(½+it)| ≪ |t|^{1/4+ε}, |χ(σ₂+it)| ≍ |t|^{½−σ₂}), the horizontal segments vanish, and the residue computation is
identical. ∎

### Corollary 1.2 (half-line identity). PROVED.
W_T(Ef) = 𝒲[Ψ_f], with Ψ_f = Φ_f 1_{(−∞,−T)}, and |Ψ_f(y)| ≤ Ce^{3y/2}.
*Proof.* Ef = Φ_f − Ψ_f a.e. on ℝ, and W_T(Ef) = 𝒲[Ef] for a function supported in Ī_T (the comb terms with
log n ≥ 2T vanish). 𝒲[Ef] = 𝒲[Φ_f] − 2𝒲(Φ_f,Ψ_f) + 𝒲[Ψ_f] = 𝒲[Ψ_f] by Theorem 1.1 applied twice. ∎

The inputs are (I) coefficients 1 on ℕ (Φ̃_f = ζ·Mf), (E) −(ζ′/ζ)·ζ = −ζ′ has no singularity besides s = 1, which is
Λ∗1 = log, and (F) the functional equation with χ′/χ = −m on the line (Γ_ℝ, conductor 1). The residue bookkeeping uses
ζ(0) = −½ and the residue 1 at s = 1. All four are used at once; none can be dropped.

### Proposition 1.3 (the defect for an arbitrary comb). PROVED.
Let w ≥ 0 be any comb weight with Σ w(n)n^{−σ} < ∞ for σ > 1, 𝒲^w the complete form with Λ replaced by w, and
𝒫_u the bilinear comb form with weight u (so 𝒲^w = 𝒲 + 𝒫_{Λ−w}). For f admissible,
  W^w_T(Ef) − 𝒲^w[Ψ_f] = 𝒫_{Λ−w}[Ef] − 𝒫_{Λ−w}[Ψ_f].
*Proof.* W^w_T(Ef) = 𝒲[Ef] + 𝒫_{Λ−w}[Ef] = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ef] (Corollary 1.2), and 𝒲^w[Ψ_f] = 𝒲[Ψ_f] + 𝒫_{Λ−w}[Ψ_f]. ∎
Instances. (a) w = cΛ: 𝒫_{(1−c)Λ} = (1−c)𝒫_Λ, and by the proof of Theorem 1.1, 𝒫_Λ(Φ_f,·) = 𝒜𝒫(Φ_f,·) with 𝒜𝒫 the
archimedean-plus-pole form; the defect is (1−c)(𝒫_Λ[Ef] − 𝒫_Λ[Ψ_f]). (b) w = a_P (all primes p < P deleted): the
natural summation map with coefficients 1_{(n,∏_{p<P}p)=1} is Φ_{f_P}, f_P = Σ_{d|∏_{p<P}p}μ(d)f(d·), again an
admissible function; Theorem 1.1 makes it radical for 𝒲, not for 𝒲^{a_P}, and the defect is
𝒫_{Λ1_{P-smooth part}}[E f_P] − 𝒫_{…}[Ψ_{f_P}], where the comb runs over prime powers p^k, p < P. (When P > N, E f_P = Ef
since f(d·) for d ≥ P > N is a gauge element.) (d) w = Λ + e, e finitely supported: defect −𝒫_e[Ef] + 𝒫_e[Ψ_f].

### Proposition 1.4 (no common radical vector for c ≠ 1). PROVED.
If c ≠ 1 and F ∈ L²(ℝ) with F = O(e^{3x/2}) at −∞ and F = 0 on [T,∞) lies
in the radical of both 𝒲 and 𝒲^c (against C_c^∞), then F = 0.
*Proof.* 𝒲^c − 𝒲 = (1−c)𝒫_Λ, so F is in the radical of 𝒫_Λ and hence of 𝒜𝒫 = 𝒲 + 𝒫_Λ. Radicality of 𝒜𝒫 against
C_c^∞ means m(D)F = −B(F)e^{x/2} − A(F)e^{−x/2} as distributions. The left side is tempered (F ∈ L², m of logarithmic
growth); the right side is tempered only if A(F) = B(F) = 0. Then m(τ)F̂(τ) = 0 a.e., and m vanishes only at ±t₀, so
F̂ = 0 a.e. ∎
So no function is simultaneously the summation image for Λ and for cΛ. Whether some other coefficient sequence a
(D_a ≠ ζ) makes Φ^a_f radical for 𝒲^c: by the computation of Theorem 1.1 this needs a Dirichlet series D with
−c(ζ′/ζ)·D free of singularities in the strip and a functional equation whose gamma factor gives m; for D = ζ^c the
gamma factor is Γ_ℝ^c and ζ^c is not meromorphic, and the Hamburger-type rigidity (functional equation with Γ_ℝ,
conductor 1, finite order, one pole ⇒ multiple of ζ) excludes all others. ARGUED (Hamburger's theorem CITED; the
reduction of "radical" to "functional equation" is argued, not proved, for general D). For Beurling systems: no
functional equation is available, same conclusion, ARGUED.

### Proposition 1.5 (the c-exterior value is not a function of g). ARGUED.
For c ≠ 1, f ↦ 𝒲^c[Ψ_f] is not constant on the fibre {f admissible: Ef = g}.
*Reduction (PROVED).* For φ ∈ 𝒢_T, Ψ_{f+tφ} = Ψ_f + tΦ_φ and Φ_φ is 𝒲-radical, so
𝒲^c[Ψ_{f+tφ}] − 𝒲^c[Ψ_f] = (1−c)(2t𝒜𝒫(Ψ_f,Φ_φ) + t²𝒜𝒫[Φ_φ]), a polynomial in t with leading coefficient
(1−c)𝒜𝒫[Φ_φ]. So the claim follows from: 𝒜𝒫[Φ_φ] ≠ 0 for some φ ∈ 𝒢_T.
*Argument for the last step (ARGUED).* Take φ in the gauge oscillating at Mellin frequency Ω on a fixed dyadic piece of
(0,1/λ); then Φ_φ has its Fourier mass near |τ| ≈ Ω, so ⟨m(D)Φ_φ,Φ_φ⟩ ≈ log(Ω/2π)‖Φ_φ‖² → +∞ relative to ‖Φ_φ‖²,
while the rank-two pole term 2A(Φ_φ)B(Φ_φ) tends to 0 relative to ‖Φ_φ‖² by Riemann–Lebesgue; the error control is that of
lem:ext-osc, not written out here.
Consequence: for c ≠ 1 there is no "exterior form on the gauge quotient". This is R-Q6 in explicit form.

### 1.6 Does the failure carry a sign?
(i) The defect of Proposition 1.3(a) is (1−c)(𝒫_Λ[Ef] − 𝒫_Λ[Ψ_f]); 𝒫_Λ[Ef] = Σ v_n c_g(log n) has no sign on the core
(take g concentrated near one contact), and 𝒫_Λ[Ψ_f] has no sign either (prop:ext-pairs: the diagonal class is
positive on shallow bumps and −D² on deep ones). Indefinite. PROVED (by these two examples).

(ii) The cell cancellation. **Lemma 1.6 (comb monotonicity on cells). PROVED.** Under the hypotheses of
lem:ext-cell (supp ϱ ⊂ [J+δ, J+1−δ]), the comb contribution to 𝔔^w[ϱ] is −2‖ϱ‖²Σ_{n≤J}(w∗1)(n)/n (lem:ext-cell(ii)). It
is ≤ 0 and nonincreasing in w pointwise. Hence for every w ≤ Λ pointwise (cΛ with 0 ≤ c ≤ 1; a_P, where
(a_P∗1)(n) = log n − Σ_{p<P}v_p(n)log p ≤ log n; Λ − e with e ≥ 0 finitely supported), 𝔔^w ≥ 𝔔 on single-cell data,
and every positivity statement for 𝔔 on single-cell chirps (cor:ext-cellpos) holds verbatim for 𝔔^w.
*Proof.* Monotonicity of a sum with nonnegative coefficients 1/n against w∗1, and (w∗1) ≤ (Λ∗1) when 0 ≤ w ≤ Λ. ∎
Falsifier test of "cell positivity" as a sign step: it fails for cΛ with c > 1 (cor:ext-cfals(ii)) and survives
(a) cΛ with c < 1, (b) a_P, (d) every downward finite modification. It is therefore not a sign step for (★). The
"detection of c > 1" is comb monotonicity, not a Λ-specific mechanism: any statement on a cone where the comb pairing
is a nonnegative functional of w∗1 detects upward perturbations and is blind to downward ones. NO-GO for the key
cancellation as a sign source, PROVED (class: statements on cones of data with sign-definite comb pairing).

(iii) Note on what cor:ext-cfals(ii) proves. 𝔔^{c′}[ϱ] is the c′-window form at T₀ = ½log(J+1) evaluated on the window
function Ψ̌_ϱ (translation invariance); it is not the c′-window form in exterior coordinates, which by
Proposition 1.3 is 𝔔[ϱ] + (1−c′)𝒫_Λ[Ef]. So cor:ext-cfals(ii) exhibits a negative direction of the c′ > 1 window form
(correct, PROVED there), but it is not a property of the exterior representation of the c′ problem.

### 1.7 Verdict on DOSSIER §6(d)
- Comb-genericity of the half-line identity: FALSE as claimed in §ext-constraints item 2. PROVED (Theorem 1.1 shows the
  exact inputs; Propositions 1.3–1.5 the failure). Already recorded in the corpus (C_001, R-Q6, PIMU).
  Correction for Paper 47 when it is next edited: item 2 should read "…hold for the comb Λ only; for cΛ, a_P and
  Beurling systems the window form in exterior coordinates acquires the window term 𝒫_{Λ−w}[Ef] − 𝒫_{Λ−w}[Ψ_f], and
  for cΛ no summation map is radical (Prop. 1.4)". (No edit made: phase rule.)
- Clause (5) of prop:spec. In Mellin coordinates, for g in the core with admissible representative f and φ₀ fixed as in
  §2.3, Ψ̃_f = Φ̃_f − g̃ = ζ·Mf − g̃ and Mf = M_N·g̃ + (polar/gauge terms), M_N(s) = Σ_{m<N}μ(m)m^{−s} (lem:ext-mob), so
  Ψ̃_f = (ζM_N − 1)g̃ + (gauge/polar) — SPEC_SIGN_OBJECT_002 T.1. The exterior form is 𝒲 evaluated on the product of
  the test function with the mollified factor ζ(½+iτ)M_N(½+iτ) − 1. Its coupling of Λ(n), n < N, with the functional
  equation runs through the factor ζ(½+iτ) (with a Möbius mollifier), i.e. through the route that clause (5) asks to
  avoid; specifically it is the mollifier case of thm:spec-K2 (ARGUED there). NO-GO for "first object meeting
  clause (5)". Label: the identity is PROVED; the classification is a reading of the clause (ARGUED).

---------------------------------------------------------------------------------------------------------------------
## 2. Construction toward (ext-L)

### Lemma 2.1 (the edge is one point and is flat). PROVED.
(a) Φ_f is continuous on ℝ, so Ψ_f(−T⁻) = g(−T⁺). If N ∉ ℤ, Φ_f is C¹ near −T and Ψ_f′(−T⁻) = g′(−T⁺). For g in the core
both vanish: the tail matches the window to first order at the edge.
(b) In the universal frame (ϱ(X) = λr(λX), u(x) = e^{x/2}ϱ(e^x), u_n(y) = u(y+log n)1_{y>0}): all dilates are cut at the
same point y = 0, with jumps u_n(0⁺) = n^{−½}·n^{½}ϱ(n) = ϱ(n), and
  Ψ̌_ϱ(0⁺) = Σ_{n≥1}ϱ(n) = Σ_{1≤k<N}h(k),   h(t) = f(t/λ)   (Poisson over ℤ, h even, 𝓕h(0) = h(0) = h(N) = 0),
which is λ^{½}·(Ef)(−T) = 0 on the core.
*Proof.* (a) Each term e^{x/2}f(ne^x) is continuous on ℝ; the sum is locally finite. Its derivative has jumps only where
ne^x = λ (jump of f′ at λ), i.e. x = T − log n; at x = −T this needs n = N. (b) Σ_{n∈ℤ}𝓕h(n) = Σ_{k∈ℤ}h(k), with
𝓕h even and 𝓕h(0) = 0, h(0) = 0, supp h ⊂ [−N,N], h(N) = 0. The relation to Ef(−T) is the definition of E at x = −T:
Ef(−T) = λ^{−½}Σ_{n<N}f(n/λ). ∎
So the "layer edges κ_{T+log n}" are, in the tail variable, a single edge carrying the jumps ϱ(n) of the individual
dilates, whose sum is forced to vanish (to first order) by Poisson summation. Splitting by layers replaces a C¹-flat
function by pieces with jumps whose absolute sum Σ|ϱ(n)| is not small; any bound applied layer by layer loses this
cancellation. (This refines FF.2 of PROOF_L_SHARP_FF_001.)

### Proposition 2.2 (edge terms are comb-free). PROVED.
For Ψ supported in [0,∞) (tail variable), the archimedean part is
  ⟨m(D)Ψ,Ψ⟩ = C₀‖Ψ‖² + ¼∬_{(0,∞)²}|Ψ(x)−Ψ(x′)|²K(|x−x′|)dx dx′ + ∫_0^∞|Ψ(y)|²κ(y)dy,   κ(y) = ½∫_y^∞K(t)dt,
and in any decomposition Ψ̌ = Σ n^{−½}u_n the per-layer edge terms are polarisations of the last integral and of the
cross terms of the double integral across y = 0. All of them involve K and C₀ only.
*Proof.* lem:K applied to the zero extension; the cross region x > 0 > x′ gives ½∫|Ψ(x)|²∫_{−∞}^0K(x−x′)dx′dx. ∎
Falsifier test: every edge term is identical for Λ, cΛ, a_P, Beurling data and finite modifications (the comb does not
enter); hence no bound on edge terms can be a sign step. With Lemma 2.1, κ(y) ~ ½log(1/y) is integrated against
|Ψ̌(y)|² = O(y⁴) for core data (N ∉ ℤ), so the edge term is a bounded, smooth archimedean functional with no
singular part. **The layer-edge residue is void: NO-GO, PROVED (class: archimedean-only terms).**

### Proposition 2.3 (the coupling to φ₀ is a forced scalar). PROVED.
Let g be in the core, 𝗉 and σ_g as in thm:ext-lattice, f = Σ_{m<N}μ(m)𝗉(m·) + φ₀ admissible. Put
I(g) := ∫Σ_{m<N}μ(m)𝗉(m·) = σ_g(0)·M̃₁(N), M̃₁(N) = Σ_{m<N}μ(m)/m. Fix once and for all an even φ_* ∈ C²,
supp φ_* ⊂ [−1/λ,1/λ], φ_*(0) = 0, ∫φ_* = 1, with the C²-matching data of 𝗉 at ±1/λ. Then φ₀ = −I(g)φ_* + φ_𝒢 with
φ_𝒢 ∈ 𝒢_T, and
  W_T(g) = 𝒲[Σ_m μ(m)Υ_m − I(g)Υ_*],   Υ_* = tail of φ_*,
where neither summand is in the domain of 𝒲 separately (each carries the polar mode e^{y/2} at depth with coefficient
±I(g)), and their sum is.
*Proof.* Admissibility forces ∫φ₀ = −I(g), φ₀(0) = 0 and the matching at ±1/λ; the difference of two such φ₀ is in 𝒢_T,
which is radical (prop:ext-gauge); ∫𝗉(m·) = σ_g(0)/m. The polar growth: Φ_φ(x) ~ e^{−x/2}∫φ as x → −∞. ∎
Consequence for rem:ext-latno: the non-integer classes a ≥ 2 couple to φ₀ only through one scalar, I(g) =
σ_g(0)M̃₁(N), with |M̃₁(N)| ≤ 1; for a_P the same holds with Σ_{m<N, P∤m}μ(m)/m, bounded by (1−P^{−1})^{−1}
(rem:ext-latno(c)). A bound using only the size of this scalar is comb-generic. The pointer of rem:ext-latno
therefore reduces to: the Gram form of 𝒲 on {Υ_m}_{m<N squarefree} ∪ {Υ_*} with the fixed vector (μ(m))_m ⊕ (−I(g)).
That is prop:ext-latred with Υ₀ replaced by I(g)Υ_*; positivity on the span is stronger than needed (rem:ext-latno(b)).
No sign. (The polar relocation is PROOF_L_SHARP_II_001.)

### Proposition 2.4 (what (ext-L) says about near-minimizers). CONDITIONAL on (ext-L).
Let ψ_k be the prolate functions of [−λ,λ] with bandwidth λ (c = 2πN), normalised in L²[−λ,λ], with concentrations
χ_k. Assume (ext-L) with (κ, A₀). Let g be a unit vector in the core with W_T(g) ≤ η. Then for every ε′ ∈ (0,1),
  dist(g, E(span{ψ_k : 1−χ_k ≤ ε′})) ≤ 2N^{½}(ηN^{A₀}/(κε′))^{½}.
*Proof.* (ext-L) gives ℓ(g) ≤ ηN^{A₀}/κ. Take an admissible f with Ef = g and leak(f) ≤ ℓ(g) + δ. Expanding
f = Σa_kψ_k, double orthogonality gives leak(f) = Σ|a_k|²(1−χ_k), so the part f_> on {1−χ_k > ε′} has
‖f_>‖² ≤ (ℓ+δ)/ε′; ‖E‖ ≤ 2√N (lem:ext-mob); let δ → 0. ∎
(i) With the PROVED upper bound λ^W_T ≤ λ_A(T) ≤ 4·10⁹T·N^{−7.72} (T ≥ 1; cor:margin1) and η = 2λ^W_T: unit
near-minimizers lie within 2(8·10⁹T)^{½}κ^{−½}N^{(A₀−6.72)/2}ε′^{−½} of E(span{ψ_k: 1−χ_k ≤ ε′}). With ε′ = N^{−B}
the span has dimension 4N + O(log N·log(N^B)) (Landau–Widom count, CITED; half of it for even f), and the bound is
o(1) as soon as A₀ + B < 6.72. So: **(ext-L) with A₀ < 6.72 forces near-minimizers to be o(1)-close to E of the
bulk prolate span**, an N-dependent subspace of dimension ≈ 4N. This is the quantitative form of DOSSIER §6(g).
(ii) With the measured margin law λ^W ≈ κ′μ^{9/2}e^{−4πμ} (PATTERN_001, NUMERICAL, μ = N) and the asymptotic
1−χ_k ~ √π2^{3k+2}c^{k+½}e^{−2c}/k! (CITED, Slepian, Fuchs), the ratio (1−χ_k)/(1−χ₀) ~ (8c)^k/k! grows like N^k, so the
choice ε′ = N^{a}(1−χ₀) with a > A₀ + 5.5 gives: the minimal-leakage representative of a near-minimizer lies, up to
an o(N^{−½}) error in L², in span{ψ₀,…,ψ_K} with K = K(A₀) independent of N. CONDITIONAL (on (ext-L) and on the
NUMERICAL margin law).
Structural reading. Under (ext-L), the decision at the minimizer sits in a fixed, finite prolate sector, and the
relevant matrix is prop:ext-consol(b) restricted to k ≤ K. On that sector the leading order of 𝔔/leak is the Γ-limit of
K3_GAMMA_001, which is comb-generic; Λ enters only through the O(1) correction Q₁. So, if (ext-L) is true with small A₀,
**the whole Λ-dependence at the minimizer is the term Q₁ on span{ψ₀,…,ψ_K}**. This is consistent with the recorded
numerics (Mori μ = 15: background = E f_P with f_P ∈ span{ψ₀,ψ₄}, overlap 0.99981; staircase λ_j(W_T) ≈
(1.5–4)(1−χ_{4j}); W_T(g*) = 4.978·10⁻⁷⁰ against ℓ(g*) ≤ 8.5·10⁻⁷⁰, ratio ≥ 0.59), so it is not falsified. It is not a
proof of anything: it constrains near-minimizers given (ext-L), and the converse direction (knowing the minimizer
lies in the sector) is a functional of the minimizer (Theorem X wall).
Falsifier status: Proposition 2.4 is a consequence, not a sign step; for cΛ with c > 1, (ext-L) is false and the
statement is vacuous.

### 2.5 The non-integer classes: what was tried and where it stops
By Proposition 2.3 the lattice reduction is v_gᵀ𝔊v_g with v_g = (μ(m))_{m<N}⊕(−I(g)), Gram 𝔊 of 𝒲 on
{Υ_m}∪{Υ_*}. The integer classes (a = 1) have coefficients 𝖼_b = M̃₁(N) → 0, comb-generic in size (rem:ext-latno(c)).
The classes a ≥ 2 have 𝖼_{b/a} = μ(a)a^{−1}M̃_a(N/a). The only Λ-specific content would be a signed correlation of
these Möbius means with the Gram entries 𝒲(s_q, s_{q′}) — but by Lemma M of phase 202 every Möbius sum of archimedean
pairings of dilates collapses to ∫m|r̂̃|²D_N(½−iτ)dτ (the 1/ζ channel, closed), and by R-Q2 the classes are coordinates
inside the radical. I found no inequality on 𝔊 restricted to a ≥ 2 that is not either a size bound (comb-generic) or
a rewriting of 𝒲[g]. OPEN; no attempt beyond this is justified without a new identity.

---------------------------------------------------------------------------------------------------------------------
## Result

**NO-GO with class.** (1) The fused reading of the exterior form: the half-line identity is indeed Λ-specific (PROVED,
with a zero-free proof), but the failure for cΛ, a_P, finite modifications carries no sign, the cell cancellation is
comb monotonicity (fails the falsifier test for c < 1, a_P, downward modifications), and the fusion is the factor
ζ(½+iτ) with a Möbius mollifier, so it does not meet clause (5). Class: objects whose Λ-dependence is the radical of
𝒲 (multiplication by ζ in Mellin). (2) The layer-edge residue of phase 202 is void (single flat edge; archimedean-only
terms). (3) The coupling of the non-integer classes to φ₀ is a forced scalar.

## What was proved
- Theorem 1.1 / Corollary 1.2: radical lemma and half-line identity with a zero-free proof; exact inputs (I),(E),(F),
  ζ(0) = −½, residue 1. PROVED.
- Proposition 1.3: defect formula for any comb w. PROVED.
- Proposition 1.4: no common radical vector for 𝒲 and 𝒲^c, c ≠ 1. PROVED. (Nonexistence of any summation map for cΛ,
  Beurling: ARGUED.)
- Proposition 1.5: c-exterior value is not gauge invariant for c ≠ 1. Reduction PROVED, last step ARGUED.
- Lemma 1.6: comb monotonicity on single-cell data; cell positivity holds for every w ≤ Λ. PROVED.
- Lemma 2.1: tail continuity/C¹ at the edge; Ψ̌(0⁺) = Σϱ(n) = Σ_{k<N}h(k) = 0 on the core. PROVED.
- Proposition 2.2: edge terms are archimedean-only. PROVED.
- Proposition 2.3: φ₀ enters only through I(g) = σ_g(0)M̃₁(N). PROVED.
- Proposition 2.4: near-minimizer concentration under (ext-L). CONDITIONAL (part (ii) also on a NUMERICAL law).

## What failed and why
- Using the fusion as a sign source: the defect between Λ and the falsifiers is (1−c)(𝒫_Λ[Ef] − 𝒫_Λ[Ψ_f]), indefinite in
  both terms (§1.6(i)). The only sign-definite comb pairing found (single cells) is monotone in the comb and so blind
  to downward perturbations (Lemma 1.6).
- Clause (5): the exterior datum is (ζM_N − 1)g̃ in Mellin; the coupling to the functional equation is through ζ(½+iτ).
- Layer edges: they are one edge (Lemma 2.1), and edge terms contain no comb (Proposition 2.2).
- Non-integer classes: every Möbius-weighted sum of archimedean dilate pairings collapses to the 1/ζ channel (Lemma M,
  phase 202); no inequality on the a ≥ 2 block was found that is not a size bound or a rewriting.

## Next concrete step
Proposition 2.4(ii) isolates the only place left for a Λ-specific sign on the exterior form, if (ext-L) holds with
small A₀: the O(1) correction Q₁ of K3_GAMMA_001 on the fixed sector span{ψ₀,…,ψ_K} (K ≈ A₀ + 6). Write Q₁ exactly as a
K×K matrix in the comb weights (it is linear in w through the (1,n) resonances of thm:ext-layer(iv) and the cell
weights 𝔴_N), and decide by pure computation whether Q₁ separates Λ from cΛ (c < 1) and from a_P. If Q₁ is monotone in
w, the exterior route is closed by Lemma 1.6's class; if not, the K×K matrix is the first finite object on which a
Λ-specific sign can be tested.
