# Row D — the reduced statement (2026-09-23)

Status: **synthesis of record after phases 134–156. No new theorem, no label change.** Every line cites a labelled
statement of Paper 46 (`04-papers/46-row-d-the-sign/main.md`), Paper 47 (`04-papers/47-row-d-dual-certificates/main.tex`,
84 pp.) or a phase file. Row D has no label. No sign is proved for ζ at any window beyond those listed in §3.

---

## §1 What row D is, and its single remaining content

Row D (the sign of Weil's method over `Spec Z`) is RH. Each of the following is equivalent to RH:

| # | form | source |
|---|---|---|
| E1 | `∀T: λ^W_T ≥ 0` (complete Weil form `eq:W` on `L²(I_T)`) | Weil; P47 §1 |
| E2 | `∀T: λ^A_T = λ_min(A_T\|P_T) ≥ 0` (primitive form) | P45 Thm 10.4, Bombieri 2000 Thm 1 (global, not effective in `T`) |
| E3 | `∀T:` there is a flat-top certificate, i.e. a one-sided smoothing of the zero measure | P47 `thm:Z`, `cor:RH` (proof repaired in R4-2) |
| E4 | `∀T: v_T = (2Λ(n)/√n)_{n<e^{2T}} ∈ 𝒱_T`, a closed convex set defined by Γ-data alone | P47 `prop:finite`, `prop:uniform` (8b) |
| E5 | `lim_{T→∞} λ^A(T) ≥ 0` | P47 `cor:margin2` (8d) |
| E6 | the Hodge-index inequality on the adelic square | P46 §5 |

**The content that remains** (E4, 8b Prop 1.3): at a fixed window, row D is a finite, decidable condition on finitely
many `Λ(n)` together with the Γ-factor. The entire difficulty is **uniformity in `T`**. By `thm:Z` and P46 W4, that
uniformity is `ψ(x) − x ≪ x^{½+ε}`.

## §2 What is proved at a single window (structure)

* **High frequencies are done** for every window: above `2πe^{A_T}`, `m(τ)` beats the comb (P47 Lemma 4.1, `prop:env`).
  The sign is decided in the band `[2πe^{2T}, 2πe^{A_T}]`, on the alignment arcs of the prime phases (`prop:band`,
  `prop:align`).
* **The archimedean part** (primes removed, P47 §9):
  * `n₋(A_∞|P_T)` is exactly `0 / 1 / 2` below `T*_ev`, on `(T*_ev, T*_odd)`, and on `(T*_odd, 0.90]` (`thm:index`).
  * `T*_∞ ≤ 0.4608 < 0.58 ≤ T*_{∞,P} ≤ 0.60` (`prop:archneg`, `cor:Tarch`).
  * (H1) holds at `log 2` (`cor:H1`).
  * Past `0.60`, the archimedean form is indefinite on `P_T`, so **the primes are necessary**.
* **From the primitive form to the complete form** (156c, `thm:parityschur`, `prop:polarcap`):
  * `In(W_T) = In(A_T|P_T) + In(𝔊_T)`.
  * `λ^W_T > 0 ⟺ λ^A_T > 0 ∧ 𝔊_T ≻ 0`, where `𝔊_T` is the 2×2 polar capacity `S^Sch_T + J`.
  * **The per-window converse `λ^A ≥ 0 ⟹ λ^W ≥ 0` is not structural.** It fails in comb models on `[0.4608, 0.58]` and at
    `½log3` for the weights `θΛ(2)` with `θ ≤ 0.8148` (`cor:convfail`, interval-certified). E1 ⟺ E2 holds only
    globally.
* **Kreĭn** (`thm:KEP3`, corrected chain of R156_004 A12):
  `∃Al_T ⟺ λ^W > 0 ⟺ [λ^A > 0 ∧ 𝔊_T ≻ 0] ⟹ KEP(T) indeterminate ⟹ λ^W ≥ 0`. Indeterminacy is one-directional.

## §3 What is proved for ζ (the sign), by form

| form | windows | source |
|---|---|---|
| primitive `λ^A ≥ 0` | `T ≤ log 2` | Paper 42 (certified) |
| primitive | `T = ½log3`: `λ_min ≥ 8.8577·10⁻⁵` (endpoint of record) | P47 `thm:C` |
| complete `λ^W ≥ 0` | `T ≤ ½log2` | Yoshida 1992, Bombieri 2000 |
| complete (hence primitive) | `(½log2, 0.8]` | Zhu 2026 Thm 1.2 — **cited, not re-verified** |
| either | `T > 0.8` | **nothing** |

Rule of record (R156_004 A14): "`T ≤ log 2`" holds only for the primitive form. Always state which form.

## §4 Why every known route stops (proved obstructions)

1. **The margin decays:** `λ^A(T) ≤ 4·10⁹·T·e^{−15.449T}`, so no `T`-uniform margin exists (`thm:margin`,
   `cor:margin1–2`; crossings at `T = 1.430` and `2.054` after R4-1).
2. **No classical prime-side theorem decides any window** beyond `½log2`: modified combs keep ψ up to a constant, keep
   all the zeros and the pole, and still fail (`thm:finmod`, `cor:void`). The per-window converse requires `Λ(2)`
   itself, not the class it belongs to (`cor:convfail`).
3. **The zeros do not suffice either:**
   * no finite zero set carries a certificate (`thm:finZ`);
   * positivity is never termwise in the zeros (`lem:Rrig`);
   * positivity is never obtained prime by prime or from a sub-comb (`thm:SC`).
4. **No finite truncation decides the even Schur complement** (`thm:arena`). Finite-rank compressions and a monotone
   spectral flow are closed (N5, D.53).
5. **Frame.**
   * The frame-defect theorem (P46 Thm 19.25) now holds on `C_c^∞ ⊕ ℝK` too (Cor 19.25b, R156_002/003).
   * On the bare set `𝒢_min`, the hypothesis of Thm 12.3 is satisfiable ⟺ RH (Rem 19.25c).
   * D-HS is killed (R155_054); no arithmetic-geometry candidate remains.
   * T1, T2, T5 and the polar/entire classification stand (P46 §28.2).
6. **Methods:** duality without attainment (`thm:O`), log exchange (`thm:Vp`), Toeplitz ceilings for lattice classes
   (`thm:N`, `thm:Np`), and no upward induction in `T` (`cor:mono`, `lem:monoT`).

## §5 Open items that remain (none of them is the sign)

| item | nature |
|---|---|
| (H1) at `0.80`, `n_odd(0.80) = 0` | certified computation off-machine (`τ_N ≈ 60`) |
| per window, `RD_T ⟹ λ^P_T ≥ 0`; an effective window shift for ζ | pure math, OPEN |
| the converse for ζ at `T > 0.8` | as hard as the sign there |
| Horn B (R2), the B4 traces at `F_R` | frame residual, OPEN |
| O-150.1 (H-DMV) | **blocked: needs the Diamond–Montgomery–Vorhauer 2006 PDF from the owner** |
| optimised lattice class `Θ(1/M)`; fixed-M lossiness of Thm R | OPEN, optional |
| P46 Lemma 19.20(iv) zero count for `21 ≤ T ≲ 2·10⁴` (E3 of R156_003) | citation gap, flagged |
| P46 Cor 6.2 per field (`ξ_K(½) = 0` case) | repaired in the memo, not integrated |

## §6 Decision for the owner

Row D is reduced to one statement: **uniformity in `T` of a per-window, decidable, finite condition**, and that
statement is RH. Every attempted reduction of it is either an equivalence or has a proved obstruction (§4). Two options:

* **(A) Declare row D closed in the map (final).** The map is complete: address, structure, obstructions, open
  residuals. The remaining work is maintenance of Papers 46–47 (the §5 items).
* **(B) Continue** only with a mechanism that §4 does not exclude. By item 2, it would have to use exact values of
  `Λ(n)`, not only class properties. By items 1 and 4, it would have to be uniform in `T` without a margin and without a
  finite truncation. No such mechanism is on record, and the programme has none to propose today.
