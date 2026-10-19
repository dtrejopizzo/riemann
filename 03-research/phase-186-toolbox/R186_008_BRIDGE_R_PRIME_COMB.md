# R186.008 — The bridge: R = P E (1−P) F_∞ P and the prime comb of 2

Model of R186.003/007: L²(ℝ₊,du), P = 1_{(0,λ]}, F_∞ kernel 2cos(2πux), E = Σ_{k≥0} D_{2^k}, F_S = E F_∞ E⁻¹.

## Status

| # | Statement | Label |
|---|---|---|
| B | R = Σ_{k≥1} 2^{−k/2} P T_{k log 2} (1−P) F_∞ P in the logarithmic variable, with 2^{−k/2} = v_{2^k}/(2Λ(2^k)) | PROVED (trivial; see warning in §2) |
| C | F_S = F_∞ U, U = e^{iφ(D)} unimodular scale multiplier, φ'(t) = −Σ_{k≥1} v_{2^k} cos(kt log 2) **exactly** | PROVED |
| C' | Tr(ϑ(h)(P̂^S − P̂_∞)) = Σ_{k≥1} log 2 · 2^{−k/2}(h(2^k)+h(2^{−k})) **exactly**, for all λ and all Schwartz h; density ρ_{1−P̂^S} − ρ_{1−P̂_∞} = −(1/2π)Σ_k v_{2^k} cos(kt log 2), with no remainder | PROVED |
| C'' | The same for arbitrary finite S: Σ_{p∈S}Σ_k (comb of p) | PROVED |
| (Δ) | Atom −log2·2^{−1/2} at ±log 2: reproduced without a model for the linear part 1−P̂ | PROVED |
| Π | Density of the nonlinear Sonin projection Π_S = (1−P)∧(1−P̂^S) minus Π_∞ | OPEN (the "comb" part is exact in 1−P̂; the rest lives in the intersection) |
| N | Counting: N(ε) := #{\|λ_n(A_S)\| > ε} ≍ λ² ε^{−2}, i.e. \|λ_n\| ≍ λ n^{−1/2}; Σ_{n≤N} λ_n² ≍ log N | ARGUED (not NUMERICAL: Galerkin N ≤ 40 insufficient) |

Verdict: the bridge exists and is **exact**, but not through R. The correct object is the **scattering
phase** φ of U = F_∞⁻¹F_S: its derivative is the prime comb of the window form, coefficient by coefficient
(Λ appears via the logarithmic derivative), and the Birman–Krein/Toeplitz trace formula for half-lines turns this
into an exact trace identity, independent of λ. The correspondence "weights of R = v_{2^k}/(2 log 2)" is an
accident of a single prime (it fails for |S| ≥ 2).

## 1. Logarithmic variable

W: L²(ℝ₊,du) → L²(ℝ,dx), (Wf)(x) = e^{x/2} f(e^x), unitary. T_c g(x) := g(x+c), D := −i d/dx, T_c = e^{icD}; in Fourier (t dual to x), T_c is multiplication by e^{ict}. Then
 W D_2 W⁻¹ = 2^{−1/2} T_{log 2}, E = Σ_{k≥0} q^k T^k, E⁻¹ = 1 − qT, E^* = Σ q^k T^{−k}, q := 2^{−1/2}, T := T_{log 2}.
P ↦ P_a := 1_{x ≤ a}, a = log λ. F_∞ reverses the scale: F_∞ D F_∞ = −D (s ↔ 1−s); F_∞² = 1. (Normalization fixed in R186.007: A_∞ reproduces 0.783.)

## 2. Theorem B (PROVED)

(P E (1−P) g)(u) = Σ_{k≥0} 1_{u≤λ} 1_{2^k u>λ} g(2^k u); k = 0 contributes nothing. Hence
 R f(u) = 1_{u≤λ} Σ_{k≥1} 1_{(λ, 2^kλ]}(2^k u) · (F_∞ P f)(2^k u),
and in the variable x:
 **W R W⁻¹ = Σ_{k≥1} 2^{−k/2} P_a T_{k log 2} (1−P_a) F_∞ P_a**,
with the k-th term seeing only the outer Fourier mass in the shell (λ, 2^kλ]. Since v_{2^k} = 2Λ(2^k)2^{−k/2} = 2 log 2 · 2^{−k/2}:
 W R W⁻¹ = (1/(2 log 2)) Σ_{k≥1} v_{2^k} P T_{k log 2}(1−P) F_∞ P.
Normalizations: the factor 2^{−k/2} comes from du (not d*u) via the u^{1/2} unitarization; the cosine vs. full Fourier version only affects F_∞ (kernel 2cos), not the weights.

**Warning (why this is not yet the bridge).** The weights of R are the Dirichlet coefficients of L₂(s) = (1−2^{−s})⁻¹ (all 1·n^{−1/2}), not those of −L₂'/L₂ (Λ(n)n^{−1/2}). For a single prime, Λ(2^k) = log 2 is constant and the two are proportional; for S = {∞,2,3}, E = Σ_{n∈⟨2,3⟩} D_n has weight n^{−1/2} at n = 6, while v_6 = 0. "R = comb" is therefore a single-prime coincidence. The invariant identity is the one in §3.

## 3. Theorem C: scattering phase = prime comb (PROVED)

F_S = E F_∞ E⁻¹ = F_∞ (F_∞ E F_∞) E⁻¹ = F_∞ U, U := E^* E⁻¹ (F_∞ E F_∞ = E^*, R186.007 §1). In the variable x:
 U = (1 − qT)/(1 − qT⁻¹), symbol U(t) = (1 − q e^{ict})/(1 − q e^{−ict}), c = log 2,
a quotient of conjugates: |U(t)| = 1, U(t) = e^{iφ(t)} with φ(t) = 2 arg(1 − q e^{ict}) = −2 Σ_{k≥1} q^k sin(kct)/k. Differentiating:
 **φ'(t) = −2 log 2 Σ_{k≥1} 2^{−k/2} cos(kt log 2) = −Σ_{k≥1} v_{2^k} cos(kt log 2).**
This is exactly the prime-2 term of the symbol θ(s) = m(s) − Σ_n v_n cos(s log n) of R183.018 (s = t). For finite S, U_S = ∏_p U_p, φ_S = Σ_p φ_p, φ_S' = −Σ_{p∈S}Σ_k v_{p^k} cos(kt log p): only prime powers, with the correct Λ (C''). The "−" and the Λ of the Weil prime term are the sign and the logarithmic derivative of the phase of F_S relative to F_∞.

## 4. Theorem C': exact trace identity (PROVED)

**Lemma (half-line trace, absolute-Fourier version).** Let U = Σ_n u_n T_{nc} with Σ_n (1+|n|)|u_n| < ∞, |U(t)| ≡ 1, and ĥ Schwartz, k(x) := (1/2π)∫ĥ(t)e^{itx}dt. Then ĥ(D)(U P_a U^* − P_a) is trace class and
 Tr ĥ(D)(U P_a U^* − P_a) = −(1/2π) ∫ ĥ(t) φ'(t) dt, U = e^{iφ}.
Proof. T_{nc} P_a T_{−mc} = P_{a−nc} T_{(n−m)c} and Σ_{n,m} u_n ū_m T_{(n−m)c} = UU^* = 1, hence
 U P_a U^* − P_a = Σ_{n,m} u_n ū_m (P_{a−nc} − P_a) T_{(n−m)c}.
P_{a−nc} − P_a = −sgn(n) 1_{I_n}, |I_n| = |n|c. ĥ(D) 1_I is trace class with ‖·‖₁ ≤ C_h (1+|I|) (Birman–Solomyak, f(x)g(D) with f,g ∈ ℓ¹(L²): CITED), and the series converges in trace norm by Σ|u_n||u_m|(1+|n|) < ∞. Term by term, the kernel of ĥ(D)T_d is k(x−y+d), trace over I_n = |I_n| k(d):
 Tr = −c Σ_{n,m} n u_n ū_m k((n−m)c) = −(1/2π)∫ ĥ(t) (−iU'(t)) Ū(t) dt = −(1/2π)∫ ĥ φ' dt. ∎
(Sign check: U = T_c gives P_{a−c} − P_a = −1_{(a−c,a]}, trace −c k(0), φ' = c. ✓)
Here u_n: u_1 = −q, u_n = q^{−n}(1−q²) for n ≤ 0, 0 for n ≥ 2: geometric, hypothesis satisfied.

**Theorem C'.** With ϑ(h) := ∫ h(a) a^{1/2} D_a d*a (multiplier ĥ(t) = ∫ h(a) a^{−it} d*a, so that k(x) = h(e^x)), P̂^S := F_S P F_S^*, P̂_∞ := F_∞ P F_∞:
 P̂^S − P̂_∞ = F_∞ (U P U^* − P) F_∞, F_∞ ĥ(D) F_∞ = ĥ(−D),
 **Tr ϑ(h)(P̂^S − P̂_∞) = −(1/2π)∫ ĥ(−t) φ'(t) dt = Σ_{k≥1} log 2 · 2^{−k/2} (h(2^k) + h(2^{−k})).**
Independent of λ, with no o(1) term or remainder: unlike Connes's semilocal trace formula for P̂P (CITED, Selecta 1999, with o(1) as Λ → ∞), the difference of the band projections is exactly the local Weil distribution at 2. In density (R183.021 Thm 3.1, ρ defined by Tr ϑ(g)Πϑ(g)^* = ∫ρ_Π|ĝ|²):
 ρ_{1−P̂^S}(t) − ρ_{1−P̂_∞}(t) = −(1/2π) Σ_{k≥1} v_{2^k} cos(kt log 2)
(as a difference: each density individually diverges). This is the statement, with **zero** remainder, for the linear part 1−P̂. It answers (Δ) of R183.027/029 without the two-edge model: the atom −log 2·2^{−1/2} at ±log 2 is the k = 1 coefficient.

**What is NOT proved.** The target asks for ρ of Π_S = (1−P)∧(1−P̂^S). The intersection is not linear in P̂; Π_S − Π_∞ ≠ (1−P̂^S) − (1−P̂_∞). My reading (not checked against R183.025/029 line by line): the terms ∫c_h ε'_p + ∫|φ|²r_p of the semilocal identity are exactly the contribution of the non-linearity of ∧, and the comb is the linear contribution, which is proved here with zero remainder. The HS character of the remainder ((M) of R183.029) remains OPEN; §2 does not decide it (R is not HS, but R is not the object that carries the comb).

## 5. Counting law of A_S (ARGUED)

Decomposition by shells: the k-th term of A_S is P D_{2^k} F_∞ E⁻¹ P = 2^{−k/2} × (dilation isometry) × 1_{(0,2^kλ]} F_∞ E⁻¹ P. Splitting 1_{(0,2^kλ]} = Σ_{j≤k} 1_{shell_j}, shell_j = (2^{j−1}λ, 2^jλ], shell j appears with total weight Σ_{k≥j} 2^{−k/2} = 2^{−j/2}/(1−q). P → shell_j has time–frequency area ≈ λ·2^jλ, hence (Landau) ≈ λ²2^j singular values of order 1. Thus shell j contributes ≈ λ²2^j eigenvalues of size ≈ 2^{−j/2}, and
 N(ε) ≍ Σ_{j: 2^{−j/2} > ε} λ² 2^j ≍ λ² ε^{−2}, |λ_n| ≍ λ n^{−1/2}, Σ_{n≤N} λ_n² ≍ log N.
Each power 2^j contributes HS² mass = (weight)² × (Landau count) = 2^{−j} · 2^j = O(1): this is the honest form of "Σ 2^{−k} (ℓ² mass of the comb)": the ℓ² mass of the comb cancels exactly against the growth of the shell area, and the logarithmic divergence Σ_j 1 is the non-HS result of R186.007 §3 (where each m contributed ½∫∫χ, consistent). Archimedean (Landau–Widom): N_∞(ε) = (const)λ² + (1/π²) log(λ²) log(1/ε) + o: logarithmic in ε. The excess N(ε) − N_∞(ε) is the entire ε^{−2}-scale count.
Missing: (i) that the shells are nearly orthogonal (the E⁻¹ interleavings and Landau tails between neighboring shells); (ii) the alternating signs are not explained here; (iii) numerical verification (requires N ≫ λ²ε^{−2}; the N ≤ 40 Galerkin of R186.007 is not enough). Label: ARGUED.

## 6. What changes in the toolbox

- New object: the **folded outer Fourier mass** (1−P)F_∞P returned by dyadic dilations (R). It governs the spectrum (§5: n^{−1/2} law, not HS) but NOT the comb.
- The comb that the window form sees is the **derivative of the scattering phase** of F_S relative to F_∞, and it enters the trace via the exact half-line formula (§4). This cleanly separates: (linear) exact comb, with no remainder; (nonlinear) Sonin intersection, where the corrections of R183.025/029 live.
- For |S| ≥ 2, Theorem C'' gives Σ_{p∈S} (comb of p) with no cross terms: the additivity of φ_S is the operator version of Λ supported on prime powers.

## Audit notes

1. Theorem B is a rewriting; it should not be claimed as content. The content is C/C'.
2. Lemma §4: verify the trace-norm convergence and the exchange with the trace (Birman–Solomyak CITED; geometry of u_n).
3. Overall sign: checked in the linear case U = T_c. The sign of C' is + for P̂ and − for 1−P̂; the ("−") corresponds to 1−P̂.
4. F_∞ ĥ(D) F_∞ = ĥ(−D): F_∞ commutes with dilations except for the inversion D ↦ −D (s ↔ 1−s); check against the unitary normalization ϑ(h) (a^{1/2}D_a).
5. C' does not use λ: if the audit finds a dependence on λ, there is an error.
6. §4 "what is NOT proved": the claim about Π_S is explicitly open; do not cite it as PROVED.
7. No equivalence with RH; the identities are local at 2 and do not fix the signs of the window form.

## For Paper 47

- Insertable as a lemma (PROVED): "semilocal scattering phase": F_S = F_∞ e^{iφ_S(D)}, φ_S' = −Σ_{p∈S}Σ_k v_{p^k}cos(kt log p); and the exact trace identity Tr ϑ(h)(P̂^S − P̂_∞) = Σ_{p∈S}Σ_k log p·p^{−k/2}(h(p^k)+h(p^{−k})), with the proof of §4 (only Birman–Solomyak as CITED). Natural location: alongside the discussion of the prime terms of the symbol θ (R183.018).
- Do not insert §5 (ARGUED) nor the interpretation of the corrections of R183.025/029 without the pending verification.
- Vocabulary: "prime comb", "scattering phase"; not "proof", not "criterion".

## Note (R186_094)

* C and C′ correct, exact, with no remainder, λ-independent (verified numerically). MAJOR-1: C′ proves the LINEAR part (1−P̂); (Δ) on Π_S remains CONDITIONAL on (M)/OPEN; correct the table. MAJOR-2: C is a one-line computation; C′ = Fourier dual of R183_015 + classical phase trace formula; withdraw "with no o(1), unlike Connes". MINOR: the multiplier of 007 §1 is (1−2^{−s})/(1−2^{−(1−s)}); cite Simon Trace Ideals Thm 4.5; hypothesis "h(e^y) Schwartz"; C″ for several primes still to be written. Paper 47: C and C′ admissible as lemmas with these corrections; do not insert §5.

## Note (R186_020)

* Thm C is the quasi-inner function u = ρ_∞ρ_2 of **CC arXiv:2008.10974** (Lemma 3.1); relabel CITED + verification. New relative to that source: non-HS, L2_S, (84)_S.
