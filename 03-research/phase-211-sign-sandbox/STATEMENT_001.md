# The sign problem in isolation: the statement of record for phase 211

Everything in this phase refers to the objects below and to nothing else. No equivalence with any
other statement is used, named or invoked. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN /
NO-GO / NUMERICAL.

## 1. The window form (Paper 47, §1.1)

For T > 0, I_T = (−T, T). For F ∈ L²(I_T) (extended by zero) write F̂(τ) = ∫ F(t) e^{iτt} dt and
c_F(u) = ∫ F(t) conj F(t−u) dt (autocorrelation, continuous, supported in [−2T, 2T], ĉ_F = |F̂|²).

    m(τ) = Re ψ(1/4 + iτ/2) − log π,          v_n = 2Λ(n)/√n,
    s_T(τ) = m(τ) − Σ_{n ≥ 2, log n < 2T} v_n cos(τ log n),
    a_T(F) = (1/2π) ∫_ℝ s_T(τ) |F̂(τ)|² dτ,
    A(F) = ∫ F(t) e^{t/2} dt,   B(F) = ∫ F(t) e^{−t/2} dt,   P_T = {F : A(F) = B(F) = 0},
    λ_A(T) = inf { a_T(F) : F ∈ P_T, ‖F‖ = 1 }.

Target (★): λ_A(T) ≥ 0 for every T > 0.
Known: PROVED (certified) for T ≤ ½ log 5; CITED for T ≤ ½ log 15 (Mori) and T ≤ 17/16 (Liu, preprint);
OPEN beyond. T ↦ λ_A(T) is continuous and non-increasing (PROVED).

Lévy form (PROVED, Paper 47 Lemma lem:K, Theorem thm:A):

    K(u) = 1/(2 sinh(u/2)) + 1/(2 cosh(u/2)) = 2 Σ_{j≥0} e^{−(2j+½)u}   (u > 0),
    m(τ) = C_0 + ∫_0^∞ (1 − cos τu) K(u) du,   C_0 = ψ(1/4) − log π = −5.3721834…,
    a_T(F) = C_0 ‖F‖² + ∫_0^∞ (c_F(0) − Re c_F(u)) K(u) du − Σ_{log n < 2T} v_n Re c_F(log n).

## 2. One explicit function of one real variable (PROVED, Paper 47 Theorem thm:oneprofile)

Fix a > 0 and b with |b| > ½, and 2T_0 < log 2 throughout. Put g = e^{bt} 1_{[0,a]}, c_g = g ∗ g̃, G_0 = c_g ∗ c_g, T_0 = 2a,
F_0 = (¼ − ∂²) G_0 normalised to ‖F_0‖ = 1 (so c_0(0) = 1). Then F_0 ∈ P_{T_0}, F̂_0(τ) = (τ² + ¼)|ĝ(τ)|⁴ > 0, and with c_0 = c_{F_0}

    B(d) = (1/2π) ∫ m(τ) F̂_0(τ)² cos(τd) dτ − ½ Σ_{n≥2} v_n [c_0(log n − d) + c_0(log n + d)].

(★) holds if and only if B is a positive definite function on ℝ.
Taking 2T_0 < log 2, (★) holds iff the integer-lattice matrices 𝔸_M = [B(log m − log k)]_{m,k ≤ M}
are positive semidefinite for every M (Proposition prop:AM), and
𝔸_M = Arch_M − Div_M − Near_M (exact Dirichlet coincidences k·n = m separated from the near ones).

## 3. The same function written as a smoothed Chebyshev fluctuation (CITED: Paper 47 lem:transl(iv) and thm:band; constants re-checked)

For d > 2T_0 the archimedean term is an exact finite exponential sum: since c_0(d) = c_0(d+u) = 0,

    (1/2π) ∫ m F̂_0² cos(τd) dτ = −½ ∫ K(d − u) c_0(u) du = −Σ_{j≥0} e^{−(2j+½)d} ∫ e^{(2j+½)u} c_0(u) du ,

and the j = 0 term vanishes because ∫ e^{u/2} c_0(u) du = A(F_0) B(F_0) = 0. Hence, with x = e^{d}
and φ(y) := y^{−1/2} c_0(log y) (supported in [e^{−2T_0}, e^{2T_0}] ⊂ (½, 2)),

    B(log x) = − x^{−1/2} Σ_{n≥2} Λ(n) φ(n/x) − Σ_{j≥1} γ_j x^{−(2j+½)},   x > e^{2T_0},
    γ_j = ∫ e^{(2j+½)u} c_0(u) du  (explicit, the trivial exponents),
    ∫ φ(y) dy = ∫ φ(y) dy/y = 0   (the two Tate conditions on F_0).

So, for x beyond the first window, B(log x) is minus the smoothed, normalised fluctuation of the
Chebyshev function at scale x, with a smoothing φ of two vanishing moments, up to an explicit
O(x^{−5/2}) tail. For d ≤ 2T_0 the formula of §2 holds with its archimedean part.

Consequence (PROVED, Bochner; this is the 2×2 band of Paper 47 thm:band): (★) implies |B(d)| ≤ B(0)
= a_{T_0}(F_0) for all d, i.e. |Σ_n Λ(n) φ(n/x)| ≤ a_{T_0}(F_0) √x + O(x^{−2}) for x > e^{2T_0}. This
is a two-sided bound without sign; it is necessary, not sufficient. The full statement (★) is the
positive definiteness of B, i.e. the positivity of all Toeplitz minors [B(d_i − d_j)], of which the
band is the 2×2 case. Any proof of (★) must therefore bound the smoothed fluctuation at scale √x
with an explicit constant, and must do more.

NUMERICAL (validation only, a = 0.15, b = 1, 2400001 nodes on |τ| ≤ 600, Λ up to 4.4·10⁵):
B(0) = +0.01492, and |B(d)| ≤ 0.0122 for 0 < d ≤ 13; the archimedean part is below 10⁻⁶ for d ≥ 1.5.
Consistent with (★); proves nothing.

## 4. What the proof must do (Paper 47 Problem prob:region and Proposition prop:spec)

The sign step must (i) use the exact values Λ(n), n < e^{2T}, not a class closed under modification
(deleting the primes below P, or scaling Λ ↦ cΛ, c ≠ 1, falsifies (★) at explicit windows);
(ii) use the Euler product over ℕ and the functional equation with Γ(s/2) jointly;
(iii) be non-linear in Λ (not a certificate, not an operator identity closed by Cauchy–Schwarz);
(iv) not be a bounded functional of the weights, not local on the negative set of s_T, not a
mean-square or absolute-value bound; (v) win from the fluctuation of Λ, not its density; (vi) be
exact at the centre and at the integer resolution: the sign is decided on vectors that see the
near-coincidences m ≈ k·n, m ≠ k·n.

The open clause: an object coupling (Λ(n))_{n<N} with the functional equation by a route other
than the factor ζ(½ + iτ). No such object is known. Building it is the task of this phase.

## 5. Internal reformulations

Within this phase the target may be rewritten in any form proved equivalent to (★) from the
definitions above (forms (L2), (N), (S), (B), the Kreĭn extension form, the leakage form). Such
rewritings are moves inside the sandbox. What is excluded is any equivalence with, or reduction to,
statements about objects outside the definitions above.
