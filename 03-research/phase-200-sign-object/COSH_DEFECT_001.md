# COSH_DEFECT_001 — The cosh defect as a quadratic form in y: exact identity, indefinite sign, structure of the Euler extremes

Phase 200, round 8. Scripts and outputs: `COSH_DEFECT_001_data/` (`cosh_defect.py`,
`cosh_defect_part2.py`, `*_out.txt`; reuse `LEMMA_E_EPSTEIN_001_data/cert_epstein.py`).

## Summary (≤300 words)

Starting from Lemma E (Z_Q/2 = √(ζ_K L_ψ)·cosh y), the **exact cosh-defect identity** is proved (PROVED):
with y = Σ b_n n^{−s}, Λ_cosh(n) = log n·Σ_{j≥1} κ_j b^{∗2j}(n) (κ₁ = ½, κ₂ = −1/12, κ₃ = 1/45, …; finite sum, j ≤ Ω(n)/2),
and for every g ∈ P_T: 𝔇(g) = −𝒬_g[b] − R₄(g), 𝒬_g[b] = Σ_{m,n} b_m b_n w_g(mn), w_g(N) = log N·N^{−½}c_g(log N): a
**multiplicative Hankel** form in b. For (L₁, L₂) = (ζ_K, L_ψ): b_n ≤ 0, b∗b ≥ 0 coefficient-wise.
**Sign (NO-GO for the uniform version):** 𝒬_g[b] does **not** have a definite sign: (i) as a form in b (g fixed), the Hankel
matrix at the witness has eigenvalues −0.150, −0.048, +0.037, +0.519; (ii) as a form in g (b fixed), its numerical range on P_T
is [−4.02, +4.01] at T = 1.6 and [−1.51, +1.51] at T = 1 (NUMERICAL). The "definite-sign cosh-defect theorem" is false.
**Test (NUMERICAL):** witness T = 8/5: 𝒬_g[b] = +3.4713, R₄ = +0.0078, 𝔇 = −3.4791 (matches Lemma E to 10⁻⁶; order 2
explains 99.8%). The witness almost saturates the minimum of the defect (−3.479 vs −4.03). Mori μ = 15: 𝒬_{g*}[b] = 1.0847·10⁻⁶ =
exact defect (only n = 4 contributes).
**Structure (PROVED):** in the family Z_t = √(L₁L₂)cosh(ty) the form is an **even polynomial in t** of degree ≤ 2⌊Ω_max/2⌋,
with value ½(𝔞^{L₁}+𝔞^{L₂}) at t = 0; in the Euler family L_θ = L₁^{(1−θ)/2}L₂^{(1+θ)/2} it is **affine** in θ. The concavity
in t depends on g: it is not a uniform structure. **Comb–Γ compatibility (PROVED as a criterion, OPEN as a source of sign):**
the Weil distribution W_a = arch_Γ + pole − comb is atomic with positive integer weights for ζ, ζ_K, L_ψ, Z_Q, and is not so for
a_P, ζ^c (c ∉ ℕ), nor for L_θ with θ ∉ {±1}. "Euler ∧ integer divisor" identifies (anchoring), it does not give a sign.

## 0. Index and corpus check

Grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` for "Epstein", "cosh", "Euler", "average", "concav", "convex",
"second order", "Hankel", "Jensen", "integral", "ζ_K", "Hecke":

- **LEMMA_E_EPSTEIN_001** (l.533): starting point; C-E. This memo quantifies its quadratic term: it does not retry it.
- **PROOF_L_SHARP_Q_001** (l.462): "the prime part is NOT Hankel … Do not retry CM tests on log(mn)." Here the Hankel
  object is different (a quadratic form in the coefficients b of y, not the prime part of 𝔔 on the exterior carrier), and
  it does **not** use a CM test as a sign source: the sign is measured and found indefinite. New reason in writing: the kernel is
  w_g(mn) on the support of b ⊂ odd powers of primes of a non-principal class; it is an object that does not exist for ζ (y ≡ 0).
- **BB_001** (l.434): EL identity with coefficient 2(a⋆a)(N)/√N, quadratic in the comb. It is formally parallel (squared
  Dirichlet convolution read at c(log N)), but there a = Λ and the identity is comb-generic; here b is the *log-ratio* of two
  Euler products and the form comes from log cosh, not from Euler–Lagrange. Not a retry; it inherits the lesson "polynomial
  identity in c ⇒ no sign," which §2 confirms.
- **INV_I_001 / I2** (l.395), **BB4**, **BARRIER_001 A3** (l.421): coefficient-by-coefficient integrality NO-GO. §4 uses
  integrality of the **divisor** (zero side of the explicit formula), not of coefficients; it is labeled as identification/anchoring
  (BARRIER_001: π_N S = {Λ}, 𝒞₁) and it is stated why it gives no sign.
- l.34 (Jensen/Laguerre–Pólya): Jensen on zeros, different matter; l.212 "Γ concavity gap (REF-D tautology)" and
  BARRIER_D2_001 (l.423): "segments only give upper bounds (concavity)." §3 falls partly here: affinity in θ and the
  even polynomial in t only compare with the extremes; this is stated.
- **GUO_QUANT_001** (l.529): C-Guo asks for "Euler product entering quadratically": this memo writes that term.
- **META_200_BARRIER_001** (l.528): Λ channel declared here: (Euler) via b = log-ratio, quadratic; falsifier that kills it:
  Lemma E's own witness (and any g with 𝒬_g[b] < 0 in the opposite direction).

Nothing is retried without the new reason written above. No new sign route is proposed; one is closed (§2) and a structure
is written down (§3–4).

## 1. The defect as a quadratic form in y (PROVED)

### 1.1 Exact coefficient identity
Let L₁, L₂ be Euler products with the same gamma factor and conductor, L_i = exp(Σ ℓ_i(n) n^{−s}) for Re s > 1, and
y := ½log(L₂/L₁) = Σ_{n≥2} b_n n^{−s}, b_n = ½(ℓ₂(n) − ℓ₁(n)) ∈ ℝ (supported on prime powers). Z := √(L₁L₂)·cosh y =
½(L₁ + L₂). Then −Z′/Z = ½(−L₁′/L₁ − L₂′/L₂) − (log cosh y)′, and since log cosh z = Σ_{j≥1} κ_j z^{2j} with
κ₁ = ½, κ₂ = −1/12, κ₃ = 1/45, κ₄ = −17/2520 (entire series of radius π/2), and y^{2j} = Σ b^{∗2j}(n) n^{−s} (Dirichlet
convolution), and ∂_s n^{−s} = −log n·n^{−s}:

  **Λ_cosh(n) = log n · Σ_{j≥1} κ_j b^{∗2j}(n),**

a **finite** sum (b^{∗2j}(n) = 0 if 2j > Ω(n), since b₁ = 0). On Re s > σ₀ large the series converges absolutely (|y| < π/2), and
the coefficient identity is formally exact. (It is the same thing as expanding −tanh(y)·y′ = −y y′ + (1/3)y³y′ − …: the
leading term −y y′ = −½(y²)′ has coefficients ½ log n·(b∗b)(n).)

**Verification (`cosh_defect.py`):** for (L₁, L₂) = (ζ_K, L_ψ), exact b (b₂ = −1, b₃ = −2, b₇ = −2, b₈ = −1/3, b₂₃ = −2,
b₂₇ = −2/3, b₃₂ = −1/5, b₄₃ = b₄₇ = −2, …); Λ_Q − ½(Λ_K+Λ_ψ) matches orders 2+4+6 for n < 64 with error 9·10⁻¹⁶.
On the window T = 1.6 (n ≤ 24) order 2 lives on {4, 6, 9, 14, 16, 21, 24}, order 4 on {16, 24} (with Λ_cosh(24) = 0 due to
exact cancellation 2.1187 − 2.1187: 24 = 2³·3 is "2·2·2·3" with opposite signs at orders 2 and 4), order 6: nothing.

### 1.2 The quadratic form
The window form is linear in the comb with a common archimedean part (Lemma E §4.1). For g ∈ P_T, c = c_g,

  𝔇(g) := 𝔞^Q(g) − ½(𝔞^{L₁}(g)+𝔞^{L₂}(g)) = −Σ_n 2Λ_cosh(n) n^{−½} c(log n)
        = −Σ_{j≥1} 2κ_j ⟨b^{∗2j}, w_g⟩,   w_g(N) := log N · N^{−½} c_g(log N)·1_{log N<2T}.

The j = 1 term is **𝒬_g[b] := ⟨b∗b, w_g⟩ = Σ_{m,n} b_m b_n w_g(mn)**, and 𝔇 = −𝒬_g[b] − R₄(g), R₄ := Σ_{j≥2}2κ_j⟨b^{∗2j},w_g⟩.
𝒬_g is a quadratic form in b with kernel **K_g(m,n) = w_g(mn) = log(mn)(mn)^{−½}c_g(log m + log n)**: Hankel in the
additive variable x = log m (depends on x + x′), i.e. *multiplicative* Hankel. (PROVED: it is a reordering of a finite sum.) The
factor (mn)^{−½} is a diagonal congruence (it does not change the inertia); the inertia is decided by φ_g(u) := u·c_g(u) on the set
of sums {log m + log n} in the support of b.

## 2. Does 𝒬_g have a sign? — NO (NO-GO of the uniform theorem)

There are two senses, and both fail.

**(a) In b, with g fixed.** The support of b with mn ≤ 24 is {2, 3, 7, 8}. At the Lemma E witness (T = 8/5):

| | 2 | 3 | 7 | 8 |
|---|---|---|---|---|
| 2 | 0.1341 | 0.2789 | 0.1164 | −0.0960 |
| 3 | 0.2789 | 0.2241 | 0.1145 | 0.0061 |
| 7 | 0.1164 | 0.1145 | 0 | 0 |
| 8 | −0.0960 | 0.0061 | 0 | 0 |

eigenvalues **−0.1495, −0.0481, +0.0367, +0.5191** (NUMERICAL): indefinite. What is true (PROVED) is weaker and
structural: for the Lemma E pair, **b ≤ 0 coefficient-wise** (y = −Σ_{p∈𝒩} e_p Σ_{k odd} p^{−ks}/k), hence
b^{∗2j} ≥ 0 and 𝒬_g[b] = Σ_N (b∗b)(N)·w_g(N) is a **non-negative** combination of the values w_g(N); its sign is that of w_g
averaged over the "class composites" N = mn, m, n ∈ supp b. That is, the sign is not set by the form: it is set by c_g at the
points log N.

**(b) In g, with b fixed.** As a quadratic functional of g ∈ P_T (Legendre, degree < 30, Gauss quadrature, P_T via the kernel of the
two Tate conditions; `cosh_defect_part2.py`), the ratio −𝒬_g[b]/‖g‖² has numerical range

| T | range of −𝒬_g[b]/‖g‖² | range of 𝔇(g)/‖g‖² (exact) |
|---|---|---|
| 1.0 | [−1.507, +1.513] | [−1.507, +1.513] |
| 1.6 | [−4.024, +4.011] | [−4.031, +4.023] |
| 2.0 | [−5.558, +5.158] | [−5.595, +5.308] |

(NUMERICAL). Nearly symmetric: the reason is elementary — c_g(u) for u > 0 changes sign under the modulation g ↦ g·cos(ξt) (with
a codimension-2 Tate correction), and the kernel of 𝒬 only sees u > 0 (u = log N ≥ log 4). Proof of the indefiniteness
(PROVED, sketch): take g_ξ = projection onto P_T of φ(t)cos(ξt), φ a bump; c_{g_ξ}(u) = ½c_φ(u)cos(ξu) + O(1/ξ) uniformly;
choosing ξ with cos(ξ log 4) = ±1 and φ with support < ½log(6/4) to isolate N = 4, the sign of 𝒬 is ± that of c_φ(log 4)·(b∗b)(4) > 0.
Both signs are attained.

**Conclusion §2 (NO-GO, PROVED):** *There is no theorem "𝔞^Q = ½(𝔞^{L₁}+𝔞^{L₂}) − 𝒬_g[b] − O(y⁴) with 𝒬_g[b] of definite sign."*
The identity does hold (PROVED, §1); the sign is g-dependent in both senses. In particular there is **no** uniform
inequality "𝔞^{cosh} ≤ Euler average" on P_T: for half the spectrum the average in Z *raises* the form.

Positive reading of the data: the Lemma E witness gives 𝔇 = −3.479 against a minimum of −4.031: **the vector that falsifies Epstein is
(within 14%) the bottom eigenvector of the cosh defect.** Lemma E's certificate is, in essence, "choose g that aligns c_g
positively at log 6, log 9, log 14, log 21" — the class composites.

## 3. Structure: the cosh family, the Euler family, and what is an extreme

### 3.1 Two families (PROVED)
With L₁, L₂ and b as in §1:

- **Euler family** L_θ := L₁^{(1−θ)/2}L₂^{(1+θ)/2} = √(L₁L₂)e^{θy}, θ ∈ [−1,1]. It is a formal Euler product (local
  factors raised to real exponents), Λ_θ = ½(Λ₁+Λ₂) + θ·½(Λ₂−Λ₁). **The form is affine in θ:**
  𝔞^{(θ)}(g) = ½(𝔞^{L₁}+𝔞^{L₂})(g) + (θ/2)(𝔞^{L₂}−𝔞^{L₁})(g).
- **Cosh family** Z_t := √(L₁L₂)cosh(ty), t ∈ ℝ. Z_1 = ½(L₁+L₂), Z_0 = L_0 = √(L₁L₂). Λ_{(t)} = ½(Λ₁+Λ₂) + Σ_j t^{2j}Λ^{(2j)},
  Λ^{(2j)}(n) = κ_j log n·b^{∗2j}(n). **The form is an even polynomial in t**, of degree ≤ 2⌊Ω_max(T)/2⌋, Ω_max(T) = max Ω(n)
  over n < e^{2T}:

  **𝔞^{Z_t}(g) = 𝔞^{L_0}(g) − t²𝒬_g[b] − Σ_{j≥2} t^{2j}·2κ_j⟨b^{∗2j}, w_g⟩.**

  At T = 1.6 (n ≤ 24, Ω ≤ 4), exactly 𝔞^{Z_t}(g_E) = 3.4172 − 3.4713t² − 0.0078t⁴.

Relation between the two (PROVED, elementary Jensen on the mixing variable): Z_t = ½(L_{−t}+L_t) — **the average is taken in Z,
not in log Z** —, and since log is concave, log Z_t − ½(log L_{−t} + log L_t) = log cosh(ty) ≥ 0 pointwise for large real s.
But the window form sees −(log cosh)′ read at c_g(log n), and there the pointwise positivity of log cosh is lost (§2b).

### 3.2 Structure theorem (with labels)

**Theorem S (structure of the cosh defect).** Let L₁ ≠ L₂ be Euler products with the same gamma factor, conductor and poles,
b = ½(ℓ₂ − ℓ₁). For g ∈ P_T:
(i) (PROVED) 𝔞^{½(L₁+L₂)}(g) = ½(𝔞^{L₁}+𝔞^{L₂})(g) − 𝒬_g[b] − R₄(g), with 𝒬_g multiplicative Hankel (§1.2) and R₄ = O(t⁴) in the
family, exact polynomially.
(ii) (PROVED) In the Euler family the form is affine in θ; the Euler products L₁, L₂ are the **extremes** of the segment, and
the midpoint L_0 = √(L₁L₂) has form ½(𝔞^{L₁}+𝔞^{L₂}).
(iii) (PROVED) The jump L_0 ↦ Z_1 (from the geometric to the arithmetic mean) is the sole source of difference between Z_1 and the Euler
average, and it is even and of order ≥ 2 in b.
(iv) (NO-GO, §2) The sign of 𝒬_g[b] is not uniform in g; the concavity of t ↦ 𝔞^{Z_t}(g) at t = 0 holds exactly on the
half-space {g : 𝒬_g[b] ≥ 0} (which contains the Lemma E witness and excludes a direction of equal size).
(v) (honest) None of (i)–(iv) gives a sign for ζ. For ζ, L₁ = L₂ = ζ, b ≡ 0: all families are constant and the theorem
says 𝔞^ζ = 𝔞^ζ. Using it "in reverse" (ζ positive because it is the extreme of a concave family) requires the sign at the
extremes, which is exactly what is being sought: **REF-D**. Moreover the concavity is not uniform (iv), so there is not even a
concave family in which ζ is the boundary.

What the structure does give: **"the window form is affine in the Euler direction (θ) and an even polynomial, of
g-dependent curvature sign, in the cosh direction (t); Euler products with an integer divisor are the extremes θ = ±1 of the
Euler segment."** The requested version "concave in the cosh direction" is NO-GO as a uniform statement; it is PROVED as a
statement on the half-space {𝒬_g ≥ 0}, which is where Epstein-type falsifiers live.

### 3.3 Why Epstein falls and the extremes do not (data, NUMERICAL + PROVED)
At g_E: 𝔞^{L_θ}(g_E) = 3.4172 − 1.6320θ (L₁ = ζ_K, L₂ = L_ψ) ∈ [1.785, 5.049] > 0 on the whole Euler segment (affine, positive
extremes; PROVED given Lemma E §4.1, which certifies the extremes on intervals). 𝔞^{Z_t}(g_E) = 3.4172 − 3.4713t² − 0.0078t⁴
crosses 0 at t ≈ 0.991 < 1. That is: **the whole Euler segment is positive at g_E, and the arithmetic mixture Z_1 is not**; the
failure lies entirely in the quadratic term, and Epstein is "just past" the crossing (t* = 0.991).

## 4. What ζ has and what the Euler falsifiers (a_P, ζ^c) do not

### 4.1 The comb–Γ compatibility identity
For a comb a = (a_n) and a gamma factor Γ_* with conductor q and declared poles, define the **Weil distribution**
W_a := (polar term) + (archimedean of Γ_*, q) − (comb a), as a functional on tests h = g∗g̃ (this is exactly the complete window
form, before restricting to P_T: 𝔞(g) = W_a(g∗g̃)). The explicit formula (CITED, Weil 1952) states: if
D(s) = Σ a-generated continues to a function with a functional equation of factor Γ_*, conductor q, order 1, then

  **W_a(h) = Σ_ρ m_ρ ĥ(γ_ρ)**, m_ρ ∈ ℤ_{>0}, ρ = ½ + iγ_ρ the zeros (with multiplicity) of the completed function.

**Compatibility criterion (C-int).** *W_a is an atomic measure with positive integer weights* (over ℂ, via analytic ĥ).
This is the "nonnegative integer count" of the objective: with a Fejér/flat-top test, W_a(h) is a smoothed N(T).

**Proposition 4.1 (PROVED, given the CITED facts).**
(a) ζ, ζ_K, L_ψ, Z_Q satisfy C-int (they are entire functions of order 1 after completion, functional equation CITED).
(b) a_P with Γ_ℝ(s), conductor 1: W_{a_P} = arch + pole − (finite trigonometric sum): its archimedean part has density
(1/2π)m(τ) ~ (1/2π)log τ, absolutely continuous, and the comb part is a finite sum of cosines (almost periodic, not atomic)
⇒ W_{a_P} is not atomic ⇒ C-int fails.
(c) ζ^c (comb cΛ, Γ_ℝ, pole): W_{cΛ} = c·W_Λ + (1−c)(arch + pole) = c·Σ_ρ δ_{γ_ρ} + (1−c)·(a.c. density) ⇒ C-int fails if
c ≠ 1 (weights c ∉ ℤ and nonzero continuous part).
(d) In the Euler family L_θ, W_{Λ_θ} = ½(1−θ)W_{Λ₁} + ½(1+θ)W_{Λ₂} (common archimedean part) = a combination of two entire
atomic measures with weights (1∓θ)/2; if L₁ and L₂ have some zero in common with neither (for ζ_K, L_ψ: NUMERICAL, first
zeros distinct), C-int holds **only at θ = ±1**. Thus C-int isolates the Euler extremes of the segment.
(e) In the cosh family, Z_t for t ∉ {0, ±1}: Z_t = ½(L_{−t} + L_t) is not entire (L_{±t} have branch points at the zeros
of L₁, L₂ with non-integer exponents); C-int fails (ARGUED: it requires the sum to not cancel the branchings, generic).
Z_1 = Z_Q does satisfy C-int.

### 4.2 Is "C-int ∧ Euler" the sign object?
Table:

| object | Euler | C-int | 𝔞 ≥ 0 on P_T (large T) |
|---|---|---|---|
| ζ | yes | yes | objective |
| ζ_K, L_ψ | yes | yes | 𝔞^K, 𝔞^ψ > 0 at g_E (not proved in general) |
| a_P, ζ^c | yes (formal) | **no** | no (phase-198 certificates) |
| L_θ, θ ∉ {±1} | yes (formal) | **no** | — |
| Z_Q (Epstein) | **no** | yes | no (Lemma E) |
| DH mod 5 | no | yes | no (CITED: Davenport–Heilbronn, zeros off the line) |

The conjunction separates every falsifier in the battery (PROVED as a table, given the CITED facts). But (honestly):

1. **It is identification, not a mechanism.** Euler + C-int + Γ_ℝ + conductor 1 + simple pole at 1 is (up to axiom details)
   the Selberg class of degree 1 and conductor 1, whose only element is ζ (CITED: Kaczorowski–Perelli, degree-1 classification).
   It is an anchoring premise (BARRIER_001: π_N S = {Λ}; INV_I 𝒞₁): "the class that contains only ζ." Deciding the sign on it is
   the original problem. REF-D if presented as a sign step.
2. **C-int is on the zero side.** Entire atomic W_a is a statement about the divisor of the completed function (BARRIER_001 A7). Its
   positivity (weights m_ρ > 0) is free and says nothing about where the γ_ρ are; Epstein's integer weights are positive and the
   form is negative. The nonnegative integer count does not force 𝔞 ≥ 0 (Epstein, DH: PROVED/CITED).
3. **"Integer count + cosh concavity"** as an object: cosh concavity is g-dependent (§2), and on the half-space where it holds it
   *sinks* the form (Z_Q < average). So "cosh concavity" is a property of the **falsifier**, not of the object: what one would need for
   ζ is the absence of that direction (b ≡ 0), which is trivial for ζ and carries no sign. NO-GO for the composite candidate as
   stated (PROVED by §2 + Lemma E).

What remains of value (ARGUED, design): C-int and Euler are **orthogonal** in the sense that each falsifier violates
exactly one; the family (θ, t) is a two-parameter plane where Euler ⟺ t = 0 (the θ line) and C-int ⟺ {θ = ±1} ∪ {(t,θ) = (1,0)}
(plus the integer-order cosh points). ζ (b = 0) is the collapse of the whole plane to a point. A sign object that "sees" the
Euler ∩ C-int intersection in a non-anchoring way would have to distinguish θ = ±1 from θ = ±1 − ε **by a property of the
window form**, not of the divisor: by affinity in θ, any linear functional of the form is continuous in θ, so **no
linear inequality in 𝔞 separates the Euler extremes from their neighborhood** (PROVED, trivial; consistent with BARRIER_D2_001 Thm 2).
New constraint C-θ below.

## 5. Tests (NUMERICAL)

### 5.1 Lemma E witness (T = 8/5, certified vector of degree 48; `cosh_defect_out.txt`)
c_g(log n)/c_g(0): 4: +0.1935, 6: +0.3812, 9: +0.3060, 14: +0.1650, 16: −0.1385, 21: +0.1723, 24: +0.0095.

| piece | value |
|---|---|
| 𝒬_g[b] (order 2) | **+3.47130** |
| contributions to −𝒬: n = 4, 6, 9, 14, 16, 21, 24 | −0.1341, −1.1154, −0.8965, −0.4654, +0.0640, −0.9157, −0.0082 |
| R₄ (orders ≥ 4; only n = 16, 24) | **+0.00780** (−0.0160 at 16, +0.0082 at 24, entering with a − sign) |
| order 6 | 0 (no n ≤ 24 with Ω_𝒩 ≥ 6) |
| 𝔇 = −𝒬 − R₄ | **−3.47910** (Lemma E, intervals: −3.47910 ✓) |
| b^T H b (Hankel, §2a) | 3.47130 = 𝒬 ✓ |

Order 2 explains 99.78% of the defect. The four "class composites" 6 = 2·3, 9 = 3·3, 14 = 2·7, 21 = 3·7 give 97% of 𝒬;
16 (= 2·8, the only one with c_g < 0) is the only one in favor. 𝔇 = −3.479 against the infimum −4.031 of the defect on P_T.

### 5.2 Mori extremal μ = 15 (g*, ‖g*‖ = 1, 2T = log 15; `cosh_defect_part2_out.txt`)
Contacts of the support of b∗b with n < 15: 4, 6, 9, 14. −𝒬_{g*}[b] = **−1.0847·10⁻⁶** (n = 4: −1.085·10⁻⁶; n = 6: −7.7·10⁻¹²;
9, 14: ~10⁻¹⁶, noise). Exact defect = the same (R₄ = 0: no n < 15 has order 4 in 𝒩). Matches the
"Epstein − ½(K+ψ) = −1.08·10⁻⁶" of Lemma E §3 ✓. Reading: g* is a bump of width ≈ 0.21 with c_{g*}(log 4) ≈ 10⁻⁶ —
it does not see the class composites; the cosh defect is irrelevant at the extremal of ζ, as was already known.

## 6. Labels

- **PROVED:** exact identity Λ_cosh(n) = log n·Σ κ_j b^{∗2j}(n) (finite); 𝔇 = −𝒬_g[b] − R₄ with 𝒬_g multiplicative Hankel
  w_g(mn); b ≤ 0 and b^{∗2j} ≥ 0 for (ζ_K, L_ψ); even polynomiality in t of the cosh family and affinity in θ of the
  Euler family; Theorem S (i)–(iii); indefiniteness of 𝒬_g in g (modulation scheme, §2b); Prop 4.1(a)–(d) given the CITED facts;
  "no linear inequality in the form separates θ = ±1 from its neighborhood."
- **NO-GO (PROVED):** "definite-sign cosh defect" (both senses); "uniform cosh concavity"; "integer count ≥ 0 +
  cosh concavity" as a sign object.
- **CITED:** explicit formula (Weil 1952); functional equation of Epstein/Hecke; Z_Q = ζ_K + L_ψ; degree-1 classification of the Selberg
  class (Kaczorowski–Perelli); existence of zeros of Z_Q and of DH off the line (Davenport–Heilbronn 1936).
- **NUMERICAL:** eigenvalues of the Hankel matrix at g_E; ranges [−4.02, 4.01] etc.; 𝒬 = 3.4713, R₄ = 0.0078; t* ≈ 0.991; Mori
  −1.0847·10⁻⁶; distinct zeros of ζ_K, L_ψ (for 4.1(d)).
- **ARGUED:** 4.1(e) (non-entirety of Z_t, t ∉ {0,±1}); design reading "Euler and C-int orthogonal."
- **OPEN:** L′♯; positivity of 𝔞^K, 𝔞^ψ in general; row D.

## 7. New constraint

**C-θ (HARD).** *Every proof of L′♯ that uses the Euler product must do so via a property that is **not** continuous in the
local exponent*: the window form is affine in θ along L_θ = L₁^{(1−θ)/2}L₂^{(1+θ)/2} (formal Euler products with
real exponents), so any linear or convex inequality in the form that holds at θ = ±1 holds along the whole segment,
where C-int fails. The property separating ζ from a_P/ζ^c is the **integrality of the divisor** (C-int), which is on the zero
side; from Epstein it is Euler, which enters the form only via the even term −𝒬_g[b] − R₄ of g-dependent sign.
Operative corollary: a sign object must be **nonlinear in θ** (detect integer exponents) **and** feel 𝒬_g[b] at the
class composites (C-E), or else be coupled to the minimizer g (not uniform in g, by §2b).

## 8. Index entry

- **COSH_DEFECT_001 (phase 200, round 8):** exact identity PROVED Λ_cosh(n) = log n·Σ_j κ_j b^{∗2j}(n) (κ = ½, −1/12, 1/45, …;
  b = coefficients of y = ½log(L₂/L₁)); defect 𝔇 = −𝒬_g[b] − R₄ with 𝒬_g[b] = Σ b_m b_n w_g(mn) multiplicative Hankel,
  w_g(N) = log N·N^{−½}c_g(log N). **NO-GO PROVED: 𝒬_g has no sign** in b (eigenvalues ±) nor in g (range [−4.02, 4.01] at T = 1.6,
  NUM). Witness E: 𝒬 = 3.4713, R₄ = 0.0078 (order 2 = 99.8%); g_E ≈ bottom eigenvector of the defect; Mori: −1.08·10⁻⁶.
  Structure PROVED: form affine in θ (Euler family L_θ), even polynomial in t (cosh family). "Integer count (C-int) ∧ Euler"
  separates the whole battery but is anchoring (degree 1, Kaczorowski–Perelli) and on the zero side; "integer count + cosh concavity"
  NO-GO. Constraint C-θ. Do not retry: definite sign of the cosh defect, concavity in the mixture, linear separation of the Euler
  extremes.

## 9. Next exact lemma

**Lemma N_θ (nonlinearity in the exponent, OPEN).** *Find a functional Φ_T of the window form restricted to P_T
(nonlinear: e.g. the infimum λ_A, or a Gram/cofactor determinant of the matrix of the form in a fixed basis of P_T) such that
θ ↦ Φ_T(𝔞^{L_θ}) distinguishes θ ∈ {±1} from θ ∈ (−1,1) for the pair (ζ_K, L_ψ), with a mechanism that does not use zeros.*
First concrete, decidable step: λ_A^{(θ)}(T) := inf_{P_T} 𝔞^{L_θ}/‖·‖² is **concave** in θ (infimum of affine functions; PROVED), hence
on the segment it is ≥ min(λ_A^{(−1)}, λ_A^{(1)}) — the concavity of the infimum **favors** the extremes only if the minimum is at
the extremes. Compute (Galerkin, NUMERICAL; then intervals) λ_A^{(θ)}(1.6) and λ_A^{(θ)}(1.9) at θ ∈ {−1, −½, 0, ½, 1} and the
analogue for the cosh family λ_A^{Z_t}; report whether the **crossing to negative** of the cosh family (t* ≈ 0.99 at g_E) is stable in the
infimum and whether there exists t₀ < 1 with λ_A^{Z_t} ≥ 0 ∀t ≤ t₀ at T = 1.6 (defect threshold, "positivity width" in the
cosh direction). That t₀(T) is the exact quantity that a C-E-type sign object must control.
