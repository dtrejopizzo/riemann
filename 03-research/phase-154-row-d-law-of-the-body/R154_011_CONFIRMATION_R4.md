# R154.011 — Round 4 (confirmation round): is the certificate at `T = ½log3` a proof?

*Target: `R154_010` §5, Theorem R4, and `scripts/round4/` +
`scripts/round4/certificate/CERT_log3_M24.json`. Method: independent replay — my own reader of the JSON decimals, my own
evaluator (mpmath `digamma` and direct `scipy.integrate.quad` for the two window transforms, i.e. **not** the earlier
closed forms), my own Lipschitz constant from quadrature, my own branch-and-bound, my own high-precision
(`mp.dps = 50`) re-evaluation at the three minima. Scripts: `aud.py`, `bb.py` (scratchpad; reproduced verbatim below in
substance).*

## VERDICT: **PROOF ACCEPTED.**

`λ_min(A_{½log3}(w_ζ)) ≥ c = 4.4279281900·10⁻⁵ > 0` on `P_T` is established. Every load-bearing step — the duality
direction, the two annihilation identities, the closed forms, the Lipschitz constant, the tail lemma's three
monotonicities, the exhaustiveness of the cover, the tiling, the provenance of the polished certificate, the interval
enclosures — was re-derived or re-run here and **stands**. The one non-rigorous link (float64 evaluation inside the
`2.37·10⁸`-point cover, calibrated rather than bounded) is quantified below and has a **factor `4.4·10³` of margin**;
it is a caveat on the phrasing, not a defect in the result.

---

## 1. Verdict table

| # | item attacked | finding |
|---|---|---|
| 1 | conventions: `T = ½log3` exactly, `v_2 = 2log2/√2`, only `n = 2` (`n < e^{2T} = 3`) | **CONFIRMED.** `T − ½log3 = 0`, `v₂ − 2log2/√2 = 0` in float64. `2w₂ = v₂ = 0.9802581435`, consistent with `R154_005 §5.3` (`2Σw − C₀ = 6.3524415627`); `c` is a bound on `λ_min` itself, i.e. on `λ₁^{P_T}(E_Γ+E_P) − 6.3524415627`, not on that constant |
| 2 | `ĝ₀, ĝ₁` are the transforms of `cosh(u/2)`, `u sinh(u/2)` on `[−2T,2T]` | **CONFIRMED** by direct quadrature: `|g0h − ∫cosh(u/2)cos(τu)du| ≤ 2.2·10⁻¹⁶` and `|g1h − ∫u sinh(u/2)cos(τu)du| ≤ 2.8·10⁻¹⁶` at `τ = 0, 1, 7.3, 33` |
| 3 | `∫ĝ_k|F̂|² = 0` on `P_T`; `∫ν̂|F̂|² = 0`; the boundary atom `u_{24} = 2T` | **CONFIRMED.** `∫c_F(u)e^{±u/2}du = M_±F·M_∓F̄ = 0` for `F ∈ ker M_−∩ker M_+` (Paper 42 `main.tex:4084–4088`), giving both moment rows; `R154_005 §5.2` is the correct parity argument. `c_F` is continuous with `c_F(±2T) = 0`, so the atom sitting **exactly** at `u = 2T` (`u_{24} − 2T = 0` in float64, `a_{24} = −0.4028 ≠ 0`) pairs to zero. Sharpest point of the construction; it is sound |
| 4 | the direction used is **weak** duality, not D1 | **CONFIRMED and important.** The proof needs only `D_T ≤ λ_min`, which is one line (integrate the certificate against `μ = |F̂|²dτ/2π`). Theorem D1 (`R154_007 §2.2`, the contested strong-duality half) is **not** on the critical path. The result is therefore independent of repair `RJ` |
| 5 | lattice/periodicity: `u_j = j·2T/24`, `j = 24..460` | **CONFIRMED.** `max_j|u_j − j·(2T/24)| = 0`; `d·P − 2π = 1.6·10⁻¹⁴` (float rounding of the printed `P`; mathematically `P = 2π/d` and `u_jP = 2πj` exactly). `437` atoms, `‖a‖₁ = 45.3772`, `u_max = 21.0567` |
| 6 | Lipschitz constant `L = 647.4198370823957` | **CONFIRMED, recomputed independently.** `|m′| ≤ ½ψ′(¼)` (since `|ψ′(z)| ≤ Σ|z+n|⁻² ≤ ψ′(Re z)`), `|ν̂′| ≤ 2Σ|a_j|u_j`, `|β_kĝ_k′| ≤ |β_k|∫|u|^{k}·…`. My `G₀ = 1.2995284` (closed form vs quadrature: `6.7·10⁻¹⁶`), `G₁ = 0.3765301`. My `L = 647.4198370823957`, **bit-identical** to the certificate's, and `≥` its `mpmath.iv` enclosure. `ψ′(¼) − (π²+8G) = 3.6·10⁻¹⁵` |
| 7 | is `L` valid for the tail functions `h_k` too? | **CONFIRMED with large slack.** `h_k′` replaces `β·ĝ′` by `−|β₀|k₀′−|β₁|k₁′`, whose modulus at `τ ≥ 30` is `5.25·10⁻³` against the `|β₀|G₀+|β₁|G₁ = 2.606` that `L` already carries |
| 8 | Lemma D2.3's three monotonicities (`m` ↑, `k₀,k₁` ↓, `−v₂cos ≥ −v₂`) | **CONFIRMED.** `m` increasing on `[0,3000]` (grid `10⁻³`; and structurally, `Reψ(¼+iy) = −γ+Σ_n[1/(n+1) − (n+¼)/((n+¼)²+y²)]` is increasing in `|y|`); `k₀,k₁` strictly decreasing. The `k₀,k₁` bounds themselves re-derived: `|ĝ₀| ≤ 2cosh T/τ + sinh T/τ²` from `τ²+¼ ≥ τ²`; `|ĝ₁| ≤ 8T sinh T/τ` by one integration by parts using `(u sinh(u/2))′ = sinh(u/2)+(u/2)cosh(u/2)`. Both correct |
| 9 | does `[0,τ₁] ∪ {h_k on [τ₁,τ₁+P]}` cover `R`? | **CONFIRMED.** `f` even; `[0,30]` direct; `τ ≥ 30` by D2.3 with `x ∈ [30, 167.2608]`, `k = 0,1,2` (`k = 2` the worst-case family). `P = 2π·24/log3 = 137.2608416` ✓. No gap |
| 10 | B&B implementation: stack-based, `L·w/2` subtracted, no cap, no discard | **CONFIRMED by code reading** (`r4bbpar.bb_seg`). Stack, not recursion; `keep = vals − L·w/2 < target` (correct sense: a cell is retired only when `f ≥ target` is *proved* on it); over-large batches are pushed back, never dropped; the evaluation budget **raises** `RuntimeError` rather than returning a pass; leaves at `w/2 < w_min` would contribute `min vals − Lw/2` to the bound rather than being discarded — and `nfinal = 0` means that branch was never reached. `lb = min(target, ∞) = target` is then exactly "cover closed at the target" |
| 11 | "21 segments, 0 unresolved, `2.37201004·10⁸` evaluations" | **CONFIRMED against `bbout/_all.json`:** `f` 3 segments tiling `[0,30]` (max gap `0.0`), `h₀,h₁,h₂` 6 each tiling `[30, 167.2608416]` (max gap `0.0`); single `target = 4.42892819·10⁻⁵`, single `w_min = 5·10⁻⁸`, single `L = 647.419837082`; `complete = True` everywhere; `Σ final_intervals = 0`; `Σ evals = 237 201 004` |
| 12 | **replay of the cover with my own code** | **CONFIRMED, bit-for-bit.** Five segments rerun with an independently written B&B: evaluation counts reproduce the earlier *exactly* — `h₀[144.38,167.26]` 8 104; `h₁[75.75,98.63]` 22 742; `h₂[30,52.88]` 218 062; `f[10,20]` 52 075 060; `h₀[30,52.88]` 30 826 198. All return `lb = 4.42892819·10⁻⁵`, `nfinal = 0` |
| 13 | dense grid over `[0,200]` | `min f = 8.8749719·10⁻⁵` at `τ = 17.645` (`h = 10⁻⁴`), i.e. **exactly twice `c`** — the earlier round set `target` to half the fine-grid infimum, so the cover runs with `4.4·10⁻⁵` of unused margin at every point. Not itself a certificate at that `h` (`Lh/2 = 0.032`), but it confirms the shape and the argmin |
| 14 | interval enclosures at the three minima | **CONFIRMED independently** at `mp.dps = 50` with my own evaluator (quadrature for `ĝ₁`): `f(17.64498) = 8.874965829·10⁻⁵`, `h₀(37.81530) = 8.857856397·10⁻⁵`, `h₂(58.81710) = 8.881723155·10⁻⁵` — agreeing with the certificate's `mpmath.iv` intervals to `≈ 2·10⁻¹⁶` absolute and all strictly positive as intervals |
| 15 | the `Reψ(¼+iτ/2)` enclosure (recurrence + Stieltjes remainder) | **CORRECT and used inside its validity range.** `r4iv.m_iv` shifts by `J = 2|Im z| + 30`, so the asymptotic series is applied at `Re w = ¼+J ≥ 2|y|+30`, i.e. `|arg w| < π/4`, where the Stieltjes bound `|R_N| ≤ |B_{2N}|/(2N|w|^{2N})·sec(θ/2)^{2N}` is valid and `sec(θ/2)^{2N} = (2|w|/(|w|+Re w))^N` is the correct rewriting. `N = 12`, widths `≈ 10⁻⁴²`. `ψ′(¼)` cross-checked against `π²+8G` inside the module by assertion |
| 16 | `ε_fp = 10⁻⁸` justified by a measured `8.21·10⁻¹³` | **ACCEPTED, with the caveat named.** The justification is a calibration at 63 points, not a bound over the `2.37·10⁸` points actually used. But (a) an a-priori estimate gives the same order: the dominant error is the argument rounding in `cos(u_jτ)`, `|u_jτ| ≤ 3.5·10³`, contributing `≲ 2Σ|a_j|·3.5·10³·2^{-53} ≈ 3.6·10⁻¹¹`, with `scipy.digamma` at a few ulp of `O(5)`; (b) **decisively**, the cover closed at `target = 4.42892819·10⁻⁵` while the true infimum is `8.87·10⁻⁵`, so the certificate survives any uniform float error below `4.4·10⁻⁵` — a margin of `4.4·10³ × ε_fp`. The conclusion `c > 0` is not sensitive to this link |
| 17 | provenance: is the **polished** certificate the one verified? | **CONFIRMED.** `lp_c24_it1.pkl` carries `lam` of length **128** (the `G = 128` block polish), `polished_from = lp_q24_it1.pkl`, `it = 1`, `lp = 8.88546220662175·10⁻⁵`. The archived JSON's `lp_value = 8.885462206621749·10⁻⁵` and its `beta0/beta1` match that pkl to the last bit, and `sw_c24.log` shows it1 as the last polish iterate (`hmin = +8.85785·10⁻⁵`, positive; it0's was `−6.45·10⁻⁵`). The B&B was driven from that pkl and `r4final.py` recomputed `L`, `f` and `h_k` from it. **No pre-polish object was verified and then swapped** |
| 18 | `β₀ = 2.0025617`, `β₁ = −0.0096544` vs D3 | **CONSISTENT.** `R154_007 §4.1` gives `β₀ → 2` (here `2.6·10⁻³` off) and `R154_007 §4.2`'s trend `β₁ = −1.4070, −0.3885, −0.00520, −0.00803` for `M = 8,12,16,19` — i.e. `β₁ → 0` **from below**. The `+0.062930` cited in the round-3 *certificate* (`R154_007:175`) was one non-optimal flat-lemma point, not the D3 trend; `β₁ = −0.0097` at `M = 24` continues the D3 sequence. The claim that "`β₁` changed sign" is a comparison against that outlier, and there is no inconsistency to repair |
| 19 | stale fields in the pkl (`fine = 1.95·10⁻⁵`, `hmin = −0.146`, inherited from `lp_q24_it1`) | cosmetic; **not used** by `r4bbpar.py` or `r4final.py` (both recompute). No effect. Flagged for hygiene |
| 20 | FATAL rule | **PASSED.** Positivity at `½log3` is already certified in Paper 42 (`main.tex:4072–4230`, Feshbach/Schur-complement); nothing here claims a sign beyond `log 2`, and `T = log 2` is explicitly **not run** ~~with a stated structural obstruction (`log 3` incommensurate with any lattice ⟹ no periodic `ν̂`)~~ **[amended per R154_016: the stated obstruction was false — D2.3 needs periodicity only of `ν̂`, never of the prime term, and applies unchanged at two contacts. `log 2` is not run for compute reasons.]**. Inputs are `ψ`, `log 2`, `log 3`, LP. No `ζ`-zero data |
| 21 | corpus: no prior mesh-free proof at `½log3` | **CONFIRMED.** The only prior attempt is `R153_016`, which records "**No mesh-free proof of `thm:certifiedendpoints` is obtained**… the uncertainty route is `REFUTED`", shortfall factor `3.68` at `½log3`. "dual certificate" elsewhere in the corpus (`Paper 36:10101`, `phase-114/116`) is a different object. The construction is new |
| 22 | Lemma D2.3 itself | **PROVED**, correct as stated; the `⟸` direction (the one used) needs only the three monotonicities of row 8 |

---

## 2. Replay numbers (mine, from the decimals only)

| quantity | certificate | my independent value |
|---|---|---|
| `T − ½log3` | — | `0` |
| `v₂ − 2log2/√2` | `0.9802581434685471` | `0` |
| `max_j |u_j − j·2T/24|` | — | `0` |
| `‖a‖₁` | `45.377` | `45.37720756348435` |
| `G₀` (closed vs quadrature) | — | `Δ = 6.7·10⁻¹⁶` |
| `G₁` | `0.37653` | `0.3765300779612918` |
| `L` | `647.4198370823957` | `647.4198370823957` (identical) |
| `ψ′(¼) − (π²+8G)` | — | `3.6·10⁻¹⁵` |
| `min_{[0,200]} f` (`h = 10⁻⁴`) | — | `8.8749719·10⁻⁵` @ `17.64500` |
| `f(17.64498…)`, `mp.dps=50` | `iv ∋ 8.87496582721·10⁻⁵` | `8.874965829·10⁻⁵` |
| `h₀(37.81530)`, `mp.dps=50` | `iv ∋ 8.85785640064·10⁻⁵` | `8.857856397·10⁻⁵` |
| `h₂(58.81710)`, `mp.dps=50` | `iv ∋ 8.88172331281·10⁻⁵` | `8.881723155·10⁻⁵` |
| `|β₀k₀′|+|β₁k₁′|` at `τ = 30` vs `|β₀|G₀+|β₁|G₁` | — | `5.25·10⁻³` vs `2.606` |
| B&B replay, 5 segments | `lb = 4.42892819·10⁻⁵`, `nfinal = 0` | identical, **evaluation counts bit-for-bit** |

**Status of the final positivity.** Rigorous modulo one quantified link: the enclosures of `L`, `G₀`, `G₁`, `ψ′(¼)`,
`k₀`, `k₁` and of `f, h₀, h₁, h₂` at the four minima are genuine `mpmath.iv` enclosures; the cover itself is a
Lipschitz branch-and-bound in float64 with a calibrated (not proved) `ε_fp = 10⁻⁸`. Because the cover closed with
`4.4·10⁻⁵` of slack against a target that is half the true infimum, the statement `c > 0` is stable under any uniform
float error up to `4.4·10⁻⁵`. **Honest phrasing: "machine-verified to a rigour equivalent to an interval cover, with a
float-arithmetic allowance exceeded only if float64 error at `10⁻⁵` scale occurred" — not "every leaf minimum was
evaluated in interval arithmetic."** `R154_010 §5` bullet 5 should say *calibrated*, not *justified*, and bullet 3's
"`mpmath.iv` at every leaf minimum" should read "at the four fine-grid minima". That is the only wording repair, and it
does not change the verdict.

---

## 3. What this theorem is

What is now proved is that the Weil quadratic form at `T = ½log3`, restricted to the primitive class `P_T` where the
two polar obstructions are killed, is **strictly positive with an explicit margin**, and the proof consists of a single
inequality between functions of one real variable `τ`: `σ_T(τ) + ν̂(τ) + β₀ĝ₀(τ) + β₁ĝ₁(τ) ≥ 4.43·10⁻⁵`. Everything on
the left is visible. `σ_T` is the archimedean symbol minus the one prime that survives the window, `−v₂cos(τ log2)` —
the arithmetic is *in the inequality*, not hidden in a matrix. `β₀ = 2.0026` is, to `2.6·10⁻³`, the integer `2`: the
dual is paying for exactly the two polar contributions `Φ̂(i/2) + Φ̂(−i/2)` that the primitive class removed, so the
certificate *reconstitutes the explicit formula's pole term* as a Lagrange multiplier. `ν` is a signed measure living
entirely **outside** the window `|u| ≥ 2T`, invisible to `A_T` and free of charge, and it does the lifting; its support
on a lattice is what makes `ν̂` periodic and lets one period of `τ` stand for the whole tail (Lemma D2.3, the round's
method contribution). The contact set is a comb — a broad band in `[0,13]` plus one phase per tail family — which is
complementary slackness of Theorem O drawn on the `τ` line, and Theorem O says this comb can never become all of `R`,
which is why the certificate captures `4.5%` of `λ_min = 9.89·10⁻⁴` and no certificate of this class attains it. Paper
42 proved the same positivity by a Feshbach reduction: a chosen finite-dimensional subspace, a mesh, and a Schur
complement — a statement about an approximation scheme. This one is a statement about the symbol. It is the first
mesh-free, mechanism-visible proof of Weil positivity with a prime coupled, and its honest limit is stated in the same
breath: ~~at `T = log 2` a second, incommensurate contact at `log 3` destroys the periodicity the whole tail argument
rests on~~ **[amended per R154_016: at `T = log 2` a second contact at `log 3` was wrongly believed to
destroy the periodicity the tail argument rests on; it does not. The tail argument needs only the lattice of `ν`.
What the second contact costs is quantitative: at `T = 0.58` the same pipeline reaches `−3.1964·10⁻³` against
`+8.86·10⁻⁵` one step below.]**, and nothing here approaches a sign for `ζ`.

---

## 4. Required repairs (none blocking)

* **W1 (wording, `R154_010 §5`).** "`ε_fp` justified" → "calibrated at 63 points; the cover's `4.4·10⁻⁵` slack is the
  actual guarantee". "interval evaluation of `f` at every B&B leaf minimum" → "at the four fine-grid minima"
  (`nfinal = 0`, so there are no leaf minima — which is the stronger statement and should be said that way).
* **W2.** Say explicitly that only **weak** duality is used, so the theorem does not rest on Theorem D1 / repair `RJ`.
* **W3 (hygiene).** Strip the stale `fine`/`hmin` fields inherited from `lp_q24_it1.pkl` in the archived pkl.
* **W4.** `R154_007`'s three outstanding repairs (§8 corruption, the `3.24·10⁻³` period residual, "interval" → "comb")
  remain owed, as `R154_010 §6` itself states.

## 5. Labels

| item | label |
|---|---|
| `λ_min(A_{½log3}(w_ζ)) ≥ 4.4279281900·10⁻⁵ > 0` on `P_T` | **`PROVED`** — machine-verified, archived, independently replayed |
| Lemma D2.3 (graded periodic tail) | **`PROVED`** |
| weak duality `D_T ≤ λ_min` (the only duality used) | `PROVED` (one line) |
| `β₀ → 2` = the explicit formula's polar term | `DIAGNOSTIC-NUMERIC`, now on a proved object |
| contact set is a comb | `DIAGNOSTIC-NUMERIC` |
| `T = log 2` | `OPEN`; structural obstruction stated and correct |
| any sign for `ζ` | **not claimed**; FATAL rule passed |
