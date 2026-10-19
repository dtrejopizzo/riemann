# R162_2701 — The 2×2 Tate transfer canonical system (O8, cell 4E)

Cell **4E** (Euler × flow in T). Nearest routes: phase-61 OPEN-PROBLEMS O8, RH-PROOF-PAPER 11.3-ter;
R160_S2 §3.2 (index collapse κ₀+|S|→0); grid §6 items 12, 47. Target residual: O2601.1 (R162_2601 §6).
Status: **NO-GO (PROVED)**. Tools Thm TC, Thm P and Thm I are PROVED and RH-neutral. No sign is claimed. Gate 1 remains OPEN.

## 0. Falsifier lines first

The object is the phase-61 local Tate transfer, with s = ½ − iz and ℓ_p = log p:

  T_p(z) = (1−1/p)^{−1/2} [[1, −p^{−s}], [−p^{−(1−s)}, 1]],   J₃ = σ₃,  T_p(x)* σ₃ T_p(x) = σ₃ on ℝ.

The table below is proved in §2–§3.

| falsifier | is H_S defined? | H_S ≻ 0? | H_S the same as for ζ? |
|---|---|---|---|
| deletion (remove primes) | yes | yes (Thm P) | no, but same class |
| M_m = ξ·(rational) | yes (same primes) | yes | **identical** (Thm I) |
| Λ̃ (atomic, non-log-derivative weights) | yes (reflection r_x = tanh w_x) | yes | same class |
| two-atom curve | yes | yes | same class |
| Beurling DMV | yes | yes | same class |
| Λχ₂ | yes (r_p = χ(p)p^{−1/2}) | yes (general formula) | same class |
| DH | only as a sum of two chains, which has no product | — | — |

The system does not detect any falsifier. DH is excluded only by hypothesis (it has no local factors), not by any property of H_S.

## 1. Structure lemma: each T_p is a conjugated boost

Let E_ℓ(z) = diag(e^{izℓ/2}, e^{−izℓ/2}) (free propagation) and C_p = cosh θ_p · I − sinh θ_p · σ₁, where tanh θ_p = p^{−1/2}.
Then **T_p = E_{ℓ_p} C_p E_{ℓ_p}^{−1}**. Direct check: the (1,2) entry is −cosh θ_p · tanh θ_p · e^{izℓ_p} = −(1−1/p)^{−1/2} p^{−1/2+iz}. PROVED.

Consequences:
- The z-dependence of T_p is pure conjugation by free propagation. Its spectrum {(1 ± p^{−1/2})(1−1/p)^{−1/2}} does not depend on z.
- The Euler factor appears only in the Tate vector e = (1,1)ᵀ: T_p e = c_p (ζ_p(s)^{−1}, ζ_p(1−s)^{−1})ᵀ.
- T_q e is not proportional to e, so the ordered product T_S does not carry ζ_S(s)^{−1} as an entry or as an eigenvalue. The "product of local Euler factors" does not survive as a 2×2 product.

## 2. Theorem TC: the explicit Hamiltonian (answers (a))

Order S = {p₁ < … < p_n} and write ℓ_k = log p_k. Telescoping gives

  T_S = ∏_k E_{ℓ_k} C_k E_{−ℓ_k} = M_S(ℓ_n) · E_{−ℓ_n},   M_S(x) = E_{ℓ₁} C₁ E_{ℓ₂−ℓ₁} C₂ ⋯ C_k E_{x−ℓ_k} on [ℓ_k, ℓ_{k+1}).

**Gauge.** Let G(x) = C₁⋯C_k for ℓ_k ≤ x < ℓ_{k+1}, and set N = M_S G^{−1}.
- N is continuous: the jump C_k is absorbed by G.
- N solves **N′ = z N J^{−1} H_S(x)**, with J = −iσ₃, N(0) = I.
- H_S(x) = ½ (G(x) G(x)*)^{−1}. This uses σ₃ G σ₃ = G^{−*}, which follows from the σ₃-unitarity of G.
- All C_p are σ₁-boosts, so they commute, and G = exp(−Θσ₁). This gives

  **H_S(x) = ½ exp(2Θ(x) σ₁) = ½ [[cosh 2Θ, sinh 2Θ], [sinh 2Θ, cosh 2Θ]]**, where

  Θ(x) = Σ_{p ≤ e^x, p∈S} artanh(p^{−1/2}) and e^{2Θ(x)} = ∏_{p≤e^x} (1+p^{−1/2})/(1−p^{−1/2}) = ∏_{p≤e^x} ζ_p(½)²/ζ_p(1).

PROVED. This is a Dirac–Krein system with potential Θ′ = Σ θ_p δ_{log p}. Its properties:
- det H_S = ¼ and tr H_S = cosh 2Θ.
- As S grows to all primes, Θ(x) ~ 2e^{x/2}/x. So ∫ tr H = ∞ and the system is limit point.

**Answer to (a).** Yes, H_S is explicit, but the arithmetic enters only through two things:
1. the positions log p;
2. one z-independent monotone function Θ. Its expansion is Σ_{p, k odd} p^{−k/2}/k: only primes appear, even prime powers are absent, and the Euler product is evaluated at the fixed point s = ½.

The nonlinearity (exp 2Θ) is a nonlinearity in the central Euler product at one point, not in the local factors as functions of z. The non-commutativity of the chain comes only from the free propagation E, which contains no arithmetic.

## 3. Theorems P and I (answers (b))

**Thm P (positivity).** For any sequence of positions x_k and σ₃-unitary jumps C_k, H = ½(GG*)^{−1} ≻ 0. The complex-χ case has non-commuting boosts and is covered by the same formula. Therefore N_S is J-inner, with Pontryagin index 0, exactly. PROVED.

**Index remark.** The phase-61 index κ₀+|S| belongs to the free back-propagation factor E_{−ℓ_n}, which contains no arithmetic. The kernel chain rule K_{AB} = K_A + A K_B A* gives

  ind_−(K_{T_S}) ≤ ind_−(K_{E_{−ℓ_n}}) = ∞ (the negative Paley–Wiener kernel).

So the finite count reported on a grid is a discretization artefact and was never certified (R160_001 D11). After right-normalizing by E_{ℓ_n}, κ = 0 for every S. The route "wall = collapse κ₀+|S|→0" therefore has no content: the index is 0 after normalization and ∞ before it, and neither value depends on the zeros.

**Thm I (M_m-invariance).** H_S is a function of the prime set alone. M_m = ξ × rational factor has the same primes as ζ, so it has the **identical** H_S, yet it has m off-line zeros. PROVED (immediate from Thm TC).

**Answer to (b).** Positivity and trace normalization of H_S are case **(ii)**: weaker than E1, provable, and RH-neutral. They are **not** (i) E1 and **not** (iii) a candidate for O2601.1.

## F1. Deletion

The deleted system is again a boost chain, and H ≻ 0 by Thm P. Suppose the spectral measure of the full-S Hamiltonian were the zero set. Then deletion, which has off-line zeros, would contradict the fact that a canonical system with H ≥ 0 has real spectrum. Hence the spectrum of H_S is not the zero set, for ζ or for any falsifier. Any identification of the two would need an extra ingredient that fails for deletion, and H_S contains no such ingredient.

## F2. M_m and Λ̃

- M_m gives an identical H_S (Thm I).
- For Λ̃, set r_x = tanh w_x for arbitrary positive atoms. This gives a system of the same form with H ≻ 0.

Therefore no functional of H_S can bound the off-line count while failing for M_m. O2601.1 requires exactly such a property.

## M. Mechanism and verdict

The Tate 2×2 transfer factors as free propagation, which is J-inner, times z-independent hyperbolic rotations, which are gauge. Everything z-dependent carries no arithmetic, and all the arithmetic is z-independent. This is the trilemma of W12 (exact structure without a sign) in its cleanest form: the positive object exists, but it is blind to the zeros.

**NO-GO (PROVED).** O8 is closed and grid §6 items 12 and 47 are absorbed. For cell 4E, this removes the residual "O8 / S2 §3.2"; the other three 4E residuals are unaffected. O2601.1 remains live, with no candidate. Any future Tate-type construction must make the arithmetic z-dependent in a way that is not gauge. For example, the Tate vector e would have to be propagated by a non-J-unitary diagonal factor diag(ζ_p(s)^{−1}, ζ_p(1−s)^{−1}), which is J-unitary only up to the scalar |ζ_p|^{−2} on ℝ. That is the scalar HB route already shown dead in O8.
