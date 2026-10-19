# Adversarial referee report R2 — `main.tex` (Paper 47), 53 pp., after the additions of 2026-09-21/22

Scope: whole paper, one pass, as a top-journal referee. R1 (`TEX_ADVERSARIAL_REVIEW_R1.md`) was read
first; its 23 findings are **all verified repaired** in the current file (spot-checked: Rem. 2.5
`\rem:Kprim` now states the two real conditions correctly; `prop:M` no longer calls the function
bounded and records the `log|τ|` growth; `prop:env` separates the multiplier-free threshold
`2πe^{A_T}` from `2πe^{A_T+‖ν‖_TV}`; `rem:RHcert` is explicitly labelled heuristic; `thm:W` allows
complex multipliers; the abstract now says "a lower bound for the bottom of the spectrum"). Nothing
below repeats an R1 finding.

**VERDICT: MAJOR REVISION.**

Not because a headline theorem is false — the core (`thm:D1`, `thm:O`, `thm:E`, `thm:Z`,
`thm:Zexh`, `cor:RH`, `thm:C`, `thm:N`, `thm:Np`, `thm:finDet`/`thm:finZ`) survives a full reading
and several independent re-derivations — but because (a) one theorem, `thm:AL`, is stated under
hypotheses that contradict the paper's own Definition `def:W` and mis-identifies the density of
`ν_w` (Finding 1, FATAL as stated); (b) the paper's central constant `A_T` at `log 2` is printed
with two different values in two places, one of them load-bearing for `cor:arena` (Finding 2);
(c) `cor:KEP08` — the only unconditional statement in the KEP subsection, and a clause of the
abstract — is not proved on the whole range it claims (Finding 3); (d) at 53 pp. the paper has
grown by accretion and needs the restructuring of §4 below before it is refereeable at length.

Severity: **FATAL** (statement false or unprovable as written) / **MAJOR** (proof incomplete, label
unearned, statement overclaims, or a printed constant is wrong) / **MINOR** / **COSMETIC**.

---

## 1. GLOBAL CONSISTENCY

### 1.0 Mechanical checks — CLEAN

- **Labels/references.** Every `\ref` resolves; no duplicate `\label`; no dangling label. The only
  labels never referenced are `eq:*` (all used through `\eqref`) and five `subsec:*` anchors —
  harmless.
- **Bibliography.** Every `\cite` has a `\bibitem` and every `\bibitem` is cited. Zhu, Groskin,
  Suzuki (×3), Connes–Consani, Kreĭn, Sasvári, Schoenberg, Karlin, Bombieri–Lagarias, Coffey are
  all present with complete entries (lines 3195–3244). Two register notes only: `Coffey2004` is
  keyed 2004 but the entry reads "**8** (2005), 211–255" (line 3203–3204) — pick one; and
  `Groskin2026`/`Zhu2026` carry arXiv numbers (2607.02828, 2608.24827) that a referee cannot
  resolve — R1's Finding 18 flagged this and it is unchanged. **MINOR.**
- **`thm:finZ` is not proved twice.** The old five-step proof now lives only inside `thm:finDet`
  (lines 1380–1425); `thm:finZ` (1438–1452) is four lines and derives from it. The derivation is
  complete: `lem:fdict` gives `φ = w·g_Z` positive definite with `φ̂ = f_{w,Z} ∈ L¹`,
  `∫f_{w,Z} = 2πd`, hence `ν_w := f_{w,Z}dτ/2π` is a finite positive symmetric measure whose
  transform equals `g_Z` on `(−2T,2T)`; `thm:finDet` forces `ν_w = μ_Z`, i.e. `w·g_Z = g_Z`; the
  Cesàro/geometric-sum contradiction with `w(ma) → 0` closes it. I re-derived each step. **CLEAN.**
- **`rem:galerkin` rule.** Grep for `10^{-6}`, `10^{-7}` near `log 2`: **no numerical value of
  `inf W` at a two-prime window is printed anywhere.** The only two-prime numbers are (i) the
  Galerkin *upper* bound `2.16·10^{-4}` at `T = 0.58` (line 1120, explicitly `\textsc{diagnostic}`),
  (ii) the *archimedean* values `λ^{∞,P} ≈ −0.154`, prime form `≈ +0.188` at `log 2` (lines
  2476–2478), which are not `inf W`, and (iii) the certified subspace eigenvalues of `thm:nest`,
  which are eigenvalues on `E_k`, not on `P_T`. `rem:galerkin` (2567–2574) is correctly worded.
  **CLEAN** — with one exception, Finding 8 below (line 2486 calls a Galerkin upper bound "truth").
- **"primitive form" vs "complete form".** Used correctly throughout. `thm:C` = primitive (`λ^P`,
  line 921); Zhu = complete (`Q = W_T`, lines 1018–1019, 1732–1734); `cor:KEP08` rests on Zhu and
  says so (line 1733, and the remark 1737–1745 explains why `thm:C` does *not* give it, with the
  correct quantitative reason `|β₀−2|ĝ₀(0) = 5.9·10^{-3} ≫ c = 8.86·10^{-5}`). §1.4 (lines 285–290)
  states the same. **CLEAN and well done** — this is the sharpest part of the label discipline.

### Finding 1 — FATAL (as stated). `thm:AL` (lines 2930–2959): hypotheses contradict `def:W`, and `G` is not the density of the a.c. part of `ν_w`

Three independent defects in one statement:

1. **Line 2931–2932:** "*Let `w` be a flat-top weight with `w ≡ 1` on `[0,2T]` and on `[U,∞)`*".
   A weight that is `≡ 1` on `[U,∞)` is not in `W_T` (Def. `def:W`, line 2144–2145, requires
   `|w(u)| ≤ Ce^{−(1/2+δ)|u|}`), and for such a `w` the measure `ν_w` of `eq:nuw` is **infinite**
   (its density contains `2w(u)cosh(u/2)`), so `(ν_w,2,0)` is not a dual feasible point and
   `c_w = inf f_w` is not "the value of the continuous dual point" (line 2934). Presumably the
   intended hypothesis is `w ≡ 0` on `[U,∞)`.
2. **Line 2932–2933:** "*let `G = (1−w)K` be the density of the absolutely continuous part of `ν_w`
   on `[2T,U]`*". By `eq:nuw` (line 1148) that density is `½(1−w)K + 2w cosh(u/2)`. Both the factor
   `½` and the entire `cosh` block are missing. I checked the `½` against the proof of `thm:Z`
   (line 1178) and against `thm:Dtail` (lines 1794–1798): the paper's own convention is
   `ν̂_w|_K = ∫_{2T}^∞(1−w)K cos τu du`, i.e. density `½(1−w)K`. So `G` as defined is off by 2.
3. Consequently the conclusion is a statement about `Ĝ_e` alone, whereas `c_lat(M)` is the value of
   the full certificate `σ_T + ν̂_lat + β·ĝ`. The proof (2948–2958) only compares `ν̂_lat` with
   `Ĝ_e` and never restores the `2ŵcosh`/`2ĝ₀` block, which by the paper's own
   `thm:Dtail` (1798–1804) is exactly the block that carries the irreducible `O(τ^{-1})` edge term.
   Nor are the prime atoms of `ν_w` (`−Σ_{n∉N_T}(v_n/2)w(log n)δ_{±log n}`) sampled or accounted.

**Edit:** either restate `thm:AL` for the object it actually proves — an aliasing bound
`|ν̂_lat(τ) − Ĝ_e(τ)| ≤ ε_r(M)` on `|τ| ≤ P/2` for a compactly supported even `G ∈ C^{r-1}` with
`G ≡ 0` on `[−2T,2T]`, which *is* correct and is a clean lemma — and then derive `c_lat` by adding
the `cosh` block and the atoms explicitly; or withdraw the theorem and keep `cor:ALdef`'s
qualitative reading, which does not depend on it. As it stands neither `thm:AL` nor `cor:ALdef`
("the lattice costs `O(M^{-r})`") is supported.

One further item inside the proof is correct and should be kept: "*`(D)` imposes no moment equality
on `ν`*" (line 2949–2950) is right — `def:PD` constrains only `supp ν ⊆ {|u| ≥ 2T}` — and the
boundary atom at `±2T` is harmless by `c_F(±2T) = 0`, exactly as in `prop:weak`. Also the parenthesis
"*minus the deleted low atoms, which are absorbed in the flat-top window*" (2952–2953) is vacuous
rather than wrong: `G_e(jd) = 0` for `|j| < M` since `w ≡ 1` there. Say so instead.

### Finding 2 — MAJOR. Two different values of `A_T` at `T = log 2` are printed: `2.24883` and `2.24889`

- Line 1119: "`A_T = 2.24883`, `B = 7.62101`" (§6.4, two-prime windows).
- Line 2222: "`A_T = 2.24883`" (`thm:Np`).
- **Line 2709: "`At T = log2, where A_T = 2.24889`"** (`cor:arena`).

I computed `2·log2/√2 + 2·log3/√3 = 2.2488263447…`, so **`2.24883` is right and `2.24889` is a
typo**. It is not cosmetic: `cor:arena` uses it in a two-sided comparison at the margin,
"`m(τ₁₁) ≤ 2.2168 ≤ A_T` and `m(τ₁₂) ≥ 2.2596 > A_T`". I checked that the conclusion `N* ≥ 12`
**survives** with the correct value (`2.2168 ≤ 2.24883 < 2.2596`), so no result changes — but a
referee who recomputes will stop here. Corroboration that `2.24883` is the paper's own value:
`cor:mono`'s printed `2.327` at `log 2` is `C₀ + 2.2488263 + φ((3π/2T)²)`, which I reproduce as
`2.326752`. Also check `B = A_T − C₀`: I get `7.6210097`, and line 1054 prints `7.621`, line 1119
`7.62101` — consistent.

**Edit:** `2.24889 → 2.24883` at line 2709.

### Finding 3 — MAJOR. `cor:KEP08` is not proved for `T < ½log2`, yet claims "every `T ≤ 0.8`"

`cor:KEP08` (1726–1735) concludes indeterminacy "for every `T ≤ 0.8`" by monotonicity of `λ^W` plus
`thm:KEP3(a)`. But `thm:KEP3(a)` is stated **"For every `T ≥ ½log2`"** (line 1704), and the route
through `thm:Zexh(i)` genuinely needs `T ≥ ½log2` (line 1199, and the proof's use of
`D(u) > 0` for `u ≥ 2T ≥ log2`, line 1212–1213). So the range `0 < T < ½log2 = 0.34657` is
uncovered. The repair exists three lines away and the author already wrote it: it is the
`(1)⇒(4)` small-`T` device of `thm:KEP3(b)` (lines 1717–1721), "*a certificate at `T' = ½log2` is
one at `T`, and the perturbation of `thm:KEP1(ii)` applies, its `χ` being supported in
`{|u| ≥ log2}`*". **Edit:** add one sentence to the proof of `cor:KEP08` invoking that device for
`T < ½log2`.

### Finding 4 — MAJOR. The abstract's KEP clause does not attribute the unconditional half to Zhu

Abstract, lines 100–101: "*RH is equivalent to the indeterminacy of a Kreĭn extension problem at
every window, **a property that holds unconditionally for `T ≤ 0.8`**.*" The equivalence is the
paper's (`thm:KEP3`); the unconditional clause is **entirely** Zhu's `Thm. 1.2`, cited and not
re-verified (line 1733, and the §9 table entry at 3133 says so plainly). §1.4 also says so
(lines 287–289). The abstract is the one place a reader takes the claim at face value, and it is
the one place the attribution is missing. **Edit:** "…*a property that holds unconditionally for
`T ≤ 0.8`, by Zhu's certificate for the complete form* \cite{Zhu2026}."

### Finding 5 — MINOR. "the first window in which a prime is coupled" is false (twice)

Lines 85–86 (abstract) and 200–201: `T = ½log3` is called "*the first window in which a prime
(`n = 2`) is coupled*". The contact set `N_T = {n ≥ 2 : log n < 2T}` becomes non-empty at
`T > ½log2 = 0.34657`, not at `½log3 = 0.54931`. Every `T ∈ (½log2, ½log3)` couples `n = 2`.
**Edit:** "*a window in which exactly one prime is coupled*", or "*the largest window with a single
contact*" (which is correct: `N_T = {2}` for `½log2 < T ≤ ½log3`, since `n = 3` enters at `½log3`).

### Finding 6 — MINOR. `−3.18·10^{-3}`, `−3.1964·10^{-3}`, `−3.20·10^{-3}` for one number

Line 1126 gives the computed value `−3.1964·10^{-3}`; lines 218 (intro) and 3111 (§9 Open (3))
round it to `−3.18·10^{-3}`; line 2918 rounds it to `−3.20·10^{-3}`. **Edit:** `−3.20` everywhere
outside line 1126.

### Finding 7 — MINOR. `thm:N` Step 4 says "three enclosures" and then lists four

Line 2173: "*The same **three** enclosures … give `c ≤ −9.038987·10^{-2}` (`M=3`),
`−6.234677·10^{-2}` (`M=5`), `−2.175677·10^{-2}` (`M=6`) and `−4.242754·10^{-2}` (`M=7`)*". Four
values. The §9 table (line 3143) correctly says "`M = 3,5,6,7,8` by interval enclosure", i.e. five
enclosures in all. **Edit:** "three" → "four".

### Finding 8 — MINOR (rule 3). A Galerkin upper bound is called "a truth"

Line 2486: "*which at `T = ½log3` reads `≥ −0.92` against **a truth** of `+9.8·10^{-4}`*". The
number `9.8·10^{-4}` is the Galerkin upper bound `9.893·10^{-4}` (line 907, `\textsc{diagnostic}`),
not a truth. The paper's own convention (line 353, "*Galerkin eigenvalues are variational upper
bounds … and are always quoted as such*") is violated here. **Edit:** "against a
\textsc{diagnostic} upper bound of `9.89·10^{-4}` and a certified lower bound of `8.86·10^{-5}`".

### Finding 9 — MINOR. `thm:nest`'s first certified eigenvalue is inconsistent with `thm:w11`

`thm:w11` certifies `W_{log2}[F*] ∈ [0.0342113430, 0.0342182500]` (line 2538). `thm:nest` lists the
certified `λ_min` on `E_1 = span{F*}` as `3.4212·10^{-2} = 0.034212` (line 2597), which is **larger**
than the certified lower endpoint `0.0342113`. A certified lower bound cannot exceed the lower end
of its own enclosure. Presumably `3.4211·10^{-2}` was intended (or the `E_1` entry is a midpoint,
which would be a labelling error in a `\textsc{proved (machine-verified)}` list).
**Edit:** `3.4212·10^{-2} → 3.4211·10^{-2}`, or state that the listed values are lower bounds and
round down throughout.

### Finding 10 — MINOR. `rem:RHcert` (the only explicitly heuristic passage) is absent from the §9 table

Statements carrying a `\label` and missing from the §9 table: `def:PD`, `def:W`, `prob:A`,
`prob:B`, `rem:Kprim`, `rem:OvsB`, **`rem:RHcert`**. The first six are definitions, problems or
cross-reference remarks and may fairly be omitted; `rem:RHcert` is the paper's one heuristic
paragraph ("*This paragraph is heuristic*", line 1593) and the table is precisely where a reader
looks to find out. **Edit:** add a row "`rem:RHcert` (why `β₀ → 2`; the certificate at infinity) —
\textsc{heuristic}".

Everything else in the §9 table checks out: every label in it exists, and I verified each label
against the body for `thm:C`, `thm:N`, `thm:Np`, `thm:w11`, `thm:nest` (all four
`\textsc{proved (machine-verified)}` in body **and** table), `cor:KEP08` (\textsc{proved},
resting on `\cite{Zhu2026}` \textsc{cited, not re-verified} — matches body), `prop:NC`, `thm:J`,
`thm:arena`/`cor:arena`, `thm:Dtail`, `rem:comblp` (\textsc{diagnostic} in body and table),
`rem:Zcheck`, `rem:nodal`, `rem:signrule`, `prop:arch`, `rem:PF2`, `thm:P3`, `cor:AP`, `cor:CP`,
`thm:AL`, `prop:schur`, `prop:G`, `lem:N`, `lem:smooth`, `cor:Li`, `lem:Rrig`, `lem:fdict`,
`thm:finDet`, `thm:finZ`, `prop:finuniv`, `cor:infinite`. **No mismatch found.**

---

## 2. ABSTRACT, CLAIM BY CLAIM

Numbering the abstract's assertions in order of appearance (lines 71–104):

| # | claim | line | supported? |
|---|---|---|---|
| A1 | `A_T` = truncated Weil form with the two Tate moments killed; positivity for every `T` ⟺ RH | 71–73 | **YES** — §1.1, lines 127–134, via `\cite[Thm.~10.4]{Paper45}`, `\cite[Thm.~1]{Bombieri2000}`. |
| A2 | Lévy exponent representation of `m` with `K(u)=½/sinh+½/cosh` completely monotone | 74–77 | **YES** — `lem:K`, re-derived; the three forms of `K` and the digamma integral both check. |
| A3 | the infimum over the primitive autocorrelation class **is a lower bound for the bottom of the spectrum of `A_T` on `P_T`** | 77–79 | **YES**, and this is the R1 Finding-2 repair: the paper now claims `λ^P ≤ λ^A` (`thm:A`, `rem:Kprim`) and never `λ^P = λ^A`. Correct. |
| A4 | that infimum is the value of a semi-infinite LP with dual variables outside `[−2T,2T]` plus two polar multipliers; strong duality with finitely atomic duals (`thm:D1`) | 79–83 | **YES** — `thm:D1`, lines 498–544. The interior-point argument (step ii) and the Cesàro/`ĝ`-determinant argument are both sound; the `2×2` determinant `sinh T cosh T + T > 0` is correct. |
| A5 | the dual supremum is never attained by finite objects (`thm:O`) | 83–84 | **YES** — `thm:O`, 562–590. The contradiction (bounded continuous `Σβ_jh_j` vs `½K(u) ~ 1/(2u)` plus atoms) is airtight, and it is correctly noted to hold for `v = 0`. |
| A6 | exponential columns exhaust the dual (`thm:E`) | 84 | **YES** — `thm:E`, 838–858; the totality of `{t^pe^{-t}}` in `L¹` is correctly justified. |
| A7 | tail lemmas make any certificate verifiable on a bounded interval | 84–85 | **YES** — `lem:F1`, `lem:T`, `lem:hybrid`, `prop:TAY`, and now also `thm:Dtail`. |
| A8 | explicit certificate proving `λ_min ≥ 8.8577·10^{-5}` at `T = ½log3` | 85–86 | **YES** as to substance (`thm:C`), but **`λ_min` is bare** and the body proves `λ_A ≥ λ^P ≥ c` for the **primitive** form. A reader will take `λ_min` for `λ^W`. **Edit:** write `λ_min(A_T|P_T)`. **MINOR.** |
| A9 | "the first window in which a prime is coupled" | 86 | **NO** — Finding 5. |
| A10 | the optimal multiplier restores exactly the two polar terms of the explicit formula | 86–87 | **YES** as a statement about the *computed* `β₀ = 2.0026` (§5.2 item 1) plus `prop:P`'s theorem that `β₀ = 2` is the unique multiplier bounding `W_T`. The word "exactly" is doing rhetorical work for a number that is `2.0026`, not `2`; the body is careful (line 648: whether the optimal duals converge to `(2,0)` is \textsc{open}). **Edit:** "…restores, to within `1.3·10^{-3}`, the two polar terms". **MINOR.** |
| A11 | the exchange between escaped primal mass and value is exactly logarithmic (`thm:Vp`) | 88–89 | **YES** — `thm:Vp`(i)(ii)(iii), 1053–1084; the construction in (ii) with the `λ`-mixture correcting the moment defect is correct. |
| A12 | no pointwise envelope can lower the verification threshold `2πe^{A_T}`, `A_T = Σ_{n<e^{2T}}2Λ(n)/√n` | 89–91 | **YES** — `prop:env`(ii) via `lem:mbounds`(iii) (Kronecker). The R1 Finding-7 repair (separating the multiplier-free threshold) is in place. |
| A13 | lattices of order `M ≤ 8` cannot certify at `½log3` (`thm:N`) | 91–92 | **YES** — `thm:N`. Labels match; the `β`-box logic (only the *qualitative* content of `thm:Bbeta` is used, with a factor 21 to spare) is sound, and the sublattice-inclusion reduction for `M ∈ {1,2,4}` is correct. |
| A14 | lattices of order `M ≤ 24` cannot certify at `T = 0.68` or `log 2` (`thm:Np`) | 92–93 | **YES** — `thm:Np`. The sixteen enclosed `M` are `{6,7,9,11} ∪ {13,…,24}` = 16 ✓, and the omitted `{1,2,3,4,5,8,10,12}` all divide 20 or 24, both of which are enclosed ✓. The archived-node guard (residuals `< 10^{-60}`, and the candid footnote about the earlier run with coincident nodes) is exactly the right level of disclosure. |
| A15 | a proved positive value of the complete form at `log 2` in one explicit direction (`thm:w11`) | 93–94 | **YES** — `thm:w11`, and the body correctly insists it is "*one direction, not a sign for the form*" (2563–2565). |
| A16 | "*its positive definiteness on nested seven-dimensional even subspaces*" (`thm:nest`) | 94–96 | **PARTLY** — the subspaces are nested of dimensions `1,…,7`; "nested seven-dimensional subspaces" reads as seven subspaces each of dimension 7. **Edit:** "on a nested tower of even subspaces up to dimension seven". **MINOR.** |
| A17 | the dual variable **is** the explicit formula; every certificate is, up to arbitrarily small correction, the explicit formula on `w(u)cos(τu)` (`thm:Z`) | 96–100 | **YES** — `thm:Z`(i)(ii) and `thm:Zexh`. I re-derived `eq:fw` term by term against `eq:nuw` (the `½` on the `K` block, the `4∫_{2T}^∞ w cosh cos + 2ĝ₀ = 2Ŵ` regrouping) and it is right. |
| A18 | `λ_min` is the best lower bound for the flat-top smoothing, and RH ⟺ existence of one such one-sided smoothing per window | 100–101 | **YES** — `cor:RH`. The `(a)⇒(c)` direction's Jensen/exponential-type argument (`N(t) ≫ t log t` beats the `O(t)` zero count of a type-`T` entire function) is correct. |
| A19 | RH ⟺ indeterminacy of a Kreĭn extension problem at every window | 101–102 | **YES** — `thm:KEP3`(b). |
| A20 | "…*a property that holds unconditionally for `T ≤ 0.8`*" | 102–103 | **YES in substance, MIS-ATTRIBUTED and under-proved** — Findings 3 and 4. |
| A21 | "*We state precisely what a closing argument must do, and what the theorems here show it cannot be.*" | 103–104 | **YES** — §8.1–§8.3, `prob:A`, `prob:B`. |

Net: 17 clean, 2 wording repairs (A8, A16), 1 factual slip (A9), 1 attribution + range gap (A20).
**No clause of the abstract asserts a sign for `ζ` beyond `T ≤ log 2`.**

---

## 3. RIGOUR SPOT-CHECKS (proofs read in full)

**`thm:KEP1`–`thm:KEP3`, `cor:KEP08`.** The form core in `thm:KEP2` (lines 1694–1700) is
correct and carefully done: dilation `F_λ(t) = F(t/λ)` with `F̂_λ(τ) = λF̂(λτ)`, convergence in the
`log(2+|τ|)`-weighted norm because the weight is doubling, then mollification below scale
`(1−λ)T`. The tempered pairing in `thm:KEP2` is legitimate (`ĥ = |F̂|² ≥ 0` rapidly decreasing
against a positive tempered `ν`). The continuum construction in `thm:KEP1`(ii) is correct in
substance — `χ` supported in `{|u| ≥ max(2T, log2)}` so that the prime atoms it touches are all
*outside* the window and `D(u) = 2cosh(u/2) − ½K(u) > 0` is available — **but the displayed `r_χ`
carries a factor-2 error**: from `eq:nuw`, perturbing `w ↦ w + εχ` changes `ν̂_w` by
`ε[2∫_ℝ χ cosh cos − Σv_nχ(log n)cos − **½**∫_ℝ χK cos]`, whereas line 1669 prints
`−∫_{|u| ≥ 2T} χ(u)K(u)cos τu du`, which over the symmetric support is `∫_ℝ`, i.e. twice too much.
Nothing downstream uses the constant (only `|r_χ| ≤ R` and `r_χ ≢ 0`, and the non-vanishing
argument correctly goes through the density `χD`), so this is **MINOR**, but it should be fixed:
`−∫ → −½∫_ℝ`, or restrict the displayed integral to `u ≥ 2T`. Strictness under RH via `cor:RH`'s
proof (`λ^W > 0`, not merely `≥ 0`) is used correctly in `thm:KEP3`(b)(1)⇒(4) and is the right
hypothesis for `thm:KEP1`(ii). `thm:KEP1`(iii) (`μ_ζ` purely atomic, hence distinct from every
`ν_w`) is clean. `cor:KEP08` — Finding 3.

**`thm:finDet`.** All five steps verified. Step 1's lattice `a ∈ (0, 2T/d] \ E` with `r ≤ d` gives
`ra ≤ 2T`, so `φ(ka) = g_Z(ka)` is asserted for `|k| ≤ r` — but the hypothesis `ν̂ = g_Z` is only on
the **open** `(−2T,2T)`, and the case `r = d`, `a = 2T/d` puts `k = r` exactly on the boundary.
**MINOR gap, trivially repaired:** take `a ∈ (0, 2T/d)` in Steps 1–4 and recover the endpoint in
Step 5 by the continuity argument already written there. Step 2's `A = V*DV`, `rank A = r`,
`ker A = ℂ·v` with `v` the coefficient vector of `∏(z − z_j)`, `v ∈ ℝ^{r+1}` by conjugation-closure,
`|v₀| = 1 ≠ 0`: correct. Step 3's extraction of `b*v = 0` from the `(r+2)`-point Gram matrix by
choosing the phase of `t` adversely and letting `|t| → 0` is the right argument (the `|t|²c₀` term is
second order). Step 4's induction uses `v₀ ≠ 0`, which Step 2 supplies. **Step 5 (variable lattice
step) is the new and correct idea** and is exactly what buys "no decay hypothesis and no product
structure": fix `m`, note the identity holds off a discrete `E`, both sides continuous in `a`, then
`⋃_m m·(0,2T/d] = (0,∞)`. Uniqueness among finite symmetric measures then follows from uniqueness of
the spectral measure of a continuous positive definite function, correctly routed through
`prop:finuniv`(ii) — and `prop:finuniv`(ii) is itself honest about why symmetry is needed
(even test functions determine only the even part). **CLEAN.**

**`thm:J`.** Dirichlet modes `sin(jπ(t+T)/2T)` span `D_k ⊂ H¹₀(I_T)` with
`‖F'‖² ≤ (kπ/2T)²‖F‖²` ✓. Jensen in the variable `τ²` against `dμ = |F̂|²dτ/(2π‖F‖²)` requires `φ`
concave, which is `thm:S`(i) (complete Bernstein ⇒ concave) ✓, and `∫τ²dμ = ‖F'‖²/‖F‖²` by
Plancherel ✓. `φ(τ₀²) = −C₀` is exactly `m(τ₀) = 0` ✓ — I recomputed `τ₀ = 6.2898359888369…`,
matching the printed `6.28983599…` to all digits shown. Largest `k` with `kπ/2T < τ₀` is
`⌈2Tτ₀/π⌉ − 1` ✓ (for `2Tτ₀/π ∉ ℤ`). The `−3`: `⌈·⌉ − 1` on `L²(I_T)`, minus 2 for the codimension
of `P_T` ✓. **The vacuity statement is correct and honestly flagged:** `2Tτ₀/π = 2.1996` at `½log3`
and `2.7755` at `log 2` (I reproduce both), so the `P_T` bound reads `n_- ≥ 0` at both windows, and
line 3036 says so in italics. The matching asymptotic `n_-(A_∞|P_T) = (2τ₀/π)T + O(log T) =
4.004T + O(log T)` — I get `2τ₀/π = 4.00423` ✓, and the upper half is correctly flagged as resting
on Landau–Widom, \textsc{cited, not re-verified}. **CLEAN.**

**`thm:arena` / `cor:arena`.** Even min–max: `A_∞` commutes with parity; on even functions the two
Tate conditions coincide (both read `∫F cosh(t/2) = 0`), so `P_T^ev` has codimension **1** in
`L²_ev(I_T)` ✓ — this is the step that makes the `k+2` even Dirichlet modes
`cos((2j+1)πt/2T)`, `j ≤ k+1`, leave a subspace of dimension `≥ k+1` ✓, and min–max then bounds
`λ^ev_{k+1}` ✓. The `O`-terms: `m(τ) = log(τ/2π) + O(1/τ)` by `lem:mbounds`(ii), and
`τ_k = (2k+3)π/2T`, so `m(τ_k) = log k + O(1)` ✓. `cor:arena`'s counting identity
`#{k ≥ 0 : k ≤ Tτ*/π − 3/2} = ⌊Tτ*/π − ½⌋` ✓. The two window evaluations rest on the **exact
`lem:mbounds`(ii) lines**, as claimed — I re-derived `τ₁₁ = 25π/(2log2) = 56.65`,
`τ₁₂ = 27π/(2log2) = 61.18`, and the printed brackets `2.2168`/`2.2596` straddle the correct
`A_T = 2.2488263`, so **`N* ≥ 12` at `log 2` and `N* ≥ 2` at `½log3` both hold** — but see
Finding 2 for the printed `A_T`. The asymptotic `N* ≥ 2Te^{A_T}(1+o(1)) = exp(4e^T(1+o(1)))` is
correct (the `2T` factor is absorbed since `A_T ~ 4e^T`). **CLEAN modulo Finding 2.**

**`thm:AL`.** See Finding 1.

**`prop:NC`.** Correct and pleasingly explicit. `A_∞(F) ≥ C₀b + m(τ₁)(1−b)` on `P_T` (pole term
vanishes, `m` increasing) ⇒ `A_∞(F) < 0` forces `b > θ(τ₁)` ✓; min–max on an `n`-dimensional
negative subspace gives `λ_{n-1}(S) > θ` ✓; Markov with `tr S_{T,τ₁} = 2Tτ₁/π` ✓. The band-split is
the whole argument and it is clean. I independently minimised `2τ₁/(πθ(τ₁))` over `τ₁ > τ₀` and get
the minimum `68.5135` at `τ₁ = 14.88` — matching the printed `τ₁ = 14.8815`, `68.51T` — and
`⌊68.51T⌋ = 37, 47, 54` at `½log3`, `log2`, `0.80` ✓ exactly as printed. **CLEAN.**

**`thm:Dtail`.** The regrouping with `2ĝ₀` is the heart of the theorem and is done right, including
the *reason*: the density of `ν_w` at `2T⁺` is `2cosh T ≠ 0`, so `ν̂_w` alone is only `O(τ^{-1})`,
and `2ĝ₀(τ) = 4cosh T sin(2Tτ)/τ + O(τ^{-2})` (from `lem:gbounds`) cancels the edge term exactly,
which is visible because `W = w(|u|)cosh(u/2)` has no edge at all (lines 1798–1804). Integration by
parts: `2Ŵ = −2τ^{-2}∫e^{iτu}dW'`, `|2Ŵ| ≤ 2V(W')τ^{-2} = 4∫_0^∞|W''|τ^{-2} = D_c` ✓; for
`R = (1−w)K`, `R(2T) = R'(2T) = 0` because `w ≡ 1` and `w ∈ C¹` across the edge, so the even
zero-extension is `C¹` with `R'` of bounded variation, and `Ψ_w = ½R̂` gives
`|Ψ_w| ≤ ½V(R')τ^{-2} = D_K τ^{-2}` ✓ — the `½` is handled correctly here, which is what makes
Finding 1(2) a genuine slip rather than a convention change. The **atoms** carry no decay and are
bounded only by `E_at(w)`, correctly, with the `s > ½` threshold appearing in the same place in
case (b) as in `def:W` ✓. `cor:comb` and `cor:bprof` follow. `rem:Dgrade`'s claim that `τ^{-2}`
cannot be improved without `w ∈ C³` is consistent with `rem:loc`. **CLEAN.**

**`lem:Rrig` / `lem:fdict`.** `lem:Rrig`: the summability route (Gauss–Weierstrass means, monotone
convergence against `ŵ ≥ 0` giving `∫ŵ = 2πw(0) < ∞`, then Bochner) is correct, and the
`3×3` Gram inequality `|φ(u+a) − φ(u)|² ≤ 2φ(0)(φ(0) − Re φ(a))` with `w(a) = w(0) = 1` forcing
every `a ∈ (0,2T]` to be a period, hence (continuity) `w ≡ 1 ∉ L¹`, is airtight and elegant.
`cor:nontermwise` correctly patches the measurable-vs-continuous gap. `lem:fdict` is the clean
dictionary and both directions are proved. **CLEAN.**

**`prop:schur`.** The algebraic identity `w[F] = w₁₁(x + β(G)/w₁₁)² + s[G]` is pointwise and uses no
topology, as stated ✓. Converse conditions: `(⇐)` both terms `≥ 0` ✓; `(⇒)` take
`x = −β(G)/w₁₁` and use `‖xe + G‖ ≥ ‖G‖` (valid since `G ⊥ e`) ✓; the coercive converse correctly
requires `β` bounded ✓. (ii) `w₁₁ = 0` forcing `β ≡ 0` by letting `x → ±∞` ✓. (iii) `L^{-1} =
I + w₁₁^{-1}(b ⊗ e)` requires `(b⊗e)(b⊗e) = ⟨b,e⟩ b⊗e = 0`, true since `b ∈ V = e^⊥` ✓; and the
insistence that a congruence "*preserves the sign of the form and not its eigenvalues*" is exactly
the right caveat. The parity splitting (`R`-invariance of `A_∞`, `Π_T` and `P_T`; `β` vanishes on
`V_odd` for even `e`) ✓. **CLEAN.**

**`thm:w11`, `thm:nest` — the computational trust base.** The paper states it, and I record it here
explicitly since the brief asks for it. It is: (1) **`mpmath` 1.3.0 interval arithmetic** (`iv`),
declared at line 3193, at 25 digits for `thm:N`/`thm:Np` and 40 digits for `thm:C`; (2) **archived
coefficient vectors read as exact decimal data** — for `thm:w11`/`thm:nest` the degree-17 even
Legendre coefficient vectors of `F* = e₁, e₃, …, e₁₃`, with the disclaimer "*how it was obtained is
irrelevant to the statement*" (line 2546), which is the correct posture; (3) **panel construction**:
`K` squeezed between two affine functions on each panel of `[δ,2T]`, licensed by convexity of
`1/(2sinh(u/2))` and concavity of `1/(2cosh(u/2))` for `u/2 < arccosh√2 = 0.88137`, which covers
`T = log2 < 0.88137` — I checked this inequality and it is right, and it is the one place where the
method would *break* at a wider window, which the paper does not say and should; (4) exact interval
polynomial autocorrelation by rational arithmetic on the Legendre recurrence, no quadrature and no
interpolation, so **no quadrature remainder enters** the body integral; (5) the `[0,δ]`,
`δ = 10^{-6}` endgame via `K(u) ≤ u^{-1} + ½` and `g(u) ≤ G₁u`; (6) closed forms in intervals for
`C₀`, `∫_{2T}^∞K`, and the atoms by interval Horner.

**On the archived `F*` and `P_T`: the defect *is* declared and *is* accounted.** Step (f), lines
2558–2560: "*The enclosure does not assume `F* ∈ P_T`: it pays for the defect,
`|A|,|B| ≤ 1.30·10^{-14}` by exact interval integration of the polynomial against `e^{±t/2}`, so
`|2AB| ≤ 3.4·10^{-28}`.*" So `F*` is in `P_T` only up to `1.3·10^{-14}`, the pole term `2AB` is
bounded by `3.4·10^{-28}`, and that bound is inside the total width `6.91·10^{-6}` by 22 orders.
**This is exactly right and is the single best-executed piece of machine-verification hygiene in the
paper.** `thm:nest` extends it correctly: only *quadratic* values are enclosed, off-diagonals by
polarisation `W(e_i,e_j) = ¼(W[e_i+e_j] − W[e_i−e_j])`, with the stated reason — the affine sandwich
is licensed by `c(0) − c ≥ 0`, which is Cauchy–Schwarz for an **auto**correlation and false for a
cross-correlation (lines 2609–2610). That is precisely the trap, and the author saw it. Interval
Cholesky of `M − μI` with every pivot interval strictly positive certifies `λ_min > μ` for every
real symmetric matrix in the interval matrix ✓; the Gram defect `1.07·10^{-15}` per entry handles
the Rayleigh transfer ✓. **CLEAN**, modulo Finding 9 (the `E₁` digit).

**`thm:Np`, `thm:N` — the `β`-box tolerance form and the GL node guard.** The tolerance form is the
right design: the proof never uses the *value* of `V*/r₀`, only that `‖β‖_∞ ≤ B` for some explicit
`B` (`9.7·10^5` in `thm:N`, `4.7·10^9` in `thm:Np`), with margins of `21×` and `2.5·10^5×` over the
computed constants. This immunises the theorems against the floating-point provenance of `r₀, V*`
(which the §9 table at 3142 correctly labels as computed in floating point and used only through
the tolerance). Equally right: "*Any pair `(τ₀,q)` gives a valid bound, so the provenance of the
pair — in practice a double-precision eigenvector — is irrelevant to the proof*" (2162–2163), and
"*nonnegativity of `φ` is structural, since it is evaluated as a sum of two squares*" (2254–2255).
The **GL node guard** is disclosed with unusual candour (lines 2262–2266): nodes Newton-refined at
60 digits, widened before entering interval arithmetic, guarded by archived residuals
`max_i|P_p(x_i)|` and `|Σw_i − 2|`, both `< 10^{-60}`, **and** the parenthetical that an earlier
run without the guard produced two coincident nodes, `Σw_i = 2.19`, and an "enclosure" not
containing the true value. That disclosure should stay in the published version; it is what makes
the remainder formula applicable to the rule actually used. The optimisation of `q` against
`a + B(|b₀|+|b₁|)` rather than taking the bottom eigenvector, driving `|b₀|+|b₁|` to `10^{-16}`–
`10^{-18}` so that the `β`-allowance is `< 1.3·10^{-11}` against `|a| ~ 10^{-6}`–`10^{-7}`, is the
correct design and is honestly costed (quadrature error `0%`–`6.7%` of `|a|`). The caveat that
steps `d` with `2T/d ∉ ℕ` are **not** covered is stated in both theorems ✓. **CLEAN**, modulo
Finding 7.

**`cor:Li`.** The Laguerre closed form is right: I verified `n = 1` end to end —
`Φ₁(γ) = 2/(4γ²+1) = (½)/(γ²+¼)`, and `w₁(u) = −½e^{-|u|/2}L₁'(|u|) = ½e^{-|u|/2}` has transform
`(½)/(¼+τ²)` ✓. `1 − 1/ρ = (γ+i/2)²/|γ+i/2|² = B(γ)` ✓, `B` a Möbius map with a simple pole at
`i/2` and simple zero at `−i/2`, so `B^n` has an `n`-fold pole at `i/2` and `B^{-n}` at `−i/2` ✓;
`½(B^n + B^{-n}) = 1 − n²/(2γ²) + O(γ^{-4})` gives `Φ_n ∈ L¹ ∩ C` ✓. **The three exclusions are all
three present and distinct** (lines 1317–1320): nonnegative transform, which `cor:nontermwise`
forbids; decay exactly `e^{-|u|/2}`, i.e. `δ = 0` in `def:W`; nowhere locally constant, so no flat
top. **The "zero half only" sentence is present and correctly sharpened** (1320–1324): `ŵ_n(±i/2) =
∞` and `Σ_mΛ(m)m^{-1}P_n(log m)` diverges (correctly, since `Σ_{m≤X}Λ(m)(log m)^j/m ≍ (log X)^{j+1}`),
so `w_n` is not an admissible test function at all and `λ_n` is the zero-sum half of a Weil
functional, not a Weil-functional evaluation. This is the right statement and it is proved.
**One MINOR branch slip:** the proof writes `θ(γ) = 2arg(γ + i/2)` while the statement writes
`θ(γ) = 2arctan(1/(2γ))`; these agree for `γ > 0` but not for `γ < 0` (`arg ∈ (π/2,π)` there).
`Φ_n = 1 − cos nθ` is even in `γ` under the `arctan` reading (since `arctan(1/2γ)` is odd), so the
statement is fine and only the proof's identification needs "for `γ > 0`, and by evenness".
**CLEAN modulo that.**

**`prop:NC` band-split, `lem:N`, `prop:G`.** `lem:N`'s reduction of `Re(R_Tτ_aR_T)` to the one-sided
overlap `∫_{a-T}^T F(z-a)e(z)dz` is verified (the adjoint term maps to the same expression under
`z ↦ −z` using evenness of both `F` and `e` — the evenness hypothesis is load-bearing and is
stated) ✓. `prop:G`'s sign forcing: for `a > T + max(z_F,z_e)` and `z ∈ (a−T,T)`, one has `z > z_e`
so `e(z) > 0`, and `z − a ∈ (−T,−z_F)` so `F < 0` by evenness ✓, interval non-empty since `a < 2T` ✓.
**CLEAN.**

**`thm:P3` / `cor:AP`.** I reproduced the three printed radii from
`R(ε,η) = 2πexp(1 + C₀ + G(ε)/η)` with `B = 7.621`: `8.98·10^5`, `1.02·10^{13}`, `2.70·10^{32}` —
all three match. The positive part `(E_R+C₀)^+` in (iii) is correctly flagged as non-cosmetic.
`cor:AP`'s `c ≤ (λ^P + ε + Wη)/(1−η)` ✓. **CLEAN.**

**`thm:SC` / `cor:SC1`.** I recomputed `A = 0.5636670136…` for the ten listed primes and
`C₀ + A + φ((3π/2T)²) = −2.1228307…` at `T = 6.869974` — matching the printed `−2.122831` exactly.
`T₀(0) = 0.7492069…` matches `0.74921` ✓. **CLEAN.**

**`prop:arch` — MINOR gap.** (iv) asserts `½log2 ≤ T*_∞`, but (iii) only gives `λ^∞(T) ≥ 0` for
`2T < log2` and explicitly declines to re-prove strictness ("*the strict inequality is not
re-proved here*", line 2388). A non-strict bound does not bound `sup{T : λ^∞(T) > 0}` from below.
**Edit:** either cite strict positivity from `\cite{Bombieri2000}`/`\cite{Yoshida1992}` (Yoshida
proves *strict* positivity at `a = ½log2`, so the citation is available) or weaken (iv) to
`T*_∞ ≤ T*_{∞,P} ≤ 0.74921`.

---

## 4. OVERCLAIM SWEEP

**No sign for `ζ` beyond `T ≤ log 2` is asserted anywhere.** §1.4 (lines 284–290) is explicit, and
line 1129–1130 repeats it at the point of maximum temptation: "*nothing is certified at any
`T > ½log3` by the methods of this paper, and the sign there rests on `\cite{Paper42,Zhu2026}`*".
`thm:w11` and `thm:nest` are both followed immediately by disclaimers that they are not a sign for
the form (2563–2565, 2624–2627). **No "first beyond log 2" claim appears** — the phrase does not
occur, and §1.3 states plainly "*Our window is smaller than Zhu's*" (line 267) and §5.3 "*his window
is larger*" (line 1019). **No positivity of the complete form at any window is claimed except by
Zhu** — verified against `cor:KEP08`, its remark, and the §9 table. **(H1) is not proved and is not
claimed**: the string "(H1)" does not occur; the nearest object is the hypothesis `n_- = 1` above
`T*_{∞,P}`, which `prop:NC`'s following paragraph (line 3004–3005) and the §9 table (3157) both
label `\textsc{hypothesis}` / "*not proved here*". **Clean on all four counts.**

### Finding 11 — MAJOR. "necessary" and "must exhibit" for a fact resting on a DIAGNOSTIC value

Lines 2478–2480: "*Past `T*_{∞,P}` the primes are therefore **necessary** and not a perturbation —
every proof of `λ_A ≥ 0` **must exhibit** `Π_T(F) ≥ −A_∞(F)` on a cone on which the archimedean
block is actively negative.*" What is **proved** (`prop:arch`(ii)) is `T*_{∞,P} ≤ 0.74921`. What
places `T*_{∞,P}` *below `log 2 = 0.6931`* — which is what the sentence needs at the window it is
applied to — is the **Galerkin** bound `T*_{∞,P} ≤ 0.5958` (line 2469), labelled `\textsc{diagnostic}`
two lines earlier, and the diagnostic value `λ^{∞,P} ≈ −0.154` at `log 2`. So the modal verbs are
unearned at `log 2` and at `½log3`; they are earned only for `T > 0.74921`.
**Edit:** "*For `T > 0.74921` the primes are provably necessary … ; the \textsc{diagnostic} Galerkin
bound `T*_{∞,P} ≤ 0.5958` suggests, but does not prove, that this already applies at `log 2`.*"

### Finding 12 — MINOR. "the endpoint of record" (twice) invites the wrong reading

Lines 2564–2565 and 2625: "*the endpoint of record remains that of Theorem `thm:C`*". Read cold,
this says `½log3` is the record endpoint for Weil positivity, which is false — Zhu holds `0.8` for
the complete form, and the paper says so elsewhere. **Edit:** "*the endpoint of record **for the
methods of this paper** remains Theorem `thm:C`*".

### Finding 13 — MINOR. `cor:nontermwise`'s "the whole family of strategies … is empty"

Line 1293. Correct as proved (`ŵ ≥ 0` is impossible for a flat-top `w ∈ L¹`), but "empty" is a
strong word for a statement whose hypothesis is the flat top; `cor:Li` then shows the Li kernels
evade it by *not* being flat-top. The two paragraphs together are honest; the single sentence, if
quoted alone, is not. **Edit:** "*the whole family of strategies "choose a flat-top `w` with
`ŵ ≥ 0`" is empty*".

Other modal usages checked and found **earned**: "cannot be lowered" (`prop:env`(ii), a theorem via
Kronecker); "cannot be shortened" (§8.3 item 3, same); "no rate lemma uniform over the feasible set
exists" (`thm:Vp`(iii), proved); "cannot converge" (line 2669, backed by `thm:arena`/`cor:arena`);
"never a termwise one" (`lem:Rrig`, proved); "is a search of an empty set" (`thm:Np`'s remark,
proved). `rem:LiSC`'s closing sentence is explicitly flagged "*an **interpretation**, not a theorem,
the two conditions being equivalent*" (2360–2361) — exactly right.

---

## 5. EXPOSITION: length, duplication, notation

At 53 pp. the paper carries three distinguishable research programmes (the duality theory, the
explicit-formula identification + Kreĭn reformulation, and the class impossibilities + archimedean
structure). §8 alone runs from line 1883 to 3104 — roughly 40% of the paper — and contains 9
subsections of very unequal weight. It is refereeable but not readable, and the accretion shows:
`Γ_T` is defined twice, `D` has seven meanings, and §8.6 interleaves three `\textsc{diagnostic}`
paragraphs between two theorems.

### Proposed structure

**Core (§2–§7, ~26 pp., unchanged in substance):**
- §2 the Lévy exponent (`lem:K`, `thm:S`, `thm:A`, `cor:mono`) — move `rem:PF2` to an appendix, it
  is a route-closure and interrupts the flow at line 425 before the duality has been stated.
- §3 the two programmes (`def:PD`–`prop:P`).
- §4 tail control (`lem:mbounds`–`prop:TAY`) — move §4.1 (`thm:P3`, `cor:AP`, `rem:P3exp`) to
  §4 end or to Appendix A; it is the most technical page in the paper and nothing before §8 uses it.
- §5 the certificate (`thm:C` + §5.2–§5.4) — **move `lem:bern` (§5.3) to Appendix A**; it is a
  methodological warning, not a result, and it is not used by `thm:C` (which uses no grid).
- §6 negative theorems.
- §7 the dual variable is the explicit formula (`thm:Z`–`cor:KEP08`, `thm:Dtail`).

**§8 split into three short sections:**
- **§8 class impossibilities** (`prob:A`, `prop:TK`, `thm:Bbeta`, `lem:val`, `thm:N`, `thm:Np`,
  `thm:SC`, `cor:SC1`, `rem:LiSC`) — one theme: what a class cannot do.
- **§9 archimedean structure** (`prop:arch`, `prop:nodes`, `prop:schur`, `thm:w11`, `thm:nest`,
  `prop:bprime`, `prop:shifts`, `thm:arena`, `cor:arena`, `lem:N`, `prop:G`, `prop:NC`, `thm:J`) —
  one theme: the operator without the primes, and what the primes must supply.
- **§10 the log-2 direction and what a closing argument must do** (`prop:decide`, §8.2–§8.4,
  `prob:B`, Verdict).

**Appendices:**
- **App. A — enclosure methods:** the two "*The enclosure*" paragraphs (2181–2203, 2253–2279), the
  trust base of `thm:w11`/`thm:nest` (the panel sandwich, the `arccosh√2` constraint, the
  polarisation rule, the interval Cholesky), `prop:TAY`, `lem:bern`, and the reproduction
  subsection. This is ~5 pp. of genuinely reusable methodology currently scattered across three
  sections in small type.
- **App. B — the Li/NB dictionary:** `cor:Li`, `rem:LiSC`, and the `Φ_n` computation. Self-contained
  and currently interrupting the flow between `cor:nontermwise` and `lem:fdict`.
- **App. C — the DIAGNOSTIC record:** `rem:Zcheck`, `rem:comblp`, `rem:nodal`, `rem:signrule`, the
  measured ceilings, the Galerkin thresholds, the `0.28M^{-1.2}` fit. Collecting these in one place
  would let §9's label table shrink by a third and would make the body's proved/measured boundary
  visible at a glance. **This is the single highest-value structural change.**

Estimated result: ~34 pp. body + ~12 pp. appendices.

### Finding 14 — MINOR. Duplicated definition: `Γ_T`

`Γ_T(F) = C₀‖F‖² + 𝔈(c_F)` is defined at line 2416 (`prop:nodes`) and **defined again**, with the
same words and the same cross-reference, at line 3012 (`thm:J`). Checked the other candidates the
brief names: **`A_∞` is defined once** (2370), **`Π_T` once** (2374, re-described but not redefined
in `prop:shifts`), **`P_T` once** (§1.1, line 124), **`𝒲_T`/`W_T^reg` once** (`def:W`). So `Γ_T` is
the only genuine duplicate. **Edit:** delete the redefinition at 3012, keep the `\ref{prop:nodes}`.

### Finding 15 — MAJOR (exposition). Notation collisions

- **`D` has seven meanings**: the dual programme value `D_T` and `D(U)` (`def:PD`, `thm:D1`); the
  function `D = σ_T + ν̂ + Σβ_jĥ_j − λ^P` in `thm:O`'s proof (line 577); the positive denominator
  `D(u) = 2cosh(u/2) − ½K(u)` (`thm:Zexh`, 1212); the target rate `D(T,d,U)` (`prob:A`); the tail
  constants `D(w), D_c(w), D_K(w)` (`thm:Dtail`); the Dirichlet-mode spans `D_k` (`thm:J`); the form
  domain `D(W)` (`prop:schur`(iii)). **Edit:** rename at least the `thm:O` function (→ `Δ` or `ρ`)
  and `thm:Zexh`'s denominator (→ `d_∗(u)`); `Δ` is itself taken by `thm:R`, so pick fresh symbols.
- **`B` has five meanings**: the Tate moment `B(F)` (§1.1); the depth `B = A_T − C₀` (`thm:Vp`,
  `thm:P3`); the `β`-box tolerance `B` (`thm:N`, `thm:Np`); the Möbius map `B(γ)` (`cor:Li`); and
  `B` as the generic bound in `thm:N` Step 1. The collision between `B(F)` and `B = A_T − C₀` is
  live on the same page in `thm:P3`. **Edit:** rename the depth to `𝔟` or `B_∗`.
- **`A`**: the operator `A_T`, the constant `A_T = 𝖠_T` (`\Aconst`), the Tate moment `A(F)`, the
  Toeplitz block `A` in `thm:finDet`, `A := Σ_k|c_k|p_k!` in `cor:T2`, `A = Σv_n` in `thm:SC`, and
  `A'` in `cor:T2`/`lem:W`. The macro `\Aconst = \mathsf A_T` does distinguish the constant
  typographically from `A_T`, which helps, but `A(F)` vs `A` vs `A'` inside `cor:T2` and `lem:W` is
  genuinely confusing.
- **`d`**: the lattice step `2T/M` (throughout §4–§8) and `d = |Z|` (`thm:finDet`, `thm:finZ`).
  Since `thm:finDet` also uses a lattice step (there called `a`), this is a live collision.
  **Edit:** `|Z| =: N_Z` or `κ`.
- **`P`**: the primal programme (P), the period `P = 2π/d`, the subspace `\PT = 𝒫_T`, the polynomial
  `P(z)` (`thm:finDet`), the Legendre polynomial `P_p` (the enclosure), `P_n` (`cor:Li`), `P(U)`
  (`thm:D1`), and the projection `P_V` (`prop:schur`).
- **`N`**: the contact set `𝒩_T`, the arena count `N*(T)`, the zero-counting function `N(t)`, the
  number of tail rows `N` (`lem:F1`), and the number of atoms `N` (`thm:D1`).
- **`E`**: `E_R` (`thm:P3`), `E_at` (`thm:Dtail`), the exceptional set `E` (`thm:finDet`), the
  subspaces `E_k` (`thm:nest`), the span `ℰ` of exponential columns (`thm:E`).

**On the two the brief specifically asks about:** `\PT` (= `𝒫_T`, the primitive subspace) and
`\PiT` (= `Π_T`, the prime form) are **already distinct macros and are used consistently** — I found
no place where the prime form is written `P_T`. Likewise `\Lev` (= `𝔈`, the Lévy energy) and
`𝔖(T)` (the KEP solution set, written out literally in `def:KEP`) **do not collide**. So two of the
brief's three suspected clashes are clean; the third (`N_T` vs `N*` vs `N(t)`) is real but mild.

### Finding 16 — MINOR. Constants: the audit

Checked every repeated constant. **Consistent:** `C₀ = −5.3721834…` (lines 91, 2301);
`τ₀ = 6.28983599…` (2984, 3013 — and I confirm `6.2898359888…`); `2τ₀/π = 4.004` (3043);
`2π/τ₀ = 0.9989426…` (3051); `tr M_- = 4.495774T` (3070 — I confirm `4.4957742`);
`T₀(0) = 0.74921` (2303, 2384, 2392); `𝖠_T = 0.98025814` at `½log3` (906) vs `0.98026` (2711) —
consistent rounding; `𝖠_T − C₀ = 7.621` (1054) / `7.62101` (1119); `c = 8.8577·10^{-5}` (85, 204,
919, 921) against the verification target `8.8578·10^{-5}` and binding minimum `8.85786·10^{-5}`
(934, 945) — correctly conservative; `9.893·10^{-4}` Galerkin at `½log3` (907, 2911); the `9%`
(1016) = `8.8577e-5/9.893e-4 = 8.95%` ✓; the `15%` (2052) = `8.8577e-5/5.9e-4 = 15.0%` ✓;
`cor:mono`'s `1.291` and `2.327` (I reproduce `1.291108`, `2.326752`) ✓; `68.51T` and `37/47/54`
(2991–2992) ✓; `cor:SC1`'s `−2.122831` ✓; `16.7` and `59.5` for `2πe^{𝖠_T}` (1103, 2346) ✓.
**Inconsistent:** `𝖠_T` at `log 2` — Finding 2; the `T = 0.58` certificate value — Finding 6;
`thm:nest`'s `E₁` eigenvalue — Finding 9.

---

## 6. LIST OF EXACT EDITS

Ordered by severity, with line numbers in the current `main.tex`.

**Must fix (FATAL/MAJOR):**

1. **L2930–2959** (`thm:AL`): restate. Either (a) replace the hypothesis "`w ≡ 1` on `[U,∞)`" by
   "`w ≡ 0` on `[U,∞)`" **and** define `G := ½(1−w)K` **and** extend the proof to the `2Ŵ` block and
   the prime atoms of `ν_w`; or (b) demote to a lemma about aliasing,
   "`|ν̂_lat(τ) − Ĝ_e(τ)| ≤ ε_r(M)` on `|τ| ≤ P/2`", and rewrite `cor:ALdef` accordingly. Also
   replace the vacuous parenthetical at L2952–2953 by "*the atoms with `|j| < M` are absent because
   `G_e ≡ 0` on the window*".
2. **L2709**: `2.24889` → `2.24883`.
3. **L1730–1735** (`cor:KEP08` proof): append "*For `T < ½log2`, apply the argument of
   Theorem~\ref{thm:KEP3}(b)(1)⇒(4): a certificate at `T' = ½log2` is one at `T`, and the
   perturbation of Theorem~\ref{thm:KEP1}(ii) applies with `χ` supported in `{|u| ≥ log2}`.*"
4. **L100–103** (abstract): "…*a property that holds unconditionally for `T ≤ 0.8`*" → "…*a
   property that holds unconditionally for `T ≤ 0.8`, by Zhu's certificate for the complete form
   \cite{Zhu2026}*".
5. **L2478–2480**: replace "*the primes are therefore necessary … every proof … must exhibit*" by
   the `T > 0.74921` / diagnostic-suggests formulation of Finding 11.
6. **L577, L1212** and passim: resolve the `D` collision (Finding 15); at minimum rename `thm:O`'s
   `D` and `thm:Zexh`'s `D(u)`.

**Should fix (MINOR):**

7. **L85–86, L200–201**: "the first window in which a prime is coupled" → "the largest window with
   a single contact".
8. **L218, L3111**: `−3.18·10^{-3}` → `−3.20·10^{-3}` (or `−3.1964`).
9. **L2173**: "three enclosures" → "four enclosures".
10. **L2486**: "a truth of `+9.8·10^{-4}`" → "a \textsc{diagnostic} upper bound `9.89·10^{-4}`".
11. **L2597**: `3.4212·10^{-2}` → `3.4211·10^{-2}` (or state that the list is of lower bounds).
12. **L1669**: `−∫_{|u|≥2T}χK cos` → `−½∫_ℝ χK cos` (equivalently `−∫_{2T}^∞`).
13. **L1386–1389** (`thm:finDet` Step 1): `a ∈ (0,2T/d]` → `a ∈ (0,2T/d)`; recover the endpoint in
    Step 5 by the continuity already written there.
14. **L1331–1333** (`cor:Li` proof): after "`θ(γ) = 2arg(γ+i/2)`" add "*for `γ > 0`; the case
    `γ < 0` follows by evenness*".
15. **L2386–2392** (`prop:arch`(iii)–(iv)): cite strict positivity from `\cite{Yoshida1992}` or
    weaken (iv) to the upper bounds only.
16. **L3012**: delete the redefinition of `Γ_T`; keep `(Proposition~\ref{prop:nodes})`.
17. **L3120–3174** (§9 table): add a row for `rem:RHcert` labelled \textsc{heuristic}.
18. **L2564, L2625**: "the endpoint of record" → "the endpoint of record for the methods of this
    paper".
19. **L1293**: "the whole family of strategies … is empty" → "…the whole family of strategies
    *choose a flat-top `w` with `ŵ ≥ 0`* is empty".
20. **L86, L93–96** (abstract): `λ_min` → `λ_min(A_T|P_T)`; "nested seven-dimensional even
    subspaces" → "a nested tower of even subspaces up to dimension seven"; "restores exactly" →
    "restores to within `1.3·10^{-3}`".
21. **L2550–2553** (`thm:w11` proof (c)): add that `T < arccosh√2 = 0.88137` is what licenses the
    affine sandwich, so the method as written does **not** extend past `T = 0.88137` — currently the
    reader is left to notice this.
22. **L3203–3204**: reconcile `Coffey2004` key with the 2005 volume year. **L3209, L3242**: the
    arXiv identifiers `2607.02828` and `2608.24827` cannot be resolved by a referee (R1 Finding 18,
    unchanged).

**Restructuring:** §4 above; the highest-value single move is Appendix C (the `\textsc{diagnostic}`
record), which would shorten §8 by ~4 pp. and let the §9 label table shrink by a third.

---

## 7. WHAT IS CORRECT, AND WHAT THE ADDITIONS OF 2026-09-21/22 ADD

For the record, since an adversarial report reads as uniformly negative. The new material is the
strongest in the paper. `thm:finDet` is a genuinely clean theorem with a new proof idea (the
variable lattice step in Step 5) and no decay or product hypothesis; `thm:finZ` now follows from it
in four lines instead of the old five-step argument, and the pair (`thm:finZ` supplies the sign with
no fine print, `rem:loc` supplies the location under fine print, "neither statement contains the
other") is exactly the right way to present it. `thm:Dtail`'s regrouping with `2ĝ₀`, and the
explanation of *why* it is forced by the jump of `ν_w` at the window edge, is a real improvement on
`lem:T`. `cor:Li` finally pins down in what sense the Li coefficients are the termwise strategy, and
the "zero-sum half only" sharpening is correct and, as far as I know, not in the literature in this
form. `thm:arena`/`cor:arena` turn the informal "Galerkin doesn't converge" into a proved
doubly-exponential mode count, and the `E₇`-inside-an-arena-of-12 reading is the right one.
`prop:NC` and `thm:J` bracket `n_-` from both sides with matching asymptotics and honest sourcing of
the cited half. And the machine-verification hygiene in `thm:w11`/`thm:nest`/`thm:Np` — the declared
`P_T` defect, the polarisation-not-cross-correlation rule, the GL node guard with its disclosed
earlier failure — is better than what one usually sees in certified-computation papers.

None of that is in question. What is in question is `thm:AL`, one constant, one range in
`cor:KEP08`, two modal verbs, and 19 pages of structure.


---

## Changes since R1 (revision applied )

All 16 findings and all 22 exact edits of this report are applied in `main.tex`; the backup of the
reviewed file is `main_pre_R2.tex.bak`.

1. **Finding 1 (FATAL).** `thm:AL`/`cor:ALdef` as printed are **retracted**; `subsec:lat` is
   rewritten around the corrected theorem (comb-vanishing `w`, true density
   `G = ½(1−w)K + 2w cosh(u/2)`, end-point-corrected sampling with `κ_{±M} = ½`, signed measure with
   countably many atoms and finite TV, `β = (2,0)`). The cost is an **edge** effect,
   `E_edge = (4/π)cosh T·d + O(d²)`, sharp; the smooth blocks cost `O_r(M^{−r})`. The plain
   (uncorrected) sampling constant is `cosh T√(4+16/π²) = 2.37 cosh T`. "The lattice is never the
   deficit" is withdrawn; the optimised lattice class is open. The `prop:TK` sentence is kept as an
   explicit *reading*, since `f_lat − f_w` is not a trigonometric polynomial; and the edge rate is
   explicitly **not** compared with the archimedean `0.28 M^{−1.17}` deficit, which lives in the
   programme without a polar block. Table row rewritten.
2. **Finding 2.** `2.24889 → 2.24883`. 3. **Finding 3.** `cor:KEP08` now covers `T < ½log2` by the
   small-`T` device of `thm:KEP3`(b). 4. **Finding 4.** Abstract attributes the unconditional half to
   Zhu. 5–13, 16. All applied as specified (single-contact window, `−3.20·10⁻³`, four enclosures,
   Galerkin bound not "a truth", `3.4211·10^{-2}`, `rem:RHcert` row added, "for the methods of this
   paper", flat-top qualifier, `½∫_ℝ χK`, open lattice interval, `arg` branch, `prop:arch`(iv)
   weakened, `Γ_T` defined once, `Coffey2005` key aligned with the volume year).
14–15. **Notation.** `thm:O`'s function is `ϱ`, `thm:Zexh`'s denominator `d_*(u)`, the depth is
   `B_*`, the cardinality of a finite zero set is `ℓ`; a notation paragraph in §1.5 fixes each
   symbol once.
21. The `arccosh√2 = 0.88137` limitation of the affine sandwich is now stated in the proof.
**Restructure (§4 of the report).** §8 → three sections (class impossibilities; the archimedean form:
structure and index; what a closing argument must do), plus Appendix A (enclosure methods),
Appendix B (the Li/NB dictionary) and Appendix C (the diagnostic record, with the diagnostic rows of
the label table). All `\label`s preserved.
**Audited additions.** A Ky Fan ceiling for the time–band limiting operator (Legendre diagonal,
`Σ_j R_j = tr S_c`), its quadrature-free corollary, and the resulting `n₋(A_∞|P_T) ≤ 5, 7, 8` at
`½log3, log 2, 0.80` — replacing the trace values `37, 47, 54` as the quoted counts, with the grid
values `5, 6, 7` kept only as DIAGNOSTIC — together with the two-sided brackets obtained with
`thm:J` and a remark on the floor of the two-value relaxation.

Result: 57 pp. (50 core, 5 appendices, 2 references), 0 errors, no undefined or multiply-defined
references.
