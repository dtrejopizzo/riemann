# Round 22, memo A — «Undoing the sum»: a single object?, and the Möbius congruence on 𝔸_M

Notation of P47 and of round 7. `S_N = Σ_{n≤N} n^{−1/2}τ_{log n}`, `S_ζ = S_∞` (R160_D4_R2 §3),
`Φ_G` Mellin transform in the convention of P46 (`Φ_{G⋆H} = Φ_GΦ_H`), `𝒩` the radical of P46 thm:radical,
`𝒲` the full form on the line (P47, definition preceding lem:ext-mob). Lattice: P47 prop:AM (main.tex l.7811),
`𝔸_M = Arch_M − Div_M − Near_M`, `Div_M = Δ + Δᵀ`, `Δ_{mk} = 1_{k|m}Λ(m/k)(m/k)^{−1/2}` (normalization correction
recorded in N_BUILD_022 §2).

## Four-point filter

1. **Closest antecedents (read in primary sources).**
   Part 1: `phase-160-row-d-infinite-T/R160_D4_R2.md` Theorem 4.3 (the image `S_ζh` of tests with `Φ_h(1) = 0` lies in the
   kernel of `𝒲`; the Poisson term `Φ_h(1)e^{−t/2}` decides admissibility) and Theorem 5.1 (a line that enters
   through a Dirichlet convolution identity on tests is not the one carrying the sign); P46 thm:radical
   (`𝒩 = {Φ_N(0) = Φ_N(1) = 0, Φ_N(ρ) = 0}`, ideal for `⋆`); P47 lem:ext-mob, thm:ext-half, rem:ext-killing,
   prop:ext-gauge (l.9899–9960; Guo Lemma 4.4); `phase-161-row-d-sum-product-square/R161_001` Theorems 2.1, 3.1 (PC), 4.1;
   `R160_M4_R1` Theorem A, C; `ROUND_020_B` §4.2; `ROUND_021_A` §3(c).
   Part 2: `phase-188-closing-D/N_BUILD_022` §§1–3 (matrix `Z`, `ZΔ = [L, Z]`, NO-GO for Near);
   `phase-162-.../R162_903` Theorem 3.2 (terminating BCH, `log Z = M_T(Λ/log)`), Theorem 4.1 (Sylvester collapse under
   unitriangular congruence, valid for Λχ₂, Beurling, deletions), Theorem 4.2 (Moore), §8 (residue: the exact step
   «must not be invariant under integral unipotent congruence»); `R162_1003` Cor. 4.3 (every representation `Z*DZ` with `Z`
   unipotent is a congruence); `ROUND_004_A` (R4-a, R4-b), `ROUND_004_C` (R4-d); L2_BUILD_028 §2(c).
2. **New.** Nothing that passes the filter. Two pieces of writing: (a) the unified statement (U) of Part 1 as an
   explicit corollary of existing citations, with the observation `K_Pó = S_ζ g_0` (Gaussian profile); (b) the closed
   Λ-free formula of `Zᵀ Div_M Z` (Lemma 2.1).
3. **Why it does not avoid the difficulty.** The congruence of Part 2 is exactly the class closed by R162_903 Thm. 4.1
   and R162_1003 Cor. 4.3; the Near block is not touched (N_BUILD_022 §3). See Part 3.
4. **Connection with global positivity.** `𝔸_M ⪰ 0 ⟺ Zᵀ𝔸_M Z ⪰ 0` (Sylvester); no new inequality.

**Verdict of the cross-check: repetition in both parts.** The precise statement requested and what remains different follow.

## Part 1 — A single object?

**Observation 1.1 (PROVED, direct computation).** With `g_0(t) := (2π²e^{9t/2} − 3πe^{5t/2}) e^{−πe^{2t}}`,
`n^{−1/2}g_0(t + log n) = (2π²n⁴e^{9t/2} − 3πn²e^{5t/2})e^{−πn²e^{2t}}`, hence `K_Pó = S_ζ g_0` (Riemann–Pólya series) and,
since `S_ζ` commutes with translations and derivatives, `M = (−∂² + ¼)K_Pó = S_ζ g`, `g := (−∂² + ¼)g_0`; `M∗φ = S_ζ(g∗φ)`.
`Φ_{g_0}(s) = ½s(s−1)π^{−s/2}Γ(s/2)` (convention of P46 Def–Thm 11.7, ARGUED in the normalization of constants).
Thus the family of R160_M4_R1 / ROUND_021_A is an image of `S_ζ`. The gauge is an image of the same sum: P47 l.9877,
`Φ_φ` with Mellin `ζ(s)𝓜φ(s)`, `Φ_φ(x) = e^{−x/2}Σ_{k≥1}𝓕φ(ke^{−x})`.

**Lemma (U) (CONDITIONAL only in the verification of domains; content CITED).** Let `h` with `S_ζh ∈ D_W` and
`Φ_h` holomorphic in a strip containing `0 ≤ Re s ≤ 1`, with `ζ(s)Φ_h(s)` vanishing at `s = 0` and `s = 1`. Then
`S_ζh ∈ 𝒩` and `𝒲(S_ζh, G) = 0` for every `G ∈ D_W`.
*Proof.* For `Re s > 1`, `Φ_{S_ζh} = Σ_m m^{−s}Φ_h = ζΦ_h` (R160_D4_R2 Lemma 3.1(a)); continuation; it vanishes at each
`ρ` and at `0, 1` by hypothesis; P46 thm:radical. ∎ Cases: `h = g∗φ` (family of `M`), `h = φ ∈ 𝒢_T` on the multiplicative side
(Guo Lemma 4.4 / prop:ext-gauge), `h = c_F` with `F ∈ P_T` (R160_D4_R2 Thm. 4.3(c), identity (C′′)).

**What distinguishes the input classes (PROVED except where indicated).** Radicality does NOT distinguish: the same lemma
(explicit formula on a Mellin divisible by ζ) serves for all. Hence the claim of ROUND_020_B §4.2
«the radical of `M` uses the functional equation and that of the gauge does not» is inaccurate as a statement about radicality: in
both cases the proof is P46 thm:radical, whose geometric side already contains Euler, FE and Γ. What is correct
is `M ∉ 𝒢_T` (support). What distinguishes the inputs is **where `S_ζh` lives relative to the window**:
- compactly supported `h` (gauge; R160_D4_R2 Thm. 4.3(a)): `S_ζh` vanishes exactly on one side and on the other is
  `Φ_h(1)e^{−t/2} + O(e^{Nt})` by Poisson: the Poisson defect is the polar term.
- Gaussian `h` (self-dual under Fourier): by theta inversion `S_ζh` decays doubly-exponentially on both sides;
  truncating to `[−T, T]` costs `e^{−πe^{2T}}` (R160_M4_R1 Thm. A/C). This is the only input in which
  self-duality intervenes: in the localization, not in the radical.
- finite `S_N` (PC): the defect is `E_N = S_N𝓕 − JS_N` (finite Poisson) plus `H_{M,N}` (hyperbola, without coefficients
  `k ≤ N` by Λ∗1 = log, R161_001 Thm. 2.1). (PC) is the truncated-operator version of the same lemma.
- (d) high prolate block of 211: NOT identified. ROUND_021_A §3(c) leaves it OPEN; I have no proof.

**Is it already written as a single statement?** Almost: R160_D4_R2 Thm. 4.3 is (U) for `h ∈ C_c^∞` with the explicit Poisson
defect, and its Thm. 5.1 closes the class «Dirichlet convolution identity on tests» as carrier
of the sign. P46 thm:radical (ideal) gives the case `M∗φ`. The only thing not written is to combine `K_Pó = S_ζg_0` with that theorem; it is
one line, not a new result. Answer to the hypothesis under test: **(a), (b), (c) are one object in the sense of
(U) (CITED); (d) OPEN.** The form on the image is «boundary terms» by (U) + truncation, and those boundaries are
exactly Poisson defect + hyperbola tail; none carries a sign by R160_D4_R2 Thm. 5.1.

## Part 2 — The congruence `𝔹_M = Zᵀ𝔸_M Z`

`Z_{mk} = 1_{k|m}(m/k)^{−1/2}` is the matrix of `S_M` in lattice coordinates: `s ↦ Zs` corresponds to
`Σ_k s_kτ_{log k}F_0 ↦ Σ_m(Zs)_mτ_{log m}F_0`, i.e. to `S_{M/k}` applied to the atom `k` (triangular truncation, not
uniform in `N`). `Z⁻¹_{mk} = 1_{k|m}μ(m/k)(m/k)^{−1/2}` (N_BUILD_022).

**Lemma 2.1 (PROVED; NUMERICAL control to `10⁻¹⁴` at `M = 60`).** `ZΔ = ΔZ = LZ − ZL` (commutative Dirichlet convolution
on a divisor-closed set; `1∗Λ = log`), hence
`Zᵀ Div_M Z = 2ZᵀLZ − (LG + GL)`, `G := ZᵀZ`, and entrywise, with `l = lcm(a,b)`, `g = gcd(a,b)`:

    (ZᵀDiv_M Z)_{ab} = (√(ab)/l) Σ_{j ≤ M/l} [log(l/g) + 2 log j] / j  ≥ 0.

*Proof.* `G_{ab} = Σ_{l|m≤M} √(ab)/m`; `(ZᵀLZ)_{ab} = Σ_{l|m≤M} √(ab)log m/m`; `2log(lj) − log(ab) = log(l/g) + 2log j`. ∎
Λ disappears completely: it is N_BUILD_022 §1 (= R162_903 B2.1) read as a congruence. With `cΛ`:
`Zᵀ Div^{(c)} Z = c·(the above)`, which is not weight-free (`(c−1)ZᵀDivZ` left over) — automatic, without sign (F1).

**Structure of `𝔹_M`.** `𝔹_M = ZᵀArch_MZ − [2ZᵀLZ − {L, G}] − ZᵀNear_MZ`. (i) What cancels: only the part of
exact coincidences (Div), and the cancellation is paid for by a hyperbola tail `Σ_{j≤M/l} log j/j ≍ ½log²(M/l)` that grows
with `M`: the «interior» does not stay at zero, it is transported to a function of `(a,b,M)` without arithmetic.
(ii) What does not change: `ZᵀNear_MZ`, without exact identity (N_BUILD_022 §3, NO-GO PROVED: the defect is Near itself).
(iii) **No block ≈ 0 appears.** The entries `e_k` of the atom basis are `τ_{log k}F_0` with `F_0` of support
`2T_0 < log 2`: compact input, not Gaussian, with `Φ_{F_0}(1) ≠ 0` in general, so that by R160_D4_R2 Thm. 4.3(a)
the image `S` grows at the polar rate; the closeness to the radical of Part 1 requires Gaussian inputs in the
continuous variable, which on the lattice are not finitely supported vectors. The near-null block of 211 does not become an
explicit block of `𝔹_M` under this congruence (ARGUED; I did not do the spectral computation).

**Controls.** The congruence holds for every weight (R162_903 Thm. 4.1(c)): inertia of `𝔹^{(w)}` = inertia of `𝔸^{(w)}`.
`2Λ`: an additional `−ZᵀDivZ` appears, entrywise ≤ 0 by Lemma 2.1; deleting `p^k`: `Zᵀ(δ_{p^k}-diagonal)Z`;
Beurling: `Z` changes support (generalized integers). No NAMED step loses sign because no step has a
sign: by Sylvester the congruence is an isomorphism of forms.

## Part 3 — Verdict

- **Part 2: repetition / class NO-GO already recorded.** Class: integer unitriangular congruences on the
  divisibility order (R162_903 Thm. 4.1–4.2, §8; R162_1003 Cor. 4.3; N_BUILD_022 §§1–3). The proposed «difference» (exact sum
  on the lattice, not a weight or approximate inverse) lies literally inside that class: `Z` is the matrix of the
  exact sum.
- **Part 1: the unified statement is CITED** (R160_D4_R2 Thm. 4.3 + P46 thm:radical + Obs. 1.1), with a correction to
  ROUND_020_B §4.2: Gaussian self-duality enters in the localization, not in the radicality. (d) OPEN.
- Intermediates: Lemma 2.1 (closed form, Λ-free and entrywise ≥ 0, of `ZᵀDivZ`) is a rewriting of
  N_BUILD_022 §1; it is not new in content.
- **Next operation: none** from this standpoint. The only open question it leaves is (d): whether the near-null
  cluster of 211 lies in `Π_T S_ζ(Gaussians)`; it is an identification statement, without sign (R160_D4_R2 Thm. 5.1).
