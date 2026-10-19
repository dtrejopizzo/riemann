# scripts/r7a — round 7a, the prolate concentration floor

`r7a_01_floor.py` — Theorem P / Corollary P3, grid (trapezoid-quadrature) evaluation of `Λ_k(c)`.
Runtime **6.4 s**. Outputs `r7a_01.json`.

`r7a_02_closedform.py` — Corollary P1, quadrature-free closed-form `Λ*_k(c)` (finite series of
rationals times powers of `c`). Runtime **2 s**. Outputs `r7a_02.json`.

[amended 2026-09-22 per R155_048]

* Runtimes above are the measured rerun values, not the `~55 s` (`~50 s` + `~5 s`) originally
  estimated for `r7a_01_floor.py` + `r7a_02_closedform.py`.
* `r7a_02_closedform.py`'s series sum (`Lstar`) overflows in `c**(2*j+1)` for large `τ₁` (`c ≳ 100`,
  i.e. `c^159` at `j=79`); those `τ₁` are silently skipped in the scan. The optimum sits at
  `τ₁ ≈ 6.4`, so the reported `n₋` bounds (`5/7/8`) are unaffected.
* `Λ*_k(c)` is evaluated as the partial sum over `j < 80` (`J=80`), i.e. a *lower* bound on the true
  infinite series; the omitted tail is `< 10⁻¹⁷⁰`, so the `PROVED` inequality `λ_k ≤ Λ*_k` is not
  endangered by the truncation.
