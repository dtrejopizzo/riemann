# Round 012 A — The packet bound (1.2) above the plunge: certified small-T range, the all-profile operator form, and three NO-GOs for a uniform proof

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Notation of ROUND_011_A/C: λ = e^T, N = λ², v_n = 2Λ(n)/√n,
m(τ) = Re ψ(¼ + iτ/2) − log π, P^ρ_T(τ) = Σ_{n<N} v_nρ(log n/T)cos(τ log n), ρ = ρ_β the normalised autocorrelation of a
real profile β ∈ L²[−1, 1], Σ^ρ_T = P^ρ_T(0), Ω_lo = 2πN(1 + δ), δ = 0.1. The statement under study is
(1.2)_κ: P^ρ_T(τ) ≤ m(τ) − κ for all τ ≥ Ω_lo.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check

Searched ROUTES-TRIED-INDEX rows P211-6C (Theorem B, large values of P_T), P211-10A, P211-11A, P211-11C, the closed
mean-square / large-sieve / Montgomery–Vaughan families, ledger C24–C27. Differences: §2 is a finite certified
computation extending the automatic range of 11C Lemma 1.1 (not an indexed route); §3 is a definitional reformulation
(not a method); §4 records why the three routes proposed for a uniform proof (mean value + Sobolev/Gallagher; trivial bound
with a decaying profile; T-dependent short packets) close, the first being an instance of the closed mean-square family,
quantified here only to record the loss. No zero information is used anywhere. Not a sign step.

## 1. Two elementary facts on profiles (PROVED)

**Lemma 1.1.** For every real β ∈ L²[−1, 1], β ≠ 0: (i) |ρ_β(u)| ≤ 1; (ii) |ρ_β(u)| ≤ ½ for |u| ≥ 1; (iii) ρ_β(u) = 0 for |u| ≥ 2.
*Proof.* a(u) = ∫β(x)β(x + u)dx. (i) Cauchy–Schwarz. (ii) For u ≥ 1 the integrand lives on A = [−1, 1 − u], and
x + u ∈ B = [u − 1, 1]; A ∩ B has measure ≤ 0 (2 − 2u ≤ 0), so |a(u)| ≤ ‖β1_A‖‖β1_B‖ ≤ ½(‖β1_A‖² + ‖β1_B‖²) ≤ ½‖β‖². (iii) support. ∎

**Lemma 1.2 (cos² profile).** For β = cos²(πx/2) on [−1, 1],
ρ(u) = [π(−u cos πu − 2u + 2cos πu + 4) + 3 sin πu]/(6π) on [0, 2], and ρ is nonincreasing on [0, 2].
*Proof.* Direct integration of ∫_{−1}^{1−u}β(x)β(x + u)dx = ½ − u/4 + cos πu/4 − u cos πu/8 + 3 sin πu/(8π), divided by
a(0) = ¾. 6ρ′(u) = π(u − 2)sin πu + 2(cos πu − 1). On [0, 1] both terms are ≤ 0. On [1, 2], with w = 2 − u ∈ [0, 1] and
t = πw/2 ∈ [0, π/2]: 6ρ′ = πw sin πw − 4sin²t = 4 sin t (t cos t − sin t) ≤ 0 since t ≤ tan t. ∎

Consequence: for cos², T ↦ Σ^ρ_T is nondecreasing (each term ρ(log n/T) is nondecreasing in T, and terms entering at
log n = 2T enter with value ρ(2) = 0), and T ↦ m(Ω_lo(T)) is nondecreasing (m increasing, 11C Lemma 1.1(i)).

## 2. Certified range (PROVED, computer-assisted where stated)

**Theorem 2.1 (all profiles, T ≤ log 2).** For every T ∈ (0, log 2], every real profile β on [−1, 1] and every τ ≥ Ω_lo,
P^ρ_T(τ) ≤ m(τ) − 0.069.
*Proof.* By 11C Lemma 1.1(i) it suffices that S(T) := sup_β Σ^{|ρ|}_T ≤ m(Ω_lo(T)) − 0.069, and m(Ω_lo(T)) is increasing in T.
For T ≤ ½log 2 the sum is empty and m(Ω_lo) ≥ m(2π·1.1) = 0.0944. For T ∈ (½log 2, ½log 3]: only n = 2, log 2/T ≥ 1, so
S ≤ ½v_2 = 0.4901 < m(Ω_lo(½log 2)) = 0.7871. For T ∈ (½log 3, log 2]: n ∈ {2, 3}, log n/T ≥ 1, S ≤ ½(v_2 + v_3) = 1.1243
< m(Ω_lo(½log 3)) = 1.1931 (slack 0.0688); n = 4 enters only for T > log 2. (Lemma 1.1(ii); m values by the digamma
function at 30 digits.) ∎
Beyond log 2 the all-profile trivial bound fails (at T = 0.7: v_2 + ½v_3 + ½v_4 = 1.96 > m(Ω_lo) = 1.50); see §3.

**Theorem 2.2 (cos² profile, T ≤ 2.64).** For β = cos²(πx/2), (1.2)_κ holds on the whole high range [Ω_lo, ∞) for every
T ∈ (0, 2.64], with κ = 0.0486 (and κ ≥ 0.137 on T ≤ 2.6, κ ≥ 0.33 on T ∈ [0.3, 2.5], κ ≥ 0.094 on T ≤ 0.3).
*Proof.* By 11C Lemma 1.1 and the monotonicity in §1, it suffices to check on a grid T_0 < T_1 < … that
Σ^ρ_{T_{j+1}} + κ ≤ m(Ω_lo(T_j)). tools/cos2_trivial_cert.py does this with Σ^ρ enclosed in 50-digit interval arithmetic
(mpmath.iv; every term log p, √n, sin, cos enclosed) and m by the 50-digit digamma function; grid step 0.01 on [0, 2.5],
0.002 on [2.5, 2.6], 0.001 on [2.6, 2.64]. Minimum slacks: 0.0944 / 0.3316 / 0.1367 / 0.0486. ∎
The trivial bound for cos² fails at T = 2.662 (slack −0.004): beyond that the range [Ω_lo, τ*_0] of 11C is nonempty.
(The bump profile has no closed-form ρ; Table 1.1 of 11C gives its trivial range as T ≤ 2.0, not certified here.)

## 3. What (HR)(a) actually needs: the all-profile operator form (PROVED)

By 11A Proposition 1.2, coercive (HR)(a) on the high block implies (1.2) for **every** profile β, not for one chosen
profile. A fixed easy profile (cos²) therefore verifies a necessary instance only. The all-profile family is one operator
statement:

**Proposition 3.1.** For τ ∈ ℝ let A_τ be the bounded self-adjoint operator on L²[−T, T],
(A_τ f)(x) = ½Σ_{n<N} v_n cos(τ log n)[f(x + log n) + f(x − log n)]·1_{[−T,T]}(x) (f extended by 0).
Then sup_β P^{ρ_β}_T(τ) = λ_max(A_τ), the supremum over real β ∈ L²[−1, 1]∖{0}. Hence (1.2)_κ for all profiles at all
τ ≥ Ω_lo ⟺ λ_max(A_τ) ≤ m(τ) − κ for all τ ≥ Ω_lo.
*Proof.* With f(x) = β(x/T): ⟨f, A_τ f⟩ = Σ_n v_n cos(τ log n)∫f(x)f(x + log n)dx = ‖f‖²Σ_n v_n cos(τ log n)ρ_β(log n/T).
Taking the supremum of the Rayleigh quotient over real f (A_τ is real symmetric) gives λ_max. ∎
Reading. A_τ is the comb part of W_T on a single frequency cell: it is a finite Toeplitz-type (shift) operator of the
comb tail with Dirichlet phases cos(τ log n). The (HR)(a) statement is "the archimedean symbol at τ dominates the top of
the comb operator twisted by τ", uniformly in τ ≥ Ω_lo. By 11C Lemma 1.1 (λ_max(A_τ) ≤ ‖A_τ‖ ≤ Σ_n v_n) only
log τ < Σ_{n<N}v_n + κ + log 2π is open.

## 4. Why a uniform-in-T proof of (1.2) is not reached by the proposed routes

**4.1 Trivial bound with a fixed profile — NO-GO (class: P ≤ Σ^ρ_T).** For every fixed β there is T_β < ∞ beyond which
Σ^ρ_T > m(Ω_lo). *Proof.* Pick u₀ ∈ (0, 2) with ρ(u₀) =: r > 0 and ρ ≥ r/2 on [0, u₀] (continuity, ρ(0) = 1; if ρ changes
sign on [0, u₀] shrink u₀). Then Σ^ρ_T ≥ (r/2)Σ_{n ≤ e^{u₀T}} v_n ≥ (r/2)·2ψ(x)/√x with x = e^{u₀T}, and Chebyshev's bound
ψ(x) ≥ x/2 for x ≥ x₀ (CITED) gives Σ^ρ_T ≥ (r/2)e^{u₀T/2}, while m(Ω_lo) = 2T + log(1 + δ) + O(N⁻²). ∎
Making ρ vanish to order k at u = 2 changes only u₀; the exponential growth stays.

**4.2 T-dependent short packets — NO-GO (class: packet families of length L = o(T)).** Narrowing the packet to
β(x/L), L ≪ T, makes Σ ≈ 4e^{L} ≤ 2T possible (L ≤ log T + O(1)), but cannot discharge (HR)(a): Proposition 1.2 of 11A is
a necessity statement for length-T packets, so every proof of coercivity on the high block must in particular give (1.2)
for all length-T profiles (Proposition 3.1). A sufficiency argument built from short packets f = Σ_j g_j must control the
cross terms Σ_n v_n⟨g_j, g_k(· + log n)⟩ with log n ≈ |x_j − x_k| up to 2T; for a train of equal short packets these cross
terms reassemble exactly P^{ρ'}_T with ρ' the autocorrelation of the train envelope (a length-T profile). Bounding them
by absolute values returns Σ^{ρ'}_T, i.e. 4.1. (PROVED as a logical statement from 11A Prop 1.2 + Prop 3.1.)

**4.3 Mean value + Sobolev/Gallagher — NO-GO (closed mean-square family; recorded with the loss).** Montgomery–Vaughan
(CITED) on [Ω_lo, CΩ_lo] gives the mean square ½Σ v_n²ρ² ≈ 2T²a_ρ, a_ρ = ∫₀²sρ(s)²ds (a = ⅓ for the triangle);
numerically RMS = 0.72T–0.74T (ind), 0.48T–0.50T (cos²) at T = 3–4.5. Gallagher/Sobolev over K ≍ (C − 1)NT cells of width
1/T converts this into sup ≲ √K·RMS ≍ T^{3/2}e^T, against the needed 2T + log(1 + δ) − κ: loss e^{T}√T. Any method losing
a multiplicative constant is excluded anyway by §5: the bound must be accurate additively to O(1) on a quantity ≍ 2T.

**4.4 Extreme-value heuristic — ARGUED, and contradicted by the data.** Independent-Gaussian modelling of the cells predicts
sup P ≈ RMS·√(2 log K) ≈ 2√(2a_ρ)T^{3/2}, which would exceed 2T for T > 1/(2a_ρ) (≈ 1.5, ind). It is wrong at T ≤ 4.5:
Table 4.1 (NUMERICAL, tools/packet_margin.py functions, grid 1/(12T) + Brent refinement, range [1.1, 3]·2πN only):

| T | profile | Σ^ρ_T | RMS | sup P (at τ/2πN) | m there | min (m − P) |
|---|---|---|---|---|---|---|
| 3.0 | ind / cos² / bump | 17.8 / 7.02 / 8.76 | 2.17 / 1.44 / 1.63 | 5.78 (1.16) / 4.91 (1.11) / 5.56 (1.11) | 6.14 / 6.11 / 6.11 | 0.361 / 1.194 / 0.544 |
| 3.5 | ind / cos² / bump | 27.3 / 9.94 / 12.5 | 2.56 / 1.70 / 1.92 | 6.76 (1.12) / 6.02 (1.26) / 7.10 (2.08) | 7.11 / 7.23 / 7.73 | 0.350 / 1.211 / 0.634 |
| 4.0 | ind / cos² / bump | 41.3 / 13.7 / 17.5 | 2.95 / 1.97 / 2.22 | 7.83 (1.21) / 7.52 (1.64) / 8.07 (1.64) | 8.19 / 8.50 / 8.50 | 0.359 / 0.980 / 0.430 |
| 4.5 | ind / cos² / bump | 61.9 / 18.6 / 24.1 | 3.35 / 2.23 / 2.51 | 8.93 (1.33) / 9.21 (2.56) / 9.73 (2.56) | 9.29 / 9.94 / 9.94 | 0.355 / 0.730 / 0.208 |

(The values are minima of m − P^ρ_T over [1.1, 3]·2πN; the margin "min" is the true infimum over the high range only where
11C closed the rest, i.e. T = 3 cos²/bump. Above 3·2πN the range up to τ*_0 is not scanned at T ≥ 3.5.)
Observations. (a) The peak/RMS ratio is ≈ 2.7 at T = 4.5 against the Gaussian ≈ 4.9; the peaks do not grow like T^{3/2}.
(b) For the mollified indicator the margin is flat, 0.361, 0.350, 0.359, 0.355 at T = 3–4.5 (with 0.341 at T = 2): the
peaks track m(τ) − 0.35, i.e. sup P ≈ log(τ/2π) − 0.35 on the first cells — a locking of the peak to the logarithm, not a
random extreme. (c) Smooth profiles have larger but decreasing margins (cos² 1.19 → 0.73; bump 0.54, 0.63, 0.43, 0.21 at T = 3–4.5, now below the ind margin), with the
minimiser moving up to 1.6–2.6·2πN.

## 5. Falsifier note (size statement)

Theorems 2.1–2.2 are not sign steps; they use only v_n ≥ 0, |ρ| ≤ 1 (resp. ≤ ½ beyond 1) and the size of finitely many
v_n, and survive (b), (d) and small c in (a), failing for c > 1 + slack/Σ (e.g. c > 1.07 at T = 2.5 for cos²). The open
statement (1.2) uniform in T is a size statement and must fail for cΛ: with the observed flat ind margin 0.355 and peak
8.93 at T = 4.5, m − cP vanishes at c ≈ 1.040 (budget ≈ 0.35/(2T), shrinking; cf. 1.09 at T = 2). Hence any proof must
bound P^ρ_T on the first cells above the plunge with additive error O(1) on a quantity ≍ 2T: no constant-losing estimate
(MV constant, large sieve, Sobolev, Hölder over moments) can be part of it. A Beurling system (c) with the same block masses
reproduces Σ^ρ, RMS and the trivial range, so §2 cannot distinguish it; the locking in 4.4(b), if real, is where an ℕ-specific
argument would have to enter.

## Result

PROVED piece + NO-GO with class.
PROVED: (1.2) holds on the entire high range [2πN(1.1), ∞) (i) for all profiles when T ≤ log 2 (κ = 0.069, Theorem 2.1);
(ii) for the cos² profile when T ≤ 2.64 (κ = 0.0486; computer-assisted, interval arithmetic, Theorem 2.2). The all-profile
form that (HR)(a) needs is λ_max(A_τ) ≤ m(τ) − κ for a single explicit cell operator A_τ (Proposition 3.1).
NO-GO: (4.1) trivial-bound class for any fixed profile (exponential growth of Σ^ρ_T); (4.2) T-dependent short packets
(necessity is for length-T packets of every profile; short-packet cross terms reassemble long profiles); (4.3) mean value +
Sobolev/Gallagher (loss e^T√T; closed family).
OPEN: the uniform statement below.

### What was proved
- Lemma 1.1 (|ρ| ≤ ½ beyond 1), Lemma 1.2 (cos² autocorrelation explicit and nonincreasing).
- Theorem 2.1 (all profiles, T ≤ log 2), Theorem 2.2 (cos², T ≤ 2.64), tools/cos2_trivial_cert.py.
- Proposition 3.1 (all-profile (1.2) ⟺ λ_max(A_τ) ≤ m(τ) − κ).

### What failed and why
- No uniform-in-T proof: the trivial bound fails for every fixed profile at finite T (4.1); shrinking packets is not
  allowed by the necessity direction (4.2); mean-square-to-sup loses e^T√T (4.3); and by §5 any constant-losing method fails.
- The remaining asymptotic statement, precisely: (U) there exist κ > 0 such that for all T > log 2 and all τ with
  2πN(1 + δ) ≤ τ ≤ 2π·exp(Σ_{n<N}v_n + κ), λ_max(A_τ) ≤ m(τ) − κ; for the cos² instance, for T > 2.64 and the same τ-range
  with Σ^ρ_T in place of Σ v_n.
- NUMERICAL (not proof): no violation at T ≤ 4.5 on [1.1, 3]·2πN; ind margin flat at ≈ 0.35; Gaussian extreme heuristic refuted.

### Next concrete step
Explain the locking sup P^ind_T ≈ log(τ/2π) − 0.35 on the first cells (4.4(b)) by an ℕ-specific identity at τ ≈ 2πN·(1–2):
P^ρ_T(τ) as the smoothed Σ_{n<N}Λ(n)n^{−1/2−iτ} at height comparable to the length, where the Poisson/van der Corput B-process
(dual length τ/(2πn) ≈ N/n) is available for the integer sum Σ n^{−1/2−iτ} and Vaughan's identity transports it to Λ
without zero information; test whether the dual sum reproduces −m(τ) + O(1). In parallel compute λ_max(A_τ) (Proposition 3.1)
on [1.1, 3]·2πN for T ≤ 3 to see whether the all-profile margin stays positive.
