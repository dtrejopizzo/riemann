# EXP_002 — Controls, computed in the same run as Λ

All numbers NUMÉRICO (double precision; floor = 2.2·10⁻¹⁶‖A_M‖M; "negative" means λ_min < −10·floor). Profile b = 1.
Controls (same lattice {log m : m ≤ M}, same profile, same code path as Λ; data/controls_T00.3.json, controls_T00.15.json):
a_P = Λ with primes < P deleted (P = 3, 5); pert_n(±ε) = v_n multiplied by 1 ± ε (n = 2, 3, 7; ε = 10⁻⁵, 10⁻²); amp2(c) = v₂ + c;
Poisson combs (Paper 46 thm:poisson: Poisson process on (log 2, ∞), intensity e^u/u, weights 2xe^{−x/2}; 5 seeds; atom counts match the
prime-power counts, e.g. 428–467 vs 450 at M = 1500, T₀ = 0.3); Beurling combs (generalized primes q = p·e^{ε_p}, ε_p uniform in
±0.02, weights 2 log q·q^{−a/2} on powers; evaluated both on the integer lattice and on the lattice of its own generalized integers
≤ M, where the exact products are its "Div"); quartet model M₁ = Λ + 𝔮_{δ,γ₁}, γ₁ = 14.1347, δ = 0.1 and 0.3 (rank-4 Toeplitz kernel
Q(d) added to B(d), EXP_001 §1).

## 1. First negative M and size of the negativity (T₀ = 0.3)
| comb | M = 50 | 100 | 200 | 400 | 700 | 1000 | 1500 |
|---|---|---|---|---|---|---|---|
| Λ | +3.3e−5 | +4.5e−6 | +5.9e−7 | +7.8e−8 | +1.5e−8 | +5.2e−9 | +1.6e−9 (floor 1.3e−10) |
| a₃ | −1.5 | −2.9 | −5.7 | −11.3 | −19.8 | −28.2 | −42.4 |
| a₅ | −2.4 | −4.2 | −7.2 | −14.6 | −25.4 | −36.3 | −54.3 |
| pert₂(+10⁻⁵) | +3.1e−5 | +2.4e−6 | −2.0e−5 | −1.7e−4 | −3.6e−4 | −5.2e−4 | −7.9e−4 |
| pert₂(−10⁻⁵) | +3.5e−5 | +6.3e−6 | +1.5e−6 | −7.9e−6 | −9.9e−5 | −1.9e−4 | −3.2e−4 |
| pert₂(±10⁻²), pert₃(±10⁻²), pert₇(±10⁻²) | −0.005…−0.024 | −0.018…−0.055 | −0.04…−0.11 | −0.09…−0.23 | −0.16…−0.40 | | −0.34…−0.85 |
| Poisson (5 seeds) | −3.0…−6.8 | −4.2…−17.5 | −16…−35 | −28…−69 | −42…−127 | | −82…−237 |
| Beurling (int. lattice / own lattice) | −1.5/−1.5, −1.3/−1.2 | −3.2/−3.1, −2.3/−2.2 | −6.4/−6.1, −4.7/−4.7 | −12.3/−12.1 | −20.9/−21.0 | | −44.8/−44.5 |
| M₁ δ = 0.1 / 0.3 | −0.22/−2.4 | −0.50/−5.4 | −1.0/−10.9 | −2.0/−22.3 | −3.7/−41.9 | | −7.3/−84.3 |
(The 10⁻⁵ perturbations are positive at M ≤ 100 and turn negative between M = 100 and 400; all structural controls are negative already at M = 50.) T₀ = 0.15 (M = 100…800): same picture; pert₂(+10⁻⁵) negative from
M = 400, pert₂(−10⁻⁵) from M = 800; a₃: −1.1 → −7.8; Poisson −3…−90; M₁(0.1): −0.02 → −0.39.
**Every control is indefinite at M = 400 for both T₀; Λ is positive at every M computed.**

## 2. Amplification threshold c*(M) (v₂ → v₂ + c; log-bisection to 40 steps, data/analysis_min_T0*.json)
| T₀ | M = 100 | 200 | 400 | 800 | 1200 |
|---|---|---|---|---|---|
| 0.3: c* | 2.0e−5 | 2.9e−6 | 3.4e−7 | 2.9e−8 | 6.4e−9 |
| 0.3: first order −λ_min/(v^T ∂_cA v) | 2.3e−5 | 3.3e−6 | 4.5e−7 | 5.9e−8 | 1.7e−8 |
| 0.15: c* | 1.2e−4 | 1.7e−5 | 2.5e−6 | 3.6e−7 | 1.2e−7 |
| 0.15: first order | 1.3e−4 | 1.9e−5 | 2.7e−6 | 3.9e−7 | 1.2e−7 |
c*(M) ≍ λ_min(A_M)/0.18 (T₀ = 0.3) and decays like M^{−3} (same exponent as λ_min, EXP_003 §1). v^T(∂A/∂c)v = −0.17…−0.20 (T₀ = 0.3),
−0.20…−0.29 (0.15): the derivative of the bottom in the weight of n = 2 is O(1) and M-independent, so the threshold is λ_min itself up to a
constant. This is prop:wit-sens at the matrix level, with the explicit scale: at T₀ = 0.3, M = 1200 (window T = T₀ + ½log M ≈ 3.85) a change of
6.4·10⁻⁹ in v₂ (relative 6.5·10⁻⁹) destroys positivity.

## 3. Where the controls fail: the negative eigenvectors
At T₀ = 0.3, the bottom eigenvector of every negative control is a **smooth packet of consecutive integers at the largest scale** that the
window allows (data/controls_T00.3.json, field `vec`): a₃ at M = 700: support ≈ m ∈ [60, 150] peaked at 107 (participation ratio 220); at
M = 1500: peak 229 (PR 469); pert₂(+10⁻²): peak 163 (M = 700), 349 (M = 1500); pert₂(±10⁻⁵): peaks 160/105 (M = 700), 342/139 (M = 1500);
amp2 at c*: peak 160 (M = 700), 342 (M = 1500); Beurling, Poisson: peaks at various m with PR 100–500. The peak position scales like
0.15M–0.25M, i.e. the packet sits at log m₀ ≈ log M − (1.4 … 1.9): the failure is always produced at the top of the window, by a wide
(width ≈ 1–1.5 in log m) low-frequency packet. On these vectors Div(v) ≈ 0 (|Div| ≤ 0.6), Gram(v) ≈ Arch(v) (in-phase translates) and
Near(v) ≈ Arch(v) + |λ_min|: the negativity is "Near exceeds Arch by |λ|" with no divisor part at all. Example (pert₂(+10⁻⁵), M = 1500):
Arch 120.12, Div 0.60, Near 119.52, Gram 119.78, λ = −7.9·10⁻⁴. For M₁ the extra kernel carries the negativity (Extra = −7.3 at
δ = 0.1, −86.9 at δ = 0.3, M = 1500) on a vector concentrated at m = 1, 2, 3, 6 — a different mechanism (rank-4 kernel), as expected.
For Λ the bottom eigenvector is of a completely different kind (EXP_003 §2): global, ≈ m^{−½}, Div(v) ≈ 7, Near(v) ≈ −6.6.

## 4. Near at the failure
For the negative controls, the Near mass on the negative eigenvector is carried by the smallest atoms with the sign of the perturbation
(data/near_triples_T00.3_M800.json; "Near_n(v)" = contribution of atom n): pert₂(1+10⁻⁵), M = 800: Near₂ = +41.9, Near₃ = +27.9, Near₄ = +10.5,
Near₅ = −14.1, Near₇ = −4.8 (total +63.5 vs Arch 64.1, λ = −4.1·10⁻⁴); a₃: Near₃ = +21.8, Near₅ = +24.2, Near₇ = +9.4 (total +61.7 vs Arch 39.4,
λ = −22.6); Poisson seed 0: Near = +116.8 vs Arch 39.2. On the h-slices (h = m − kn) the mass is flat in h (0.36…0.63 for |h| ≤ 3) for
all combs, including Λ (3.4…4.6, EXP_003 §4): the additive-shift decomposition does not separate Λ from the controls.

## 5. The one-variable lag function B(d) (2×2 band, thm:band), d ≤ 15, primes to 6·10⁶ (data/band_T0*.json)
sup_{2T₀<d≤15}|B(d)|/a₀ (no violation means the 2×2 sections are all positive up to d = 15):
| comb | T₀ = 0.3 | 0.15 | 0.05 |
|---|---|---|---|
| Λ | 0.942 (at d = 12.69), 0 violations | 0.733 (7.92), 0 | 0.368 (7.17), 0 |
| a₃ | 0.991 (1.78), 0 | 0.733, 0 | 0.368, 0 |
| a₅ | 1.032 (1.78), 24 grid points | 0.732, 0 | 0.368, 0 |
| amp2(0.05), pert₂(1.01) | 0.942, 0 | 0.733, 0 | 0.368, 0 |
| Poisson (5) | 3.5–5.8, ≈3000 points each | 1.9–2.5, 330–810 | 0.66–0.88, 0 |
| Beurling (2) | 1.28–1.44, 113–304 | 0.88, 0 | 0.71, 0 |
So: the 2×2 band kills Poisson, Beurling (T₀ = 0.3) and a₅, but **a₃, amp2(0.05) and pert₂(1.01) pass the band up to d = 15 and are
indefinite at M = 100–200**. At T₀ ≤ 0.15 the band kills nothing among the arithmetic controls. Confirms the index (L2_023, P46 (S)): the
2×2 sections are necessary only; the sign is in the multi-scale joint matrix. Note for Λ at T₀ = 0.3 the band is nearly saturated
(0.942 at d = 12.69) without being violated — recorded in EXP_005 as a (zero-side) observation, not as a ζ-specific prime-side fact.

## 6. Conclusion of the control run
Every control fails at M ≤ 400, in a way that is visible with margin (O(1)–O(100) for structural controls, O(ε·M) for ε-perturbations).
Λ is the only comb in the run with A_M ⪰ 0 at every M, and its λ_min sits at the sharpness scale c*(M) ≍ M^{−3}: the matrices A_M(Λ)
are critical, not comfortably positive. Any ζ-specific regularity of Near claimed in EXP_003/005 must therefore survive a 10⁻⁵ change of
one weight only if it is an exact identity; statistical regularities of Near (norms, spectra, sign fractions, mass by atom) are shared by
the 10⁻⁵ perturbations to 5 digits and are NOT ζ-specific by construction.
