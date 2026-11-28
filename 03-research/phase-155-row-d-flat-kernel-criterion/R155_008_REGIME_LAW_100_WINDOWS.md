# R155.008 — The regime law over 103 windows `T ∈ [½log3, 1.20]`

* REVERSE-ENGINEERING track of phase 155. request: "ya sabiendo cómo
son las rows A/B/C y cómo debería ser D, busquemos 100 casos donde ya sabemos que RH se cumple, y
veamos cuál es el patrón que tienen, porque ese patrón lo podemos extrapolar sí o sí."*
*Faithful form: the known truth is Odlyzko's table of zeros; by Theorem Z (Paper 46 §7) the certificate
at window `T` is the flat-top weight `w_T` with `f_w(τ) = Σ_ρ ŵ(τ−γ_ρ) =` prime/Γ side. Map ~100
windows across all prime-entry regimes and extract the pattern.*
*Inherits `R155_005` and every repair required by its audit `R155_006` (ACCEPT WITH REPAIRS).*
*Scripts, data, exact commands and runtimes: `scripts/reverse/regime/` (README), table
`scripts/reverse/regime_table.csv`.*
**Every measured number in this file is `DIAGNOSTIC`. The four propositions of §7 and the lemma of
§7bis are `PROVED` and use no zeros. Nothing here is a statement about RH, and no sign is claimed for
any `T > log 2`.**

## §0 Verdict (five lines)

1. **There is a pattern, it is exact, and it is provable without any zeros: the entry law.**
 `A_T = Σ_{n<e^{2T}} v_n` jumps by exactly `v_n = 2Λ(n)/√n` at `T = ½log n`, so the verification
 threshold `τ_env = 2πe^{A_T}` is multiplied by exactly `e^{v_n}` there and the difficulty index is
 the closed formula `D(T) = τ_env/2πe^{2T} = e^{A_T−2T}` — no computation needed. Measured against
 103 windows and 7 entries (`n = 4,5,7,8,9,11`; `n=3` is the left endpoint): **7/7 ratios agree to 5
 significant figures** (`2.0000, 4.2187, 4.3535, 1.6325, 2.0801, 4.2460`).
2. **The other half of the pattern is the opposite of what `R155_005` reported: at a fixed verification
 domain the value is CONTINUOUS across every prime entry** (measured ratios `0.999 … 1.011` at the six
 entries inside the range), and that continuity is `PROVED` in §7 (Prop. C) from Theorem Z: no term of
 the prime/Γ side jumps, because `w(log n)` is continuous at `log n = 2T` (`w` is flat-topped, `w(2T)=1`).
 `R155_005`'s "`c(T)` is a step function of `N_T`" was an artefact of letting the LP domain move with
 `τ_env`. **What jumps at a prime entry is the length of the interval on which the certificate must be
 checked, never the certificate problem's data.**
3. **The reverse-engineered profile is universal.** At the fixed budget `L = 20` the optimal weight is
 the *same* non-negative monotone shoulder at all 103 windows and in all 8 regimes:
 `‖w‖_∞ = 1.0002 ± 0.0014`, `∫_{2T}^∞ w = ∫|w| = 3.128 ± 0.067`, decay rate `0.173 ± 0.014`,
 half-height at `v = 2.90 ± 0.14`, `0–3` sign changes, `23.8 ± 1.7` contacts; every window's profile is
 within `0.1332` (sup norm), mean `0.0599`, of one global mean profile [amended per
 R155_010: corrects `0.0785`, a 17-point sampling artefact — R155_009 §4(A)]
 `w(2T+v) = 1.000, 0.859, 0.790, 0.735, 0.662, 0.569, 0.494, 0.427, 0.342, …` (`v = 0, ½, 1, …`).
4. **The honest extrapolation test now passes for the profile and for the value, and it predicts
 failure.** Training inside regime `k` and predicting the first window of regime `k+1` (never
 re-optimising): profile sup error `0.021–0.055` on a profile of sup norm `1`, value error
 `0.3–11 %` (affine) and `0.2–1.1 %` (last value). **The sign is kept in 6/6 predictions — and the
 sign is negative every time.** The pattern extrapolates; what it extrapolates is that this class
 never produces a certificate.
5. **The wall is the domain, and the cap hides it.** With the LP domain capped at `τ ≤ 60` the value
 drifts smoothly `−1.8·10⁻² → −2.9·10⁻¹` over the whole range. Re-evaluating the *same* certified
 weight on its true interval `[0, τ_env]` costs a further factor `2.4` at `|N_T| = 3`
 (`−7.13·10⁻² → −1.74·10⁻¹`, argmin `τ = 73.1`) and `4.6` at `|N_T| = 4`
 (`−1.39·10⁻¹ → −6.45·10⁻¹`, argmin `τ = 484.7`), always near the right end. The difficulty is
 `D(T) = e^{A_T−2T}`, which runs `0.89 → 455.8` across our range.

## §1 Corpus check

`grep -rin` over `03-research`, `04-papers`, `05-meta-and-planning`, `scripts`.

| term | hits | reading |
|---|---|---|
| `100 windows`, `tau_env` (as a scanned variable) | only this deliverable's own scripts | the sweep is new |
| `regime` | `phase-118/RESUME.md`, `phase-137/R137_001b`, `phase-137/R137_003`, several scripts | all are "asymptotic regime"/"density regime"; **no prime-entry regime decomposition of a window scan** |
| `prime entry` | `phase-155/R155_005`, `R155_006`, `README`; `phase-120/P3_FROBENIUS_SEAM`, `phase-114/114_d_81` (unrelated senses) | the notion exists only in `R155_005`/`R155_006`, and there only qualitatively ("the problem changes kind at a prime entry") |
| `difficulty index` | `R155_005`, `R155_006`, `PLAN.md` | `τ_env/2πe^{2T}` is `R155_005`'s; **no closed form for it is anywhere in the corpus** — §7 (N2) supplies one |
| `tscan`, `sweep over T` | `phase-153/R153_008` (`q2_tscan.py`, parity-resolved tip scan of a *model*), `phase-154/R154_001` (`tscan.py`, `λ(T)` for the primal LP, `K = 200`, `h = 0.002`) | the closest precedents. Both scan `T` on the **primal** side (eigenvalue of `A_T`), on a lattice-LP model, and neither decomposes by `N_T` nor fits a law per regime. `R154_001:181` even asks whether `λ(T)` has a kink at `½log(32/9)` — the same question this file answers structurally (Prop. C: no kink in the data; the kink is in `τ_env`) |
| `jump law`, `extrapolación entre regímenes` | none | new |
| `shoulder` | `R155_005`, `R155_006`, `PLAN.md` | the shape reading is `R155_005`'s; its **universality in `T`** is new here |
| `Krein`, `Suzuki` | `04-papers/47/main.tex:242–243, 1366–1370` (screw-function programme, related work) | the §7bis toy-universe statement is a remark on that literature, not a new theorem |
| circularity no-go | `phase-4-krein-space-realization/proofs/00-PROOF-LOG.md:168` ("Zero-side `K` presupposes the unknown zeros (circular as tool)"), `phase-136-row-d-map/MAP_1_WALLS_AND_MASTER_DOCS.md:141` (ES-2) | respected by labelling throughout; see §8 |

Conclusion: the entry law, the closed form for the difficulty index, the continuity proposition, the
rigidity lemma and the per-regime fits are not in the corpus. The `w`-side LP machinery is
`R155_005`'s and is reused, not rewritten.

## §2 Method, with the audit repairs

### 2.1 The class, fixed once for all 103 windows

`w ≡ 1` on `[−2T,2T]`; for `u > 2T` (even extension)

```
w(u) = Σ_{i=1..4} y_i ψ_{s_i}(u−2T) + Σ_{j=2..31} x_j β((u−u_j)/h),
ψ_s(v) = (1 + s v + ½ s²v²) e^{−sv}, s ∈ {2.5, 4, 8, 16},
β = cardinal cubic B-spline (C², support 4h, ∫ = h), u_j = 2T + j h, h = 0.25 FIXED.
```

`Σ_i y_i = 1` is an equality constraint of every LP, so `w` is **C² across the window edge** and
`ŵ(t) = O(t⁻⁴)` (audit repair: `≥ C¹` required; C² obtained). Support `U = 2T + 8.25`.

**Why `h` is fixed and not `2T/M`.** `R155_006 §5` rejects comparing a coefficient budget `L` across
windows when the lattice step `h = 2T/M` moves with `T`. Here `h`, the number of nodes and the four
edge scales are `T`-independent, so in the variable `v = u − 2T` the admissible set is *literally the
same* at every window; only the edge position `2T` moves. In addition every run reports the true norms
`‖w‖_∞` and `∫|w|`, which is what §3/§4 compare.

Budget `Σ_i|y_i| + Σ_j|x_j| ≤ L`, with `L = 20` (primary) and `L = 5` (a tame control) at every window.

### 2.2 The LP (it never sees the primes)

Maximise `c` subject to `f^known_w(τ_i) = Σ_{|γ|≤Γ} ŵ(τ_i−γ) ≥ c` on `τ_i ∈ [0, τ_max]`, step `0.02`,
`τ_max = min(τ_env, 60)`, plus `Σ y_i = 1` and the budget. `69` variables, `≤ 3002` rows, HiGHS, `0.3 s`.

### 2.3 How many zeros (audit repair: state and measure the far-zero residual)

`resid_check.py`: optimise at `Γ = 800` and re-evaluate the same weight at `Γ = 400, 800, 2000, 6000,
20000` (`202 … 22 491` zeros), **run at the single window `T = 0.62` only** [amended per
R155_010: R155_009 notes `resid_check.py` was quoted as justifying `Γ = 800` across all 103 windows
but is a one-window probe]. `min f` moves by `6·10⁻⁸` from `Γ = 400` to `Γ = 800` and by `4.7·10⁻⁹`
from `Γ = 800` to `Γ = 20000` at `T = 0.62`; this single-window measurement is what is available, not
a bound established at every window. **The whole 103-window run uses the 491 zeros below
`γ = 800`**, and that is a consequence of the C² edge (`ŵ = O(t⁻⁴)`, `R155_005 §3.2`), not of luck.
`τ_env ≤ 31 535 < 74 920.83` at every window, so the table would in principle reach the whole
verification interval; it is the `τ`-grid, not the zeros, that forces the cap of §2.2.

### 2.4 Certification of every reported value (audit repairs 2 and 4)

*Grid.* LP on a `0.02` grid; every value re-evaluated on a `0.005` grid refined around the low band
(`c_fine` in the table). Measured inflation `c_LP − c_fine = 8.1·10⁻⁴ ± 3.3·10⁻⁴` over the 103
windows — **not** the factor `2` of `R155_005 §3.1(3)` nor the `58×` the audit measured, because
these weights are tame (`‖w‖_∞ = 1.000`); grid exploitation is a property of the wild weights the
budget here forbids.

*Bernstein grid lemma.* `f_w` is band-limited of exponential type `U`, so `‖f''‖_∞ ≤ U²‖f‖_∞` and
`min_ℝ f ≥ min_{δ-grid} f − ½U²‖f‖_∞δ²`. With `δ = 0.005` the slack is `0.0133 ± 0.0022`, an order of
magnitude below `|c|`; `c_cert = c_fine − slack` is in the CSV and is negative at every window by a
margin of at least `5·10⁻³`. **Every negative reading in this file is certified in this sense.**

*Both sides (audit repair: no reading without the prime side).* `crosscheck_regime.py`, one window per
regime, Gauss–Legendre order **800** on the B-spline `K`- and `cosh`-integrals:

| `T` | `N_T` | `max_τ |f^{zero} − f^{prime}|` | `min f^{prime}` | `min f^{zero}` |
|---|---|---|---|---|
| `0.5493` | `{2}` | `2.58e−7` | `−1.81128e−2` | `−1.81127e−2` |
| `0.5498` | `{2,3}` | `2.48e−7` | `−5.78649e−2` | `−5.78651e−2` |
| `0.6936` | `{2,3,4}` | `3.22e−7` | `−7.14486e−2` | `−7.14486e−2` |
| `0.8052` | `{2,3,4,5}` | `7.90e−7` | `−1.38752e−1` | `−1.38752e−1` |
| `0.9735` | `{..,7}` | `1.03e−6` | `−2.10998e−1` | `−2.10998e−1` |
| `1.0402` | `{..,8}` | `1.30e−6` | `−2.11951e−1` | `−2.11949e−1` |
| `1.0991` | `{..,9}` | `4.60e−7` | `−2.34435e−1` | `−2.34435e−1` |
| `1.1994` | `{..,11}` | `2.82e−6` | `−2.91149e−1` | `−2.91149e−1` |

Theorem Z is thus verified numerically **across all eight prime regimes** (`R155_005` verified it at one
window; the audit confirmed the normalisation line by line). Nothing positive was found, so the
"no positive reading unless certified by both sides" rule is not exercised.

**One new numerical fact, and it is a trap worth recording.** Taking the prime sum only up to
`e^U` (which `R155_005`/`revlib2` do, on the ground that the B-splines are compactly supported) leaves
a systematic `1.60·10⁻⁴` disagreement between the two sides — *larger than `λ_min(A_{½log3}) =
8.86·10⁻⁵`*. The cause is that the **`ψ_s` edge functions are not compactly supported**, and the LP
uses them with large cancelling coefficients (`y = (5.17, −5.66, 1.78, −0.30)` at `½log3`), so the
`n^{-s-1/2}` tail of the prime sum is amplified. Measured at `½log3`: cutting the prime powers at
`e^U = 11 487`, `4·10⁴`, `1.5·10⁵`, `6·10⁵` gives `1.60·10⁻⁴, 1.71·10⁻⁵, 1.54·10⁻⁶, 1.16·10⁻⁷`.
All runs here use `6·10⁵` (`49 298` prime powers). Raising the Gauss–Legendre order `200 → 800 → 3000`
changes nothing at this `h`, so this is a *different* artefact from the one the audit found, and it
is larger.

### 2.5 Fitting discipline (audit repair 3)

Every fit in §4 and every extrapolation in §6 is performed **inside one prime regime** and tested on
the first window of the next. No training set straddles an entry.

## §3 The 103 windows

Full table: `scripts/reverse/regime_table.csv` (103 rows, 28 columns) and
`scripts/reverse/regime/regime_windows.json` (adds `y`, `x`, the contact sets). Grid: 69 equally
spaced `T` in `[½log3, 1.20]` plus 6 windows clustered around each of the seven entries
(`−0.020, −0.008, −0.002, +0.0005, +0.003, +0.010`), de-duplicated at `5·10⁻⁴`.
Columns: `T, N_T, A_T, τ_env, 2πe^{2T}, index, τ_max, capped, env_below_table, c_lp, c_fine, c_cert,
bern, mass, absmass, winf, rate, half, centroid, last_node, sign_changes, ncontacts, argmin` and the
four `L = 5` columns. Excerpt (31 of 103 rows; every regime boundary is shown as the pair
below/above):

| `T` | `N_T` | `A_T` | `τ_env` | `2πe^{2T}` | `D(T)` | `τ_max` | `c_LP` | `c_fine` | Bern | `‖w‖_∞` | `∫w` | rate | contacts | `c_fine(L=5)` |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `0.549306` | `2` | `0.9803` | `16.75` | `18.85` | `0.89` | `16.75` | `−1.8088e−2` | `−1.8498e−2` | `0.010` | `1.011` | `3.076` | `0.163` | `19` | `−3.0120e−2` |
| `0.549806` | `2,3` | `2.2488` | `59.54` | `18.87` | `3.16` | `59.54` | `−5.7792e−2` | `−5.8619e−2` | `0.010` | `1.000` | `3.160` | `0.170` | `22` | `−1.0007e−1` |
| `0.578013` | `2,3` | `2.2488` | `59.54` | `19.96` | `2.98` | `59.54` | `−5.7959e−2` | `−5.8467e−2` | `0.010` | `1.000` | `3.055` | `0.185` | `25` | `−9.7039e−2` |
| `0.625858` | `2,3` | `2.2488` | `59.54` | `21.97` | `2.71` | `59.54` | `−6.5990e−2` | `−6.6216e−2` | `0.011` | `1.000` | `3.196` | `0.176` | `24` | `−1.1369e−1` |
| `0.673147` | `2,3` | `2.2488` | `59.54` | `24.15` | `2.47` | `59.54` | `−6.9532e−2` | `−6.9986e−2` | `0.011` | `1.000` | `3.076` | `0.197` | `24` | `−1.1604e−1` |
| `0.692842` | `2,3` | `2.2488` | `59.54` | `25.12` | `2.37` | `59.54` | `−7.1385e−2` | `−7.1831e−2` | `0.011` | `1.000` | `3.080` | `0.190` | `21` | `−1.1718e−1` |
| `0.693647` | `2,3,4` | `2.9420` | `119.09` | `25.16` | `4.73` | `60.00` | `−7.1310e−2` | `−7.1755e−2` | `0.011` | `1.000` | `3.080` | `0.190` | `22` | `−1.1717e−1` |
| `0.711980` | `2,3,4` | `2.9420` | `119.09` | `26.10` | `4.56` | `60.00` | `−7.0112e−2` | `−7.0514e−2` | `0.011` | `1.000` | `3.134` | `0.184` | `26` | `−1.2319e−1` |
| `0.759825` | `2,3,4` | `2.9420` | `119.09` | `28.72` | `4.15` | `60.00` | `−8.4843e−2` | `−8.5332e−2` | `0.011` | `1.000` | `3.007` | `0.187` | `22` | `−1.8263e−1` |
| `0.796719` | `2,3,4` | `2.9420` | `119.09` | `30.92` | `3.85` | `60.00` | `−1.3301e−1` | `−1.3384e−1` | `0.012` | `1.000` | `3.198` | `0.151` | `24` | `−2.3272e−1` |
| `0.802719` | `2,3,4` | `2.9420` | `119.09` | `31.29` | `3.81` | `60.00` | `−1.3670e−1` | `−1.3750e−1` | `0.013` | `1.000` | `3.219` | `0.148` | `24` | `−2.3256e−1` |
| `0.805219` | `2,3,4,5` | `4.3815` | `502.39` | `31.45` | `15.98` | `60.00` | `−1.3829e−1` | `−1.3908e−1` | `0.013` | `1.000` | `3.231` | `0.145` | `26` | `−2.3279e−1` |
| `0.814719` | `2,3,4,5` | `4.3815` | `502.39` | `32.05` | `15.67` | `60.00` | `−1.4533e−1` | `−1.4585e−1` | `0.013` | `1.000` | `3.232` | `0.165` | `22` | `−2.3475e−1` |
| `0.855515` | `2,3,4,5` | `4.3815` | `502.39` | `34.78` | `14.45` | `60.00` | `−1.4376e−1` | `−1.4443e−1` | `0.013` | `1.000` | `3.143` | `0.190` | `22` | `−2.3454e−1` |
| `0.903360` | `2,3,4,5` | `4.3815` | `502.39` | `38.27` | `13.13` | `60.00` | `−1.4192e−1` | `−1.4268e−1` | `0.013` | `1.000` | `3.066` | `0.186` | `23` | `−2.4325e−1` |
| `0.951205` | `2,3,4,5` | `4.3815` | `502.39` | `42.11` | `11.93` | `60.00` | `−1.8607e−1` | `−1.8756e−1` | `0.014` | `1.000` | `3.150` | `0.154` | `24` | `−3.3966e−1` |
| `0.970955` | `2,3,4,5` | `4.3815` | `502.39` | `43.81` | `11.47` | `60.00` | `−2.0826e−1` | `−2.0946e−1` | `0.014` | `1.000` | `3.219` | `0.181` | `26` | `−3.4854e−1` |
| `0.973455` | `{..,7}` | `5.8525` | `2187.13` | `44.03` | `49.68` | `60.00` | `−2.0982e−1` | `−2.1100e−1` | `0.014` | `1.000` | `3.241` | `0.179` | `24` | `−3.4972e−1` |
| `0.989481` | `{..,7}` | `5.8525` | `2187.13` | `45.46` | `48.11` | `60.00` | `−2.0741e−1` | `−2.0803e−1` | `0.015` | `1.000` | `3.241` | `0.163` | `25` | `−3.5149e−1` |
| `1.027758` | `{..,7}` | `5.8525` | `2187.13` | `49.08` | `44.57` | `60.00` | `−2.0923e−1` | `−2.1041e−1` | `0.015` | `1.000` | `3.098` | `0.166` | `23` | `−3.5386e−1` |
| `1.037327` | `{..,7}` | `5.8525` | `2187.13` | `50.03` | `43.72` | `60.00` | `−2.1058e−1` | `−2.1128e−1` | `0.015` | `1.000` | `3.083` | `0.165` | `22` | `−3.5442e−1` |
| `1.040221` | `{..,8}` | `6.3426` | `3570.55` | `50.32` | `70.96` | `60.00` | `−2.1079e−1` | `−2.1195e−1` | `0.015` | `1.000` | `3.090` | `0.163` | `23` | `−3.5470e−1` |
| `1.046896` | `{..,8}` | `6.3426` | `3570.55` | `50.99` | `70.02` | `60.00` | `−2.1125e−1` | `−2.1263e−1` | `0.015` | `1.000` | `3.064` | `0.161` | `23` | `−3.5575e−1` |
| `1.078612` | `{..,8}` | `6.3426` | `3570.55` | `54.33` | `65.72` | `60.00` | `−2.2587e−1` | `−2.2692e−1` | `0.015` | `1.000` | `3.057` | `0.170` | `22` | `−3.6036e−1` |
| `1.096612` | `{..,8}` | `6.3426` | `3570.55` | `56.32` | `63.39` | `60.00` | `−2.3281e−1` | `−2.3392e−1` | `0.015` | `1.000` | `3.053` | `0.172` | `27` | `−3.6700e−1` |
| `1.099112` | `{..,9}` | `7.0750` | `7427.04` | `56.61` | `131.21` | `60.00` | `−2.3329e−1` | `−2.3444e−1` | `0.015` | `1.000` | `3.050` | `0.171` | `27` | `−3.6818e−1` |
| `1.123448` | `{..,9}` | `7.0750` | `7427.04` | `59.43` | `124.97` | `60.00` | `−2.3382e−1` | `−2.3492e−1` | `0.016` | `1.000` | `3.084` | `0.170` | `25` | `−3.8777e−1` |
| `1.171293` | `{..,9}` | `7.0750` | `7427.04` | `65.40` | `113.57` | `60.00` | `−2.5991e−1` | `−2.6128e−1` | `0.017` | `1.000` | `3.248` | `0.155` | `26` | `−4.4498e−1` |
| `1.196948` | `{..,9}` | `7.0750` | `7427.04` | `68.84` | `107.89` | `60.00` | `−2.9019e−1` | `−2.9113e−1` | `0.017` | `1.000` | `3.177` | `0.160` | `25` | `−4.6967e−1` |
| `1.199448` | `{..,11}` | `8.5210` | `31535.46` | `69.18` | `455.82` | `60.00` | `−2.9066e−1` | `−2.9160e−1` | `0.017` | `1.000` | `3.166` | `0.161` | `24` | `−4.7125e−1` |
| `1.200000` | `{..,11}` | `8.5210` | `31535.46` | `69.26` | `455.32` | `60.00` | `−2.9076e−1` | `−2.9169e−1` | `0.017` | `1.000` | `3.162` | `0.161` | `24` | `−4.7161e−1` |

`env_below_table = 1` at all 103 windows (`τ_env ≤ 31 535 < 74 920.83`). `capped = 1` from the entry
of `4` on (`τ_env > 60`), i.e. at 79 of the 103 windows; see §5.3 for what the cap costs.
**Every value is negative, at every window, at both budgets, before and after certification.** This
class is far weaker than the corpus's certified endpoint `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`
(Paper 46 Thm. C), which is the honest comparison and the reason nothing here touches the label.

## §4 The law inside each regime

`fit_regime.py`, `L = 20`, fits performed only inside a regime.

| `|N_T|` | `N_T` | windows | `T` range | `c_fine` range | affine-in-`T` residual, value | affine residual, profile (sup) | `∫w` | `‖w‖_∞` | rate | contacts |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `{2}` | 1 | `0.5493` | `−1.850e−2` | — | — | `3.076` | `1.011` | `0.163` | `19` |
| 2 | `{2,3}` | 20 | `0.5498–0.6928` | `−7.200e−2 … −5.790e−2` | `1.70e−3` | `0.044` | `3.110 ± 0.046` | `1.000` | `0.18 ± 0.01` | `21–25` |
| 3 | `{2,3,4}` | 17 | `0.6936–0.8027` | `−1.375e−1 … −7.051e−2` | `1.50e−2` | `0.041` | `3.118 ± 0.055` | `1.000` | `0.17 ± 0.02` | `22–26` |
| 4 | `{2,3,4,5}` | 23 | `0.8052–0.9710` | `−2.095e−1 … −1.391e−1` | `2.65e−2` | `0.128` | `3.147 ± 0.063` | `1.001` | `0.18 ± 0.02` | `21–27` |
| 5 | `{..,7}` | 12 | `0.9735–1.0373` | `−2.117e−1 … −2.072e−1` | `2.53e−3` | `0.044` | `3.181 ± 0.070` | `1.000` | `0.17 ± 0.01` | `22–26` |
| 6 | `{..,8}` | 12 | `1.0402–1.0966` | `−2.339e−1 … −2.120e−1` | `3.24e−3` | `0.037` | `3.071 ± 0.018` | `1.000` | `0.16 ± 0.01` | `22–27` |
| 7 | `{..,9}` | 16 | `1.0991–1.1969` | `−2.911e−1 … −2.341e−1` | `1.86e−2` | `0.062` | `3.138 ± 0.086` | `1.000` | `0.16 ± 0.01` | `24–27` |
| 8 | `{..,11}` | 2 | `1.1994–1.2000` | `−2.917e−1 … −2.916e−1` | — | — | `3.164` | `1.000` | `0.16` | `24` |

**(A) The profile law.** The affine-in-`T` model fits the profiles to `0.037–0.128` in sup norm on a
profile of sup norm `1`, i.e. `4–13 %` — the audit's in-regime rerun of `R155_005` obtained `0.041`,
and this reproduces it across all six fittable regimes. But the stronger statement is that **the
affine term is barely needed**: the deviation of *every one* of the 103 windows from a single global
mean profile is at most `0.1332`, mean `0.0599` [amended per R155_010: corrects `0.0785`
sup / `0.041` mean, which were a 17-point sampling artefact — R155_009 §4(A); the true values are
measured on the full `321`-point `v`-grid the script itself uses]. The mean profile, `w(2T+v)` at
`v = 0, ½, …, 8`:

```
1.000 0.859 0.790 0.735 0.662 0.569 0.494 0.427 0.342 0.274 0.213 0.169 0.119 0.072 0.051 0.033 0.006
```

Not an exponential: the best `e^{−rv}` fit on `[0,3]` has `r = 0.2225` and misses by `> 0.08`; the
measured local decay rate on the first two units is `0.173 ± 0.014`, the half-height is at
`v = 2.90 ± 0.14`, and the tail is fatter than exponential out to the support cap. At `L = 5` the
profile is a *different* universal shape, steeper and with a tiny negative tail
(`1.000 0.780 0.661 0.569 0.475 0.347 0.260 0.200 0.117 0.061 0.036 0.014 −0.001 …`), also stable to
`0.1378` across all 103 windows [amended per R155_010: corrects `0.095`, the same
17-point sampling artefact — R155_009 §4(A)]. **Both budgets give a `T`-independent shape; `L` selects
which.**

**(B) Two class invariants.** `‖w‖_∞ = 1` within `10⁻²` at 102 of 103 windows [amended per
R155_010: corrects "exactly at 102 of 103" — R155_009 measures `‖w‖_∞ ≤ 1+10⁻⁶` at 98 windows,
`≤ 1+10⁻³` at 99, `≤ 1+10⁻²` at 102; six windows have `‖w‖_∞ > 1`] (`1.011` at `½log3`) and
`∫|w| = ∫w`, i.e. the optimal tail is **non-negative everywhere** at `L = 20`, with `0–3` sign changes
among the 30 spline coefficients. Neither was imposed. `R155_005` reported `∫w` locking at `+5.0…5.2`
in its own class; here it locks at `3.128 ± 0.067` — so the *constancy* survives the change of class
and the *value* does not. The constant is a property of `(h, J, U, L)`, not of the problem.

**(C) What binds.** `last_node = 7.75` (the last lattice node) at 102 of 103 windows: the support cap
binds everywhere, exactly as in `R155_005`. The optimiser always wants a longer tail than it is given.

**(D) The value.** Inside a regime `c_fine(T)` is *not* monotone (e.g. `−0.1453` at `T = 0.8147` rises
to `−0.1419` at `0.9034` before falling), residual of the affine fit `1.7·10⁻³ … 2.65·10⁻²`. §7 (N4)
explains why this is a class artefact and not a statement about `λ^W`.

## §5 The jump law at a prime entry

### 5.1 What jumps: the threshold, by exactly `e^{v_n}`

| entry `n` | `½log n` | `v_n = 2Λ(n)/√n` | measured `τ_env(+)/τ_env(−)` | predicted `e^{v_n}` | measured `2πe^{2T}` ratio |
|---|---|---|---|---|---|
| `4` | `0.693147` | `0.693147` | `2.0000` | `2.0000` | `1.0016` |
| `5` | `0.804719` | `1.439549` | `4.2187` | `4.2187` | `1.0050` |
| `7` | `0.972955` | `1.470994` | `4.3535` | `4.3535` | `1.0050` |
| `8` | `1.039721` | `0.490086` | `1.6325` | `1.6325` | `1.0058` |
| `9` | `1.098612` | `0.732408` | `2.0801` | `2.0801` | `1.0050` |
| `11` | `1.198948` | `1.446005` | `4.2460` | `4.2460` | `1.0050` |

(`n = 3` is the left endpoint of the range: `16.75 → 59.54`, ratio `3.554` against `e^{v_3} = 3.5564`,
the small gap being the `5·10⁻⁴` offset of the first two windows.) Exact, 6/6, and **`PROVED` in §7
(N1) without touching a zero.** The resolution scale `2πe^{2T}` is continuous: it moves by `0.2–0.6 %`.

### 5.2 What does not jump: everything else

| entry `n` | `c_fine` below → above | ratio | `sup_v|Δw|` | `∫w` below → above | contacts |
|---|---|---|---|---|---|
| `4` | `−7.1831e−2 → −7.1755e−2` | `0.999` | `0.0019` | `3.080 → 3.080` | `21 → 22` |
| `5` | `−1.3750e−1 → −1.3908e−1` | `1.011` | `0.0064` | `3.219 → 3.231` | `24 → 26` |
| `7` | `−2.0946e−1 → −2.1100e−1` | `1.007` | `0.0225` | `3.219 → 3.241` | `26 → 24` |
| `8` | `−2.1128e−1 → −2.1195e−1` | `1.003` | `0.0114` | `3.083 → 3.090` | `22 → 23` |
| `9` | `−2.3392e−1 → −2.3444e−1` | `1.002` | `0.0054` | `3.053 → 3.050` | `27 → 27` |
| `11` | `−2.9113e−1 → −2.9160e−1` | `1.002` | `0.0064` | `3.177 → 3.166` | `25 → 24` |

The windows compared straddle the entry by `ΔT = 0.0008–0.0029`. Value, profile, mass and contact count
move by less across an entry than they do between two ordinary neighbouring windows inside a regime.
**This is the direct refutation of `R155_005 §0.4/§4.1** ("`c(T)` is a step function of the prime set,
not a function of `T`", "four orders of magnitude across the entry of `3`"): that step was produced by
`τ_max = min(τ_env, 200)`, which multiplied the LP's domain by `3.55` at the same instant. The
the audit flagged the `M`-dependence and the domain, but "the domain is the whole of it" is WITHDRAWN
[amended per R155_010, R155_009 §2(C).2–3]: Proposition C and its corollary establish only
that the value at a *fixed* domain is continuous, not that `λ^W(T)` or `W_T` itself is; the
moving-domain artefact is confirmed as a contributing hypothesis at this one tested entry, not
established as the complete explanation of `R155_005`'s step.

### 5.3 And what the cap hides

`domain_probe.py` re-evaluates the certified `L = 20` weight of the first window of each regime on the
multiplier-free interval `[0, τ_env]` instead of `[0,60]` — **not** its "true" verification interval
[amended per R155_010: the word "true" is DELETED — R155_009 flags it as false. Paper 46
Prop. env's actual threshold is `2πe^{A+‖ν‖_TV+o(1)}`; for these weights `‖ν_w‖_TV ≈ 48.7`, so the
threshold is `≈ 2.4·10²²`, not `16.7…502`. `τ_env = 2πe^{A_T}` used here is only the multiplier-free
part]:

| `|N_T|` | `T` | `τ_env` | `min f` on `[0,60]` | `min f` on `[0,τ_env]` | at `τ =` |
|---|---|---|---|---|---|
| 1 | `0.54931` | `16.75` | `−1.80876e−2` | `−1.80876e−2` | `6.16` |
| 2 | `0.54981` | `59.54` | `−5.77923e−2` | `−5.77923e−2` | `55.60` |
| 3 | `0.69365` | `119.09` | `−7.13102e−2` | `−1.74215e−1` | `73.12` |
| 4 | `0.80522` | `502.39` | `−1.38752e−1` | `−6.44675e−1` | `484.70` |

(Regimes 5–8 are not affordable: `τ_env` reaches `31 535`.) The extra damage is `2.4×` and `4.6×`, and
it sits **at the right end of the newly opened interval** — the argmin tracks `τ_env`, not the primes.
So the honest form of the jump law is: *at a prime entry the certificate's data is unchanged and its
required domain is multiplied by `e^{v_n}`; the value falls only because it must now be defended on
the new piece, and the new piece is where the class is weakest.*

## §6 The extrapolation test

Train inside regime `k` (affine in `T`, coefficient-wise on the profile grid and on the value),
predict the **first window of regime `k+1`**, never re-optimising there.

| train `|N_T|` | `n` train | test `|N_T|` at `T` | profile sup error | `c` predicted | `c` true | rel. | last-value predictor | rel. | sign kept |
|---|---|---|---|---|---|---|---|---|---|
| 2 | 20 | 3 at `0.693647` | `0.0212` | `−7.2503e−2` | `−7.1755e−2` | `1.0 %` | `−7.1831e−2` | `0.1 %` | yes (negative) |
| 3 | 17 | 4 at `0.805219` | `0.0338` | `−1.2703e−1` | `−1.3908e−1` | `8.7 %` | `−1.3750e−1` | `1.1 %` | yes (negative) |
| 4 | 23 | 5 at `0.973455` | `0.0555` | `−1.8779e−1` | `−2.1100e−1` | `11.0 %` | `−2.0946e−1` | `0.7 %` | yes (negative) |
| 5 | 12 | 6 at `1.040221` | `0.0299` | `−2.0955e−1` | `−2.1195e−1` | `1.1 %` | `−2.1128e−1` | `0.3 %` | yes (negative) |
| 6 | 12 | 7 at `1.099112` | `0.0253` | `−2.3518e−1` | `−2.3444e−1` | `0.3 %` | `−2.3392e−1` | `0.2 %` | yes (negative) |
| 7 | 16 | 8 at `1.199448` | `0.0546` | `−2.8534e−1` | `−2.9160e−1` | `2.1 %` | `−2.9113e−1` | `0.2 %` | yes (negative) |

**Plainly stated.** (i) The prediction *works*, for the profile (`2–6 %`) and for the value (`0.3–11 %`
affine, `0.2–1.1 %` for the trivial "same as the last window" predictor, which beats the affine fit at
every entry). **[amended per R155_010: this file does not run the end-to-end conditioning
test — predicting the profile, then evaluating that predicted profile's own `min f` (not the LP-optimal
`c`) — that R155_006 §6 and R155_009 flag as missing. R155_009 ran it: the honest end-to-end prediction
loses `1.2–1.6×` against re-optimising, not the `0.3–11 %` value error quoted above for the LP-value
comparison, and at least one predicted weight is infeasible. Both numbers are correct for what they
measure; they answer different questions (LP-value error vs. evaluated-prediction loss), and the
weaker (`1.2–1.6×`) is the one relevant to whether extrapolation could ever substitute for
re-optimising.]** (ii) **The prediction keeps the sign in 6 cases out of 6, and the sign is negative
every time.** Extrapolation across a prime entry is therefore not the obstruction `R155_005 §5` claimed —
its failure (`61×`, `234×`) came from a training set that straddled an entry and from a moving domain.
(iii) What is *not* extrapolable is anything positive: there is no window in the range where this class
is close to `0`, so no amount of correct extrapolation produces a certificate. The "ese patrón
lo podemos extrapolar sí o sí" is confirmed as a statement about the pattern and refuted as a route to
a sign: **the pattern that extrapolates is the pattern of not closing.**

## §7 What is necessary, and what is only observed

### 7.1 `PROVED`, from Theorem Z + the definitions, with no zeros

**Proposition E (entry law).** `A_T = Σ_{n<e^{2T}} v_n`, `v_n = 2Λ(n)/√n`, is a left-continuous step
function of `T` (`N_T = {n : \log n < 2T}` is defined with strict inequality, so the entering `n` is
excluded at `T = ½\log n`), constant on each interval between consecutive points `½log n` (`Λ(n) > 0`),
with **`A_{T^+}−A_T = v_n` at `T = ½log n`** [amended per R155_010: corrects
`A_T − A_{T^-} = v_n`, which is false under the strict-inequality convention actually used
(`A_T − A_{T^-} = 0` there) — R155_009 §2]. Consequently the **multiplier-free** part of the envelope
threshold of Paper 46 Prop. env, `τ_env(T) := 2πe^{A_T}` [amended per R155_010: Prop. env's
full threshold is `2πe^{A+‖ν‖_TV+o(1)}`; `τ_env` here names its multiplier-free part only], satisfies
`τ_env((½log n)^+)/τ_env((½log n)^-) = e^{v_n} = e^{2Λ(n)/√n}` exactly [amended per
R155_010: corrects the direction of the ratio to match the right-hand limit], and is constant between
entries. *Proof:* immediate from the definition of `A_T` and `N_T = {n : \log n < 2T}`. ∎

**Proposition D (closed form for the difficulty index).** With `τ_res(T) = 2πe^{2T}` (Paper 46 §8.2),
`D(T) := τ_env(T)/τ_res(T) = e^{A_T − 2T}`. Hence `D` decays like `e^{−2(T−T_n)}` inside each regime and
is multiplied by exactly `e^{v_n}` at each entry, and `D(T) → ∞` doubly exponentially since
`A_T = (4+o(1))e^T`. *Proof:* substitute. ∎
`R155_005 §4.2/§6.2` introduced `D` as an empirical index; it needs no experiment. Its values on our
grid (`0.89` at `½log3`, `455.8` at `1.20`) are reproduced by the formula to all printed digits.

**Proposition C (the objective is continuous at an entry).** Fix the shape family of §2.1 and a
coefficient vector `(y,x)`. Then for each `τ`, `T ↦ f_{w_T}(τ)` is continuous on `(0,∞)`.
[amended per R155_010: "and real analytic off the set `{½log n}`" is DELETED — false for
this family (R155_009 §2(C).1): the cubic-spline nodes `u_j = 2T+jh` move with `T`, so `w(\log n)` is
only piecewise polynomial with breakpoints where `\log n` crosses a moving knot; continuity, and `C²`,
is all that is available.] *Proof:* use the prime/Γ side of Theorem Z,
`f = m(τ) + ∫_{2T}^∞(1−w)K\cos τu\,du − Σ_n v_n w(\log n)\cos(τ\log n) + 2∫_{|u|\ge2T} w\cosh\frac u2\cos τu\,du`.
The three integrals depend on `T` through the endpoint `2T` and through `w(\cdot;T)`, both continuously.
In the prime sum the coefficient of `n` is `v_n w(\log n)`, and `w(\log n) = 1` for `\log n \le 2T`,
`= φ(\log n − 2T)` for `\log n > 2T`, where `φ(0) = w(2T) = 1` by the flat-top constraint. So each
coefficient is continuous in `T`, uniformly, and the sum converges uniformly by `|w| \ll e^{-s|u|}`,
`s > ½`. ∎
**Corollary — WITHDRAWN as stated, [amended per R155_010, R155_009 §2(C).2–3].** The claim
"at a prime entry nothing in the certificate problem jumps except the *domain*" is broader than
Proposition C supports: the proposition fixes the coefficient vector inside one `T`-independent shape
family and says nothing about `W_T` itself (which does change: `W_{T'} ⊊ W_T`) nor about `λ^W(T)`,
whose continuity is not proved anywhere in this file. What is proved is only: *the value of the §2.1
sub-class at a fixed verification domain is continuous in `T`.* Correspondingly, "`R155_005`'s step
was a moving-domain artefact" is a hypothesis the experiment here does not establish (the domain here
is frozen at `τ ≤ 60` on both sides of the comparison, and at the one moving-domain entry tested the
value jumps `3.2×`), not a conclusion; it is NOT asserted as established.

**Proposition M (monotonicity and the direction of induction).** If `T' ≥ T` then `W_{T'} ⊆ W_T`
(a weight flat on `[−2T',2T']` is flat on `[−2T,2T]`, and the decay condition does not involve `T`).
Hence `λ^W(T) := \sup_{w∈W_T}\inf_ℝ f_w` is non-increasing in `T`. *Proof:* a supremum over a smaller
set. ∎
So the class-optimal value can only fall; there is no upward induction in `T` at the level of the
class, which is the dual form of Paper 46 §8.3(4). (Our measured `c_fine` is not monotone inside a
regime because the *sub*-class of §2.1 is **not** nested — its lattice `u_j = 2T + jh` moves with `T`.
The non-monotonicity in §4(D) is therefore a class artefact and carries no information.)

**Lemma S (smoothness ⇒ far-zero decay), as in `R155_006 §2`,** is used but not restated: for `w`
with `w^{(k)}` continuous and `w^{(k+1)}` of bounded variation, `\hat w(t) = O(|t|^{-k-2})` and, under
RH below `Γ`, `Σ_{|γ|>Γ}|\hat w(τ−γ)| = O(Γ^{-k-1}\log Γ)`. Measured here at `k = 2`: beyond `Γ = 800`
the contribution is `< 10^{-9}` (§2.3).

**Bernstein grid lemma,** as in `R155_006 §11(a)(2)`: `f_w` is band-limited of type `U`, so
`\min_ℝ f \ge \min_{δ\text{-grid}} f − \tfrac12U^2\|f\|_∞δ^2`. Used for every `c_cert` (§2.4).

**Lemma R (rigidity)** — see §7bis(2).

### 7.2 Observed only (`DIAGNOSTIC`)

| observation | status |
|---|---|
| the universal profile (`‖w‖_∞ = 1` within `10⁻²`, `∫w = 3.128 ± 0.067`, non-negative tail, rate `0.173 ± 0.014`, one global shape to `0.1332` sup / `0.0599` mean across 103 windows and 8 regimes [amended per R155_010: corrects `0.0785`, a 17-point sampling artefact — R155_009]) | `DIAGNOSTIC`; a property of `(h,J,U,L)` as much as of the problem, since the `L = 5` shape is a different universal shape |
| `c_fine(T)` falling `−1.8·10⁻² → −2.9·10⁻¹` over the range, with in-regime wobble | `DIAGNOSTIC`; the overall fall is consistent with Prop. M, the wobble is a class artefact |
| extrapolation across an entry works to `0.3–11 %` | `DIAGNOSTIC` |
| the extra factor `2.4×`/`4.6×` from un-capping the domain, argmin near `τ_env` | `DIAGNOSTIC`, two windows only |
| contacts `23.8 ± 1.7`, independent of `T` and of `N_T` | `DIAGNOSTIC`. Note this does **not** reproduce `R155_005 §4.4`'s reading that the contacts form the class's Nyquist comb `2π/U`: here `2π/U ≈ 0.67` would allow `≈ 89` contacts on `[0,60]` and only `24` appear, mean spacing `2.5`. The Nyquist reading is class-specific and does not survive |
| the `1.6·10⁻⁴` prime-sum truncation artefact (§2.4) | `DIAGNOSTIC`, but it is a *reproducible bug class*: any `w` built from non-compactly-supported edge functions with cancelling coefficients needs the prime sum far beyond `e^U` |

## §7bis The toy universe of ten zeros

*the question: "what would `D` have to be for RH to hold on 10 zeros, if the whole universe were
those 10 zeros?"*

### (1) In a finite universe the certificate is the zero set itself, and it is free

Let `Z = {±γ_1,…,±γ_{10}}` be the first ten Odlyzko ordinates (`γ_1 = 14.134725`, …,
`γ_{10} = 49.773832`), all real. Define the toy Weil functional on even Schwartz `h`,
`W_Z(h) := Σ_{j} \hat h(γ_j)` (both signs). **Claim: `W_Z` is automatically positive on the Weil cone,
and its optimal dual certificate is the atomic measure `D_Z = Σ_j (δ_{γ_j} + δ_{−γ_j})`.**
*Proof (three lines).* (i) For `h = g \star \tilde g` with `g` even real, `\hat h = |\hat g|^2`, so
`W_Z(h) = Σ_j |\hat g(γ_j)|^2 \ge 0`; the only input is `γ_j ∈ ℝ`, i.e. that the toy "zeros" lie on the
critical line. (ii) `W_Z(h) = \int \hat h \,dD_Z` by definition, so `D_Z` is a representing measure and
is dual-feasible with value `0`. (iii) It is minimal: any positive measure `μ` with
`\int\hat h\,dμ = W_Z(h)` for all `h` has `\hat\mu = \hat D_Z` as tempered distributions, hence
`μ = D_Z`. ∎ `PROVED` (trivial). This is the finite-dimensional shadow of the Kreĭn/Suzuki screw-function
representation cited in Paper 46's related-work section: in a finite universe the representing measure
*is* the spectrum, there is nothing to construct, and positivity is a tautology. **The toy universe has
no content: for any finite set of real points RH is true by fiat, so no `D` needs to be found.**

### (2) The rigidity lemma: in a finite universe there is no decaying flat-top certificate at all

**Lemma R (`PROVED`).** Let `w ∈ L^1(ℝ)` be even, continuous, with `w ≡ 1` on `[−2T,2T]` for some
`T > 0`, and suppose `\hat w \ge 0` on `ℝ`. Then `w ≡ 1` on all of `ℝ` — in particular no such `w` is
integrable, so **no non-trivial flat-top weight has a non-negative Fourier transform.**
*Proof.* `\hat w \ge 0` and `\int\hat w = 2π w(0) < ∞`, so `\hat w\,dt/2π` is a finite positive measure
whose Fourier transform is `w`; by Bochner, `w` is positive definite, with `w(0) = 1`. For a positive
definite `φ` the standard inequality (positivity of the `3×3` Gram matrix at `0, −u, a`) gives
`|φ(u+a) − φ(u)|^2 \le 2φ(0)\,(φ(0) − \operatorname{Re}φ(a))` for all `u, a`. Take any `a` with
`0 < |a| \le 2T`: then `w(a) = 1 = w(0)`, so the right-hand side vanishes and `w(u+a) = w(u)` for all
`u`. Thus `w` is periodic with every period in `(0, 2T]`, hence — being continuous — constant, equal
to `w(0) = 1`. ∎
**Consequences.** (a) In `Cor. 7.4` the non-negativity of `f_w(τ) = Σ_ρ \hat w(τ−γ_ρ)` can *never* be
termwise: `\hat w` takes negative values for every admissible `w`, so the certificate is a statement of
**cancellation across the zeros**, not of positivity of a kernel. (b) In particular, with only finitely
many zeros the sum `Σ_{j\le N}\hat w(τ−γ_j)` is a finite sum of a function that is negative somewhere
and `→ 0` at infinity, so it is negative for `τ` far from all `γ_j`: **a finite zero universe admits no
flat-top certificate whatsoever.** Positivity of `f_w` is possible only because the zero density
`\sim(2π)^{-1}\log(t/2π)` is infinite in the mass sense — the `m(τ) = \log(τ/2π)+O(τ^{-1})` growth of
Paper 46's `σ_T`. This is why rows A/B/C (Weil positivity on the *complete* spectrum) and row D (a
certificate at a single window) cannot be reduced to finite verification.

### (3) The toy prime side carries no information about ζ

For the toy universe the "explicit formula" is the definition `W_Z(h) = \int\hat h\,dD_Z`, i.e. the
comb `g_Z(u) = Σ_{j} 2\cos(γ_j u)` (the inverse transform of `D_Z`, regularised by any Gaussian
`e^{-εu^2}`). The one and only structural requirement for the toy universe to be "RH-consistent" is
that `g_Z` be positive definite as a distribution — which, by Bochner, is exactly the statement
`D_Z \ge 0`, i.e. that the `γ_j` are real. That is Weil's criterion and nothing more: **rows A/B/C
territory, and vacuous in a finite universe.** No arithmetic enters: the archimedean term
`m(τ) = \operatorname{Re}ψ(¼+iτ/2) − \logπ` and the prime comb `Σ_n v_n\cos(τ\log n)` of the real
explicit formula are *not* recoverable from `D_Z`, because `D_Z` determines only itself. Ten zeros
(or `10^5`) fix no prime; the prime comb of ζ is determined by the *whole* zero set through the
explicit formula, and every finite truncation of it is compatible with infinitely many different
prime combs. **Hence no pattern read off a toy universe can be extrapolated to ζ**, which is the
same wall as the circularity no-go (`phase-4-krein-space-realization/proofs/00-PROOF-LOG.md:168`, ES-2), seen from the
other side.

### (4) The cancellation budget: how many zeros a certificate needs

`toy10.py`, `T = ½log3`, the certified `L = 20` weight of window 1 (`U = 9.349`), prime/Γ side with
`49 298` prime powers and Gauss–Legendre order `800`:

| zeros used `N` | `γ_N` | `min_τ Σ_{j\le N}\hat w(τ−γ_j)` | `max_τ |f_N − f^{\text{prime}}|` |
|---|---|---|---|
| `1` | `14.135` | `−1.234522e−1` | `1.7154e−1` |
| `2` | `21.022` | `−3.710077e−2` | `9.1772e−2` |
| `5` | `32.935` | `−2.043596e−2` | `3.3207e−3` |
| `10` | `49.774` | `−1.847708e−2` | `4.0204e−4` |
| `100` | `236.524` | `−1.810942e−2` | `6.0202e−6` |
| `1000` | `1419.422` | `−1.811278e−2` | `1.3954e−7` |
| `10⁴` | `9877.783` | `−1.811279e−2` | `1.1902e−7` |
| `10⁵` | `74920.827` | `−1.811279e−2` | `1.1910e−7` |

Reading (`DIAGNOSTIC` for the numbers, but the shape of the conclusion is forced by Lemma S):
**ten zeros leave a deficit of `4.0·10⁻⁴`, which is `4.5×` the corpus's best certified value at this
window (`λ_min(A_{½log3}) \ge 8.8577·10⁻⁵`, Paper 46 Thm. C).** A hundred zeros bring the deficit to
`6.0·10⁻⁶`, a thousand to the `1.2·10⁻⁷` floor of the double-precision evaluation. So the answer to
"what would `D` have to be on ten zeros" is: *nothing at all, because on ten zeros the problem is
empty (§7bis 1–2); and if one asks instead how much of the real `f_w` the first ten zeros account for,
the answer is: all but `4·10⁻⁴`, which is already too much to hide a certificate in.* The first
`\approx100` zeros are the cancellation budget of a certificate at `½log3`; beyond `10^3` the zeros are
irrelevant to this window, which is the same fact as §2.3 (`Γ = 800` suffices) seen from the value side.

## §8 Labels

| item | label |
|---|---|
| Propositions **E**, **D**, **C** (+ corollary), **M**, and Lemma **R** (§7, §7bis) | `PROVED` — elementary, no zeros, no numerics |
| Lemma **S** (smoothness ⇒ far-zero decay) and the Bernstein grid lemma | as in `R155_006 §11(a)`: `PROVED` modulo being written up; used here as tools |
| the 103-window table, all values `c_LP`, `c_fine`, `c_cert`, all profile statistics, all fits, the extrapolation test, the domain probe, the cancellation budget | `DIAGNOSTIC` — the LP is trained on a table of zeros (circular as a tool, `phase-4-krein-space-realization/proofs/00-PROOF-LOG.md:168`, `phase-136/MAP_1:141` ES-2); double precision; finite grids; `τ` capped at `60` at 82 of 103 windows [amended per
R155_010: corrects `79` — R155_009]; no interval arithmetic |
| the numerical verification of Theorem Z across eight regimes (§2.4) | `DIAGNOSTIC` verification of a `PROVED` statement; value is as a regression test |
| row D label | **unchanged.** No sign is claimed for any `T > log 2`. Endpoint of record unchanged: `λ_min(A_{½log3}) \ge 8.8577·10⁻⁵` (Paper 46 Thm. C) |
| `R155_005` §0.4 / §4.1 ("`c(T)` is a step function of `N_T`", "four orders across the entry of 3") | **superseded** by §5 and Prop. C. The step was a moving-domain artefact |
| `R155_005` §4.4 (contacts at the Nyquist comb `2π/U`) | **not reproduced** in this class (§7.2) |
| `R155_005` §5 ("no law for `w_T` in `T`") | **superseded**: the profile law is universal across all eight regimes (§4(A)), and extrapolation across an entry works (§6). The audit's in-regime rerun is confirmed and extended |

## §9 Proposed pure-math statements

1. **The regime dichotomy (Props. E + D + C), for Paper 46 §8.2.** *At `T = ½log n` the certificate
 problem's data — the archimedean term, the prime comb coefficients, the class `W_T` — varies
 continuously; the only discontinuity is the verification threshold, which is multiplied by exactly
 `e^{2Λ(n)/√n}`, and the difficulty index has the closed form `D(T) = e^{A_T−2T}`.* Half a page, no
 zeros, and it replaces `R155_005`'s empirical index and Paper 46 §8.2's qualitative "three scales".
 It also says precisely which entries are expensive: `e^{v_p}` for a prime is `\gg` that for a prime
 power, so the hard steps are `3, 5, 7, 11, …` (factors `3.6, 4.2, 4.4, 4.2`) and `4, 8, 9` are cheap
 (`2.0, 1.6, 2.1`).
2. **Lemma R (rigidity), for Paper 46 §7, next to Cor. 7.4.** *No non-trivial flat-top weight has
 `\hat w \ge 0`; hence `f_w \ge 0` is never a termwise statement and is impossible over any finite set
 of zeros.* This is the sharpest one-line answer to "what must `D` look like": whatever it is, it is
 not a positive kernel, and it cannot be certified on a finite spectrum. It also disposes, in three
 lines, of the natural family of attempts that try to build `w` with `\hat w \ge 0`.
3. **Proposition M as the direction of induction.** `λ^W(T)` is non-increasing because `W_{T'} ⊆ W_T`;
 therefore the only induction available in `T` runs *downward*, and any programme that hopes to climb
 from `½log3` to `\log 2` to `½log5` must gain from the arithmetic, never from the class. Worth one
 sentence in Paper 46 §8.3(4), which currently states the same thing without the inclusion.
4. **The bounded-profile conjecture, sharpened (Problem A).** At `L = 20` the optimiser returned
 `0 \le w \le 1` at 102 of 103 windows *without being asked*. Conjecture: `\sup\{\inf f_w : w ∈ W_T,\,
 0 \le w \le 1\}` is attained, its optimal profile is `T`-independent in `v = u − 2T` up to
 `O(e^{-cT})`, and it is bounded away from `λ^W` for every `T` (weight-side Theorem O). The audit's
 warning in `R155_006 §12(ii)` applies and is now sharper: the escape mechanism of Thm. O is mass
 leaving to large `u` against `\cosh(u/2)`, so the right compactness hypothesis is `0 \le w \le 1`
 **plus** a fixed decay modulus, and the honest open question is whether `0 \le w \le 1` alone
 suffices. The evidence here is cleaner than `R155_005 §2.4`'s (no grid exploitation: `c_LP − c_fine
 = 8·10⁻⁴`), but it is still evidence for an upper bound, i.e. another negative, not the lower bound
 Problem A asks for.
5. **A verification-budget lemma.** From Lemma S plus §7bis(4): for `w ∈ W_T ∩ C^2` with
 `\|x\|_1 \le L` and support `U`, `|f_w(τ) − Σ_{|γ|\le Γ}\hat w(τ−γ)| \le C(L,U)Γ^{-3}\log Γ` under RH
 below `Γ`, with `C` explicit; hence a certificate of value `c` can be *falsified* from a table of
 zeros of height `Γ \gg (C/c)^{1/3}`, but never *verified* from one. At `½log3` with `c = 8.86·10⁻⁵`
 the crossover is `\approx 100` zeros — small, and the reason the whole reverse-engineering track was
 affordable. Elementary; it belongs beside Cor. `zeros`.

---
*Scripts: `scripts/reverse/regime/` (`reglib.py`, `resid_check.py`, `run_regime.py`, `fit_regime.py`,
`crosscheck_regime.py`, `domain_probe.py`, `toy10.py`), README with exact commands and runtimes; total
compute for this deliverable `\approx 12` minutes in one process, of which `496 s` is the 103-window
run. Data: `scripts/reverse/regime_table.csv`, `regime_windows.json`, `fit_regime.json`,
`crosscheck_regime.json`, `domain_probe.json`, `toy10.json`, `resid_check.json`, logs
`run_regime.log`, `analysis.log`, `analysis2.log`.*
