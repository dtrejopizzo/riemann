# R155.050 — Audit of R155.049 (the AL correction)

*Phase 155. Target: `R155_049_AL_CORRECTION.md`, `scripts/r49/r49_01_edge.py`.
Against Paper 46 `main.tex` `def:PD`(450–458), `prop:weak`(460–474), `eq:nuw`(1147–1151),
`thm:Dtail`(1764–1791), `thm:AL`(2930), `prop:TK`, `lem:gbounds`(476–).*

**Verdict: the retraction is JUSTIFIED and Theorem AL′ is CORRECT, with four defects — one of them
a conflation that must be removed before the text enters Paper 46.** No sign for `ζ`. Endpoint of
record unchanged.

---

## §1 Item-by-item

### 1. Retraction of `thm:AL`/`cor:ALdef` — **CONFIRMED, justified**
`eq:nuw` (`main.tex:1148`) gives the a.c. density `½(1−w)K + 2w cosh(u/2)`; the printed `thm:AL`
uses `G = (1−w)K`, dropping the `½` and the whole polar block. `w(2T) = 1` (`def:W`,
`main.tex:1144`) makes that block jump by `2 cosh T` at `2T⁺` — the very jump `thm:Dtail`'s proof
already names (`main.tex:1799–1800`: "*the density of `ν_w` at `u = 2T⁺` equals `2 cosh T ≠ 0`*").
So the printed paper contradicts itself, and the `O(M^{−r})` Poisson step is void. The hypothesis
"`w ≡ 1` on `[U,∞)`" contradicts `def:W`'s decay and makes `ν_w` infinite. Three independent fatal
defects; `TEX_HOSTILE_REVIEW_R2` finding 1 sustained. **RETRACTED** is right.

### 2. Theorem AL′ — **PROVED**, with two hypothesis errors
* **Signed `ν` is allowed.** `def:PD` (`main.tex:455`) reads "`ν` a finite even **signed** Borel
 measure". So no positivity of `G` is needed and **`0 ≤ w ≤ 1` must NOT be assumed** — which is
 essential, since comb-vanishing weights have sign changes (`R155_016`, `‖w‖_∞ ≤ 3`) and `G` is
 genuinely signed. `ν_w` itself is signed in Paper 46 (the prime atoms of `eq:nuw` carry both
 signs). The the audit's worry is answered; `R155_049`'s proof correctly never uses `G ≥ 0`. The
 replacement LaTeX should nevertheless **say** "signed" once, as it currently leaves the reader to
 check `def:PD`.
* **ERROR (`R155_049:§2`, "a finite atomic even measure … (finitely many atoms …)").** `ν_lat` has
 **countably many** atoms, not finitely many: for `|u| > U` one has `w = 0` and `G = ½K(|u|) > 0`,
 so `G(jd) ≠ 0` for every large `j`. What is true is `‖ν_lat‖_TV = d Σ|G(jd)| < ∞`
 (`G ∈ L¹ ∩ BV` on `[2T,∞)`), which is all Step 4 uses. Same slip in the LaTeX of §4. Fix the
 parenthetical; `V_0 = ‖G‖_{L¹}` and `‖ν_lat‖_TV = V_0 + O(d)` are unaffected.
* **Minor.** "`w ∈ C^{r−1}` with `w^{(r)}` of bounded variation" should read "`w^{(r−1)}` locally
 absolutely continuous with `w^{(r)} ∈ BV`", else `w^{(r)}` need not exist. `R ∈ C^{r−1}`,
 `W ∈ C^{r−1}` then follow correctly from `w ≡ 1` on the window (`w^{(j)}(2T) = 0`, `1−w(2T) = 0`).
* **Feasibility ✓.** Atoms at `|j|d ≥ Md = 2T ⊂ {|u| ≥ 2T}`; the boundary atom at `±2T` is
 explicitly admissible by `prop:weak` (`main.tex:471`, "`č_F(±2T) = 0`, so an atom of `ν` at `±2T`
 is harmless"); `β` free in `def:PD`. Comb-vanishing kills the prime atoms of `eq:nuw`, so
 `ν_w = G du` — the step the printed `thm:AL` omitted.
* **Constants re-derived, all ✓:** `Σ_{k≠0}(ξ_k²+¼)^{−1} ≤ π²/P²` ⟹ `2π² sinh T/P²`;
 `4 cosh T·(2/P) = 8 cosh T/P = (4/π)cosh T·d`; `¼Σ|ξ_k|^{−3} ≤ (7ζ(3)/2)P^{−3} = 4.207/P³` ⟹
 `16.83/P³ ≤ 16.9/P³`. `ε_r`: `Σ_{k≠0}|τ+kP|^{−r} ≤ 2·2^r(1−2^{−r})ζ(r)P^{−r}
 = 2(1−2^{−r})ζ(r)(P/2)^{−r}` ✓, and `P/2 = πM/2T` matches the LaTeX.

### 3. The mechanism and the alleged pole — **the objection is void; the proof is right**
The Mittag-Leffler sum is over `k ≠ 0`: `Σ_{k≠0}(τ+kP)^{−1} = P^{−1}[π cot πz − 1/z]`, `z = τ/P`,
and the subtracted `1/z` is exactly the removed `k = 0` term, so the function is **regular** at
`z = 0` (odd, decreasing, `= −2` at `z = ½`, hence `|·| ≤ 2/P` on `|z| ≤ ½`). No pole, and no
two-jump cancellation is needed: the `k = 0` alias is not an error term, it *is* `2ĝ₀`, which the
end-point-corrected trapezoid reproduces to `O(d²)`. (Belt and braces: at `τ = kP` one also has
`sin 2Tτ = sin(2πMk) = 0`, so the `cosh T` term vanishes there anyway.) The two edges `±2T` enter
through the single real combination `cos 2Tτ`, `sin 2Tτ`, as displayed. Phase coherence
`2T·P = 2πM` ⟹ `e^{2iTkP} = 1` ✓.
**Reproduction (`scripts/r49/r49_01_edge.py`, rewritten and rerun, 3 s, `τ`-grid 2·10⁴ on `[0,P/2]`):**
`sup|2ĝ₀−T_d|/d = 1.4050, 1.4535, 1.4660, 1.4681` at `M = 16,64,256,1024`, `T = ½log3`, vs
`(4/π)cosh T = 1.4702`; `1.5211, 1.5735, 1.5870, 1.5892` at `T = log 2` vs `1.5915`. **Both quoted
values (1.4660, 1.5870) reproduce exactly; the constant is confirmed and approached from below.**
(The script named in `R155_049` did not exist in the repo at audit time — it has now been written
at that path. `DIAGNOSTIC` status unchanged.)

### 4. Corollary AL′.1, the uncorrected sampling — **bound true, "cost" over-stated**
`(2 + 4/π)cosh T·d` is a valid **upper** bound but not the cost: the added term `2d cosh T cos 2Tτ`
is in quadrature with the `sin 2Tτ` edge term, so the sharp plain constant is
`cosh T·√(4 + 16/π²) = 2.3708 cosh T`, not `3.2566 cosh T`. Measured: `2.7375 / 2.9637` at
`M = 256` (`T = ½log3 / log2`), i.e. `2.3464 cosh T`, rising to `2.3708 cosh T` — the triangle
bound is never approached. **Consequently the claimed improvement factor `(2+4/π)/(4/π) = 2.57` is
wrong; the true factor is `√(4+16/π²)/(4/π) = 1.862`.** Fix both numbers; the qualitative claim
("the endpoint correction improves the constant, nothing improves the order") stands. "At `τ = 0`
the discrepancy equals `2d cosh T` exactly" is correct only up to the `O(d²)` corrected error.

### 5. Consequences — **one CONFLATION, must be struck**
* "the lattice is never the deficit" **WITHDRAWN** ✓ — correct and necessary.
* **ERROR (`R155_049:§0` last sentence; `§3.3`).** The measured `0.28·M^{−1.17}` is the **`Ceil_∞`**
 deficit of `R155_033 §2.5` (`R155_033:218–247`): the **archimedean** programme `(D_∞)`, where
 `β = 0`, the polar block is absent, `G = (1−w)K` vanishes to order `r` at `2T`, there is **no
 jump**, and sampling really is `O(M^{−r})` — as `R155_049 §3.4` itself states. So the edge rate
 `Θ(1/M)` **cannot** explain the `M^{−1.17}` archimedean deficit; the two live in different
 programmes and the "coherence with the numbers" is a conflation of exactly the kind the retraction
 was about. What survives: (i) in `(D_∞)` the deficit is *not* the edge and its source remains the
 `V_r ↑ ∞` trade-off of `R155_033 §2.3`; (ii) in the full programme no `Ceil` has been computed at
 all, so `E_edge` is compared to nothing. Replace the sentence by: "*the edge rate `Θ(M^{−1})` is a
 statement about the full programme; the measured `0.28M^{−1.17}` is archimedean, where no edge
 exists, and the two must not be compared.*" The same correction applies to `§3.1`'s "the two
 statements now agree instead of competing" (they are simply about different programmes) and to
 `§3.3`'s "the corrected rate makes `D ≍ M^{−1}` the natural conjecture" — downgrade to a
 `READING`, unsupported by the `Ceil_∞` table.
* **ERROR (`R155_049 §3.2` and `cor:ALdef`(ii)): "`f_lat − f_w` … is a trigonometric polynomial of
 degree `< M`" is FALSE.** `T_d` is a trig sum with frequencies `jd`, `|j| ≤ M` (degree `M`, not
 `< M`); `2ĝ₀` is **not** a trigonometric polynomial and not even periodic, and the difference is
 therefore not one. The correct statement: `f_lat − f_w = 2ĝ₀ − T_d + O_r(M^{−r})`, where `T_d` is
 the `P`-periodic trig sum of degree `M` sampling the polar block. The `prop:TK` reading ("`TK`'s
 ceiling rests on orthogonality to every mode `|j| < M` and hence bounds lattice but not flat-top
 certificates") is a **READING**, not proved by AL′, and must be labelled so.
* `§3.4` (archimedean AL survives), `§3.5` (unaffected list) — spot-checked ✓.

### 6. Amendments and the replacement LaTeX
`R155_033 §0.1(β)` (`:23`) and `§2.3` (`:184–193`) carry the amendment and are consistent: the
`(D_∞)` statements there are correctly retained, and the `V_r ↑ ∞` reading is already flagged
`DIAGNOSTIC`-conditional. `TEX_HOSTILE_REVIEW_R2` finding 1 **is** fully addressed by §4's
replacement LaTeX, subject to the four fixes above. The required table edit at `main.tex:3156`
("the deficit is the continuous problem") is correctly identified; the grep is confirmed — `thm:AL`
occurs only at `:2930`, in `cor:ALdef` and at `:3156`.

---

## §2 Statement ready for Paper 46 (hypotheses fixed)

> **Theorem (lattice sampling of a flat-top certificate).** Let `r ≥ 2` and let `w ∈ 𝒲_T` be even
> with `w^{(r−1)}` locally absolutely continuous, `w^{(r)} ∈ BV ∩ L¹`, `supp w ⊆ [−U,U]` with
> `C^{r−1}` contact with `0` at `±U`, and `w(log n) = 0` for every `n` with `log n > 2T`
> (comb-vanishing; finitely many conditions). No sign or bound `0 ≤ w ≤ 1` is assumed. Put
> `W(u) = w(|u|)cosh(u/2)`, `R = ½(1−w)K·1_{|u|≥2T}`, `G = R + 2W·1_{|u|≥2T}` (the a.c. density of
> `ν_w`, which by comb-vanishing is all of `ν_w`), `V_0 = ‖G‖_{L¹}`,
> `V_r = ‖R^{(r)}‖_{L¹} + 2‖W^{(r)}‖_{L¹}`, `c_w = inf f_w`. For `M ∈ ℕ` set `d = 2T/M`,
> `P = 2π/d = πM/T`, and let
> `ν_lat = Σ_{|j| ≥ M} d κ_j G(jd) δ_{jd}`, `κ_{±M} = ½`, `κ_j = 1` for `|j| > M`,
> a **signed** even measure with countably many atoms, supported in `{|u| ≥ 2T}` and of finite total
> variation `‖ν_lat‖_TV = V_0 + O(d)`. Then `(ν_lat, β = (2,0))` is feasible for `(D)` and
> `c_lat(M) ≥ min{ c_w − E_edge(M) − ε_r(M), m(πM/2T) − 𝖠_T − ‖ν_lat‖_TV − 2ĝ₀(0) }`, with
> `E_edge(M) = 8cosh T/P + 2π² sinh T/P² + 16.9 cosh T/P³ = (4/π)cosh T·d + O(d²)` and
> `ε_r(M) = 2(1−2^{−r})ζ(r) V_r (πM/2T)^{−r}`. Moreover
> `sup_τ|f_lat − f_w| = (4/π)cosh T·d(1 + O(d))`: the rate `M^{−1}` and its constant are attained,
> and no smoothness of `w` improves them, because they are the alias of the jump of
> `2cosh(u/2)·1_{|u|<2T}` at `±2T`, an object independent of `w`.
>
> **Corollary.** At fixed `w`, `c_w − c_lat(M) ≤ (8T/π)cosh T·M^{−1} + O(M^{−2}) + O_r(V_r M^{−r})`.
> Without the endpoint correction (`κ_{±M} = 1`) the sharp constant is
> `cosh T·√(4 + 16/π²)·d = 2.3708 cosh T·d`, so the boundary atom of weight `d cosh T` at `±2T`
> improves the constant by the factor `1.862` and nothing improves the order.

## §3 Labels of record (audited)

| item | label |
|---|---|
| `thm:AL`/`cor:ALdef` as printed | **RETRACTED** — confirmed, three independent defects |
| Theorem AL′ (with the §2 hypothesis fixes) | `PROVED` |
| sharp constant `(4/π)cosh T·d` | `PROVED`; `DIAGNOSTIC` reproduced to 3 digits (`r49_01_edge.py`) |
| Corollary AL′.1 as written (`(2+4/π)`, factor `2.57`) | **ERROR** → `2.3708 cosh T·d`, factor `1.862` (`DIAGNOSTIC`+quadrature argument) |
| "`ν_lat` has finitely many atoms" | **ERROR** → countably many, finite TV |
| "`f_lat − f_w` is a trig polynomial of degree `< M`" | **ERROR** → `2ĝ₀ − T_d`, `T_d` of degree `M`; `prop:TK` reading = `READING` |
| "coherent with the measured `0.28M^{−1.17}`" / "`D ≍ M^{−1}` natural" | **CONFLATION** (archimedean vs full); strike / downgrade to `READING` |
| "the lattice is never the deficit" | **WITHDRAWN** ✓ |
| Theorem AL of `R155_033 §2.3` in `(D_∞)` | `PROVED`, unaffected ✓ |
| `R155_033 §0.1(β)`, `§2.3` amendments | consistent ✓ |

Row-D label and the endpoint of record (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`) unchanged.
