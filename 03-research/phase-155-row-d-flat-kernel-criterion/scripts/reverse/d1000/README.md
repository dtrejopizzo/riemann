# `scripts/reverse/d1000` — R155_011: build `D` against a universe of 1000 zeros

Aim: restrict the zero universe to 1000 zeros, build the `D` satisfied by exactly those zeros, and
read off from it what shape `D` must have.

Protocol (non-circular by construction, **"zeros to FIND, primes to PROVE"**):

1. **FIND.** An LP over C² flat-top weights `w ∈ W_T` maximises `min_{τ∈[0,τ_max]} f_w(τ)` where the
 objective is evaluated **only** from a finite zero table (Odlyzko, first `N` zeros). The LP never
 sees a prime.
2. **PROVE.** The *same* `f_w` is recomputed from the prime/Γ side of Theorem Z, eq. (7.2)
 (`C₀ + ∫(1−w cos τu)K − Σ_n v_n w(log n)cos(τ log n) + 2∫ w cosh(u/2)cos τu`), with the full
 prime-power sum to `e^{U_max}` and Gauss–Legendre panels; the two sides must agree, and the
 *prime-side* number is the only one that could ever enter a proof.

Everything produced here is `DIAGNOSTIC` unless the report says otherwise.

## the identity that makes this cheap

For even `w` supported in `[−U,U]` and zeros `±γ`,
```
f_w(τ) = Σ_ρ ŵ(τ−γ_ρ) = 4 ∫_0^U w(u) cos(τu) Z(u) du, Z(u) = Σ_{γ>0} cos(γ u).
```
`Z` is computed **once** on a knot-aligned Gauss–Legendre panel set; every LP row and every fine-grid
evaluation is then a single matrix product. Checked against the closed-form transforms of
`revlib2.zero_side` to `1.8·10⁻¹¹`.

## files
| file | what |
|---|---|
| `dlib.py` | window geometry (`ψ`-edge + cubic B-spline lattice of step `h = 2T/M`, `M = 24`; **NOT** "above the Theorem-N/TK ceiling" — see R155_012 §9 / R155_011 §2.1 amended: `prop:TK`/`thm:N` concern lattice-supported measures and do not cover flat-top classes), the panel quadrature, `Z(u)`, `f_w`, `ŵ`, the `‖f″‖_∞` bound and the `|Z|` envelope |
| `primeside.py` | prime/Γ side of (7.2): `f_prime` (per-B-spline, GL order 800) and `f_prime_fast` (one shared panel set; agrees to `2.7·10⁻¹⁰`) |
| `run_d1000.py` | the LP + cutting planes + the certified interval minimum |
| `check.py` | the prime-side re-evaluation, the 10/100/1000-zero residual ladder, the far scan, the norm budget `E₁+E₂+E₃` |
| `insight.py` | INSIGHT (i)–(v): kernel lobes, contacts vs zero gaps, which zeros carry the value, `w` in `u` vs `log p`, and the `T`-dependence |
| `runall.sh` | the exact command sequence below |

## exact commands
```
python3 run_d1000.py NAME T M NZEROS L BINF BETA [TAUMAX]
python3 check.py NAME FAR
python3 insight.py NAME...
```
see `runall.sh`; runtimes and outputs (`d_*.json`, `chk_*.json`, `insight.json`) are archived beside
the scripts, and the console log is `runall.log`.

## certification used for the reported minima
`f_w` is band-limited of type `U = sup supp w`, so (Paper 46 `lem:bern`, in the sharper
`‖f″‖_∞δ²/8` form of its own proof) `min_ℝ f ≥ min_grid f − ‖f″‖_∞ δ²/8`, and
`‖f″‖_∞ ≤ 4∫u²|w(u)||Z(u)|du =: B₂` is computed from the same quadrature with a rigorous running-max
envelope for `|Z|`. **This certifies the minimum over the LP's τ-interval only**, never over `ℝ`.

## exact command sequence and runtimes (one core, numpy/scipy, `runall.sh`)
```
python3 run_d1000.py log3h 0.5493061443340548 24 1000 60 3 0 # 28 s lambda^W control (beta fixed at (2,0))
python3 run_d1000.py log3h_b 0.5493061443340548 24 1000 60 3 1 # 26 s beta free
python3 run_d1000.py log3h_b60 0.5493061443340548 24 1000 60 3 1 60 # 64 s same, domain [0,60]
python3 run_d1000.py log3h_z10 0.5493061443340548 24 10 60 3 1 # 12 s control: 10 zeros
python3 run_d1000.py log3h_z100 0.5493061443340548 24 100 60 3 1 # 13 s control: 100 zeros
python3 run_d1000.py w058 0.58 24 1000 60 3 1 # 61 s
python3 run_d1000.py w062 0.62 24 1000 60 3 1 # 47 s
python3 run_d1000.py wlog2 0.6931471805599453 24 1000 60 3 1 # 44 s
for n in log3h log3h_b log3h_b60 log3h_z10 log3h_z100 w058 w062 wlog2; do
 python3 check.py $n 300 > chk_$n.log; done # ~210 s each
python3 insight.py log3h_b log3h_b60 w058 w062 wlog2 # ~120 s
python3 tables.py # renders the report's tables
```
Arguments: `NAME T M NZEROS L_budget BINF BETA [TAUMAX]`; `L_budget` bounds `Σ|y|+Σ|x|`, `BINF`
bounds each `|x_j|` (an `‖w‖_∞` budget), `BETA=1` frees the two primitivity multipliers `(β₀−2, β₁)`,
`TAUMAX` overrides the multiplier-free envelope `2πe^{A_T}`.

Total single-process wall time ≈ 40 min, of which the LPs are ≈ 5 min and the prime-side checks
≈ 30 min (the `τ ≤ 300` far scan against 93 372 prime powers). Declared as a deviation from the
 10-minute budget in `R155_011 §2.5`.

## outputs
`d_NAME.json` (LP optimum: `y`, `x`, `β`, the cutting-plane history, norms, `B₂`, certified value),
`chk_NAME.json` (prime-side minima, the 10/100/1000 residual ladder, the far scan, `E₁+E₂+E₃`),
`insight.json` (kernel lobes, contacts, per-zero term rankings, `w` near each `log n`, profiles),
`runall.log` (the console log of the whole run).

## labels
Everything here is `DIAGNOSTIC`. The prime-side numbers are *evaluations* in double precision with
a rigorous grid slack but no interval arithmetic, and they are minima over a finite τ-interval, never
over `ℝ`: they are not certificates and they bound neither `λ^W` nor `λ^P`. See `R155_011 §7`.

## added (R155_012 repairs + R155_013)
| file | what |
|---|---|
| `amend.py` → `amend.json` | the recomputations the audit forced: **true** negative-lobe counts on `[0,60]` (the old `12` was an `insight.py` `[:24]` artefact), the honest `‖ν_w‖_TV` and `log₁₀τ_env` (`A_T` restored; a.c. densities combined before `|·|`; atoms restricted to `log n > 2T`), the honest Bernstein pad, and `D(w) = D_K + D_c` with `τ_stop` of `R155_013` Theorem D |
| `dense.py` → `dense_NAME.json` | a **genuine** `lem:bern` enclosure: the prime side at every node of a dense grid of the whole LP interval, pad `B₂δ²/8`. At `log3h_b`, `δ = 2.5·10⁻⁴`: `min ≥ +1.3486·10⁻³` (30 s) |
| `p3.py` → `p3_NAME.json`, `p3.log` | **P3**: the bounded-profile class `0 ≤ w ≤ 1` (pointwise on an `h/8` grid), `[0,60]`, four windows × (`β` free, `β=(2,0)`). All eight values negative; see `R155_013 §6` |

`check.py` and `insight.py` have been amended in place (marker
`[amended per R155_012]`); `check.py` now reports `pad_localised_NOT_an_enclosure`
beside a genuine coarse-grid enclosure, and `TV_exact`/`A_T` beside the old `E₁,E₂,E₃`.
**The `M = 24` lattice is NOT "above the Theorem-N/TK ceiling"**: `prop:TK`/`thm:N` cover
lattice-supported measures and do not have the flat-top class in their hypotheses.

## Other files in this folder

- `*.json` (25 files, e.g. `chk_log3h.json`) — output data files.
- `*.log` (8 files, e.g. `chk_log3h.log`) — run logs.
