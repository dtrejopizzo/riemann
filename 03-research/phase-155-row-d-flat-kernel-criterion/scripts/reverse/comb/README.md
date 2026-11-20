# `scripts/reverse/comb/` — the comb-vanishing LP (R155_016)

Corollary D.2 of `R155_013` says: if a compactly supported `C²` flat-top weight `w`
satisfies the **comb equalities** `w(log n) = 0` for every prime power `n` with
`2T < log n ≤ U`, then `E_at(w) = 0` and Theorem D closes the tail at
`τ_stop = O(D(w)^{1/2}) ≈ 10²`. This directory runs the LP over exactly that class.

`DIAGNOSTIC` throughout: the LP oracle is the first 1000 zeros; the prime side
(`comblib.f_prime`, full prime-power sum to `e^{Umax}`, GL order 12 on knot-aligned
panels, exact analytic `K`-tail beyond `Umax`) is evaluated at the argmin as a check.

## Files

| file | what |
|---|---|
| `comblib.py` | the class. `WinC(T, U, M)`: `w ≡ 1` on `[−2T,2T]`, `w = B + Σ_{j≥2} x_j β((u−u_j)/h)` on `u > 2T`, `h = 2T/M`, `supp w ⊂ [−U,U]`, globally `C²`. The three unit coefficients of `B` are **forced** by `C²` matching at the edge. Zero side `f_w(τ) = 4∫ w cos(τu) Z(u) du`; `Dw_and_taustop` = Theorem D constants; `f_prime` = prime side. |
| `count.py` | equalities `m`, dof, rank, nullity and least-squares residual of the comb system, for `T ∈ {½log3, 0.58, 0.62, log2}`, `U ∈ {3,…,8}`, `M ∈ {24,48}`. → `count.json` |
| `lp.py` | the LP. The equalities are eliminated exactly (`x = x_p + N z`, `N = null(A)`), then `max_z min_τ f_w(τ)` on `[0, TAUMAX]` with cutting planes, `‖x‖_∞ ≤ 3`, `‖x‖₁ ≤ 60`. → `lp_<NAME>.json` |

**Why the `ψ`-edge basis of `../d1000/dlib.py` (round R155_011) could not be reused:** `ψ_s(v) = (1+sv+s²v²/2)e^{−sv}`
has **infinite** support, so `E_at(w)` is an infinite sum and the comb conditions could never be a
finite set. Compact support is a hypothesis of Cor. D.2, not a convenience.

## Commands (single process, one at a time)

```
python3 count.py                                              # 1.0 s
python3 lp.py c_log3h_U6_b   0.5493061443340549 6.0 24 1 115  # 21 s
python3 lp.py c_log3h_U5_b   0.5493061443340549 5.0 24 1 115  # 19 s
python3 lp.py c_log3h_U4_b   0.5493061443340549 4.0 24 1 115  # 15 s
python3 lp.py c_log3h_U6_w   0.5493061443340549 6.0 24 0 115  # 20 s   (β = (2,0))
python3 lp.py c_log3h_U6_nc  0.5493061443340549 6.0 24 1 115 nocomb   # 50 s (control)
python3 lp.py c_log3h_M48    0.5493061443340549 6.0 48 1 200  # 87 s
python3 lp.py c_w058_M48     0.58               6.0 48 1 200  # 75 s
python3 lp.py c_w062_M48     0.62               6.0 48 1 200  # 65 s
python3 lp.py c_wlog2_M48    0.6931471805599453 6.0 48 1 200  # 41 s
```

Total ≈ 6.5 min of wall time, one process at a time.
Arguments: `NAME T U M BETA [TAUMAX] [nocomb]`; `BETA=1` frees `(β₀−2, β₁)`, `BETA=0` fixes `β=(2,0)`.

## Result in one line

**Every window is negative**; the comb equalities are always *feasible* (residual `0`) but the
null space **saturates** at `U ≈ 5` (`M=24`) / `U ≈ 6` (`M=48`) — comb-vanishing ⟹ effectively
bounded support. See `../../../03-research/phase-155-row-d-flat-kernel-criterion/R155_016_COMB_VANISHING_LP.md`.
