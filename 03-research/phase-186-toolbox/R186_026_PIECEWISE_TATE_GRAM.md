# R186_026 — The piecewise Tate Gram matrix G_k(T): closed form, structure, positivity, limit

Phase 186, round 13. Sources: Paper 47 (thm:A Lévy form in x-space, lem:K, thm:S(iii), thm:margin), R186_024 (𝒱_k ⊕ E_k, §1.3–1.4: K₁ = K − 2e^{−u/2}), R186_104 (audit: (L2) inherits the entire margin), R186_019/R155 (edge-mode Schur).
Script: `r026_gram.py` (standalone; mpmath dps = 30 for the closed form, 1-D quadrature in float64 as an independent check, `r024_schur.py` as a third check). Labels: PROVED / NUMERICAL / CONDITIONAL / OPEN / NO-GO.

## 0. Verdict

1. **Complete closed form of G_k(T)** (PROVED, §1): every entry is a finite combination of exponentials of the block endpoints, ψ(¼+·/2), log, artanh, Li₂ and the Legendre chi function χ₂, evaluated at z = e^{−2·(endpoint difference)}. Verified against the 1-D quadrature of the analytic integrand (difference ≤ 6·10⁻¹⁶) and against the Galerkin computation of `r024_schur.py` (λ_min(W|E_k) matches to 7 digits at ½log3 and ½log5, for both orbit partitions and equal-k partitions).
2. **Structure** (§2): in the variable ξ = e^{2x}, G_k is an integrated Cauchy-type matrix (kernel 1/(ξ−η) against monomials ξ^p over intervals); all cross archimedean entries and all prime entries are ≤ 0; it is not totally positive, has no product determinant, and no low numerical rank (singular values of the cross part 1.0, 0.41, 0.40, 0.39, 0.33, …). The Tate vectors are explicit and the Tate kernel has a **local** basis (support on two blocks, PROVED), but no basis makes it diagonally dominant: in the full basis G_k is indefinite for every k (PROVED: 𝔞_T(e^{x/2}1_{I_T}) < 0), and in the local Tate basis dominance fails by 3.75 at ½log5 (NUMERICAL). **Structural finding:** G_k(T) has **exactly one negative eigenvalue** in the full basis for every T ∈ [0.36, ½log5] and every k ≤ 13 (NUMERICAL; also for 𝔞_T over all of L²(I_T) with a dimension-70 Galerkin discretization), and hence (Lemma 2.4, algebra PROVED) positivity over E_k is equivalent to a **scalar criterion**: det(T_k G_k^{−1} T_kᵀ) < 0, with T_k the 2×2k Tate matrix. The 2×2 matrix S_k = T_kG_k^{−1}T_kᵀ always has one eigenvalue equal to −1.000 (to 10⁻⁵ with k = 13, at every T): OPEN (unexplained).
3. **Positivity** (§3): the exact finite inequality (L2_k) has margin λ_min(W|E_k) ≥ λ_A, decreasing in k toward λ_A (E_k is a form core: PROVED). This is a pure rewriting: **NO-GO as a route**; the closed form is kept as a lemma, with two honest uses: **exact, certifiable** upper bounds on λ_A (λ_A ≤ λ_min(W|E_k), elementary functions) and the scalar criterion of Lemma 2.4.
4. **Limit k → ∞** (§4): G_k converges to the jump kernel 𝒢_T(x,x′) = 𝔞_T(ψ_x, ψ_{x′}), ψ_x(y) = 2 sinh((y−x)/2)1_{(x,T)}(y), explicit in the same functions; D on the window T ⟺ conditional positivity (modulo the two Tate functionals) of the 2×2 matrix kernel (𝒢^{χχ}, 𝒢^{χψ}; 𝒢^{ψχ}, 𝒢^{ψψ}) over finite jump configurations (PROVED as a reformulation; OPEN as a tool).

**Sign contact: none.** No computation gives λ_min(W|E_k) < 0: all values are positive (table §3), consistent with λ_A > 0 from Paper 47. The single negative direction of G_k in the full basis is eliminated by the two Tate conditions.

## 1. Closed form of G_k(T) (PROVED)

Basis: φ_{j,α} = e^{αx}1_{B_j}, α ∈ {±½}, B_j = (a_j, b_j), j = 1..k, a partition of I_T = (−T,T). Form (thm:A): 𝔞_T(F,G) = C₀⟨F,G⟩ + ∫₀^∞K(u)(⟨F,G⟩ − 𝒞_{FG}(u))du − Σ_{n∈𝒩_T} v_n𝒞_{FG}(log n), 𝒞_{FG}(u) = ½[∫F(t)G(t−u)dt + ∫G(t)F(t−u)dt], K(u) = 2Σ_{m≥0}e^{−s_m u}, s_m = 2m+½ (lem:K). Notation:

 E(γ;a,b) := ∫_a^b e^{γx}dx, τ(r) := ∫_r^∞K = log coth(r/4) + π − 2 arctan e^{r/2} (thm:S iii), z_D := e^{−2D},
 S₁(z,a) := Σ_{m≥1} z^m/(m+a) = zΦ(z,1,1+a), S₂(z,a) := Σ_{m≥1} z^m/(m+a)² = zΦ(z,2,1+a), Q_L(c) := (1−e^{−cL})/c (Q_L(0) = L). (1.1)

The only parameters that appear are a ∈ {0, ¼, ½} (and 5/4, 3/2 in ψ), for which Φ is elementary: Φ(z,1,1) = −log(1−z)/z, Φ(z,1,3/2) = 2z^{−3/2}(artanh√z − √z), Φ(z,2,1) = Li₂(z)/z, Φ(z,2,3/2) = 4z^{−3/2}(χ₂(√z) − √z) with χ₂(w) = ½[Li₂(w) − Li₂(−w)]; Φ(z,1,5/4) is elementary with log and arctan of z^{1/4} (the same antiderivative ∫dt/(1−t⁴) that gives τ).

**Lemma 1.1 (cross entries).** For B_i = (a,b) to the right of B_j = (c,d) (d ≤ a):

 X_{ij}^{αβ} = −½∬_{B_i×B_j}K(x−y)e^{αx}e^{βy}dxdy = −Σ_{m≥0}E(α−s_m;a,b)E(β+s_m;c,d)
 = −E(α−½;a,b)E(β+½;c,d) − ¼ Σ_{x∈{a,b}} Σ_{y∈{c,d}} σ_xσ_y e^{αx+βy−(x−y)/2} Λ(z_{x−y}; ¼−α/2, ¼+β/2), (1.2)

with σ_a = σ_d = +1, σ_b = σ_c = −1 and Λ(z;a₁,a₂) := Σ_{m≥1}z^m/((m+a₁)(m+a₂)) = [S₁(z,a₁) − S₁(z,a₂)]/(a₂−a₁) if a₁ ≠ a₂ (and = [ψ(1+a₂) − ψ(1+a₁)]/(a₂−a₁) if z = 1, adjacent blocks), Λ = S₂(z,a₁) if a₁ = a₂ (ζ(2,1+a₁) if z = 1). The first term is the m = 0 term from R186_024 §1.4 (2e^{−u/2}, rank one, killed by the Tate condition of either block); the sum is the coupling with kernel K₁. The (+,+) and (−,−) entries are log/artanh; the (+,−) and (−,+) ones (a₁ = a₂) carry Li₂/χ₂.
*Proof.* For disjoint supports ⟨F,G⟩ = 0 and 𝒞_{FG}(u) = ½∫F(t)G(t−u)dt, so the entry is −½∬K(x−y)F(x)G(y) (prop:nodes of Paper 47); inserting the series from lem:K (Tonelli, everything positive) and integrating term by term; E(α−s;a,b)E(β+s;c,d) is expanded at the four vertices with 1/((s_m−α)(s_m+β)) = ¼/((m+¼−α/2)(m+¼+β/2)) and e^{−s_m(x−y)} = e^{−(x−y)/2}z^m. ∎

**Lemma 1.2 (same-block entries).** With L = b−a, z = z_L, γ = α+β:

 A_{jj}^{αβ} = (C₀ + τ(L))E(γ;a,b) + D^{αβ}(a,b), D^{αβ} := ∫₀^L K(u)[E(γ;a,b) − ½(e^{−αu}+e^{−βu})E(γ;a+u,b)]du. (1.3)

(i) α = β (γ = 2α = ±1):

 D^{αα} = (1/γ){ e^{γb}[2(Q_L(½) − Q_L(½+α)) + ψ(5/4+α/2) − ψ(5/4) − e^{−L/2}S₁(z,¼) + e^{−(½+α)L}S₁(z,¼+α/2)]
 + e^{γa}[2(Q_L(½−α) − Q_L(½)) + ψ(5/4) − ψ(5/4−α/2) − e^{−(½−α)L}S₁(z,¼−α/2) + e^{−L/2}S₁(z,¼)] }. (1.4)

(ii) β = −α (γ = 0):

 D^{α,−α} = L[4(1−e^{−L/2}) − L − (1−e^{−L})] + L²/2 + 1 − e^{−L}(1+L) + L·Σ_Q + Σ_I,
 Σ_Q = ½[ψ(1) + ψ(3/2)] − ψ(5/4) − e^{−L/2}S₁(z,¼) − ½log(1−z) + ½e^{−L}S₁(z,½),
 Σ_I = π²/24 + π²/8 − 1 − ¼Li₂(z) + (L/2)log(1−z) − ¼e^{−L}S₂(z,½) − (L/2)e^{−L}S₁(z,½). (1.5)

*Proof.* For u ≥ L, 𝒞_{FG} = 0 and we are left with E(γ;a,b)τ(L). For u < L, ∫F(t)G(t−u) = e^{−βu}E(γ;a+u,b) and the symmetric expression with α; the bracket is O(u), so K·bracket is analytic on [0,L] (uK is) and the series from lem:K can be integrated term by term (each term converges, the sum converges like Σ1/m²). In (i) the bracket is [e^{γb}(1−e^{−αu}) + e^{γa}(e^{αu}−1)]/γ; in (ii) it is L(1−cosh(u/2)) + u cosh(u/2). The sums Σ_{m≥1}[1/(m+a) − 1/(m+b)] = ψ(1+b) − ψ(1+a), Σ_{m≥1}z^m/(m+a) = S₁, Σ_{m≥1}∫₀^L u e^{−cu} give ψ, S₁, S₂, Li₂; the m = 0 term is written separately because it contains the cases s₀ ∓ α = 0 (Q_L(0) = L). ∎

**Lemma 1.3 (primes).** For n = p^r with log n < 2T, ℓ = log n, v_n = 2 log p/√n:

 P_{ij}^{αβ,n} = −(v_n/2)[ e^{−βℓ}E(γ; B_i ∩ (B_j+ℓ)) + e^{−αℓ}E(γ; B_j ∩ (B_i+ℓ)) ], E(γ;∅) := 0, B ∩ (B′+ℓ) = (max(a,c+ℓ), min(b,d+ℓ)). (1.6)

Entry nonzero only if |B_i − B_j| reaches ℓ; ≤ 0 always (γ real ⇒ E > 0). *Proof:* ∫F(t)G(t−u)dt with F = e^{αt}1_{(a,b)}, G = e^{βy}1_{(c,d)} equals e^{−βu}∫_{(a,b)∩(c+u,d+u)}e^{γt}dt. ∎

**Lemma 1.4 (mass and Tate).** M_{ij}^{αβ} = δ_{ij}E(α+β;B_j) (2×2 per block, [[E(1), L],[L, E(−1)]]); the two Tate functionals in coordinates are t_±(j,α) = E(α±½;B_j), i.e. t₊ = (e^{b_j}−e^{a_j}, L_j)_j, t₋ = (L_j, e^{−a_j}−e^{−b_j})_j; E_k = {c : t₊·c = t₋·c = 0}, dim 2k−2; and

 λ_min(W|E_k) = minimum eigenvalue of the pencil (ZᵀG_kZ, ZᵀM_kZ), Z a basis of ker(t₊,t₋), G_k = A_diag + A_cross + Σ_nP^n. (1.7)

**Verification (NUMERICAL).** (a) (1.2)–(1.5) against the Gauss quadrature (80 nodes) of the analytic integrand, 10 test entries: difference ≤ 6·10⁻¹⁶. (b) exact λ_min(W|E_k) vs `r024_schur.py` (N = 14, min G_EE column): ½log3 orbit 0.1141811 / 0.1141811; ½log3 k = 5 equal 0.01627632 / 0.01627632; ½log5 orbit 0.01410093 / 0.01410093; ½log5 k = 5 0.01685231 / 0.01685231; ½log5 k = 9 0.001963476 / 0.001963476. Seven digits in every case (the polynomial basis of r024 approximates e^{±x/2} to 10⁻¹⁵ on blocks of length ≤ 0.8).

## 2. Structure of G_k(T)

**2.1 Cauchy in ξ = e^{2x} (PROVED).** With X = e^x, Y = e^y and x > y: K(x−y) = 2X^{3/2}Y^{1/2}/(X²−Y²), so K(x−y)e^{αx}e^{βy}dxdy = ½ ξ^{α/2−¼}η^{β/2−¾}/(ξ−η)·dξdη with ξ = X², η = Y². The cross archimedean part is the integral of the Cauchy kernel 1/(ξ−η) against monomials ξ^p η^q (p ∈ {0,−½}, q ∈ {−½,−1}) over rectangles: an "integrated Cauchy" structure, which is where the log/artanh terms (p+q integer) and the Li₂ terms (p+q half-integer) come from. Consequences: (i) the triangular kernel K(x−y)1_{x>y} is totally positive (Cauchy ordered by positive factors), but the symmetric kernel K(|x−y|) is not (K is log-convex on (0,∞), not PF₂: 1/|u| already fails), and G_k has entries of both signs on the block diagonal; **G_k is not totally positive, not block-Toeplitz (τ(L) and the endpoints break the invariance), and has no product determinant** (the Cauchy integral over rectangles is not a Cauchy matrix). (ii) Signs (PROVED by (1.2) and (1.6)): all cross archimedean entries are ≤ 0 (each E > 0, each Λ > 0) and all prime entries are ≤ 0; on the block diagonal the three entries (+,+), (+,−), (−,−) equal (C₀ + τ(L))E + D with D > 0 of order L: positive for short blocks (L = 0.18 at ½log5, k = 9: +0.023, +0.047, +0.096), negative for long blocks (a single block I_T at ½log5: 𝔞_T(e^{x/2}1_{I_T}) = −5.592).

**2.2 Numerical rank (NUMERICAL, ½log5, k = 9).** Singular values of A_cross: 0.996, 0.409, 0.397, 0.394, 0.331, 0.252, 0.154, 0.146, …: slow decay (the 1/u term of K₁ between adjacent blocks is of Hilbert type, essential spectrum [0,π], R186_104 §5b). No low rank. Rank of the prime terms: n = 2: 16, n = 3: 12, n = 4: 8, with r_n := #{j : a_j + log n < T} = 6, 3, 2 blocks reached; the general bound is

 rank P^n ≤ 4 r_n(k), r_n(k) = ⌈k(1 − log n/2T)⌉ (+1), (2.1)

(PROVED: S_ℓ maps E_k into Tate exponentials over the shifted partition, image of dimension ≤ 2r_n; symmetrizing doubles it), adjusted for n = 3, 4. **The rank grows linearly in k**: the primes are not a bounded-rank perturbation except for the most recent contact (log n ≈ 2T).

**2.3 Inertia (NUMERICAL, a finding).** In the full basis (2k functions, no Tate), G_k(T) has **exactly one negative eigenvalue** in every computed case: T ∈ {½log3, log 2, ½log5} × k ∈ {5, 9, 13}, and at T = 0.36 for k ≤ 13. The archimedean part alone has n₋ = 2 (½log3) and 3 (log 2, ½log5): the primes *reduce* the negative inertia to 1. Same for 𝔞_T over the whole of L²(I_T) (Galerkin from r024, dimension 42–70, no Tate): n₋ = 1 at all eight T in [0.36, ½log5], with λ₁ ∈ [−1.34, −3.33] and λ₂ ≈ λ_A (9.45·10⁻⁴ at ½log3, 3.2·10⁻¹² at ½log5). That n₋ ≥ 1 is PROVED: 𝔞_T(e^{x/2}1_{I_T}) = −5.592 at ½log5 (closed form (1.3)–(1.4) with one block). That n₋ ≤ 1 is OPEN (R155 Thm P only gives n₋ ≤ 5/7/8).

**Lemma 2.4 (scalar criterion; algebra PROVED).** Let G be symmetric invertible n×n with n₋(G) = 1, T_k ∈ ℝ^{2×n} of rank 2, S := T_kG^{−1}T_kᵀ. Then G ⪰ 0 on ker T_k ⟺ n₊(S) = 1 ⟺ det S < 0 (or = 0 with one positive eigenvalue, a boundary case). *Proof:* Haynsworth inertia additivity for the bordered matrix [[G, T_kᵀ],[T_k, 0]]: n₋(bordered) = n₋(G) + n₋(−S) = 1 + n₊(S), and G|ker T_k ⪰ 0 ⟺ n₋(bordered) = 2 (Finsler). ∎
Application (CONDITIONAL on n₋(G_k) = 1): positivity per window on E_k is the sign of an implicit closed-form 2×2 determinant (the resolvent of G_k applied to the two Tate vectors). NUMERICAL: eigenvalues of S_k = (−1.0004, +0.117) at T = 0.36, k = 3; (−1.00001, +0.997) at ½log5, k = 13; at every computed (T,k) the negative eigenvalue is −1.000 ± 4·10⁻³ and converges to −1 as k grows, while the positive one grows toward 1. With no primes, the 2×2 matrix is negative definite at ½log3, log 2 and ½log5 (n₊ = 0, so n₋(𝔞_∞|E_k) = n₋(𝔞_∞) − 2 = 0, 1, 1: the archimedean part alone is positive only at ½log3, consistent with the 0.596 threshold of R155). The exact eigenvalue −1 is OPEN: we have no explanation internal to the form 𝔞_T; it is recorded as a potential falsifier for any future identity.

**2.5 Basis changes.** (i) Explicit Tate vectors: (1.7). (ii) **Local Tate basis (PROVED):** for each adjacent pair (B_j, B_{j+1}) the kernel of t_± restricted to span{e^{±x/2}1_{B_j}, e^{±x/2}1_{B_{j+1}}} has dimension 2; the 2(k−1) vectors so obtained are independent and generate E_k (equivalently: E_k = (¼−∂²)𝒮_k with 𝒮_k = {G ∈ H₀²(I_T) : G ∈ span{e^{±x/2}, xe^{±x/2}} on each block, C¹}, "Tate splines" with minimal support of two blocks). (iii) Jump basis: F = Σ_j[δ_jχ_{x_j} + δ′_jψ_{x_j}], χ_x = cosh((y−x)/2)1_{y>x}, ψ_x = 2sinh((y−x)/2)1_{y>x}, explicit triangular change of basis. (iv) **Diagonal dominance: NO** (NUMERICAL at ½log5, k = 9): jump basis min(diag − Σ|off|) = −48; local Tate basis (mass-normalized) diagonals ≥ 1.33 but min(diag − Σ|off|) = −3.75; archimedean alone −2.03. And it is impossible in the full basis (PROVED, 2.3: G_k indefinite). Nor does "tridiagonal + primes" work: the archimedean symbol over the Tate splines is m(τ)(τ²+¼)² ~ log|τ|·τ⁴, not local; in the jump basis the entries decay like |x_j − x_l|^{−3} (two derivatives of 1/u), they do not vanish.

## 3. Positivity on E_k: the finite inequality and its margin

**3.1 Decomposition (PROVED).** G_k = Lev_k − |C₀|M_k − Σ_n P^n, where Lev_k := A_diag + A_cross − C₀M_k is the Gram matrix of the Lévy form ¼∬K(|x−y|)|F(x)−F(y)|² + ½∫κ|F|² (prop:nodes), positive semidefinite as a continuous sum of rank-one terms ‖F − S_uF‖²K(u)du (not finite rank one: each u gives a rank-2k form). The primes are −Σ_n P^n with rank (2.1). The exact inequality that decides W ≥ 0 on E_k is

 (L2_k): cᵀLev_k c ≥ |C₀| cᵀM_k c + Σ_n cᵀP^n c for every c with t₊·c = t₋·c = 0, (3.1)

with constants: |C₀| = 5.3721834, v₂ = 0.9803, v₃ = 1.2686, v₄ = 0.6931, and all entries from (1.2)–(1.6).

**3.2 Margin (NUMERICAL; k equal blocks; λ_A from Paper 47 / r024 as a reference).**

| T | k=3 | k=5 | k=9 | k=13 | k=20 | k=30 | λ_A (Galerkin) |
|---|---|---|---|---|---|---|---|
| ½log3 | 1.06e-1 | 1.63e-2 | 4.89e-3 | 1.81e-3 | 1.18e-3 | 9.87e-4 | 9.45e-4 |
| 0.62 | 1.70e-1 | 2.41e-2 | 3.72e-3 | 1.35e-3 | 2.84e-4 | 8.39e-5 | 1.87e-5 |
| log 2 | 1.40e-1 | 3.55e-2 | 5.13e-3 | 1.46e-3 | 2.70e-4 | 7.09e-5 | 1.35e-7 |
| ½log5 | 8.30e-2 | 1.69e-2 | 1.96e-3 | 8.55e-4 | 2.61e-4 | 6.27e-5 | 3.2e-12 |

All positive (no negative eigenvalue of the pencil at any (T,k)).

Reading: λ_min(W|E_k) ≥ λ_A always (E_k ⊂ 𝒫_T) and decreases monotonically toward λ_A; at ½log3 with k = 30 it is within 4% of λ_A; at ½log5 (λ_A ≈ 3·10⁻¹²) it drops by 10³ between k = 3 and 30 and is still eight orders away: the convergence is that of thm:margin (λ_A ~ e^{−15T}), not of the method. **Theorem 3.3 (PROVED).** For nested partitions with mesh → 0, ∪_kE_k is a form core for 𝔞_T and λ_min(W|E_k) ↓ λ_A. *Proof:* piecewise Tate exponentials interpolate any F ∈ C²(I_T) with uniform error O(h²) and k jumps of size O(h²); the Lévy energy of the difference is ≤ C(h² + k·h⁴) → 0 (smooth part with derivative O(h) against uK ≤ 1; k jumps of size O(h²)); the Tate defect of the interpolant is O(h²) and is corrected by adding O(h²) multiples of two fixed functions of E_k (form cost O(h⁴)); C²(Ī_T) is a form core (interior dilation + regularization in the norm ∫log(2+|τ|)|F̂|², the domain of thm:A). ∎
Consequence: (3.1) is **necessary** for D on the window for every k and **sufficient only in the limit**, where its margin is exactly λ_A, that of thm:margin. A pure rewriting: **NO-GO as a route** (confirms R186_104 §6). What remains as a lemma: (a) λ_A ≤ λ_min(W|E_k), an upper bound **exact in elementary functions** (certifiable by interval arithmetic with no quadrature) and much finer than thm:margin at finite T; (b) the scalar criterion of Lemma 2.4.

## 4. Limit k → ∞: the jump kernel

**Theorem 4.1 (reformulation; PROVED).** Let 𝒮: g ↦ ∫ψ_x dg(x) be the causal Green's operator of ∂² − ¼ on [−T,T) (ψ_x as in 2.5(iii); g a distribution of order ≤ 1 with atoms at −T for the initial data). Then for every finite jump configuration F = Σ_j[δ_jχ_{x_j} + δ′_jψ_{x_j}],

 𝔞_T(F) = Σ_{j,l} (δ_j, δ′_j) 𝒢_T(x_j,x_l) (δ_l, δ′_l)ᵀ, 𝒢_T(x,x′) := [[𝔞_T(χ_x,χ_{x′}), 𝔞_T(χ_x,ψ_{x′})],[𝔞_T(ψ_x,χ_{x′}), 𝔞_T(ψ_x,ψ_{x′})]], (4.1)

with 𝒢_T in closed form via Lemmas 1.1–1.3 applied to the blocks (x, x′), (x′, T) (χ_x, ψ_x are combinations of e^{±y/2}1_{(x,T)}, and (x,T) = (x,x′) ∪ (x′,T)): for x < x′, 𝒢^{ψψ}(x,x′) = Σ_{α,β}σ_ασ_β e^{−αx−βx′}[X^{βα}_{(x′,T),(x,x′)} + A^{αβ}_{(x′,T)} + primes] (the right block (x′,T) carries β in (1.2)), σ_± = ±1, and analogously with ½ for χ. The Tate functionals are t_±(x) = (∫_x^Te^{±y/2}χ_x, ∫_x^Te^{±y/2}ψ_x), elementary. By Theorem 3.3:

 D on window T ⟺ Σ_{j,l}(δ_j,δ′_j)𝒢_T(x_j,x_l)(δ_l,δ′_l)ᵀ ≥ 0 for every finite configuration with Σ_j[δ_jt_±(x_j)₁ + δ′_jt_±(x_j)₂] = 0, (4.2)

that is, **conditional positivity (modulo two explicit functionals) of the continuous matrix kernel 𝒢_T** on [−T,T]². Label: PROVED as a reformulation equivalent to row D per window; OPEN as a tool (𝒢_T is not translation-invariant —τ(L), the endpoints and the primes prevent it—, so Bochner/Schoenberg do not apply directly). NUMERICAL (½log5): 𝒢^{ψψ} is continuous (𝒢(0,0) = −0.18447, 𝒢(0,10⁻⁶) = −0.18447) and negative over the whole square (−3.67 at (−0.8,−0.8) to −0.0056 at (0.4,0.4)): all the positivity is created by the two Tate relations, as in 2.3.

## 5. Audit notes

- The closed forms are verified by two independent methods (series/Lerch in mp, Gauss quadrature in float64) and by a third (Galerkin r024). A shift error (log p instead of log n for n = 4) was detected precisely through the discrepancy with r024 at ½log5 and fixed; the current script reproduces all five comparisons to 7 digits.
- n₋(G_k) = 1 and the −1 eigenvalue of S_k are NUMERICAL on the grid (T ≤ ½log5, k ≤ 13, Galerkin dim ≤ 70); nothing is claimed beyond that. Lemma 2.4 is algebra; its application is CONDITIONAL.
- Theorem 3.3 (form core) uses only the domain of thm:A and the bound uK ≤ 1 (R186_024 §1.4); Theorem 4.1 is bilinearity + 3.3.
- Nothing is claimed about the sign: all λ_min(W|E_k) are positive. No equivalence between row D and other statements is used.
- For Paper 47: Lemmas 1.1–1.4 and Theorem 3.3 (exact upper bound on λ_A via piecewise Tate exponentials) can be integrated as lemmas (verified against thm:A/lem:K/thm:S iii); the n₋ = 1 observation only as NUMERICAL. Do not integrate "(L2_k) as a finite target".
