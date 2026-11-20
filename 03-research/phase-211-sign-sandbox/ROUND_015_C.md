# Round 015 C — The T = 1.5 violation of λ_max(A_τ) ≤ m(τ): real for the operator, an artefact for the form

Notation of ROUND_012_A §3 and ROUND_013_B: N = e^{2T}, v_n = 2Λ(n)/√n, m(τ) = Re ψ(¼+iτ/2) − log π,
A_τ f(x) = ½Σ_{n<N} v_n cos(τ log n)[f(x+log n) + f(x−log n)] on L²[−T,T] (f extended by 0). Everything below is
NUMERICAL unless labelled otherwise. Tools: tools/A_tau_lmax.py (unchanged), tools/eig_packet_direct.py (new: direct
W_T on the top eigenvector, projected to P_T, same quadrature as tools/packet_direct.py), tools/galerkin_mp.py.

## 0. Corpus check

Index rows read: P211-13B (the reported −0.504), P211-12A (Proposition 3.1), P211-11C (direct W_T on packets),
REVIEW_009 (Proposition 1.2 of 011A is a necessity statement up to o(1)). This memo is a verification of P211-13B,
not a new route.

## 1. Is −0.504 at T = 1.5 real for the operator? Yes.

**Comb.** comb(1.5) = {2,3,4,5,7,8,9,11,13,16,17,19}: 16 included, 20 is not a prime power, 19 < e³ ≈ 20.09 is the
last term. Consistent.

**Convergence in Nb** (fine scan τ ∈ [138,143], step 0.02): minimiser τ = 140.44 for every Nb,
λ_max = 3.6105 / 3.6146 / 3.6166 / 3.6180 and margin = −0.5036 / −0.5077 / −0.5097 / −0.5111 at Nb = 400/600/800/1000.
Rayleigh–Ritz monotone from below: the true margin is ≤ −0.511.

**Fine τ-scan** τ ∈ [138,146], step 0.02, Nb = 400: minimum −0.5036 at 140.44; the margin is negative on ≈ 10% of the
points (max +1.67). Not a wrong local minimum.

**T-scan 1.40–1.60, step 0.01** (Nb = 300, τ ∈ [Ω_lo, Ω_lo+20], step 0.05): the full margin is negative at every T
(−0.11 at 1.40, −0.50 at 1.50, −0.29 at 1.51 after the minimiser jumps to the next cell, −0.60 at 1.60). No jump at a
contact threshold; T = 1.5 is not isolated.

**The positive values at T = 2.0–3.0 in ROUND_013_B were basis-truncation artefacts.** With Nb = 400 the sine basis
on [−2,2] resolves frequencies only up to 400π/4 ≈ 314 < τ_min ≈ 417. At T = 2.0, Nb = 400 gives +0.347 on
[Ω_lo, Ω_lo+25]; Nb = 800 (max frequency 628) gives **−1.712** at τ = 380.76. At T = 1.0 (Nb = 400 resolves 628 ≫ 55)
the margin +0.312 is reproduced. So the all-profile operator inequality fails generically once the basis can
represent oscillation at frequency τ; the non-monotone pattern of ROUND_013_B is an artefact of Nb·π/2T vs τ.

## 2. What the top eigenvector is

Spectral content of the top eigenvector f of A_τ at (T,τ) = (1.5, 140.434): 99.95% of ‖f̂‖² lies above |ξ| = τ/2
(Nb = 400/600/800 all ≥ 99.94%; at (2.0, 380.76) 99.91%). The maximiser is not an envelope: f ≈ h(x)cos(τx + φ)
with h slowly varying. ARGUED: for such f, c_f(u) ≈ ½cos(τu)c_h(u) up to a term oscillating at 2τ, so ⟨f, A_τ f⟩ ≈ ½Σ_n v_n cos²(τ log n)c_h(log n): the
Dirichlet phase enters squared, every term is non-negative, which explains λ_max > m(τ).

Proposition 3.1 of ROUND_012_A (PROVED as stated: sup over all real β ∈ L²[−1,1]) is correct, but the identification
"P^{ρ_β}_T(τ) = comb part of W_T on the packet β(x/T)cos(τx)" rests on c_{β cos τ·}(u) ≈ ½cos(τu)c_β(u), which needs β
to vary slowly against τ (the dropped term ½∫f f(·+u)cos(τ(2x+u)) is not small when f oscillates at τ). The sup in
Prop 3.1 is attained exactly in the regime where that reduction is invalid.

## 3. Direct W_T on the violating test function

g = P_T[f(x)cos(τx)] (two Tate constraints ∫g e^{±x/2} = 0), W_T(g) = (1/2π)∫m|ĝ|² − Σ v_n c_g(log n), FFT grid
2^15+1 points, zero padding ×32, exact comb (12 terms). Per ‖g‖²:

| (T, τ, Nb) | packet prediction m−λ_max | W_T(g) | arch | comb | projection loss |
|---|---|---|---|---|---|
| (1.5, 140.434, 400) | −0.5037 | **+0.7912** | 3.7875 | 2.9963 | 0.665 |
| (1.5, 140.434, 600) | −0.5078 | **+0.7991** | 3.7909 | 2.9918 | 0.663 |
| (1.5, 140.434, 800) | −0.5098 | **+0.7985** | 3.7932 | 2.9948 | 0.662 |
| (2.0, 380.755, 800) | −1.7118 | **+1.0540** | 4.7353 | 3.6813 | 0.661 |

Control: the bare eigenvector g = P_T f (itself a packet at frequency τ): W/‖g‖² = +4.498 (T = 1.5, arch 3.113 ≈ m(τ),
comb −1.385) and +3.243 (T = 2.0). Modulating f by cos τx produces components at 0 and 2τ; the projection removes
≈ 66% of the norm (the low-frequency half), and the remaining 2τ-part sees the larger m(2τ). No negative direct value.

**Galerkin λ_A(1.5)** (tools/galerkin_mp.py, dps = 30): −8.8·10⁻⁵⁰ (N = 80), −2.1·10⁻⁴⁹ (N = 120), against an estimated
Arch entry error 2·10⁻⁴⁶: **unresolved at dps 30** (the value is below the quadrature noise; λ_A(1.5) is expected
of order 10⁻¹⁰ or smaller by tools/galerkin_mp.margin_bound). No contradiction either way; a dps ≥ 80 run is needed to resolve the sign.

## 4. Envelope-restricted operator

Restricting A_τ to the first k_c sine modes with k_cπ/2T ≤ τ/4 (envelopes band-limited to |ξ| ≤ τ/4, the regime where
the packet reduction holds), same T-scan 1.40–1.60: margin **+0.46 to +0.72** at every T (+0.468 at T = 1.50,
τ = 140.42). The violation disappears under the band restriction.

## Falsifier note

No sign step is made. The verification is a diagnosis of a numerical object; falsifiers (a)–(d) are not applicable.

## Result

NUMERICAL, answer (a): the −0.504 is real for the operator λ_max(A_τ) (converged in Nb, ≤ −0.511 at Nb = 1000, negative
on all of T ∈ [1.40,1.60], and also at T = 2.0, −1.71, once the basis resolves frequency τ — ROUND_013_B's positive
values at T ≥ 2 were truncation artefacts), but it is **not a negative value of W_T**: the maximiser oscillates at
frequency τ, outside the validity of the packet reduction, and the direct W_T on the corresponding projected test
function is +0.79 (T = 1.5) and +1.05 (T = 2.0) per unit norm. The packet error is the dropped 2τ cross term (O(1), not
o(1)), plus a 66% projection loss.

## What was proved

Nothing (NUMERICAL only).

## What failed and why

The all-profile operator form "λ_max(A_τ) ≤ m(τ)" of ROUND_012_A Proposition 3.1 is false (NUMERICAL) at T = 1.4–1.6 and
T = 2.0; as an unrestricted sup over L² profiles it is not a valid condition for (HR)(a), because its maximisers are
not packets. The correct object is A_τ compressed to envelopes band-limited well below τ.

## Next concrete step

Re-state Proposition 3.1 with a band restriction (|ξ| ≤ ητ, η < ½) and recompute the envelope margin at T = 2.0–3.0
with Nb resolving τ; quantify the margin's dependence on η.
