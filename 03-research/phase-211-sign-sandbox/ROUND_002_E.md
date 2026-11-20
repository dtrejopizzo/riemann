# Round 002 E — Galerkin test of the comb-null archimedean bottom Θ_T against the falsifiers

Notation of STATEMENT_001 and ROUND_002_D: Arch(F) = (1/2π)∫ m|F̂|², Π_w(F) = Σ_{x<2T} w_x Re c_F(x) for a finite
weight vector w on positions x (the comb Λ is w_{log n} = v_n), a_T = Arch − Π, Ψ_T(w) := λ_A(T; w) = inf_{S_T}[Arch − Π_w],
Θ_T(w) := inf{Arch(F) : F ∈ S_T, Π_w(F) = 0} = max_c Ψ_T(cw) (ROUND_002_D Theorem 1). Labels: PROVED / CITED / CONDITIONAL /
ARGUED / OPEN / NO-GO / NUMERICAL.

## 1. Corpus check

The object Θ_T and its falsifier test are those of ROUND_002_D §1–§7 (corpus check there: joint range / comb-null cone not in
the index). New here: (i) Galerkin values of Θ_T for six modified combs; (ii) the structural lemmas of §2 (Lipschitz
persistence, the convex body 𝒦_T, the correction of Corollary 3 under degenerate bottoms). The near-degeneracy of the bottom
of a_T at T = ½log5 and T = 0.9 is CITED from the corpus (λ_A(0.9) ≈ 5.8·10⁻¹⁷ in high precision, phase 186 coupling theory
and phase 197 barrier tables); it is used below only as a reading of the numerics, not as an input to any proof.

## 2. Pure mathematics

Let 𝒲 = ℝ^K be the space of weight vectors on fixed positions 0 < x_1 < … < x_K < 2T.

Lemma 1 (PROVED). For every w ≠ 0, Π_w takes both signs on S_T.
Proof. Let x_0 be the smallest position with w_{x_0} ≠ 0. Choose 0 < ε < x_0 smaller than the distance from x_0 to every
other position and with x_0 + ε < 2T; take G ∈ C_c^∞(J), J ⊂ I_T an interval of length ε with J + x_0 ⊂ I_T, A(G) = B(G) = 0,
and F_θ = G + e^{iθ}G(· − x_0). Exactly as in ROUND_002_D Theorem 1(ii) (A, B of the translate are e^{±x_0/2} times those of
G, hence 0), c_{F_θ} is supported in (−ε, ε) ∪ ±(x_0 − ε, x_0 + ε), which meets the positions only at x_0, and
Π_w(F_θ)/‖F_θ‖² = w_{x_0} cos θ /2. ∎

Lemma 2 (PROVED). 𝒦_T := {w ∈ 𝒲 : Ψ_T(w) ≥ 0} is convex and compact, and Θ_T(w) ≥ 0 ⟺ the line ℝw meets 𝒦_T.
Proof. Ψ_T is an infimum of affine functions of w, hence concave; it is finite and |Ψ_T(w) − Ψ_T(w')| ≤ ‖w − w'‖_1
(|Re c_F(x)| ≤ ‖F‖²), so 𝒦_T is closed and convex. Boundedness: by Lemma 1 and compactness of the unit sphere of 𝒲 together
with the 1-Lipschitz bound, Ψ_T(w) → −∞ as ‖w‖ → ∞ (for |w| = 1 pick F_w with Π_w(F_w) > 0; continuity in w gives a uniform
δ > 0 and a uniform Arch bound on finitely many such F covering the sphere, so Ψ_T(tw) ≤ C − tδ). The last statement is
Θ_T(w) = max_c Ψ_T(cw) (ROUND_002_D Theorem 1(iii), whose proof only used Lemma 1 for w). ∎

So (I.a) for the comb w is the statement "the direction of w lies in the closed cone ℝ·𝒦_T". The comb enters through a
direction; the archimedean form enters through the compact convex body 𝒦_T (independent of the comb).

Lemma 3 (PROVED, persistence). For all w, w': Θ_T(w') ≥ Θ_T(w) − |c*_T(w)|·‖w − w'‖_1, with c*_T(w) any maximiser.
Proof. Θ_T(w') ≥ Ψ_T(c*w') ≥ Ψ_T(c*w) − |c*|‖w − w'‖_1 = Θ_T(w) − |c*|‖w − w'‖_1 (Lemma 2's Lipschitz bound). ∎

Corollary 4 (PROVED). If Θ_T(Λ) > 0 then every finite modification of the window weights of ℓ¹-size < Θ_T(Λ)/|c*_T|
keeps Θ_T ≥ 0. Hence (I.a) can fail for all small finite modifications at a window T only if Θ_T(Λ) = 0, and then
Θ_T(Λ) ≥ λ_A(T) ≥ 0 forces λ_A(T) = Θ_T(Λ) = 0 under (★). Consequently,
wherever Θ_T(Λ) > 0, (I.a) survives small finite modifications and so does not pass falsifier test (d) of the brief (rule 4). (I.a) is a candidate separator
only at tangency windows, where the line ℝΛ touches 𝒦_T.

Correction to ROUND_002_D Corollary 3 (PROVED). The statement "Π(F*) = 0 iff c*_T = 1" assumes a simple bottom. In general,
for Hermitian forms on a finite-dimensional space (and on S_T whenever the bottom is an isolated eigenvalue of finite
multiplicity), the superdifferential of Φ_T at c = 1 is {−Π(F) : F a unit vector in the bottom eigenspace}, an interval
(Toeplitz–Hausdorff in that eigenspace). Hence c*_T = 1 ⟺ 0 ∈ [min, max] of Π on the bottom eigenspace. With a degenerate
(or nearly degenerate) bottom this can hold with Π(F*) ≠ 0 for the computed eigenvector F*, which is what is observed in §3.
Proof: Danskin's theorem for the minimum eigenvalue of an affine Hermitian pencil (CITED, standard perturbation theory). ∎

Remark (ARGUED). Θ_T is not monotone under deletion of a contact: deleting w_x replaces the cone {Π_w = 0} by {Π_{w'} = 0},
and neither contains the other. Lemma 2 gives the correct replacement: deletion moves the direction w to its coordinate
projection, and Θ_T ≥ 0 survives iff that projected line still meets 𝒦_T. Table §3 shows both outcomes occur
(T = log 2: survives; T ≥ ½log5: fails).

## 3. Computation (NUMERICAL)

Method. Orthonormal Dirichlet sines φ_k(t) = T^{−1/2} sin(kπ(t+T)/2T), k = 1..N (both parities), N = 20, 40, 80 (nested);
P_T imposed exactly in the span (null space of the 2 × N matrix of A, B by 800-point Gauss–Legendre). Arch matrix by midpoint
quadrature of (1/2π)∫ m φ̂_j φ̂_k on |τ| ≤ 6000, step 0.004 (φ̂_k closed form; orthonormality reproduced to 5·10⁻¹⁰); Π matrix
in t-space by 600-point Gauss–Legendre (agrees with the Fourier-side value to 10⁻¹²). Θ^{(N)} = max_μ λ_min(Arch − μΠ) on the
reduced space (grid on [−20, 20] then bounded Brent). Since each trial space is a subspace of S_T, Θ^{(N)} ≥ Θ_T and
λ^{(N)}_A ≥ λ_A: a NEGATIVE Θ^{(N)}, stable across N and far above quadrature error (≲10⁻⁹), proves Θ_T < 0 up to rounding; a
positive value proves nothing. Scripts: scratchpad p211/theta.py, run.py, lam.py (session scratchpad, not in the repo).

Combs on the window (positions log n < 2T): T₁ = ½log5 + 10⁻³ and T = 0.9 see n = 2,3,4,5; T = log 2 sees n = 2,3 only.
(b) delete 2 and 4; (c) delete 3; (d) Λ(2) → log 2 + η; (e) v_2 ↔ v_3; (f) atoms log 2, log 3.2, log 5 with weights
2log p/√p, p = 2,3,5. Values Θ^{(N)} / c* / λ^{(N)}_A(c=1) at N = 80 (N = 20, 40 in brackets for Θ).

T₁ = ½log5 + 10⁻³
| comb | Θ^{(80)} [20, 40] | c* | λ_A^{(80)} |
| (a) Λ | +3.8·10⁻⁹ [8.7·10⁻⁹, 4.1·10⁻⁹] | 0.9999999 | +3.1·10⁻¹² |
| (b) no 2 | −0.2680 [−0.2442, −0.2602] | −0.416 | −0.507 |
| (c) no 3 | −0.0986 [−0.0798, −0.0922] | +0.502 | −0.368 |
| (d) η=+0.1 | +0.00725 [stable] | 0.793 | −0.084 |
| (d) η=−0.1 | −0.0590 [stable] | 1.122 | −0.080 |
| (d) η=+0.5 | +0.0155 [0.0194, 0.0178] | 0.432 | −0.430 |
| (d) η=−0.5 | −0.2772 [−0.2546, −0.2695] | −0.595 | −0.408 |
| (e) swap | −0.00486 [+0.0020, −0.0024] | 0.579 | −0.240 |
| (f) 3 → 3.2 | −0.0843 [−0.0839, −0.0841] | 0.750 | −0.206 |
| empty | −0.3049 | — | −0.305 |

T = log 2
| (a) Λ | +6.5·10⁻⁵ [8.2·10⁻⁵, 7.0·10⁻⁵] | 0.99833 | +1.1·10⁻⁷ |
| (b) no 2 | +0.0533 | −1.055 | −0.436 |
| (c) no 3 | +0.0354 | 0.572 | −0.083 |
| (d) η=+0.1 | +0.0075 | 0.801 | −0.065 |
| (d) η=−0.1 | −0.0538 [−0.0529, −0.0535] | 1.050 | −0.055 |
| (d) η=+0.5 | +0.0205 | 0.451 | −0.336 |
| (d) η=−0.5 | −0.0186 [+0.0074, −0.0102] | −1.300 | −0.307 |
| (e) swap | +0.0199 | 0.606 | −0.133 |
| (f) 3 → 3.2 | +0.0078 [0.0190, 0.0117] (decreasing) | 0.757 | −0.125 |
| empty | −0.1501 | — | −0.150 |

T = 0.9
| (a) Λ | ≈ 0: Φ^{(80)}(1) = λ_A^{(80)} = 4.5·10⁻¹⁵, c* = 1 to 10⁻⁸ (optimiser returns −2.6·10⁻⁹, an artefact: Θ^{(N)} ≥ Φ^{(N)}(1)) | 1.0000000 | +4.5·10⁻¹⁵ |
| (b) no 2 | −0.4152 [−0.4014, −0.4106] | −0.203 | −0.526 |
| (c) no 3 | −0.3430 [−0.3254, −0.3366] | 0.372 | −0.590 |
| (d) η=+0.1 | −0.0241 [−0.0225, −0.0236] | 0.805 | −0.092 |
| (d) η=−0.1 | −0.0624 [−0.0619, −0.0622] | 1.100 | −0.090 |
| (d) η=+0.5 | −0.0771 [−0.0722, −0.0751] | 0.448 | −0.470 |
| (d) η=−0.5 | −0.4192 [−0.4050, −0.4146] | −0.149 | −0.458 |
| (e) swap | −0.1235 [−0.1173, −0.1210] | 0.609 | −0.266 |
| (f) 3 → 3.2 | −0.0971 [−0.0890, −0.0938] | 0.786 | −0.291 |
| empty | −0.4200 | — | −0.420 |

Bottom structure for Λ (NUMERICAL, N = 80): T₁: λ₁ = 3.1·10⁻¹², λ₂ = 6.5·10⁻¹⁰, Π(F*) = 0.062, Φ(0.9) = −0.026,
Φ(1.1) = −0.094. T = 0.9: λ₁ = 4.5·10⁻¹⁵, λ₂ = 2.3·10⁻¹⁴, Π(F*) = 0.046, Φ(0.9) = −0.039, Φ(1.1) = −0.112. T = log 2:
λ₁ = 1.1·10⁻⁷, λ₂ = 1.3·10⁻⁵, Π(F*) = 0.088, c* = 0.9983 < 1 (the sign predicted by the supergradient −Π(F*) for a simple
bottom). At T₁ and 0.9 the bottom is a near-degenerate pair and c* = 1 to 7–8 digits although Π(F*) ≠ 0: the correction to
Corollary 3 in action.

Rigorous content (NUMERICAL, up to rounding): Θ_T < 0 is established for (b), (c), (d η = −0.1, −0.5), (e), (f) at T₁; for
(d η = −0.1, −0.5) at T = log 2; for all of (b)–(f) at T = 0.9. Nothing is established for the positive entries.

## 4. Reading

1. (I.a) is sensitive to the falsifiers at T = 0.9: every modified comb tested, including both signs of a finite
   modification of Λ(2), has Θ_T < 0 (stable, margins 0.02–0.42), while Λ sits at Θ ≈ λ_A ≈ 0 with c* = 1. At T = 0.9 the
   true comb is (numerically) the only tested direction meeting 𝒦_T, and it meets it tangentially.
2. At T = log 2 (Θ(Λ) ≈ 6.5·10⁻⁵ > 0) and at T₁ for η > 0, (I.a) survives modifications, as Corollary 4 forces wherever
   Θ_T(Λ) > 0. So (I.a) is not a separator at every window; it separates only at tangency windows.
3. Tangency is self-consistent with the corpus near-degeneracy: at T₁ and 0.9, Θ_T(Λ) = λ_A(T) to the precision available.
   At such windows (I.a) carries no less information than (★) itself: Θ_T = λ_A. The split (I.a) ∧ (I.b) does not lower the
   bar there; it changes the object (an archimedean infimum on a quadric cone instead of the full window form).

## Result

PIVOT with reason: Candidate I is not NO-GO (it is not generic: Θ_T ≥ 0 fails, numerically-rigorously, for deletion of 2,
deletion of 3, the swap, the Beurling shift 3 → 3.2 and for finite modifications of both signs at T = 0.9), but by Lemma 3 it
can only separate at windows where Θ_T(Λ) = 0, and there Θ_T(Λ) = λ_A(T), so the statement to prove is not weaker than (★)
at that window.

## What was proved

- Lemma 1 (PROVED): every nonzero weight vector gives an indefinite Π_w on S_T.
- Lemma 2 (PROVED): 𝒦_T = {w : λ_A(T; w) ≥ 0} is compact convex and Θ_T(w) ≥ 0 ⟺ ℝw ∩ 𝒦_T ≠ ∅.
- Lemma 3 / Corollary 4 (PROVED): Θ_T is Lipschitz-persistent, Θ_T(w') ≥ Θ_T(w) − |c*|‖w − w'‖_1; (I.a) fails small
  finite modifications only at windows with Θ_T(Λ) = 0.
- Correction of ROUND_002_D Corollary 3 (PROVED): c*_T = 1 ⟺ 0 lies in the range of Π on the bottom eigenspace; with a
  degenerate bottom, Π(F*) ≠ 0 is compatible with c* = 1.
- NUMERICAL (upper bounds, rigorous up to rounding for negative values): table §3.

## What failed and why

- (I.a) as a universal sign step: survives finite modifications (and at T = log 2 also deletions, swap and the Beurling
  shift) wherever Θ_T(Λ) > 0, by Corollary 4; violates rule 4 at those windows.
- Monotonicity of Θ_T under deletion: false in both directions (survives at log 2, fails at T₁, 0.9); Lemma 2 replaces it.

## Next concrete step

Lemma to prove (OPEN), at T = 1 (and every T beyond the certified range where the bottom is degenerate):

    inf { (1/2π)∫ m(τ)|F̂(τ)|² dτ : F ∈ P_T, ‖F‖ = 1, Σ_{log n < 2T} (2Λ(n)/√n) Re c_F(log n) = 0 } ≥ 0,

i.e. the archimedean form (the Lévy form C_0‖F‖² + ∫_0^∞ (c_F(0) − Re c_F(u))K(u)du) is non-negative on the comb-null quadric
cone of P_T. Before attacking it: (i) compute Θ^{(N)}_1 and the bottom pair at T = 1 to confirm tangency (Θ_1 ≈ λ_A(1));
(ii) by the correction of Corollary 3, the useful structure is the two-dimensional bottom eigenspace E_T on which Π changes
sign; the concrete target is to identify E_T (a pencil Arch − Π with a degenerate bottom whose Π-range straddles 0) by a
mechanism that uses the exact values Λ(n), since every perturbed comb tested at T = 0.9 lost the degeneracy and Θ.
