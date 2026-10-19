# N_BUILD_005 — The window operator in the truncated causal algebra: exact Euler product, comb = −∂_s log Z_s, and the stability test

Pen and paper. Test requested: is the multiplicative structure (Λ = μ*log, ζ·ζ^{-1} = 1, −ζ′/ζ) destroyed by BOTH
modifications of N_BUILD_003 (tail deletion, uniform ε-rescaling)? Only such a structure can escape W-tail + prop:wit-sens.

## Corpus check
grep "Möbius|Mobius|μ * log|convolution|Euler product|Euler tower|causal algebra|unipotent|nilpotent" over 03-research,
04-papers, 05-meta, MAP_D, grid.
- R161_066 §2 / R161_099: "local Möbius inversion" (finite unitriangular inverse) leaves the transport block unchanged;
  returns to P121_CMO_SOURCE_MATRIX_NO_GO (log-differentiation). Operator-level, inside the first-contact transport.
- phase-146 R146_003 §D.47: single-prime Euler tower (pointwise local symbol bound).
- Paper 44 (row B): Möbius cofibre — row-B arithmetic family, not the window form.
- L2_BUILD_009 §1(iii): rewriting (¼−∂²)²dψ̃ creates no cancellation.
Differences here: (1) the exact finite algebra 𝔄_T in which Euler product, log and Möbius inversion are identities with no
tail; (2) the stability test of the multiplicative structure under the two modifications, which none of the above did.

## 1. The truncated causal algebra (PROVED)
𝔄_T := finite Borel measures on [0,∞) modulo those supported in [2T,∞), with convolution. It is a commutative unital
algebra (unit δ₀); the ideal is closed under convolution with measures on [0,∞). Pairing ⟨ν, c_F⟩ := ∫_{[0,2T)} Re c_F dν is
well defined on 𝔄_T for F ∈ L²(I_T) (c_F = 0 on [2T,∞)).
(i) Every ν supported in [log 2, 2T) is nilpotent: ν^{*k} = 0 in 𝔄_T for k > 2T/log 2.
(ii) Z_s := Σ_{n<N} n^{−s}δ_{log n} = δ₀ + (nilpotent) is invertible, Z_s^{−1} = Σ_{n<N} μ(n)n^{−s}δ_{log n}, and
 Z_s = Π_{p<N}(δ₀ − p^{−s}δ_{log p})^{−1} (finite product, each inverse a finite geometric series), N = e^{2T}.
(iii) log Z_s := Σ_{k≥1}(−1)^{k+1}(Z_s − δ₀)^{*k}/k (finite) equals Σ_{n<N} (Λ(n)/log n) n^{−s}δ_{log n}, and
 −∂_s log Z_s = Σ_{n<N} Λ(n)n^{−s}δ_{log n} = Z_s^{−1} * (−∂_s Z_s)   (Λ = μ*log, exact).
*Proof.* (i) supports add. (ii)–(iii): the map a ↦ Σ_{n<N} a(n)n^{−s}δ_{log n} is a ring homomorphism from arithmetic
functions (Dirichlet convolution) modulo {a : a(n) = 0 ∀n<N} onto its image in 𝔄_T, because log(nm) = log n + log m and
nm ≥ N ⇒ log nm ≥ 2T. The identities 1*μ = δ, ζ = Π(1−p^{−s})^{−1}, log ζ = ΣΛ/log·n^{−s}, Λ = μ*log hold as formal
Dirichlet series and hence in the quotient. ∎
**Window form (PROVED).** With s = ½: Σ_{n∈N_T} v_n Re c_F(log n) = 2⟨−∂_s log Z_s|_{s=½}, c_F⟩, so on P_T
 𝔞_T(F) = 𝔞_∞(F) − 2⟨−∂_s log Z_{½}, c_F⟩ — the window form sees ζ only through its truncated Euler algebra.
(Also: by §1 of N_BUILD_002, operator form ⟨U_μF, U_log F⟩_{L²(ℝ)} with finite shift sums U_μ = Σμ(d)d^{−½}τ_{−log d},
U_log = Σ log m·m^{−½}τ_{log m}; the constraint dm < N is automatic since the supports separate.)

## 2. Stability test — the Euler-product structure is NOT destroyed (NO-GO, PROVED)
(a) Partial Euler products. For a finite prime set S, Z^S := Π_{p∈S}(δ₀ − p^{−s}δ_{log p})^{−1} is a genuine Euler
product in 𝔄_T; its comb is a_S := Λ·1_{n is an S-power}. WP_T(a_S) fails for all large T: proof of N_BUILD_003 Thm 1
verbatim (dominated convergence: Σ_{p∈S,k} v_{p^k} < ∞), limit value C₀ − Σ_{p∈S,k≥1} v_{p^k} < 0.
(b) Powers. Z_s^{α} := exp(α log Z_s) (exact in 𝔄_T) has comb αΛ; α = 1 ± ε fails when ε > λ_A/|κ_T| (prop:wit-sens;
CONDITIONAL on κ_T ≠ 0).
Hence any argument that uses only "the comb is −∂_s log of an Euler product in 𝔄_T" (or of a real power of one)
decides no window for large T. Euler product + Möbius inversion + log-derivative are all preserved by the two
modifications in this generalized sense: they do not pass the test.

## 3. What the two modifications do destroy (PROVED)
Both destroy exactly the coefficient identity (C): Z_{s} = Σ_{n<N} 1·n^{−s}δ_{log n}, i.e. 1*a = log on [1, N).
(Deletion: 1*a(n) = log of the S-part of n; rescaling: 1*a = (1+ε)log.) And (C) determines a = Λ on [1,N) uniquely
(Möbius inversion in the quotient). So "use (C)" = "use the exact vector (Λ(n))_{n<N}": the stability test is passed
only by the full integer comb Z_s itself, i.e. by the ADDITIVE structure of ℕ in log scale (all coefficients 1), not by
multiplicativity. Combined with rem:twohalves (Epstein: coefficients r_Q(n), functional equation, no Euler product) the
needed input must use both: coefficients exactly 1 (additive) and the Euler product (multiplicative) — jointly.

## 4. The surviving object (OPEN; next construction)
In 𝔄_T split the integer comb additively by Euler–Maclaurin (exact, first order):
 Z_s = M_s + B_s,  M_s := e^{(1−s)u}du on (0,2T) + ½δ₀ (+ boundary at 2T, zero in 𝔄_T),
 B_s := the measure ∫ f dB_s = −∫₁^N ({x}−½) d/dx[f(log x)x^{−s}] dx (sawtooth; Fourier series Σ_k sin(2πkx)/(πk)).
Then −∂_s log Z_s = −∂_s log M_s − ∂_s log(δ₀ + M_s^{−1}*B_s). The first term is the pole/main term (it carries the
e^{u/2} density that P_T converts into +4, N_BUILD_001); the second contains all primes. Question (Ω_EM): is
⟨−∂_s log(δ₀ + M_{½}^{−1}*B_{½}), c_F⟩ controllable with sign on P_T? Here B is a bounded-oscillation (Bernoulli)
object: this is where "coefficients exactly 1" enters, and both modifications break it (they are not of the form M + B
with B a sawtooth). Note M_s^{−1} exists in 𝔄_T only after removing the δ₀-unit: M = ½δ₀ + (absolutely continuous),
invertible since ½ ≠ 0 (exact Volterra resolvent).

## Barrier position
§1 exact (inherits the margin). §2 is a NO-GO for the class "Euler-product structure" — new, extends W-tail to
multiplicative modifications. §4 escapes W-tail and prop:wit-sens by construction (it is not preserved by them); it is not
in W-loc/W-mom; its relation to W-coh: the Bernoulli remainder is not a Lipschitz functional of the coherence. Epstein
(rem:twohalves) is escaped only if the Euler product is used jointly — §4 keeps it inside log.

## Self-review
1. §1(ii): homomorphism needs nm ≥ N ⇒ term vanishes — yes since δ_{log nm} with log nm ≥ 2T is in the ideal. log Z is
a finite series by (i). Correct.
2. §2(a): a_S includes p^k with p^k ≥ N, but those have log ≥ 2T and vanish in the window — fine. The W-tail proof needs
only finitely many n per T — here the number grows with T but the dominated sum converges. Correct.
3. §3 "uniquely": Möbius inversion in the quotient ring — correct. The conclusion "needed input must use both" is a
reading of rem:twohalves + §2–3, ARGUED, not a theorem.
4. §4: the Euler–Maclaurin decomposition is exact; M_s^{−1}*B_s is not small in total variation (B has mass ~ Σ n^{−½}
in variation), so log(δ₀ + M^{−1}B) is defined only through nilpotency of the part supported in [log2,2T) — need to check
that M^{−1}*B has no δ₀-component: B has none (sawtooth integral is absolutely continuous plus jumps at integers n ≥ 2,
and at x=1 a boundary term absorbed into M's ½δ₀). So log is a finite series. OK. (Ω_EM) is OPEN.
No sign contact; no negative value.
