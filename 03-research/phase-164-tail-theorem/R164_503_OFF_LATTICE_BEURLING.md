# R164_503: The discrete Beurling frontier below θ = 1/3, OFF the Witt lattice (grid cell 5G)

Pure mathematics, no numerics. Inputs: R164_201 (Theorem L, O164.201a), R164_291 (audit, R1–R4), R163_803 (Theorem C),
R163_101 (C_{1/3}, §5 analytic NO-GO), R164_190 (identification audit), 00-references/beurling-dmv (DMV 2006 and Zhang 2007 via secondary
sources only: BDV 2004.11501 §1, zbMATH Zbl 1121.11061; Broucke 2409.10051). Gate 1, Row D and (★_cell) stay **OPEN**.

## Status table

| # | Statement | Label |
|---|---|---|
| 1 | Exact relation: N − ρx = O(x^θ) ⟹ ζ_P(s) − ρs/(s−1) holomorphic and O(\|t\|) in Re s > θ; it gives **no** zero information; zeros may sit anywhere in Re s > θ | PROVED (standard; §1) |
| 2 | **Goal B ⟹ RH.** Any theorem "discrete, θ < θ₀ (θ₀ > 0) ⟹ zeros on Re s ≤ ½" applied to ℕ (θ = 0) proves RH | PROVED (trivial; §2) |
| 3 | Goal B with θ₀ > 131/416 ⟹ GRH for every quadratic character (ideal monoids of quadratic fields have θ ≤ 131/416 < 1/3) | PROVED-CITED (Huxley's lattice-point exponent, cited from memory, flagged; §2) |
| 4 | Hence B is **RH-hard**: it is not a closure route; its "first lemma" must already contain an RH-strength input for ℕ | PROVED (as a logical statement) |
| 5 | Prime-side rounding (DMV, Zhang, idea (i) moving prime positions, idea (ii) greedy on Π) is capped at x^{1/2}·x^{o(1)}: the factor exp G(s), G = s∫(Π−Π₀)u^{−s−1}du, has a stationary-phase term of size \|t\|^{½−σ} that no rounding of Π removes | ARGUED (§3; mechanism of Zhang's exp(c(log x)^{2/3}) loss) |
| 6 | Below ½ the target must be set on the **integer** side (lattice-point structure), not on a continuous prime density; every known discrete system with θ < ½ is a lattice-point count (ℕ, ideal monoids, Theorem C rescales) | ARGUED (survey of the record + §3.4) |
| 7 | Exact integrality in the rescaled class (primes at p^{k+1}, multiplicity p^k) forces a ∈ ℤ, i.e. θ = k/(k+1) ≥ ½ | PROVED (§4.1) |
| 8 | Position-smearing of a non-integer multiplicity (copies at q·u_i) turns the zero of ζ(w) into a branch point (w−ρ)^{U(s)} unless U(s_ρ) ∈ ℤ; this is incompatible with item 1 | PROVED (§4.2) |
| 9 | Goal A (θ < 1/3, discrete, off-line zero) | **OPEN**; no construction found; all four tried mechanisms closed (items 5, 7, 8 and Theorem L) |
| 10 | Decision A vs B | **A kept as the only admissible target; B rejected as a route (RH-hard), not refuted** |

## 1. What an integer error exponent says about ζ_P

ζ_P(s) = s∫_1^∞ N(x)x^{−s−1}dx. If N(x) = ρx + E(x) with E = O(x^θ), then ζ_P(s) = ρs/(s−1) + ρ + s∫E x^{−s−1}dx, and the last
integral converges absolutely for Re s > θ. So ζ_P − ρs/(s−1) is holomorphic there with |ζ_P(σ+it)| ≪_σ |t|. Nothing more follows:
zeros are allowed anywhere in Re s > θ, and Broucke's ζ_θ (extended class) realizes zeros at (1+θ)/2 with this growth. The zeros
govern ψ_P, not N. The only integrality constraint known (Hilberdink 2005, via Révész 2207.00665:186, R163_101 §1 item 5) is
max over the two largest of the exponents of N, ψ, M_G ≥ ½; with θ < ½ it pushes ψ to exponent ≥ ½, which is consistent with
off-line zeros. **PROVED** (standard) / CITED-2.

## 2. Goal B is RH-hard

ℕ is a discrete Beurling system with N(x) = ⌊x⌋, error O(1), θ = 0. A theorem "every discrete system with error O(x^{θ}), θ < θ₀,
has all zeros in Re s ≤ ½" therefore contains RH. For an imaginary/real quadratic field K, the ideal count is a lattice-point
problem in an ellipse / hyperbolic region; Landau gives 1/3 and Huxley-type exponent-pair bounds give 131/416 < 1/3
(**PROVED-CITED, from memory, flagged**). So θ₀ > 131/416 would also give GRH for ζ_K = ζ·L(·,χ_D).

Consequence for the task: the requested test ("must not exclude Theorem C at θ > 1/3, must exclude ζ_θ by discreteness") has a
third, decisive test: **the first lemma must hold for ℕ and then imply RH**. No integrality lemma in the record (Lemma W, Lemma D,
R164_201 §4) or here passes that test; R164_201 §4 already records that its lemma carries no zero information. Goal B is not refuted,
but it is not a route: proving it is at least as hard as RH. **PROVED** (logical).

## 3. Why prime-side rounding stops at ½ (ideas (i), (ii), Zhang)

### 3.1 Set-up
Let Π₀ be a continuous target with ζ₀ = exp(∫u^{−s}dΠ₀ + …) giving N₀ = ρx + O(x^{θ₀}). Any discrete Π (integer jumps, positions
free) gives ζ_P = ζ₀·exp G·(higher-order factor holomorphic in Re s > ½ up to the prime-power corrections), with
G(s) = s∫_1^∞ (Π − Π₀)(u)u^{−s−1}du.

### 3.2 The best rounding is already O(1)
Quantile placement p_j = Π₀^{−1}(j) (or greedy, idea (ii)) gives |Π − Π₀| ≤ 1. So G converges for Re s > 0. Moving positions
(idea (i)) cannot improve on |Π − Π₀| ≤ 1 in sup norm. The loss is not in the size of Π − Π₀ but in its **oscillation**:
Π − Π₀ = −ψ(Π₀(u)) + O(1/u-scale) (sawtooth of the target). **PROVED** (partial summation).

### 3.3 Stationary phase
∫ψ(Π₀(u))u^{−σ−it−1}du: expand ψ in Fourier modes e(kΠ₀(u)); the phase kΠ₀(u) − (t/2π)log u is stationary at u/log u ≈ t/(2πk),
with second derivative ≍ 1/(u log² u)·(…). Each stationary point contributes ≍ u^{−σ−1}(u log u)^{1/2}, so G(σ+it) has a term of
size ≍ |t|^{½−σ} (log factors suppressed). For σ > ½ this is bounded (DMV/Zhang get N error ≈ x^{½+o(1)}); for σ < ½ it grows like a
power of |t| in the exponent, so |ζ_P/ζ₀| reaches exp(c|t|^{½−σ}) on a set of t, and Perron's formula with that growth, optimized
in (σ, T), yields x^{½}exp(c(log x)^{κ}); Zhang's κ = 2/3 is of this shape. The term comes from the Fourier coefficients of the sawtooth
(|ĉ_k| ≍ 1/k, independent of the rounding), so no choice of positions or greedy correction removes it in mean square over t.
**ARGUED** (the mean-square lower bound needs a large-sieve inequality for well-spaced real points of density 1/log u; standard
in shape, not written out).

### 3.4 Consistency check (ℕ)
ℕ has θ = 0 although its primes are a "rounding" of li. This does not contradict 3.3: for ℕ, ζ₀ (from Π₀ = li) is **not** of
polynomial growth below ½, and exp G exactly cancels that. So the decomposition ζ_P = ζ₀·exp G is useless below ½: the
target must be the integer structure itself. This is why every θ < ½ system in the record is a lattice-point count. **ARGUED**.

## 4. Integer-side attempts off the lattice

### 4.1 Exact integrality forces θ ≥ ½
Primes at p^{k+1} with multiplicity p^k (k ∈ ℕ): Π(x) = Σ_{p ≤ x^{1/(k+1)}} p^k ~ x/log x, and ζ_P(s) = ζ((k+1)s − k)·H(s) with H from
the necklace correction (absolutely convergent on the relevant half-plane). Zeros of ζ go to Re s = (k+½)/(k+1) > ½. This is the
Theorem C class with a = k ∈ ℤ, ε_p = 0, θ = k/(k+1) ≥ ½. Removing the rounding defect costs exactly the regime below ½. **PROVED**.

### 4.2 Smearing a non-integer multiplicity in position
Replace the non-integer weight p^a by integer copies at positions q·u_i (q = p^{1/(1−θ)}). Then
log ζ_P = Σ_k (1/k) U(ks) P(kw) with U(s) = Σ_i u_i^{−s}, P(w) = Σ_p p^{−w}, w = (s−θ)/(1−θ). Near a zero ρ of ζ(w),
P(w) = log(w − ρ) + holomorphic, so ζ_P ≈ (w − ρ)^{U(s)}·(holomorphic, non-vanishing). If U(s_ρ) ∉ ℤ this is a branch point in
Re s > θ, forbidden by item 1; if U(s) is to be an integer at every image zero while U(1) ≈ p^a-density, U must be locally constant
in the relevant sense, which returns to integer multiplicity at a single point (4.1) or to rounding (Theorem L). **PROVED** (the
branch-point statement); the "returns to" clause is **ARGUED**.

### 4.3 Remaining unexplored mechanism
Integer-side systems that are not rescales of ℕ: e.g. ideal-like monoids whose Dirichlet series is ζ(w)·L(w) with L carrying the
off-line image of a line, built from a lattice-point problem with exponent < 1/3 **and** a nontrivial power rescale. Every such
attempt in the record is a rescale and hits max(θ, (1−θ)/2) ≥ 1/3 (R164_201 L*). No non-rescaled mechanism is known. **OPEN**.

## 5. Decision

- **Goal B: rejected as a route.** It implies RH (item 2), so it cannot serve as a closing lemma for integrality; no first lemma
  passes the ℕ test.
- **Goal A: OPEN, narrowed.** Prime-side constructions (DMV, Zhang, ideas (i)–(ii)) are capped at ½ (ARGUED); exact integrality on
  the rescaled lattice gives θ ≥ ½ (PROVED); smearing gives branch points (PROVED); rounding on the lattice gives ≥ θ+δ (Theorem L)
  and conjecturally ≥ 1/3 (L*). A counterexample below 1/3 needs a new integer-side lattice-point mechanism.
- Net for integrality (R164_190): the 1/3 frontier is a statement about **constructions**, not a theorem about zeros, and the
  zero-forcing direction is RH-hard. O164.201a ("off-lattice") is sharpened to "off-lattice **and** not prime-side-rounded".

## Ledger

| id | item | status |
|---|---|---|
| O164.503a | Write the mean-square lower bound of §3.3 (large sieve for spaced reals, density 1/log u) | OPEN (ARGUED → PROVED target) |
| O164.503b | Verify the Huxley-type exponent for quadratic ideal counts from a primary source | OPEN (citation check) |
| O164.503c | Find any discrete system with θ < 1/3 not of rescaled-lattice type and not ℕ/ideal monoid | OPEN |
| O164.503d | Close the "returns to" clause of §4.2 | OPEN |

## Grid cell 5G (append to R162_2300 master grid)

5G — discrete Beurling below 1/3, off lattice: B (θ<θ₀ ⇒ RH) **is RH-hard** (ℕ at θ=0; quadratic fields at 131/416); prime-side rounding capped
at ½ (ARGUED, stationary phase |t|^{½−σ}); exact integrality ⇒ θ ≥ ½; smearing ⇒ branch points. A OPEN, no mechanism. No label change.
