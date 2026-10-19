# R166_102 — The exchange flow Z_s: coupling the canonical exchange (R163_001/114) with Det+ / Det−

Status: closed. **Verdict: no contradiction. The two bounds on T_c(s) have the same leading order, ½ log log(1/s), and they
cannot cross, because both are bounds on one quantity that exists (for M_m as well as for ζ). This is the W2/M wall again
(Theorem M smallness, read in s instead of T).**

## Status table

| Item | Statement | Label |
|---|---|---|
| 1 | Exact formula for W^{(s)}_T in terms of W_T plus the quartet difference | PROVED |
| 2 | Continuity in s of λ^{(s)}_T for fixed T; Lipschitz constant ≤ C·T²e^{2Tδ*} | PROVED |
| 3 | The sign of ∂_s 2Re F̂(t_s)² is **not** definite (correction to the brief) | PROVED |
| 4 | λ^{(0)}_T > 0 for every T > 0 | PROVED-CITED (Beurling–Landau sampling) |
| 5 | T_c(s) → ∞ as s → 0⁺ | PROVED |
| 6 | Det+ applied to Z_s: a*(s) → a finite nonzero limit, but B*(s) contains log(1/s), so τ(s) = ½log log(1/s) + O(1) → ∞ | PROVED (given Ξ(γ*) ≠ 0; otherwise replace k) |
| 7 | Lower bound T_c(s) ≥ ½log log(1/s) − O(log log log(1/s)) | ARGUED (needs an explicit lower frame bound λ^{(0)}_T ≥ exp(−C e^{2T}T)) |
| 8 | Crossing of the lower and upper bounds | IMPOSSIBLE (both bound the true T_c(s)); M_m passes |
| 9 | The atomicity of the prime side at s = δ* shows up in the window forms | NO: W_T depends only on the prime side on |u| ≤ 2T, and the correction λ_s is not seen by any T_c bound |

## 1. The exact form (PROVED)

Ξ_s := Ξ·(Q_s/Q_{δ*})^k with Q_s(z) = (z² − t_s²)(z² − t̄_s²), t_s = γ* − is. This function is entire, even, real on ℝ, and of
order 1. Its zeros are Z_s. By (1.1) applied to the zero set Z_s (a definition; it is also the explicit formula of ξ_s),
for real even F ∈ 𝒟_T

  W^{(s)}_T(F) = W_T(F) + 2k·[Re F̂(t_s)² − Re F̂(t*)²]·2,   (both members of each conjugate pair; ±t give the factor 2)

that is, W^{(s)} − W = 4k Re[F̂(γ*−is)² − F̂(γ*−iδ*)²]. Prime side: the difference of logarithmic derivatives has Fourier
image λ_s(u) − λ_{δ*}(u), with λ_s(u) = 4k cos(γ*u)·cosh(su)/… (the R163_001 §2 density). This is continuous in u, and it
vanishes identically only at s = δ*. Paired with c_F (supported on |u| ≤ 2T), it reproduces the line above.

## 2. Continuity and Lipschitz (PROVED)

For ‖F‖₂ = 1 and supp F ⊂ [−T,T]: |F̂(z)| ≤ √(2T)e^{T|Im z|} and |F̂′(z)| ≤ T√(2T)e^{T|Im z|}. Hence
|∂_s 4k Re F̂(t_s)²| ≤ 8k|F̂||F̂′| ≤ 16k T² e^{2Ts}, and |λ^{(s)}_T − λ^{(s′)}_T| ≤ 16kT²e^{2Tδ*}|s − s′|.

## 3. Sign of the s-derivative (PROVED: indefinite)

d/ds F̂(γ−is)² = −2i F̂F̂′, so d/ds 2Re F̂² = 4 Im(F̂F̂′) = 4 Im(F̂²·(F̂′/F̂)). The brief identified this with
|F̂|² Im(F̂′/F̂), but that equals Im(conj(F̂)·F̂′), which is a different quantity. When F̂ is real-rooted,
Im(F̂′/F̂)(γ−is) = Σ_x s/((γ−x)²+s²) > 0. Writing F̂′/F̂ = A + iB with B > 0 and arg F̂² = 2φ, we get
Im(F̂F̂′) = |F̂|²(A sin2φ + B cos2φ). The sign is set by the same phase 2φ that the cone condition of Lemma 3.1 places in
(π/2, 3π/2) at a witness. So at the witness cos2φ < 0, the term BCos2φ is negative, and A sin2φ has either sign. No
monotonicity in s follows. This is ω(E) again (R165_201 Cor 2.2).

## 4–5. T_c(s) → ∞ (PROVED)

For Z₀ every zero is real, so W^{(0)}_T(F) = Σ_γ F̂(γ)² (with multiplicity) for real even F. The ordinates of ζ have
density (1/2π)log γ → ∞. Choose a uniformly separated subset that has lower Beurling density > T/π (for large t, every
interval of length 1 contains an ordinate, classical). By Beurling–Landau this subset is a sampling set for PW_T, so
W^{(0)}_T ≥ c(T)‖F‖² with c(T) > 0. By §2, λ^{(s)}_T ≥ c(T) − 16kT²e^{2Tδ*}s > 0 for s < s₀(T). Since λ_T is nonincreasing
in T, T_c(s) ≥ T for s < s₀(T). Hence T_c(s) → ∞.

## 6. Det+ along the flow (PROVED). This resolves the apparent contradiction.

For Z_s the reduced coefficient is a*(s) = lim Ξ_s/Q_s^k at t_s, which equals Ξ(t_s)/Q_{δ*}(t_s)^k. It tends to
Ξ(γ*)/Q_{δ*}(γ*)^k, which is finite and nonzero when Ξ(γ*) ≠ 0. This part of the brief is correct. But Det+'s constant is

  B*(s) = log(1/|a*(s)|) + log(3350(1+γ*²)/(γ* s)),

and it contains log(1/s) explicitly. That factor comes from |R(t_s)| ≥ 2γ*s, the price of rotating the phase into the
cone. So X*(s) ≈ log(1/s) + πγ*/4 + O(log γ*), and

  τ(s) = ½ log(X*(s)/π) = ½ log log(1/s) + O(1)   (s → 0),   = T_L(γ*) + 0.226 + o(1) while log(1/s) ≪ γ*.

The brief's "O(log(1/s)/γ*)" is the linearization in Cor Det+.1. It is valid only while log(1/s) ≪ γ*. Beyond that, τ(s)
grows like ½ log log(1/s). The upper bound therefore does diverge, and there is no conflict with §5.

## 7. Lower bound rate (ARGUED)

The sampling constant c(T) is not explicit. Theorem M (PROVED-CITED record) gives the upper estimate
λ^{(0)}_T ≤ exp(−e^{(2−ε)T}). The plausible matching lower estimate c(T) ≥ exp(−C T e^{2T}) (a prolate/Turán-type lower
bound) would give s₀(T) ≈ exp(−CTe^{2T}), hence T_c(s) ≥ ½log log(1/s) − ½log log log(1/s) − O(1).

**Margin function.** μ(s) := τ(s) − T_c^{lower}(s) = ½ log log log(1/s) + O(1) > 0. Both bounds have the same leading
½ log log(1/s). The gap sits entirely in the subleading constants: the e^{2T} coefficient of the doubly exponential
smallness against the Riemann–Pólya decay exp(−πe^{2T}) in Det+. This is the W2/M wall in the s-variable. A truncated Φ
costs exp(−πe^{2T}), and the positive form at s = 0 degenerates at the same doubly exponential rate.

## 8. Falsifier (M_m) and logic (PROVED)

All of §§1–7 use only (1.1) on a zero set, the shape of the functional equation, and |ζ| ≤ ζ(2) on σ ≥ 2 (Det+). The last
input also holds for M_m, whose rational quartet factor is bounded there. For M_m the flow Z_s exists, T_c(s) is a genuine
finite number, and every bound above holds. A lower bound and an upper bound on the same real quantity cannot cross. So no
"crossing" is possible for ζ either, unless one bound uses something M_m lacks. None does. The only ζ-specific datum
(the λ_s correction vanishes at s = δ*, so the prime side is atomic there) never enters a T_c bound. Window forms see c_F on
|u| ≤ 2T, where the Λ-comb plus a continuous density is just another real measure. The tail quantity 𝒜(s) on u > 2T₀ is
invisible to λ_T for T ≤ T₀ by support.

## Ledger
- New PROVED: §1 exact flow form; §2 Lipschitz; §3 correction (∂_s sign indefinite, governed by ω(E)); §5 T_c(s) → ∞;
  §6 τ(s) ~ ½ log log(1/s), which corrects the brief's uniform-in-s claim.
- ARGUED: §7 lower rate and the margin μ(s) = ½ log log log(1/s) + O(1).
- Dead: "exchange-flow contradiction" (crossing). It is killed by M_m, and the cause is the δ in Det+'s |R(t*)| ≥ 2γ*δ*.

## Cells
- **7E (exchange flow):** CLOSED negative. The flow is well defined and continuous, and T_c(s) ∈ [½loglog(1/s) − o, ½loglog(1/s) + O(1)].
  No contradiction. Wall = W2/M.
- **7F (s-monotonicity of the quartet term):** CLOSED negative. ∂_s 2Re F̂² = 4|F̂|²(A sin2φ + B cos2φ) is indefinite, and it
  reduces to ω(E).
- **1F (atomic endpoint visible to windows):** CLOSED negative. λ_s affects W only through c_F on |u| ≤ 2T. Atomicity at
  s = δ* is not a window invariant. Any use of it must go through the f_t side of the dichotomy (R166_190 §0).
