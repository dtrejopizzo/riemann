# INV_V_002 — Affine near-coincidence form and the Hecke–Chebyshev transfer of Ш (phase 196)

Memo, continuation of INV_V_001 (notation there). honest labels.
Corpus/index check: as in INV_V_001 §0, plus `INV_H_001` (Chebyshev/Ramanujan/Vaughan identities used linearly: DEAD),
`INV_K_001` (divisor gauges), `INV_I_001` (`𝒞_1` = identification, R163_1001), N_018 (Euler/Möbius identities + CS),
Hamburger rigidity (R162_2601c, prop:spec(5)), residue R9 / problem (S) (near-coincidences `m ≈ kn` in the multiplicative
variable), phase 190. **New reason vs those:** the near-coincidences here are *additive* (`y = n(z+a)`, `a ∈ ℤ∖0`) between
continuous window points, produced by Poisson; and Chebyshev's identity is used as an operator identity on the distribution Ш,
then tested for a *quadratic* lift — never as a linear identity for Λ inside the window form.

## 1. The affine near-coincidence form

For `F ∈ 𝒫_T ∩ C_c^∞(I_T)`, `f`, `δ_n`, `⟨·,·⟩_Ш` as in INV_V_001, `V := Σ_{n∈𝒩_T} v_n δ_n`, define
`R_n(F;a) := (δ_n f * f̃)(a) = ∫ n^{1/2} f(nx) \overline{f(x−a)} dx`, and
**`𝔄ff_T(F) := Σ_{n∈𝒩_T} v_n Σ_{a∈ℤ∖0} Re R_n(F;a)`.**

In the log variables `y = log|nx|`, `z = log|x−a|` the integrand lives on the curve `e^y = n(e^z + a)` (sign cases
aside): a **non-translation** correspondence of the window `I_T × I_T` (the "+" of the semiring acting after the "·").
Only `0 < |a| < e^T(1+1/n)` contribute (support), so the sum is finite: `#(n,a) ≲ N·√N`.

**Thm V2.1 (exact split; PROVED).**
`𝔞_T(F) = A_∞(F) + ½ 𝔄ff_T(F) − ½ Re⟨Vf, f⟩_Ш`, with `A_∞(F) = (1/2π)∫ m|F̂|²`.
*Proof.* INV_V_001 Thm V1.1 and Poisson `⟨δ_n f,f⟩_Ш = Σ_{a∈ℤ} R_n(F;a)`, the `a=0` term being `⟨δ_n f,f⟩ = 2𝒞F(log n)`. ∎

**Prop V2.2 (properties; PROVED unless marked).**
(a) *Not a dual certificate.* In Mellin variables the kernel of `𝔄ff_T` is `D_N(s)·[ζ(1+i(s−s′)) − c·δ(s−s′)]·γγ̄`
(`D_N(s) = Σ_{n<N} v_n n^{−is}`, normalisation constants as in V1.3), which is not diagonal; so `𝔄ff_T` is not of the form
`∫ σ|F̂|²` and is not produced by any `(ν,β)` of def:PD with `ν` dilation-invariant. (Diagonal part would require
`ζ(1+iu) ∝ δ(u)`.)
(b) *Not a product over places* (ARGUED): `ζ(1+iu) − cδ(u)` is not a Schur product of local kernels (the Euler product
`ζ(1+iu)` is; subtracting the `a=0` atom destroys the product structure). As a form it is the difference between the
Schur-factorised Ш-form and the diagonal window form.
(c) *ℤ-specific*: uses translations by `a∈ℤ` (Beurling systems have no `τ_1`; for a lattice `αℤ`, `α≠1`, Poisson pairs
`αℤ` with `α^{−1}ℤ` and Thm V2.1 changes; ℤ is the self-dual point).
(d) *Comb-generic in `v`* (PROVED): `𝔄ff_T` is linear in the comb, so Thm V2.1 holds verbatim for `a_P`, `cΛ`, Beurling
weights placed on ℕ. Requirement "distinguishes Λ" is **not** met by the form alone.

## 2. Where Λ is intrinsic: the Hecke–Chebyshev transfer of Ш

**Thm V2.3 (transfer; PROVED).** As distributions on `(−e^{T}, e^{T})∖{0}` (more generally on `0<|x|<N`),
`V^* Ш = 2 log|x| · Ш`, i.e. for every window `f`: `Σ_{n} v_n Σ_{a∈ℤ} (δ_n f)(a) = 2 Σ_{a∈ℤ} log|a| f(a)`.
*Proof.* `δ_n^* Ш = n^{1/2} Σ_a δ_{na}`; so `V^*Ш = Σ_m 2(Λ*1)(|m|) δ_m = 2Σ_m log|m| δ_m` for `|m|<N`, `m≠0`;
`f(0)=0`. ∎
In the log variable `log|x|·` is the position operator `U: F(u) ↦ uF(u)`, so V2.3 reads `(V^* − 2U)Ш = 0`: **the
von Mangoldt Hecke operator and twice the position operator agree on the Dirac comb.** By Poisson the same statement on the
Fourier side is the derivative of the functional equation of ζ restricted to the window (Riemann–Hamburger), hence a
rigidity identity, not an inequality.

*Falsifier behaviour (PROVED, quantitative):* for `a_P`, `V_P^*Ш − 2UШ = −2Σ_m (Λ𝟏_{p<P} * 1)(m) δ_m`
(defect `= −2 log` of the `P`-smooth part of `m`, nonzero at `m = 2`); for `cΛ` the defect is `2(c−1)log|m|`; Beurling
systems have no Ш. So V2.3 separates Λ from all three falsifiers — but it is a linear identity in Λ, i.e. the
identification class `𝒞_1` (R163_1001) / INV_H collapse, when used alone.

**Thm V2.4 (Chebyshev rigidity: no quadratic lift; PROVED).** Let `c: ℕ×ℕ→ℂ` and suppose the Λ-Hecke operator acts on
the first variable of the lattice kernel `𝒦 = Σ_{a,b} c(a,b) δ_a⊗δ_b` as `2 log` (exact transfer), i.e.
`Σ_{n|m} Λ(n) c(m/n, b) = log m · c(m,b)` for all `1 ≤ m < M`, all `b`. Then `c(m,b) = c(1,b)` for `m < M`: the kernel is
constant in the transferred variable. Consequently every Hermitian lattice kernel admitting the exact transfer has the
form `𝟏 ⊗ φ` on the window, i.e. rank one, and the quadratic forms it produces are `Re[ℓ_Ш(Vf)·\overline{ℓ_φ(f)}]`:
products of two linear functionals, sign-blind on `𝒫_T` (codimension ≥ 3 subspaces kill them).
*Proof.* Fix `b`, write `c = 1*h` (Dirichlet convolution in the first variable, `h = μ*c`). Then `Λ*c = (Λ*1)*h = log*h`,
while `log·(1*h) = log*h + 1*(h·log)` (log is a derivation of Dirichlet convolution). Exact transfer ⟺ `1*(h·log) = 0` on
`[1,M)` ⟺ `h(m) log m = 0` for `1<m<M` (Möbius) ⟺ `h = h(1)δ_1` there ⟺ `c(·,b) ≡ c(1,b)`. ∎

So the Λ-specific relation lives only on the rank-one distribution Ш; the moment one asks for a positive *Hermitian* object
(needed to compare with `𝔞_T`), exact transfer forces rank one. This is a precise version of lesson (iii): ℤ-specificity
survives Poisson, survives Hecke, but Chebyshev's `Λ*1 = log` is a statement about a single vector (Ш), and quadratic
positivity needs a Hermitian kernel.

## 3. Precise remaining gap (OPEN)

(G1) **Approximate Chebyshev eigen-kernels.** For a positive Hermitian lattice kernel `c`, the transfer defect is
`2·1*(h·log)` (proof of V2.4). Wanted: a positive kernel on `{1 ≤ a,b < √N}` with large rank whose transfer defect is
controlled by `A_∞(F)` on `𝒫_T`. The defect is a divisor-sum expression; if the control is only through identities +
Cauchy–Schwarz it falls under N_018 (ARGUED). OPEN.
(G2) **One-sided affine inequality.** By V2.1, row D on the window ⟺ `𝔄ff_T(F) ≥ Re⟨Vf,f⟩_Ш − 2A_∞(F)` on `𝒫_T`.
This is a reformulation (REF-D, a valid target), whose new feature is that the left side is a *finite additive* count of
window coincidences `e^y = n(e^z+a)`, `0<|a|<e^T(1+1/n)`, and the right side's Ш-part is a Schur product over places at
σ = 1. Cauchy–Schwarz in the Ш-geometry gives only the trivial bound (W-lin / J2 direction), so it is excluded as the
mechanism. OPEN.

## 4. Requirements and six-clause self-check

| requirement | 𝔄ff_T (V2.1) | transfer (V2.3) |
|---|---|---|
| non-factorizable over places | ARGUED yes (V2.2b) | yes (uses ℤ and Λ*1 jointly) |
| additive structure of ℤ (sums, not logs) | yes | yes |
| exact relation to 𝔞_T, not a dual certificate | yes, exact, non-diagonal (PROVED) | no relation to 𝔞_T (linear, not a form) |
| built-in positivity without the target | inherited Ш-positivity only of the *other* term | none (identity) |
| distinguishes Λ / a_P / cΛ / Beurling | NO (linear in comb) | YES, quantitatively (PROVED) |

The two target properties appear, but **in two different objects that cannot be merged exactly** (Thm V2.4).
Clauses: (1) 𝔄ff fails (comb-linear), transfer passes as a separator but is identification-class alone; (2)–(4) pass;
(5) transfer meets it through Ш/Poisson (FE) and Λ*1, not through ζ(½+iτ) — but only linearly, which by Hamburger is
rigidity, not sign (ARGUED); (6) no ∂log is crossed (Λ*1 = log is used undifferentiated) — passes vacuously.
**Verdict:** NO-GO for the class "exact Hermitian lifts of the Hecke–Chebyshev transfer" (PROVED, V2.4). Live residue: (G1)
approximate eigen-kernels; (G2) the affine one-sided inequality (REF-D). No sign.
