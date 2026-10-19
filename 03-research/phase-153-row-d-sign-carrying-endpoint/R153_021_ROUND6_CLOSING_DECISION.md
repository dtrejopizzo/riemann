# R153.021 — Closing decision, round 6 (the prime-free body W_T and the arithmetic half-space)


## 1. Verdicts of record

| item | statement | label |
|---|---|---|
| separation | `A_T ≥ 0 on P_T ⟺ W_T ⊂ H_w`, `W_T` = joint range of `(x_0, c_F(log n))` on the unit sphere of `P_T` (prime-free), `w_n = Λ(n)/√n` (arithmetic); reduces to `conv W_T` | `PROVED` (trivial reformulation of Weil, made explicit) |
| convexity | closure of `W_{log 2}` convex (AYP on sections + limit); `W_T` itself open question; 4 forms: `OPEN` | `PROVED` (closure) |
| **Lemma 3.1** | for `supp F ⊂ [−T,T]`: `min c_F(a)/‖F‖² = −cos(π/m)`, `max = +cos(π/m)`, `m = ⌈2T/a⌉ + 1`, incl. `a = 2T` (`m=2`, value 0). Jacobi-chain direct integral. Different statement from R147 Lemma A.6 (Galois-orbit min–max); its table coincides with R147_002's refuted "`cos(π/m)` for all `m`" row — to be flagged there. | `PROVED` (new) |
| box vs body | box bound in direction `w_ζ` = `−1.278`; truth `+1.0·10⁻⁷`; the deficit grows with `|v|`. **No projection-only (Ingham/Boas–Kac-type) argument can reach Weil positivity at any `T`.** "100% coupling" tautological; "≥56% three-way" an observation about three relaxations | `PROVED` (deficit) / `DIAGNOSTIC` |
| facet at `w_ζ` | simple exposed point `x(F_min) = (0.0880, 0.0745, 0.0118)`, spectral gap `1.14·10⁻⁵`; quasi-facet (second extreme point 0.33 away, `1.14·10⁻⁵` above the plane) | `DIAGNOSTIC-NUMERIC` |
| Krein bands | `w_3 ∈ [0.6341709, 0.6342883]`, `w_2` band width `4.46·10⁻⁴` (3.8× wider than `w_3`'s, contrary to the construction's text); `w_4` band at `½log5`: `[0.3465729, 0.3465736]`, width `7·10⁻⁷`. In every case the distance to the upper edge equals `λ_min/(2x_n(F_min))` to 0.2–0.3% (Hellmann–Feynman). **"The weights sit at the edge" carries no information beyond `λ_min ≈ 0`**; the percentages are not scale-invariant and are withdrawn. | `DIAGNOSTIC-NUMERIC`; "edge" reading `WITHDRAWN` |
| **the one curvature datum** | apex of the joint `(v_2, v_3)` admissible sliver at `v_2* = 0.4901375`; `w_2` lies `8.5·10⁻⁶` below it, 12.4× the first-order normal distance `6.8·10⁻⁷` — not predicted by `λ` alone | `DIAGNOSTIC-NUMERIC` (promoted; meaning OPEN) |
| `½log5` | `λ_min(A_{½log5}|P_T) ≤ 3.2·10⁻¹²` (Galerkin upper bound; roundoff floor `1.4·10⁻¹⁵`); `x_4(F_min) = 2.8·10⁻⁵` (K-stable, not zero); construction's "`w_4` at the optimum / flat direction" **REFUTED** (`λ_max/λ(w_4) = 10`; same edge law). (P153.3) not answered, only bounded. | `DIAGNOSTIC-NUMERIC`; §7 text `WITHDRAWN` |
| falsifier | on the correct body (doubled Gamma, four-moment space) `Ξ_{0.45}` exits `H` at `log 2` (`−5.07·10⁻²`); the construction's leading comparison against the `ζ` body is illegitimate | `DIAGNOSTIC-NUMERIC`; §0 comparison `WITHDRAWN` |
| T6 | "no prime-free closed law" is asserted, not supported by the non-commutativity remark (`‖[S_2,S_3]‖_rel = 0.10`) | `OPEN` (expectation only) |

FATAL rule clean; no sign for `ζ` beyond `log 2`; Paper 42 cited for containment.

## 2. Reading
Round 6 delivers the exact geometry/arithmetic separation and one durable theorem: the body is not the box, so every argument that
uses only axis-wise autocorrelation bounds (Ingham, Boas–Kac, `cos(π/m)`) is dead for Weil positivity at every `T` — the positivity
lives entirely in the joint constraints between `c_F(log 2)`, `c_F(log 3)` and the Gamma energy. The "weights at the edge" picture
is `λ_min ≈ 0` restated and is withdrawn. The single datum that is not first-order — `w_2` sitting `8.5·10⁻⁶` below the apex of the
admissible sliver, twelve times the normal distance — is recorded as the only review worth a thought, with no interpretation offered.

## 3. Decision
Round 6 closed. Phase 153 closed; row D unchanged. Repairs R1–R9 of R153_020 recorded as binding on R153_019. New open:
(P153.16) meaning of the apex offset; (P153.17) closed form for `λ_min(M_0 − v·S)` on `P_T` — the prime-free law — status unknown.
