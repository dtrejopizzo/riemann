# R153.009 — Hostile audit, round 3 (Tracks 1 and 2)

*Auditor of record: Claude Opus 5 (1M). Date 2026-09-19. Inputs: `R153_006_ROUND3_BLUEPRINT.md`,
`R153_005_LEAD_CLOSING_DECISION.md`, `R153_007_TRACK1_SINGLE_PAIR.md`, `R153_008_TRACK2_NEEDLE.md`,
all of `scripts/round3/`. Sources of truth consulted directly: Paper 42 `main.tex:1963–1970`
(`eq:evalcoords`), `main.tex:4072–4230` (`subsec:primitiveendpoints`, `eq:localizedprimitiveoperator`,
`thm:certifiedendpoints`), `scripts/audit/aud_spectral.py`. Independent re-computations were run from a
scratch re-implementation (own quadrature grading, own `basis_hat`, own panel counts) for the FATAL point
and from the builder's modules with independent drivers for the rest.
Labels: `PROVED` / `RESTATEMENT` / `DIAGNOSTIC-NUMERIC` / `OPEN` / `WITHDRAWN`.*

---

## 0. Resolution of the blueprint's paradox (attack point (a)) — read this first

The blueprint's consistency test is correct and the builder's object is **not** the object it tests.

**What `Q` is, exactly.** The builder's operator is

```
        Q_T(a,γ_0) := A_T − C(a,γ_0),        ⟨C F,F⟩ = 4 Re X,
        X = F̂(½+a+iγ_0) · conj F̂(½−a+iγ_0) = ∫_{−2T}^{2T} c_F(r) e^{(a+iγ_0)r} dr,
        4 Re X = 4 ∫_{−2T}^{2T} c_F(r) cosh(a r) cos(γ_0 r) dr,
        F̂(s) = ∫_{−T}^{T} F(t) e^{(s−½)t} dt,   c_F(r) = ∫ F(t)F(t+r) dt.
```

(`scripts/round3/track1.py`, `matC`: `C = 2(u_R v_R^⊤ + v_R u_R^⊤ − u_I v_I^⊤ − v_I u_I^⊤)` with
`u = mom(a+iγ_0)`, `v = conj mom(−a+iγ_0)` — this is exactly `4 Re X` as a quadratic form.)

So **`Q = A_T − (quadruple term)`**, i.e. the third of the three options in the orders. It is *not*
`A_T + R_T`, it is *not* `4 Re X` alone, and the on-line pair term `−2|F̂(½+iγ_0)|²` of the blueprint does
**not** appear in it at all.

**Is `Q` the Weil form of a divisor?** No, and it is not meant to be. `Q` is the Weil form of the
*complementary divisor*: under the hypothesis `H(a,γ_0)` = "the non-trivial zeros of `ζ` are the four points
`½±a±iγ_0` together with zeros on the critical line only", the unconditional identity
`⟨A_T F,F⟩ = Σ_ρ m_ρ F̂(ρ)F̂(1−ρ)` (T1.1) splits as

```
        ⟨A_T F,F⟩ = 4 Re X  +  Σ_{other ρ, on the line} |F̂(½+iγ)|² ,
```

and `⟨Q_T F,F⟩` **is** that remaining sum, which is a sum of squares, hence `≥ 0`. `Q ≥ 0` is therefore a
valid one-sided consequence of `H`, and `λ_min(Q_T) < 0` refutes `H`. The logic is sound. `STANDS`.

**Why `a = 0` can be negative, and why the blueprint's test does not bite.** The blueprint's `B_T = A_T + R_T`
is a perfectly well-defined bilinear form (the Weil pairing of the counterfactual divisor "`ζ`'s zeros with
`½±iγ_0` replaced by the quadruple", evaluated with `ζ`'s own primes and Gamma factor). The blueprint's
observation is right: at `a = 0`, `R_T = −2|F̂|² + 4|F̂|² = +2|F̂|² ≥ 0`, so `B_T ≥ A_T ≥ 0` at `T = log 2` and
`B_T` can never be negative there. **But `T*(0,γ_1) = 0.234` is not a value of `B_T`; it is a value of
`Q = A_T − 4|F̂(½+iγ_0)|²`,** whose negativity says: *more than one quarter of the total Weil mass
`Σ_ρ |F̂(½+iγ)|²` can be placed on the single ordinate `γ_0`* — which refutes a **double** zero at `γ_0`
under "all else on the line". No contradiction; the two forms are different objects, and the builder
discarded the blueprint's one. The blueprint's `B_T` route is correctly `WITHDRAWN`.

**One correction to the builder's own reason for discarding `B_T`.** `R153_007` §1 says `B_T` is "the divisor
of no zeta function, so Weil positivity says nothing". That is true but understates: under `H`, `A_T`
*already contains* the quadruple, so `B_T` applies the modification **twice** (it subtracts an on-line pair
that is not in the divisor and adds a quadruple that is). `B_T` is not "an unjustified form", it is the form
of the wrong divisor. Repair the sentence; the verdict is unchanged.

**Consequence for labelling.** Since `Q` is `a`-blind to first order (§3 below) and at `a = 0` refutes a
double on-line zero, `T*(a,γ_0)` is **not** a detection threshold for off-lineness. It must be relabelled.
Required: rename `T*(a,γ_0)` to `T_conc(γ_0;a)` (a *Weil-mass concentration threshold*) everywhere in
`R153_007` and in whatever reaches Paper 46, and drop the phrase "detection law" for `ζ` in favour of
"single-ordinate concentration criterion". The builder says this in §5 in prose; the naming must follow.

---
## 1. Verdict table

### Track 1

| # | claim (`R153_007`) | verdict | one-line reason |
|---|---|---|---|
| 1 | T1.1 `⟨A_TF,F⟩ = Σ_ρ m_ρ F̂(ρ)F̂(1−ρ)` on `P_T` | `STANDS` (`RESTATEMENT`) | matches Paper 42 `main.tex:1963–1970` up to the global sign convention there (`I_∂` has `−Σ_ρ`); the numerical check against 600 true ordinates fixes the convention empirically |
| 2 | verification ratio `0.9983…0.999978`, `1−10⁻⁶` at minimisers | `STANDS` (`DIAGNOSTIC-NUMERIC`) | independent re-derivation of the normalisation agrees; the residual is the `γ>600` tail as claimed |
| 3 | T1.2: on-line pair `→ 2|F̂|²`, quadruple `→ 4 Re X` | `STANDS` (`PROVED`) | re-derived below (§2); the blueprint's `2` is genuinely wrong |
| 4 | blueprint's cross coefficient `2` | `STANDS: WITHDRAWN` | confirmed |
| 5 | `B_T = A_T + R_T` rejected | `STANDS`, with the *reason* `RESTATEMENT`-grade repair of §0 | `B_T` is well-defined but is the form of the wrong divisor (double-counts the modification), not "the form of nothing" |
| 6 | T1.3 `|F̂(½±a+iγ)| ≤ e^{|a|T}‖F‖_1` | `STANDS` (`PROVED`, trivial) | one line |
| 7 | T1.4 `4ReX = 4∫c_F(r)cosh(ar)cos(γ_0r)dr` | `STANDS` (`PROVED`) | re-derived (§2) |
| 8 | T1.5 growth constant `cosh(2aT)`, attained up to factor 2 | `STANDS` (`PROVED`), but **`RESTATEMENT`-grade** | the identity `X = ∫c e^{(a+iγ)r}` plus `|cosh| ≤ cosh(2aT)` is Young's inequality; the "no textbook statement found" framing over-values it. Keep `PROVED`, drop the "classical in spirit but new" claim |
| 9 | T1.6 conditional exclusion, all `T`, independent of Paper 42 | `STANDS as a theorem`, `DOWNGRADE in content` | the proof is "drop a sum of squares", two lines, correct and non-circular; but it is **empirically subsumed**: the hypothesis `H(a,γ_0)` is already false for every `γ_0 ≤ 3·10¹²` by Platt–Trudgian *regardless of any computation*, and nothing above that is reached (§4) |
| 10 | `T*(a,γ_1)` `a`-independent to four decimals | `STANDS at γ_1 only`; **headline `DOWNGRADE`** | true at `γ_1` (`cosh(2aT) ≤ 1.0264` there — recomputed exactly), but at `γ_100`: `T* = 0.79308 / 0.78084 / 0.76751` for `a = 0 / 0.30 / 0.45`, a spread of `2.6·10⁻²` = 50× the bisection tolerance (§5). "`a`-independent" is a small-`T` statement, not a law |
| 11 | Table 2 `γ_0`-growth of `T*` | `STANDS` (`DIAGNOSTIC-NUMERIC`) | `T*(0,γ_100) = 0.79308` reproduced (builder `0.79284`) |
| 12 | naming `T*(a,γ_0)` a "detection law / threshold" | **`RESTATEMENT` required** | it is a Weil-mass-concentration threshold; at `a = 0` it refutes a double zero (§0) |
| 13 | **`γ_0^max(log 2) = 200.8 ± 1`, "identical for `a = 0` and `a = 0.45`"** | **`REFUTED`** | `λ_min(Q_{log2})` is **not monotone in `γ_0`**; a bisection is invalid. Fine scan at `a = 0.45` (`Ω`-mult 3, K-stable at mults 3/5/8): positive `≈+1.0·10⁻⁷` at `γ_0 = 150,170,180,191…198, 201…212`, **negative** at `γ_0 = 120 (−0.336), 189 (−0.0700), 190 (−0.0351), 199 (−0.0392), 200 (−0.154)`. The excluded set is a union of narrow windows, not the interval `[0,201]` |
| 14 | "above `γ_0^max` the correction is invisible; `λ_min(Q) = λ_min(A)`" | `STANDS` for the sampled `γ_0 ≥ 201` | independently reproduced at `γ_0 = 300` with a *from-scratch* assembly: `+1.0318/1.0139/1.0056/1.0008 ·10⁻⁷` at `K = 300/500/700/900`, `τ_max = 4000…20000`, versus `λ_min(A) = 1.0334…1.0014·10⁻⁷`. Also `+1.01·10⁻⁷` at `γ_0 = 400,410,420,430,700` |
| 15 | "FATAL rule satisfied with margin `10¹⁰`" | `DOWNGRADE` (conclusion survives, reasoning does not) | the margin argument rests on the refuted monotone cut-off. The correct clearance is logical, not numerical: `H(a,γ_0)` is already false below `3·10¹²`, so T1.6 cannot produce new information there, and no negativity was found at any sampled `γ_0 > 200` |
| 16 | "(P153.5) answered negatively: concentration, not off-lineness" | `STANDS` | supported by (a), by `a = 0` negativity, and by `cosh(2aT) ≤ 1.2010` at `T = log 2`; the `a`-effect is real but second-order (§5) |
| 17 | (P153.6)–(P153.9) open list | `STANDS`, add (P153.10) below | |

### Track 2

| # | claim (`R153_008`) | verdict | one-line reason |
|---|---|---|---|
| 18 | parity split `λ_min = min(λ_e,λ_o)` | `STANDS` (`PROVED`, elementary) | `R P_T = P_T` because `R` exchanges `M_±`; symbol even; shifts symmetric |
| 19 | Hellmann–Feynman `dλ/db = −2w_3 c'_{F_b}(b)` | `STANDS` (`PROVED`, standard) | builder's 3-digit check is the right check |
| 20 | peak is an **exact even/odd crossing** | `STANDS` (`DIAGNOSTIC-NUMERIC`); **the number `1.0·10⁻¹¹` `WITHDRAWN`** | independent golden section: gap `7.31·10⁻¹⁴` (K=160), `4.74·10⁻¹⁴` (K=240) — i.e. the gap is bounded only by how close to `b*` one evaluates, so quoting "gap `1e−11`" as a measured quantity is meaningless. The *linear closure* and the 90° eigenvector rotation are the real evidence and they stand |
| 21 | needle width is a level-set artefact, `|N(log2)| ≈ 2.0·10⁻⁵` | `STANDS` (`DIAGNOSTIC-NUMERIC`) | `3.64e−6·(1/0.263+1/0.584) = 2.007·10⁻⁵`, arithmetic checks |
| 22 | `argmax_b λ_min ≠ log 3`, displacement `1.30·10⁻⁵` | `STANDS` (`DIAGNOSTIC-NUMERIC`), error statement **must be repaired** | reproduced independently: `b*−log3 = +1.4302·10⁻⁵` (K=160), `+1.3898·10⁻⁵` (K=240). Quadrature perturbation (`τ_max 4000→8000`, `npan 400→600`, `ng 24→32`) moves `b*` by `2.8·10⁻¹⁰` / `5.1·10⁻¹⁰`. **Correct error statement: the displacement exceeds the quadrature error by `≈ 3·10⁴`, and exceeds the K = 160→240 basis drift (`4·10⁻⁷`) by `≈ 35`.** The builder's "`10⁶` times the noise" compares a `b`-displacement with an *eigenvalue* noise — a category error, even though the conclusion holds |
| 23 | `b*(T)` strictly decreasing, sweeps `log 3` at `T_c ≈ 0.7036` | `STANDS` (`DIAGNOSTIC-NUMERIC`) | independent K=240 run: `b*−log3 = +3.1191e−5 (T=0.68), +5.7886e−6 (0.700), −1.4676e−6 (0.704), −7.3595e−6 (0.706)`, so `T_c = 0.7032` at K=240 vs `0.7036` at K=160 — monotone drift confirmed; quote `T_c ≈ 0.703` with a `±0.001` basis uncertainty, not four digits |
| 24 | "the needle follows `T`, not `log 3`" | `STANDS` | direct consequence of #23 |
| 25 | `λ_min(A_{log2}|P_T) ≈ 9.9·10⁻⁸` "**above** Paper 42's certified `8.63386·10⁻⁸`" | **`REFUTED` as a comparison** | `R153_004` item 23 already established that `8.6339·10⁻⁸` is a two-level **Feshbach capacity margin** (`capacity 1.8328136e−6 − ell_eff 1.746475e−6`), *not* an `L²` Rayleigh lower bound; the two numbers live in different normalisations. Comparing them, and in particular inferring "consistent with / above the certificate", is illegitimate and re-imports the error `R153_004` removed |
| 26 | candidate (P153.4′) with its proof requirements | `STANDS` (`OPEN`) | requirements correctly identified; add the parity-block spectral-gap certification |
| 27 | "`b = log 3` unique contact" | `STANDS: WITHDRAWN (refuted)` | confirmed by #22, #23 |
| 28 | caveat that `n = 4` is omitted for `T > log 2` | `STANDS` | and it is the right caveat: the true form is more negative, so `T_c` is an upper bound |

---

## 2. (b) The cross coefficient and the growth constant, rederived independently

With `F̂(s) = ∫_{−T}^{T}F(t)e^{(s−½)t}dt` and `F` real, `conj F̂(s) = F̂(s̄)`; Paper 42's pairing uses
`conj F̂(ρ′)`, `ρ′ = 1−ρ̄`, and `conj F̂(1−ρ̄) = F̂(1−ρ)`. Put `A := F̂(½+a+iγ_0)`, `B := F̂(½−a+iγ_0)`, so
`F̂(½−a−iγ_0) = conj B` and `F̂(½+a−iγ_0) = conj A`.

| `ρ` | `1−ρ` | `F̂(ρ)F̂(1−ρ)` |
|---|---|---|
| `½+a+iγ_0` | `½−a−iγ_0` | `A·conj B = X` |
| `½−a+iγ_0` | `½+a−iγ_0` | `B·conj A = conj X` |
| `½+a−iγ_0` | `½−a+iγ_0` | `conj A·B = conj X` |
| `½−a−iγ_0` | `½+a+iγ_0` | `conj B·A = X` |

Total `2X + 2conj X = 4 Re X`. **The builder's `4` is right; the blueprint's `2` is wrong.** The `a → 0`
consistency test also confirms it: `X → |F̂(½+iγ_0)|²`, so `4ReX → 4|F̂|² = 2·(2|F̂|²)`, exactly a double
on-line pair. An on-line pair gives `2|F̂|²` (`1−ρ = ρ̄`), as claimed.

Growth: `A·conj B = ∫∫F(t)F(s)e^{(a+iγ_0)t}e^{−(a+iγ_0)s}\,dt\,ds = ∫_{−2T}^{2T}c_F(r)e^{(a+iγ_0)r}dr`
with `r = t−s` and `c_F` even and supported in `|r| ≤ 2T`. Taking real parts, the odd part
`sinh(ar)sin(γ_0r)` integrates against the even `c_F` to zero, leaving
`Re X = ∫ c_F(r)\cosh(ar)\cos(γ_0 r)dr`. Hence `|4ReX| ≤ 4\cosh(2aT)‖c_F‖_1 ≤ 4\cosh(2aT)‖F‖_1²`. The
constant is `cosh(2aT)`, **not** `e^{2aT}` and not the blueprint's `e^{aT}`-squared dichotomy.
Values recomputed: `cosh(2·0.45·log2) = 1.2009763…`; `cosh(2·0.49·0.23383) = 1.0263707…`
(the builder's "`≤ 1.026` in the `T*` range" is exact). **T1.2, T1.4, T1.5 all confirmed.**

---

## 3. (c) Is T1.6 vacuous or circular?

**Not circular.** It uses only the unconditional explicit-formula identity T1.1 (Paper 42 `eq:evalcoords`,
cited) and then discards a sum of squares. It does not use `A_T ≥ 0` anywhere, so it does not use
`thm:certifiedendpoints`, and the builder is right to say so against the blueprint's framing. The
`log 2` window plays no logical role; it is a reading position.

**Not logically vacuous, but empirically subsumed.** What is proved is exactly:

> For every `T>0` and every real `F ∈ P_T`, `4∫_{−2T}^{2T} c_F(r)\cosh(ar)\cos(γ_0 r)dr ≤ ⟨A_T F,F⟩`,
> **given** that `ζ`'s non-trivial zeros are `½±a±iγ_0` plus zeros on the line only.

Its contrapositive refutes `H(a,γ_0)` whenever a single `F` violates it. Two limitations the write-up
should state and does not:

1. **The hypothesis is already refuted below `3·10¹²` with no computation at all.** `H(a,γ_0)` asserts an
   off-line quadruple at height `γ_0`; Platt–Trudgian verify RH for `|γ| ≤ 3·10¹²`, so every `H(a,γ_0)` with
   `γ_0 ≤ 3·10¹²` is false already. T1.6 therefore adds information **only** for `γ_0 > 3·10¹²`, and §4
   reaches nothing near that. The builder's "margin `10¹⁰`" presents as comfort what is in fact the
   statement that the result is empty. This is not an error — the FATAL rule is passed — but the framing
   inverts the meaning and must be corrected.
2. **Direction of the numerics.** Galerkin/Rayleigh–Ritz gives an **upper** bound for `λ_min`. That is the
   *favourable* direction for the exclusions (a computed negative value exhibits an explicit `F`, modulo
   quadrature), and the *unfavourable* direction for the non-exclusions (a computed `+1.0·10⁻⁷` does **not**
   prove `λ_min ≥ 0`). So every "not excluded" entry in the FATAL table, including the whole basis of the
   `10¹⁰` margin, is numerically one-sided the wrong way. State this.

---

## 4. (d) The FATAL check recomputed

**Own quadrature, `γ_0 = 300`, `a = 0.45`, `T = log 2`** (scratch re-implementation: uniform panels to
`τ = 200` then geometric, `npan = 800`, `ng = 32`, own `basis_hat`/`moments`):

| `K` | 300 | 500 | 700 | 900 |
|---|---|---|---|---|
| `τ_max` | 4000 | 8000 | 12000 | 20000 |
| `λ_min(Q_{log2})` | `+1.031809e−7` | `+1.013902e−7` | `+1.005600e−7` | `+1.000761e−7` |
| `λ_min(A_{log2})` | `+1.033401e−7` | `+1.014884e−7` | `+1.006365e−7` | `+1.001413e−7` |

**Confirmed**: at `γ_0 = 300` the rank-four correction moves `λ_min` by `≈10⁻¹⁰`, i.e. it is invisible, and
the point is not excluded. The builder's `+1.0315·10⁻⁷ / +1.0181·10⁻⁷` is reproduced to three digits by an
independent assembly.

**But the cut-off is `REFUTED`.** Fine scan at `a = 0.45`, `Ω`-mult 3 (values stable at mults 3/5/8):

| `γ_0` | 120 | 150 | 170 | 180 | 188 | **189** | **190** | 191–198 | **199** | **200** | 201–212 | 250–262, 300–312, 400–412 | 700 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `λ_min(Q)` | `−3.36e−1` | `+9.98e−8` | `+9.73e−8` | `+9.85e−8` | `+9.81e−8` | `−7.00e−2` | `−3.51e−2` | `+1.0e−7` | `−3.92e−2` | `−1.54e−1` | `+1.0e−7` | `+1.01e−7` | `+1.00e−7` |

`λ_min(Q_{log2})` is a **two-level function of `γ_0`**: it sits at `λ_min(A) ≈ 1.0·10⁻⁷` except in narrow
windows where it plunges to `−O(10⁻¹)`. This is the expected structure (`C` has rank 4, so `Q ≱ 0` exactly
when the top eigenvalue of `C` in the `A`-metric exceeds 1, and once it does the negative branch dives
steeply), but it destroys the builder's construction: **a bisection in `γ_0` presupposes monotonicity and
there is none.** `γ_0 = 195` and `γ_0 = 198` lie below the claimed cut-off and are *not* excluded;
`γ_0 = 120, 189, 190, 199, 200` are. The honest statement is:

> The set of `(a,γ_0)` excluded by Theorem T1.6 read at `T = log 2` is `{(a,γ_0) : λ_min(Q_{log 2}(a,γ_0)) < 0}`,
> a union of narrow `γ_0`-windows. Windows were found at `γ_0 ≈ 120, 189–190, 199–200`; none was found at any
> sampled `γ_0` in `[188,212]∖{189,190,199,200}` and in `[250,262] ∪ [300,312] ∪ [400,412]` (unit spacing), nor at `430, 500, 700, 1000, 2000`. No upper bound on the
> excluded set is established by these computations.

**Answer to the (i)/(ii) alternative: (i), with a caveat.** The exclusions *are* a genuine consequence of the
explicit formula under `H` — they do not depend on the certificate and do not depend on `Q` being a Weil
form (it is the Weil form of the complementary divisor, §0). They are *not* an artefact of `Q`. The
**artefact** is the number `201` and the interval shape of the excluded set.

The exact sentence for the record, with the certificate not needed:

> *(Conditional exclusion, `PROVED` modulo one floating-point Rayleigh quotient.)* If the non-trivial zeros of
> `ζ` consisted of `½±a±iγ_0` with `a = 0.45`, `γ_0 = 200`, together with zeros on the critical line only,
> then `Σ_ρ F̂(ρ)F̂(1−ρ) < 4Re X` for an explicit `F ∈ P_{\log 2}`, contradicting the explicit formula.
> Hence that configuration is impossible.

Confirmation that this is inside Platt–Trudgian: yes, and *strictly* inside — `γ_0 = 200 ≪ 3·10¹²`, and the
configuration is in fact already excluded by Platt–Trudgian directly, so the statement carries no new
information about `ζ`. The FATAL rule is passed on both readings.

---

## 5. (e) Is the verdict right, and does `a`-independence persist?

**The verdict is right.** `T*(a,γ_0)` at `a = 0` is nonzero and nearly equal to its value at `a = 0.45`;
the quantity being detected is concentration of `Σ_ρ|F̂(½+iγ)|²` on one ordinate. `STANDS`.

**The `a`-independence is a small-`T` phenomenon, and the headline overstates it.** Recomputed:

| | `a = 0` | `a = 0.30` | `a = 0.45` |
|---|---|---|---|
| `T*(a,γ_1)` (builder) | `0.23419` | `0.23383` | `0.23383` |
| `cosh(2aT*)` | `1` | `1.0398` | `1.0894` |
| **`T*(a,γ_100)` (this audit)** | **`0.79308`** | **`0.78084`** | **`0.76751`** |
| `cosh(2aT*)` | `1` | `1.1118` | `1.2482` |

At `γ_1` the spread is `3.6·10⁻⁴` = the bisection tolerance; at `γ_100` it is `2.56·10⁻²`, **71× the
tolerance and monotone in `a`** in the expected direction (a larger `a` is detected on a shorter window).
So "`T*` is `a`-independent to four decimals" must be restricted to `γ_0 = γ_1`; the general statement is
"the `a`-dependence enters only through `cosh(2aT)−1`, hence is a `≤ 25 %` effect on the form and a
`≤ 3 %` effect on `T*` for all `a < ½` and all `T ≤ 0.8`". That still supports the verdict.

---

## 6. (f)–(g) Track 2 numbers, re-run independently

Independent driver (own golden section to `10⁻¹²`, builder's assembly):

```
 (f)  K=160  b*-log3 = +1.4302e-05  lam(b*) = 3.801228e-06  gap_12 = 7.31e-14  lam_3 = 2.160e-03  lam(log3) = 1.067545e-07
      quadrature-varied (taumax 8000, npan 600, ng 32):  b*-log3 = +1.4302e-05  (shift 2.8e-10)
      K=240  b*-log3 = +1.3898e-05  lam(b*) = 3.701545e-06  gap_12 = 4.74e-14  lam_3 = 2.119e-03  lam(log3) = 1.043782e-07
      quadrature-varied:                                    b*-log3 = +1.3899e-05  (shift 5.1e-10)
 (g)  T=0.6800  b*-log3 = +3.1191e-05  lam(b*) = +7.770503e-06
      T=0.7000  b*-log3 = +5.7886e-06  lam(b*) = +1.636233e-06
      T=0.7040  b*-log3 = -1.4676e-06  lam(b*) = -3.332022e-07
      T=0.7060  b*-log3 = -7.3595e-06  lam(b*) = -2.023189e-06
```

The crossing persists at both `K`; the third eigenvalue is `2·10⁻³`, i.e. `10³` times the branch gap, so the
two crossing branches are cleanly isolated and the parity reading is safe. The argmax displacement is
stable: `1.4302e−5 → 1.3898e−5` from `K = 160` to `240`, quadrature-insensitive at the `5·10⁻¹⁰` level.
**Error of record for the displacement: `5·10⁻¹⁰` (quadrature) and `4·10⁻⁷` (basis, `K` 160→240).** Both are
orders below `1.3·10⁻⁵`. The monotone drift of `b*(T)` is confirmed at two `T` values with numbers matching
the builder's to five digits, and the sign change lands between `T = 0.700` and `T = 0.704`.

---

## 7. (h) The `8.63·10⁻⁸` comparison

**Illegitimate. Flagged.** `R153_004` item 23 (citing `W4_CERTIFIED_RANGE.md:197–208`) established that
`8.6339·10⁻⁸ = capacity(1.8328136·10⁻⁶) − ell_eff(1.746475·10⁻⁶)` is a **two-level Feshbach capacity
margin**, and that its numerical proximity to `λ_min ≈ 1.0·10⁻⁷` is a coincidence across two
normalisations. `R153_008` item 6 writes `λ_min ≈ 9.9·10⁻⁸` "above Paper 42's certified margin
`8.63386·10⁻⁸`", which re-asserts exactly the comparison that was refuted one round earlier, and would, if
repeated, suggest the certificate is within 15 % of sharp — a claim with no basis.

**Required replacement for `R153_008` §1 last sentence and verdict-table row 6:**

> `λ_min(A_{log 2}|P_T) ≈ 9.9·10⁻⁸` (`1/K`-Richardson from `1.0993/1.0675/1.0438/1.0307·10⁻⁷` at
> `K = 100/160/240/320`), a Galerkin **upper** bound in the `L²` Rayleigh normalisation, consistent with the
> audit's `≤ 1.05·10⁻⁷`. No comparison is made with Paper 42's `8.63386·10⁻⁸`: per `R153_004` item 23 that
> number is a Feshbach capacity margin in a different normalisation, not a lower bound on this Rayleigh
> quotient, so the two are not commensurable and nothing about the sharpness of the certificate follows.

---

## 8. (i) Withdrawals from `R153_005` and the exact replacement text

Both flagged items must indeed be withdrawn.

**(i.1) `R153_005` §1, the `b`-scan row.** Current text: *"`λ_min(b)` has an isolated positive needle at
`b = log 3` of height `≈1.1·10⁻⁷` and width `~10⁻⁷`, negative elsewhere in the scanned range. Reading: at
`T = log 2` positivity of the two-prime Weil form is exactly critical and the critical point sits at the
arithmetic contact. Not a theorem."* — `WITHDRAWN` (the width, the location of the critical point, and the
arithmetic reading). Replacement:

> | `b`-scan | replacing the shift `log 3` by `b`: `A_T(b)` splits by parity and `λ_min(b) = min(λ_e,λ_o)`; the
> two branches cross transversally with one-sided slopes `+0.263 / −0.584`, so `λ_min` has a corner-maximum at
> `b* = log 3 + 1.30·10⁻⁵` (K-extrapolated; `+1.43/+1.39·10⁻⁵` at `K = 160/240`, quadrature-stable to
> `5·10⁻¹⁰`) with `λ_min(b*) ≈ 3.5·10⁻⁶ ≈ 35·λ_min(log 3)`. The positivity set `N(log 2) = {b : λ_min(b) > 0}`
> is an interval of length `≈ 2.0·10⁻⁵`, and `log 3` lies inside it, `≈ 4·10⁻⁷` from its left endpoint. The
> "needle of width `10⁻⁷`" was a level-set artefact of near-criticality. Reading: at `T = log 2` the two-prime
> form is exactly critical, and the critical point is **not** at the arithmetic contact. | `DIAGNOSTIC-NUMERIC`
> (supersedes the round-2 row) |

**(i.2) `R153_005` §2, item 4.** Current text: *"The endpoint `log 2` is critical, not comfortable.
`λ_min(A_{log 2}|P_T) ≲ 10⁻⁷` in L² normalisation, and the `b`-needle says the two-prime form is positive
essentially only at `b = log 3`. Whatever mechanism eventually extends positivity past `log 2` must be
arithmetic (use the contacts), not analytic domination."* — second and third sentences `WITHDRAWN`.
Replacement:

> 4. **The endpoint `log 2` is critical, not comfortable — and the criticality is a parity phenomenon.**
>    `λ_min(A_{log 2}|P_T) ≲ 10⁻⁷` in `L²` normalisation (a Galerkin upper bound; not commensurable with
>    Paper 42's Feshbach capacity margin). Moving the second contact to `b` shows the even and odd blocks of
>    the form within `1.3·10⁻⁵` of an exact crossing at `T = log 2`: positivity is held by the **even** block
>    by `≈10⁻⁷`, while the **odd** block is the one that turns negative first as `T` grows, at
>    `T ≈ 0.703` in the two-contact model. The position of the critical contact moves smoothly with `T` and
>    passes through `log 3` at an arithmetically meaningless `T ≈ 0.703`, so no arithmetic role for `log 3`
>    beyond its weight `w_3 = Λ(3)/\sqrt3` is supported. Consequence for `(P153.3)`: organise any extension
>    past `log 2` **by parity block and expect the obstruction in the odd block** — not, as previously stated,
>    by "using the contacts".

---

## 9. General compliance

- **Labels.** Track 1's labels are correct except items 12, 13, 15 of §1 (see the table); Track 2's are
  correct except items 20 (number) and 25.
- **FATAL rule.** Passed on both tracks. Track 1's clearance must be re-argued as in §3/§4 (logical
  subsumption + no negativity found above `γ_0 = 200`), not as a bisection margin. Track 2 is deflationary
  and imports nothing.
- **No sign for `ζ` beyond `log 2`.** Respected. T1.6 is the explicit conditional and is correctly flagged as
  conditional; Track 2's `T_c ≈ 0.703` is correctly flagged as an upper bound for a *model* that omits
  `n = 4`, with no claim for `ζ`.
- **Corpus checks.** Re-run, one per track, and genuine. Track 1: `grep -rIl "single off-line"` returns
  phase 105 (`105_02_OFF_LINE_ZERO_EXPONENTIAL_THEOREM`, a Li-coefficient statement), phase 64
  (`FACE-C-spectral-shift-monotonicity`, `CONSTRUCTION-boundedness`), phases 66/67/79 scripts, and phase 153
  — as reported; `grep -rIn "cosh(2aT)"` outside phase 153 returns nothing. Track 2: `grep -rIl "needle"`
  returns only phase-153 files (`R153_002/003/004/005/008` and the round-3 scripts) — as reported.

## 10. Required repairs

1. `R153_007` §4: delete `γ_0^max(log 2) = 200.8 ± 1` and the bisection; replace with the window statement of
   §4 above and a plot-grade scan. Delete "margin `10¹⁰`"; replace with the logical clearance of §3.
2. `R153_007` headline and §3: restrict "`a`-independent to four decimals" to `γ_0 = γ_1`; add the `γ_100` row.
3. `R153_007` §1: repair the reason for rejecting `B_T` (§0 above).
4. `R153_007` throughout: rename `T*(a,γ_0)` to a concentration threshold; drop "detection law" for `ζ`.
5. `R153_007`: add to every non-exclusion the sentence "Rayleigh–Ritz gives an upper bound, so a computed
   positive `λ_min` does not prove non-exclusion".
6. `R153_008` §1 and row 6: replace the `8.63386·10⁻⁸` comparison with the text of §7.
7. `R153_008` row 3: withdraw the number `1.0·10⁻¹¹`; state instead that the gap closes linearly and is
   limited only by `|b−b*|` (independently `7·10⁻¹⁴` at a tighter `b*`), and that `λ_3 ≈ 2·10⁻³` isolates the
   pair.
8. `R153_008` §2.4 / §3: quote `T_c = 0.703 ± 0.001` (K-dependence), not `0.7036/0.7037`.
9. `R153_005`: apply the two replacements of §8.
10. New open item **(P153.10)**: characterise `{γ_0 : λ_min(Q_T(a,γ_0)) < 0}` — is it a finite union of
    windows, does it terminate, and can the top eigenvalue of `C` in the `A`-metric be bounded uniformly in
    `γ_0`? Without this, T1.6 read at a fixed `T` has no known reach. `OPEN`.

---

## 11. Honest reading of what round 3 established

Round 3 produced two clean, entirely deflationary results and one repaired formula. Track 1 showed that the
single-off-line-pair analogue of Theorem A exists, is exact, and is worth almost nothing: the whole
`a`-dependence of the Weil form over a window of length `2T` is the factor `cosh(2aT)` (`≤ 1.21` at
`T = log 2`), so a bounded window cannot tell an off-line quadruple from a double on-line zero — it can only
measure whether more than a quarter of the Weil mass sits on one ordinate. The conditional exclusion T1.6 is
true and proved in two lines from the explicit formula, needs neither Paper 42's certificate nor any window
restriction, and is empirically empty: everything it can refute at `T = log 2` sits at `γ_0 ≲ 200`, where
Platt–Trudgian has already refuted it, and the builder's tidy cut-off `γ_0^max ≈ 201` does not exist — the
excluded set is a union of narrow windows and this audit found no upper bound for it. Track 2 killed the
arithmetic reading of the `b`-needle: the peak is an ordinary transversal crossing of the even and odd
parity blocks with `O(1)` slopes, its position is `log 3 + 1.3·10⁻⁵`, it drifts smoothly with `T` and crosses
`log 3` at a meaningless `T ≈ 0.703`, and the "needle" was only the level set of a form that barely clears
zero. The one durable, forward-looking item in either track is Track 2's parity redirection: positivity at
`log 2` is held by the even block and is lost first in the odd block, so `(P153.3)` should be attacked block
by block. Against that, Track 2 re-imported a comparison between an `L²` Rayleigh quotient and a Feshbach
capacity margin that the previous round had explicitly removed, which must not reach Paper 46. Row D's label
is unchanged, and nothing in round 3 moves the sign for `ζ` by a single window.

*Audit scripts of record: `scripts/round3/audit_r3_fatal_independent.py` (own assembly, §4 table),
`audit_r3_gamma_scan.py` (the `γ_0` fine scan), `audit_r3_track2_recheck.py` (§6), `audit_r3_tstar_gamma100.py` (§5).*
