# Round 031 B — Primitivity as a quantitative bound and generation of the negative block by translations in log ℕ

Object: `a^w_T(F) = Arch(F) − Σ_{n≥2} w_n c_F(log n)` on `P_T = {F ∈ L²(−T,T) : ∫F e^{±t/2} = 0}`
(P46 `eq:form`, `thm:A`, `rem:Kprim`; Galerkin matrices of `free_weight_scripts/forms.py`, audited against
the paper). (PBP_T): `Tr(ρ·Arch) ≥ 0` for every state `ρ` on `P_T` with `Tr(ρ C_n) = 0`, `2 ≤ n < e^{2T}`,
where `C_n` is the form `F ↦ c_F(log n)`. Script: `free_weight_scripts/block_span_031B.py`.

## Cross-check (four-point filter)

1. **Closest antecedent.** (a) Phase 204 (index, l. 9330): in `E_N`, `N ≈ 4T`, even positivity
   reduces to the inertia of an explicit Toeplitz−Hankel matrix; "the comb cancels all negative
   directions except one". (b) P211-11B, `ROUND_011_B` (index, l. 6432): Schur assembly in two blocks
   low/high, NUMERICAL NO-GO ("do not retry two-block LM/HI Schur … K-uniform"). (c) R160_M2_R1 Thm 4.1
   (strong duality: (PBP_T) ⟺ there is a free weight `w` with `a^w_T ⪰ 0`) and 212-26-A (`V*_T > 0` NUMERICAL).
   (d) 212-30-B (primitivity was not turned into a bound; reopening condition: Paley–Wiener-type
   inequality with the type and the zeros at `±i/2`). (e) I6 (index, l. 4823/4889): dimension bound of the
   negative block from arithmetic data, OPEN. `ROUND_031_A.md` did not exist at the start.
2. **What would be new.** (i) Exact quantitative value of primitivity (step 1). (ii) The reading on the
   state side: "the compressed `C_n` generate the symmetric matrices of the block" as a mechanism for annihilating `ρ` on
   the block, and its comparison with systems without `log ℕ` (step 2).
3. **Why it would avoid the antecedent.** (b) works with the form `a_T` of the true weight; here the weight is
   free and only the geometry of the family `{C_n}` on the block is measured (rank and conditioning).
4. **Global connection.** Weak duality (PROVED, one line): if `a^w_T ⪰ 0` for some `w` and `ρ` is
   admissible, `Tr(ρ Arch) = Tr(ρ a^w_T) ≥ 0`. Hence any `w` built from the generation of the block
   gives (PBP_T), and from there only CONDITIONAL on the rigidity 212-30-A.

Result in advance: (1) PROVED and optimal bound, worth exactly two directions; (2) the generation of the
block holds with few `n`, also with the odd `n`, so it is not a property of the lattice; the
mechanism reduces to a low/complement Schur assembly with conditioning that decays fast:
selection NO-GO by repetition of (b) and (c).

## 1. Model problem without comb: how much primitivity is worth

**1.1 Kernels.** With `F̂(τ) = ∫F(t)e^{iτt}dt`, `F̂ ∈ PW_T` and the reproducing kernel
`k_z(τ) = sin(T(τ − z̄))/(π(τ − z̄))`. The conditions of `P_T` are `F̂(±i/2) = 0`, i.e. `F ⊥ e^{±t/2}`:
`‖k_{±i/2}‖² = sinh T/π`, `⟨k_{i/2}, k_{−i/2}⟩ = T/π`; independent for every `T > 0` (Gram
`(sinh²T − T²)/π² > 0`). `P_T` has codimension 2 in `L²(−T,T)`, invariant under `t ↦ −t`, with one
even condition (`cosh(t/2)`) and one odd (`sinh(t/2)`).

**1.2 Proposition (PROVED; Courant–Fischer min–max).** Let `λ_1 ≤ λ_2 ≤ …` be the eigenvalues of Arch on
`L²(−T,T)` and `λ_k^P` those of Arch on `P_T`. Then `λ_k ≤ λ_k^P ≤ λ_{k+2}`; by parity, separately
`λ_k^{ev} ≤ λ_k^{ev,P} ≤ λ_{k+1}^{ev}` and likewise in the odd sector. In particular
`n_−(Arch|P_T) ≥ n_−(Arch|L²) − 2` and `λ_1^P ≤ λ_3`.
Primitivity is worth, as an index bound, at most **two directions** (one even, one odd) at every `T`.

**1.3 Regime (ARGUED with Landau–Widom concentration CITED).** The number of low-frequency
directions in `|τ| ≤ τ* = 6.2898` is the Shannon number `(2T)(2τ*)/2π = 2Tτ*/π ≈ 4.00·T`; since
`m(τ) < 0` only there, `n_−(Arch|L²) ≈ 4T + O(log T)` and `λ_1, λ_3 → m(0) = −5.372` as `T → ∞`
(the first prolates concentrate their mass in `|τ| ≪ 1`). Thus:
- `T ≲ 0.6`: the two conditions are the whole low block; primitivity closes it (P46 `thm:index`:
  `λ^P > 0` for `T ≤ 0.58`). It is the only regime where it decides the sign.
- Large `T`: it removes 2 of `≈ 4T` directions and the minimum eigenvalue on `P_T` tends to `m(0)`: the
  gain in the lower bound of `∫m dμ` is `o(1)`. There is no bound on "low-frequency mass" better than
  the prolate one, except for the two dimensions.

**1.4 NUMERICAL** (Legendre `N = 24–40`, quadrature 240; the values on `P_T` reproduce `thm:index`):

| T | `n_−` on L² | 3 smallest on L² | `n_−` on P_T | 3 smallest on P_T |
|---|---|---|---|---|
| 0.6 | 2 | −1.946, −0.473, 0.031 | 1 | −0.007, 0.293, 0.613 |
| 0.9 | 4 | −2.471, −0.900, −0.377 | 2 | −0.424, −0.116, 0.205 |
| 1.2 | 5 | −2.863, −1.222, −0.668 | 3 | −0.732, −0.408, −0.087 |
| 1.6 | 6 | −3.265, −1.573, −0.966 | 4 | −1.066, −0.706, −0.384 |

The drop in the index is exactly 2 in the four cases: the bound 1.2 is attained. `λ_1^P` lies between
`λ_2` and `λ_3` of the full space. **Consequence:** the reopening condition of 212-30-B ("Paley–Wiener
with the zeros at `±i/2`") has a closed answer: the most the zeros give is Prop. 1.2, and for the
deficit `1.498` of 212-30-B, which lives in `π/log 2 < |τ| < 6.29`, they contribute `o(1)` as `T → ∞`.

## 2. The conditions Φ(log n) = 0 on the negative block

**2.1 Precise setting.** Let `B` be the eigenspace of Arch|P_T with eigenvalues `< 0` (dim `d`), `C` its
complement in `P_T` (Arch ≥ `γ ≥ 0` on `C`). A state `ρ ⪰ 0`, `Tr ρ = 1`, is written in blocks
`ρ_BB, ρ_BC, ρ_CC`, and `Tr(ρ C_n) = Tr(ρ_BB C_n^{BB}) + 2 Tr(ρ_BC C_n^{CB}) + Tr(ρ_CC C_n^{CC})`.

**2.2 Correction of the proposed count.** "If the `C_n^{BB}` generate the symmetric matrices of the block, `Tr(ρC_n)=0`
forces `ρ_BB = 0`" is false: the conditions couple `ρ_BB` with `ρ_BC` and `ρ_CC`, and `C` is infinite-dimensional,
so the ratio "conditions / dimension" makes no sense on the full carrier.
Moreover (PROVED) Arch and all the `C_n` commute with `t ↦ −t` (symmetrization of `c_F`) and `P_T` is
invariant: the `C_n^{BB}` can only generate the **parity-diagonal** matrices of the block, of dimension
`d_e(d_e+1)/2 + d_o(d_o+1)/2`; the even–odd part of `ρ` is invisible to Arch and to the conditions.

**2.3 Correct statement (PROVED, elementary).** If there is real `w` with
(a) `Arch^{BB} − Σ w_n C_n^{BB} ⪰ α`, (b) `Arch^{CC} − Σ w_n C_n^{CC} ⪰ β`, (c) `‖Σ w_n C_n^{BC}‖² ≤ αβ`,
with `α, β > 0`, then `a^w_T ⪰ 0` and (PBP_T) holds at that `T` (Schur + weak duality). Since `|c_F(u)| ≤ ‖F‖²`,
`‖C_n‖ ≤ 1` and (b)–(c) follow from `‖w‖_1 ≤ γ − β` and `‖w‖_1² ≤ αβ`. If the `C_n^{BB}` generate the
parity-diagonal matrices with smallest nonzero singular value `σ_min`, the minimum-norm `w` solving
`Σ w_n C_n^{BB} = Arch^{BB} − αI` satisfies `‖w‖_2 ≤ ‖Arch^{BB} − αI‖_F/σ_min`. Hence
`(PBP_T) ⟸ [parity-diagonal generation] + [‖Arch^{BB}−αI‖_F·√(#n)/σ_min ≤ min(γ − β, √(αβ))]`.
It is exactly a low/complement Schur assembly with free weight: by strong duality (antecedent c)
it is a sufficient condition for the problem of 212-26-A, not a new mechanism for the sign.

## 3. Numerical check (T = 0.9, 1.2, 1.6; with all n and with only the odd ones)

| T | `d` (even, odd) | #n (odd) | rank | nonzero `σ_min` all / odd | min-norm `‖w‖_1` | λ_min(a^w_T) |
|---|---|---|---|---|---|---|
| 0.6 | 1 (1,0) | 2 (1) | 1 = 1 | 0.199 / 0.075 | 0.37 / 0.76 | **+0.034 / +0.037** |
| 0.9 | 2 (1,1) | 5 (2) | 2 = 2 | 0.365 / 0.076 | 1.37 / 8.3 | **+0.008** / −2.03 |
| 1.2 | 3 (2,1) | 10 (5) | 4 = 4 | 0.014 / 0.0058 | 5.4 / 24.7 | −0.82 / −6.67 |
| 1.6 | 4 (2,2) | 23 (11) | 6 = 6 | 0.0013 / 0.00038 | 14.7 / 16.9 | −4.21 / −3.96 |

(`α = 0.05`; the rank always equals the parity-diagonal dimension; block `BB` stays at `0.05` by
construction and the failure is entirely in `CC`, which before the weight had minimum `0.205, 0.100, 0.001`.)
Readings (NUMERICAL):
- Generation of the block already holds with the first `n` and **also without the multiples of 2**: it does not
  distinguish `log ℕ` from the odd integers (nor, for the same reason, from a Beurling-type system with
  `≥ d(d+1)/2` generic translations). The sought "totality" is generic.
- `σ_min` drops `0.365 → 0.014 → 0.0013` between `T = 0.9` and `1.6` (≈ a factor 10 every 0.4 in `T`), and the
  `w` that cancels the block destroys the complement from `T = 1.2`. The minimum-norm `w` is not the optimum
  (212-26-A obtains `V*_T > 0` with SDP), but this shows that generation without control of the coupling gives
  nothing: all the information is in (b)–(c), which is the low/high coupling already recorded (antecedent b).
- The number of conditions (`≈ e^{2T}`) versus `d(d+1)/2 ≈ 8T²` does not enter: the rank saturates at the
  parity-diagonal dimension with very few `n`, and the rest of the conditions only improve the conditioning,
  with no structure specific to `log ℕ` visible at these `T`.

## 4. Verdict

- **PROVED:** Prop. 1.2 (primitivity is worth at most 2 in the index and `λ_1 ≤ λ_1^P ≤ λ_3`), optimal
  (NUMERICAL: attained at `T = 0.6–1.6`); parity of the family (2.2); sufficient Schur criterion (2.3).
- **ARGUED:** the gain in `inf ∫m dμ` is `o(1)` for `T → ∞` (prolate concentration); primitivity
  does not help recover the deficit `1.498` of 212-30-B.
- **Selection NO-GO (step 2):** "the compressed `C_n` generate the negative block" is a reformulation
  of the free-weight dual (R160 Thm 4.1 / 212-26-A) in low/complement Schur form (P211-11B). The
  generation is generic (holds with odd integers) and does not use the lattice; the whole difficulty is the coupling with the
  complement, whose conditioning `σ_min` decays fast in `T`.
- **How much is missing and where:** for (PBP_T) at `T ≥ 1.2` one would need a `w` with `‖Σ w_n C_n^{CC}‖ ≤ γ(T)`
  (`γ(1.6) ≈ 0.001`) and at the same time cancellation of the block, whose cost in `‖w‖` grows like `1/σ_min`. No
  counting argument gives that; it would have to come from a structure of `log ℕ` distinguishing the integers from
  the odd integers in the coupling `C_n^{BC}`, `C_n^{CC}`, not in the block.
- **Reopening condition:** a bound on `‖Σ w_n C_n^{CC}‖` for the `w` that cancels the block, better
  than `‖w‖_1`, that uses the arithmetic (and fails with the odd integers or with Beurling).

Suggested record for Part V of the index (not edited here): "212-31-B — Quantitative primitivity and
generation of the negative block by `{C_n}`: interlacing Prop. PROVED (worth 2 directions); generic
generation (holds without multiples of 2) NUMERICAL; selection NO-GO by reduction to low/complement Schur
with free weight; details in ROUND_031_B.md, `free_weight_scripts/block_span_031B.py`."
