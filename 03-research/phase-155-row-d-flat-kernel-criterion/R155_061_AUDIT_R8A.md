# R155.061 — Audit of round 8a (`R155_052`, the exact negative index by the multi-band relaxation)

*Phase 155. Object: `R155_052_ROUND8A_INDEX_MULTIBAND.md` (474 lines) and
`scripts/r8a/` (`r8a_lib.py`, `r8a_01_upper.py`, `r8a_02_lower.py`, `r8a_03_recheck_lower.py`, `README.md`, all
JSON), with the inherited `scripts/r4a/r4a_lib.py`. Reference texts read (the paper's **own** definitions, rule
`feedback-check-against-paper-definitions`): Paper 47 `main.tex:114–150` (`eq:symbol`, `eq:form`, Tate moments,
`\PT`, `eq:W`), `:336–420` (`lem:K`, `thm:S`, `thm:A`), `:1139–1150` (`def:W`, `eq:nuw`), `:2326–2460` (`\Ainf`,
`\laminfP`, `prop:arch`, `prop:nodes` incl. the Dirichlet-form identity, the DIAGNOSTIC `0.5958`), `:2471–2625`
(`prop:NC`, `thm:P`, `cor:P1`, `cor:P3`, `rem:P4`, `thm:J`, the `T₂ ≤ 0.9989426` remark); `R155_023:23–24,195,365`,
`R155_025:179–190`, `R155_039:245`. mpmath 1.3.0 source (`ctx_iv.py:30–45, 425–445`: outward conversion of
`int`/`str`/`float`, exact pass-through of `mpf`). Compute done: the eight archived `r8a_01` cases re-run with the
corrected script **strictly one at a time** (13.2–14.0 s each, machine idle, load 0.25), and `r8a_03` re-run
(0.1 s). Nothing else was computed. The archived JSON were copied to the scratchpad before any run; no archived
file was overwritten (the script writes `_rerun.json`, verified at `r8a_01_upper.py:187–188` and by `ls`).*

**Verdict in one line.** Every PROVED statement of `R155_052` survives. Theorem 5.1, Corollaries 5.2–5.3 and
Lemma 4.3 are **correct**. The sign of the border coupling is `+` (derived independently below). The corrected
re-runs reproduce every archived certificate **bit for bit** (same `r`, same margins `μ` to the last printed digit,
same midpoint spectra). Six AMENDs, none changing a PROVED statement: the certificates of record move to the
re-runs (A1); a new small finding, a non-rigorous `C₀` guard inside `r4a_lib` under `r8a_02`'s import order, is
absorbed by `r8a_03`'s inflation and makes `r8a_03` (not `r8a_02`) the certificate of record for the lower bounds
(A2); an unproved-as-coded `1e-30` tolerance in the `s ≤ c_N` assertion is closed by a one-line argument (A3); and
three wording/arithmetic fixes (A4–A6). No FAIL.

---

## Per-claim findings

### (i) Definitions against Paper 47 — PASS

* `m(τ) = Re ψ(¼+iτ/2) − log π` (`eq:symbol`), `C₀ = ψ(¼) − log π` (`lem:K`); `ψ(¼) = −γ − π/2 − 3log 2`, so
 `C₀ = −γ − 3log2 − π/2 − log π = −5.3721834…` as in the memo and in `r8a_lib.C0_interval`.
* `K(u) = 1/(2sinh(u/2)) + 1/(2cosh(u/2)) = 2Σe^{−(2k+½)u}` (`lem:K`) — matches `r4a_lib._Ksv + _Kc` and Lemma 4.3(3).
* `thm:S(i)`: `m − C₀ = φ(τ²) = Σ τ²/(a_k(τ²+4a_k²)) = Σ s/(a_k(a_k²+s))`, `s = τ²/4` — matches `m_interval`.
* `A = ∫Fe^{t/2}`, `B = ∫Fe^{−t/2}`, `P_T = {A = B = 0}` (`main.tex:128–130`); `\Ainf = 2A(F)B(F) + C₀‖F‖² + Lev(c_F)`
 and `\laminfP` = bottom of `\Ainf` on the unit sphere of `P_T` (`:2338–2344`); `T*_{∞,P} = sup{T : \laminfP > 0}`
 (`prop:arch(iv)`); `Γ_T = C₀‖F‖² + Lev(c_F)` (`prop:nodes`), so `\Ainf = Γ_T` on `P_T`. The memo's notation block is
 a faithful transcription. The form certified by `r8a_01`/`r8a_02` is `Γ_T` restricted to `P_T^par` (bordered by
 `ℓ = ⟨·,g_par⟩`), i.e. `\Ainf|P_T`, **not** `W_T` (see (vii)).
* `thm:P`: `S_c = Q_TB_sQ_T`, `c = Ts`, `⟨S_ce_j,e_j⟩ = (2/π)(2j+1)∫_0^c j_j²`, `tr S_c = 2c/π`,
 `Λ_k(c) = Σ_{j≥k}⟨S_ce_j,e_j⟩`. The script's `Rdiag_all[j] = (2/π)(2j+1)I_0^{(jj)}(c_*)` and
 `LamK = 2c_*/π − Σ_{j<K}R_j` (both parities) are exactly this. PASS.
* Real vs complex. Paper 47 writes `\Ainf` with `2A(F)B(F)` (no conjugate), i.e. on real `F`, while `L²(I_T)` in
 §1 is complex. No discrepancy: `m` is even and real, so for `F = u + iv` one has `Γ[F] = Γ[u] + Γ[v]` (the cross term
 `(1/π)∫m Im(û\bar v̂)` has an odd integrand), and `A, B` are real functionals; the complex negative index and bottom
 equal the real ones. (Recorded as a one-line remark under Lemma 4.1, A6.)

### (ii) Lemma 2.1 (bordered inertia) — PASS

`v = w + tv₀`, `b = q[w] + 2tq(w,v₀) + t²q[v₀] + 2ξt = q[w] + (t²q[v₀] + 2tη)`, `η = ξ + q(w,v₀)`; no cross term
between `w` and `(t,η)`; the binary form has determinant `−1` whatever `q[v₀]` is. Correct. In `r8a_02` the
degenerate cases (`ℓ = 0` on the span, or `F, h` dependent) are harmless: a negative-definite subspace of the pulled-
back Gram form maps injectively, and if `ℓ ≡ 0` the span already lies in `P_T^par` (memo §3.1 handles the first).

### (iii) Lemma 2.2 (multi-band minorant) — PASS, AMEND A3 (tolerance) and A5 (edge count)

The chord/offset argument is right: `h = m − ℓ`, `h'' ≤ M2`, `h + M2(τ−τ_a)(τ_b−τ)/2` concave and `0` at the ends,
so `h ≥ −M2Δ²/8`; lowering the end values to `m_lo` lowers the chord. Band 0 (`s = C₀`) and the tail (`s = c_N =
m_lo(τ_N) ≤ m(τ_N) ≤ m(τ)`) use only `lem:mbounds(i)`. `m_interval`'s tail bracket is right: `∫_X^∞ s/(y(y²+s))dy =
½log(1+s/X²)` (differentiated back), and the summand is decreasing in `y`.

*Gap as coded (A3).* `M = c_N − L ≥ 0` needs `s ≤ c_N` everywhere; `r8a_01_upper.py:83` asserts it at the band ends
only up to a tolerance `+1e-30`, which by itself proves nothing. It is true for a reason the memo does not state: every
chord end value is `m_lo(τ^{(b)}) − off ≤ m_lo(τ^{(b)})`; the enclosure widths of `m` are `≤ f(K₀) ≈ s/X³ ≤ 7·10⁻⁹`
(at `τ_N ≤ 27.6`), while consecutive edges have `m(τ^{(b+1)}) − m(τ^{(b)}) ≥ 0.03` (increments of an increasing `m` on
bands of width `≥ 0.15` near `0`, where `m' ≈ 32τ`, and on geometric bands where `m' ≳ 1/τ`); so `m_lo` is increasing
along the edges and every end value is `≤ m_lo(τ_N) = c_N`, with equality possible only at the right end of the last
band, where the true value is `c_N − off_N ≤ c_N` exactly. The chord is affine, so `s ≤ c_N` on every band. The
tolerance only absorbs interval over-estimation at that one point. Also `W = c_N − min s` is computed from the lower
ends of the (affine) band values, hence an upper bound on `c_N − s`. Minor (A5): "7 geometric edges `9 → τ_N`" is
8 edges `9, …, τ_N` (20 fixed + 7 + `τ_N` = 28 edges, 28 bands with band 0 = `[0, 0.15]`); `τ_N = c_*/T` is rounded
to 6 decimals, so `c_* = Tτ_N ≈ 16` (not exactly `16`); nothing depends on either.

### (iv) Lemma 2.3 (the `m''` summand) — PASS (doubt 3 resolved)

Independently: with `φ_k(s) = s/(a(a²+s))`, `φ' = a/(a²+s)²`, `φ'' = −2a/(a²+s)³`, `ds/dτ = τ/2`, `d²s/dτ² = ½`:
`d²φ_k/dτ² = φ''·s + φ'/2 = a(a² − 3s)/(2(a²+s)³)`. The script's summand `u_k = a(a²/2 − s)/(a²+s)³ = a(a² − 2s)/(2(a²+s)³)`
exceeds it by `as/(2(a²+s)³) ≥ 0`. Quasi-convexity: `u_k' = a(a²+s)^{−4}(2s − 5a²/2)` and, for the exact summand,
`∝ s − a²`; each is decreasing-then-increasing, so its sup over an `s`-interval is at an end. The positive tail is
`≤ Σ_{k≥K₀}1/(2a_k³) ≤ ∫_{K₀−1}^∞dx/(2(x+¼)³) = 1/(4(K₀−¾)²)` ✓; dropping the negative parts of the tail only raises
the bound ✓. **The endpoint argument covers the whole band:** `m2sup(mp.mpf(ta.a), mp.mpf(tb.b))` is evaluated on
the outer ends of the interval edges, i.e. on an `s`-interval containing the true band, and termwise sup-at-an-end
gives `Σ_k sup u_k ≥ sup Σ_k u_k ≥ sup_band m''`. So `M2_a ≥ sup_{band a} m''` and the offset `max(M2_a,0)Δ²/8` is valid.

### (v) Prop 2.4 — PASS; (d) sign derived independently; AMEND A1 (certificates of record) and A4 (arithmetic, wording)

**(a)** `B₂₂ = c_N − P_YMP_Y`, `P_YMP_Y ≤ W P_YS_{c_*}P_Y`, and `‖P_YS_{c_*}P_Y‖ ≤ ‖P_K^⊥S_{c_*}P_K^⊥‖ ≤
tr(P_K^⊥S_{c_*}P_K^⊥) = Λ_K(c_*)`: `Y ⊂ ran P_K^⊥` and `P_K^⊥SP_K^⊥ ≥ 0`. `0 ≤ c_N − s ≤ W·1_{|τ|<τ_N}` gives
`0 ≤ M ≤ W S_{c_*}` with `c_* = Tτ_N` = `cs[-1]` ✓. Clipping `Λ_K` to `[0, ·]` is legitimate.

**(b)/(d) The sign, derived from the Haynsworth split.** Write `F = Σ_{i∈iK}a_ie_i + y`, `y ∈ Y`. Then
`B(F,ξ) = L[Σa_ie_i] + 2ξΣa_ig_i + 2L(Σa_ie_i, y) + 2ξ⟨y,g⟩ + L[y]`. The `X×Y` block is read off the cross terms:
`B((e_i,0), y) = L(e_i, y) = ⟨(c_N − M)e_i, y⟩ = −⟨P_YMe_i, y⟩` (as `⟨e_i,y⟩ = 0`) and `B((0,1), y) = ⟨g, y⟩ = ⟨P_Yg, y⟩`.
So the `Y`-columns are `v_i = −P_YMe_i`, `v_ξ = +P_Yg`. With `B₂₂ ≥ γ`, `B₁₂B₂₂⁻¹B₂₁ ≤ γ⁻¹Gram(v)` and
`S ≥ R = B₁₁ − γ⁻¹Gram(v)`: `R_{ij} = L_{ij} − γ⁻¹⟨P_YMe_i,P_YMe_j⟩`, **`R_{iξ} = g_i − γ⁻¹⟨v_i,v_ξ⟩ = g_i +
γ⁻¹⟨P_YMe_i, P_Yg⟩`**, `R_{ξξ} = −γ⁻¹‖P_Yg‖²`. The memo's (b) and the corrected `r8a_01_upper.py:155` (`gc[i] +
gram/gamma`) are right; the archived runs had `−`.

The memo's perturbation bound is also right in substance: `g_l² = 2T(2l+1)i_l(z)²`, `i_l(z) ≤ z^le^{z²/2}/(2l+1)!!`
(termwise from `i_l = Σz^{l+2k}/(2^kk!(2l+2k+1)!!)`), and at `T = 0.9`, `l = 22`: `81·0.45⁴⁴·e^{0.2025}/(45!!)² ≈ 8.4·10⁻⁷¹`
(`45!! ≈ 2.54·10²⁸`), so `‖P_{22}^⊥g‖ ≤ 9.2·10⁻³⁶` and `|E_{iξ}| ≤ 2W‖P^⊥g‖/γ ≤ 1.3·10⁻³⁴`. Arithmetic slip (A4):
`‖E‖_F ≤ √(2·11)·1.3·10⁻³⁴ = 6.1·10⁻³⁴`, not `≤ 6·10⁻³⁴` — immaterial. **But the argument is no longer needed:** the
corrected script was re-run on all eight archived cases (table below) and returns identical certificates. The
certificates of record are now the `_rerun.json` files (A1); Prop 2.4(d) becomes a remark.

**(c)** `‖P^⊥_{K2}Me_i‖² = ⟨M^{½}(M^{½}P^⊥M^{½})M^{½}e_i,e_i⟩ ≤ ‖P^⊥MP^⊥‖M_{ii} ≤ WΛ_{K2}M_{ii} = ρM_{ii}` ✓ (uses
`‖M^{½}P^⊥M^{½}‖ = ‖P^⊥MP^⊥‖`); Cauchy–Schwarz gives the two tail boxes exactly as coded (`:144–151`). `M` preserves
parity (`m` even), so `⟨P_YMe_i,P_YMe_j⟩ = Σ_{l≥K, l≡par}M_{il}M_{jl}` = `iT` sum + tail ✓. `‖g_0‖² = T + sinh T`,
`‖g_1‖² = sinh T − T` ✓. `R_{ξξ} = −gtail_K/γ` ✓.

**(e)** Correct: `U^TRU ≻ 0` (all matrices in the box) forces `U` injective, so `R` is positive definite on an
`(n−r−1)`-dimensional subspace and `n₋(R) ≤ r+1`; `n_par ≤ n₋(R) − 1 ≤ r`. Wording (A4): `U` is not "converted
exactly" — `iv.mpf(repr(float))` encloses the shortest decimal of each float; the certificate is for that decimal
matrix, which is equally good.

**Bessel moments.** `beta_coeffs` is DLMF 10.8.3 with exact `Fraction`s; `iv.mpf(numerator)/iv.mpf(denominator)` is
outward (mpmath `from_int` with floor/ceiling). Tail: for `k ≥ max(a, 2c)`, `(a+2k)/(a+k) ≤ 2`, `(a+2k+1)/(k+1) < 3`,
so the ratio is `< 1.5c²/(k+1.5)² ≤ 3/8` (also for the `t_0`, `t_1` sequences, which carry the extra factors
`n/(n+2)`, `(n+1)/(n+3) < 1`); the alternating remainder is `≤` the next term `≤` the last included term ✓.
`kstar = int(2·float(c.b)) + 2 > 2c` ✓ (the only float there chooses a truncation index).

**Doubt 6 (cancellation at `c_* = 16–24`).** Every certified quantity in `r8a_lib`/`r8a_01` is an `iv` interval: the
grep of `float(`/`np.` in both files hits only data (band edges, `τ_N`, `kstar`, the midpoint matrix and its
eigenvectors, the bisection trial `μ` — passed back as `iv.mpf(repr(μ))`) and output formatting (`lo/hi/mid`). The
`mp` (non-interval) values that enter are `mp.mpf(v.a)` endpoints, which `iv.mpf` passes through exactly
(`ctx_iv.py:31`). Cancellation of `≈ 2c_*log₁₀e` digits widens the intervals (to `≤ 1.7·10⁻¹³` in `R`), it cannot
make them wrong. PASS; the memo's warning that `c_* ≳ 35` needs `IVDPS` raised is correct and is about success, not
rigour.

### (vi) Re-run of the corrected `r8a_01` (doubt 1) — PASS

Run :05, one process at a time (file mtimes 15 s apart), machine idle; default `K = 22`, `K2 = 36`,
`c_* = 16`, 28 bands; outputs `scripts/r8a/r8a_01_<T>_par<p>_rerun.json`.

| `T` | par | archived `r` / `μ` | **re-run `r` / `μ`** | Δμ | max Δ(midpoint eigs) | width of `R` | re-run time |
|---|---|---|---|---|---|---|---|
| `0.58` | 0 | `0` / `0.015998191123` | **`0` / `0.015998191123`** | `0` | `0` | `9.0e-14` | `13.2 s` |
| `0.58` | 1 | `0` / `0.047516053575` | **`0` / `0.047516053575`** | `0` | `0` | `1.0e-14` | `14.0 s` |
| `log 2` | 0 | `1` / `0.420225447224` | **`1` / `0.420225447224`** | `0` | `0` | `1.1e-13` | `13.4 s` |
| `log 2` | 1 | `0` / `0.041093050709` | **`0` / `0.041093050709`** | `0` | `0` | `1.3e-14` | `13.5 s` |
| `0.80` | 0 | `1` / `0.298000128861` | **`1` / `0.298000128861`** | `0` | `0` | `1.4e-13` | `13.3 s` |
| `0.80` | 1 | `1` / `0.161623582519` | **`1` / `0.161623582519`** | `0` | `0` | `1.6e-14` | `13.6 s` |
| `0.90` | 0 | `1` / `0.185541470433` | **`1` / `0.185541470433`** | `0` | `0` | `1.6e-13` | `13.7 s` |
| `0.90` | 1 | `1` / `0.144839528294` | **`1` / `0.144839528294`** | `0` | `0` | `1.9e-14` | `13.5 s` |

Bit-identical, as the `10⁻³⁴` size of the corrected term (far below the `10⁻¹³` interval widths and below double
resolution of every printed number) predicts. All eight runs are under 60 s; the §8 deviation is closed. Not re-run
(not load-bearing): `r8a_01_0p80_par1_fine.json` and `…_K30_K244_c24.json` (both only `≤ 1` at `0.80` odd, which
already follows from `0.90` par 1 by Lemma 4.2, and DIAGNOSTIC for §6). Observation: the archived
`r8a_01_0p80_par1.json` (22:37) has no `grid` key, so it was produced before the sign fix; it too is superseded.

### (vii) `r8a_02` / `r4a_lib`: the form is `\Ainf|P_T`, primes off, pole unused (doubt 5) — PASS, AMEND A2

* `LF.atoms = []` is set after construction (`r8a_02:63`); `W()` builds `prim` by looping over `self.atoms`
 (`r4a_lib:262`), so `prim = 0`, and in any case `Gam` discards the total and reads
 `gam = LF.C0·d['c0'] + d['INT'] + d['c0']·LF.Ktail` (`r8a_02:67`). The pole enclosure is computed and unused. This is
 `C₀‖F‖² + ∫_0^{2T}(c(0)−c)K + c(0)∫_{2T}^∞K = C₀‖F‖² + Lev(c_F) = Γ_T[F]` (`thm:A` with `N_T = ∅`, support of `c_F`
 in `[−2T,2T]`). With `F(t) = p(t/T)/√T`, `c_F(Ts) = q(s)`, `INT = T∫_0^2G(s)K(Ts)ds` ✓. `Ktail = log((e^T+1)/(e^T−1))
 + 2arctan e^{−T} = log coth(T/2) + π − 2arctan e^T` (`thm:S(iii)`) ✓, arctan series tail `≤ z^{401}/401` ✓.
 `⟨F,g_0⟩ = (A+B)/2`, `⟨F,g_1⟩ = (A−B)/2` ✓ (`g_0 = cosh(t/2)`, `g_1 = sinh(t/2)`); the moment series and its
 `2|a|^{90}e^{|a|}/90!` tail ✓. Certified object: the bordered form of `Γ_T` on `L²_par ⊕ ℝ` with border
 `⟨·,g_par⟩`, i.e. `Γ_T` on `P_T^par`, which is `\Ainf|P_T^par`. Not `W_T`.
* Range: the affine sandwich needs `1/(2cosh(u/2))` concave, `sech''(v) = sech v(1 − 2sech²v) ≤ 0 ⟺ cosh v ≤ √2`, on
 `u = 2v ≤ 2T`, i.e. `T < arccosh√2 = 0.881374` ✓; `1/(2sinh(u/2))` is convex on `u > 0` ✓. Singular end:
 `K ≤ 1/u + ½` ✓ and `G(s) ≤ G1·s` with `G1 = Σ|Chebyshev coeffs of G'|` on the shifted interval ✓. The panels are
 in `s ∈ [10⁻⁶, 2]` (`u ∈ [10⁻⁶T, 2T]`), not "`[10⁻⁶, 2T]`" (A5).
* **New finding (A2).** `r8a_02` imports `r4a_lib` (which sets `iv.dps = 60`, `mp.dps = 80`) and then `r8a_lib` (which
 resets `iv.dps = 40`, `mp.dps = 50`). `LevyForm` is built afterwards, so `r4a_lib._constants` computes
 `iv.mpf(mp.nstr(mp.euler, 60)) + [−10⁻⁵⁵, 10⁻⁵⁵]` with `mp.euler` rounded to `mp.prec ≈ 169` bits: its 60 printed
 digits are wrong from about the 51st, so the true `γ` can lie up to `≈ 10⁻⁵¹` outside the guarded interval. The
 `C₀` used in `r8a_02` is therefore not a rigorous enclosure at the `10⁻⁵¹` level, and `r8a_02`'s own
 `certified_two_negative` flag is not by itself a proof. Effect on any entry `≤ ‖F‖²·10⁻⁵¹`, absorbed `10⁴²` times over
 by `r8a_03`'s `±10⁻⁹` inflation. (`r8a_lib.C0_interval` itself is fine: 45 digits against a `10⁻⁴³` guard at 50 dps.)
 Also `iv.dps` is 40, not 60, inside `r8a_02` — only widths. Consequence: **the lower-bound certificates of record
 are `r8a_03`'s, not `r8a_02`'s** — which the memo's proof of Theorem 5.1(ii) already cites; §3.2 must say why.
* Quadrature (lesson of `R155_024`): no Gauss–Legendre node enters any certified number. `r8a_01` uses exact moment
 series; `r4a_lib` integrates monomials exactly on each panel; the only GL rules (`leggauss(600)` in
 `gamma_fourier`, `leggauss(200)` for `h`) choose the test vectors `F, h`, which are then *exact* decimal
 polynomials whose values are enclosed independently. The `fine` grid's `m''` is float but only places edges. PASS.

### (viii) Lemma 3.3 and `r8a_03` (doubt 4) — PASS; re-run identical

Constants checked against the archived JSON: `max|F_k| = 0.870`, `‖F‖ = 1`, `|h_k| ≤ ‖g‖ ≤ 1.30`, so `|u_k| ≤ 2.2`,
`|δ_k| ≤ 2.5·10⁻¹⁶`; `Σ_{k<18}√(2k+1) ≈ 69` gives `‖δ‖_∞ ≤ 3·10⁻¹⁴` at `T ≥ 0.6`, and `‖δ'‖_∞ ≤ 4·10⁻¹²` ✓.
`∬_{I×I}(|x−y| + |x−y|²/2)/4 = 2T³/3 + T⁴/3 ≤ T²(2T + 2T²)` (the memo's bound is conservative) ✓; `∫κ = 2∫_0^∞K(u)
min(u,2T)du ≈ 10.3 ≤ 10.7` at `T = 0.9` ✓. `Lev(v) ≤ 2Lev(F) + 2Lev(h) ≤ 2(5.4 + 5.3) < 50` from the archived
`Γ[h] = −2.31…−3.76` (even) and `−0.037…−0.088` (odd) ✓. Total `≤ 10⁻¹⁰` per polarised entry ✓. Stored ends
`float(mp.mpf(x.a))` are round-to-nearest (`≤ 2·10⁻¹⁶` off); the `mp` subtraction `mp.mpf(lo) − mp.mpf(1e-9)` at
50 dps rounds to nearest too (`10⁻⁵⁰`); `1e-9` is a double near `10⁻⁹`. Required coverage `10⁻¹⁰ + 2·10⁻¹⁶ + 10⁻⁵¹`
(A2) `≪ 10⁻⁹` ✓. `r8a_03` re-run (0.1 s): `r8a_03_recheck.json` **identical** to the archived one (diff empty):
certified `0.60`, `log 2`, `0.80` even (`μ = 0.006627, 0.147170, 0.290056`) and `0.81`, `0.82` odd (`μ = 0.005124,
0.012368`); `0.90` odd out of range; `0.75`, `0.78`, `0.80` odd not certified. Smallest margin `0.005124 ≫ 10⁻⁹`.

### (ix) Lemma 4.1 (parity split) — PASS

For real even `F`, `F̂` is real and even; for real odd `F`, `F̂` is odd; `m` even, so `Γ(F_e,F_o) = (1/2π)∫mF̂_e\bar{F̂_o}
= 0`. `⟨F_e,g_0⟩ = (A+B)/2`, `⟨F_o,g_1⟩ = (A−B)/2` (the other pairings vanish by parity). `P_T = P_T^ev ⊕ P_T^odd`,
orthogonal for both `⟨·,·⟩` and `Γ`; indices add and bottoms take the minimum. Add the real/complex remark of (i) (A6).

### (x) Lemma 4.2 (zero extension) — PASS; "same form" confirmed

Zero extension `ι: L²(I_T) → L²(I_{T'})` is an isometry; `A(ιF) = A(F)`, `B(ιF) = B(F)` (integrals of the extended
function), parity preserved, so `ι(P_T^par) ⊂ P_{T'}^par` — the primitive constraints are preserved trivially, as the
brief says. The form is the **same** form: `Γ(F) = (1/2π)∫m|F̂|²` with `F̂` the transform of the zero extension on
`ℝ`, and `C₀‖F‖² + Lev(c_F)` depends on `F` only through `c_F` on `ℝ`; the form domain `{∫log(2+|τ|)|F̂|² < ∞}` is
`T`-free; and on `P_T` the paper's `\Ainf = 2AB + Γ_T` reduces to `Γ_T` for every `T` (`prop:arch(i)`: "`\Ainf` does
not depend on `T`"). So `n_par` is nondecreasing, `λ_par` nonincreasing, with no range condition at either window.

### (xi) Lemma 4.3 (strict monotonicity) — PASS (doubt 2 resolved)

* (0) Attainment: `Γ − C₀‖·‖² = Lev ≥ 0` closed, compact form-domain embedding (`prop:nodes(i)` proof); `P^par_{T'}` is
 closed in `L²` (`A, B` are `L²(I_{T'})`-continuous); minimising sequences converge in `L²` on a subsequence, the
 limit has norm 1 and lies in `P^par_{T'}`, lower semicontinuity gives attainment ✓.
* (1) Euler–Lagrange: `F*` (extended) attains `λ_par(T) = λ_par(T')` on `P^par_T`; first variation on `F* + εG`,
 `G ∈ P^par_T ∩ D(Γ)`, gives `Γ(F*,G) = λ⟨F*,G⟩` ✓.
* (2) **The constant `−½`.** Two independent derivations. (a) From `Lev[F] = ¼∬_{ℝ²}K(|x−y|)|F̃(x)−F̃(y)|²`
 (`prop:nodes(i)`: `2Lev = ½∬_{ℝ²}K|F̃(x)−F̃(y)|²`), polarisation gives `Lev(F,G) = ¼∬K(F(x)−F(y))(G(x)−G(y))`; with
 `FG ≡ 0` pointwise this is `−¼∬K[F(x)G(y) + F(y)G(x)] = −½∬K(|x−y|)F(x)G(y)`, absolutely convergent since
 `dist(supp F*, supp G₀) > 0` (difference of the two absolutely convergent integrals `Lev[F±G]`). (b) From `thm:A`:
 `Γ(F,G) = C₀⟨F,G⟩ + ∫_0^∞K(u)[⟨F,G⟩ − ½(c_{FG}(u) + c_{FG}(−u))]du`, `c_{FG}(u) = ∫F(t)G(t−u)dt`; with `⟨F,G⟩ = 0`
 this is `−½∫_ℝK(|u|)c_{FG}(u)du = −½∬K(|t−s|)F(t)G(s)` ✓. (The value of the constant is not load-bearing — only
 that it is nonzero.) `R`-invariance: `Γ(F*,RG₀) = Γ(RF*,G₀) = ±Γ(F*,G₀)` with the parity sign, so
 `Γ(F*,G₀ ± RG₀) = 2Γ(F*,G₀)` ✓; `⟨F*,G⟩ = 0` by disjoint supports ✓; `C₀⟨F*,G₀⟩ = 0` ✓.
* **Lagrange-multiplier step.** `G₀ ∈ C_c^∞(T',T)` with both `∫G₀e^{±y/2} = 0` makes `G = G₀ ± RG₀ ∈ P^par_T` (the
 sector needs only `∫G₀cosh(y/2) = 0` resp. `∫G₀sinh(y/2) = 0`; imposing both only shrinks the test class). Then
 `G₀ ↦ ∫ΦG₀` vanishes on `ker ℓ₊ ∩ ker ℓ₋`, hence equals `αℓ₊ + βℓ₋` on `C_c^∞(T',T)`, so `Φ = αe^{y/2} + βe^{−y/2}`
 as distributions, and pointwise since `Φ` is continuous there ✓.
* (3) Analyticity: for `y > T' ≥ x`, termwise (Tonelli, `Σ_k‖F*‖₁e^{−(2k+½)(y−T')} < ∞`)
 `Φ(y) = 2e^{−y/2}Σ_kc_kw^k`, `w = e^{−2y}`, radius `≥ e^{−2T'}`, so `Φ` is real-analytic on `(T',∞)` and the identity
 extends there; `Φ → 0`, `e^{y/2} → ∞` forces `α = 0`; the identity theorem in `w` gives `2c_0 = β`, `c_k = 0`
 (`k ≥ 1`); **`c_0 = ∫F*e^{x/2} = A(F*) = 0` because `F* ∈ P_{T'}`** — correct and essential (this is where the
 primitive constraint is used; on all of `L²` the argument would stop at `c_0 = β/2`, as it must, since the
 unconstrained problem has a different Lagrange structure). (4) `u = e^{2x}`: `c_k = ∫f(u)u^kdu`,
 `f = F*(½log u)u^{−3/4}/2 ∈ L¹` on a compact subinterval of `(0,∞)` ✓ (`e^{(2k+½)x} = u^{k+¼}`, `dx = du/(2u)`);
 Weierstrass gives `f = 0` ✓. Contradiction with `‖F*‖ = 1` ✓. Consequences (i)–(iii) ✓ (for (i), the `λ > 0` half
 uses only monotonicity and the definition of the supremum).

### (xii) Lemma 4.4 — PASS

`r = 0` certifies `L ≥ 0` on `ker ℓ ∩ L²_par`; `Γ[F*] − L[F*] = (1/2π)∫(m−s)|F̂*|² > 0` because `m − C₀ > 0` on
`0 < |τ| < 0.15` (`lem:mbounds(i)`) and `F̂*` is entire and `≢ 0` ✓.

### (xiii) Theorem 5.1 — PASS (machine-verified), certificates of record per A1/A2

Inputs: upper `r8a_01` re-runs (`0.58` par 0/1 `r = 0`; `log 2` par 1 `r = 0`; `0.90` par 0/1 `r = 1`); lower `r8a_03`
(`0.60` par 0; `0.81` par 1). (i)–(iv) follow exactly as written: `n_par ≤ 1` on `(0,0.90]` by Lemma 4.2;
`λ_par > 0` at `0.58` (both) and at `log 2` (odd) by Lemma 4.4; `λ_ev(0.60) < 0`, `λ_odd(0.81) < 0` by Prop 3.1 +
Lemma 4.3(ii); `T*_ev ∈ [0.58, 0.60]`, `T*_odd ∈ [log 2, 0.81]`, `T*_ev < T*_odd`; counts `0/1/2` on the three open
ranges by Lemma 4.3(i) and Lemma 4.1. Windows: `½log3 = 0.5493 < 0.58` ✓; `0.60`: `n_ev = 1`, `n_odd = 0` ✓;
`log 2`: `1 + 0` ✓; `0.80`: `1 + {0,1}` ✓; `0.81, 0.82, 0.90`: `1 + 1` ✓ (odd `≥ 1` from `0.81` via Lemma 4.2, so the
out-of-range `r8a_02 0.90` is correctly unused). Threshold points undecided and unused ✓.

### (xiv) Corollary 5.2 — PASS; consistency with the record

`0.58 ≤ T*_{∞,P} ≤ 0.60`; `λ^P_∞` strictly decreasing, `> 0` on `(0,T*)`, `< 0` on `(T*,∞)`; `λ^P_∞(½log3) > 0`.
Consistency: `R155_023:23–24,195` (amended per `R155_025`) records the Galerkin value `0.5958` (`[0.595781, 0.595859]`)
as an **upper bound** `T*_{∞,P} ≤ 0.5958`, DIAGNOSTIC; Paper 47 `main.tex:2438–2441` the same. `0.5958 ∈ [0.58, 0.60]`
✓; the certified upper bound `0.60` is *weaker* than the DIAGNOSTIC `0.5958`, which is expected (the lower-bound
certificate at `0.60` has `Γ[F] ≈ −0.0070`, consistent with a crossing just below `0.60`). `prop:arch(iv)`
(`≤ 0.74921`) improved ✓. The lower bound `0.58` promotes the DIAGNOSTIC "`0.58 < T*_{∞,P}`" of `R155_023 §7.3` /
`R155_025:190` to PROVED (machine-verified) (weakly: `≤` not `<`); the corpus had no prior certified lower bound
(`R155_031:117`) ✓.

### (xv) Corollary 5.3 — PASS, AMEND A6 (wording)

`(H1)` is `R155_039:245`: `n₋(\Ainf|P_T) = 1` on `(T*_{∞,P}, T₂]`. It holds for every `T₂ < T*_odd`, in particular
`T₂ = log 2`, and fails for every `T₂ > T*_odd`; `T₂ = T*_odd` is undecided. The sentence "every admissible `T₂`
satisfies `log 2 ≤ sup T₂ = T*_odd ≤ 0.81`" conflates `T₂` with its supremum; reworded. Replaces `T₂ ≤ 0.9989426`
(Paper 47 remark after `thm:J`) by `sup T₂ = T*_odd ≤ 0.81` ✓.

### (xvi) §5.4 table — PASS (arithmetic checked against the paper)

`thm:J` on `P_T`: `⌈2Tτ₀/π⌉ − 3` with `2Tτ₀/π = 2.1996, 2.7755, 3.2033, 3.2433, 3.6037` at `½log3, log 2, 0.80,
0.81, 0.90` → `0, 0, 1, 1, 1` ✓. `cor:P3`: `5, 7, 8` proved, DIAGNOSTIC `5, 6, 7` ✓. `rem:P4`: floor `5` of the two-value
relaxation at `log 2` ✓; the memo's reading (multi-band minorant handled exactly on 22 modes, Ky Fan only in the
far tail) is accurate and does not contradict `rem:P4`, which is scoped to the two-value relaxation (`R155_048`
Caveat 1).

### (xvii) §6, labels, runtime — PASS

`n_odd(0.80)` OPEN, the `τ_N`-attribution DIAGNOSTIC (three runs), the `e_∞` extrapolation HEURISTIC: labels
correct. The Galerkin odd bottoms are upper bounds on `λ_odd` only up to the float constraint (`⟨F,g⟩ ≈ 1.7·10⁻¹⁵`,
not `0`) — DIAGNOSTIC is the right label. Runtime: every `r8a_01` run is `13–14 s` uncontended (re-runs above);
the 87–106 s archive figures were contention, as the memo says.

---

## Verdicts

| statement (`R155_052`) | verdict | label after audit |
|---|---|---|
| Notation vs Paper 47 (`m`, `C₀`, `K`, `A`, `B`, `P_T`, `\Ainf`, `\laminfP`, `Γ_T`, `S_c`, `Λ_k`) | PASS | — |
| Lemma 2.1 (bordered inertia) | PASS | PROVED |
| Lemma 2.2 (multi-band minorant, `0 ≤ M ≤ WS_{c_*}`) | **AMEND** (A3 tolerance argument; A5 edge count) | PROVED |
| Lemma 2.3 (`m''` summand dominates; endpoint sup covers the band) | PASS | PROVED |
| Prop 2.4(a)–(c),(e) | PASS (A4 wording) | PROVED |
| Prop 2.4(d) (sign `+`; perturbation `≤ 10⁻³³`) | PASS, **AMEND** (A1: superseded by the re-run; A4 `6.1·10⁻³⁴`) | PROVED (now a remark) |
| Re-run of the 8 archived `r8a_01` cases | PASS, bit-identical | — |
| Prop 3.1 (explicit negative plane), `T < 0.88137` | PASS | PROVED (machine-verified) |
| §3.2 enclosures (`r4a_lib`, primes off, pole unused, `Γ_T` not `W_T`) | **AMEND** (A2 `C₀` guard; A5 panel domain) | — |
| Lemma 3.3 (polarisation rounding `≤ 10⁻¹⁰`) | PASS | PROVED |
| `r8a_03` (`±10⁻⁹` recheck), re-run | PASS, identical | certificate of record for all lower bounds |
| Lemma 4.1 (parity split) | PASS (A6 real/complex remark) | PROVED |
| Lemma 4.2 (monotonicity by zero extension; same form) | PASS | PROVED |
| **Lemma 4.3** (strict monotonicity) | **PASS** | **PROVED** |
| Lemma 4.4 (`r = 0` ⇒ `λ > 0`) | PASS | PROVED |
| **Theorem 5.1** | **PASS** | **PROVED (machine-verified)** |
| **Corollary 5.2** (`0.58 ≤ T*_{∞,P} ≤ 0.60`; `\laminfP(½log3) > 0`) | **PASS** | **PROVED (machine-verified)** |
| **Corollary 5.3** (`(H1)` at `T₂ = log 2`; `sup T₂ = T*_odd ∈ [log2, 0.81]`) | PASS, **AMEND** (A6 wording) | **PROVED (machine-verified)** |
| §5.4 table | PASS | PROVED (arithmetic) |
| `n_odd(0.80)`; `(H1)` at `0.80` | PASS | OPEN |
| §6 attribution / extrapolation / Galerkin bottoms | PASS | DIAGNOSTIC / HEURISTIC / DIAGNOSTIC |

**No FAIL.**

## Mandatory fixes (all applied in place to `R155_052`, marked "[amended per R155_061]")

* **A1** (§0 item 6, §2.4(d), §5.1 proof, §7, §8, §9, footer): certificates of record for the upper bounds are the
 eight `r8a_01_<T>_par<p>_rerun.json` of the corrected script (bit-identical to the archive, 13–14 s each); §2.4(d)
 becomes a remark; the references "Lemma 2.4" are corrected to "Prop 2.4(d)".
* **A2** (§3.2, §3.3, §9): `r4a_lib`'s `C₀` guard `±10⁻⁵⁵` is not rigorous under `r8a_02`'s import order (`mp.dps =
 50`, error up to `≈ 10⁻⁵¹`); `r8a_02`'s flag is not a proof by itself; `r8a_03` (`±10⁻⁹`) is the certificate of
 record for every lower bound. Note `iv.dps = 40` in `r8a_02`.
* **A3** (§2.2): the argument that `s ≤ c_N` holds exactly (the script's `1e-30` tolerance is only interval slack at
 the right end of the last band).
* **A4** (§2.4(d),(e)): `‖E‖_F ≤ 6.1·10⁻³⁴` (say `≤ 7·10⁻³⁴`); "`U` converted exactly" → decimal-enclosed.
* **A5** (§2.2, §3.2): 8 geometric edges `9, …, τ_N`; `c_* ≈ 16`; panels in `s ∈ [10⁻⁶,2]`.
* **A6** (§4.1, §5.3): real/complex remark; the `sup T₂` sentence reworded.

`scripts/r8a/README.md` gets a short "audit re-runs" section (new files only). Paper 47 and the phase README are not
touched.

## What is cleared for Paper 47 (§9.2 `subsec:negindex`, with two items for §9.1 `subsec:arch`)

Cleared, with the proposed LaTeX labels:

1. **`lem:parity`** — Lemma 4.1: `P_T = P_T^{ev} ⊕ P_T^{odd}`, orthogonal for `L²` and `Γ_T`; `n₋(\Ainf|P_T) =
 n_{ev} + n_{odd}`, `\laminfP = min(λ_{ev}, λ_{odd})`. **PROVED.** (§9.2.)
2. **`lem:strict`** — Lemma 4.3: `λ_{ev}`, `λ_{odd}` and `\laminfP` are strictly decreasing on `(0,∞)`, the bottoms are
 attained, and `λ_par(T) < 0 ⟺ n_par(T) ≥ 1`. **PROVED.** (Best placed in §9.1 as `prop:arch(v)` or right after it;
 it upgrades `prop:arch(i)` "nonincreasing" to strict.)
3. **`thm:index`** — Theorem 5.1 (i)–(iv) as amended: `n₋(\Ainf|P_T) = 0` on `(0,T*_{ev})`, `= 1` on
 `(T*_{ev},T*_{odd})`, `= 2` on `(T*_{odd}, 0.90]`, with `0.58 ≤ T*_{ev} ≤ 0.60`, `log 2 ≤ T*_{odd} ≤ 0.81`;
 `n₋ = 1` at `0.60` and `log 2`, `n₋ = 2` at `0.81, 0.82, 0.90`, `n₋ ∈ {1,2}` at `0.80`. **PROVED (machine-verified)**
 — method lemmas 2.1–2.3, Prop 2.4, Prop 3.1, Lemma 3.3, Lemma 4.2, Lemma 4.4 go with it (the enclosure details
 belong in `app:encl`); certificates: the `r8a_01` re-runs and `r8a_03`. (§9.2, after `prop:NC`, replacing "the
 hypothesis that `n₋ = 1` … is not proved here".)
4. **`cor:Tarch`** — Corollary 5.2: `0.58 ≤ T*_{∞,P} ≤ 0.60`, and `\Ainf` is positive definite on `P_{½log3}`
 (`\laminfP(½log3) > 0`; the value `≈ 0.083` stays DIAGNOSTIC). **PROVED (machine-verified).** (§9.1, as
 `prop:arch(iv′)`; the text at `main.tex:2438–2446` must then keep `0.5958` as DIAGNOSTIC upper bound and turn
 "positive on `P_T` by itself" at `½log3` into a proved sign.)
5. **`cor:H1`** — Corollary 5.3 as amended: `(H1)` holds for every `T₂ < T*_{odd}`, in particular `T₂ = log 2`, fails
 for every `T₂ > T*_{odd}`; `sup T₂ = T*_{odd} ∈ [log 2, 0.81]`. **PROVED (machine-verified).** (§9.2, the remark
 after `thm:J`: `0.81` in place of `0.9989426`.)
6. A one-sentence addendum to **`rem:P4`**: the multi-band relaxation, with an exact 22-mode section and a Ky Fan tail,
 returns the exact count `1` at `log 2`. **PROVED** (as a statement about the method, via item 3).

Not cleared (stay out of the paper or enter only with their labels): `n_odd(0.80)` and `(H1)` at `0.80` (OPEN); the
`τ_N`-attribution of the `0.80` residual (DIAGNOSTIC); `e_∞ ≈ +0.0037`, "`τ_N ≈ 60` certifies" (HEURISTIC); Galerkin
bottoms and the crossing in `(0.80,0.81)` (DIAGNOSTIC); `r8a_02` at `0.90` (outside `T < 0.88137`, not certified,
not needed). When inserting, check every sentence against `\PT`, `\Ainf`, `\laminfP` and `prop:arch` as printed
(rule); the row-D label and the endpoint of record (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`) are unchanged,
and nothing here is a statement about `W_T` or the zeros of `ζ`.

[note per TEX_HOSTILE_REVIEW_R4 item 4] The remark above that "on all of `L²` the argument would stop at `c_0 = β/2`" is wrong, and the clause "`c_0 = A(F*) = 0` … correct and essential" is not essential: `c_k = 0` for all `k ≥ 1` already gives `∫(uf(u))u^j du = 0` for all `j ≥ 0`, hence `uf = 0` by Weierstrass, so strictness holds also for `λ_∞` and for the bottom of `Γ_T` on `L²(I_T)`; the editor's omission of the remark from Paper 47 was right (applied in `lem:strict` per R4-12).
