# AUDIT_196 — INV_V_001 + INV_V_002 (phase 196)

Review. Checked against Paper 47 `main.tex`: eq:symbol (`c_F(u)=∫F(t)\bar F(t−u)`,
`𝒩_T={n≥2: log n<2T}`, `v_n=2Λ(n)/√n`), eq:form, `𝒫_T={A=B=0}`, def:PD (certificates = symbol inequalities
`s_T+ν̂+β·ĝ ≥ c`, `supp ν ⊆ {|u|≥2T}`), thm:Z, prop:spec; and against the index (G5H-122, N_018, INV_I_001 I2/I4 = R163_1001,
INV_H_001).

## (a) Non-factorisation of 𝔅 (Thm V1.2)
`δ_pτ_1δ_p^* = τ_{1/p}`: verified (`δ_p^*g(x)=p^{−1/2}g(x/p)`). (ii) PROVED but trivial and overlong: if `τ_1` sits in the
∞-factor it commutes with `δ_p`, contradicting `τ_{1/p}≠τ_1` in one line. Non-factorisation of an *algebra* carries no
positivity information (B(L²) is also non-factorised). Weight: nil.

## (b) V1.1 exact formula
`⟨δ_nf,f⟩ = 2c_F(log n)` and `𝔞_T = A_∞ − ½Σ v_n Re⟨δ_nf,f⟩`: VERIFIED against eq:symbol (the `t`-sign is immaterial:
cos and Re are even/real). NUMÉRICO: `R_n(0)` vs `2c_F(log n)` agree to 1e−13 (n=2,3, T=0.6). PROVED.

## (c) V1.3 Schur factorisation
(a) PROVED (checked: `(δ_nf)^(ξ)=|ξ|^{−1/2}G(log n−log|ξ|)`, `j=0` killed by `f̂(0)=2A(F)=0`). (b) With P47's Fourier
convention the kernel is `ζ(1−i(s−s′))` (conjugate; harmless). The `ε↓0` limit is a boundary value
`1/(ε+iu) → πδ(u) − i p.v.(1/u)`; PD of the Schur product holds for `ε>0` and passes to the limit as a distribution. But
`‖f‖²_Ш = Σ|f̂(j)|² ≥ 0` is trivial, and *any* measure `Σ_j w(j)δ_{log j}` with completely multiplicative `w` has an Euler
product: the "Schur factorisation" is a rewriting of `1/j` being multiplicative, not a structural discovery.
Cor V1.4: correct, but it is an instance of the indexed comb-genericity barrier (B″ clause 1; INV_I_001 I2 for the
`T≥0.60` threshold via O_6/`a_P`). Label: PROVED, SUBSUMED.
Remark V1.5 / Prop V2.2(a): the constant in "`ζ(1+iu) − 2πδ(u)`" is not checked against the boundary-value `πδ`; downgrade
the normalisation to ARGUED. Non-diagonality survives (p.v. term + entire part `ζ(s)−1/(s−1)` give an infinite-rank Toeplitz
kernel).

## (d) V2 split and 𝔄ff_T
Thm V2.1: PROVED; NUMÉRICO (script `audit196_v2_split_check.py`, smooth bump·quadratic F ∈ 𝒫_T, |A|,|B|≈3e−12, T=0.6,
𝒩_T={2,3}): Poisson side vs Fourier side of `⟨δ_nf,f⟩_Ш` agree to ≈1e−12 (n=2: −0.0281948325; n=3: −0.0291880534);
`𝔄ff` per-n parts −0.0399645, −0.0291919.
*Disguised certificate?* No: in log variables the kernel of `R_n(·;a)`, `a≠0`, lives on `e^y=n(e^z+a)`, not a function of
`y−z`, so the form on `L²(I_T)` is not Toeplitz, while every def:PD certificate restricted to the window is a symbol form.
Genuinely not a dual certificate (PROVED). But note `𝔄ff_T = 2(𝔞_T−A_∞) + Re⟨Vf,f⟩_Ш` identically: its whole non-diagonal
content *is* that of `Re⟨Vf,f⟩_Ш`; it is not an independent object.
Prop V2.2(b) stays ARGUED and is ill-posed (no definition of "Schur product" for a difference of forms).
**Prop V2.2(c) is FALSE as stated:** Poisson for `αℤ` gives the same split for every `α>0`
(`Σ_{a∈αℤ}` vs `α^{−1}Σ_j ĝ(j/α)`); the transfer V2.3 also holds for `αℤ` with `log|x/α|`. ℤ is a scale choice, not a
self-dual specificity of `𝔄ff`.

## (e) Transfer and Chebyshev rigidity
V2.3: PROVED (pointwise `Λ*1=log`; all `n|m` with `|m|<e^T` lie in `𝒩_T`). It is the identification class 𝒞_1
(R163_1001 / INV_H_001); the "Fourier side = derivative of FE" sentence is ARGUED, unverified.
V2.4: PROVED (log is a derivation of Dirichlet convolution; Möbius on initial segments). Stronger than stated: Hermitian
plus transfer in the first variable forces `c` constant, i.e. `c·𝟏⊗𝟏`. Error: "codimension ≥3 subspaces kill them" is wrong
(`𝒫_T` has codim 2; `Re[ℓ_1\bar ℓ_2]` stays indefinite on `𝒫_T` unless `ℓ_i∈span(A,B)`); conclusion "sign-blind" holds a
fortiori. Class ("exact Hermitian eigen-kernels of the transfer") is very narrow; NO-GO real but low value.

## (f) (G2)
`𝔄ff_T ≥ Re⟨Vf,f⟩_Ш − 2A_∞` on `𝒫_T` is `𝔞_T ≥ 0` rearranged by the exact identity V2.1 — the target itself, not a
consequence of thm:Z. "Finite additive count" is only compact support. Neither side has a sign (`Re⟨Vf,f⟩_Ш<0` in the check;
`V` is not positive). Not worth pursuing unless a concrete non-CS bound on `𝔄ff` is named. Label: REF-D (tautological), OPEN.

## (g) (G1)
Does not escape: the transfer defect `2·1*(h·log)` is linear in Λ, so forms built from it are INV_I_001 I4 (degree ≤1 in
`a`: O_4-blind or identification); positivity via identities + CS is N_018; the first non-homogeneous source (Selberg Λ²) is
already excluded in I4. Label: ARGUED inside N_018 ∪ I4; OPEN only nominally.

## Verdict
No error in the main identities (V1.1, V1.3a, V2.1, V2.3, V2.4 PROVED). Corrections: V2.2(c) FALSE; V1.5/V2.2a constants
ARGUED; V2.4 codim remark wrong; V1.4 subsumed; G2 tautological REF-D; G1 not escaping N_018/I4. No sign. Row D: OPEN.
