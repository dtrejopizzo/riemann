# R155.047 — Builder, round 7a: the prolate concentration floor

*Phase 155, round 7a, 2026-09-22. Executes `R155_046 §4(a)`. Inherits `R155_033` (Prop NC, amended),
`R155_039` (Theorem J, the "Jensen gives ceilings only" remark, amended), `R155_044` (Theorem N4,
arena, amended), `R155_023` (amended; `τ₀ = 6.28983599`, `C₀ = −5.3721834`), Paper 47 §2 (`thm:S`,
`lem:mbounds`), §3, §8 (`prop:NC`, `thm:J`). Paper 47 is **not** touched. Scripts: `scripts/r7a/`.*

**No sign for `ζ` is claimed at any `T`. Endpoint of record unchanged (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`,
Paper 47 Thm C). No value of `inf W` at `log 2` is asserted.**

**[amended 2026-09-22 per R155_048]** hostile audit accepted with one numerical erratum and three
scope caveats; repairs applied in place at §0.2 (Erratum 1), §0.3 (two-value relaxation scope), §4
(Remark PA closing clause), §5 (labels), §6 (THEOREM vs DIAGNOSTIC citation). All original labels
otherwise stand.

---

## §0 Verdict

1. **The missing lemma is now a theorem, and it is elementary — no prolate literature is needed.**
   Theorem P (§3.1): for the Landau–Pollak–Slepian operator `S_c = Q_T B_s Q_T` (`c = Ts`),
   `λ_k(c) ≤ Λ_k(c) := (2/π)∫_0^c (1 − G_k(x)) dx`, `G_k(x) = Σ_{j<k}(2j+1) j_j(x)²`, with the
   quadrature-free corollary `Λ_k(c) ≤ Λ*_k(c) := (2/π) Σ_{j≥k} c^{2j+1}/((2j+1)!!)²`. Proof: the
   Legendre basis diagonalises the *trace* of `S_c` exactly (spherical-Bessel diagonal), then Ky Fan
   and `S_c ≥ 0`. Both are `PROVED`.
2. **Combined with Prop NC this gives the first proved, small upper bounds on `n₋`:**

   | `T` | Thm J lower (`Γ_T`) | **PROVED upper (Thm P + NC)** | quadrature-free variant | Prop NC trace bound | diagnostic prolate count | true (Galerkin) `n₋(A_∞\|P_T)` |
   |---|---|---|---|---|---|---|
   | `½log3` | `2` | **`5`** | `5` | `37` | `4` | `0` |
   | `log 2` | `2` | **`6`** | `7` | `47` | `5` | `1` |
   | `0.80` | `3` | **`7`** | `8` | `54` | `6` | `1` |

   **[amended 2026-09-22 per R155_048, Erratum 1]** the `0.80` diagnostic prolate count is `6`, not `5`
   (`4, 5, 6` at the optimal `τ₁`, not `4, 5, 5`); `04-papers/47-row-d-dual-certificates/main.tex:3157`
   carries the same erratum and should be re-checked if that line is touched.

   A factor `≈ 7–8` gain over Prop NC, and within one of the `DIAGNOSTIC` count that `R155_033 §3.4`
   said an import of Bonami–Karoui would buy — obtained instead by a two-line self-contained argument.
3. **`n₋(A_∞|P_{log2}) = 1` is NOT proved.** The proved interval at `log 2` is `0 ≤ n₋(A_∞|P_T) ≤ 6`
   (and `2 ≤ n₋(Γ_{log2}) ≤ 6` on `L²`). The gap `1` vs `6` is *not* a defect of Theorem P: at the
   optimal `τ₁` the true eigenvalues are `0.9982, 0.9536, 0.6611, 0.1979, 0.0218, 0.0012, …` against
   `θ = 0.00387`, so **Prop NC's own criterion cannot return less than `5` there**, whatever prolate
   estimate is used. The remaining `5 → 1` is the `m`-grows-only-logarithmically wall of
   `R155_033 §3.3`, not the missing lemma. Round 7a therefore **closes the "prolate floor" lead**: it
   delivers the lemma, and the lemma proves the lead cannot reach `1` **[amended 2026-09-22 per
   R155_048]: proved for the two-value relaxation only; the multi-band relaxation `Σᵢ cᵢ 1_{Bᵢ}`
   (operator `Σ(cᵢ − cᵢ₊₁)S_{T,τᵢ}`) is the obvious untested refinement, exact in the limit.**
4. **Problem A (§4): the floor does not transfer.** It is a min–max (one direction per subspace)
   statement; Theorem R's `Δ` needs a floor *uniform over the feasible set*, which the Legendre
   diagonal does not supply. Stated precisely as Remark PA; no class-dependent lower bound follows.

---

## §1 Literature (added to `00-references/PROLATE-REFERENCES.md`)

The folder `00-references/` exists (PDFs); a bibliography file `PROLATE-REFERENCES.md` was added there.
Summary of what is available and what it gives (all `CITED-NOT-VERIFIED`, no copy held):

* **Slepian–Pollak (BSTJ 40, 1961, 43–63)**, **Landau–Pollak (BSTJ 40, 1961, 65–84; BSTJ 41, 1962,
  1295–1336)**: `λ_n(c) ∈ (0,1)`, simple, decreasing; the plateau/plunge picture. No usable explicit
  `λ_n` bound at `c ≈ 4`.
* **Landau–Widom (JMAA 77, 1980, 469–481)**: `#{n : λ_n(c) > θ} = 2c/π + π^{−2} log c · log((1−θ)/θ)
  + o(log c)`. **Asymptotic in `c`; no explicit threshold**, so at `c = 3.5–5.1` it is unusable as a
  proof input. (It is the source of the `R155_023` Prop 3(ii) asymptotic, kept as such.)
* **Bonami–Karoui (C. R. Math. 352 (2014) 229–234; Constr. Approx. 43 (2016) 15–45; ACHA 42 (2017)
  1–20)** and **Bonami–Jaming–Karoui (J. Math. Phys. 62 (2021) 033511)**: non-asymptotic
  super-exponential decay `λ_n(c) ≤ …` valid for `n` above a threshold of the form
  `n ≥ 2c/π + O(log c)`. Exact constants and thresholds cannot be quoted here without a copy; they
  were the intended import of `R155_033 §3.4`.
* **Osipov–Rokhlin–Xiao, Springer AMS 187 (2013)**: explicit inequalities, Legendre expansion of the
  PSWFs, algorithms.

**Consequence for the round.** Every candidate import is either asymptotic (3) or quotable only from a
copy (4–8), and all of them are needed exactly in the regime `n ≳ 2c/π` where Theorem P below is
already effective. Theorem P is therefore used in their place and the counts in §0.2 are `PROVED`
without any external inequality. Items (4)–(8) remain the reference point for **sharpness**: they
should improve `Λ_k` by constants, not by the order of the count.

---

## §2 Task (1): Prop NC optimised, and what the literature would give

`θ(τ₁) = m(τ₁)/(m(τ₁) − C₀)`, `m(τ) = Re ψ(¼ + iτ/2) − log π` (`lem:mbounds`), `m(τ₀) = 0`,
`C₀ = m(0) = −5.3721834`, `τ₀ = 6.289835989`.

**Re-derivation of the quantifier (the order's question).** Prop NC's proof fixes `τ₁` *first* and
then applies min–max; the conclusion is, for each fixed `τ₁ > τ₀`,
`n₋(Γ_T) ≤ #{n : λ_n(Tτ₁) > θ(τ₁)}`. A negative direction need not satisfy the criterion for *every*
`τ₁` simultaneously in any joint sense beyond this — but since the inequality holds for each `τ₁`
separately, one may take the **minimum over `τ₁`**:
`n₋(Γ_T) ≤ inf_{τ₁>τ₀} #{n : λ_n(Tτ₁) > θ(τ₁)}` (`PROVED`; each term is a valid bound, so the
infimum is). This is what §0.2 optimises. `θ_min := inf_{τ₁>τ₀} θ(τ₁) = 0` (as `τ₁ ↓ τ₀`,
`m(τ₁) ↓ 0`), so a `θ_min` taken alone is vacuous: the optimisation is genuinely joint, `θ(τ₁)`
against `λ_n(Tτ₁)`, and its optimum sits just above `τ₀` (`τ₁ = 6.42`–`6.62`), not at the trace
bound's `τ₁ = 14.88`.

**Evaluation (`scripts/r7a/r7a_01_floor.py`).** At the optimal `τ₁` the true spectrum (`DIAGNOSTIC`,
300-node Gauss–Legendre Nyström) is

| `T` | `τ₁` | `θ` | `c = Tτ₁` | `λ_0 … λ_7` | count `> θ` |
|---|---|---|---|---|---|
| `½log3` | `6.4222` | `3.869e−3` | `3.5277` | `.99037, .83872, .36193, .05174, 2.96e−3, 9.7e−5, 2.2e−6, 3.5e−8` | `4` |
| `log 2` | `6.4222` | `3.869e−3` | `4.4515` | `.99820, .95360, .66108, .19793, .02185, 1.21e−3, 4.3e−5, 1.1e−6` | `5` |
| `0.80` | `6.3576` | `1.994e−3` | `5.0861` | `.99945, .98242, .81755, .36924, .06397, 5.01e−3, 2.4e−4, 8.2e−6` | `6` |

So **the best `n₋` this route can ever return is `4 / 5 / 5–6`**, even with exact eigenvalues. A
Bonami–Karoui import would reproduce these numbers as `PROVED`; Theorem P reaches `5 / 6 / 7`
without it. The claim of `R155_033 §3.4` ("a real but modest gain … `n₋ ≤ 5` at `log 2`, not `1`") is
confirmed and made unconditional up to one unit.

---

## §3 Task (2): the own theorem

### 3.1 Theorem P (`PROVED`)

Let `I_T = (−T,T)`, `Q_T` restriction to `I_T`, `B_s` the band projection to `|τ| < s`,
`S_c := Q_T B_s Q_T` on `L²(I_T)`, `c := Ts`. Then `0 ≤ S_c ≤ I`, `tr S_c = 2c/π`, and with
`j_j` the spherical Bessel functions and `G_k(x) := Σ_{j<k}(2j+1) j_j(x)² ∈ [0,1]`:

> **Theorem P.** For every `k ≥ 0`,
> `λ_k(S_c) ≤ Λ_k(c) := (2/π) ∫_0^c (1 − G_k(x)) dx`.
> In particular `Λ_0(c) = 2c/π` (the trace) and `Λ_k(c) = O(c^{2k+1})` as `c → 0`.

*Proof.* Let `e_j(t) := √((2j+1)/(2T)) · P_j(t/T)`, `j ≥ 0`, the orthonormal Legendre basis of
`L²(I_T)`. From `∫_{−1}^{1} P_j(u) e^{−ixu} du = 2(−i)^j j_j(x)`,
`ê_j(τ) = √((2j+1)/(2T)) · 2T(−i)^j j_j(τT)`, so `|ê_j(τ)|² = 2T(2j+1) j_j(τT)²`. By Plancherel,
```
R_j(c) := ⟨S_c e_j, e_j⟩ = (1/2π)∫_{−s}^{s}|ê_j|² dτ = (2(2j+1)/π) ∫_0^c j_j(x)² dx .
```
The addition theorem `Σ_{j≥0}(2j+1) j_j(x)² = 1` gives `Σ_j R_j(c) = 2c/π = tr S_c` (a check that the
basis captures the whole trace, i.e. that no mass is lost to the off-diagonal). By the Ky Fan
maximum principle, `Σ_{j<k} λ_j(S_c) ≥ Σ_{j<k} R_j(c)`. Since `S_c ≥ 0` and its eigenvalues are
non-increasing, `λ_k ≤ Σ_{n≥k} λ_n = tr S_c − Σ_{j<k} λ_j ≤ Σ_{j≥k} R_j(c)
= (2/π)∫_0^c (1 − G_k(x)) dx`. ∎

> **Corollary P1 (quadrature-free).** `|j_n(x)| ≤ x^n/(2n+1)!!` for `x ≥ 0`, hence
> `λ_k(S_c) ≤ Λ*_k(c) := (2/π) Σ_{j≥k} c^{2j+1}/((2j+1)!!)²`, a convergent series of rationals.

> **Corollary P2 (the concentration floor).** For every subspace `V ⊆ L²(I_T)` with `dim V = k+1`
> there is a unit `F ∈ V` with `E_out(F) := 1 − ‖B_sF‖²/‖F‖² ≥ 1 − Λ_k(Ts)`. Equivalently: a
> `(k+1)`-dimensional family of window-supported functions cannot all concentrate more than
> `Λ_k(Ts)` of their spectral mass in `|τ| < s`.

Corollary P2 is the floor the last three rounds asked for. It is a min–max floor (one direction per
subspace), which is exactly what Prop NC consumes — and, per §4, exactly what Problem A does not.

### 3.2 The count

> **Corollary P3 (`PROVED`).** `n₋(A_∞|P_T) ≤ n₋(Γ_T on L²(I_T)) ≤ min_{τ₁>τ₀} min{ k : Λ_k(Tτ₁) ≤ θ(τ₁) }.`

*Proof.* Prop NC (each `τ₁` separately) plus Theorem P: if `Λ_k(Tτ₁) ≤ θ(τ₁)` then `λ_k(Tτ₁) ≤ θ(τ₁)`,
so `#{n : λ_n > θ} ≤ k`. The first inequality is `P_T ⊂ L²(I_T)` with the pole term vanishing on `P_T`
(`prop:arch`); the two Tate constraints only remove directions, so they can only help — and are not
used. ∎

Evaluation (`r7a_01`, `r7a_02`), with `Λ_k(c)` at the optimal `τ₁`:

| `T` | optimal `τ₁` | `θ` | `c` | `Λ_0, Λ_1, …` | `k` | `Λ*` variant |
|---|---|---|---|---|---|---|
| `½log3` | `6.4222` | `3.869e−3` | `3.5277` | `2.246, 1.342, .5850, .1572, 2.64e−2, 2.95e−3` | **`5`** | `5` (`τ₁=6.6159`) |
| `log 2` | `6.4222` | `3.869e−3` | `4.4515` | `2.834, 1.911, 1.121, .4728, .1312, 2.45e−2, 3.22e−3` | **`6`** | `7` (`τ₁=6.3576`) |
| `0.80` | `6.3576` | `1.994e−3` | `5.0861` | `3.238, 2.297, 1.503, .7921, .2919, 7.35e−2, 1.31e−2, 1.71e−3` | **`7`** | `8` |

`Λ_k` is evaluated by trapezoid on a `2·10⁵`-point grid (`DIAGNOSTIC` evaluation of a `PROVED`
inequality; margins `Λ_k/θ ≈ 0.76–0.86` at the selected `τ₁`, quadrature error `≈10^{−10}`). The
`Λ*` column uses **no quadrature at all** and is the number to cite if a reader objects to the
grid: `n₋ ≤ 5 / 7 / 8`, fully explicit.

### 3.3 Two-sided count, and the exact statement of what is now known

With Theorem J (`n₋(Γ_T) ≥ ⌈2Tτ₀/π⌉ − 1`) and Corollary P3:

| `T` | Thm J | Cor P3 | true `n₋(Γ_T)` (Galerkin, `r5a_01`) | true `n₋(A_∞\|P_T)` |
|---|---|---|---|---|
| `½log3` | `2` | `5` | `2` | `0` |
| `log 2` | `2` | `6` | `3` | `1` |
| `0.80` | `3` | `7` | — | `1` |

The two-sided proved interval is `[2,5]` / `[2,6]` / `[3,7]`, containing the true `L²` counts `2`/`3`.
No window yields an exact proved count; `½log3` comes closest (`[2,5]`, true `2`).

### 3.4 Why the gap to `1` is structural (`PROVED` obstruction to the route)

At the optimal `τ₁` the true `λ_4(c) = 2.18e−2 > θ = 3.87e−3` at `T = log 2`, so
`#{λ_n > θ(τ₁)} ≥ 5` there; a scan over `τ₁` (`R155_033 §3.3`, `r7a_01`) gives minimum `5`. Hence

> **Remark P4.** No improvement of the prolate estimate can bring Prop NC's bound below `5` at
> `T = log 2`, since the bound already equals the exact count `#{λ_n(Tτ₁) > θ(τ₁)}` there. The
> distance from `5` to the true `n₋(A_∞|P_{log2}) = 1` is charged entirely to the two-value
> relaxation `m ≥ C₀·1_{|τ|<τ₁} + m(τ₁)·1_{|τ|≥τ₁}` and to `codim P_T = 2`, not to prolate theory.

This closes the lead named in `R155_046 §3` as "the one live analytic lever": the lever exists
(Theorem P), it is cheap, and it lands at `5–7`.

---

## §4 Task (3): Problem A

> **Remark PA (`REMARK`, negative).** Corollary P2 does not produce a class-dependent lower bound on
> the archimedean form's lattice certificates. Reason: P2 is a min–max statement — for each
> `(k+1)`-dimensional `V` it produces **one** direction with `E_out ≥ 1 − Λ_k`. Theorem R's deficit
> `Δ` is an infimum over the feasible set `F` of measures/weights, so what is needed is
> `inf_{F ∈ F} E_out(F) ≥ ε₀ > 0` — a floor **uniform on `F`**, i.e. a statement that *no* feasible
> direction concentrates. The Legendre diagonal gives the opposite quantifier. A uniform floor does
> follow when `F` is contained in a subspace of finite codimension `d` complementary to the top
> prolate eigenspace, since then `sup_{F∈F} ‖B_sF‖²/‖F‖² ≤ λ_d ≤ Λ_d`; but the feasible set of
> `prob:A` contains the near-`λ_0` direction (the flat top itself is the extremal concentrator,
> `thm:O`'s edge mechanism), so no such `d` exists **[amended 2026-09-22 per R155_048]: this closing
> clause is `HEURISTIC`, not proved — it asserts `inf_{F∈F}E_out(F)=0`, which `thm:O` does not state**.
> **Problem A is untouched by round 7a.**
> The `R155_039 §2.4` reading ("a floor ⟺ a prolate spread bound") is hereby refined: the prolate
> spread bound exists and is proved; it is the *uniformity*, not the spread bound, that was missing.

---

## §5 Labels

| statement | label |
|---|---|
| **Theorem P**: `λ_k(S_c) ≤ (2/π)∫_0^c(1−G_k)`, `G_k = Σ_{j<k}(2j+1)j_j²` | **`PROVED`** (Ky Fan + Legendre/spherical-Bessel diagonal + `Σ(2j+1)j_j²=1`); elementary, likely folklore — presented as self-contained, **not** claimed new |
| **Corollary P1**: `λ_k(S_c) ≤ (2/π)Σ_{j≥k} c^{2j+1}/((2j+1)!!)²` | **`PROVED`**, quadrature-free |
| **Corollary P2** (concentration floor, min–max form) | **`PROVED`** |
| **Corollary P3**: `n₋(A_∞\|P_T) ≤ min_{τ₁}min{k : Λ_k(Tτ₁) ≤ θ(τ₁)}` | **`PROVED`** |
| numerical values `n₋ ≤ 5 / 7 / 8` (quadrature-free series, Cor P1) | **`THEOREM`** values **[amended 2026-09-22 per R155_048]**: proved inequality, finite explicit series, needs only arithmetic |
| numerical values `n₋ ≤ 5 / 6 / 7` (grid, Theorem P) | **`DIAGNOSTIC`** **[amended 2026-09-22 per R155_048]**: proved inequality but evaluated by trapezoid quadrature (double precision, no interval arithmetic) — no theorem in the paper depends on this row |
| Prop NC's optimised form `n₋ ≤ inf_{τ₁} #{λ_n(Tτ₁)>θ(τ₁)}` | **`PROVED`** (each `τ₁` separately; the infimum is legitimate) |
| **Remark P4**: the route cannot return `< 5` at `log 2` | **`PROVED`** modulo the `DIAGNOSTIC` eigenvalues (`λ_4 = 2.18e−2` vs `θ = 3.87e−3`, margin `5.6×`) — **[amended 2026-09-22 per R155_048]**: for the **two-value** relaxation only (§0.3) |
| **Remark PA**: no transfer to Problem A | **`REMARK`** (negative, quantifier-level); **[amended 2026-09-22 per R155_048]**: closing "no such `d` exists" clause is `HEURISTIC`, not proved |
| `n₋(A_∞\|P_{log2}) = 1` | **NOT PROVED**; proved interval `[0,6]` |
| Bonami–Karoui / Landau–Widom / ORX inequalities | **`CITED-NOT-VERIFIED`**, not used in any proof above |

Row-D label unchanged. Endpoint unchanged. No sign for `ζ` beyond `log 2`.

---

## §6 Paper 47 proposal (not executed)

`subsec:arch` gains, after `prop:NC`: **Theorem P** with its four-line proof, **Corollary P1**
(quadrature-free), **Corollary P2** (floor), **Corollary P3** with the table of §3.3, and
**Remark P4** (the route's floor at `5`, scoped to the two-value relaxation). `prop:NC`'s statement
is amended to carry the infimum over `τ₁` explicitly. **[amended 2026-09-22 per R155_048]**: cite the
quadrature-free `5/7/8` (Corollary P1) as the `THEOREM` values in the statement, and keep the grid
`5/6/7` (Theorem P, trapezoid quadrature) only as a `DIAGNOSTIC` table row, so no theorem in the paper
depends on a trapezoid rule. `prob:A` gains **Remark PA** as the precise reason the prolate floor does
not answer it (its closing clause marked `HEURISTIC`). Net: about 1.5 pages, no numerics in the
statements except the table, which is marked
`DIAGNOSTIC`. Recommended only after the round-7b hostile TeX review `R155_046 §4(b)`.

*Scripts: `scripts/r7a/` (`r7a_01_floor.py`, `r7a_02_closedform.py`, `README.md`). References:
`00-references/PROLATE-REFERENCES.md`.*
