# L2_BUILD_018 — Problem (A): an atomic comb positive at EVERY window exists

Problem (A) of N_BUILD_011: can a purely atomic comb (point masses at real positions u_j = log x_j, x_j ≥ 1) with Chebyshev
density κ > κ* lie in Pos (window form ≥ 0 on P_T for all T)? Answer: YES, by a multiscale exact-trapezoid construction.
This is NOT a statement about ζ. No sign contact.

## Corpus check
N_BUILD_011 + its review (Theorem 1: ρ_κ = 2κe^{u/2}du ∈ Pos ⟺ κ ≥ κ*, κ* ≥ |C₀|/4 ≈ 1.343; η_κ := inf g_κ > 0 for κ > κ*,
g_κ := m + κ/(¼+τ²); Corollary 2 continuous Beurling systems in Pos). R167_103 Theorem S, R163_803 BFdisc, R184_005 ℕ∪√2ℕ (atomic
falsifiers, negative). grep "trapezoid / quadrature / coth / lattice comb / multiscale / aliasing": no atomic comb in Pos in the
record. New: Lemma 1 (exact trapezoid error), Theorem A (one window), Theorem B (all windows).

Conventions: comb ν ≥ 0 on [0,∞); 𝔞^ν_T(F) = 𝔞_∞(F) − ∫_{[0,2T)} Re c_F dν; on P_T, ∫_0^{2T}2κe^{u/2}Re c_F du = −κ𝔭(F) (N_BUILD_001 (A)),
Re c_F(u) = (1/2π)∫cos(τu)|F̂|²dτ. Hence for every comb ν and F ∈ P_T ∩ D_T:
  𝔞^ν_T(F) = (1/2π)∫ [g_κ(τ) − Re E^ν_T(τ)] |F̂(τ)|² dτ,  E^ν_T(τ) := ∫_{[0,2T)} e^{iτu}dν − ∫_0^{2T} 2κe^{(½+iτ)u}du.   (★)
So it suffices that Re E^ν_T(τ) ≤ g_κ(τ) − η for all τ (pointwise symbol positivity).

## Lemma 1 (exact trapezoid error; PROVED)
Let a < b, h > 0 with b − a ∈ hℕ, w = ½ + iτ, and τ_h[a,b] := h[½δ_a + Σ_{0<j<(b−a)/h} δ_{a+jh} + ½δ_b]·2κe^{u/2}. Then
  ∫e^{iτu}dτ_h − ∫_a^b 2κe^{wu}du = 2κ(e^{wb} − e^{wa})·[(h/2)coth(hw/2) − 1/w] =: ε_h(τ;a,b).
(i) For all τ: |ε_h| ≤ 2κ(e^{b/2} + e^{a/2})(4 + h²/24).
(ii) For |w| ≤ π/h: |ε_h| ≤ (2/9)κ(e^{b/2} + e^{a/2})h²|w|.
*Proof.* Geometric sum: h Σ_{j=0}^{M−1}e^{w(a+jh)} = h(e^{wb} − e^{wa})/(e^{wh} − 1); adding h(e^{wb} − e^{wa})/2 gives (h/2)coth(hw/2)(e^{wb}−e^{wa}).
(i) |coth(x+iy)|² = (cosh2x + cos2y)/(cosh2x − cos2y) ≤ coth²x; with x = h/4, (h/2)coth(h/4) ≤ (h/2)(4/h + h/12) = 2 + h²/24
(coth x ≤ 1/x + x/3); |1/w| ≤ 2; |e^{wb} − e^{wa}| ≤ e^{b/2} + e^{a/2}. (ii) With z = hw/2, |z| ≤ π/2: (h/2)coth(hw/2) − 1/w =
(z coth z − 1)/w, and Mittag-Leffler z coth z − 1 = Σ_{k≥1}2z²/(z² + π²k²) with |z² + π²k²| ≥ π²k² − π²/4 ≥ ¾π²k² gives
|z coth z − 1| ≤ (8/(3π²))(π²/6)|z|² = (4/9)|z|². So |ε_h| ≤ 2κ(e^{b/2}+e^{a/2})(4/9)(h²|w|²/4)/|w|. ∎

## Theorem A (one window; PROVED)
Fix T > 0, κ > κ*, η := η_κ. Let h ≤ 1 with 2T ∈ hℕ, satisfying (a) (4π/9)κ(e^T + 1)h ≤ η/4 and (b) log(1/(2h)) − 1 ≥ 9κ(e^T+1) + η.
Then ν := τ_h[0,2T] satisfies 𝔞^ν_T(F) ≥ (η/2)‖F‖² on P_T ∩ D_T.
*Proof.* E^ν_T = ε_h(τ;0,2T) (the atom at 2T is invisible: c_F(2T) = 0; the atom at 0 is included in both sides consistently).
For |w| ≤ π/h: |E| ≤ (2/9)κ(e^T+1)h²·(π/h) ≤ η/4 by (a), so g_κ − Re E ≥ ¾η. For |w| > π/h: |τ| ≥ π/h − ½ ≥ π/(2h), and by
lem:mbounds(ii) m(τ) ≥ log(|τ|/2π) − 1/|τ| − 1/(2τ²) ≥ log(1/(4h)) − 1 ≥ 9κ(e^T+1) + η − log 2 by (b). Lemma 1(i) gives
|E| ≤ 2κ(e^T+1)(4 + 1/24) ≤ 8.1κ(e^T+1). So g_κ − Re E ≥ m − |E| ≥ 0.9κ(e^T+1) + η − 0.7 ≥ η since κ > 1.34.
Then (★). ∎ (h is doubly exponentially small: h ≈ exp(−9κe^T).)

## Theorem B (all windows: Pos ∩ atomic ≠ ∅; PROVED)
Let κ > κ*, η = η_κ, T_j := j (j ≥ 0), blocks [2j, 2j+2], dyadic steps h_j = 2^{−n_j} with
 (H1) (4π/9)κ e^{j+1}h_j ≤ η 2^{−j−4},  (H2) log(1/(2h_j)) − 1 ≥ 30κe^{j+1} + η,  (H3) h_{j+1} ≤ h_j.
Define ν := Σ_{j≥0} τ_{h_j}[2j, 2j+2] (at the shared endpoints the two half-atoms add: all atoms positive). Then for every T > 0,
𝔞^ν_T(F) ≥ (η/4)‖F‖² on P_T ∩ D_T.
*Proof.* Fix T, J with 2J ≤ 2T < 2J+2. In [0,2T) the comb is Σ_{j<J}τ_{h_j}[2j,2j+2] + (the atoms of τ_{h_J}[2J,2J+2] in [2J,2T)).
Write the last as τ_{h_J}[2J, b′] + (½-atom correction at b′) where b′ := max(2J + h_Jℕ ∩ [2J, 2T)); the density on [b′, 2T) and the
correction contribute at most 2κe^{T}h_J·2 ≤ η/16 to |E| (H1). So E^ν_T = Σ_{j<J}ε_{h_j}(τ;2j,2j+2) + ε_{h_J}(τ;2J,b′) + O(η/16).
Band decomposition: for τ with |w| ≤ π/h_0, all blocks are in regime (ii): |E| ≤ Σ_j (2/9)κ·2e^{j+1}h_j²·(π/h_j) + η/16 ≤ Σ_j η2^{−j−4} + η/16
≤ η/4, so symbol ≥ ¾η − … ≥ η/2. For π/h_{i−1} < |w| ≤ π/h_i (i ≥ 1): blocks j ≥ i in regime (ii) contribute ≤ η/8; blocks j < i by
Lemma 1(i) contribute ≤ Σ_{j<i}2κ(e^{j+1} + e^{j})(4.05) ≤ 8.1κ(1+e^{−1})Σ_{j<i}e^{j+1} ≤ 8.1·1.37·1.59κe^{i} ≤ 18κe^{i}; and
g_κ(τ) ≥ m(τ) ≥ log(1/(4h_{i−1})) − 1 ≥ 30κe^{i} + η − log 2 by (H2) at j = i−1. So
symbol ≥ 30κe^i + η − 0.7 − 18κe^i − η/8 ≥ η/2 (12κe^i ≥ 0.7). Hence g_κ − Re E ≥ η/4 for all τ, and (★) gives the claim. ∎
Remarks. (1) The comb approximates ρ_κ with weighted discrepancy O(κh_je^{u/2}) at u in block j (one atom's weight) — negligible. (2) Positions: x = e^{u}, u ∈ h_jℤ ∩ [2j,2j+2], all real ≥ 1, ℚ-dependent
(lattice), not integers. (3) Weights 2κh_je^{u/2}: arbitrary positive reals, NOT of Beurling form 2(log x)x^{−½}·(integer multiplicity),
and no prime-power structure. Whether a genuine Beurling generalized-prime measure (positive prime measure Π, prime powers included)
realizes such a comb is OPEN (Möbius inversion ψ ↦ Π may produce negative atoms).

## What ℤ-primes lack relative to it (the arithmetic content, PROVED as comparisons)
(a) Density: ζ's comb has κ = 1 < 1.343 ≤ κ* (N_BUILD_011): its main term alone is not in Pos.
(b) Resolution: Theorem A/B need atom spacing h ≲ exp(−9κe^{T}) at window T, i.e. the first aliasing peak at τ ≈ 2π/h where
m ≥ total comb mass. ℤ's comb at window T has spacing ≈ 2Te^{−2T}·… (consecutive log p), so its "aliasing" (Kronecker-type
coherence) frequencies start near e^{2T}, where m ≈ 2T while the comb mass is A_T ≈ 4e^{T}: quadrature cannot be the mechanism.
(c) Hence for ζ the sign cannot come from (★) pointwise; it must come from P_T-correlation (the negative set U_T of the symbol is
non-empty for ζ, Paper 46 §subsec:band), i.e. exactly the anti-alignment on 𝒩_T identified in 017. The difference between ν of
Theorem B and Λ is: κ > κ* and super-fine lattice positions (pointwise symbol positivity) versus κ = 1 and integer positions
(symbol negative on U_T, positivity only after the P_T-constraint) — this is the arithmetic content of D in this frame.

## Review
- Lemma 1: geometric-sum identity verified; coth modulus bound verified; Mittag-Leffler constant verified (Σ1/k² = π²/6).
- Theorem A's bookkeeping in the high band is sloppy in wording but correct with (b): m(τ) ≥ log(|τ|/2π) − 1/|τ| − 1/(2τ²) and |τ| ≥ π/(2h)
  give m ≥ log(1/(4h)) − 1 ≥ log(1/(2h)) − 1 − log 2; (b) supplies ≥ 9κ(e^T+1) + η, and |E| ≤ 8.1κ(e^T+1); margin 0.9κ(e^T+1) − 0.7 ≥ 0 since
  κ > 1.34. PROVED.
- Theorem B: the band argument needs that in band i the blocks j ≥ i satisfy |w| ≤ π/h_j: true since h_j ≤ h_i (H3). Constants
  checked (Σ_{j<i}e^{j+1} ≤ e^{i}·e/(e−1) = 1.59e^{i}). The truncated last block: correct. PROVED.
- Is pointwise symbol positivity too strong? It is sufficient only; that is fine for existence.
- Scope: this is an existence theorem for an artificial atomic comb; it says nothing about ζ's sign. No negative value for ζ; no sign
  contact. It refutes any proposed barrier of the form "no atomic comb with ψ = κx + o(x) can be in Pos": such a barrier is false.
- Open sub-questions: (Q1) Beurling realizability with positive prime measure; (Q2) same with ℚ-independent positions (generic
  reals) — Kronecker resonances then occur only at τ ≳ exp(cN) where m is huge, so likely YES, not proved; (Q3) minimal resolution:
  is h ≲ exp(−cκe^T) necessary for pointwise positivity of an atomic comb at window T? (Mean-square/large-sieve lower bounds suggest
  the oscillation at the resolution frequency is ≍ (Σν_j²)^{1/2}; not settled here.)
