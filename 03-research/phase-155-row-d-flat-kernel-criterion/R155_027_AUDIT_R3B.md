# R155.027 — Audit of round 3B (`R155_024`, `scripts/r3b/`)

*Reruns: `gauss_legendre(6)` Σw test; full recomputation of the
bound from all 32 archived JSONs; one live re-run `r3b_enclosure.py 0.68 7 121 6 0.2` (21 s).
No LP, no branch-and-bound, nothing about the zeros of ζ.*

## §0 Verdicts

| item | verdict |
|---|---|
| **Theorem N′** (`M ≤ 24` at `T = 0.68`, `log2`, β-uniform) | **UPHELD — PROVED (machine-verified)**, modulo the node-certification nit N-3 |
| the 32 enclosure rows of Table 2.2 | **REPRODUCED exactly** from the JSONs; one live re-run agrees to 9 digits |
| sublattice coverage of `M ∈ {1,2,3,4,5,8,10,12}` | **UPHELD**; inclusion direction is correct |
| Gauss–Legendre panel remainder + order-`2p` derivative bounds | **UPHELD**; formula and numbers check |
| admissibility of `q` (`φ ≥ 0`, degree `< M`) | **UPHELD, trivially** (see N-1) |
| `M = 9` two-placement remedy | **UPHELD**; the final bound is a single-kernel bound |
| **Prop. P1**, **Cor. P2** (`R(ε,η;T)`), numerical table | **PROVED**; all six radii reproduced |
| **Theorem 3.3ᴾ** | **PROVED with one unstated hypothesis** (N-5) |
| **Cor. Aᴾ** | **PROVED**, fully explicit |
| **Remark P3** | boxed claim **OVERSTATED**; corrected form **PROVED** (N-6) |
| **Cor. Bᴾ**, **Cor. Cᴾ(a)**, **Cᴾ(b)** | **PROVED** (`K(ε,δ,T)` non-explicit, as declared) |

## §1 Reproductions

* `gauss_legendre(6)`: `max_i|P_6(x_i)| = |Σw_i − 2| = 3.1115·10⁻⁶¹`. Archived `gl_residual` identical
 in all 32 JSONs. The §0.5/§2.3(iv) failure story is consistent with `dbg.py`.
* All 32 rows: recomputing `a_hi + (|b₀|+|b₁|)·B` from the stored intervals reproduces
 `ceiling_upper_bound` to the last printed digit, and **all 32 are `< 0`**. Table 2.2's columns
 `a`, `|b|₁`, `B·|b|₁`, bound, `B`-tolerance all match. Min tolerance `4.7·10⁹` at `(0.68, M=22)` ✓.
* Live re-run `(0.68, M=7)`: `a_hi = −6.524981688·10⁻²`, `|b|₁ = 6.31·10⁻¹⁶`,
 `bound = −6.524981687·10⁻²`, `gl_residual = 3.1·10⁻⁶¹`, 21 s — Table 2.2 row reproduced.
* `R(ε,η)` table §3.1: all six values recomputed independently; `R(0.5,0.5) = 8.977·10⁵`,
 `R(0.1,0.1) = 2.699·10³²`, `R(0.25,0.25) = 3.736·10¹²` (§3.5) ✓. `C₀ = −5.3721834192`,
 `B = A_T − C₀ = 7.62100976` ✓ (`main.tex:946` gives `7.621`).

## §2 Checks

**(a) Logical chain.** Identical to Theorem N. `r3b_enclosure.py:249–262`: `bnd = aI +
(|b0I|+|b1I|)·B`, output `float(bnd.b)` — the *upper* endpoint, i.e. `c ≤ a + b·β ≤ a_hi + |b|₁B`,
valid because Theorem B gives `‖β‖₂ ≤ V⋆/r₀` hence `‖β‖_∞ ≤ B`, and `B` used (`1.90e4`, `1.71e4`,
`r3b_enclosure.py:59`) exceeds the computed `18905.2`, `17031.3` ✓. `∫_Wν̂φ = 0` by the mode gap
(`φ` has modes `|j| ≤ M−1`, `ν̂` modes `|j| ≥ M`) ✓; denominator `P‖q‖²` exact, no quadrature error ✓.

**(b) Sublattice inclusion. Correct, and the direction in the source is right.** With `d = 2T/M`,
`d' = 2T/(kM) = d/k`: a `ν` on `{±jd : j ≥ M}` sits on `{±j'd' : j' = jk ≥ kM}`, so
class(`M`) ⊆ class(`kM`) and `Ceil(M) ≤ Ceil(kM)`; `Ceil(kM) < 0 ⟹ Ceil(M) < 0`. Coverage:
`1,2,3,4,6,8,12 | 24`; `5,10 | 20`; `20` and `24` are both certified **directly** at both windows
(rows in Table 2.2) ✓. Together with the direct rows `6,7,9,11,13…24`, every `M ≤ 24` is covered.
No gap.

**(c) Quadrature.** Panel remainder `H^{2p+1}(p!)⁴/((2p+1)((2p)!)³)·sup|f^{(2p)}|` is the classical
Gauss–Legendre form ✓ (`r3b_enclosure.py:217–219, 243–245`, summed over `N` panels with
`H = float(Hiv.b)`, upper endpoint — conservative). `zeta_quarter_ub(j) = 4^j + ζ(j) ≥ ζ(j,¼)`
since `ζ(s,¼) = 4^s + Σ_{k≥1}(k+¼)^{−s} ≤ 4^s + ζ(s)` ✓. Growth check at `j = 2p = 12`:
`2^{−12}·12!·(4¹³+ζ(13)) = 7.8·10¹²`, dominating `C_σ = 2.879·10¹⁴` through `Γ = (Σ|q_k|)² = 19.12`;
`555·0.19978¹³·1.8809·10⁻¹⁶·2.879·10¹⁴ = 2.43·10⁻⁸ = err_sigma` ✓. Asymptotically the product of the
derivative bound and the GL constant is `~πp(H/2)^{2p}H`, so the factorial growth is beaten for
`H < 2` — the scheme is sound, not a lucky cancellation. `j = 0` entry `max(|C₀|, m(τ_max))+1e−9`
with `τ_max = |τ₀|+P` is a valid (conservative) window bound by `lem:mbounds`(i) ✓.

**(d) Admissibility of `q`. Non-negativity is structural, not certified-by-Fejér–Riesz.**
`φ(τ) = |Σ_{k<M}q_k e^{ikdτ}|²` is coded as `re²+im²` (`r3b_enclosure.py:181`), so `φ ≥ 0` for
**any** complex `q` and any rounding of it; degree `≤ M−1` by construction. No eigenvector property
is used. **N-1**: the write-up should say this outright (§2.3 says "any `(τ₀,q)` gives a valid upper
bound" — correct, but the reader looks for a positivity certificate that is not needed).
`q` is frozen to 15 decimals (`np.round(...,15)`) and enters intervals via `repr(float(·))`, i.e. as
exact decimal data used identically in `φ` and in `Γ = (Σ|q_k|)²` ✓.

**(e) `M = 9`.** `ncand = 12`: the code scans 12 placements, optimises within each, and keeps the
**single** best `(τ₀,q)` (`r3b_enclosure.py:117–121, 130`). The archived bound is therefore an
ordinary single-kernel bound, not a mixture; a min over kernels would also be valid. §2.5's account
is accurate, and the "principled remedy" (convex mixture) is correctly described as not used.
**N-2 (minor, undisclosed): `M = 6` also needed the scan** — both `M = 6` JSONs carry `ncand = 8`,
and the recovered fraction of the double ceiling is 90 % / 74 %. §2.2 and §0.2 mention only `M = 9`.
Fix one sentence.

**(f)** Done, §1.

**(g) Scope wording.** §2.6 states the `2T/d ∉ ℕ` limit in exactly the form `R155_007` R-1 demanded,
and §2.1 spells out "any range, any number of atoms, any signs, any `β`, any tail lemma". Compliant.

### Defects found (Theorem N′)

* **N-3 (MINOR, rigour).** `r3b_enclosure.py:246–248` widens the Newton-refined GL nodes/weights by
 `10⁻⁴⁵` and archives the residual `|P_p(x_i)|`, but never converts the residual into a certified
 node error (that needs a lower bound on `|P_p'|` near the node, plus a separation argument). With
 `res = 3·10⁻⁶¹` and `|P_6'|` of order 1 this is a formality, but as written the enclosure is
 "interval arithmetic around uncertified constants" — the same species of gap as `R155_007` R-2, and
 one decade of margin covers it either way. State it, or add the two-line Newton–Kantorovich bound.
* **N-4 (COSMETIC, but a number).** `R155_024:462` says the tolerance at `(M=24, T=0.68)` is
 `B ≤ 9.7·10¹⁰`; §0.3 and Table 2.2 both say `1.0·10¹¹`. Stale digit; fix `:462`.
* **N-7 (COSMETIC, contradiction).** `R155_024:459` labels `M = 9` **PROVED (machine-verified)**,
 `:500` (§5 item 5) proposes to label it **DIAGNOSTIC**, and `:482` says "`M ≤ 24` except `M = 9`".
 `M = 9` **is** proved (JSON verified above). §5 must be corrected, not §4.

## §3 Theorem 3.3ᴾ

* **Prop. P1 — PROVED.** (P) is an *even probability measure* (`main.tex:420`), so `μ(ℝ) = 1`, which
 is what makes `∫Σv_n cos dμ ≤ A_T` legitimate (`lem:mbounds`(iii), `main.tex:630`); `m(0) = C₀` and
 `m` increasing give `m − C₀ ≥ 0`; Chebyshev is then unconditional. The constraint set is used only
 through `μ ≥ 0`, `μ(ℝ) = 1` and the value — correctly, and that is why it is uniform on `ℱ_ε`.
* **Cor. P2 — PROVED.** For `R ≥ 2`, `1/R + 1/(2R²) ≤ 0.625 ≤ 1`, so `m(R) ≥ log(R/2π) − 1` from
 `lem:mbounds`(ii); `m` monotone gives the "for every `R ≥ max{R(ε,η),2}`" form. Constants verified.
* **Remark P3 — OVERSTATED as boxed; corrected form PROVED. N-6 (MAJOR-lite).** `R155_024:355–357`
 asserts "no radius of the form `R'(ε,η) = o(e^{cB/η})` for every `c > 0` can work". What
 `thm:Vp`(ii) (`main.tex:958–966`) delivers is a feasible `μ'` in `ℱ_ε` with escaped mass `≈ η`
 whenever `η(log R + C₁) ≤ ε − δ`, i.e. a forced threshold `log R ≳ (ε−δ)/η` — the constant is `ε`,
 **not** `B`. The doc concedes exactly this two lines later (":361–362", "only the constant
 (`G(ε)` versus `ε`) is open"), so the box contradicts its own proof. Replace the box by:
 *no radius with `log R'(ε,η) = o(1/η)` can work; the exponential in `1/η` is forced, the constant
 in the exponent is open between `ε` and `G(ε)`.* Also `:355` attributes the construction to
 V′(iii); it is V′(ii).
* **Theorem 3.3ᴾ — PROVED under one unstated hypothesis. N-5 (MINOR).** The tail step
 (`R155_024:375`) bounds `∫_{|τ|>R}(E_R+C₀)dμ ≤ (E_R+C₀)η`, which requires **`E_R + C₀ ≥ 0`**.
 Since `C₀ = −5.372 < 0`, this fails for small certificates (`‖ν‖_TV + A_T + |β|k − c < 5.372`).
 Either add the hypothesis or write `(E_R+C₀)^+`. Harmless for the certificates on file
 (`‖ν‖_TV ≈ 48.7`), but it is a hypothesis, not a remark. Everything else checks: `∫f dμ = ∫σ_T dμ`
 by `prop:weak`, `λ^P − c ≤ ∫(f−c)dμ`, split at `R`, P1 on the first piece, P2 on the second.
* **Cor. Aᴾ — PROVED, fully explicit.** `W := A_T+‖ν‖_TV+|β₀|ĝ₀(0)+|β₁|ĝ₁(0) − C₀ > 0` always
 (the `−C₀` saves it, unlike N-5), `f ≥ −W` on ℝ, `μ([−R,R]) ≥ 1−η`, and for `c ≥ 0`
 `λ^P+ε ≥ c(1−η) − Wη`. Algebra correct. This is the paper-ready statement of §3.
* **Cor. Bᴾ — PROVED** (Hölder with exponents `1+δ`, `(1+δ)/δ`); `K = K(ε,δ,T)` non-explicit, as
 declared; the density claim cites `thm:Vp`(ii)'s `F₀ ∈ C_c^∞(I_T)`, whose `F̂` is Schwartz ✓.
* **Cor. Cᴾ — PROVED.** (a) `Δ·μ(>P/2) ≤ [(m(P/2)−C₀)+K_β]·G/(m(P/2)−C₀) = G[1+K_β/(m(P/2)−C₀)]` ✓,
 `O(1)` and genuinely not `o(1)` on the full feasible set, for the reason given (V′). (b)
 `[(m−C₀)+K_β]K/(m−C₀)^{1+δ} = K(m−C₀)^{−δ}+O((m−C₀)^{−1−δ})` and `m(P/2)−C₀ = log M + O_T(1)` ✓.
* §3.5 consistency check against `prop:env` (`main.tex:1001–1010`): the quoted `59.5`, `10⁴⁰` are
 the paper's ✓; the comparison is qualitative and correctly flagged as "not the same object".

## §4 Paper-ready

1. **Theorem N′ + Table 2.2 → Paper 47 §8, beside `thm:N`.** Ready after N-2, N-4, N-7 (three
 sentences) and a decision on N-3 (state the node gap, or close it). Half a page as proposed.
2. **Tolerance form of the β-box → §8, `thm:N` paragraph.** Ready; it is the repair `R155_007` R-2
 asked for and the margin is `2.5·10⁵`.
3. **Prop. P1, Cor. P2, Theorem 3.3ᴾ, Cor. Aᴾ → §3/§4.** Ready after N-5 (add `E_R+C₀ ≥ 0`, or `(·)^+`).
4. **Remark P3 → §4, after `thm:Vp`.** Only in the corrected form (N-6). Do not print the boxed
 `o(e^{cB/η})` claim.
5. **Cor. Cᴾ(a)/(b) → §8.** Ready.
6. Gauss–Legendre interval scheme + the `Σw = 2` guard → methods appendix. Ready; the recorded
 failure is worth printing verbatim.

**FATAL-rule compliance of `R155_024`: verified.** No statement concerns the zeros of ζ; no sign is
claimed for `T > log2`; the endpoint of record is untouched; every §2 statement is an upper bound on
a class. Labels in §4 are correct except N-7.
