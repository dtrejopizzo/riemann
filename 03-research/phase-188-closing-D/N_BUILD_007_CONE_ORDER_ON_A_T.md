# N_BUILD_007 — The order on 𝔄_T induced by the primitive autocorrelation cone; the resolvent map is order-indefinite

Pen and paper. 𝒦_T^c := {Re c_F|_{[0,2T)} : F ∈ P_T} (autocorrelation cone; thm:nyq-cone: Fourier side = f ≥ 0 of type 2T
with double zeros at ±i/2, Akhiezer/Blaschke). Dual cone in 𝔄_T: 𝒦_T^* := {ν : ⟨ν, c⟩ ≥ 0 ∀c ∈ 𝒦_T^c}; order ν ≼ ν′ iff
ν′ − ν ∈ 𝒦_T^*. Window positivity WP_T is exactly: μ_T^{form} ∈ 𝒦_T^* (thm:Z / R186_052 Thm 3.4, mesh form).

## 0. Correction to N_BUILD_005 §4 / 006 addendum (PROVED)
Z = Σ_{n<N} n^{−½}δ_{log n} has δ₀-coefficient 1. To make B atom-free at 0, put the whole unit into M:
M := δ₀ + e^{u/2}du|_{(0,2T)}, Laplace transform (z+½)/(z−½), hence **M^{−1} = δ₀ − e^{−u/2}du** (not 2δ₀ − 2e^{−u/2}).
B := Z − M = Σ_{2≤n<N} n^{−½}δ_{log n} − e^{u/2}du has no atom at 0, so M^{−1}*B is quasi-nilpotent in 𝔄_T (atoms at
≥ log 2 are nilpotent; the absolutely continuous Volterra part has spectral radius 0) and
Z^{−1} = Σ_{j≥0}(−M^{−1}*B)^{*j} * M^{−1} converges in total variation with NO weight. Theorem 1 of 006 holds with B
in place of the old one up to the term ½f(0) (bounded). The 006 addendum's conclusion stands in corrected form: the series
converges, but ‖Z^{−1}‖_{TV} = Σ_{d<N}|μ(d)|d^{−½} ≍ e^{T}: absolute norms lose e^{T}; a cancellation-sensitive order is needed.
That is what this memo tests.

## Corpus check
grep "dual cone|cono dual|Kreĭn|Akhiezer|Blaschke|Hardy gauge|order|monotone|preserv|Volterra" in phases 161, 170, 186,
188, Paper 47 §15, grid. Found: R186_052 Thm 3.3–3.5 (𝒦_T^{(0)*} = sinc-smoothings of positive measures, Kreĭn; conditional
modulo (−1)^k, R186_118 MAJOR-1), Paper 47 rem:nyq-dual (dual-cone description "neither proved nor used"); R161_015
(canonical Hardy gauge, norm slope); phase-170 W12 (EM port identities). Nobody tested whether convolution in the causal
algebra preserves 𝒦_T^*. New: §1–§3.

## 1. Elementary members of 𝒦_T^* (PROVED)
(i) δ₀ ∈ 𝒦_T^*. (ii) δ₀ ± δ_a ∈ 𝒦_T^* for 0 < a < 2T (|Re c(a)| ≤ c(0)). (iii) e^{−u/2}du ∈ 𝒦_T^*: ∫₀^{2T}e^{−u/2}Re c_F =
½·(1/2π)∫|F̂|²/(¼+τ²) ≥ 0 (positive-definite kernel e^{−|u|/2}). (iv) δ_a ∉ ±𝒦_T^* for 0 < a < 2T.
*Proof of (iv).* Take φ ∈ C_c^∞ of support length < min(a, 2T−a)/4 with φ̂(±i/2) = 0 (two linear conditions), and
F_± := φ ± τ_aφ placed inside I_T. F_± ∈ P_T, Re c_{F_±}(a) = ±‖φ‖² (cross term only). ∎

## 2. Convolution operators preserving 𝒦_T^* (PROVED)
If ν ↦ ρ*ν maps 𝒦_T^* into itself then ρ ∈ 𝒦_T^* (apply to δ₀) and ρ ± τ_aρ ∈ 𝒦_T^* for all a (apply to δ₀ ± δ_a).
By §1(iv), ρ = δ_a (a > 0) fails. Positive multiples of δ₀ preserve. Whether any ρ with nontrivial part preserves is not
settled in general.

## 3. The resolvent map is order-indefinite (NO-GO, PROVED)
ρ := M^{−1}*B = B − e^{−u/2}*B. On (0, log 2), B = −e^{u/2}du and e^{−u/2}*B = −(e^{u/2} − e^{−u/2})du, so
**ρ = −e^{−u/2}du on (0, log 2)**; ρ has the atom +2^{−½} at log 2 (from B; the e^{−u/2}*B part is absolutely continuous).
(a) ρ ∉ 𝒦_T^*: take F ∈ P_T of support length 2ε < ½log 2 with F̂(0) ≠ 0. Then c_F lives in [0, 2ε) and
⟨ρ, c_F⟩ = −∫₀^{2ε}e^{−u/2}Re c_F = −½(1/2π)∫|F̂|²/(¼+τ²) < 0.
(b) −ρ ∉ 𝒦_T^*: F = φ + τ_{log 2}φ, φ of width ε with φ̂(±i/2) = 0, ‖φ‖ = 1. ⟨−ρ, c_F⟩ = (local part on [0,2ε): positive,
O(ε)) − 2^{−½}·1 + (density of ρ on (log2 − 2ε, log2 + 2ε): O(ε)) < 0 for ε small.
Hence neither ν ↦ ρ*ν nor ν ↦ −ρ*ν preserves 𝒦_T^* (§2), and the iteration Z^{−1} = M^{−1} − ρ*Z^{−1} is not
monotone for the cone order. **NO-GO: no sign for (Ω_μ) by monotone iteration in the 𝒦_T^*-order.** The obstruction is
local and arithmetic: the first atom (n = 2) of the integer comb against the continuous density.

## 4. Compatibility with Odlyzko–te Riele (ARGUED)
A monotone (cone-preserving) iteration would yield, at each T, one-sided bounds on Möbius sums correlated with every
c ∈ 𝒦_T^c, including near-δ tests (short F), i.e. essentially pointwise one-sided bounds on smoothed M(x)/√x at
resolution 1. Pointwise exponent-½ bounds of Mertens type with fixed constant are false (Odlyzko–te Riele, CITED; and
M(x)/√x is unbounded on both sides, CITED as classical consequence). §3 is consistent with this: the cone order is
destroyed already by the first atom. Any (Ω_μ)-type statement must be correlated with the archimedean form (as in (N^♯)),
never a free-standing Möbius bound.

## Self-review
1. §0: Laplace computation: M̂(z) = 1 + ∫e^{u/2}e^{−zu}du = 1 + 1/(z−½) on the half-line; truncation is a quotient,
so M^{−1} in 𝔄_T is the truncation of the half-line inverse — correct. Quasi-nilpotence: correct (Volterra L¹ kernel +
atoms ≥ log2). The 006 addendum's "M^{−1} = 2δ₀ − 2e^{−u/2}" was wrong because of the ½δ₀ convention; corrected here, and
its NO-GO is restated (absolute norms lose e^{T}).
2. §1(iv): F_± need P_T: F̂_±(±i/2) = φ̂(±i/2)(1 ± e^{∓a/2}·…) = 0 since φ̂(±i/2) = 0. Correct.
3. §3(a): needs F ∈ P_T short with F̂(0) ≠ 0: three conditions (two vanish, one not) on a finite-dim space of bumps — fine.
(b): F ∈ P_T as in §1(iv). Signs checked: ρ's atom at log 2 is +2^{−½} so −ρ's is −2^{−½}, and Re c_F(log 2) = +1. Correct.
4. §4 is a reading, labelled ARGUED.
No sign contact; no negative value of 𝔞_T.

## Next construction
The cone order is the wrong order. Replace it by the order induced by the FULL window form: ν ≼_T ν′ iff
⟨ν′ − ν, c_F⟩ ≥ −θ·𝔞^♯(F) for a fixed θ ∈ (0,1) (archimedean-relative order, N_BUILD_002). Test whether ρ = M^{−1}*B is a
θ-contraction for this relative order on short and two-bump tests (the two failures of §3 are both paid by m^♯ ~ log(1/ε)
at width ε: the local term in (a) is O(1) against 𝔞^♯(F) ≍ log(1/ε)). This is a quantitative, pen-and-paper test.
