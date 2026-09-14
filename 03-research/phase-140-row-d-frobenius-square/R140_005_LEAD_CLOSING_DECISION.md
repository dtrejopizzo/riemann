# R140.005 — Lead closing decision, phase 140 (the Frobenius side of (P139): the square as a tensor structure)

*Lead of record: Fable 5.1. Date 2026-09-13. Inputs: R140_000, R140_001 (rounds 1–2 in place),
R140_002 (hostile: 1 FATAL, 8 MAJOR, 6 MINOR), R140_003 (ledger), R140_004 (confirmation: CONFIRMED with
residue R2, R8, R11). Lead's own reading: Thm D.23.10/D.23.13 as Bochner positivity of the Toeplitz
kernel on a translate orbit (RESTATEMENT — agreed with the auditor before the round-2 order); Cor.
D.24.12.*

## 1. Results of record

| item | statement | label |
|---|---|---|
| D.22 | `Frob_𝔫` ideal-indexed for every number field; inverse-semigroup law; bidegree `(N𝔫^{±½})`; `Sh_{O_K}(Frob_𝔫) = Cone(𝔫L_S ↪ L_S)` with `L_S = ∏_{𝔓∈S_f}O_𝔓`, `H⁰ ≅ O_K/𝔫`, `deg_det = log N𝔫`, non-monoidal by `Tor₁`; **O-9 closed** | PROVED |
| D.23.4–6 | the *Pólya realization* `r(Frob_n) = τ_{log n}(2K)` collapses mod `𝓝_∞` to `NS(P¹×P¹)` (rank 2, genus 0, Castelnuovo with equality) — a property of that realization, which deletes the weights `Λ(𝔫)N𝔫^{−½}` | PROVED |
| D.23.12 | three Gram forms: (A) pure Frobenius (`W_fin` only, sparse, weights `Λ(q^k)q^{−k/2}`, **unsigned at every finite chart** by Paper 44 Thm 8bis.4a); (B) unit-averaged = full Weil kernel (sign ⟺ RH, factorization forgotten); (C) Pólya realization, rank 2, sees neither; no object carries (A) and (B) together | PROVED (R2 wording residue) |
| D.23.13 | Castelnuovo on all finite spans of a translate orbit of `E_0` ⟺ Bochner positive-definiteness of the Toeplitz kernel `c ↦ W(E_0,τ_cE_0)` ⟺ RH for the zeros `E_0` sees (necessity via Bohr almost-periodicity) | RESTATEMENT |
| D.24.3a | tensor-square `h⁰_□(E) = h_c(deg⁻E)h_c(deg⁺E)`, `h_c = max(x,0)`: growth exactly `(r²/4)m²` at `mK_K` (`¼m²` for `Q`) — the growth wall of phase 136 is cleared **by this object** | PROVED |
| D.24.4 | optimal `χ = c²/2 = 1/8` for `ξ` (`r²/8` for `ξ_K`), witness `½F_1`; lead's `χ = ¼` refuted | PROVED |
| D.24.5 | (c) for a bidegree-function ⟹ RH (general); ⟸ only under (D.24.5a) | PROVED |
| D.24.7 / D.24.11 | **no nonzero `h⁰` factoring through the bidegree satisfies (b′)** (witness `E_0 + tF`, `F` primitive in `C_c^∞`); every `h⁰` built from pairings with `r(Div_□)` factors through the bidegree | PROVED |
| D.24.12 | an admissible `h⁰` must separate equal-bidegree classes with different zero data, hence must read `Z(E)` through pairings `I_∞(E,X)` with `Z(X) ≠ 0` (= `PRIME − ARCH` of `E⋆X^∨`, no zero named); `r(Div_□)` is exactly the wrong family | PROVED (first half) / GUIDANCE (second) |
| CC candidate (β) | withdrawn as refutation; OPEN with the two units problems (U1) degree dictionary, (U2) `dim_S` vs real functional | OPEN |

## 2. The complementary failure (the phase's finding)

Two `h⁰` now exist in the corpus and fail on opposite clauses of Theorem 12.3:
* `h⁰_Z` (Frobenius-lattice count, phases 135–137): satisfies (a), (b′); growth `(log m)^{3/2}` — fails (c).
* `h⁰_□` (tensor square, this phase): satisfies (a) and (c)'s growth `¼m²`; fails (b′) for every bidegree-function.
By Cor. D.24.12 the missing ingredient is the same for both: an `h⁰` that reads the zero data through the
**arithmetic Gram entries of the pure Frobenius family (A)** — the weights `Λ(q^k)q^{−k/2}` are axiom A8
read directly, as T2 demands — while Paper 44 Thm 8bis.4a warns that (A)'s own form is not positive at
any finite chart (and its colimit version is OPEN, R3).

## 3. Residues carried
R2: distinguish Paper 44's `Q_fin` (form on radial profiles) from the discrete Gram matrix of
`{Frob_n^{sm}}` (no diagonal) in the (A) row — one sentence, to be entered with Part III.
R8: O-17 (primitive bridge for `Ξ_Q`) — template Paper 46 Prop. 12.4B with `P = {0,1}`, non-real DH zero.
R11: O-14′ ill-posed as written — fixed in the phase-141 blueprint (below).
Count correction: R140_002 has 15 findings (1 FATAL + 8 MAJOR + 6 MINOR).

## 4. Decision
Phase 140 closed; no label change for row D. Phase 141 opens on O-14′ first (well-posed per R11), then
O-17, with O-15 (the moment cone) as a tool, not a sign-carrier (it is model-uniform, T2).
Paper-facing list carried: P44-4, P44-5, P46-10…P46-13, P46-15, P44/46-16 (P46-14 withdrawn).
