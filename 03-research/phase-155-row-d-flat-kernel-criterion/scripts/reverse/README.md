# phase 155 — REVERSE-ENGINEERING track: scripts

Reverse-engineer the closing object `w_T` of Paper 47 §7 (Theorem Z) from the
*known* zeros of ζ, treating them as training data.  Everything here is
**DIAGNOSTIC** (double precision, finite grids, truncated zero lists).
No statement about RH or about a sign for `T > log 2` is made or implied.

## zeros
`zeros1.txt` — Odlyzko's table of the first 100 000 zeros
(<https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1>, downloaded
2026-09-21, `md5 b7b8be60df6d46e78cd60874f9fd76c0`, 1.8 MB).
Ordinates `γ` to 9 decimals, `γ_1 = 14.134725142`, `γ_100000 = 74920.827498994`.
Precision of each entry ≈ `10^-9`; that is the only precision claim made for them.

## files
| file | what |
|---|---|
| `revlib.py` | conventions, `m(τ)`, `C₀`, `K(u)`, prime powers, **basis 1** (exponential columns `e^{-s(|u|-2T)}`, `s>1/2`), zero-side sums with a near/far split, prime/Γ side of Theorem Z |
| `revlib2.py` | **basis 2** (the one used): `ψ_s(v)=(1+sv+s²v²/2)e^{-sv}` edge functions (C² across the window edge) + cardinal cubic B-splines on the lattice `u_j = 2T + j·2T/M`; all transforms analytic; prime/Γ side |
| `lp2.py` | the LP (max `c` s.t. `f^known_w(τ_i) ≥ c`), `Σ|·|`-budget `L`, edge constraint `Σ y_i = 1` |
| `run_lp.py` | TASK 1 with basis 1 (the negative control) |
| `run_window.py` | TASK 1 with basis 2, one window per run |
| `crosscheck.py` | TASK 2: zero side vs prime/Γ side of Theorem Z |
| `extrapolate.py` | TASK 4: fit the profile on `T ≤ 0.68`, predict at `log 2` and `0.80` |
| `t_sanity.py` | Theorem Z identity check on a hand-made C² weight |

## exact commands and runtimes (one core, numpy 1.26 / scipy 1.11)
```
curl -s -o zeros1.txt https://www-users.cse.umn.edu/~odlyzko/zeta_tables/zeros1   # 2 s
python3 t_sanity.py                                    #   5 s
python3 run_lp.py lp_results.json                      # 280 s   (basis 1, the negative control, all 7 windows)
python3 run_window.py log3h 0.5493061443340548         #  15 s
python3 run_window.py 058   0.58                       #  60 s
python3 run_window.py 058_M16 0.58 16                  #  70 s
python3 run_window.py 062   0.62                       #  85 s
python3 run_window.py 065   0.65                       #  95 s
python3 run_window.py log2  0.6931471805599453         #  90 s
python3 run_window.py 075   0.75                       # 260 s
python3 run_window.py 080   0.80                       # 270 s
python3 crosscheck.py log3h 2000.0                     # 300 s  (two zero-side passes, Gamma=6000 and 74920)
python3 crosscheck.py log3h 20.0                       # 300 s
python3 extrapolate.py 20.0                            # 330 s
```
Outputs `win_*.json`, `xc_*.json`, `extrap_*.json` are archived beside the scripts.

## labels
Everything produced here is `DIAGNOSTIC`: double precision, a finite `τ`-grid whose values are
optimistic by a factor `≈2` (see `R155_005` §3.1), a truncated zero table, and no tail lemma beyond
`τ_env`. The LP is trained on a table of zeros and therefore cannot enter a proof
(`phase-4/00-PROOF-LOG:168`, `phase-136/MAP_1:141` ES-2). `zeros1.txt` is kept uncompressed so the
scripts run as archived.
