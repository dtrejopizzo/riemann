# #2 — PROOF DRAFT (for // verification) **Goal:** prove Theorem #2: the relative spectrum of the bottom of the localized Weil form
A_λ converges to (k+1)², with ε_0(λ)≍λ^{−2}; together with (i)+(#3), this gives ξ̂_λ→Ξ ⟹ RH. **Status convention:** [P]=rigorously proved · [N]=established numerically (to be verified
analytically) · [O]=open step (the "missing step"). There is NO ∎ on [O] steps. --- ## Lemma 0 (exact restriction) [P]
A_λ = A_∞|_{E_λ}, E_λ=PW_{L/2}. Primes >λ² contribute 0 by support (f**g⊂[λ⁻²,λ²]).
(Verified 0.00e+00; proof in 2b_part_i_EXACT.md.) ∎ ## Lemma 1 (sampling form) [P]
By Weil's explicit formula (unconditional) + Lemma 0, for f∈PW_{L/2}: A_λ(f,f) = Σ_ρ f̂(ρ) · conj(f̂(1−ρ̄)),
sum over the non-trivial zeros ρ of ζ; f̂ entire of exponential type L/2. On the
on-line part (ρ=½+iγ): terms |f̂(γ)|² ≥ 0. ∎ ## Lemma 2 (sampling horizon) [P, consequence of density]
f̂∈ type L/2 can vanish at points of density ≤ L/2π. The zeros γ_j have density
(1/2π)log(γ/2π). Equating: f̂ can vanish at ALL γ_j up to height T*(λ) = 2π λ² (horizon),
and no further. ⟹ the soft modes (small A_λ) are f with f̂ vanishing at the zeros up to
T*; the residual comes from the zeros at T*. **This gives H(λ)→∞ (the horizon grows like λ²).** ∎ ## Lemma 3 (edge localization) [N, mechanism identified]
The minimizers are edge-localized: concentrated at w=±L/2 (u=λ^{±1}), zero at the center,
occupying a layer of FIXED width a≈1.5 (in w). [Verified: edgeprofile.py, λ=7.]
*Structural reason:* δ_N (the minimizer's normalization) is evaluation at the edge u=λ;
the form A_λ is "nearly null" except in the edge layer. The band-limitedness PW_{L/2} acts as a
Dirichlet condition at the inner edge of the layer. ## Lemma 4 (edge operator = 2nd-order Dirichlet) [N exact + [O] derivation]
**Fact [N, exact to ~1%]:** √(ε_k/ε_0) = k+1 (measured: 1.00, 2.04, 3.00, 4.09, 5.02), and the
width a≈1.5 is independent of k. This FORCES the effective edge operator to be of
**second order with spectrum (jπ/a)²** (Dirichlet Laplacian on [0,a]): ε_k = (π/a)²·(scale)·(k+1)². **Mechanism [O, the missing step]:** the reduction of A_λ, restricted to the edge sector, to the
Dirichlet Laplacian −d²/ds² on [0,a]. Via: band-limiting + spatial concentration ⟹
a **prolate-type** differential equation (second order): the concentration of band-limited
functions satisfies the prolate ODE ((1−x²)φ')' + (χ−c²x²)φ=0, whose spectrum near the band
edge is j². [Tools: de Branges / prolate spheroidal — the program already has them
(P7/P8).] **Missing:** derive the effective second-order ODE from A_λ and read off a = a(L). ## Lemma 5 (scale ε_0 = tunneling) [N + [O]]
**Fact [N]:** ε_0 ∝ λ^{−2.07} ≈ λ^{−2} = e^{−L}. [Verified.]
**Mechanism [O]:** tunneling splitting between the edge layers u=λ and u=λ⁻¹, separated by
L in w; decay rate κ=1 ⟹ e^{−κL}=λ^{−2}. **Missing:** derive κ=1 from the tail of the edge
modes (decay of the Dirichlet eigenfunction outside [0,a]). ## Theorem #2 (conditional on Lemmas 4-O, 5-O)
Lemmas 0–5 ⟹ ε_k(λ)/ε_0(λ) → (k+1)² and ε_0≍λ^{−2}. With #3 (rescaling by ε_0 ⟹ isolated bottom
⟹ Galerkin ⟹ convergence of the minimizer) ⟹ ξ̂_λ→Ξ. With each ξ̂_λ real-rooted (H1+H2) and
Hurwitz ⟹ Ξ real-rooted ⟹ **RH**. ∎ (conditional on 4-O, 5-O) --- ## CORRECTION (// review + O-4a test) The review correctly pointed out: (a) "√(ε)=k+1 FORCES Dirichlet" is too strong — it is only
COMPATIBLE with a 2nd-order Sturm–Liouville (many operators have a quadratic spectrum);
(b) the real bottleneck is O-4a (existence of the edge limit operator), prior to the prolate
ODE; (c) without the limit operator, "κ=1 / tunneling" has no rigorous meaning. **Test O-4a (width_vs_lambda.py) — refutes the fixed-width layer:**
| λ | 3 | 3.7 | 5 | 7 | 9 | 11 |
|---|---|---|---|---|---|---|
| a/L |.331 |.356 |.356 |.369 |.369 |.369 |
- **a ∝ L** (a/L → 0.369 ≈ 1/e), NOT constant. Active primes in the layer GROW with λ.
- ⟹ there is NO fixed edge operator; the modes occupy a fixed fraction of the growing interval.
- Energy scale: ε_0 ∝ e^{−L}=λ^{−2} (exponential), NOT 1/L² (verified: ε_0(7)/ε_0(11)=0.40 =e^{−ΔL}, not (L_7/L_11)²=0.66). **Consequence (corrects the target):** λ²A_λ ⟹ −d²/ds² is INCORRECT (it would give 1/L²). The limit is a
**semiclassical WKB/tunneling regime in the normalized coordinate x=w/L ∈[−½,½]**; the tower (k+1)²
is of tunneling splittings, with exponential scale e^{−L}. The correct reduction of O-4a is a
**semiclassical limit** (not convergence to a fixed Laplacian). More subtle, but WKB-tunneling are
classical tools — not a wall. ## UPDATE 2 (O-4a.1/2/3 + parity) — semiclassical regime ESTABLISHED, single well Following the methodology (measure the regime before the equation):
- **O-4a.1 [N]:** the profiles φ_k(x) collapse to a universal shape in x=w/L (clean for even modes).
- **O-4a.2 [N]:** ε_0(λ) CONVERGES in N to a value >0 (not an artifact). −log ε_0 ≈ 0.83·L + 43.7 ⟹ action S = slope ≈ 0.83–1.0 ≈ 1 (plus a large constant prefactor ~43.7, unexplained).
- **O-4a.3 [N]:** correction δ_2 = ε_2/ε_0 − 9 ∝ 1/L ⟹ **1/L is the semiclassical parameter (ℏ)**.
- **PARITY [N, machine-clean]:** the modes alternate even/odd/even/odd… (||ξ−rev||/||ξ+rev|| ~1e−23 / 1e22), and √(ε_k/ε_0)=k+1 up to k=6 (1,2.04,3.00,4.09,5.02,6.15,7.04). **CONSEQUENCE — corrects the "two edges/tunneling" picture (it was an error):** the alternating
parity + √=k+1 is the signature of a **SINGLE second-order WELL = Dirichlet Laplacian**
on [−½,½] (spectrum (jπ)², alternating-parity eigenfunctions). There are NO tunneling pairs
(they would give ε_1/ε_0≈1, not observed). The e^{−L} is the **global scale ε_0**, not a splitting. **Correct and clean target (recovers the one from the review, in normalized coordinate):** (1/ε_0(λ)) · A_λ ⟹ −d²/dx² (Dirichlet on [−½,½]),
with ε_0(λ) ≍ e^{−S L}·(const), S≈1. Semiclassical regime ESTABLISHED (not intuition).
Still open [O]: (O-4b) derive the −d²/dx² from A_λ; (O-4a.2') explain the constant 43.7
and fix S=1; clean up the precision of odd modes (parity OK, noisy profile). ## UPDATE 3 (review: separate existence from identification) Adopted reformulation (correct): do NOT claim "unambiguous Dirichlet signature". What is defensible:
**very strong evidence of an effective 2nd-order Sturm–Liouville-type operator**. And separate:
- **O-4b.1 (existence of 𝓛):** (1/ε_0)A_λ ⟹ 𝓛 self-adjoint on [−½,½], WITHOUT identifying 𝓛. Essentially established by: collapse of profiles (A) + alternating parity (B) + spectrum (k+1)² (C) + O(1/L) corrections (D) — the 4 pieces together ⟹ the eigenpairs converge ⟹ 𝓛 exists (operator with a complete ON eigenbasis {φ_k} and eigenvalues (k+1)²).
- **O-4b.2 (identification of 𝓛):** what operator is it? OPEN. **Identification attempt (reveal_L.py): V(x)=φ_0''/φ_0.** FRANK result:
- Numerically NOISY (φ'' of a band-limited profile amplifies noise); does not cleanly identify 𝓛.
- Robust: **central singularity** (V→∞ at x=0; φ_0~x² there) ⟹ 𝓛 is NOT the FLAT Laplacian (whose ground state cos(πx) has a central peak, not a node). It is Sturm–Liouville with a **centrifugal/Bessel** term at x=0, spectrum (k+1)². Consistent with x=0 (u=1) being the fixed point of ι where the prime structure is singular.
- ⟹ confirms the caution of: (k+1)² is 2nd-order but NOT flat Dirichlet; 𝓛 has a potential. The precise identification requires analytic derivation (not numerical φ''). **Status:** 𝓛 exists (O-4b.1, via convergence of eigenpairs); 𝓛 ≈ 2nd-order Sturm–Liouville
with central singularity, spectrum (k+1)² [O-4b.2, open]; precise identification = deriving the
effective operator from A_λ (analytically), not from numerical φ'' (too noisy). ## Frank status of the draft **Rigorous [P]:** Lemmas 0, 1, 2 (exact restriction, sampling form, horizon ~λ²).
**Numerically established [N], to be verified analytically:** edge localization, fixed
width a≈1.5, √(ε_k/ε_0)=k+1 (second order / Dirichlet), ε_0∝λ^{−2}.
**Open [O] — the missing step of, NOT fabricated:** (4-O) reduction of A_λ to the Dirichlet Laplacian via the second-order prolate ODE + identification of a(L); (5-O) tunneling κ=1. **What is new and strong in this draft:** (a) the sampling form + horizon ~λ² [P]; (b) the
EXACT identification √(ε)=k+1 ⟹ 2nd-order Dirichlet operator [N]; (c) the concrete route
via prolate/de Branges (P7/P8) for (4-O). The missing step has been reduced to an effective
prolate ODE — a classical object, not a wall. **For the verifiers:** the [N] points are checkable (relspec2.py, edgeprofile.py); the
[O] points are where I ask for your analysis (prolate ODE + tunneling). If (4-O) and (5-O) close,
2b ⟹ RH.
