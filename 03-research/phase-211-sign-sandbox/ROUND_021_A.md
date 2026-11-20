# Round 21 A — The positivity window J_R(T) of the complete R-cell form

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_016_B, ROUND_018_A, ROUND_019_A (𝔇_R, Q_R, V_R, ℓ_g, Π, v_n).
λ = e^T. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Index rows read: P211-18A (R-cell form against ℓ_g, collapse for R ≥ 5), P211-19A (band family; three-cell threshold
c₂* ≈ 1.016 / 1.008; two-sided failure of falsifier (a) at R = 4, ARGUED 𝔇-comb/Π cancellation; §5.1: fixed-R statements
are invariant under modifications beyond the R-th cell). What differs here: no new constraint family is introduced; the
object is the *set of weights* for which the already-defined R-cell form is nonnegative, J_R(T) = {c : Q_R^{(c)} ≥ 0 on V_R},
and its behaviour in R. Neither 18A nor 19A computed a window as a function of R, nor split Π by atom. Two indexed results
are close and are used, not retried: P211-17A recorded, for the full form on P_T, that c > 1 dies at first order at
λ_A/Π_T(F) and c < 1 at the size of the next rung; P211-18B Lemma 1.1 used Λ∗1 = log to collapse the comb to c·log N on
tails. Here the same two mechanisms are located on the idealised R-cell form, with the identity written in the truncated
Dirichlet algebra of the window (an exact "iff" on n < R), and the question is whether the R-dependence adds anything.

## 1. Set-up
### 1.1 Split form (PROVED bookkeeping)
For weights w = (w_n)_{n<R, n prime power} put Π_w = Σ_n w_n Π_n, Π_n[H] = v_n c^sym_H(log n), v_n = 2Λ(n)n^{−1/2}, and
    Q_R^{(w)}[F] = 𝒜[𝔇_R F] − Π_w[𝔇_R F] + 2A(𝔇_R F)B(𝔇_R F),    𝔇_R = Σ_{N<R} N^{−1/2}τ_{log N}
(18A §2.1; Π_w with w ≡ 1 is Π). Q_R^{(w)} is affine in w. J_R := {c ∈ ℝ : Q_R^{(c·1)} ≥ 0 on V_R}; per-prime windows
J_R^{(p)} := {x : Q_R^{(w)} ≥ 0, w_n = x for n = p^k, w_n = 1 otherwise}; atom windows J_R^{[m]} (only w_m varies).

### Lemma 1.1 (PROVED). Each window is a closed interval (possibly empty or a point).
*Proof.* c ↦ inf_{F∈V_R, ‖F‖=1} Q_R^{(c)}[F] is an infimum of affine functions of c, hence concave and upper semicontinuous;
its superlevel set {≥ 0} is a closed convex subset of ℝ. Same for every one-parameter affine family. ∎
So J_R is determined by its endpoints c_−(R) ≤ c_+(R), and bisection on the sign of the bottom eigenvalue is legitimate.

### 1.2 Tool (NUMERICAL)
tools/multi_cell/window_build.py R Nb T J dps builds Q₀ = 𝔇ᵀ𝒜𝔇 + abᵀ + baᵀ and Q_n = 𝔇ᵀΠ_n𝔇 per atom (exact closed form for
Π_n; Σ_nΠ_n agrees with the Λ-comb matrix of galerkin_mp to 10^{−dps}), the four transported constraints and ℓ_g^{fam}
exactly as cellRg_mp.py (Nb sine modes, J gauge functions, mpmath 50–110 digits). tools/multi_cell/window_scan.py prints
bottom values of Q/‖F‖² and Q/ℓ_g on V_R along a family and bisects the endpoints by a Cholesky (inertia) test.
Check: R = 3, T = 0.8, c = 1, 1.1 reproduce 19A (Q/ℓ_g = 0.737, −5.78).

## 2. Measurements

All runs Nb = 40 sine modes unless stated; J (gauge rank) 20–40; 50 digits (R ≤ 3), 70 (R = 4, 5), 90 (R = 6, 7),
110 (R = 8). δ_± := |c_± − 1|. Entries below 10⁻¹¹ come from 90-step bisection between 1 ± 10⁻⁷ and agree with the
first-order value λ₀/K₀ of §3 to two digits.

### 2.1 Resolution direction (PROVED)
Nested sine bases give nested trial spaces V_R^{Nb} ⊂ V_R^{Nb′} ⊂ V_R (the four constraints are exact functionals
restricted to the span). Hence, up to quadrature and rounding, Q_R^{(w)} ≥ 0 on V_R ⇒ ≥ 0 on V_R^{Nb}: **every Galerkin
window is an outer bound for the true window**, J_R^{true} ⊆ J_R^{Nb′} ⊆ J_R^{Nb}. Shrinking of the computed window
therefore transfers to the true window; positivity at c = 1 does not.

### 2.2 Uniform scaling c·Λ (NUMERICAL)
| R | atoms n < R | T = 0.8: c_− − 1 | c_+ − 1 | T = 1.0: c_− − 1 | c_+ − 1 | bottom λ₀ of Q_R^{(1)} on V_R (‖F‖² units), T = 0.8 / 1.0 |
|---|---|---|---|---|---|---|
| 2 | none | J₂ = ℝ | | J₂ = ℝ | | 0.547 / 0.567 (c-independent) |
| 3 | 2 | −2.07 | +1.70·10⁻² | −2.07 | +8.76·10⁻³ | 1.49·10⁻³ / 7.8·10⁻⁴ |
| 4 | 2, 3 | −5.2·10⁻³ | +5.04·10⁻⁵ | −7.2·10⁻⁴ | +4.93·10⁻⁵ | 6.5·10⁻⁶ / 2.1·10⁻⁶ |
| 5 | 2, 3, 4 | −3.7·10⁻⁵ | +6.7·10⁻⁸ | −6.3·10⁻⁶ | +1.5·10⁻⁷ | 5.8·10⁻⁹ / 1.8·10⁻⁸ |
| 6 | 2–5 | −6.5·10⁻⁸ | +1.3·10⁻¹¹ | −4.8·10⁻⁸ | +1.3·10⁻¹¹ | 2.0·10⁻¹² / 2.0·10⁻¹² |
| 7 | 2–5 | −8.8·10⁻¹¹ | +7.4·10⁻¹⁶ | −7.6·10⁻¹¹ | +7.4·10⁻¹⁶ | 9.8·10⁻¹⁷ / 9.4·10⁻¹⁷ |
| 8 | 2–5, 7 | −3.9·10⁻¹⁴ | +6.9·10⁻¹⁹ | −3.5·10⁻¹⁴ | +6.8·10⁻¹⁹ | 7.7·10⁻²⁰ / 7.5·10⁻²⁰ |

Resolution checks (outer bounds shrink, as 2.1 predicts): R = 3, Nb 48: c_+ − 1 = 1.69·10⁻² (T = 0.8); R = 4, Nb 48:
(−4.7·10⁻³, +5.02·10⁻⁵) / (−6.9·10⁻⁴, +4.93·10⁻⁵); R = 5, Nb 56: (−3.5·10⁻⁵, +3.3·10⁻⁸) / (−4.1·10⁻⁶, +1.0·10⁻⁷);
R = 6, Nb 56 (T = 0.8, 100 digits): (−2.8·10⁻⁸, +1.07·10⁻¹¹). Earlier mp runs (tools/multi_cell/mp.txt): λ₀(R = 7) = 9.8·10⁻¹⁷
(Nb 40) → 6.1·10⁻¹⁷ (Nb 48). The double-precision negatives of runs.txt (R = 6, 8) are rounding.

Answer to (1): **yes, J_R shrinks to {1}, two-sided, from R = 4 on**, and very fast: ln δ_+ drops by 5.4, 7.0, 8.0, 9.9,
7.2 per added cell (T = 0.8; the last step is resolution-limited at Nb 40, which can only overstate δ). Fits of ln λ₀
(≈ ln δ_+ + O(1)) on R = 3…8: linear in R rms 1.1–1.5; in R log R slope −2.9 rms 0.7–1.1; in R² rms 1.1; in log R rms 2.9–3.2.
The decay is faster than exponential in R; R log R fits best but the exponent is not resolved by six points. T enters
only weakly for R ≥ 6 (λ₀ agrees to 5 % at T = 0.8 and 1.0). The window is strongly asymmetric: δ_− / δ_+ ≈ 10²…10⁵,
growing with R.

### 2.3 Per-prime and per-atom perturbations (NUMERICAL, T = 0.8 / 1.0, Nb 40)
| R | only n = 2 scaled (= Λ + η·1_{n=2}, η = (x − 1) log 2) | all powers of 2 scaled | all powers of 3 scaled |
|---|---|---|---|
| 4 | (−3.1·10⁻³, +4.2·10⁻⁵) / (−3.5·10⁻⁴, +4.2·10⁻⁵) | same (4 ∉ [1,4)) | (−2.5·10⁻⁴, +7.2·10⁻³) / (−2.5·10⁻⁴, +3.4·10⁻⁴) |
| 5 | (−2.4·10⁻⁵, +5.4·10⁻⁸) / (−4.3·10⁻⁶, +1.3·10⁻⁷) | (−2.3·10⁻⁵, +5.4·10⁻⁸) / (−4.3·10⁻⁶, +1.3·10⁻⁷) | (−2.7·10⁻⁷, +5.3·10⁻⁵) / (−7.9·10⁻⁷, +1.3·10⁻⁵) |
| 6 | (−3.9·10⁻⁸, ≈1·10⁻¹¹) / (−3.2·10⁻⁸, ≈1·10⁻¹¹) | (−3.7·10⁻⁸, ≈1·10⁻¹¹) / (−3.1·10⁻⁸, ≈1·10⁻¹¹) | (−5.4·10⁻¹¹, +4.4·10⁻⁸) / (−5.2·10⁻¹¹, +4.9·10⁻⁸) |
| 7 | (−4.2·10⁻¹¹, ≲10⁻¹⁵) | (−3.9·10⁻¹¹, +5.8·10⁻¹⁶) / (−3.5·10⁻¹¹, +5.8·10⁻¹⁶) | (−2.7·10⁻¹⁵, +5.0·10⁻¹¹) / (−2.7·10⁻¹⁵, +4.8·10⁻¹¹) |
| 8 | — | (−2.1·10⁻¹⁴, +5.3·10⁻¹⁹) / (−2.0·10⁻¹⁴, +5.3·10⁻¹⁹) | (−2.3·10⁻¹⁸, +3.7·10⁻¹⁴) / (−2.3·10⁻¹⁸, +3.6·10⁻¹⁴) |
Every per-prime window shrinks to {1} at the same rate as the uniform one; the tight side flips between p = 2 and p = 3
(the bottom vector has slope ⟨Π_2∘𝔇⟩ > 0 and ⟨Π_3∘𝔇⟩ < 0, §3). In particular Λ + η·1_{n=2} is excluded for
|η| ≳ 4·10⁻¹⁹·log 2 at R = 8.

Deletions a_P (bottom of Q_R on V_R, ‖F‖² units / ℓ_g units, T = 0.8; T = 1.0 within 1 %):
| R | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|
| a_3 (delete powers of 2) | −0.19 / −4.3·10² | −0.29 / −7.6·10⁴ | −0.36 / −9.4·10⁶ | −0.41 / −3.7·10¹⁰ | −0.47 / −1.4·10¹² |
| a_5 (delete powers of 2, 3) | −0.10 / −2.6·10² | −0.13 / −4.5·10⁴ | −0.16 / −5.2·10⁶ | −0.17 / −1.6·10¹⁰ | −0.23 / −3.8·10¹¹ |
(At R = 3, a_3 = c₂ = 0 is inside J₃ = (−1.07, 1.017): 19A's certificate.) From R = 4 on, a_P fails by O(1) in ‖F‖².

## 3. Structure

### 3.1 The truncated Dirichlet algebra of the window (PROVED)
Let I = (−h, h), ℓ = 2h = log R, and for a ≥ 0 let τ_a^I F(x) = 1_I(x)F(x − a) on L²(I) (F extended by 0). For a, b ≥ 0,
τ_a^I τ_b^I = τ_{a+b}^I: the left side is 1_I(x)1_I(x − a)F(x − a − b), and x ∈ I, x − a − b ∈ I imply x − a ∈ I (I is an
interval, 0 ≤ a ≤ a + b). Also τ_a^I = 0 for a ≥ ℓ. Hence
    Φ_R : (α_n)_{n≥1} ↦ Σ_{n<R} α_n n^{−1/2} τ_{log n}^I
is a homomorphism from arithmetic functions under Dirichlet convolution to operators on L²(I), Φ_R(α∗β) = Φ_R(α)Φ_R(β),
with kernel exactly {α : α_n = 0 for n < R} (the operators τ_{log n}^I, n < R, are linearly independent: apply them to a
bump at the left end of I). 𝔇_R = Φ_R(1). Moreover, with M_x multiplication by x on I, [M_x, τ_a^I] = a τ_a^I, so
    [M_x, Φ_R(α)] = Φ_R(α·log).                                                                              (3.1)

### Proposition 3.2 (the multiplicative identity at R-cell level; PROVED)
For weights w on the prime powers n < R, put P_w := Φ_R(wΛ) = Σ_{n<R} w_nΛ(n)n^{−1/2}τ_{log n}^I. Then
    P_w 𝔇_R = [M_x, 𝔇_R]   ⟺   w_n = 1 for every prime power n < R,
and P_{c·1}𝔇_R = c[M_x, 𝔇_R] for every c. Consequently, with real F and Π_w[H] = Σ w_nv_n⟨H, τ_{log n}^I H⟩ = 2⟨H, P_wH⟩,
    Π_{c·1}[𝔇_R F] = c·𝒦_R[F],   𝒦_R[F] := 2⟨𝔇_R F, [M_x, 𝔇_R]F⟩ = 2 Σ_{m,n<R} (log n)(mn)^{−1/2}⟨τ_{log m}^I F, τ_{log n}^I F⟩,
    Q_R^{(c)} = 𝒜∘𝔇_R + 2A(𝔇_R·)B(𝔇_R·) − c·𝒦_R,
and every term on the right, as well as the four transported constraints and ℓ_g, is built from the integers n < R and
log n only: Λ has disappeared.
*Proof.* P_w𝔇_R = Φ_R((wΛ)∗1) by the homomorphism, and [M_x, 𝔇_R] = Φ_R(log) by (3.1). By injectivity on n < R they are
equal iff ((wΛ)∗1)(n) = log n = (Λ∗1)(n) for 2 ≤ n < R (CITED: Λ∗1 = log). Induction on n: if w_d = 1 for prime powers
d < n, the n-th equation reads w_nΛ(n) = Λ(n), so w_n = 1 when n is a prime power (and nothing is asked otherwise).
Linearity gives the c·1 case; the formula for Π is the definition of c^sym with v_n = 2Λ(n)n^{−1/2}. ∎
Reading. The 𝔇-comb (integer weights n^{−1/2}) and Π (weights Λ(n)n^{−1/2}) are not two independent combs: on 𝔇-images
Π *is* the position commutator of 𝔇. The ARGUED cancellation of 19A §5(ii) is literally Q₀ := 𝒜∘𝔇 + 2AB against c·𝒦_R.

### Lemma 3.3 (window sandwich; PROVED)
Let λ₀ = min_{V_R} Q_R^{(1)}/‖F‖² ≥ 0 with a unit minimiser u, K₀ = 𝒦_R[u], and ‖𝒦‖ the norm of 𝒦_R on V_R. Then
    λ₀/‖𝒦‖ ≤ c_+ − 1 ≤ λ₀/K₀ (if K₀ > 0),      1 − c_− ≥ λ₀/‖𝒦‖,      1 − c_− ≤ Q_R^{(1)}[v]/|𝒦_R[v]| for every v with 𝒦_R[v] < 0;
symmetrically with the roles of c_± exchanged when K₀ < 0. In particular J_R → {1} as soon as λ₀(R) → 0 and there are
unit vectors of bounded Rayleigh quotient with 𝒦 of both signs; and J_R ⊇ [1 − λ₀/‖𝒦‖, 1 + λ₀/‖𝒦‖].
*Proof.* Q_R^{(c)}[u] = λ₀ − (c − 1)K₀ < 0 for c > 1 + λ₀/K₀; Q_R^{(c)}[F] ≥ (λ₀ − |c − 1|‖𝒦‖)‖F‖²; the last bound is the
same Rayleigh argument with v. ∎
Measured: K₀ = 𝒦_R[u] = 0.087, 0.126, 0.086, 0.157, 0.132, 0.112 (R = 3…8, T = 0.8; similar at 1.0) and λ₀/K₀ reproduces
the bisected c_+ − 1 to 2–3 digits in every row of 2.2 (e.g. R = 4: 5.16·10⁻⁵ vs 5.04·10⁻⁵; R = 8: 6.87·10⁻¹⁹ vs 6.87·10⁻¹⁹).
The second and third eigenvectors also have K > 0 (0.30–0.80); the c < 1 side is reached through the coupling of u to
higher eigenvectors, which is why δ_− ≫ δ_+.

### 3.4 What the shrinking window is (PROVED from 3.2–3.3 + NUMERICAL λ₀)
By Lemma 3.3 the two-sided shrinking J_R → {1} is the same fact as the 18A collapse λ₀(R) → 0, read in the weight
variable: the window has width ≍ λ₀(R)/O(1). It is the R-cell counterpart of the full-form behaviour recorded in 17A
(c > 1 dies at λ_A/Π_T(F)). Nothing beyond λ₀ and the slopes enters. In particular:
(i) The window shrinking does **not** supply a lower bound; it is equivalent to the absence of one. The "identity +
coercive remainder" split asked for in the task is, after Prop. 3.2, Q_R^{(1)} = Q₀ − 𝒦_R with both pieces Λ-free; there
is no remainder left over after the identity is used — the identity *is* the rewriting, and the whole sign question is
the sign of the Λ-free form Q₀ − 𝒦_R on V_R. Its bottom λ₀(R) in ℓ_g units is 0.74, 0.68, 5·10⁻³, 1·10⁻¹, 1·10⁻⁶,
5·10⁻¹² (R = 3…8, T = 0.8, gauge rank 20; 18A, mp.txt). **No R-uniform lower bound in ℓ_g (NUMERICAL; NO-GO for an
R-uniform κ_R on this class, already recorded in P211-18A).**
(ii) Falsifier test (rule 4) on the statement "J_R shrinks to {1}" and on Prop. 3.2:
  (a) cΛ, c ≠ 1: excluded for R large (|c − 1| > δ_±(R)); the statement FAILS for (a), as required.
  (b) a_P: excluded from R = 4 on, by O(1) (2.3); FAILS for (b), as required.
  (d) finite modification at n: excluded once R > n (per-atom table); FAILS for (d) asymptotically, as required; at any
      fixed R it is blind beyond the R-th cell (19A §5.1).
  (c) Beurling systems: Prop. 3.2 holds verbatim for any generalized-integer system N with its own Λ_N (Λ_N ∗ 1_N = log
      on N is the definition of Λ_N through ζ_N′/ζ_N, CITED): the truncated algebra Φ_R is built on N ∩ [1, R) and the
      identity P𝔇 = [M_x, 𝔇] holds iff w ≡ 1 there. So the *identity* is not specific to ℕ; it singles out "the von
      Mangoldt function of whatever integer system builds 𝔇". Lemma 3.3 is system-free. Hence the mechanism of the
      shrinking window SURVIVES (c): for a Beurling system whose R-cell form is near-degenerate the window shrinks to {1}
      the same way. By rule 4 the shrinking window is not a sign step. (ARGUED for the numerical part: no Beurling
      system was computed; the structural part is PROVED.)
(iii) What would be Λ-specific is the sign of λ₀(R) itself for the Λ-free pair (Q₀, 𝒦_R) built from ℕ, i.e. the integer
data n^{−1/2}, log n, the archimedean 𝒜 and the additive A, B, f(λ) constraints. That is the original question
restricted to R-cell data; 3.2 only removes Λ from its statement.

## 4. Corpus and index notes
New: Φ_R (truncated Dirichlet algebra of a window) and Prop. 3.2 (iff form of the identity on n < R); Lemma 3.3 (window
sandwich); the measured window table. Same mechanism as P211-17A (full form) and P211-18B Lemma 1.1 (tail form); this
round moves both to R-cell data and closes the "two-sided falsifier failure as a new resource" reading of 19A §5(ii).

## Result
NO-GO (class: positivity windows in the comb weight on idealised R-cell data, uniform or per-prime) with PROVED pieces.
J_R → {1} two-sidedly and super-exponentially fast (NUMERICAL, outer bounds, R ≤ 8), but by Lemma 3.3 this is equivalent
to λ₀(R) → 0 and carries no lower bound; by Prop. 3.2 the c-dependence is c·𝒦_R with 𝒦_R Λ-free, and the mechanism
survives falsifier (c).

### What was proved
- Lemma 1.1: every weight window is a closed interval.
- §2.1: Galerkin windows are outer bounds for the true window (nested trial spaces).
- §3.1: Φ_R is an algebra homomorphism from Dirichlet convolution to compressed shifts of the window, kernel = {α_n = 0, n < R};
  [M_x, Φ_R(α)] = Φ_R(α log).
- Prop. 3.2: P_w𝔇_R = [M_x, 𝔇_R] iff w ≡ 1 on prime powers < R; Q_R^{(c)} = Q₀ − c𝒦_R with Q₀, 𝒦_R, constraints, ℓ_g Λ-free.
- Lemma 3.3: λ₀/‖𝒦‖ ≤ c_+ − 1 ≤ λ₀/K₀ and the c_− analogues.
- Falsifier analysis §3.4(ii): shrinking fails (a), (b), (d) asymptotically; the identity and the sandwich survive (c).

### What failed and why
- "Shrinking window ⇒ Λ-specific sign": the shrinking is the collapse λ₀ → 0 in another variable (Lemma 3.3), and its
  mechanism (Prop. 3.2) holds for every generalized-integer system with its own Λ.
- "Identity + coercive remainder": after Prop. 3.2 there is no remainder; the R-cell sign question is exactly
  Q₀ − 𝒦_R ≥ 0 on V_R, whose bottom decays like exp(−≈2.9 R log R) (fit, NUMERICAL) in ‖F‖² and to 10⁻¹² in ℓ_g units.

### Next concrete step
Use Prop. 3.2 as a Λ-free restatement of the R-cell problem: compute the near-null direction of Q₀ − 𝒦_R and test
whether it is (up to the transported constraints) the 𝔇_R-preimage of the bottom vector of the window form 𝒜 − Π on
(−h, h) — if so, λ₀(R) is the window form's bottom eigenvalue times ‖𝔇_R^{−1}‖-type factors (𝔇_R^{−1} = Φ_R(μ)), and the
R-cell route reduces to the known window bottom with no new information; if not, the defect locates what the transported
constraints add.

## Reproducibility
tools/multi_cell/window_build.py R Nb T J dps [NQ] → split pickle (Q₀, Q_n per atom, C, ℓ_g, 𝔇); ≤ 11 min at R = 8, Nb 40,
110 digits. tools/multi_cell/window_scan.py pickle mode [grid], modes c, p:K (powers of K), a:K (atom K), P:K (a_K),
info (bottom eigenpairs and per-atom slopes); FAST=1 uses the Cholesky test only. Every run ≤ 20 min.
