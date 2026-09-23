# `scripts/r4a/` — the even-sector Schur complement at `log 2` (phase 155, round 4a, `R155_032`)

Structure of the prime form `Π_T` on the **even** archimedean eigenbasis of `A_∞|P_T`, and rigorous
interval-arithmetic positive-definiteness of the complete Weil form `W_T = A_∞ + Π_T` on explicit
**nested even subspaces** `E_k = span{e₁,…,e_{2k−1}}` at `T = log 2` (and `0.62`, `0.65`).
Reuses `scripts/r3a/arch_core.py` **unmodified** (imported by path) and the proof structure of
`scripts/r3c/r3c_04_enclosure_iv.py`; **no file in `scripts/r3a`, `r3b`, `r3c` is touched.**

| file | what it does | runtime |
|---|---|---|
| `r4a_01_structure.py` | `N = 18` at `T ∈ {0.62, 0.65, log 2}` and `N = 36` at `log 2`: archimedean spectrum on `P_T`, parity classification, `Π_T` on the first 8 even eigenvectors, the two shift forms `−v_2C(log2)`, `−v_3C(log3)` separately, the identity `b = P_VΠ_TF*` (checked to `4.7e−15`), `b`'s components, and the Galerkin trend `λ_min(W\|E_k)` for all `k` → `r4a_01.json`, **including the archived Legendre coefficient vectors of every even eigenvector** (`even_coef`) | **25.0 s** |
| `r4a_lib.py` | the enclosure library: exact `Fraction` Legendre algebra, exact interval polynomial autocorrelation `q`, Chebyshev bound `G ≤ G₁s`, **the two panel functionals `L_lo, L_hi` computed once** (affine convex/concave sandwich of `K`), closed forms for `C₀` and `∫_{2T}^∞K`, interval prime atoms, pole defect paid for; plus interval Cholesky and a bisection lower bound on `λ_min` | (library) |
| `r4a_02_nested_enclosure.py` | loads the archived vectors, builds the interval matrix of `W_T` on `E_k` by **polarisation** (only quadratic values are enclosed, so `G ≥ 0` always holds), encloses the Gram matrix, and certifies `λ_min(E_k) ≥ μ` by interval Cholesky → `r4a_02_<T>_M<panels>_k<kmax>.json` (filename keyed by `(T, panels, kmax)` per `R155_036 §3.6`, so a rerun at different `PANELS`/`KMAX` cannot overwrite an archived certificate) | `log 2`, `M = 16000`, `k ≤ 7`: **118.9 s**; `M = 5000`, `k ≤ 5`: `49.6 s`; `M = 1500`, `k ≤ 3`: `12 s`; `0.62` / `0.65`, `M = 4000`, `k ≤ 5`: `32.1 s` / `37.7 s` |

`r4a_01` is `DIAGNOSTIC` (double precision, Galerkin; Galerkin eigenvalues are **upper** bounds on
infima) except the identity `b = P_VΠ_TF*`, which is proved in `R155_032 §2` and here only checked.
`r4a_02` is **rigorous**: `mpmath` `mp.iv` at `dps = 60`, no error budget, every truncation bounded
in closed form. Certified at `T = log 2`: `λ_min(W\|E_k) ≥ 3.421189e−2, 2.113566e−3, 4.045259e−4,
9.076318e−5, 4.095108e−5, 2.215585e−5, 6.568676e−6` for `k = 1…7`.
**This is positivity on explicit finite-dimensional subspaces, NOT positivity of the form.**

Reproduce (single process):
```
python3 r4a_01_structure.py                                        # 25 s
R4A_PANELS=16000 R4A_KMAX=7 python3 r4a_02_nested_enclosure.py     # 119 s  (log 2)
R4A_T=0.62 R4A_PANELS=4000 R4A_KMAX=5 python3 r4a_02_nested_enclosure.py   # 32 s
R4A_T=0.65 R4A_PANELS=4000 R4A_KMAX=5 python3 r4a_02_nested_enclosure.py   # 38 s
```
`R4A_PANELS=5000 R4A_KMAX=5` reproduces `k ≤ 5` at `log 2` inside the 60 s guideline.
