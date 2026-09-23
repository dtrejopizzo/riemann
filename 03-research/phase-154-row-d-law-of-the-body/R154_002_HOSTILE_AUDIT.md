# R154.002 — Hostile audit, round 1 of phase 154: is `Λ_T(v)` a genuine object?

*Auditor: Opus 5 (1M). 2026-09-20. Target: `R154_001_BUILDER_ROUND1.md` and its scripts, against
`R154_000` (incl. §4), Paper 42 `main.tex:4072–4230`, `R129_007`, `114_d_88`, `R153_016 §2.3`,
`R153_019 §3,§8,§5`, `R153_021`. Own scripts: `scripts/audit/` (`chk1`–`chk7` reproduced below;
`core.py` of phase-153 round 6 reused unchanged).*

**Headline.** The *identity* is right; the *class* is wrong. Theorem A's pointwise identity
`⟨A_T(v)F,F⟩ = C_0 + 𝔈(c_F) − Σ v_n c_F(log n)` is exact, elementary and verified to `10⁻²⁶` at the
symbol level. But the class `𝒦_{2T}` over which the builder takes the supremum is **strictly larger
than the autocorrelations of primitive `F`**: the builder collapsed the *double* zero of `Φ̂` at `±i/2`
(which `R153_016 §2.3` states correctly, in those words) into a *single* linear condition. The object he
has defined therefore computes `λ_min` on `ker M_− ∪ ker M_+`, not on `P_T`, and that number is
`1.5878·10⁻⁵` at `½log3` (not `9.7915·10⁻⁴`) and `5.171·10⁻¹⁰` at `log 2` (not `1.0675·10⁻⁷`) —
too small by `62×` and `206×`. The `10⁻⁸`/`10⁻¹²` verification in `levy.py` used
`core.Body(..., constrained=True)`, i.e. the **correct** `P_T`, so it tested the pointwise identity and
never tested the class. The repair is one line and is given in §R1.

---

## 1. Verdict table

| # | claim | verdict | reason |
|---|---|---|---|
| 1a | Lévy–Khintchine: `m(τ) = Reψ(¼+iτ/2) − logπ = C_0 + ∫_0^∞(1−cosτu)K(u)du`, `K(u)=2e^{3u/2}/(e^{2u}−1) = ½/sinh(u/2)+½/cosh(u/2)`, `C_0 = ψ(¼)−logπ` | **STANDS** | rederived analytically in closed form (§2); numerically `|Δ| < 5·10⁻²⁶` at `τ = 0.3, 1, 2.5`, `1.1·10⁻¹⁴` at `τ = 6` (quadrature). Normalisation against Paper 42's `m_0 = logπ+γ+π/2+3log2` and `g_Γ = Reψ(¼+iτ/2) − ψ(¼)` checked exactly: `g_Γ − m_0 = Reψ(¼+iτ/2) − logπ`. |
| 1a′ | "no negative-definiteness / Lévy statement in the corpus" | **RESTATEMENT (partial)** | `phase-64/CURVATURE-computation.md:18–19,100` already reads the Weil generator as a Beurling–Deny/Lévy form and names *"the continuous archimedean part (the `Reψ(¼+it/2)−logπ` density)"* of the Lévy measure; `phase-104/104_21 §4` computes a Lévy density of the Gamma factor in another normalisation. **New here**: the closed form `½/sinh+½/cosh` as that density, the exact constant `C_0`, `𝔈`, `R(T)`. The corpus-check row of §1 must be corrected. |
| 1b | `𝒦_{2T}` = normalised p.d. functions supported in `[−2T,2T]` = autocorrelations of `F` on `[−T,T]` | **STANDS, citation wrong** | the theorem is **Krein (1940) / Boas–Kac (Duke 11 (1945) 45–65)**, 1-D, `Φ` continuous p.d. with `supp ⊂[−2T,2T]` ⟹ `Φ = c_F`, `supp F ⊂` an interval of length `2T`. "Krein–Fejér" is not the name of this factorisation (Fejér–Riesz is the trigonometric-polynomial case). Cite Boas–Kac. |
| **1c** | **the sup ranges over primitive `F`** | **REFUTED as written; REPAIRABLE** | see §R1. `∫Φ cosh(u/2)du = 0` ⟺ `M_+(F)M_−(F) = 0`, i.e. **one** of the two moments vanishes. Primitivity needs the second condition `∫Φ(u)·u·sinh(u/2)du = 0` (the derivative of the double zero). Numerically (`chk7`, `K=120`, `T=log2`): for `F ∈ P_T`, `∫Φcosh = −2.7·10⁻¹⁴`, `∫Φ u sinh = 3.4·10⁻¹⁷`; for `F ∈ ker M_−` only, `∫Φcosh = −2.7·10⁻¹⁴` (**still zero**) but `∫Φ u sinh = −2.1·10⁻³`. The builder's own source, `R153_016 §2.3`, says "`Φ(±i/2) = 0` (**double zeros**)"; the parenthesis "(by evenness they are one real condition)" in R154_001 §4.1 is the error: evenness identifies the two *order-0* conditions, it does not supply the order-1 one. |
| 1c′ | `10⁻¹²` verification was against the `P_T` value | **STANDS (and is therefore not a test of the class)** | `levy.py:check` calls `core.Body(T,Kdim,contacts,constrained=True)`; `core.py:91` projects onto `null_space(moments(T,K,[−0.5,0.5]))`, i.e. **both** moments. The check validates Theorem A vector-by-vector only. |
| 1d | prime terms `Σ v_n Φ(log n)`, factor 2 | **STANDS** | `⟨(S_a+S_{−a})F,F⟩ = 2c_F(a)` since `c_F` is even; `v_n = 2Λ(n)/√n` against Paper 42 `(4120)`'s `Λ(n)/√n`. Consistent throughout (`v_2 = 0.98025814`, `v_3 = 1.26856820`, `v_2+v_3 = 2.24882634`, matching `R153_016:` `2Σw_n`). |
| 2 | Theorem A′: `x_0 = C_0 + 𝔈`, `W_T = epi(C_0+ℰ_T)`, `Λ_T = ℰ_T^*` | **STANDS**, with the class corrected, but **RESTATEMENT** of `R153_019 §2` | `R153_019:55–59` already has `h_{W_T}(−1,v) = −λ_min(...)` and "the body is the epigraph of a convex `Ψ_T` whose Legendre transform is the family of minimal eigenvalues". The *new* content is the identification of `Ψ_T` with `C_0 + ℰ_T`, `ℰ_T` = minimal Lévy energy — this is genuine and is the round's best result. |
| 3a | no measurable fibration for `T ≥ ½log3`; hyperfinite II₁ | **STANDS** (proof sketch correct) | dense subgroup translation on `R` is ergodic; induced relation on a finite-measure set is ergodic, hence non-smooth, hence no measurable transversal; `Z²` amenable ⟹ hyperfinite (Connes–Feldman–Weiss). `RESTATEMENT`-link to `114_d_88:29–38` is fair. |
| 3b | "trace `τ(x) = (2T)^{-1}⟨x·1,1⟩`" | **REFUTED (minor)** | that is not a trace on `W^*(R_Λ|_{I_T})`: it gives `τ(P_TS_aP_T) = c_1(a)/2T ≠ 0`, whereas the canonical trace is `τ(x) = (2T)^{-1}∫_{I_T}x(t,t)dt`, which vanishes on every `a ≠ 0` partial isometry. Also `M_T` is only a *subalgebra*; it is not shown to be a factor, and "the IDS has no atoms" is asserted, not proved. |
| 3c | Prop. 2.1 spectral weights `(0.2925, 0.4150, 0.2925)` at `½log3` | **DOWNGRADE** | those are fractions of *transversal length*, not of the spectral (dimension) measure. `∫k(s)ds = 2·log(3/2)+1·log(4/3) = log3 = L`; the density of states is `(0.3691, 0.2619, 0.3691)`. The graph types and frequencies `58.50%/41.50%` in `s` are correct. |
| 3d | "joint truncated top `1.05414` vs `‖B‖ = v_2+v_3 = 2.24883` (Kronecker)" | **REFUTED (two errors)** | (i) `max{v_2Φ(log2)+v_3Φ(log3)}` over the window is **`0.9009276`** (`chk3`, `K=200`, on `P_T` and unconstrained alike, agreeing to `10⁻¹⁵`), not `1.054143`. `R153_019:262` `−1.054143` is a **bound on `λ`**, not a contact maximum: `1.0535 = 0.9009276 + 0.1525744`, the second term being `−min x_0 = −λ_min(M_0|P_T)` (`min 𝔈 = 5.219609`, matching the builder's `5.2190`). (ii) `‖B_∞(v)‖ = v_2+v_3` is attained at `τ = 0` (`cos 0 = 1` for both); **no Kronecker argument is needed** and "approached but never attained" is false. The corrected headline is the deficit `2.24883 → 0.90093`. |
| 4a | `K` closed form, integrability, `𝔈` on the form domain | **STANDS, with a missing caveat** | `K(u) ~ 1/u` at `0`, `~2e^{−u/2}` at `∞`. The audit's objection ("`1−Φ = O(u²)` needs `F ∈ H¹`") **does not bite**: both sides of Theorem A are Tonelli integrals of nonnegative integrands (`1−Φ ≥ 0` since `|Φ| ≤ Φ(0)=1`; `1−cosτu ≥ 0`; `K ≥ 0`), so the identity holds in `[0,+∞]` for every `F ∈ L²`, and `𝔈(Φ) < ∞ ⟺ ∫log(2+|τ|)|F̂|²dτ < ∞ ⟺ F ∈ Q(M_0)`, which is *weaker* than `H¹`. The sup defining `Λ_T` is unaffected (non-form-domain vectors contribute `−∞`). **R154_001 should state this**; as written it asserts the identity with no domain remark. |
| 4b | `R(T) = log coth(T/2) + π − 2 arctan e^T`; `R(½log3) = 2.364155448`, `R(log2) = 2.025907507` | **STANDS** | antiderivatives verified; both closed values reproduced to `10⁻⁹`. |
| 5 | hand-proof numbers: `−1.267·10⁻³` at `½log3`, `−8.72·10⁻³` at `log2`; "structural or optimisation?" | **DOWNGRADE — the answer is BOTH, and the class ceiling is now computable** | LP reproduced independently (`chk6`): `U = 6`, `|c|_∞ ≤ 3`, `dτ = 0.01`, atom step `0.05` gives `LP = −2.4756·10⁻³` against the builder's `−2.4963·10⁻³` (✓), fine-grid `−3.63·10⁻³` (builder `−2.70·10⁻³`; the discrepancy is the verification-grid layout and confirms his own remark that the `τ`-grid is the limiting error). **The decisive point**: Theorem B's certificate class carries exactly *one* moment multiplier `β·h_T`, so by LP duality its supremum equals `λ_min` on `ker M_− ∪ ker M_+`, i.e. **`+1.5878·10⁻⁵` at `½log3` and `+5.171·10⁻¹⁰` at `log2`** — the class can *never* reach `9.79·10⁻⁴` or `1.07·10⁻⁷`. So Theorem B's "`= λ_min` by LP duality" is **false as stated**, the gap is `62×` structural at `½log3` and `206×` at `log 2` *before* any optimisation loss, and the optimisation loss on top is a further `≈80×` (`−1.27·10⁻³` vs a `+1.59·10⁻⁵` ceiling). |
| 6 | Theorem D (breakpoints `{½log(2^k3^l)}`, dense; 3-smooth integers = the `k,l ≥ 0` part) | **STANDS** | statement and proof correct; it does correct the blueprint's (B2). The "no kink detected" evidence is weak (two step sizes, second differences) but is labelled `DIAGNOSTIC-NUMERIC` — acceptable. |
| 7 | Hessian, rank-one curvature, "the apex is not a second-order datum" | **STANDS** | `∂λ/∂v_n = −x_n` (Feynman–Hellmann) and `½δᵀHδ = Σ_{k≠0}|⟨Σδ_nS_nF,F_k⟩|²/(λ−λ_k)` are the correct first/second-order formulae for `A = M_0 − Σv_nS_n`; `H ≺ 0` as required by concavity. Internal arithmetic checks out: `w_2 = 0.4901291`, apex `0.4901375` (`R153_019:200`) ⟹ measured offset `8.4·10⁻⁶`; `w_3 = 0.6342774`, apex `0.6342287` ⟹ `−4.9·10⁻⁵`; ratio `−5.8` ≈ the quoted `−6.5`. The conclusion is sound and is a genuine (negative) answer to (P153.16). |
| 8a | Theorem M (monotonicity in `T`) | **RESTATEMENT** | `𝒦_{2T} ⊂ 𝒦_{2T'}` is exactly the zero-extension argument already used in Paper 42 (`main.tex`, proof of `thm:certifiedendpoints`: *"Extension by zero … then proves every `0<T≤½log3`"*). True, clean, not new. |
| 8b | Theorem C (product semigroup, subadditive energy) | **STANDS but VACUOUS** | the inequality `1−Φ₁Φ₂ ≤ (1−Φ₁)+(1−Φ₂)` is correct. But the builder concedes the moment condition is not preserved, so the law lives on `𝒦⁰` — the class whose `λ_min` is `−2.17` / `−2.83` (`chk2`). No trial family it produces is admissible for the actual problem. |
| 8c | FATAL rule; no sign beyond `log 2` | **STANDS** | no zero-free region, no moment import, no `ζ`-zero input; §6 states explicitly that `log 2` remains certified only by Paper 42. |
| 8d | reported values `Λ_{½log3}(w_ζ) = −5.3712043`, `Λ_{log2}(w_ζ) = −5.3721833` | **REFUTED (arithmetic)** | Theorem A forces `Λ = C_0 − λ`. With `λ = 9.791586·10⁻⁴`, `Λ_{½log3} = −5.3731626`; the printed `−5.3712043` is `C_0 + λ` (sign of `λ` flipped). With `λ = 1.0675·10⁻⁷`, `Λ_{log2} = −5.37218352`, not `−5.3721833` (which lies *above* `C_0` and would give `λ < 0`). The sentence "both just below `C_0`" is right only for the corrected numbers. |

---

## 2. Rederivation of 1(a) (for the record, exact)

`ψ(z) = −γ + ∫_0^∞ (e^{−t} − e^{−zt})/(1−e^{−t})dt`. Subtracting the value at `z = ¼` and taking real
parts at `z = ¼ + iτ/2`,
`Reψ(¼+iτ/2) − ψ(¼) = ∫_0^∞ e^{−t/4}(1−cos(tτ/2))/(1−e^{−t})dt`.
Put `t = 2u`: `= ∫_0^∞ (1−cos τu)·2e^{−u/2}/(1−e^{−2u})du`, so
`K(u) = 2e^{−u/2}/(1−e^{−2u}) = 2e^{3u/2}/(e^{2u}−1)`.
With `x = e^{u/2}`: `2x³/(x⁴−1) = x/(x²−1) + x/(x²+1) = ½/sinh(u/2) + ½/cosh(u/2)`. ∎
Since `g_Γ − m_0 = Reψ(¼+iτ/2) − ψ(¼) − (logπ + γ + π/2 + 3log2) = Reψ(¼+iτ/2) − logπ` (using
`ψ(¼) = −γ − π/2 − 3log2`), the Paper-42 normalisation is exactly the builder's `m`. `C_0 = −5.37218341922567`.
Numerical check (`chk1`, mpmath `dps = 25`, `1/τ`-graded panels): `Δ = 0, −5.2·10⁻²⁶, 1.3·10⁻²⁶,
−1.1·10⁻¹⁴, −9.4·10⁻⁵` at `τ = 0.3, 1, 2.5, 6, 13.7` — the last two are quadrature, not the identity.

The moment symbol is also right: `∫_{−L}^{L}cosh(t/2)cos(τt)dt = 2[½sinh T·cos 2Tτ + τ cosh T·sin 2Tτ]/(τ²+¼) = h_T(τ)`
with `L = 2T`. `PROVED`.

## 3. The primitivity computation (1c), in full

For `A(β) := ∫F(t)e^{βt}dt` one has `∫c_F(u)e^{βu}du = A(β)A(−β)`. Hence
* order 0 at `β = ½`: `∫Φ(u)cosh(u/2)du = M_+(F)M_−(F)` — vanishes iff **at least one** moment vanishes;
* order 1: `∫Φ(u)·u·sinh(u/2)du = d/dβ[A(β)A(−β)]|_{β=½} = A'(½)A(−½) − A(½)A'(−½)`, which for
  `M_−=0, M_+≠0` equals `−M_+·∫F(t)te^{−t/2}dt ≠ 0` generically.

So `𝒦_{2T}^{prim} := {Φ : Φ` p.d., `Φ(0)=1`, `supp Φ ⊂ [−2T,2T]`, `∫Φcosh(u/2)du = 0`,
`∫Φ(u)u sinh(u/2)du = 0}`, equivalently `Φ̂ ≥ 0` of type `2T` with a **zero of order ≥ 2 at each of `±i/2`**.
Sufficiency: with double zeros at `±i/2`, a Boas–Kac factorisation can assign one zero at `i/2` **and** one at
`−i/2` to `F̂`, giving `F ∈ P_T`; with simple zeros exactly one of `M_±` can be killed.

**Damage (chk2, `K = 160`, exact shift blocks, `taumax = 4000`):**

| `T` | `P_T` (both) | `ker M_−` only | `ker M_+` only | unconstrained |
|---|---|---|---|---|
| `½log3` | `+9.791464·10⁻⁴` | `+1.587789·10⁻⁵` | `+1.587789·10⁻⁵` | `−2.166202` |
| `log2` | `+1.067543·10⁻⁷` | `+5.171401·10⁻¹⁰` | `+5.171399·10⁻¹⁰` | `−2.829058` |

So the builder's `Λ_T` as defined does *not* compute `λ_min` on `L²(−T,T)` (that is negative, as
`R153_019` says) — it computes the intermediate one-constraint value, positive but `62×`/`206×` smaller.
The sign survives; the margin does not.

## 4. Required repairs

**R1 (blocking).** Replace the definition of `𝒦_{2T}` in §4.1 by `𝒦_{2T}^{prim}` above (two linear
conditions / double zeros), cite `R153_016 §2.3` correctly, delete "(by evenness they are one real
condition)", and re-state Theorems A, A′, B over that class. Nothing in the *numerics* changes
(`levy.py` already used `constrained=True`).

**R2 (blocking).** Theorem B must carry **two** multipliers, `β_0 h_T(τ) + β_1 h_T^{(1)}(τ)` with
`h_T^{(1)}(τ) = ∫_{−2T}^{2T} t sinh(t/2)cos(τt)dt = ∂_a\{2[a sinh(2aT)cos2Tτ + τ cosh(2aT) sin2Tτ]/(a²+τ²)\}|_{a=½}`.
Only then is "the supremum equals `λ_min`" true. Re-run `dual.py` with the extra column; the class ceiling
rises from `1.59·10⁻⁵` to `9.79·10⁻⁴` at `½log3` and from `5.2·10⁻¹⁰` to `1.07·10⁻⁷` at `log 2`. This is a
`62×` free improvement and is the single most valuable action for round 2.

**R3.** Correct the two `Λ` values (§4.2) to `Λ_{½log3}(w_ζ) = −5.3731626`, `Λ_{log2}(w_ζ) = −5.37218352`.

**R4.** Replace `1.054143` in §2 by the true joint maximum `0.9009276` and drop the Kronecker sentence
(the sup `v_2+v_3` is attained at `τ = 0`). Keep `2.24883` as the untruncated norm.

**R5.** Correct the Prop. 2.1 spectral weights to `(0.3691, 0.2619, 0.3691)` (density of states) and
correct the corpus-check row 1 to a partial `RESTATEMENT` of `phase-64/CURVATURE-computation.md:100`.

**R6.** Fix the II₁ trace formula (or delete it) and mark "IDS has no atoms" as `OPEN`. Add the form-domain
remark of 4a. Cite Boas–Kac.

**R7 (labels).** `Theorem M` → `RESTATEMENT` (Paper 42 zero-extension). `Theorem C` → `PROVED, vacuous
for the constrained class`. `Theorem B` → `DOWNGRADE` until R2 is done. `Theorem A` → `PROVED` after R1.
`Theorem A′` → `PROVED (new content: Ψ_T = C_0 + ℰ_T)`, `RESTATEMENT` for the epigraph/Legendre frame.
`Theorem D`, `1a`, `4b`, §7 → unchanged.

---

## 5. Is `Λ_T` a genuine new object? — honest reading

Partly. What is genuinely new and genuinely proved is the *analytic identification of the first body
coordinate*: `x_0(F) = ψ(¼) − logπ + ∫_0^∞(1−c_F(u))K(u)du` with the explicit Lévy density
`K = ½/sinh(u/2)+½/cosh(u/2)`. That converts `R153_019`'s abstract epigraph `Ψ_T` into a concrete,
classical quantity — a window-constrained minimal Lévy energy at prescribed contact values — and it
finally explains, in one line, both the `log|τ|` growth of the archimedean symbol and where all of the
`T`-dependence sits (the elementary tail `R(T)`). That is more than a rewriting: `R153_019 §9.3` asked for
the law of the body and this answers it in the sense of *naming the functional*. What it is not, yet, is an
*object with an independent characterization* in the sense of `R154_000 §4(ii)`. `Λ_T = ℰ_T^*` is a
Legendre transform of a function nobody can evaluate; Theorem M is the old zero-extension monotonicity;
Theorem C's semigroup law is destroyed by the very constraint that makes the problem hard; Theorem D
proves that no recursion indexed by breakpoints can exist beyond `½log3`; and the one place where the
object was supposed to pay — the dual certificates — turns out, once primitivity is counted correctly, to
have a ceiling `62×` below the target at `½log3` and `206×` below at `log 2`, with a further `80×` of
optimisation loss on top. So `Λ_T` is at present a **faithful re-coordinatisation, not yet a computable
invariant**: it has an exact defining variational formula, no equation, no recursion, no closed value, and
no proved lower bound on `ℰ_T` anywhere near the contact point. Round 2's decisive test is R2: with the
second moment multiplier the dual class becomes *exactly* dual to `P_T`, and whether the hand certificate
then closes the `2.3×` gap at `½log3` is the honest measure of whether the object does work or only
records it.

---

## Appendix — independent LP reproduction (`scripts/audit/chk6.py`)

| `T` | contacts | `U` | `|c|_∞` | my LP | builder's LP | my fine grid | builder's fine grid |
|---|---|---|---|---|---|---|---|
| `½log3` | `{2}` | `6` | `3` | `−2.47563·10⁻³` | `−2.4963·10⁻³` | `−3.627·10⁻³` | `−2.699·10⁻³` |
| `½log3` | `{2}` | `14` | `3` | `−1.93727·10⁻⁴` | `−1.9382·10⁻⁴` | `−1.536·10⁻³` | `−1.267·10⁻³` |

The LP values reproduce to 4 significant figures; the fine-grid values differ by `20–35%`, which
independently confirms the builder's own caveat that the `τ`-grid, not the certificate class, is the
current limiting error **at that level** — but the class ceiling of §1 row 5 (`+1.59·10⁻⁵`) is what
actually stops the scheme, and it is reached by neither. **The two-multiplier variant (repair R2) has now been run** (`chk8.py`, `½log3`, `U = 14`,
`|c|_∞ ≤ 3`, 40-block fine grid): `LP = −1.93463·10⁻⁴`, fine grid `−1.23271·10⁻³`, against
`−1.93727·10⁻⁴` / `−1.53628·10⁻³` for the one-multiplier class. So R2 raises the *class ceiling* from
`+1.59·10⁻⁵` to `+9.79·10⁻⁴` (`62×`, and it is what makes Theorem B's duality claim true at all), but at
this atom/`τ` resolution it improves the *realised* bound by only `0.1%` in the LP value and `20%` on the
verification grid. The binding limitation at the achieved level is therefore the discretisation
(atom step `0.05`, `dτ = 0.01`), not the multiplier count — R2 is necessary for the statement and, on this
evidence, not by itself sufficient for the hand proof. Round 2 must pair R2 with a finer/continuous
`ν` parametrisation. Scripts archived: `chk1` (Lévy identity), `chk2` (the four constraint sets), `chk3` (joint
contact maximum, `min 𝔈`), `chk6` (dual LP, with the second moment column), `chk7` (the two moment
conditions on `Φ`).
