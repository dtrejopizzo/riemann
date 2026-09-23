# `scripts/r3a/` — archimedean threshold (phase 155, round 3a, `R155_023`)

Galerkin computation of the bottom of the **archimedean block** `A_inf = pole + gamma` of the Weil
form on `L^2(-T,T)`, in an orthonormal Legendre basis. Paper 47 normalisation. Single process,
double precision, no interval arithmetic: everything produced here is `DIAGNOSTIC`.

| file | what it does | runtime |
|---|---|---|
| `arch_core.py` | module: `C0`, Levy density `K`, tail `Ktail`, Bernstein `phi`, Legendre basis, autocorrelation matrix `C(u)`, `gamma_matrix`, `pole_matrix`, `prime_matrix`, `restrict` (to `P_T`) | — |
| `r3a_01_validate.py` | (i) Levy form of the Gamma block vs the direct `(1/2pi) int m |Fhat|^2` (1.867, 2.058 at cutoffs 500, 2000 against the Levy value 2.145: the log tail of `m` makes convergence slow but monotone; at `N = 10` the same check gives 1.0118, 1.0148, 1.0157 (cutoff 500, 2000, 8000) against 1.0161); (ii) `lam_min(W_T) > 0` at eight windows `T <= log 2`, reproducing the known theorem, and `lam_min(a_T|P_T)(log 2) = 9.94e-7` | ~55 s |
| `r3a_02_scan.py T1 T2 ...` | table of `lam^inf_min`, `lam^{inf,P}_min`, negative-eigenvalue counts, `||P_T||`, `A_T`, `lam_min(a_T|P_T)`, `lam_min(W_T)` | ~4 s per `T` |
| `r3a_03_threshold.py` | `tau_0` (root of `m`) and 9-step bisections for `T*_inf` and `T*_{inf,P}` | ~65 s |
| `r3a_04_groundstate.py` | prime term evaluated on the two archimedean ground states; deficits; trivial bound | ~9 s |

Accuracy: `N = 18` basis functions, `nu = 120` Gauss nodes per panel (3 panels on `[0,2T]`),
`nq = 100` nodes for `C(u)`. Values stable to `2.5e-5` against `N = 36 / nu = 400 / nq = 220`.

Reproduce: `python3 r3a_01_validate.py`; `python3 r3a_02_scan.py 0.30 0.32 ... 0.80` (in chunks of
nine to stay under 60 s); `python3 r3a_03_threshold.py`; `python3 r3a_04_groundstate.py`.
