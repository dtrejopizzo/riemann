# AUDIT_L_SHARP_6 — audit of PROOF_L_SHARP_U_001 and MORI15_EXTREMAL_001

Phase 199. ,
no zero location is used as input,
NUMÉRICO. Checked against AUDIT_L_SHARP_5 (constraints 1–17), T_001, A_001 (Thm 1.1, Rem (i)–(ii), §2), K_001, V_001,
Guo Lemmas 4.3/4.4, Thm 4.5 (as quoted in A_001 §1(c)), Mori VIII conventions (AUDIT_ZENODO_FRONTIER §B1).
Independent re-computations: scratchpad scripts (not shipped), double precision on the shipped 120-digit eigenvector, and a
110-digit Nyström computation of the prolate eigenvalues.

**Verdict in one line.** U.1 and U.2 stand as PROVED, but U.1.3 is a *polarisation* of A_001 Thm 1.1(c) (itself Guo Thm 4.5)
and U.1.2 is not needed for it; U.3 stays CONDITIONAL. MORI15's numbers reproduce (Γ_ℝ, n = 2 comb, A, pole, 1−λ₄ all
confirmed independently), but the self-duality "claim" is **not new structure**: it is the window parity of g* transported by
co-Poisson (exact identity, below) and lives in the *standard* 𝔉-sector, not in U's 𝔉_μ-sector, where the extremal is
maximally non-self-dual. κ_emp's upper end (1.09) is not justified. The "mechanism" is ARGUED; the only PROVED statement behind
it is A_001's W_T(g) = 𝒲_ext[Ψ_f]. No sector reduction of (★★) beyond the parity split exists (constraint 18). (★★) OPEN.

## 1. PROOF_L_SHARP_U_001

**U.1.1 (edge intertwining).** Recomputed: Φ_{𝔉_μh}(x) = e^{x/2}μ^{1/2}Σĥ(ne^{x+2a}) = Φ_ĥ(x+2a) = Φ_h(−2a−x) (T Lemma 1.1,
h(0) = ĥ(0) = 0); 𝔉_μ² h = h(−·), unitary. **PROVED** ✓.

**U.1.2 (radical for f_±).** Needs W∘R_a = R_a∘W. Convolution with even kernels and the symmetric prime shifts commute with any
reflection; the rank-two pole operator PΦ = e^{x/2}⟨Φ,e^{−y/2}⟩ + e^{−x/2}⟨Φ,e^{y/2}⟩ also does (checked: under R_a the two
terms swap with factors e^{±a} that cancel). Only Guo 4.4 for f itself is used. **PROVED given CITED Guo 4.3/4.4** ✓.
Caveat: U.1.2 is *not used* by the displayed formula of Thm U.1.3 — it only enters the "consistency" line.

**U.1.3 (sector formula on the carrier).** u_± = 2Φ_{f_±}(−a+·) on (0,∞) checked (Φ_f = 0 beyond a, Φ_f∘R_a = Ψ̌ there).
The first equality W_T(g) = Σ_{j≥1}L_j(ǧ)L_j(Ψ̌) + 𝒫(ǧ,Ψ̌) − A(ǧ)A(Ψ̌) is A_001 Thm 1.1(c) [= Guo Thm 4.5 in the form
Ãg = XΨ_f] written in edge coordinates with the completely monotone Hankel kernel; the second is 4xy = (x+y)² − (x−y)².
**PROVED; it is a rewrite of Guo 4.5 (via A_001) plus polarisation — no new content**, and the −SOS on u_− is forced.
*Independent numerical check of the kernels (this audit):* on Mori's g* (where ‖Ψ̌‖ ≈ 10⁻³⁵), U.1.3 + T Thm 3.1 predict
𝒲_refl[ǧ*] = W_T(g*) + O(‖Ψ̌‖). Computed (double, 400-node GL, primes q ≤ 225, j ≤ 400):
Σ_{j≥1}L_j(ǧ*)² = 0.0011391, 𝒫[ǧ*] = 2.9403889, A(ǧ*)² = 2.9415280, total −6.4·10⁻¹⁴ (V_001: 3.8·10⁻¹³) — zero to the
double floor, a 13-digit confirmation of the edge-mirror constants (j ≥ 1 Hankel, B² absorbed, 𝒫 up to q < μ²). NUMÉRICO.

**U.2.1 (gauge⊥ = 𝒮(1,1)⁺, carrier closure = 𝒮(1,μ)⁺⊥, ℓ = λ‖Πρ‖², annulus 𝒱_μ).** (a) ∫ψ is L²(−1,1)-continuous, ψ(0)
is not: closure V = {∫ψ = 0}; ρ ⊥ (1−P₁)ψ̂ ∀ψ ∈ V ⟺ ρ̂|_{(−1,1)} ≡ const ✓. (b) ∫h f̂(λ·) = ∫f ĥ(λ·) ✓ ⇒ ĥ ≡ const on
(−μ,μ) ✓. (c) Π(𝒮(1,μ)⁺)^⊥ = 𝒱_μ exactly (v ∈ 𝒱_μ is its own preimage), ∩_μ = {0} ✓. Factor λ: ‖r_f‖² = λ‖ρ‖² ✓.
**PROVED (L²)** ✓. Note: this is the L²-closure statement; the canonical gauge for ℓ is the orthogonal projection (constraint 17
satisfied), and every *finite* polynomial gauge family gives an **upper** bound on ℓ.

**U.3.1.** CONDITIONAL on (C1) closability/gauge-invariance of 𝔔 along the L²-closure and (C2) = (H1). Agreed; REF-D agreed.
Monotonicity κ_μ non-increasing: PROVED ✓ (inclusion of carriers). Core dichotomy: CONDITIONAL/OPEN ✓.

## 2. MORI15_EXTREMAL_001

**Conventions.** Mori's basis φ_j = √((2j+1)/2L)P_j(x/L), L = ½log15, parity-split (832 modes each); pole 2(∫g cosh)² −
2(∫g sinh)² = 2AB with A = ∫ge^{x/2}, B = ∫ge^{−x/2} ✓; Q = W_T with the pole term ✓. Eigen-extraction (720-bit subspace
inverse iteration, residual 2.7·10⁻¹⁴⁸) not re-run (needs the 3328-bit matrices); Galerkin bottom 4.763·10⁻⁷⁰ ≥ certified
2.40·10⁻⁷⁰, consistent. NUMÉRICO as reported.

**Independent cross-checks (double precision, Clenshaw on the shipped vector):** ‖g*‖² = 1.0000000000000; A = −0.87149255053314
(memo −0.871492550533) ⇒ pole 1.5189985312695 ✓; Γ_ℝ = ψ(¼) − log π = −5.3721834192 ✓; c(log 2) = 0.063841255107 ✓, n = 2
comb term 2Λ(2)2^{−½}c = 0.0625809102 ✓; Γ_ℝ + Lévy = −1.455794 = arch total ✓; −5.372183 + 3.916389 + 1.518999 − 0.063204
= 0 to 10⁻⁶ (double) ✓. **1−λ₄ (c = 2πμ = 30π, prolates on [−λ,λ], band λ — correct time–band product λ·λ):** even-kernel
Nyström, 110 digits, N = 120 and 150 agree: 1−λ₀ = 9.40068847·10⁻⁸¹, 1−λ₂ = 2.60802073·10⁻⁷⁵, **1−λ₄ = 1.16682499·10⁻⁷⁰**,
1−λ₆ = 2.01858425·10⁻⁶⁶ ✓ (memo to all digits). Slepian asymptotic: 9.445·10⁻⁸¹, 1.2718·10⁻⁷⁰ (Fuchs value quoted ✓, 9 % high).
W_T/(1−λ₄) = 4.0824 ✓; a₄²(1−λ₄) = 3.872·10⁻⁷⁰ ✓.

**κ_emp ∈ [0.56, 1.09] — RELABEL.** The shipped ℓ = 8.4467·10⁻⁷⁰ is the minimum over the M = 28 polynomial gauge (the JSON key
still says "M=16 family" — stale label). By U.2 the true ℓ(g*) = dist² to the full gauge closure ≤ 8.45·10⁻⁷⁰, so
**W_T/ℓ ≥ 0.564 is the only bound the data support** (NUMÉRICO). The upper end 1.09 uses the "structured part" 4.36·10⁻⁷⁰,
which is a gauge-dependent partial sum, not a lower bound on ℓ: ARGUED. Report κ_emp ≥ 0.56.

**Self-duality — what is PROVED.** For admissible f, T Lemma 1.1 gives Φ_{f̂} = Φ_f∘R (R: x ↦ −x). If g = Φ_f|_I is even,
then with f_− := (f − f̂)/2 (standard 𝔉), **Φ_{f_−} = ½(Ψ_f − Ψ_f∘R)** on all of ℝ: it vanishes on I exactly and equals ±½Ψ
outside (Φ_f = 0 on (a,∞)). Möbius inversion (absolutely convergent: Ψ_f(y) = O(e^{3y/2}) at −∞, A_001 Thm 1.1) recovers f_−
from Φ_{f_−}, so **f_− is a linear image of Ψ_f alone** (PROVED as identity; explicit μ-dependent norm constant not written).
Since Ψ_f = Z r_f (A_001 Rem (ii)), ‖f_−‖ = O_μ(√ℓ): every even window datum of small leakage is standard-𝔉-self-dual to order
√ℓ; odd data are anti-self-dual (span ψ_{4j+2}) to the same order (prediction; p1 prolate data not shipped, not checked). On g*:
anti-self-dual mass 2.3·10⁻⁷¹ ≈ (5·10⁻³⁶)², √ℓ ≈ 2·10⁻³⁵ — consistent. Hence: **not a numerical coincidence and not new
structure: it is parity** (agrees with V_001 V.1.4, whose "ARGUED tail" is upgraded here to a PROVED identity; constant OPEN).
**Not U.1's sector.** 𝔉_μf*(ξ) = μ^{½}f̂*(μξ) ≈ μ^{½}f*(μξ) is concentrated on |ξ| ≲ 0.1 (inside the gauge core 1/λ = 0.26),
while f* is O(1) on [0.26, 1.5]: in U's 𝔉_μ-splitting ‖f*_−^{(μ)}‖ ≈ ‖f*_+^{(μ)}‖ (maximally mixed; ARGUED from the profile, not computed). MORI15 §4 is right to flag
the distinction; the README/index phrase "Fourier-self-dual" must read "standard-𝔉 self-dual (= parity of g*)".
T Prop 3.3 sector orthogonality in the standard 𝔉 at cut 0 is the parity orthogonality of W_T (window-centre reflection).

## 3. The "mechanism" reading
ARGUED, as the memo says. The only PROVED statement behind items 1–2 is A_001 Thm 1.1: **W_T(g) = 𝒲_ext[Ψ_f] = −𝒲(g,Ψ_f)**,
quadratic in the below-window piece Ψ_f = Z r_f, which explains *why* W_T is of order ‖Ψ‖² ~ ℓ while every O(1) piece cancels,
but gives no sign. The requested pieces on g*: Σ_{j≥1}L_j² = 0.0011391, 𝒫 = 2.9403889, A² = 2.9415280; **ΣL_j² + 𝒫 ≥ A² is
undecided** (equality to 6·10⁻¹⁴; the true value is predicted O(10⁻³⁵)). Note the balance on ǧ* is 𝒫 (prime powers up to
225, concentrated near q ≈ μ) against A²; the archimedean SOS is 0.04 % of it. The 4.8·10⁻⁷⁰ is the cross term
¼(𝒲_refl[ǧ+Ψ̌] − 𝒲_refl[ǧ−Ψ̌]) = 𝒲_refl(ǧ,Ψ̌), products of O(1)·O(10⁻³⁵) terms cancelling to 10⁻⁷⁰; with the Galerkin floor at
10⁻³⁸ it is **not resolvable** from the shipped data (would need Ψ̌ to ~10⁻⁷² absolute). No PROVED statement follows from the
zero-side picture (zeros used as check only, correctly).

## 4. Consolidation: sector reduction (new constraint 18)
Exact lemma one would need: "(★★) holds iff it holds on 𝔉-self-dual data". Status:
- standard 𝔉: **PROVED but empty** — it is the parity split (W_T and ℓ are reflection-invariant, even/odd orthogonal), already
  used by Mori; self-dual ⟺ even g up to O(√ℓ).
- U's 𝔉_μ: **"the even-sector bottom is attained on 𝔉_μ-self-dual data" is FALSE** in exact form (f_−^{(μ)} ≠ 0 for every f ≠ 0,
  Paley–Wiener) and approximately false on g* (maximally mixed: ⟨f*,𝔉_μf*⟩ only sees f* on |ξ| ≲ 0.1; ARGUED from the shipped profile). NO-GO as a reduction.
**Constraint 18 (sector reduction).** A Fourier-sector reduction of (★★) is either the parity split (standard 𝔉: no new
content) or impossible (𝔉_μ: carrier data are never in one sector, and the extremal is maximally mixed). Any sector argument
must be stated in the standard 𝔉 and then is a statement about even/odd g, i.e. about Ψ_f, i.e. back to W_T = 𝒲_ext[Ψ_f].

## 5. Labels
| item | memo | audit |
|---|---|---|
| U.1.1 | PROVED | PROVED |
| U.1.2 | PROVED (Guo 4.4) | PROVED; not needed for U.1.3 |
| U.1.3 | PROVED, restatement of Guo 4.5 | PROVED; polarisation of A_001 Thm 1.1(c); kernels confirmed NUMÉRICO (13 digits) |
| U.2.1 | PROVED (L²) | PROVED (L²) |
| U.3.1, core dichotomy | CONDITIONAL | CONDITIONAL / OPEN |
| MORI15 pieces, A, pole, Γ_ℝ, n = 2, 1−λ₄ | NUMÉRICO | NUMÉRICO, independently reproduced |
| κ_emp ∈ [0.56, 1.09] | NUMÉRICO | κ_emp ≥ 0.56 NUMÉRICO; upper end ARGUED |
| f* self-dual | NUMÉRICO "new structural datum" | PROVED consequence of parity (identity), standard 𝔉 only; not U's 𝔉_μ |
| mechanism reading | ARGUED | ARGUED; PROVED core = A_001 W_T = 𝒲_ext[Ψ_f] |
| ΣL_j² + 𝒫 ≥ A² on ǧ* | — | undecided below 10⁻¹³ (NUMÉRICO) |
| sector reduction of (★★) | — | parity only / NO-GO for 𝔉_μ (constraint 18) |
| (★★), L′♯ | OPEN | OPEN |
**Do not retry:** "self-dual sector reduction" of (★★) (it is parity); reading MORI15 self-duality as evidence for U's 𝔉_μ
sectors; resolving 4.8·10⁻⁷⁰ from 𝒲_refl pieces with Galerkin-floor data. No sign is claimed. Row D OPEN.
