# R155.007 — Hostile audit of round 2 (`R155_004`), phase 155

*Auditor: Opus 5 (1M). 2026-09-21. Scope: `R155_004_BUILDER_ROUND2.md`, `scripts/tk_common.py`,
`scripts/r2_{a_enclosure,b_ceiling_twoprime,c_beta_bound,d_subcomb,e_rate}.py`, and the 22
`[amended 2026-09-21 per R155_002]` marks in `R155_001` against the ten repairs of `R155_003 §2`.
Read for context: `R155_000`, `R155_002`, `R155_003`, Paper 47 `main.tex` §§2,3,5,8.
Reproductions run single-process with `OMP_NUM_THREADS=1`; the `M = 64/96/128` block of (b) was not
re-run, per the orders.*

## §0. Verdict table

| item | statement | verdict |
|---|---|---|
| (a) | **Theorem N** (`Ceil(8,½log3) ≤ −5.6974·10⁻³`, β-uniform) | **PROVED WITH REPAIRS** (one scope error, R-1) |
| (a) | Lemma 2.2, the derivative/Simpson bounds, `C₀` identity, `∫φ = P‖q‖²` | **PROVED**, all re-derived |
| (b) | `Ceil(M,0.58)` table, cap `2.00·10⁻⁴`, E1 verdict | **DIAGNOSTIC**, sound in direction, values not converged (R-3) |
| (b) | `Ceil(24,0.68) < 0`, `Ceil(24,log2) < 0` | **DIAGNOSTIC**; sign robust, the quoted 7-figure values are wrong by ~33× (R-3) |
| (b) | `Ceil(64,0.68) > 0`, `Ceil(64,log2) > 0` ("the sweep must start at M ≥ 64") | **UNSUPPORTED** at the precision claimed (R-4) |
| (b) | "at every two-prime window and every `M`, `Ceil` at `β=(2,0)` is `≈10⁻⁹–10⁻¹⁰`" | **WRONG** (R-5) |
| (c) | **Theorem B** `‖β‖₂ ≤ (V⋆−c)/r₀`, Lemma 4.2, witness family, sliver | **PROVED** (constants machine-verified, not enclosed; harmless, R-2) |
| (d) | **Theorem SC**, `T₀(A)` table, **Cor. SC1** (`−2.122831`) | **PROVED**; two cosmetic slips (R-6, R-7) |
| (e) | **Lemma R1**, **Theorem R**, **Cor. R2**, **Cor. R3** | **PROVED** (R2 carries a stated hypothesis; §6.3 mis-cites it, R-8) |
| (e) | `p = 1.2505` fit, `L = 9.82·10⁻⁴` | **DIAGNOSTIC**, correctly not asserted |
| — | the 22 amendments vs the ten repairs of `R155_003 §2` | 10/10 applied; **two residues** (R-9) and one partial (R-10) |
| (f) | replace `main.tex:1271–1273` parenthesis by Theorem N | **YES, after R-1 and R-2**; ≈1 page, not half |

No FATAL. Nothing in the round touches the zeros of `ζ`; no sign is claimed for `T > log2`; the
endpoint of record is untouched.

---

## §1. (a) Theorem N

### 1.1 The logical chain, checked

* `Ceil(M,T) = sup_β inf_{τ₀} λ_min(C_M) ≥ c` for every lattice certificate: this is `prop:TK`
  (`main.tex:1237–1262`), whose proof I re-derived. `ν̂ = Σ_{j≥M}2a_j cos(jdτ)` is `P`-periodic with
  modes `|j| ≥ M`; `φ = |q(e^{idτ})|²` has modes `|j| ≤ M−1`; `∫_W ν̂φ = 0` exactly. The bound is
  therefore independent of the atom count, of the range `U`, of the signs `a_j`, and of which tail
  lemma verified `f ≥ c` — the tail lemmas (`lem:F1`, `lem:T`, `lem:hybrid`) only *verify* the
  pointwise inequality and add no atoms off the lattice (blueprint §1 definition of `L(T,d,U)`).
  **Scope is as claimed, with one exception: R-1 below.**
* The "one pair `(τ₀,q)` suffices" step is **valid for every `β`**, not only near the maximiser:
  §2.2 Step 2 is `prop:TK` at a single `(τ₀,φ)`, giving `c ≤ a + b·β` as an identity-free inequality
  for all `β ∈ ℝ²`. The smallness of `b` (`10⁻⁹`) is what makes the a priori box usable; it is not a
  hypothesis. The only `β`-dependence is via Theorem B, which needs `c ≥ 0` — exactly the hypothesis
  of the contradiction. Chain is sound.
* Normalisation of `β`: `r2_c_beta_bound.py` bounds the `β` of `Def. 3.1`
  (`f = σ_T + ν̂ + β₀ĝ₀ + β₁ĝ₁`), the same normalisation in which `β = (2,0)` is the known
  Weil/polar point (`prop:P`). `ĝ₀ = 2∫₀^{2T}cosh(u/2)cos τu`, `ĝ₁ = 2∫₀^{2T}u sinh(u/2)cos τu`
  agree with `lem:gbounds` (`main.tex:436`) and with `r2_a_enclosure.py:96–105`. **Consistent.**

### 1.2 The enclosure, checked line by line

All verified correct:
`C₀ = ψ(¼) − logπ = −γ − π/2 − 3log2 − logπ` (Gauss digamma; `r2_a_enclosure.py:75`);
`m(τ) = C₀ + Σ_k τ²/(a_k(τ²+4a_k²))`, `a_k = k+¼` (from `ψ(¼+iτ/2) − ψ(¼)`, real part);
Lemma 2.2 — `t(a) = τ²/(τ²a+4a³)` is positive, decreasing, convex (`2u′² − u″u = 2τ⁴+24τ²a²+192a⁴ > 0`),
midpoint sum under-estimates `∫_A^∞ t = ½log(1+τ²/4A²)`, deficit `≤ (1/24)∫|t″| = (1/24)|t′(A)| = E`,
and `E` matches `t′` exactly (`r2_a_enclosure.py:90`);
`|m^{(j)}| ≤ 2^{−j}j!ζ(j+1,¼)` (from `|z+n| ≥ ¼+n`), and `zeta_hurwitz_quarter_ub(p) = 4^p + ζ(p)`
is a genuine upper bound for `ζ(p,¼)`;
`|ĝ₀^{(j)}| ≤ 2cosh T(2T)^{j+1}/(j+1)`, `|ĝ₁^{(j)}| ≤ 2sinh T(2T)^{j+2}/(j+2)` (Bernstein-type,
elementary);
`|φ^{(j)}| ≤ (d(M−1))^j Σ_l|γ_l| ≤ (d(M−1))^j(Σ|q_k|)²`;
composite-Simpson remainder `Ph⁴C₄/180` with `C₄(Xφ) = Σ_j C(4,j)sup|X^{(4−j)}|sup|φ^{(j)}|`;
`∫_Wφ = P‖q‖²` exactly (orthogonality over a full period) — used as the denominator, so no
quadrature error enters it. The FFT-Simpson wrap of `tk_common.py:84–87` (folding node `n` into node
`0` because `e^{ild x_n} = e^{ild x_0}`) is correct.

**Reproduction.** `python3 r2_a_enclosure.py 8` → **bit-identical** to the archived JSON
(`a ∈ [−6.009422180·10⁻³, −6.006217874·10⁻³]`, `b₀ ∈ [3.4384, 3.7002]·10⁻⁹`,
`b₁ ∈ [2.3752, 2.4768]·10⁻⁹`, bound `−5.6973679·10⁻³`), **27.5 s** on this machine (claimed 42.5 s).

**Independent cross-check** (adaptive `scipy.integrate.quad`, `scipy.special.digamma`, no interval
arithmetic): `a = −6.0078359·10⁻³`, `b₀ = 3.5693·10⁻⁹`, `b₁ = 2.4260·10⁻⁹` — all three inside the
archived enclosures, and the resulting bound `−5.708·10⁻³ < 0`. The interval widths match the
declared Simpson remainders to the digit (`2·7.26·10⁻⁵/45.75 = 3.2·10⁻⁶` for `a`). **Theorem N's
M = 8 case is confirmed by an independent route.**

Archived `M = 3,5,6,7` JSONs reproduce Table 2.1, except: **the `|b₀|+|b₁|` entry for `M = 6` reads
`2.43·10⁻⁹` in the table (`R155_004:123`) against `2.34·10⁻⁹` in
`scripts/r2_a_enclosure_M6.json` — a digit transposition; the `c ≤` column is unaffected.**

**Sublattice inclusion (`M = 1,2,4`).** Correct: for `M | 8`, `{±j·2T/M : j ≥ M} ⊂ {±j·T/4 : j ≥ 8}`
(all multiples of `2T/M` that are `≥ 2T` are multiples of `2T/8` that are `≥ 2T`). `M = 3,5,6,7` are
*not* sublattices of `M = 8` and are correctly certified separately.

### 1.3 Errors

**R-1 (MAJOR, scope). `R155_004:18, :81–82, :501`, `README.md:17`, and — pre-existing —
`main.tex:1270–1271`.** The phrase *"no lattice certificate of step `≥ 2T/8`"* is false as literally
written: the enclosures cover `d = 2T/M` for `M ∈ {1,…,8}`, i.e. eight specific steps, not the
continuum `d ≥ T/4`. §2.4 bullet 4 concedes exactly this (`2T/d ∉ ℕ` not covered) and thereby
contradicts §2.1's "Consequently". Required wording: *"no lattice certificate of step `2T/M` with
`M ≤ 8`"*. This must be fixed before Theorem N enters the paper, and the same repair applies to the
paper's own `DIAGNOSTIC` sentence at `main.tex:1270`.

**R-2 (MINOR, disclosed).** Theorem N is `PROVED (machine-verified)` but depends on a constant
(`B = 5·10⁴`) taken from Theorem B, whose `r₀`, `V⋆` are 30-digit floating point, **not** interval
enclosed, and whose polygon inradius comes from a double-precision `ConvexHull`. The headroom is
large — the bound stays negative for any `B < 6.006·10⁻³/6.18·10⁻⁹ = 9.7·10⁵`, i.e. a factor **21**
above `45169.4` — so the conclusion is safe; but the paper text should state the tolerance
explicitly (e.g. "any `B ≤ 9·10⁵` suffices") rather than the sharp constant.

---

## §2. (b) The two-prime windows

Reproduced exactly (`r2_b_ceiling_twoprime.py 2b`, 62 s): `T = 0.68`, `M = 24`: `−2.279475·10⁻⁷`;
`M = 64`: `+1.949203·10⁻⁷`; `T = log2`, `M = 24`: `−6.820822·10⁻⁷`; `M = 64`: `+5.820239·10⁻⁸`.
Archived logs `b_1a.log`, `b_2a.log` match the tables of §3.

**R-3 (MAJOR, numerical). The `τ₀` grid is not converged where the values are near zero.**
`Ceil` is computed as `sup_β min over a 61-point τ₀ grid`; a grid *over*-estimates `inf_{τ₀}`, so the
reported number is an upper estimate. Refining at `T = 0.68, M = 24` (121 nodes, `nfft = 2¹⁷`, six
NM starts) gives **`−7.512·10⁻⁶`** against the archived `−2.279475·10⁻⁷`: a factor **33**. The sign
is therefore robust (refinement only lowers it), but the seven significant figures in §3 Run 2 are
spurious. At `T = 0.58, M = 24` the same refinement (241 nodes) moves `9.673945·10⁻⁵ → 9.435·10⁻⁵`
(2.5 %), so Run 1 and the cap are stable to two figures. *Required:* quote Run 2 to one significant
figure at most, or as "`< 0`".

**R-4 (MAJOR). `R155_004:245–251`, `README.md:17`: "at `M = 64` the ceiling turns positive … the
sweep must start at `M ≥ 64`".** `Ceil(64,0.68) = +1.95·10⁻⁷` and `Ceil(64,log2) = +5.82·10⁻⁸` are
*upper* estimates of the same kind that moved by 33× at `M = 24`, and they are smaller than that
drift. I could not refine them inside the runtime budget (the 121-node `M = 64` job exceeded 570 s
and was aborted — the machine cannot carry it in one process). Until refined, the positivity of
`Ceil(64, ·)` is **unsupported**, and with it the conclusion "the sweep must start at `M ≥ 64`". The
honest statement is: `M = 24` is dead at `T ≥ 0.68`; whether `M = 64` is alive there is open.

**R-5 (MAJOR, factual). `R155_004:238–243` reading 3:** *"At every two-prime window and every `M` in
the tables, `Ceil` evaluated at `β = (2,0)` is `≈10⁻⁹–10⁻¹⁰`, five orders of magnitude below the
maximum."* The archived logs contradict this: `T = 0.65, M = 24`: `−8.23·10⁻⁹`; `T = 0.68, M = 24`:
`−3.55·10⁻⁷`; `T = log2, M = 24`: `−1.90·10⁻⁶`; `T = 0.68, M = 64`: `+1.18·10⁻¹²`;
`T = log2, M = 64`: `+3.27·10⁻¹³`. The spread is `10⁻¹³` to `−2·10⁻⁶`, includes **negative** values,
and the "five orders below the maximum" holds only at `T = 0.58`. Recommendation 3 of §8 (run E1
with `β₀ ∈ [2.0002,2.0006]`) rests on the `T = 0.58` row only and should say so.

**Are these "the first proved negatives at a two-prime window"?** No — §3 is explicitly
`DIAGNOSTIC`, and §7 labels it so; but §3.1 reading 4 writes "**provably cannot** carry the last two
steps" in the same paragraph that declares the numbers `DIAGNOSTIC`. Contradictory wording; delete
"provably". The enclosures suggested in §8.6 remain the right next step, but per R-3 the true margin
at `M = 24` is `~10⁻⁵`, not `2.3·10⁻⁷` — *easier*, not harder, than the builder estimates.

---

## §3. (c) Theorem B

Proof checked and correct. Each step verified: `μ_F = |F̂|²dτ/2π` is an even probability measure
with `μ̌_F = c_F` supported in `[−2T,2T]` and `c_F(±2T) = 0`, so `∫ν̂dμ_F = ∫c_F dν = 0` for every
certificate measure (this is `prop:weak`'s own argument, `main.tex:433`, atoms at `±2T` harmless —
relevant, since `j = M` puts an atom exactly at `2T`); `∫ĝ_jdμ_F = Q_j(F)`; `∫σ_Tdμ_F = 𝔞_T(F)`;
the relaxed feasible set (moment constraints **dropped**) is convex and both functionals affine, so
mixtures realise `conv{w_i}` with value `≤ max_i V_i`; `β·w ≥ c − V⋆` on `{|w| ≤ r₀}`, applied to
`±w`, gives `r₀‖β‖₂ ≤ V⋆ − c`. The disc/polygon step is legitimate (`hull.equations` are unit
normals; origin verified interior).

Lemma 4.2 checked: `1 − Re c_F(u) = (2π)^{−1}∫(1−cos τu)|F̂|² ≤ min(2, u²‖F′‖²/2)` (the second from
`1−cos x ≤ x²/2`, the first from `|c_F| ≤ 1`); split at `u₀`; derivative `K(u₀)[L²u₀²/2 − 2]`
vanishes and changes sign at `u₀ = 2/L`, so it is the minimiser. `∫_{u₀}^∞K = log coth(u₀/2) + π −
2arctan e^{u₀}` matches `thm:S`(iii). Witnesses `(T²−t²)t^k ∈ H¹₀(I_T)` ✓; `Q₀ = AB`,
`Q₁ = A′B − AB′` matches `main.tex:368–371`.

**Reproduction** (`r2_c_beta_bound.py`, 1.2 s): `½log3`: `r₀ = 8.451501·10⁻⁵`, `V⋆ = 3.817495`,
`B = 45169.4`, zero interior `True`; `0.58`: `r₀ = 1.106642·10⁻⁴`, `V⋆ = 4.949601`, `B = 44726.3`.
`A_T` values check by hand (`√2log2 = 0.98025814`; `+2log3/√3 = 2.24882634`).

**Sliver.** `cosh(u/2) − ¼u sinh(u/2) = 1 − u⁴/384 + O(u⁶)` — the expansion is right, so
`Q₀ − ¼Q₁ = |∫F|² + O(T⁵)‖F‖²`, a genuine **one-sided** constraint on the whole moment image;
consequently `r₀ = O(T⁴)` holds for *any* witness family, which is what licenses "`B = O(T^{−4})` is
structural". The computed minimal-support direction is `166.19°` (I recomputed from the archived
moment polygon) against the predicted `165.96°`; §4.4's "`166.0°`" is a rounding of the former.
`DIAGNOSTIC`, as labelled. §8.2's suggestion (one-sided bound on `β₀ − 4β₁`) follows.

---

## §4. (d) Theorem SC

**Is it exactly `cor:mono`?** Yes. `cor:mono` (`main.tex:384–401`) is proved from
`λ_n(Lev) ≤ φ((nπ/2T)²)` (Song–Vondraček Prop. 2.3), `codim P_T = 2`, and
`−Σv_n c_F(log n) ≤ A_T‖F‖²`. **The last step uses only `v_n ≥ 0` and `|c_F| ≤ ‖F‖²` — nothing about
the true `v_n = 2Λ(n)/√n`** — and `main.tex:406` states outright that "any nonnegative weights may
be used". Theorem SC is therefore `cor:mono` read for arbitrary non-negative weights of mass `A`,
plus the monotonicity and limits of `φ` (immediate from the series `φ(x) = Σ x/(a_k(x+4a_k²))`).
**PROVED.**

**Reproduction** (`r2_d_subcomb.py`, 0.27 s): `A = 0.563667`, `φ((3π/2T)²) = 2.685686` at
`T = 6.869974`, `λ ≤ −2.122831` ✓; `T₀` table reproduces (`0.74921, 0.96134, 1.23295, 1.31350,
2.01848, 4.63567, 13.19461, 29.60905, 69.89558`) ✓; first-ten-primes window `T = ½log31`,
contacts `{2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29}`, `A_T = 16.640459`, Cor. 2.6 bound `+15.805966`
(vacuous, correctly so), `2πe^{A_T} = 1.0593·10⁸` ✓.

**R-6 (MINOR). `R155_004:373`:** `T₀(0.563667) = 1.313456`, not `1.31350…`; the table entry
`1.31350` is `T₀(0.5637)` (the rounded mass). Harmless, but the two numbers are printed as the same.

**R-7 (MINOR). `R155_004:391`:** "the window whose contact set is *exactly* the first ten primes" —
its contact set is the sixteen prime powers below 31, as the next sentence itself says. Reword.

The §5.2 reading ("positivity is collective; it cannot be assembled prime by prime") is the
contrapositive of SC and is correctly *not* a statement about `ζ`: `λ_min(A_T(v)|_{P_T}) ≤ −2.12`
is about the operator with those ten weights, and the full comb is untouched. FATAL rule respected.

---

## §5. (e) Lemma R1, Theorem R

**Lemma R1.** Fourier claim checked: `ρ̂(j) = ∫_W e^{−ijdτ}dρ = ∫_ℝ e^{−ijdτ}dμ = μ̌(jd)` (valid
because `e^{−ijd(τ+kP)} = e^{−ijdτ}`, `dP = 2π`), and `|jd| ≥ 2T ⟺ |j| ≥ M`, so `ρ̂(j) = 0` for
`|j| ≥ M` — **the stated direction is right**, and the boundary case `j = M` (`u = 2T` exactly) is
covered because `(P)`-feasibility is the closed condition `μ̌ = 0` on `{|u| ≥ 2T}`. Finitely many
non-zero coefficients ⇒ `ρ` is a trigonometric polynomial measure, non-negative, hence `|q|²` by
Fejér–Riesz. **PROVED.** (The parenthetical restatement of "(P)-feasible" at `R155_004:407` omits
the two moment conditions, which Theorem R then uses; add them.)

**Theorem R.** `Ceil(M,T;β) ≤ ∫_W S_β dρ = ∫_ℝ S_β(π_Wτ)dμ` ✓ (inf over `(τ₀,φ)` is at most the
value at `τ₀ = −P/2` and `φ = Pρ`). `∫S_βdμ = ∫σ_Tdμ` **needs** `∫ĝ_jdμ = 0`, which is part of
`def:PD`(P) ✓. `sup_WS_β ≤ m(P/2)+A_T+Σ|β_j|ĝ_j(0)` (`m` increasing, `|ĝ_j| ≤ ĝ_j(0)`),
`inf_ℝS_β ≥ C₀−A_T−Σ|β_j|ĝ_j(0)`, so `Δ = m(P/2)−C₀+2A_T+2Σ|β_j|ĝ_j(0)` ✓ matches the displayed
formula. Limit: `∫σ_Tdμ < ∞` and `σ_T ≥ m − A_T` give `∫m dμ < ∞`; then
`(m(R)−C₀)μ(|τ|>R) ≤ ∫_{|τ|>R}(m−C₀)dμ → 0` by dominated convergence — the "finite value"
hypothesis is used correctly and is available because one takes `μ` with `∫σ_Tdμ ≤ λ^P+δ`.
**PROVED.**

**Cor. R2.** `Δ` bounded on the box ⇒ `limsup Ceil_B ≤ λ^P` ✓. The converse half uses Theorem B
correctly: `c(M) ≤ Ceil_B(M)` needs the certificate's `β` inside the box, which Theorem B supplies
**only for `c ≥ 0`** — hence the explicit hypothesis `λ^P > 0` and "eventually" in `c(M) ↑ λ^P`. The
hypothesis is stated; the "eventually" is not, and should be. **PROVED as stated.**

**Cor. R3 vs MAJOR-4.** MAJOR-4 asked for the `|q|²`-window family not to be claimed non-lossy. R3
claims exactly the `M → ∞` half and leaves the fixed-`M` question `OPEN`, which is the correct
resolution of MAJOR-4's repair. ✓ No overreach.

**R-8 (MINOR). `R155_004:487–490`:** "By Theorem R and Cor. R2 the limit **is** `λ^P(½log3)`". The
measured `Ceil(M)` of §6.3 is the *unrestricted* `sup_β`, whereas Theorem R/R2 control `Ceil_B` on a
box (`Δ(M,β)` is unbounded in `β`). The argmax `β` in the table stays at `(2.00,−0.02)`, well inside
the box, so the reading survives; but the sentence should read "`Ceil_B`".

**The fit.** `p = 1.2505`, `L = 9.820487·10⁻⁴`, residual `7.6·10⁻⁶`, on seven points and three
parameters, from a 41-node `τ₀` grid — `DIAGNOSTIC`, and the builder does label it so, explicitly
declines to assert `λ^P = λ^A`, and keeps reading 5 withdrawn. **Confirmed: not asserted.** Given
R-3, the residuals are of the same order as the grid drift, so even "rules out `O(M^{−2})`" is
weaker than written; keep it as an impression, not a discrimination.

---

## §6. The 22 amendments vs the ten repairs of `R155_003 §2`

All ten repairs are present: (1) `R155_001:64` (notation) + `:80` + `:417`; (2) `:32`, `:344`,
`:388`; (3) `:145` (caveat (iv), verbatim from `114_d_174`); (4) `:291`, `:420`; (5) `:312`;
(6) `:338`, `:356`, `:424`; (7) `:49`; (8) `scripts/tk_ceiling_sweep_M.py:1`; (9) `:90`; (10) `:159`.

**R-9 (MAJOR, residue of repair (6)). The superseded figure survives in two summaries:
`R155_001_BUILDER_ROUND1.md:29` ("already captures **21 %** of everything its own class can ever
give") and `README.md:11` ("the 437-atom certificate is **21 %** of its own class").** The corrected
value is **15 %** (`8.8577·10⁻⁵/5.9224·10⁻⁴`), as `R155_001:338` and `R155_003 §1` record. Two files
now state both numbers. Fix both.

**R-10 (MINOR, partial repair (5)).** The lead asked for the §4.5 table to be recomputed as
`inf_{τ₀}` on a fine scan; the builder kept the four-placement table and annotated it
(`R155_001:312–316`) with the corrected `M = 8, 12` entries in prose. Every entry remains a valid
ceiling (the inequality holds per `τ₀`), so this is sound but not what was ordered; the table's
numbers are not the `Ceil` of the labels of record.

Repair (1) deserves a note: the lead's §2(1) said "`λ^prim := λ^P` throughout §2–3", while the
audit's MAJOR-1 required §2–3 to be restated for `λ^A` (which is what `μ⋆ = |F̂⋆|²dτ/2π` actually
computes) *and* for `λ^P`. The builder did the former and added one sentence for the latter,
asserting the existence of a `(P)`-minimiser from the tightness argument of `thm:D1(iii)` without
proving it. That is the mathematically honest reading of the two instructions, but the
`λ^P` restatement of Theorem 3.3 is still owed, and Problem A's deficit is `λ^P − c`.

---

## §7. (f) Paper-readiness

**Recommendation §8.1 is sound, with conditions.** `main.tex:1270–1273` currently reads: *"No lattice
certificate of step `≥2T/8` can prove positivity at `½log3`, for any `β`, range or tail lemma (an
interval enclosure of `Ceil(8)<0` would make this the first proved negative class statement of the
programme; the margin is `5·10⁻³`)."* Theorem N does discharge the parenthesis, and it is
self-contained given `prop:TK`. Conditions:

1. **R-1 must be applied to the theorem *and* to the surrounding sentence** — "step `2T/M`,
   `M ≤ 8`", with the `2T/d ∉ ℕ` scope limit of §2.4 recorded in a footnote.
2. **Theorem B must go in with it** (it is the only reason the bound is `β`-uniform), together with
   Lemma 4.2 and the witness family. State the tolerance (`any B ≤ 9·10⁵`), not the sharp `45169.4`,
   so the theorem does not depend on a non-enclosed constant (R-2).
3. **Length:** Theorem B + Lemma 4.2 + witnesses + the single-test-kernel corollary of `prop:TK` +
   the enclosure table + the reproduction paragraph is **≈1 page**, not half.
4. Nothing from §3 (two-prime ceilings) should enter the paper as more than `DIAGNOSTIC` to one
   significant figure, and the `M = 64` claims not at all until R-4 is resolved.

## §8. Surviving theorems and proposed labels

| id | statement | proposed label | paper-ready? |
|---|---|---|---|
| **Theorem N** | for `T = ½log3`, `M ∈ {1,…,8}`, `d = 2T/M`: every `ν` on `{±jd : j ≥ M}` and every `β ∈ ℝ²` have `inf_ℝ(σ_T+ν̂+β·ĝ) < 0` | **PROVED (machine-verified)** after R-1, R-2 | **yes**, ≈1 p, §8 of Paper 47 |
| Lemma 2.2 + the four derivative bounds | convex-midpoint bracket for the `ψ`-tail; `|m^{(j)}|,|ĝ_j^{(i)}|,|φ^{(j)}|` | **PROVED** | yes, as a reproduction appendix |
| **Theorem B** | `‖β‖₂ ≤ (V⋆−c)/r₀` for every certificate of value `c` | **PROVED** (constants machine-verified, not enclosed) | yes |
| Lemma 4.2 | `𝔞_T(F) ≤ C₀+A_T+(L²/2)∫₀^{2/L}u²K+2∫_{2/L}^∞K` | **PROVED** | yes |
| §4.4 sliver | `g₀−¼g₁ = 1+O(u⁴)`; `r₀ = O(T⁴)` for *any* witness family; `B = O(T^{−4})` | **PROVED** (the `166.19°` direction `DIAGNOSTIC`) | as a remark |
| **Theorem SC** + **Cor. SC1** | non-negative weights of mass `A < −C₀` ⇒ negative form for `T ≥ T₀(A)`; ten primes `< 10⁶` give `λ ≤ −2.122831` | **PROVED** after R-6, R-7 | yes — the cleanest new statement of the round |
| **Lemma R1** | the `P`-periodisation of a `(P)`-feasible `μ` is a test kernel of order `M` | **PROVED** | yes |
| **Theorem R** / **Cor. R2** / **Cor. R3** | `Ceil(M,T;β) ≤ ∫σ_Tdμ + Δ·μ(|τ|>P/2)`; `Ceil_B → λ^P`; the test-kernel family is not lossy in the limit | **PROVED** (R2 under `λ^P>0`, eventually) | yes — closes the `M→∞` half of MAJOR-4 |
| `Ceil(M,0.58)` table; cap `2.00·10⁻⁴`; "E1 not refuted" | — | **DIAGNOSTIC** (two figures only) | no |
| `Ceil(24,0.68)<0`, `Ceil(24,log2)<0` | — | **DIAGNOSTIC**, sign only (R-3) | no |
| `Ceil(64,0.68)>0`, `Ceil(64,log2)>0` | — | **UNSUPPORTED** (R-4) | no |
| Conjecture R4 / the `p = 1.2505` fit | — | **CONDITIONAL / DIAGNOSTIC**, correctly not asserted | no |
| "is the test-kernel family lossy at fixed `M`?" | — | **OPEN** | — |
| Problem A | `c ≥ λ^P − D(T,d,U)` | **OPEN**, untouched | — |

## §9. Reproductions run

| command | result | time |
|---|---|---|
| `python3 r2_a_enclosure.py 8` | bit-identical to `r2_a_enclosure_M8.json`, bound `−5.6973679·10⁻³` | 27.5 s |
| independent `quad`/`digamma` recomputation of `a,b₀,b₁` at `M=8` | `−6.0078359·10⁻³`, `3.5693·10⁻⁹`, `2.4260·10⁻⁹` — all inside the enclosures | 3 s |
| `python3 r2_c_beta_bound.py` | `r₀`, `V⋆`, `B` reproduce at both windows; `0` interior `True` | 1.2 s |
| `python3 r2_d_subcomb.py` | every number of §5 reproduces to the printed digits | 0.3 s |
| `python3 r2_b_ceiling_twoprime.py 2b` | reproduces `b_2b.log` exactly | 62 s |
| `T=0.68, M=24`, `ntau=121`, `nfft=2¹⁷`, 6 NM starts | `Ceil = −7.512·10⁻⁶` (archived `−2.279·10⁻⁷`) → **R-3** | 320 s |
| `T=0.58, M=24`, `ntau=241` | `Ceil = +9.435·10⁻⁵` (archived `+9.674·10⁻⁵`) — stable | 300 s |
| `T=0.68, M=64`, refined grid | **aborted**, > 570 s single process → R-4 unresolved | — |
| recomputation of the moment polygon's minimal-support direction | `166.19°` vs predicted `165.96°` | 1 s |

The `M = 64/96/128` block of (b) was **not** re-run, per the orders.
