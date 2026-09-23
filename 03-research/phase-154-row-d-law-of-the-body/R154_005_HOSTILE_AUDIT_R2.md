# R154.005 — Hostile audit, round 2 of phase 154

*Auditor: Opus 5 (1M). 2026-09-20. Target: `R154_004_BUILDER_ROUND2.md` against `R154_003` (orders), `R154_002`
(binding repairs), `R154_001`, `phase-64/CURVATURE-computation.md §5`, `phase-115/115_17:103,748`,
Paper 42 `main.tex:4072–4230`, and `scripts/round2/`. Everything numerical below was re-run by the auditor;
scripts rerun verbatim are named, independent reimplementations are marked "own".*

---

## 0. Verdict table

| # | item | builder's label | **audit verdict** |
|---|---|---|---|
| 1 | **Theorem O** — no outside-window certificate attains `λ_min`; proof by complementary slackness | `PROVED`, "exact obstruction theorem" | **PROVED as a theorem, DOWNGRADE as a headline.** The proof is correct (§1) once the dual class is tightened (`ν` a *finite* even signed measure). What it rules out is **attainment**. It does **not** rule out what the programme actually needs, namely a certificate with value in `(0, λ_min)`. Scope sentence must be rewritten. |
| 2 | Theorem O applies at `v = 0` (pure Γ) | `PROVED` | **CONFIRMED.** No tension with Kwaśnicki: exact solvability of the eigenproblem is not attainment of *this* dual. |
| 3 | zero duality gap | `OPEN` | **CONFIRMED OPEN** — and therefore the verdict row "the class ceiling rises `1.588e-5 → 9.79e-4`, **confirmed**" is **inconsistent**: that ceiling (`R154_002` §1 row 5) was derived *by assuming* strong duality. Ceiling and gap stand or fall together. |
| 4 | **Theorem W** — Euler–Lagrange = finite-interval Wiener–Hopf, 2-dim inhomogeneity | `PROVED` | **PROVED**, with three wording repairs (§2): `k_λ` is a hypersingular distribution, not an integral kernel; "Krein–Gohberg index **ill-posed**" → *the symbol is non-elliptic, the index is **undefined*** (the corpus's own careful wording, `115_17:103`); "the pure-Γ case is **exactly solvable**" is overstated. |
| 5 | sign-change counts `3` (`½log3`, last at `10.5310`), `11` (`log 2`, last at `46.1291`) | datum | **REPRODUCED** (`repairs2.py` rerun, identical to `10⁻⁴`). |
| 6 | Theorem S1 (`φ ∈ CBF`), S2 (`ν = Σ_k e^{−(2k+½)|u|}`, CM, pure-jump) | `PROVED` (new) | **PROVED.** Algebra re-derived in closed form and numerically (diff `0.0e0` in double precision, §3). |
| 7 | corpus row 1: "`subordinat*` / `Bernstein function`: **no hit**, new" | new | **REFUTED.** `05-meta-and-planning/ABCD-CLOSURE-PLAN/PLAN.md:840` already states *"archimedean exponent is a complete Bernstein function of τ² ⇒ subordinate BM ⇒ subordination upper bound"* (the lead's own round-2 anchor, also in `R154_003 §0`), and `04-papers/37-.../main.tex:2673,3671` uses "Bernstein function" and cites Schilling–Song–Vondraček. **The statement is the lead's; the builder's contribution is the proof.** Credit line must be corrected. |
| 8 | phase-64 §5 (archimedean factor = OU/Hermite **diffusion**) is false | `PROVED` (corrects corpus) | **UPHELD with a caveat** (§4): correct about `L_∞` (no Gaussian part, `φ(x)/x → 0`); phase-64 wrote "*in the prolate scaling*", so the two objects were never asserted equal. Correct verdict: **the identification is untenable and `(★★)` has no diffusion to draw `ρ_∞` from**; "falsified" is one notch too strong. |
| 9 | Theorem S3, `λ_min ≤ C₀ + 2Σw + φ((3π/2T)²)` = `1.2911` / `2.3268`; FATAL check | `PROVED` | **CONFIRMED, FATAL PASSED.** Own recomputation: `1.291108` and `2.326752`, both `> 0`. Min–max + `E_P ≤ 4Σw‖F‖²` + Song–Vondraček are each correct and correctly oriented. Sharpened `1.0876` / `0.1000` reproduced (`1.000028e-1`). |
| 10 | "lead's `9.87` is the factor 2 applied twice; the target is `7.62100976`" | correction | **CONFIRMED EXACTLY.** Own: `2Σw − C₀ = 6.352441563` (`½log3`), `7.621009764` (`log 2`); `2Σv − C₀ = 9.869836109` = the lead's `9.87`. |
| 11 | "verified against the assembled operator … reproducing the identity to `10⁻⁷`" | verification | **REFUTED as a verification** (§5.1). `structure.py` prints `λ − C₀ + 2Σw` against `2Σw − C₀`; the difference is *identically* `λ`. Nothing about `E_Γ + E_P` is tested. (The identity itself is correct — re-derived by hand in §5.1 — so no damage beyond the claim.) |
| 12 | §2.3 "Verified (`structure.py`, Galerkin `K = 700`, `taumax = 2·10⁴`): `λ_{1..6}(E_Γ) = 3.5365,…`" | `PROVED`/numeric | **MISATTRIBUTED.** `structure.py` runs `K = 140`, `taumax = 4000` and prints the **`P_T`-constrained** values `5.4571, 5.7561, …`; the quoted `3.5365, …` come from `phase.py`'s hard-coded `TRUE` dict. The numbers themselves are right (own Galerkin, `K = 300/500/700`, §6) and `λ_n(E_Γ) ≤ φ(μ_n)` holds; the slack is **`1.7–23%`**, not "`3–25%`". |
| 13 | R1 eigenvalues `9.89281e-4` vs `1.62041e-5`; `1.08690e-7` vs `5.24909e-10`, moment diagnostics | repaired | **REPRODUCED to all printed digits** (`repairs2.py` rerun). The `𝒦^{prim}` ⟺ `M_± = 0` equivalence is **checked independently** (§5.2: `ord(Φ̂, ±i/2) = 2·ord(F̂, ±i/2)`, so the order-≥2 condition is exactly `M_± = 0` — the parity step round 1 dropped). |
| 14 | R2 certificate `−3.02e-2`, "PROVED for the bound once the τ-inequality is verified", `O(1/τ)` tail | `DIAGNOSTIC-NUMERIC` / `PROVED` | **VALUES REPRODUCED, PROVABILITY PREMATURE AT THE PARAMETERS USED** (§7). The tail formula is rigorous, but at `τ_max = 60` it evaluates to **`−4.23` and `−4.92`** — the table silently omits the tail column, so those runs certify only `λ ≥ −4.9`. **Repaired by the auditor**: at `τ_max = 10³` the tail is `+3.7153` and the LP value is unchanged (`−3.4567e-2`), so the bound is provable after all — but it was not proved in the round, and the conclusion (`½log3` does not close) is unaffected. |
| 15 | "the a.c. class is worse than atoms; that is the price of provability" | narrative | **HALF TRUE.** Reproduced (`−9.8217e-2 → −3.4584e-2` with the second multiplier, `TV 162.9 → 168.2`, `β₀ = 1.906 → 6.193`, `β₁ = −8.203`, all to 5 digits). But it is not yet *provable* (row 14), so the stated trade-off is not yet bought. |
| 16 | `lp_atom.py` unfinished; predicted `≈ −4e-4 … −1e-3` | labelled a prediction | **ACCEPTED as labelled.** Note also `lp2.log` and `lp3.log` are **0 bytes**: §4's table has no evidence in the repository. The auditor reproduced rows 1–2 independently; rows 3–5 are **underspecified** (see §7). |
| 17 | C2 phase-shift validation `(2−α)π/8` to `10⁻⁸`, Cauchy-interval `O(1/n)` errors | `PROVED`/`DIAGNOSTIC` | **REPRODUCED EXACTLY** (`phase.py` rerun): `0.58904785/0.39269856/0.19634928/0.03926986/0`, identical at `μ = 1` and `3.7`; Cauchy errors `+2.03e-2, −5.90e-3, +2.96e-3, −1.76e-3`. |
| 18 | C2 errors `1.4e-2` (n=1), `1.1e-2` (n=2); "five orders short" | `DIAGNOSTIC-NUMERIC` | **REPRODUCED**, incl. own independent Galerkin (§6). "Five orders short" is **fair**. Headline spin: the `n = 1` absolute error at `½log3` is `3.98e-2`, not `1.4e-2`; the abstract quotes the smaller of the two. |
| 19 | `λ_min` quoted as `1.08690e-7` (§3) and `1.076e-7` (§2.1); `9.89281e-4` and `9.834e-4` | — | **INCONSISTENT INSIDE THE DOCUMENT.** These are `K = 120` and `K = 140` Galerkin values, i.e. **upper bounds** converging from above. Must be labelled as such everywhere. |
| 20 | FATAL rule, no sign beyond `log 2`, no ζ-input | — | **COMPLIANT.** Every upper bound computed is `> 0`; no zero-free region, moment import or ζ-zero enters; the `log 2` sign is deferred to Paper 42. |
| 21 | corpus grep for the dual/complementary-slackness idea | — | **NEW, CONFIRMED.** `grep "complementary slackness" → 0 hits`; `"duality gap" → only R154_004`; `"not attained"/"no se alcanza"` hit 20 places, **all** about a different object (`sup s(f,f)/‖f‖² = 0` on `D°∖rad`, `σ(Eff)`, Pontryagin defect, §5 of paper 37). No prior statement that *this* dual is unattained. |

---

## 1. Theorem O, rederived

**The proof is correct.** Rederivation, with every step checked:

1. `A_T` has compact resolvent on `P_T`: the form norm `∫(1 + φ(τ²))|F̂|²` with `φ(τ²) ≍ log|τ|` controls
   `∫_{|τ|>R}|F̂|² ≤ 1/log R`, and on `supp F ⊂ [−T,T]` the family `{F̂}` is equicontinuous; hence the form domain embeds
   compactly in `L²(−T,T)` and a minimiser `F_★ ≠ 0` exists. The divergence of `φ` is only logarithmic but that suffices.
2. `(2π)^{-1}∫ D|F̂_★|² = 0` with `D = σ_T + ν̂ + Σβ_jĝ_j − λ_min`: `∫ν̂|F̂_★|² = ∫ν\,c_{F_★}` vanishes because
   `supp c_{F_★} ⊆ [−2T,2T]`, `supp ν ⊆ {|u| ≥ 2T}` and `c_{F_★}(±2T) = 0` by continuity (so an atom exactly at `±2T` is
   harmless — worth saying); `∫ĝ_j|F̂_★|² = ∫g_j c_{F_★} = 0` because `c_{F_★}/‖F_★‖² ∈ 𝒦^{prim}` (checked in §5.2).
3. `inf D ≥ 0` + `∫D|F̂_★|² = 0` ⟹ `D = 0` off the zero set of `F̂_★`, which is discrete (Paley–Wiener), and `D` is
   continuous ⟹ `D ≡ 0`.
4. Inverse Fourier transform, restricted to `{0 < |u| < 2T}`, where `ν = 0` and `δ_0 = 0`:
   `Σ_jβ_jg_j(u) = ν_tot(u) + Σ_{log n < 2T}(v_n/2)(δ_{log n} + δ_{−log n})`. Signs check out: `m(τ) = C₀ + ∫_0^∞(1−\cos τu)K(u)du`
   (verified to `10⁻¹²`, §3), so `m̌ = −ν_tot` away from `0` with `ν_tot = K/2`; `−Σv_n\cos(τ\log n)` transforms to
   `−Σ(v_n/2)(δ_{±\log n})`. Bounded continuous `=` `1/(2u)`-singular `+` atoms: contradiction. **∎ correct.**

**Required repairs to the statement.**
- **Class of `ν`.** "any even signed measure with `supp ⊂ {|u| ≥ 2T}`" must be **finite** (`‖ν‖_{TV} < ∞`), otherwise `ν̂`
  need not be a function and step 3 has no continuity. State: *`ν` a finite even signed Borel measure*. (The LP class of §4
  is a fortiori finite.)
- `g_j`: real, even, continuous on `[−2T,2T]`, annihilating `𝒦^{prim}` — as written. Note the class is **affine**, not a
  subspace; that is harmless here but should be said.
- "`< strictly`" is **correct**: the proof yields `inf D < 0` for each *individual* `(ν, β)`. Equality "in a limit" is not
  excluded and is precisely the open zero-duality-gap question. The builder states this correctly.
- `v = 0`: **the theorem does apply**, and there is no conflict with Kwaśnicki. Kwaśnicki solves the *eigenvalue problem*;
  Theorem O says a certain *linear-programming dual* has no maximiser. Even a completely solved spectral problem can have a
  non-attained LP dual; the obstruction is the `1/(2u)` singularity of the Lévy density against a class of test objects that
  is uniformly bounded near `u = 0`.

**What Theorem O rules out, exactly.** That any single `(ν, β_0,…,β_J)` in the class achieves
`inf_τ[σ_T + ν̂ + Σβ_jĝ_j] = λ_min`. Equivalently: the dual supremum, *if* it equals `λ_min`, is not attained.

**What stays OPEN.** (i) Zero duality gap (`sup = λ_min`). (ii) — and this is the point the write-up buries —
**whether a certificate can prove the sign.** The programme needs `λ_min ≥ 0`, not `= λ_min`. Since `λ_min > 0` at both
`T`'s (`9.8e-4`, `1.1e-7`), any certificate with value in `(0, λ_min)` suffices, and Theorem O forbids none of them.
**Theorem O is therefore an obstruction to *identification*, not to *proof*, and the abstract's "no certificate of the
outside-window type can ever be exact" must not be allowed to read as "the certificate route is closed".** The honest
corollary is weaker and still useful: *any successful certificate is strictly suboptimal, so its construction is a
quantitative approximation problem with a rate, not a variational problem with a solution* — which is what §7(c) says and
what the abstract does not.

---

## 2. Theorem W

**Proved.** The stationarity argument is right: `P_T = \ker M_− ∩ \ker M_+` has codimension `2` in `C_c^∞(−T,T)`, the
distribution `(𝒜−λ)F` restricted to `(−T,T)` annihilates it, hence lies in `span\{e^{t/2}, e^{−t/2}\}` there; the
unconstrained part outside is `H`. The `P_T` of Paper 42 (`main.tex:4085–4087`) is exactly `\ker M_− ∩ \ker M_+`, and the
symbol bookkeeping matches Paper 42's `A_T = G_{Γ,T} − m_0 I − Σ(Λ(n)/\sqrt n)(S_{\log n}+S_{−\log n})` with
`m_0 = \logπ + γ + π/2 + 3\log2 = \logπ − ψ(¼)`, so `g_Γ − m_0 = \mathrm{Re}\,ψ(¼+iτ/2) − \logπ = m(τ)` — **verified**.

**Repairs.**
1. `∫_{−T}^{T}k_λ(t−s)F(s)ds` is an abuse: `k_λ = (C₀−λ)δ_0 − ν_tot(u) − Σ(v_n/2)δ_{±\log n}` is **hypersingular**
   (`ν_tot ∼ 1/(2u)`). Write the equation as `(𝒜−λ)F = α\cosh(t/2)+β\sinh(t/2)` on `(−T,T)` in the sense of distributions,
   or as the principal-value/Dirichlet-form identity. As printed it is not defined for generic `F ∈ L²`.
2. "**the Krein–Gohberg index is ill-posed**". The corpus source, `115_17:103–110`, says it better:
   *"the symbol … is real and changes sign, so it passes through 0 and has no winding number; the classical factorization
   `a = a_+a_-` and its index are undefined."* The correct statement is **non-ellipticity ⟹ the theory does not apply and
   the index is undefined**, not "ill-posed". The builder already flags this as a citation, not a theorem; keep that.
3. "**the pure-Γ case is exactly solvable**" — overstated. Kwaśnicki gives an exact *half-line* Wiener–Hopf factorization
   and a *two-term asymptotic* on the interval with `O(1/n)` error; §5's own table shows a `1.4·10⁻²` error at `n = 1`.
   Replace with "the half-line problem for `φ(ξ²) − λ` factorizes explicitly; the interval problem has a two-term law".
4. The sentence "the primes are precisely what destroys the factorisation by inserting `2·#\{contacts\}` extra sign changes"
   is a nice slogan but the counts do not match it (`3` at `½log3` with one contact, `11` at `log 2` with two). State the
   counts, drop the formula.

---

## 3. Structure (S1, S2) — confirmed

The algebra is exact and I confirm it in closed form:
`¼/\sinh(u/2) + ¼/\cosh(u/2) = ¼(\cosh+\sinh)/(\sinh\cosh)|_{u/2} = ¼ e^{u/2}/(½\sinh u) = e^{−u/2}/(1−e^{−2u}) = Σ_{k≥0}e^{−(2k+½)u}`. ✓
Numerically the two sides agree to the last bit (`diff = 0.0e0` at `u = 0.05, 0.3, 1, 2.5, 5`). Complete monotonicity is
immediate from the series. `φ` vs digamma: `7.8e-13` at `x = ¼`, `1.4e-10` at `x = 46.2` (series truncation, not error).
`CBF`: each `(1/a_k)x/(x+4a_k²)` is CBF, the cone is closed under locally uniform limits, terms are `O(k^{−3})` ✓.

**Normalisation caveat (must be fixed).** §2.1 calls `ν = ¼/\sinh + ¼/\cosh` "*the corpus kernel of `R129_007:33`,
**exactly**, with no renormalisation*". `R129_007:33` writes `K(t) = ¼[1/\sinh(t/2)+1/\cosh(t/2)]` for the **kernel `K`**,
whereas the correct Lévy–Khintchine kernel in `m(τ) = C₀ + ∫_0^∞(1−\cos τu)K(u)du` is `K = ½/\sinh + ½/\cosh`
(own check: `m(1) = −2.025146193103` vs `C₀ + ∫ = −2.025146193103`; `τ = 5` likewise to `10⁻¹²`), and `ν = K/2`.
So the two expressions coincide **numerically by a factor-of-two coincidence between `R129_007`'s `K` and this round's `ν`**,
not because they are the same object. Either `R129_007:33` is off by `2` or the identification is spurious; the round-1
`PLAN.md` line already uses `½/\sinh + ½/\cosh`. Resolve and say which.

---

## 4. Phase-64 §5 — quoted and judged

Exact quote (`03-research/phase-64-connes-route/CURVATURE-computation.md`, §5):
> "The archimedean generator `L_∞` is a **diffusion** (second-order, the Ornstein–Uhlenbeck/Hermite operator in the prolate
> scaling), which satisfies a genuine `CD(0,N)` condition with finite dimension `N` and, after the prolate confinement, a
> Bakry–Émery `CD(ρ_∞,∞)` with `ρ_∞ > 0`."

**Judgement.** S1–S2 establish that the archimedean Weil multiplier is `φ(τ²)` with `φ(x)/x → 0`, hence the
Lévy–Khintchine triple has **zero Gaussian component**: `L_∞` is pure-jump. Therefore the identification of `L_∞` with a
second-order OU/Hermite operator is **untenable**, and `(★★)` as written has no diffusion from which to draw `ρ_∞ > 0`.
This is a genuine correction of the corpus and the builder is right to record it. **Caveat:** phase-64 wrote "*in the
prolate scaling*", i.e. it was pointing at a prolate-confined model operator, never asserting `L_∞ = ` OU. So the correct
label is **"the identification is untenable; the Bakry–Émery route as written in §5 is closed"** — which the builder's own
following sentence says — rather than "phase-64 §5 is false". Also worth adding: `CD(ρ,∞)` is *not* meaningless for jump
generators; what dies is the specific additivity argument that borrowed `ρ_∞` from a diffusion. Adjust the verdict-table
row from "**is false**" to "**the diffusion identification is untenable; `(★★)` closed as stated**".

---

## 5. Bookkeeping

### 5.1 The identity, and the vacuous "verification"
Re-derived by hand: `⟨A_TF,F⟩ = (2π)^{-1}∫m|F̂|² − Σv_nc_F(\log n)`; `E_Γ = (2π)^{-1}∫(m−C₀)|F̂|²`;
`E_P = 2Σw_n‖F‖² − Σv_nc_F(\log n)`; subtracting gives the stated identity **exactly**. ✓
But `structure.py`'s "check" column is `λ − C₀ + 2Σw` compared against `2Σw − C₀`: the difference is `λ` by definition.
Rerun output: `check = 6.35342496` vs `target = 6.35244156` (difference `9.83e-4 = λ_min`), and
`7.62100987` vs `7.62100976` (difference `1.08e-7 = λ_min`). **The "reproducing the identity to `10⁻⁷`" is the value of
`λ_min` at `log 2`, nothing else.** Delete the claim or replace it with a real test (evaluate `E_Γ(F)` and `E_P(F)` on a
random `F` by quadrature and compare with `⟨A_TF,F⟩`).

### 5.2 `𝒦^{prim}` ⟺ `M_± = 0` — independently checked
For `Φ = c_F`, `\hatΦ(z) = \hat F(z)\hat F^*(−z)`, so `\mathrm{ord}(\hatΦ, ±i/2) = 2\,\mathrm{ord}(\hat F, ±i/2)`. The two moment
conditions are `\hatΦ(i/2) = 0` and `\hatΦ'(i/2) = 0`, i.e. order `≥ 2` at `i/2`, and by evenness also at `−i/2`; hence
`\hat F(±i/2) = 0`, i.e. `M_+ = M_- = 0`. (A direct moment computation gives `∫Φ\cosh(u/2) = M_+M_-` and
`∫Φ\,u\sinh(u/2) = M'(½)M_- − M_+M'(−½)`, which *looks* weaker; the parity/order argument closes the gap, and that parity
step is exactly what round 1 dropped.) **R1 is correct.**

### 5.3 Constants
Own, `mp.dps = 30`: `C₀ = −5.3721834192256654`; `w₂ = 0.4901290717`, `w₃ = 0.6342841006`;
`2Σw − C₀ = 6.3524415627` (`½log3`), `7.6210097639` (`log 2`); `2Σv − C₀ = 9.8698361086`. **The builder's diagnosis of the
lead's `9.87` is exactly right.**
Subordination: `μ₃ = 73.59585 / 46.22015`, `φ(μ₃) = 5.683033 / 5.450109`, `UB = 1.291108 / 2.326752`. **Both `> 0`:
FATAL check passed.** Sharpened bound reproduced: `1.087606` and `1.000028e-1`. The chain
(min–max on a codim-2 subspace of a 3-dim span) → (`λ₃(E_Γ) ≤ φ(μ₃)`, Song–Vondraček, correctly oriented) → (`E_P ≤ 4Σw`)
is valid at every step.

---

## 6. C2, reproduced independently

Own Galerkin of the pure-Γ killed form (`gamma_matrix − C₀G`, unconstrained), convergence from above:

| `T` | `K, τ_max` | `λ₁ … λ₅` |
|---|---|---|
| `½log3` | `300, 2e4` | `3.537370, 4.990898, 5.493345, 5.839373, 6.087596` |
| `½log3` | `500, 2e4` | `3.536776, 4.990427, 5.492890, 5.838929, 6.087157` |
| `½log3` | `700, 4e4` | `3.536519, 4.990222, 5.492692, 5.838735, 6.086964` |
| `log 2` | `700, 4e4` | `3.243609, 4.749751, 5.258975, 5.605308, 5.854046` |

— identical to the builder's "true `λ_n`" column. Residual Galerkin drift `K = 500 → 700` is `≈ 2.6·10⁻⁴`, two orders below
the `1.4·10⁻²` law error, so **the C2 conclusion is safe**: the two-term law is *not* accurate to `10⁻³` at `n = 1`, and
against a `10⁻⁷` target it is **five orders short**. Fair. Formula validation reproduced exactly (`(2−α)π/8` to `5·10⁻⁸`,
`μ`-independent; Cauchy-interval errors alternating `O(1/n)`). `ϑ(μ) ↓ π/4` reproduced (`0.87209, 0.81261, 0.79813,
0.79300, 0.78852, 0.78641` at `μ = 2, 4, 6.8, 10, 20, 50`); the limit is **not proved**, correctly labelled.

---

## 7. R2 / the certificate — reproduced, and the provability claim refuted

**Own reimplementation** (independent driver, same closed forms), at the parameters the write-up states
(`U = 14, du = 0.1, dτ = 0.02, τ_max = 60, fine 40×`):

| multipliers | LP | fine | `TV` | `β₀` | `β₁` | **tail bound for `τ ≥ τ_max`** |
|---|---|---|---|---|---|---|
| `h⁽⁰⁾` only | `−9.821677e-2` | `−9.967545e-2` | `162.9` | `1.906` | — | **`−4.2261`** |
| `h⁽⁰⁾, h⁽¹⁾` | `−3.458358e-2` | `−4.378746e-2` | `168.2` | `6.193` | `−8.203` | **`−4.9164`** |
| `h⁽⁰⁾,h⁽¹⁾`, `du = .05, cap = 50` | `−4.720896e-5` | `−2.641577e-1` | `1.59e4` | `2.007` | `−0.0047` | **`−530.25`** |

Rows 1–2 match `R154_004` §4 to every printed digit — **the values are confirmed**, and so is the `2.7–2.9×` worth of the
second multiplier and the "does not close" conclusion.

**But**: the tail column, which the write-up's table omits, is **negative**. The tail inequality is itself sound — I checked
each term: `|ν̂| ≤ 2TV/τ` by parts on a piecewise-constant density; `|h⁽⁰⁾| ≤ 2\cosh T/τ + \sinh T/τ²`;
`|h⁽¹⁾| ≤ 8T\sinh T/τ` (boundary `4T\sinh T/τ` plus `∫|f'| = 2L\sinh(L/2)`); `m` increasing. It is simply **not yet strong
enough at `τ_max = 60`**: with `TV ≈ 165` the term `2TV/τ_max ≈ 5.5` swamps `m(60) − Σv_n ≈ 1.3`. Hence the *certified*
statement from these runs is `λ_min ≥ −4.92`, not `−3.02·10⁻²`. **`τ_max ≈ 10³` is needed**, and I verified that this repair costs nothing: own run at
`U = 14, du = 0.1, cap = 5, two = True, dτ = 0.05, τ_max = 1000` gives `LP = −3.456679e-2` (unchanged from `−3.458358e-2`),
`TV = 169.6`, `β₀ = 6.194`, `β₁ = −8.203`, and **`tail ≥ +3.7153`**. So the two-multiplier bound *is* rigorously provable at
`≈ −3.46·10⁻²` once `τ_max` is raised — still `30×` the target `+9.79·10⁻⁴`, so the negative conclusion is unaffected;
only the write-up's claim to have already proved it is premature. (The `fine = −9.35·10⁻²` in that run is the coarser
`dτ/40` verification grid, not a change in the certificate.)
Second gap: the "fine grid" check is a *grid evaluation*, with no Lipschitz/interval bound. Row 3 shows how badly that can
fail (`LP = −4.7e-5`, fine `= −0.264`, `TV = 1.6e4`) — and it is exactly the degeneracy Theorem O predicts. For a
**negative** conclusion the grid error is in the safe direction, so §4's honest negative stands; for any future **positive**
certificate it will not.
**Second reproduction, `lp2.py` verbatim** (its committed `__main__`: `U = 14, du = 0.05, dτ = 0.01, τ_max = 120`, which is
*not* the parameter set §4's header states): `h⁽⁰⁾` only gives `LP = −9.449030e-2`, fine `−1.022215e-1` at `τ = 49.476`,
`TV = 732.1`, `β₀ = 1.909`, **tail `−10.2692`**; with both multipliers `LP = −2.787201e-2`, fine `−4.283019e-2` at
`τ = 0.865`, `TV = 586.2`, `β₀ = 11.82`, `β₁ = −12.52`, **tail `−8.2932`**. The certificate value improves slightly on the
reported `−3.02e-2`/`−3.46e-2` as the density grid is refined, the multiplier magnitudes and `TV` grow (the Theorem-O
degeneracy again), and the tail gets *worse*, not better, because `TV` grows faster than `τ_max`. Confirms §7's diagnosis
and the `τ_max ≈ 10³` repair.

Third: rows 3–5 of §4's table are **underspecified** (`du`, `dτ`, `τ_max` differ from both `lp2.py`'s `__main__` and the
stated header), and `lp2.log`, `lp3.log` are **0 bytes**. The repository contains no evidence for them.

---

## 8. Required repairs (binding for round 3)

**RA (Theorem O, scope).** Rewrite the abstract sentence and §7(ii) consequences. Add explicitly: *"Theorem O forbids
attainment; it does not forbid a certificate that proves `λ_min ≥ 0`, because `λ_min > 0` and any dual value in `(0,λ_min)`
suffices. The certificate route is not closed by Theorem O."* Demote the "decisive negative" framing.
**RB (Theorem O, class).** `ν` finite even signed measure; note `c_F(±2T) = 0`; note `𝒦^{prim}` is affine.
**RC (duality gap).** Remove the "class ceiling … confirmed" verdict row, or mark it conditional on strong duality — the
same strong duality the document labels `OPEN`.
**RD (tail).** Re-run §4 with `τ_max ≥ 10³` (verified by the auditor to cost nothing: tail `+3.72`, LP unchanged) and
**publish the tail column**; at `τ_max = 60` the runs certify only `λ ≥ −4.9`. Add a Lipschitz/interval bound for the
`[0,τ_max]` verification, or state that the grid check is not rigorous and is used only for a negative conclusion.
Commit the actual drivers and non-empty logs (`lp2.log`, `lp3.log` are 0 bytes).
**RE (Theorem W).** Distributional statement of `k_λ`; "index undefined / symbol non-elliptic" per `115_17:103`; withdraw
"exactly solvable" and the `2·#{contacts}` formula.
**RF (credit).** Correct corpus row 1: `PLAN.md:840` / `R154_003 §0` already state CBF ⟹ subordinate BM ⟹ the
subordination bound; paper 37 already uses "Bernstein function" and cites SSV. Label S1–S3 **"lead's statement, proved
here"**.
**RG (numerics hygiene).** Delete the vacuous identity "verification"; fix the `structure.py` attribution in §2.3 and the
`1.7–23%` slack; label all `λ_min` values as Galerkin **upper bounds** and quote one `K` consistently.
**RH (phase 64).** Soften "is false" to "the diffusion identification is untenable; `(★★)` closed as stated", keeping the
existing caveat sentence.
**RI (kernel normalisation).** Settle `R129_007:33`'s `¼` versus the Lévy kernel `K = ½/\sinh+½/\cosh`.

---

## 9. Honest reading

Theorem O is real, its proof survives hostile rederivation, and it is the kind of statement the phase's target admitted as
an alternative outcome — but it is **not** the obstruction theorem the write-up presents it as. The phase asked for a
closed-form law for `Λ_T` *or* a proof that the route cannot deliver one; Theorem O delivers something strictly weaker and
strictly softer: the outside-window dual has **no maximiser**, so `Λ_T` is a supremum over a class in which every element is
strictly suboptimal and every maximising sequence degenerates towards a measure that would have to reproduce the
`1/(2u)` singularity of the archimedean Lévy density inside a window where it is not allowed to live. That is an
obstruction to *identifying* `λ_min`, not to *bounding* it from below — and since the whole programme only ever needed
`λ_min ≥ 0`, which is a strictly interior condition, Theorem O closes nothing that was open. What `Λ_T` amounts to after
round 2 is therefore: a supremum of a concave problem over a compact convex affine slice `𝒦^{prim}_{2T}` of the
positive-definite cone, known to be **non-attained in its dual**, characterised **exactly** by a finite-interval
Wiener–Hopf equation with a non-elliptic real symbol (Theorem W) whose prime-free case has an explicit two-term spectral
law with a Kwaśnicki phase shift `ϑ ↓ π/4` (accurate to `10⁻²`, five orders short of the sign), and pinned between two
*proved* `O(1)` bounds — `λ_min ≤ 1.2911` at `½log3`, `≤ 2.3268` at `log 2`, both positive, FATAL check passed. The round's
real gains are S1–S3 and Theorem W; the certificate section is an honest negative whose provability claim has not yet been
bought; and the decisive open item is unchanged since round 1 — a lower bound for `ℰ_T` near the contact point.
