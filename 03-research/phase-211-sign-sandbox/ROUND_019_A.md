# Round 19 A — Band-limitation of the tail as a constraint family on R-cell data

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_016_B, ROUND_017_C, ROUND_018_A (F₁, 𝔇_R, Q_R, V_R, ℓ_g, κ_R).
λ = e^T. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Index rows read: P211-16B (dilation form, idealised R-cell problems, near-null in D-units), P211-17C (first-cell
certificates μ₀, μ₄), P211-18A (R-cell form against ℓ_g: κ_R ≈ 0.81, 0.75, 0.68 for R = 2–4, collapse for R ≥ 5 at T = 0.8;
Theorem 3.4; missing family = band-limitation, OPEN). What differs: 18A ran the R-cell problem on all of L²(I_R) ∩ V_R; here
the class is cut down by the Paley–Wiener structure of u = ℱf (f supported in [−λ, λ]). Two formulations are examined: the
qualitative one (u_{|(λ,Rλ)} is the restriction of an even entire function of type 2πλ in L²(ℝ)) and the quantitative one
(u is θ-concentrated on (λ, Rλ) among such functions). Prolate/time–band-limiting tools have appeared in the corpus as
Galerkin bases for the high block (15A); they have not been used as a constraint family on multi-cell data. Nothing indexed
is retried.

## 1. The qualitative band constraint is vacuous on R-cell data (PROVED, NO-GO for that formulation)

Let J_R = (λ, Rλ), E_λ = {ℱf : f ∈ L²(−λ, λ) even} (even Paley–Wiener functions of type 2πλ), and let 𝔅_R be the set of
F ∈ L²(I_R) with F(x) = e^{−x/2}u(e^{−x}), u = g_{|J_R}, g ∈ E_λ (u extended by 0 outside J_R, i.e. the R-cell truncation of
18A §2.1 applied to band-limited data).

### Proposition 1.1 (PROVED)
𝔅_R ∩ V_R is dense in V_R for the form norm of Q_R (and in L²). Consequently, for every R and T,
    inf{Q_R[F]/ℓ_g[F] : F ∈ 𝔅_R ∩ V_R} = κ_R(T),
i.e. imposing "u is the restriction of a type-2πλ function" changes nothing; the collapse of 18A §2.2(b) persists verbatim.
*Proof.* (1) Form norm. Q_R[F] = 𝒬[𝔇_R F] − cΠ[𝔇_R F] + 2A B, where Π, A, B are L²-bounded and 𝒬[H] = (1/2π)∫m|Ĥ|² with
|m(τ)| ≤ C log(2 + |τ|). For H the zero extension of a function in H¹ of a bounded interval, H ∈ H^s(ℝ) for every s < ½ with
‖H‖_{H^s} ≤ C_s‖H‖_{H¹(I)}, and ∫log(2 + |τ|)|Ĥ|² ≤ C‖H‖²_{H^s}; 𝔇_R is a finite sum of shifted truncations (each H¹ on its
piece). Hence Q_R is continuous for the H¹(I_R)-norm on each piecewise-H¹ space, and it suffices to prove density of 𝔅_R in
H¹(I_R) (C^∞(Ī_R) is dense there). The change of variables x ↦ ξ = e^{−x} and F ↦ u is a bi-Lipschitz smooth isomorphism
H¹(I_R) ≅ H¹(J_R).
(2) Density in H¹(J_R). By Hahn–Banach it suffices that every ℓ ∈ H¹(J_R)* vanishing on ρ(E_λ) is 0. Write
ℓ(u) = ∫_J(v₀u + v₁u′) with v₀, v₁ ∈ L²(J_R). For g = ℱf, f ∈ L²(ℝ) with ∫(1 + |x|)|f| < ∞, differentiation under the integral
gives ℓ(g) = ∫f(x)Φ(x)dx with Φ(x) = ∫_J(v₀(ξ) − 2πix v₁(ξ))e^{−2πixξ}dξ, an entire function of x (J_R bounded). If ℓ vanishes
on ρ(E_λ), then Φ(x) + Φ(−x) = 0 for |x| ≤ λ, hence for all x (identity theorem). So ℓ(ℱf) = ½∫f(x)(Φ(x) + Φ(−x))dx = 0
for every even Schwartz f. Every h ∈ C^∞(J̄_R) is such a restriction (extend h to an even C_c^∞ function on ℝ, J̄_R ⊂ (0, ∞),
and take f = ℱ^{−1} of it). C^∞(J̄_R) is dense in H¹(J_R), so ℓ = 0.
(3) Constraints and ℓ_g. V_R = ker(w_1, …, w_4) with L²-continuous functionals, linearly independent on the dense subspace;
pick d_1, …, d_4 ∈ 𝔅_R with ⟨d_i, w_j⟩ = δ_ij; for F ∈ V_R and F_n → F in 𝔅_R, F_n − Σ⟨F_n, w_i⟩d_i ∈ 𝔅_R ∩ V_R → F. ℓ_g is an
L²-continuous quadratic form (a squared distance to a closed subspace). The infimum of a ratio of two continuous forms over a
dense subspace equals the infimum over the closure, wherever the denominator is positive. ∎

Reading. The band-limitation is not a closed constraint on a bounded set of frequencies: restrictions of PW functions to a
bounded interval are dense. Any lift of κ_R must come from a *quantitative* form of the band structure — how much of ℱf the
datum is allowed to put outside (λ, Rλ) (below λ: in-band; beyond Rλ: later cells), equivalently the cost ‖f‖²/‖u_{|J_R}‖².
The truncation at Rλ in 18A is exactly what destroys the link between cells. Section 2 measures the quantitative family.

## 2. The quantitative band family

### 2.1 Definitions (PROVED bookkeeping)
P_λ: the orthogonal projection of L²(0, ∞) (identified with even functions on ℝ, norm on (0, ∞)) onto E_λ; its kernel is
    k_λ(ξ, η) = sin 2πλ(ξ − η)/(π(ξ − η)) + sin 2πλ(ξ + η)/(π(ξ + η)),
and ‖P_λu‖²_{(0,∞)} = ∫_0^λ|û_c(x)|²dx with û_c(x) = 2∫_0^∞u(ξ)cos 2πxξ dξ. For F ∈ L²(I_R) with tail u (zero outside J_R) put
    β[F] := ‖(1 − P_λ)u‖²_{L²(0,∞)} (band defect),   B_R := 1_{J_R}P_λ1_{J_R} (concentration operator; 0 ≤ B_R ≤ 1,
trace class, tr B_R = ∫_{J_R}k_λ(ξ, ξ)dξ = 2λ²(R − 1) + O(1)). Since F ↦ u is unitary L²(I_R) → L²(J_R), β[F] = ‖F‖² − ⟨B_RF, F⟩.
Two constraint families: the spectral family S_θ := span of eigenvectors of B_R with eigenvalue ≥ θ (a subspace, β ≤ (1 − θ)‖F‖²
on it), and the cone {β[F] ≤ ε‖F‖²}. S_θ ⊂ cone(1 − θ), so inf over S_θ ≥ inf over the cone: a lift seen on S_θ does not imply a lift on
the cone.

### Lemma 2.1 (band defect of actual data; PROVED)
Let f ∈ L²(−λ, λ) be even, g = ℱf ∈ E_λ, u = g·1_{J_R}. Then β[u]^{1/2} ≤ ‖g‖_{L²(0,λ)} + ‖g‖_{L²(Rλ,∞)}.
*Proof.* u = g − g1_{(0,λ)} − g1_{(Rλ,∞)}, (1 − P_λ)g = 0, ‖1 − P_λ‖ ≤ 1. ∎
So the band information actual R-cell data carry is exactly: band defect ≤ (in-band amplitude + amplitude beyond the R-th
cell)². On the measured high-block vectors of 18A §1, the in-band mass is < 10⁻⁴‖f‖² and the mass beyond 2λ is 0.005–0.44.

### 2.2 Tool (NUMERICAL)
tools/multi_cell/cellRb_mp.py R Nb T J c dps NQ θ-list (env MUS = penalty list). It builds Q_R, the four transported
constraints and ℓ_g^{fam} exactly as cellRg_mp.py (18A §2.1; mpmath, 50–110 digits), caches them, and adds: the matrix of B_R
in the sine basis of I_R (ψ_k(ξ) = ξ^{−1/2}e_k(T + h − log ξ), Gauss–Legendre in ξ with 400 + 300Rλ nodes, double precision;
Gram check ≤ 2.5·10⁻¹³, so band defects below ≈ 10⁻¹² are not resolved); (i) κ_R on V_R ∩ S_θ for θ ∈ {0, 0.5, 0.9, 0.99};
(ii) the penalised quotient κ_R(μ) := inf_{V_R}(Q_R + μβ)/ℓ_g^{fam} and, at its minimiser, the band defect β/‖F‖² and the
unpenalised ratio Q_R/ℓ_g. The penalty is homogeneous with the denominator: (ii) measures the frontier
"band defect comparable to ℓ_g".

## 3. κ_R with the band family (NUMERICAL)

### 3.1 Spectral family: κ_R on V_R ∩ S_θ (Nb = 40 sine modes, J = 20–40, 50–110 digits)
| T | R | θ = 0 (= 18A) | θ = 0.5 | θ = 0.9 | θ = 0.99 | dim S_θ (θ = 0.9) of 40 | band defect of the θ = 0 bottom |
|---|---|---|---|---|---|---|---|
| 0.8 | 2 | 0.809 | 0.816 | 0.985 | 1.059 | 8 | 7·10⁻³ |
| 0.8 | 3 | 0.739 | 0.745 | 0.758 | 0.777 | 18 | 2.7·10⁻⁴ |
| 0.8 | 4 | 0.676 | 0.682 | 0.699 | 0.754 | 26 | 1.2·10⁻⁵ |
| 0.8 | 5 | 0.168 (Nb 48: 0.112) | 0.644 (0.651) | 0.665 (0.703) | 0.710 (0.712) | 31 | 7.3·10⁻⁸ |
| 0.8 | 6 | 0.104 (Nb 48: 0.088) | 0.652 (0.660) | 0.660 (0.665) | 0.663 | 33 | 9.4·10⁻¹¹ |
| 0.8 | 7 | 7.7·10⁻⁵ | 0.380 | 0.648 | 0.653 | 34 | ≤ 10⁻¹² (floor) |
| 0.8 | 8 | 1.5·10⁻⁷ | 0.207 | 0.592 | 0.601 | 35 | ≤ 10⁻¹² (floor) |
| 1.0 | 3 | 0.690 | 0.725 | 0.745 | 0.761 | 27 | 3·10⁻⁴ |
| 1.0 | 4 | 0.073 | 0.510 | 0.709 | 0.713 | 33 | 3.5·10⁻⁵ |
| 1.0 | 5 | 0.021 | 0.630 | 0.652 | 0.675 | 36 | 1.7·10⁻⁶ |
| 1.0 | 6 | 0.0023 | 0.573 | 0.599 | 0.624 | 37 | 3.9·10⁻⁹ |
| 1.0 | 7 | 6.7·10⁻⁶ | 0.372 | 0.429 | 0.609 | 38 | ≤ 10⁻¹¹ |
| 1.0 | 8 | 3.2·10⁻⁸ | 3.2·10⁻⁸ | 0.404 | 0.404 | 38 | ≤ 10⁻¹² |
Readings.
(a) **The collapse is carried by the few least band-concentrated directions of the cell basis.** Removing the 1–6 eigen-
directions of B_R with concentration < 0.5 (θ = 0.5) lifts κ_R from 10⁻⁸–0.17 to 0.21–0.66; at θ = 0.9 every row is
≥ 0.40 and the T = 0.8 rows are 0.59–0.70 for R = 4–8. The second eigenvalue of the θ = 0 problem (0.33–0.67) already
showed that the collapse is one direction per R, not a band of directions.
(b) **But the collapse directions are themselves almost band-limited**: their band defect is 7·10⁻⁸ (R = 5), 10⁻¹⁰ (R = 6),
below the double-precision floor of B_R for R ≥ 7 (T = 0.8). They are not excluded by any band defect ε of realistic size; what
excludes them is that their band defect is not small *compared with their gauge leakage* ℓ_g, which is equally tiny
(β/ℓ_g = 1.7 at R = 5, 1.5 at R = 6, T = 0.8). The spectral family S_θ excludes them only because, at these sizes, a direction
with concentration < θ in the Galerkin basis contributes to the bottom vector with weight comparable to √ℓ_g. Hence the
spectral lift is a statement about the homogeneous ratio β/ℓ_g, which is what §3.2 measures.
(c) At T = 1.0 the lift is weaker and decreasing for R ≥ 6 (0.60, 0.43, 0.40 at θ = 0.9), with Galerkin capture of the
Shannon number 2λ²(R − 1) (= 103 at R = 8) incomplete at Nb = 40 (only 2 directions below 0.99): not resolved.

### 3.2 Penalised (cone) family: κ_R(μ) = inf_{V_R}(Q_R + μβ)/ℓ_g^{fam} (B_R in 300–400-bit ball arithmetic, composite
Gauss–Legendre 60 × 30 nodes in ξ and in x; 40 × 30 gives the same digits at R = 8, T = 1.0; penalty matrix PSD to 10⁻⁴⁸)
| T | R | μ = 10⁻² | μ = 1 | μ = 10² | μ = 10⁴ | μ = 10⁶ | β/ℓ_g of the μ = 10⁻² minimiser |
|---|---|---|---|---|---|---|---|
| 0.8 | 3 | 0.737 | 0.740 | — | — | — | 0.016 |
| 0.8 | 4 | 0.676 | 0.678 | — | — | — | 0.011 |
| 0.8 | 5 | 0.168 | 0.643 | 0.705 | 0.777 | 0.798 | 1.7 |
| 0.8 | 6 | 0.105 | 0.600 | 0.664 | 0.698 | 0.764 | 1.5 |
| 0.8 | 7 | 1.1·10⁻⁴ | 0.522 | 0.654 | 0.699 | 0.746 | 1.3 |
| 0.8 | 8 | 1.7·10⁻⁴ | 0.331 | 0.628 | 0.648 | 0.687 | 1.2 |
| 1.0 | 4 | 0.073 | 0.632 | 0.707 | 0.722 | 0.739 | 0.97 |
| 1.0 | 5 | 0.021 | 0.428 | 0.663 | 0.699 | 0.719 | 0.83 |
| 1.0 | 6 | 0.0024 | 0.287 | 0.624 | 0.642 | 0.674 | 0.80 |
| 1.0 | 7 | 9.3·10⁻⁵ | 0.232 | 0.592 | 0.634 | 0.672 | 0.84 |
| 1.0 | 8 | 1.0·10⁻⁴ | 0.220 | 0.451 | 0.543 | 0.627 | 0.85 |
(κ_R(μ) is nondecreasing in μ since β ≥ 0; the R = 3, 4 (T = 0.8) rows are already at their μ = 0 value.)
Readings.
(a) **The collapse directions are exactly the directions whose band defect is of the size of their gauge leakage**:
β/ℓ_g ≈ 0.8–1.7 on every collapsing row (R ≥ 5 at T = 0.8, R ≥ 4 at T = 1.0), against 0.01–0.02 on the non-collapsing
rows R = 3, 4. With a penalty μ ≥ 10² on β the ratio returns to 0.45–0.71, and at μ = 10⁶ it is ≥ 0.627 on every row
R = 3 … 8, T ∈ {0.8, 1.0}.
(b) **R-uniformity is not seen at fixed μ**: at μ = 1 the values decrease (T = 1.0: 0.63, 0.43, 0.29, 0.23, 0.22), at
μ = 10² (T = 1.0: 0.71, 0.66, 0.62, 0.59, 0.45), and at μ = 10⁶ they still decrease by 0.02–0.05 per added cell at T = 1.0
(0.74, 0.72, 0.67, 0.67, 0.63). The penalty needed to keep a fixed constant grows with R. Whether it grows boundedly
(an R-uniform (HR_g) with a band penalty) is not decided by R ≤ 8.
(c) Answer to the question of the round: **with band limitation entered as a constraint family the collapse disappears
only in the homogeneous form "band defect ≪ gauge leakage"; the qualitative band constraint changes nothing (§1), and an
absolute band defect bound β ≤ ε‖F‖² of realistic size (ε ≥ 10⁻¹²) changes nothing for R ≥ 5 (the collapse directions
have β/‖F‖² ≤ 10⁻⁷ … 10⁻¹³).**

## 4. What can be stated

### Theorem 4.1 (band-penalised (HR_g); CONDITIONAL)
Hypotheses. (H_band(μ, κ)) For every R ≥ 2 and every F ∈ V_R: Q_R[F] + μβ[F] ≥ κ·ℓ_g[F]. (H_lim) For the tail u of an
admissible f, with F_R the R-cell truncation, Q_R[F_R] → 𝒲[𝒯u] + 2A(𝒯u)B(𝒯u) and ℓ_g[F_R] → ℓ_g[F] as R → ∞, and the
transported constraints coincide with the exact ones (the transport-defect hypothesis of 18A Theorem 4.1(ii)).
Conclusion. For every even f ∈ L²(−λ, λ) satisfying the admissibility conditions,
    𝒲[𝒯u] + 2A(𝒯u)B(𝒯u) ≥ κ·ℓ_g[F] − μ·‖ℱf‖²_{L²(0,λ)}.
*Proof.* By Lemma 2.1, β[F_R] ≤ (‖ℱf‖_{L²(0,λ)} + ‖ℱf‖_{L²(Rλ,∞)})²; the second term tends to 0. Apply H_band to F_R and
let R → ∞ using H_lim. ∎
Status of the hypotheses. H_band(10⁶, 0.62) holds NUMERICALLY for R ≤ 8 at T = 0.8 and 1.0 (§3.2, Galerkin Nb = 40 with a
finite gauge family; the two approximations go in opposite directions, as in 18A §2.1), with a constant still decreasing in
R at T = 1.0; for R = 2, 3 it holds with μ = 0 (Prop. 3.1 and Theorem 3.4 of 18A; PROVED). H_lim is ARGUED (16B Lemma 2.1
plus continuity of Q in the form norm); the transport-defect part fails on the measured vectors (18A §1). The conclusion is
the strongest statement the data support: it moves the obstruction from the tail form to the **in-band mass** ‖ℱf‖²_{(0,λ)},
which the tail form cannot pay for and which belongs to the low block.

### What is needed to certify H_band for all R
(1) A certificate at fixed R ≥ 4 in the spirit of Lemma 3.3 of 18A, with the penalty μ(1 − B_R) added to Φ_P: B_R is an
explicit integral operator (sinc kernel) and its piecewise-polynomial compression is as accurate as that of the symbol
(entire kernel); for R = 4 the 𝔇-structure has pieces at log 4/3, log 3/2, log 2, log 3 and the comb shifts log 2, log 3 —
Lemma 3.2 of 18A extends verbatim with 5 pieces. (2) An R-uniform mechanism: the numerics say the constant decays slowly at
fixed μ, so H_band at fixed μ needs an argument that the (R + 1)-st cell can only create a near-null direction with
β/ℓ_g ≳ 1 — a statement about the near-null direction of the cell-transfer (lower-triangular Toeplitz 𝔇_R in log N)
being out of band at the scale of its gauge leakage. No such argument is available; OPEN. (3) A low-block bound
(LB_μ): the in-band part of the complete form dominates μ‖ℱf‖²_{(0,λ)} on admissible f modulo gauge, with μ of order
10²–10⁶; without it Theorem 4.1 does not close.

## 5. Falsifiers on Theorem 3.4 of 18A and on the band-restricted forms

### 5.1 Structural remark (PROVED)
Theorem 3.4 of 18A is a statement about Q₃ on a window of length log 3. Q₃ depends on the arithmetic only through (i) the
comb coefficient at m = 2 in Π, and (ii) the dilation operator 𝔇₃ = 1 + 2^{−1/2}τ_{log 2} and the transported functionals,
which use the integers 1, 2 (and the integers n in the A, B weights, which come from the additive structure of E, not
from Λ). Hence:
 (c) for any generalized-prime system whose generalized primes and integers in [1, 3) are {2} and {1, 2}, with
     Λ(2) = log 2, the statement is word for word the same: the theorem cannot distinguish such a system from ℕ;
 (d) a finite modification of v_n at n ≥ 3 leaves it unchanged; a modification at n = 2 is v_2 ↦ c₂v_2, i.e. the
     falsifier-(a) parameter restricted to m = 2;
 (b) a_P with P = 3 is c₂ = 0.
So any R-cell statement at fixed R survives (c) and (d) for modifications beyond the R-th cell; by rule 4 such a statement
is a coercivity piece, never a sign step. The sign, if the R-cell route carries one, can only live in R-uniformity.

### 5.2 Measurements and certificates
| test | class | result |
|---|---|---|
| (b) a_3: c₂ = 0, T = 0.8 | V₃ | CERTIFIED (cert3.py, 128-bit arb, τ* = 100, n = 70, J = 20): Q₃ ≥ 0.60·ℓ_g; γ = 0.0223, X_c = 3.8·10⁻³, Y_c = 0.784 |
| (b) a_3: c₂ = 0, T = 1.0 | V₃ | CERTIFIED (QW = 320): Q₃ ≥ 0.60·ℓ_g; γ = 0.0220, X_c = 1.5·10⁻⁶ |
| (d) v_2 ↦ 1.01·v_2, T = 0.8 | V₃ | CERTIFIED: Q₃ ≥ 0.20·ℓ_g; γ = 2.5·10⁻⁴, X_c = 1.3·10⁻³, Y_c = 0.689 |
| (d)/(a) threshold, T = 0.8 | V₃ (pw3, n = 40) | inf Q₃/‖F‖² = 1.4·10⁻³ (c₂ = 1), 5·10⁻⁴ (1.01), 8·10⁻⁵ (1.015), −3.6·10⁻⁴ (1.02): c₂* ≈ 1.016 |
| (d)/(a) threshold, T = 1.0 | V₃ (pw3) | 6.9·10⁻⁴ (1.0), −1.1·10⁻³ (1.02): c₂* ≈ 1.008 |
| c₂ sweep 0 → 1, T = 0.8 | V₃ (pw3) | κ₃ = 0.67 (c = 0), 0.83 (0.5), 0.91 (0.9), 0.86 (1.0): positive on all of [0, 1] |
| (a) c = 1.1, band, T = 0.8 | V₃ ∩ S_θ | θ = 0, 0.5, 0.9: negative (−5.8, −3.9, −1.7 in ℓ_g units); θ = 0.99: +0.50; θ = 0.999: +0.62 |
| (a) c = 1.1, band, T = 1.0 | V₃ ∩ S_θ | θ ≤ 0.9: negative (−10.2, −9.6, −0.12); θ = 0.99: +0.23; θ = 0.999: +0.42 |
| (a) c = 1.1, penalised, T = 0.8 | V₃, μ = 10⁻², 1, 10² | negative throughout (−5.8, −5.8, −3.1); minimiser band defect 3·10⁻⁴ → 3·10⁻⁵ |
| (a) c = 1.1, R = 4, T = 0.8 | V₄ ∩ S_θ, penalised | negative for every θ ≤ 0.999 (−0.06 to −0.09 per ‖F‖²) and every μ ≤ 10² |
| (a) c = 0.9, R = 4, T = 0.8 | V₄ ∩ S_θ, penalised | negative for θ ≤ 0.9 (−0.008 per ‖F‖², κ = −24) and μ ≤ 10²; positive (0.54, 0.67) at θ = 0.99, 0.999 |
Readings.
(i) Theorem 3.4 survives (b) (certified, κ = 0.60 at both T) and survives (c), (d) beyond m = 2 by 5.1. It fails (a)/(d) at
m = 2 only for c₂ > c₂* ≈ 1.016 (T = 0.8) / 1.008 (T = 1.0). **The true weight c₂ = 1 sits 0.8–1.6 % below the positivity
threshold of the three-cell form.** Theorem 3.4 is a coercivity piece, not a sign step (as 18A stated).
(ii) The band family does not repair falsifier (a) in the penalised (cone) form at R = 3, and at R = 4 the form is negative
for c = 0.9 **and** for c = 1.1 in the idealised class, in every spectral class up to θ = 0.9, and for every penalty up to
10². This is the first two-sided failure of falsifier (a) recorded in this phase: on four-cell data with the transported
constraints, the complete form is nonnegative only in a window of c around 1 that excludes 0.9 and 1.1. (ARGUED reason:
at R = 4 both comb shifts m = 2, 3 act and 𝔇₄ carries the same integers with fixed weights; the near-null direction is a
cancellation between the 𝔇-comb, which does not scale with c, and Π, which does; moving c either way breaks it at first
order, by O(0.1)·Π ≈ 10⁻² against a null value 6.5·10⁻⁶.)
(iii) The S_θ lift of c = 1.1 at R = 3 for θ ≥ 0.99 is an artefact of removing directions that the cone (μ ≤ 10²) keeps: with
the realistic constraint (§2, Lemma 2.1) the c = 1.1 failure stands.

## 6. Corpus and index notes
Proposition 1.1 closes the qualitative band family as a constraint on R-cell data (density of restrictions of
Paley–Wiener functions); the useful band information is the homogeneous ratio β/ℓ_g. Nothing in §§1–5 retries an indexed
route: the prolate/concentration operator appears in 15A only as a basis for the high block.

## Result
PIVOT with reason (and PROVED pieces). The band constraint as a closed condition is vacuous (PROVED); as a penalty it removes
the collapse (NUMERICAL, R ≤ 8) but only when the band defect is charged at a rate μ that has to grow with R, and it moves the
deficit to the in-band mass, i.e. to the low block. Falsifier (a) now fails on both sides at R = 4 (c = 0.9 and 1.1), the
first two-sided failure in this phase.

### What was proved
- Proposition 1.1: restrictions of type-2πλ Paley–Wiener functions are dense in the form domain of Q_R ∩ V_R; the
  qualitative band constraint leaves κ_R unchanged.
- Lemma 2.1: band defect of actual R-cell data ≤ (in-band amplitude + amplitude beyond Rλ)².
- §5.1: any fixed-R statement is invariant under falsifiers (c), (d) beyond the R-th cell; fixed-R statements are coercivity
  pieces, never sign steps.
- Certified (128-bit arb, cert3.py): Q₃ ≥ 0.60·ℓ_g with c₂ = 0 at T = 0.8 and T = 1.0 (falsifier (b), a_3); Q₃ ≥ 0.20·ℓ_g with
  c₂ = 1.01 at T = 0.8.
- Theorem 4.1 (CONDITIONAL on H_band, H_lim).

### What failed and why
- Qualitative band limitation: dense, so imposes nothing.
- Absolute band-defect bounds: the collapse directions have β/‖F‖² = 10⁻⁷ … 10⁻¹³; no realistic ε excludes them.
- Spectral family S_θ: lifts κ_R to 0.40–0.70 (θ = 0.9) but overstates the realistic constraint (it also lifts c = 1.1 at
  R = 3, which the cone does not).
- R-uniformity at fixed penalty: not seen; at μ = 10⁶, T = 1.0 the constant still drops 0.02–0.05 per cell.
- Theorem 3.4 is not weight-blind on the c₂ > 1 side: threshold c₂* ≈ 1.016 (T = 0.8), 1.008 (T = 1.0), so the true weight
  sits within 1.6 % of failure.

### Next concrete step
Measure the in-band side: on admissible f modulo gauge, the low-block part of the complete form against μ‖ℱf‖²_{L²(0,λ)}
(the quantity Theorem 4.1 leaves), for μ = 10², 10⁴, 10⁶ at T = 0.8, 1.0; in parallel, extend the Lemma 3.3 certificate to
R = 4 with the penalty μ(1 − B_R) (five pieces, shifts log 2, log 3) to certify H_band at R = 4.

## Reproducibility
tools/multi_cell/cellRb_mp.py R Nb T J c dps NQ θ-list; environment MUS (penalty list), BCMP=1 (B_R in ball arithmetic),
NPAN (panels, default 60). First run builds and caches Q_R, constraints, ℓ_g^{fam} (≤ 20 min at R = 8); later runs reuse the
cache (outputs collected in tools/multi_cell/runs19.txt). pw3.py for the c₂ sweep; cert3.py τ* n T J κ c for the certificates (QW=320 at T = 1.0). Every run ≤ 20 min.
