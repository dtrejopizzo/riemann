# R155.048 — Audit of round 7a (`R155_047`, `scripts/r7a/`, `PROLATE-REFERENCES.md`)

*Verdict: **ACCEPT with one numerical erratum and three scope caveats.** All labels stand.
Theorem P, Cor P1–P3 verified line by line; all numbers reproduced.*

## 1 Theorem P (§3.1, l.105–128) — **CORRECT**

* Normalisation: `e_j = √((2j+1)/(2T))P_j(t/T)`, `‖e_j‖=1` (equivalently `‖P_j(·/T)‖²=2T/(2j+1)` ✓).
 `∫_{−1}^1 P_j(u)e^{−ixu}du = 2(−i)^j j_j(x)` ✓ (the order's `2T i^{−j} j_j(τT)` for `P_j(t/T)` on `I_T`
 is the same up to the `e^{+ixu}` convention: `i^{−j} = (−i)^j`). Hence `|ê_j(τ)|² = 2T(2j+1)j_j(τT)²` ✓.
* Diagonal constant recomputed independently:
 `R_j = (1/2π)∫_{−s}^{s}|ê_j|² = (1/π)·2T(2j+1)∫_0^s j_j(τT)²dτ = (2(2j+1)/π)∫_0^c j_j(x)²dx` ✓ — the
 document's constant is exact (not off by 2 or π).
* `Σ_j(2j+1)j_j(x)²=1` (addition theorem) ⟹ `Σ_j R_j = 2c/π = tr S_c` ✓; so the Legendre basis loses
 no trace and `Λ_0 = tr`.
* Ky Fan chain: `Σ_{j<k}λ_j ≥ Σ_{j<k}R_j` (top-`k` eigenvalues dominate any `k` diagonal entries — the
 correct direction, and the document uses it in the correct direction), and `λ_k ≤ Σ_{n≥k}λ_n` needs
 only `λ_n ≥ 0` ✓ (`S_c = Q_TB_sQ_T = (B_sQ_T)^*(B_sQ_T) ≥ 0`). Chain
 `λ_k ≤ tr − Σ_{j<k}λ_j ≤ tr − Σ_{j<k}R_j = Σ_{j≥k}R_j = Λ_k` ✓. **`PROVED` confirmed.**
* Cor P1: `|j_n(x)| ≤ x^n/(2n+1)!!` holds for all `x ≥ 0` ✓ (standard, from the series with alternating
 decreasing terms / Poisson integral). Then `R_j ≤ (2(2j+1)/π)·c^{2j+1}/((2j+1)((2j+1)!!)²)
 = (2/π)c^{2j+1}/((2j+1)!!)²` — the constant in the document is exact ✓.
* Cor P2 is a restatement of P + min–max ✓; it is indeed a *min–max* (one direction per subspace) floor.

## 2 Corollary P3 (§3.2, l.140–145) — **CORRECT, no off-by-one**

With 0-based indexing, `#{n : λ_n > θ} = k* := min{k : λ_k ≤ θ}` (eigenvalues non-increasing);
Prop NC gives `n₋ ≤ #{λ_n > θ}= k*`; `Λ_k ≤ θ ⟹ λ_k ≤ θ ⟹ k* ≤ k`. So
`n₋ ≤ min{k : Λ_k(Tτ₁) ≤ θ(τ₁)}` ✓. The order's alternative route (min–max on the `n₋`-dimensional
negative subspace: `λ_{n₋−1} > θ ⟹ n₋−1 < k* ⟹ n₋ ≤ k*`) gives the identical index ✓ — consistent with
`R155_033` l.285–286. The infimum over `τ₁` is legitimate (each `τ₁` is a separate valid bound, §2
l.76–85) ✓. The first inequality `n₋(A_∞|P_T) ≤ n₋(Γ_T on L²)` is the codimension remark, not used
quantitatively ✓.

## 3 Reproduction (`scripts/r7a/`, rerun)

`r7a_01_floor.py`: `τ₀ = 6.289835989`, `C₀ = −5.3721834` ✓.

| `T` | `τ₁` | `θ` | `c` | proved `k` | `Λ_k` | true count `>θ` | Thm J |
|---|---|---|---|---|---|---|---|
| `½log3` | 6.4222 | 3.869e−3 | 3.5277 | **5** | 2.954e−3 | 4 | 2 |
| `log 2` | 6.4222 | 3.869e−3 | 4.4515 | **6** | 3.220e−3 | 5 | 2 |
| `0.80` | 6.3576 | 1.994e−3 | 5.0861 | **7** | 1.708e−3 | **6** | 3 |

`r7a_02_closedform.py`: `5 (τ₁=6.6159) / 7 (τ₁=6.3576) / 8 (τ₁=6.3576)` ✓. Eigenvalue rows of §2 and
§0.3 reproduce to all printed digits (`log 2`: `.99820.95360.66108.19793.02185 1.21e−3 …`).
Runtime **6.4 s + 2 s**, not the `~50 s + ~5 s` of `scripts/r7a/README.md:5–6` (harmless, fix the README).

**ERRATUM 1 (numerical, must fix).** `R155_047:27` — the `0.80` row of the §0.2 table gives
"diagnostic prolate count **5**"; the true value at the optimal `τ₁ = 6.3576` is **6** (§2 table, l.94,
and the rerun agree). The same `4,5,5` triple is carried in `04-papers/46-row-d-sign-radial-intersection-form/main.tex:3157`
and should be re-checked (`4,5,6` at the optimal `τ₁`) if that line is touched.

**Minor (scripts).** `r7a_02_closedform.py:15` overflows for `τ₁` large (`c ≳ 100`, `c^{159}`), so those
`τ₁` are silently skipped in the series scan; the optimum sits at `τ₁ ≈ 6.4`, so the reported values are
unaffected. Also `Λ*` is evaluated as the partial sum `j < 80`, i.e. a *lower* bound on the infinite
series; the omitted tail is `< 10^{−170}`, so the `PROVED` inequality is not endangered, but the honest
statement is "partial sum + a tail bounded by `10^{−170}`". Add one line to the docstring.

## 4 Remark P4 / "the route cannot reach 1" (§0.3 l.31–37, §3.4 l.173–184) — **CORRECT BUT OVER-BROAD IN §0**

Verified: at `T = log 2`, optimal `τ₁`, `λ₄ = 2.18e−2 > θ = 3.87e−3` (margin `5.6×`), and the `τ₁`-scan
minimum of `#{λ_n(Tτ₁) > θ(τ₁)}` is `5`. So Remark P4 as *stated* — "no improvement of the **prolate
estimate** can bring **Prop NC's** bound below 5" — is right, and correctly charges the residue to the
**two-value** relaxation `m ≥ C₀·1_{|τ|<τ₁} + m(τ₁)·1_{|τ|≥τ₁}` and to `codim P_T = 2`.

**CAVEAT 1 (scope, wording).** `R155_047:36–37` ("the lemma proves the earlier decision cannot reach `1`") and
`§0.1`'s framing overstate it. What is proved is a statement about the **two-value relaxation only**.
A multi-band relaxation `m ≥ Σ_i c_i 1_{B_i}` (thresholds `C₀` on `|τ|<τ₀`, `m(τ₁)` on `τ₀<|τ|<τ₁`,
`m(τ₂)` on `|τ|>τ₂`, …) yields the *different* operator `Σ_i (c_i − c_{i+1}) S_{T,τ_i}` and hence a
different counting problem, to which Remark P4 says nothing; in the limit of infinitely many bands the
relaxation is exact and returns the true `n₋ = 1`. So the correct statement is: *this* (two-value)
relaxation floors at 5; the multi-band family is untested and is the obvious refinement. Recommend
rewording §0.3 and adding one sentence to Remark P4 naming the multi-band family as the open refinement


## 5 Two-sided counts (§3.3) — **CORRECT**

`⌈2Tτ₀/π⌉−1`: `½log3 → ⌈2.1996⌉−1 = 2` ✓, `log 2 → ⌈2.7754⌉−1 = 2` ✓, `0.80 → ⌈3.2028⌉−1 = 3` ✓.
`R155_047` writes `2/2/3`, **not** `2` throughout (the order's suspicion is unfounded): `R155_047:25–27`
and `:166–168` both carry `3` at `0.80` ✓, and the script prints `3` ✓. Intervals `[2,5]/[2,6]/[3,7]`
contain the Galerkin `L²` counts `2/3` ✓ and the `P_T` counts `0/1/1` ✓. No contradiction with Theorem J.

## 6 Remark PA (§4) — **label correct, one clause unsupported**

It is a *"does not follow"*, not an impossibility theorem, and is labelled `REMARK` (negative) ✓ —
correct. The quantifier diagnosis (min–max per subspace vs `inf` over the feasible set of Theorem R) is
right. **CAVEAT 2:** the final clause — "the feasible set of `prob:A` contains the near-`λ₀` direction
(the flat top is the extremal concentrator, `thm:O`'s edge mechanism), so no such `d` exists" — is an
assertion, not a proof: it would need `inf_{F∈F}E_out(F)=0`, which `thm:O` does not state. Mark that
clause `HEURISTIC` inside the remark, or weaken to "no such `d` is available from `thm:O`". With that,
"Problem A is untouched by round 7a" stands.

## 7 Literature (§1, `00-references/PROLATE-REFERENCES.md`) — **CORRECT**

References 1–9 check out as bibliographic entries (Slepian–Pollak BSTJ 40 (1961) 43–63; Landau–Pollak
BSTJ 40 (1961) 65–84 and BSTJ 41 (1962) 1295–1336; Landau–Widom JMAA 77 (1980) 469–481; Bonami–Karoui
C. R. 352 (2014) 229–234, Constr. Approx. 43 (2016) 15–45, ACHA 42 (2017) 1–20; Bonami–Jaming–Karoui
JMP 62 (2021) 033511; Osipov–Rokhlin–Xiao AMS 187, Springer 2013; Israel arXiv:1502.04404), all
`CITED-NOT-VERIFIED` and **used in no proof** ✓ (grep: no numeric constant in §3 traces to §1). The
Landau–Widom formula is correctly flagged asymptotic and therefore unusable at `c ≈ 3.5–5.1` ✓.
"Theorem P likely folklore, not claimed new" — the ingredients (Legendre/spherical-Bessel diagonal of
`Q_TB_sQ_T`, Ky Fan) are all classical and the corpus grep finds no prior statement of it in 155 phases;
the modest claim is the right one. **No priority claim to police.**

## 8 Labels, readiness

All eight label rows of `R155_047 §5` are sustained as written, with two amendments: (i) the
"route cannot return `< 5`" row should read "…for the **two-value** relaxation" (Caveat 1); (ii) Remark
PA's no-`d` clause is `HEURISTIC` (Caveat 2). Row-D label unchanged ✓; endpoint
`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` untouched ✓; no sign for `ζ` claimed ✓; Paper 46 not modified ✓
(`git status`: only `scripts/r7a/` and the two new md files are new/untracked).

**Paper 46 proposal (§6): READY after the two wording fixes + Erratum 1.** Replacing `prop:NC`'s
`n₋ ≤ 68.51·T` (main.tex:2991) by `5/6/7` is a genuine and citable improvement; `main.tex:3157`'s
"prolate counts `4,5,5`" must become `4,5,6`, and `prop:NC`'s statement must carry the `inf_{τ₁}`
explicitly (it already does at `R155_033:277` for the trace form). Cite the quadrature-free `5/7/8`
in the statement and keep the grid `5/6/7` as the `DIAGNOSTIC` table row, so no theorem in the paper
depends on a trapezoid rule. Remark P4 enters as a remark, scoped to the two-value relaxation.
