# Round 030 B — Divisor chains, low-frequency spectral mass and primitivity in (PBP_T)

Object: `𝔈(Φ) = C_0 + ∫_0^∞ (1 − Φ)K` over positive-definite `Φ`, `Φ(0) = 1`, `supp Φ ⊂ [−2T, 2T]`,
`Φ(log n) = 0` (`2 ≤ n < e^{2T}`), with the two conditions of `eq:Kprim` (P46, l. 453–476, cross-checked:
`∫Φ cosh(u/2) = 0`, `∫Φ u sinh(u/2) = 0`). With `Φ = μ̂`, `μ ≥ 0` of mass 1: `𝔈 = ∫ m dμ`,
`m(τ) = Re ψ(¼ + iτ/2) − log π` (identity checked at `τ = 3` to 1e−13; script below).

## Cross-check

1. **Closest antecedent.** ROUND_026_B §§2–4 (Kreĭn + gaps; ceiling 3.0–3.4; §4 "Controls" already
   records the orthogonality `ξ_{log m} ⊥ ξ_{log n}` if `n | m` as "not exploited, shared by every Beurling
   system"); R160_M2_R1 D4–D5, Thm 4.1 (duality: the dual of `Z^prim_T` is the free-weight problem
   `K_T`); R155_033 §2.2 ("τ = 0 cap"); P46 `rem:Kprim` (primitivity in terms of `Φ̂(±i/2)`); 212-26-A.
2. **What would be new.** (i) To see whether divisibility chains give constraints *beyond* the linear ones
   `Φ(log n) = 0`; (ii) an explicit bound on the mass of `μ` in `|τ| ≤ τ_0` and on `𝔈` by pushforward to the circle;
   (iii) the reading of primitivity on `μ`.
3. **Why it would avoid the antecedent.** ROUND_026_B uses (K1)–(K2) on the `u` side; here one works on the
   `τ` side, where the singularity `K ~ 1/u` is the growth `m ~ log|τ|`, and multiplicativity enters through
   periodicity.
4. **Global connection.** A uniform `𝔈 ≥ −δ` would be a step towards (PBP_T); (PBP_T) ∀T → `K_T ≠ ∅` ∀T, and from there to the
   true weight only CONDITIONAL (212-25).

Prior grep ("divisib", "chain", "orthonormal", "Selberg", "pushforward") in the index: only NG-110, P74–P75,
INV_H_001, the projection `Π_m` (Part V, 2026-11-07) and the note of ROUND_026_B; none is this computation.
Conclusion in advance: (i) is an exact repetition of the linear dual (§1); (ii) is new as a count and gives a
PROVED but negative bound with a PROVED ceiling (§2); (iii) is already in P46 (§3).

## 1. Divisor chains add no constraints (PROVED)

In the GNS space, `⟨ξ_{log m}, ξ_{log k}⟩ = Φ(log(k/m))`. Orthogonality for `m | k`, `m ≠ k`, is
*literally* `Φ(log(k/m)) = 0` with `k/m ∈ ℕ_{≥2}`: the divisibility graph is the list of contact
constraints, nothing more. For multipliers `f = |Σ_{n∈C} a_n n^{−iτ}|²` over a chain `C`:
`∫ f dμ = Σ|a_n|²` and the bound `𝔈 ≥ inf_τ [m + λ(f − ‖a‖²)]` uses
`f − ‖a‖² = Σ_{j≠k} a_j ā_k (n_k/n_j)^{iτ}`. Summing several `(λ_i, a_i)`, what appears is the off-diagonal part of
a semidefinite matrix `G`; since every Hermitian `H` with zero diagonal is the off-diagonal part of
`H + cI ⪰ 0`, the resulting class is **exactly** `m(τ) − Σ_d w_d cos(τ log d)` with real `w`
of free sign supported on the quotients of the chain, i.e. a free-weight certificate (dual of
R160 Thm 4.1), moreover pointwise in `τ` (without using the support `[−2T,2T]`). So the positivity of `|·|²` is
lost in the closure and line (a) **is contained in `K_T`**: repetition. What GNS does not fix are the
products `⟨ξ_{log 2}, ξ_{log 3}⟩ = Φ(log 3/2)`, free; the semigroup (not group) structure of `log ℕ`
appears only as "constraints on the positive quadrant" (§2.3).

## 2. Pushforward to the circle by one generator: explicit bound

**2.1 Monotonicity (PROVED).** `Re ψ(a+iy) − ψ(a) = Σ_{k≥0} y²/((k+a)((k+a)²+y²))`, each term increasing in
`|y|`; hence `m` is even, increasing in `|τ|`, with root `τ_* = 6.28984` (NUMERICAL). Therefore
`𝔈 = C_0 + ∫_0^∞ m′(s) μ(|τ| > s) ds`, `m′ ≥ 0`.

**2.2 Theorem (PROVED, with Selberg CITED).** Let `J = ⌈2T/log 2⌉ − 1` (number of `j ≥ 1` with `2^j < e^{2T}`),
`L := π/log 2 = 4.5324`. If `Φ(j log 2) = 0` for `1 ≤ j ≤ J`, then
```
𝔈(Φ) ≥ M_2 − (m(L) − C_0)/(J+1),   M_2 := (1/L)∫_0^L m(τ)dτ = −1.4979,   m(L) − C_0 = 5.0434.
```
Proof. The pushforward `ν` of `μ` by `τ ↦ τ log 2 mod 2π` has Fourier coefficients `ν̂(j) = Φ(j log 2) = 0`
for `1 ≤ |j| ≤ J`. The Selberg majorant of degree `J` of an arc of length `ℓ` has mean
`ℓ/2π + 1/(J+1)` (CITED), hence `μ(|τ| ≤ s) ≤ ν(arc 2s log 2) ≤ s/L + 1/(J+1)` for `s ≤ L`. With `m′ ≥ 0`:
`𝔈 ≥ C_0 + ∫_0^L m′(s)(1 − s/L − 1/(J+1)) ds`, and integrating by parts `= M_2 − (m(L) − C_0)/(J+1)`. ∎
With `T → ∞`: `𝔈 ≥ −1.4979`. Likewise with generator `n`: `M_3 = −2.057`, `M_4 = −2.358`, `M_5 = −2.559`
(NUMERICAL); the best is `n = 2`.

**2.3 Ceiling of the method (PROVED).** The uniform measure on `[−L, L]` has `Φ(u) = sin(πu/log 2)/(πu/log 2)`,
which vanishes at every `j log 2` and gives `𝔈 = M_2` exactly: the bound is optimal for the data of a single
generator. Combining generators via the pushforward to the torus `(τ log 2, τ log 3)` only kills coefficients in
`ℤ²_{≥0} ∪ ℤ²_{≤0}`; the mixed ones `(j, −k)` (quotients `2^j/3^k ∉ ℕ`) remain free and a measure concentrated
near `θ_1 = θ_2` respects them. Moreover `|τ| ≤ τ_*` covers more than one period `2π/log p` for every prime
`p` (`log p ≥ 0.5 > π/τ_*`), so **no pushforward by a single generator bounds the mass on all of
`|τ| ≤ τ_*`**: the mass is only controlled on `|τ| ≤ π/log 2`. What is missing (`1.498`) has to come from the
interaction of distinct generators, which is the full linear problem `K_T` (§1). ARGUED: there is no
"torus" version that improves §2.2 without redoing that dual.

## 3. Primitivity on μ

`μ` has density `μ′ = Φ̂/2π`, entire of type `2T`. The two conditions are
`Re Φ̂(i/2) = 0` and `Re[i(Φ̂′(i/2) − Φ̂′(−i/2))] = 0` (P46, l. 472–476, CITED; with `F ∈ P_T`, `Φ̂` vanishes to
order 2 at `±i/2`). They are not functionals `∫ g dμ` with bounded `g`: they act on the analytic continuation of
the density and only make sense together with the type constraint (support `[−2T, 2T]`). The bound of §2.2 uses
neither the type nor primitivity; the example of §2.3 satisfies them only if a correction is added (the
uniform measure is not of finite type). In the dual, both are the pole terms of P46 `thm:A`/`eq:Kprim`: already
present (repetition). I did not find how to turn them into a bound on low-frequency mass: OPEN.

## 4. Test bench (extremal state of ROUND_028_A)

Frequency `≈ 6.7`: `m(6.7) = +0.063` (NUMERICAL), just above `τ_*`. Its `μ` is outside
`|τ| ≤ L`, so §2.2 does not restrict it and does not forbid it either (the bound is negative). Compatible. It shows
moreover where the real difficulty is: the extremal state avoids the zone controlled by generator 2 and lives
in `L < |τ| < τ_*`-ish, where `m ∈ (−0.33, 0)`; its `Φ` changes sign at `log n` (`n ≤ 13`) instead of
vanishing on a simple arithmetic lattice.

## 5. Controls

- Integers coprime to 2: the best generator becomes 3 and the bound drops to `M_3 = −2.057`; the argument does not
  change form. Beurling system with one generator `g`: same bound with `L = π/log g`.
- Named step that uses `log ℕ`: only "there is a generator `g` with all its powers in the set"
  (§2.2). Every multiplicative semigroup shares it; the exactness of `log ℕ` **is not used**. §1 does not use it
  either (the divisibility graph is that of any semigroup). By the filter rule: selection NO-GO
  for (a) as a sign mechanism.
- Falsifiers with weight (`cΛ`, `a_P`, deletions, Davenport–Heilbronn, …): (PBP_T) carries no weight; §2 does not
  distinguish any of them because it contains no weight.

## Result

**Small PROVED piece + selection NO-GO.** (a) divisor chains are exactly linear constraints
already contained in the free-weight dual (R160 Thm 4.1): repetition. (b) primitivity = P46
`rem:Kprim`, not turned into a mass bound: OPEN. New bound: `𝔈 ≥ −1.4979 − 5.0434/(J+1)` with `J` the number
of powers of 2 in the window, optimal for one-generator data (ceiling `−1.4979`).

## What was proved

Monotonicity of `m`; the bound of §2.2 and its optimality §2.3; the reduction §1 (closure = free weight).

## What failed and why

`1.498` is missing (one-generator ceiling) relative to 0; the deficit of ROUND_026_B (≈ 2 relative to 5.372) and this one
are the same wall seen from both sides: the mass in `π/log 2 < |τ| < 6.29`, where no isolated generator
controls anything and the information lies in the interaction of non-integer (free) quotients.

## Concrete next step

Use the type `2T` (entire density) together with order-2 primitivity at `±i/2` to bound
`μ(L < |τ| < τ_*)`: a Paley–Wiener-type inequality with prescribed zeros at `±i/2`. Before that, grep in
phases 155/160 for "Paley–Wiener" and "prescribed zeros".

Script: `free_weight_scripts/chain_mean_030B.py` (root of `m`, means `M_n`, check of `m`).
