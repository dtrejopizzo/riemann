# Round 22 A — The R-cell form over generalized integer systems

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_016_B, ROUND_018_A, ROUND_019_A, ROUND_021_A (𝔇_R, Φ_R, Q_R, V_R,
ℓ_g, Π, 𝒦_R). Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Index rows read: P211-17A, P211-18A, P211-18B, P211-19A, P211-21A; the guiding principle of the index README (the sign must
come from the semiring (ℕ,+,·), from near-coincidences m ≈ kn; a purely multiplicative property is not enough by G1, a purely
additive one is not enough by the FE-class/Epstein observations); index falsifier F-root (p ↦ p^{1/m}, ℕ ∪ √2ℕ, phases 163/184).
What differs. 21A §3.4(ii)(c) recorded that Prop. 3.2 (P_w𝔇_R = [M_x,𝔇_R] iff w ≡ 1) holds for every generalized integer
system and stated, as ARGUED and uncomputed, that the shrinking-window mechanism survives Beurling systems. No row computed the
R-cell form for a system other than ℕ. Here the object is the map 𝒩 ↦ λ₀(R; 𝒩) := bottom of Q₀^𝒩 − 𝒦_R^𝒩 on V_R, for
systems 𝒩 near ℕ and for a few structurally different ones, with the summation set of the transported constraints varied
independently of 𝒩. This is a measurement of the falsifier class (c) on R-cell data, plus a first-variation formula; it does
not reuse the window variable c of 21A.

## 1. Set-up
### 1.1 Systems
A system 𝒩 is the multiplicative closure of a set of real generators g > 1, taken as a set; Λ_𝒩 is the unique function on
𝒩 \ {1} with Σ_{de = x, d,e ∈ 𝒩} Λ_𝒩(d) = log x for all x ∈ 𝒩 (Dirichlet recursion; CITED/definition). For a free system
(no multiplicative relations among generators) Λ_𝒩(g^k) = log g and Λ_𝒩 = 0 elsewhere. On the window I = (−h, h), ℓ = 2h = log R
(the window length is kept at log R for every system),
    𝔇^𝒩 = Σ_{x∈𝒩, x<R} x^{−1/2} τ_{log x}^I,    Π^𝒩[H] = Σ_{x<R} 2Λ_𝒩(x)x^{−1/2}⟨H, τ_{log x}^I H⟩,
    Q^𝒩 = 𝒜∘𝔇^𝒩 + 2A(𝔇^𝒩·)B(𝔇^𝒩·) − Π^𝒩∘𝔇^𝒩 = Q₀^𝒩 − 𝒦_R^𝒩      (21A Prop. 3.2, valid verbatim for 𝒩).
Constraints: f₀, f_λ are system-free; the A- and B-constraints use the summation map Σ_{s∈S} f(s e^x) with a summation set S,
taken either S = ℤ_{>0} ("constraints from ℤ") or S = 𝒩 or S = another system. The gauge form ℓ_g is system-free.
Systems measured: ℕ; 2 → 2.05, 2.001, 2.0001, 1.9999, 1.999, 1.95 (other primes kept); (2,3) → (2.05, 3.1); 3 → 3.001, 2.999;
ℕ ∪ {2.5}-generated ("extra prime 2.5"); the free system on {2, 3}; √p-system (generators √p, i.e. F-root with m = 2);
ℕ ∪ √2ℕ (generators: primes and √2, with the relation (√2)² = 2, so Λ is solved by the recursion); exponent scaling p ↦ p^{1+ε}.

### 1.2 Tool (NUMERICAL)
tools/multi_cell/gen_system.py R Nb T J dps SYS CON builds 𝔇^𝒩, Π^𝒩 (exact closed form of c^sym at lags log x), the polar
vectors and, if requested, the A/B constraints from the summation set; Arch and the gauge form are taken from the ℕ build
(window_build.py pickles). Check: SYS = nat reproduces the 21A bottoms exactly (R = 3…8: 1.49·10⁻³, 6.50·10⁻⁶, 5.80·10⁻⁹,
2.03·10⁻¹², 9.8·10⁻¹⁷, 7.7·10⁻²⁰). Nb = 40; dps 50/70/70/90/90/110 for R = 3…8; T = 0.8. Bottoms in ‖F‖² units and in
ℓ_g units (gauge rank J = 20/30/30/40/40/40); the ℓ_g ratio of a negative bottom is the most negative generalized eigenvalue.

## 2. Measurements (NUMERICAL, T = 0.8, Nb = 40; constraints from ℤ unless stated)
Galerkin bottoms are outer bounds in the sense of 21A §2.1: a negative Galerkin bottom is a negative value of the true form on
an admissible vector (up to quadrature/rounding at 50–110 digits), so every "negative" entry below is a genuine failure of
positivity of the R-cell form of that system; positive entries are only upper bounds for the true bottom.

### 2.1 Bottom of Q₀^𝒩 − 𝒦_R^𝒩 on V_R: ‖F‖² units / ℓ_g units
| system | R = 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| ℕ | 1.49e-3 / 0.74 | 6.50e-6 / 0.68 | 5.80e-9 / 0.17 | 2.03e-12 / 0.10 | 9.8e-17 / 7.7e-5 | 7.7e-20 / 1.5e-7 |
| 2 → 2.05 | −0.031 / −25 | −0.051 / −1.1e4 | −0.28 / −3.6e6 | −0.43 / −3.9e10 | −0.60 / −1.5e13 | −0.78 / −1.9e16 |
| (2,3) → (2.05,3.1) | (= 2.05) | −0.052 / −1.1e4 | −0.11 / −3.1e6 | −0.29 / −2.6e10 | −0.62 / −1.2e13 | −1.04 / −1.4e16 |
| 2 → 2.001 | 8.5e-4 / 0.54 | −5.8e-4 / −1.7e2 | −2.9e-3 / −4.9e4 | −7.3e-3 / −3.6e8 | | |
| 2 → 2.0001 | 1.42e-3 / 0.73 | −5.1e-5 / −14 | −8.6e-5 / −4.9e3 | | | |
| 2 → 1.9999 | 1.55e-3 / 0.74 | 6.3e-5 / 0.68 | −1.1e-4 / −10 | | | |
| 2 → 1.999 | 2.1e-3 / 0.75 | 5.6e-4 / 0.52 | −1.6e-3 / −1.3e2 | −4.7e-3 / −1.1e6 | | |
| 2 → 1.95 | 3.2e-2 / 0.68 | −0.086 / −45 | −0.27 / −5.6e5 | −0.41 / −4.9e9 | | |
| 3 → 3.001 | (3 ∉ window) | −1.0e-4 / −18 | −1.2e-3 / −9.9e3 | −2.0e-3 / −7.5e7 | | |
| 3 → 2.999 | (3 ∉ window) | 3.1e-5 / 0.46 | −3.0e-4 / −5.7e2 | −2.5e-3 / −3.5e4 | | |
| extra prime 2.5 | −0.20 / −97 | −0.43 / −1.1e5 | −0.77 / −3.6e7 | | | |
| free on {2,3} | (= ℕ) | (= ℕ) | (= ℕ) | −0.50 / −1.0e8 | | |
| √p system (F-root, m = 2) | −0.81 / −5.3e2 | −4.6 / −4.8e5 | | | | |
| ℕ ∪ √2ℕ | −0.12 / −78 | | | | | |
| p ↦ p^{1+t}, t = +1e-3 | | −1.3e-3 / −3.0e2 | −2.3e-3 / −8.9e4 | −3.2e-3 / −7.3e8 | −3.9e-3 / −3.1e11 | |
| t = +1e-4 | | −9.6e-5 / −27 | −2.1e-4 / −8.9e3 | −2.6e-4 / −7.3e7 | −3.8e-4 / −3.1e10 | |
| t = −1e-4 | | **+1.0e-4 / 0.68** | **+5.0e-5 / 0.68** | **+2.9e-5 / 0.66** | **+2.1e-5 / 0.63** | |
| t = −1e-3 | | **+7.8e-4 / 0.70** | **+3.7e-4 / 0.69** | **+2.4e-4 / 0.67** | | |
(Empty cells: not computed within the run budget. The free system on {2,3} agrees with ℕ until 5 enters the window.)

### 2.2 Near-null spectrum and branch slopes (bottom four eigenvalues of Q^𝒩 on V_R, ‖F‖² units)
| R | ℕ | 2 → 2 + 10⁻⁶ | 2 → 2 − 10⁻⁶ | t = +10⁻⁶ | t = −10⁻⁶ |
|---|---|---|---|---|---|
| 4 | 6.5e-6, 2.9e-4, 3.3e-3, 0.11 | 5.93e-6, … | 7.07e-6, … | 5.51e-6, … | 7.50e-6, … |
| 5 | 5.8e-9, 9.5e-8, 2.4e-5, 7.4e-4 | −6.3e-7, 4.7e-9, … | 1.8e-7, 6.2e-7, … | −1.57e-6, −9.2e-7, … | 8.9e-7, 1.75e-6, … |
| 6 | 2.0e-12, 6.9e-10, 2.1e-8, 5.1e-7 | −2.8e-6, −7.4e-7, 6.5e-7, 1.7e-6 | −1.9e-6, −4.6e-7, 7.1e-7, 3.6e-6 | | |
Reading: the number of eigenvalues of Q^ℕ that are ≪ the generic O(1) scale grows with R (1 at R = 4, 2 at R = 5, ≥ 4 at R = 6),
and in a generator direction the near-null branches have slopes of size 0.5–3 and **both signs** (R ≥ 5), so the positive set
in that direction is an interval around ℕ of width ≍ (near-null eigenvalue)/(slope), already < 10⁻⁶ at R = 6. In the
exponent direction p ↦ p^{1+t} all near-null branches have **negative slope** (R = 4, 5; and the bottoms of 2.1 for R ≤ 7), so
the positive set contains a one-sided segment t ∈ [−10⁻³, 0] and ℕ sits at its edge.

### 2.3 Summation set of the transported constraints (task (2))
| R | ℕ with constraints from 𝒩' = (2.05,3.1) | from 𝒩' = ℕ∪{2.5} | from ℤ |
|---|---|---|---|
| 4 | 6.54e-6 / 0.671 | 6.49e-6 / 0.672 | 6.50e-6 / 0.676 |
| 6 | 2.03e-12 / 0.089 | 2.03e-12 / 0.101 | 2.03e-12 / 0.104 |
| 8 | 7.70e-20 / 1.2e-7 | 7.71e-20 / 1.3e-7 | 7.69e-20 / 1.5e-7 |
and, conversely, every perturbed system of 2.1 was run with constraints from ℤ (CON = Z) and from itself (CON = N): the two
bottoms agree to 0.1–3 % in ‖F‖² units in every case (e.g. R = 7, (2.05,3.1): −0.620 vs −0.623; R = 3, √p: −0.81 vs −0.92).
**The sign of the R-cell form is insensitive to the summation set of the A/B constraints**: swapping ℤ for a perturbed set moves
the ℕ-bottom by < 1 % and never changes a sign; swapping a perturbed system's own set for ℤ never restores positivity.

## 3. Dependence on the integer system (task (3))

Standing assumptions: 𝒩 free on generators g_i = e^{η_i} (no multiplicative relations), no element of 𝒩 equals R, F in the
sine span V ⊂ H¹₀(I) (extension by zero lies in H¹(ℝ)). Constraints from ℤ, so V_R and ℓ_g do not depend on 𝒩 (the four
constraint functionals and the gauge form act on F, not on 𝔇F; window_build.py, gen_system.py).

### Lemma 3.1 (Φ_R for any system; PROVED)
For any multiplicatively closed discrete 𝒩 ⊂ [1, ∞) the map α ↦ Φ_R^𝒩(α) = Σ_{x∈𝒩, x<R} α(x)x^{−1/2}τ_{log x}^I is a
homomorphism from (functions on 𝒩, Dirichlet convolution over 𝒩) to operators on L²(I), and [M_x, Φ_R^𝒩(α)] = Φ_R^𝒩(α·log).
*Proof.* 21A §3.1 used only τ_a^Iτ_b^I = τ_{a+b}^I (a, b ≥ 0), τ_a^I = 0 for a ≥ ℓ, and [M_x, τ_a^I] = aτ_a^I; none involves
integrality. ∎ Consequently 21A Prop. 3.2 holds for 𝒩: Φ^𝒩(Λ_𝒩)𝔇^𝒩 = [M_x, 𝔇^𝒩] and Q^𝒩 = Q₀^𝒩 − 𝒦_R^𝒩. (Injectivity, needed
only for the "iff", holds as in 21A.)

### Proposition 3.2 (first variation in a generalized prime; PROVED)
Put E_i = Σ_{j≥1} δ_{g_i^j}, E_i^{(1)} = Σ_{j≥1} j δ_{g_i^j}, G_i = Φ_R^𝒩(E_i), G_i^{(1)} = Φ_R^𝒩(E_i^{(1)}), ∂ = d/dx on H¹₀(I),
P = Φ_R^𝒩(Λ_𝒩) = Σ_i η_i G_i. Then, as operators V → L²(I),
    ∂_{η_i}𝔇 = −G_i 𝔇 (½ + ∂),        ∂_{η_i}P = G_i − η_i G_i^{(1)}(½ + ∂),
and for the exponent direction ∂_t := Σ_i η_i ∂_{η_i} (all x ↦ x^{1+t}, at t = 0)
    ∂_t𝔇 = −[M_x, 𝔇](½ + ∂) = −P𝔇(½ + ∂),        ∂_tP = P − Φ_R^𝒩(Λ_𝒩·log)(½ + ∂).
With Q^𝒩[F] = 𝒜[𝔇F] + 2A(𝔇F)B(𝔇F) − 2⟨𝔇F, P𝔇F⟩, the derivative in any direction δ is
    δQ[F] = 2𝒜(𝔇F, δ𝔇F) + 2A(δ𝔇F)B(𝔇F) + 2A(𝔇F)B(δ𝔇F) − 2⟨δ𝔇F, P𝔇F⟩ − 2⟨𝔇F, P δ𝔇F⟩ − 2⟨𝔇F, (δP)𝔇F⟩,
and every simple eigenvalue branch λ_k of Q^𝒩 on V_R satisfies δλ_k = δQ[u_k] (u_k unit eigenvector).
*Proof.* For F ∈ H¹(ℝ), a ↦ τ_aF is differentiable in L² with derivative −τ_aF′; multiplying by 1_I commutes with d/da.
With log x = Σ_i k_i(x)η_i, ∂_{η_i}(x^{−1/2}τ^I_{log x})F = k_i(x)x^{−1/2}(−½τ^I_{log x}F − τ^I_{log x}F′). Hence
∂_{η_i}𝔇 = −Φ(k_i)(½ + ∂). Freeness gives k_i(x) = #{j ≥ 1 : g_i^j | x in 𝒩} = (E_i ∗ 1_𝒩)(x), so Φ(k_i) = G_i𝔇 by Lemma 3.1.
Λ_𝒩 = Σ_i η_iE_i for a free system (the recursion of §1.1 is solved by it, by uniqueness); G_l depends on η_l only, and
∂_{η}(η Σ_j e^{−jη/2}τ^I_{jη}) = Σ_j e^{−jη/2}τ^I_{jη} − η Σ_j j e^{−jη/2}τ^I_{jη}(½ + ∂). Summing η_i∂_{η_i}: Σ_iη_ik_i = log,
so ∂_t𝔇 = −Φ(log)(½+∂) = −[M_x,𝔇](½+∂) by Lemma 3.1; and Σ_i η_i²E_i^{(1)} = Λ_𝒩·log (at g^j: η·jη). The formula for δQ is
the product rule (𝒜, A, B are system-free). Elements do not cross x = R under small δ, so V_R-matrices are real-analytic in
(η_i); the eigenvalue statement is analytic perturbation theory for symmetric matrices (CITED: Rellich–Kato). ∎

### Proposition 3.3 (the R-cell sign is not a monoid invariant; PROVED + NUMERICAL certificate)
The systems ℕ^{1+t} = {n^{1+t}} are isomorphic to ℕ as ordered monoids, with Λ_{ℕ^{1+t}}(n^{1+t}) = (1+t)Λ(n) (PROVED, trivial).
ℕ is the only member closed under addition (2^{1+t} = 1 + 1 forces t = 0; PROVED). The R-cell form is positive on V_R for
t ∈ [−10⁻³, 0] and negative (genuine negative values, §2 preamble) for t ∈ {10⁻⁶ (R = 5, 6), 10⁻⁴, 10⁻³} (NUMERICAL, R = 4…8,
50–110 digits). Hence the sign of the R-cell form is decided by a parameter — the embedding exponent of the monoid in
(ℝ_{>0}, ·) — that the multiplicative structure leaves free and the additive structure fixes.
Mechanism (NUMERICAL, §2.2): along ∂_t, *every* near-null branch of Q^ℕ has negative slope (R = 4: one branch, slope ≈ −1.0;
R = 5: two, ≈ −1.6, −1.0; R = 6: four, −2.2…−0.4; R = 8: four, ≈ −4.1…−2.2 from t = ±10⁻⁴), so the near-null cluster crosses
zero together at t ≈ λ₀(ℕ)/|slope| ≈ 10⁻²⁰ (R = 8). Along a single generator (∂_{η_1}, ∂_{η_2}) the branches have slopes of
both signs from R = 5 on, so the positive set in those directions is two-sided and of width < 10⁻⁶ at R = 6.
Picture: near ℕ, the set of free systems with nonnegative R-cell form is (to resolution) a thin wedge containing the ray
{ℕ^{1−ε} : 0 < ε ≤ ε₀(R)}, with ℕ at its tip.

### 3.4 Extent of the positive segment on the exponent ray (NUMERICAL)
t_+(R) ≈ λ₀(ℕ)/|∂_tλ₀| ≲ 10⁻⁶ (R = 5, 6), ≲ 10⁻⁴ (R = 8, resolution of the runs), and ≈ λ₀(ℕ) ~ 10⁻²⁰ by first order.
t_−(R) (left end): R = 5: (−0.15, −0.10) [−0.1: +2.4e-4; −0.15: −0.026]; R = 6: (−0.10, −0.03) [−0.03: +1.9e-3];
R = 7: (−0.03, −0.01) [−0.01: +5.1e-4; −0.03: −4.4e-4]; R = 8: (−0.01, −0.001) [−0.001: +7.3e-5; −0.01: −1.2e-4]; R = 4: (−0.3, −0.001) [−0.3: −0.15]. Check: t = −½ is the √p system and reproduces its bottom −4.6083 at R = 4.
So the positive segment [t_−(R), t_+(R)] contains ℕ at its right end (to resolution) and shrinks from the left by a factor
≈ 3–10 per added cell, from the right like λ₀(ℕ). Its left part has margins far above ℕ's (t = −0.01, R = 5: 2.4·10⁻³ versus
5.8·10⁻⁹).

## 4. Answer to task (2): which property of ℕ the R-cell sign uses
(i) Not the transported constraints (Poisson over ℤ in the summation map). §2.3: replacing ℤ by a perturbed summation set
changes the ℕ-bottom by < 1 % with no sign change at R = 4, 6, 8; giving a perturbed 𝔇/Π the ℤ-constraints never restores
positivity (all 2.1 rows, CON = Z vs N agree to 0.1–3 %). (NUMERICAL.)
(ii) Not the multiplicative type alone. Prop. 3.3: monoid-isomorphic systems ℕ^{1+t} (t > 0, any size ≥ 10⁻⁶ tested) are
negative. This is the R-cell counterpart of G1. (PROVED isomorphism + NUMERICAL sign.)
(iii) Not "additive regularity" in the sense of consecutive gaps. The systems ℕ^{1−ε} have no additive structure at all
(no element pair differs by a fixed amount) and are positive at R-cell level with larger margins than ℕ for ε ≤ ε₀(R).
(iv) What is used: the positions log x of the monoid elements in the dilation operator, jointly with their weights
x^{−1/2}; within the monoid's one-parameter family of embeddings (the only freedom the multiplicative structure leaves) the
sign changes exactly at the embedding fixed by +, from the positive side t < 0 to the negative side t > 0, and every
near-null mode crosses with the same sign of slope. Perturbing one generator also preserves every exact relation m = kn of the free monoid (log 6 = log 2′ + log 3 still), but changes the ratios log g_i / log g_j; it produces near-null slopes of both signs and kills positivity on both sides at R ≥ 5. Thus both tested deformations keep the exact product relations; what separates them is whether the log-positions are rescaled uniformly (one-sided, ℕ at the edge) or non-uniformly (two-sided, ℕ isolated). Near-coincidences m ≈ kn between *different* products are moved by both deformations and were not isolated by these tests.
(ARGUED reading of NUMERICAL data.)
(v) Extra or missing primes: the extra prime 2.5 (O(0.2–0.8) negative, ℓ_g −10²…−4·10⁷), the free system on {2, 3}
(−0.50 once 5 is in the window), √p (−0.8, −4.6), ℕ ∪ √2ℕ (−0.12) all fail by O(1) in ‖F‖² units at the first R at which
they differ from ℕ inside the window.

## 5. Falsifier test (rule 4) on the statement "ℕ sits at the tip of the R-cell positive set"
(a) cΛ: Λ_{ℕ^{1+t}} = (1+t)Λ at shifted positions; the c-window at fixed positions is 21A (shrinks like λ₀). FAILS for (a). 
(b) a_P: O(1) negative (21A §2.3; free system on {2,3} here). FAILS.
(c) Beurling: the ray ℕ^{1−ε} (Beurling systems, ζ_𝒩(s) = ζ((1−ε)s)) is POSITIVE at each fixed R for ε ≤ ε₀(R), with
    ε₀(R) ≈ 0.1, 0.05, 0.02, 0.005 (R = 5…8). **The R-cell positivity survives (c) on this ray at every fixed R**; it fails
    only in the limit if ε₀(R) → 0, which the data suggest but do not prove. Generic Beurling perturbations (2 → 2 ± δ,
    3 → 3 ± δ, extra prime) FAIL from R = 5 on. So no fixed-R statement is a sign step (consistent with 19A §5.1), and any
    sign mechanism built on R-cell data must produce the left edge ε₀(R) → 0 — i.e. must see the difference between ℕ and
    ℕ^{1−ε}, which the monoid cannot.
(d) finite modification: a single shifted generator fails at R ≥ 5 on both sides. FAILS.

## 6. Corpus and index notes
New: gen_system.py (R-cell form over any generalized integer system, separate summation set); Lemma 3.1 (Φ_R for any
system); Prop. 3.2 (first variation in a generalized prime and in the exponent, explicit in ℕ data: ∂_t𝔇 = −[M_x,𝔇](½+∂),
∂_tP = P − Φ(Λ log)(½+∂)); Prop. 3.3 (sign not a monoid invariant; ℕ at the tip of a thin wedge along ℕ^{1−ε});
the measurement that the summation set of the constraints is irrelevant to the sign. Closes the ARGUED item 21A §3.4(ii)(c)
(computed: the shrinking mechanism survives (c) at fixed R on the ray ℕ^{1−ε}, not on generic perturbations).

## Result
PIVOT with PROVED pieces. The R-cell sign is located (NUMERICAL, R ≤ 8, T = 0.8) at the additive normalisation of the
multiplicative embedding: among monoid-isomorphic systems ℕ^{1+t} positivity holds exactly for t ∈ [t_−(R), ≈0], ℕ at the
right end, with every near-null mode crossing at t = 0 with negative slope; generic generator perturbations, extra/missing
primes and F-root systems fail by O(10⁻⁴…1); the Poisson-transported constraints play no role. No lower bound follows.

### What was proved
- Lemma 3.1: the truncated Dirichlet homomorphism and [M_x, Φ(α)] = Φ(α log) hold for every multiplicatively closed system.
- Prop. 3.2: exact first-variation formulas of 𝔇, P, Q^𝒩 in each generalized prime and in the exponent, with Hellmann–Feynman
  slopes (CITED perturbation theory).
- Prop. 3.3 (structural part): ℕ^{1+t} ≅ ℕ as ordered monoids with Λ scaled by 1+t; ℕ is the only additively closed member.

### What failed and why
- "Perturbed systems are negative, so the sign is ℕ-specific": false along ℕ^{1−ε} at fixed R (positive, larger margin).
- "The integer spacing used through Poisson in the constraints is responsible": §2.3, no effect on the sign.
- No proof of the sign of ∂_tQ on the near-null cluster; the first-variation formula gives it as an explicit ℕ-quantity,
  δ_tQ[u_k] < 0 for all near-null u_k (NUMERICAL, R = 4…8), unproved.

### Next concrete step
Prove (or refute) the one-sided statement in the exponent variable: for every near-null vector u of Q^ℕ on V_R,
∂_tQ[u] = −2Re⟨stuff⟩ < 0, using ∂_t𝔇 = −[M_x,𝔇](½+∂) — note ∂_t is then a commutator-type derivation built from M_x and ∂,
i.e. a generator of the (x ↦ x, log-scale) dilation group, and the ½ is the weight exponent. Then measure ε₀(R) for R = 9, 10
to decide whether the left edge closes (ε₀ → 0), and isolate near-coincidences by a system that preserves all log-gaps up to
a prescribed size but breaks one relation m = kn.

## Reproducibility
tools/multi_cell/gen_system.py R Nb T J dps SYS CON (needs the window_build.py pickle for (R, T)); SYS ∈ nat | gens:a,b |
add:x | only:a,b | root2 | natsqrt2 | pow:t; CON ∈ Z | N | S:<SYS>; EIGS=1 prints the bottom four eigenvalues. 1–7 min per run
at R ≤ 8, Nb 40, 50–110 digits.
