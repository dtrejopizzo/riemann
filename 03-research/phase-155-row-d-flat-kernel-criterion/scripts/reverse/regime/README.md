# `scripts/reverse/regime/` — R155.008, the 100-window regime law

Companion code for `03-research/phase-155-row-d-flat-kernel-criterion/R155_008_REGIME_LAW_100_WINDOWS.md`.
Everything here is **DIAGNOSTIC**: the LP is trained on Odlyzko's table of zeros, which is
circular as a tool (`phase-4-krein-space-realization/proofs/00-PROOF-LOG.md:168`, `phase-136-row-d-map/MAP_1:141`
ES-2). No statement about RH and no sign claim for any `T > log 2` is made or implied.

## what is fixed across all windows

`reglib.Win(T, h=0.25, J=30)`: `w ≡ 1` on `[−2T,2T]`; outside,
`w = Σ_{i} y_i ψ_{s_i}(u−2T) + Σ_{j=2..31} x_j β((u−u_j)/h)`, `ψ_s(v)=(1+sv+s²v²/2)e^{−sv}`,
`s ∈ {2.5,4,8,16}`, `β` = cardinal cubic B-spline, `u_j = 2T + jh`, `h = 0.25` **fixed**
(not `2T/M`), `Σ_i y_i = 1` (so `w` is C² across the edge, `ŵ = O(t⁻⁴)`).
Support `U = 2T + 8.25`. Budget `Σ|y|+Σ|x| ≤ L`, `L ∈ {5, 20}`.
Because `h`, `J` and the shape family do not depend on `T`, the admissible set is literally the
same in the variable `v = u − 2T` at every window — this is the audit repair `R155_006 §5`
("`L` is basis- and `M`-dependent"); in addition `‖w‖_∞` and `∫|w|` are reported for every run.

## audit repairs adopted (`R155_006`)

| repair | where |
|---|---|
| Gauss–Legendre order 800 on the prime-side B-spline integrals | `reglib.f_prime_side(..., gl_n=800)` |
| Bernstein grid lemma `min_R f ≥ min_grid f − ½U²‖f‖_∞δ²` | `reglib.bernstein_slack`, `reglib.refine_min` |
| every reported value re-certified on a `0.005` grid | `run_regime.py` (`c_fine`), LP grid is `0.02` |
| in-regime fitting only | `fit_regime.py` (§4 fits and §6 extrapolation never cross an entry) |
| `≥ C¹` across the edge | `Σ y_i = 1` is an equality constraint of every LP |
| no "positive" reading unless certified by both sides | `crosscheck_regime.py`; nothing positive was found |
| reuse `revlib2.py` / `lp2.py` | `reglib` imports both; `reglib.zero_side` reproduces `revlib2.zero_side` to `7·10⁻¹⁰` and is 1.4× faster |

## files

| file | what |
|---|---|
| `reglib.py` | the fixed class, fast zero-side sums, profile statistics, Bernstein certification, prime/Γ side (GL 800), `A_T`, `N_T`, prime-entry table |
| `resid_check.py` | how many zeros are needed: optimise at `Γ=800`, re-evaluate at `Γ = 400…20000` |
| `run_regime.py` | the 103-window run → `regime_windows.json`, `../regime_table.csv` |
| `fit_regime.py` | §4 in-regime fits, §5 jump law, §6 extrapolation → `fit_regime.json` |
| `crosscheck_regime.py` | Theorem-Z cross-check, one window per regime → `crosscheck_regime.json` |
| `toy10.py` | §7bis cancellation budget: `f_w` from `1,2,5,10,10²,10³,10⁴,10⁵` zeros vs the prime/Γ side |

## exact commands and runtimes (one core, numpy 1.26 / scipy 1.11)

```
python3 -u resid_check.py # 105 s
python3 -u run_regime.py # 520 s (103 windows, ~5 s each)
python3 -u fit_regime.py # 2 s
python3 -u crosscheck_regime.py # 50 s
python3 -u toy10.py # 70 s
```

`zeros1.txt` (the parent directory) is Odlyzko's first 100 000 zeros,
`md5 b7b8be60df6d46e78cd60874f9fd76c0`; `resid_check.py` shows that only the
**491 zeros below 800** matter for this class (adding zeros up to `γ = 20000`
moves `f_w` by `< 1·10⁻⁹`), which is why `run_regime.py` uses `Γ = 800`.

## the prime-sum cutoff (new, and it matters)

`crosscheck_regime.py` and `toy10.py` use `NPRIME = 600000` prime powers, **not** `e^U`. The `ψ_s`
edge functions are not compactly supported, and the LP uses them with large cancelling coefficients,
so truncating the prime sum at `e^U` (as `revlib2`'s own driver does) leaves a systematic
`1.60·10⁻⁴` disagreement between the two sides of Theorem Z — larger than the corpus's certified
`λ_min(A_{½log3}) = 8.86·10⁻⁵`. Measured at `½log3`: cutoff `e^U = 11487 / 4·10⁴ / 1.5·10⁵ / 6·10⁵`
gives `1.60e−4 / 1.71e−5 / 1.54e−6 / 1.16e−7`; the Gauss–Legendre order (200/800/3000) is irrelevant
at this `h`. `analysis_primecut_eU.log` is the run with the `e^U` cutoff, kept as the record of the
artefact; `analysis2.log` is the corrected run used in `R155_008`.

## Other files in this folder

- `domain_probe.json` — output data.
- `domain_probe.py` — script.
