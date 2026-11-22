# R146.005 — Closing decision, phase 146 (the degree form on `Z[Frob]` with a count interpretation)

1–2 in place), R146_002 (14 MAJOR, no FATAL), R146_003, R146_004 (confirmation: repairs discharged; tower
result real but mis-framed: C-A, C-B, C-C, C-I MAJOR). Own check: the `−10` witness from the
definitions; the Toeplitz threshold `2/(√p+1)` as the spectral minimum of the geometric kernel.*

## 1. Results of record
| item | statement | label |
|---|---|---|
| D.45.1–2 | a finite symmetric form on `Z⟨Frob_n⟩` extending Paper 44's off-diagonal Gram exists for every finite diagonal choice; it is **not a count**: degenerate (`L(6,10) = 0`) and indefinite (`Q(5Frob_6 − 4Frob_10) = −10`); it equals Paper 47's `2ab − W` with the zero sum deleted, hence **zero-blind and `Ξ_a`-uniform** | PROVED |
| D.45.4–5 | model: `[Γ_{φ+ψ}] = [Γ_φ]+[Γ_ψ] − F_2 + 2⟨φ,ψ⟩F_1`; `Γ_{1+π}` effective with a negative coefficient in the Frobenius basis; the arithmetic sum classes pass the cosh test structurally (correction in the ruling plane) — a non-detecting test by construction | PROVED / CLASSICAL |
| **D.47.2** | **the Frobenius diagonal, from Paper 44 Thm 8bis.1b: archimedean part `n`-independent (cancels exactly in differences); `𝔡(m) − 𝔡(n)` supported on `P(m) △ P(n)`; `P(m) = P(n) ⟹ δ_m = δ_n` exactly at every `(ε, N)`, both conventions** — the first computed (not chosen) diagonal datum in row D; new in the corpus | PROVED (one-line UFD gap C-D) |
| D.47.4 | single-prime tower Gram `G^{(p)} = c_p(log p)[T(ρ) + (τ_p − 1)I]`, `ρ = p^{−½}`, `c_p = V_N` cancels in `τ_p`; PSD ⟺ `τ_p ≥ 2/(√p+1)`; off-diagonal un-normalizes to `p^{min}·log p` ↔ model `q^{min}N_{|a−b|}` | PROVED **on the domain where (8bis.2a)'s archimedean indicator vanishes** (C-B; this restriction) |
| D.47.7 | "never PSD at any chart" — **withdrawn as stated** (C-A): outside the valid domain a PSD corner exists (`S_f = {2,p}, N = 1, ε = 0.34`); inside it the form is eventually **NSD** for large `N` (C-G) — a magnitude-only object, so its sign carries no information about `ξ` (phase 60 / P122.028; C-I) | REFUTED as stated / RESTRICTED |
| D.47.x `Ξ_a` | "A3 does not enter" — **withdrawn** (C-C): no `Ξ_a` diagonal was computed; Doc 131 Thm 6.7 decides single-prime positivity iff `a = ½`, maximally `Ξ_a`-sensitive | WITHDRAWN |
| D.44.4 | Hasse test with `N_1 ↔ Λ(ℓ)` | HEURISTIC |
| O-46.6 | `Frob ⋆ Δ^rad` on the tower as phase 147 | REFUTED as chartered (adds a `Γ`-datum, inside P122.028's barred list; = phase 137 D.12) |

## 2. What the phase established
1. The additive structure Weil uses (`deg(m+nπ) = #ker`) has no realization on `Spec Z` by one-variable
   objects: the formal sums carry a form that is `2ab − W` minus the zero sum — blind to zeros. The
   multiplicative semigroup is complete and fully counted; the sign is not in it.
2. The Frobenius diagonal is computable and its differences are exact: `P(m) = P(n) ⟹ δ_m = δ_n`. This is
   real, new, and (so far) sign-free: on a single-prime tower everything is a function of `p`, `log p`,
   `p^{−k/2}` and the chart, i.e. pure magnitude, which the corpus proves three times cannot decide the sign.
3. **Diagnosis after 145–146, corrected by the audit:** "the sign lives in the diagonal counterterm
   of the additive structure `Spec Z` lacks" is half right — it locates the slot (the `H¹`/genus part of the
   self-intersection, which is item (21)'s archimedean object plus a finite-place divergence) — and half
   artifact: nothing built in the slot so far distinguishes `ξ` from `Ξ_a`.

## 3. Decision
Phase 146 closed; no label change. The Frobenius-tower thread is **closed on the negative** unless an
object carrying an explicit **phase datum** (Doc 131's `α`, unimodularity) is added — the corpus's
admissibility rule leaves no other opening on this page, and there is currently no construction
for it. Residue C-D (UFD line), C-F (README constants), C-G (W-a screen on the NSD regime) carried to Part III.

## 4. Programme-level state
Phases 135–146 have converted row D from "find `h⁰`" into a precise map: the intersection theory of the
arithmetic square is complete (explicit formula); its effective cone is the cone of Frobenius graphs and is
provably too thin (`s < 1`, also on curves); the missing ingredient is the ring structure on correspondences
(the `+`), which `Spec Z` does not have; the diagonal is computable but magnitude-only. Every construction
inside the frame is either a restatement of RH or `Ξ_a`-uniform. The next genuine move must add a
non-magnitude, non-`Γ` datum with Euler-product content — the "phase" of the unimodular roots — and no such
object exists in the corpus or in the literature the corpus has read. Options: (i) build the
phase-datum object (Doc 131's `α` promoted to a class on the square, with its `Ξ_a` version `α_± = p^{±a}`
falsifying); (ii) pause row D at the map and write Paper 47 Part III as the record of the reduction and the
obstructions (a mathematical contribution in itself: T1, T2, the frame defect theorem, the trace-cone
restatement, the computed diagonal); (iii) both, in that order.
