# R155.024 — Round 3B: the first **proved negative class statements at a two-prime window**, and the `λ^P` version of Theorem 3.3

*Orders: `R155_010 §5` (first two items) and `R155_018 §4(iii),(iv)`.
Rules obeyed: pure mathematics; the only computations are scalar quadratures and `M×M` Hermitian
eigenvalues; every run a single process with `OMP_NUM_THREADS=1` and `< 60 s` (runtimes archived in the
JSONs). **FATAL rule in force:** nothing below is a statement about the zeros of `ζ`, and no sign is
claimed for any `T > log 2`. Paper 47, `scripts/r3a` and all earlier phase files are untouched; the new
code is `scripts/r3b/`.*

---

## §0. Verdict

1. **Both enclosures close, and they close with room.** `Ceil(24, 0.68) ≤ −7.4931·10⁻⁶ < 0` and
 `Ceil(24, \log2) ≤ −6.5843·10⁻⁷ < 0`, **uniformly in `β`**, by interval arithmetic
 (`scripts/r3b/r3b_enclosure_{0.68,log2}_M24.json`). These are the programme's **first proved negative
 class statements at a two-prime window**; they upgrade the two entries that `R155_010 §1` carried as
 `DIAGNOSTIC, sign robust, digits spurious`.
2. **The statement is not confined to `M = 24`: it covers every `M ≤ 24`.** Thirty-two enclosures were
 run, one process each, and **all thirty-two close**. Sixteen values of `M` are certified directly at
 each window (`M = 6,7,9,11,13,…,24`) and the remaining `M ∈ {1,2,3,4,5,8,10,12}` follow by sublattice
 inclusion (`M | 24`, `M | 20`, `M | 16`). `M = 9` needed a second attempt — at the argmin period
 placement the minimax has **two active `τ₀`**, so no single test kernel can carry the `β`-uniform
 bound there; scanning the twelve best placements fixes it (§2.5), at the cost of recovering only
 `6–7 %` of the double-precision ceiling and of two runs at `95 s` and `75 s`, the only two in the
 round above the `60 s` guideline. **[amended per R155_027]** `M = 6` also used the same placement-scan remedy (`ncand = 8`), recovering `90 %` and `74 %` of the double-precision ceiling at the two windows; see §2.2/§2.5.
3. **The `β`-box is no longer a load-bearing constant.** `R155_007 R-2` asked for a tolerance rather than
 the sharp `V⋆/r₀`. At these windows the recomputed Theorem-B constants are
 `B(0.68) = 1.89052·10⁴` and `B(\log2) = 1.70313·10⁴` (`r₀ = 2.4309·10⁻⁴, 2.6720·10⁻⁴`;
 `V⋆ = 4.595697, 4.550671`), the enclosure uses `B = 1.90·10⁴` and `1.71·10⁴`, and the certified bound
 stays negative **for every `B ≤ 1.0·10¹¹`** at `M = 24, T = 0.68`, and for every `B ≤ 4.7·10⁹` in
 the worst of the 32 rows — a tolerance of five to seven orders of
 magnitude, because the optimised test kernel drives `|b₀|+|b₁|` to `≈ 10⁻¹⁶`. R-2 is thereby not
 merely disclosed but rendered irrelevant.
4. **The `λ^P` version of Theorem 3.3 is proved, with an explicit `R(ε,T)` that is optimal in form.**
 `R155_001 §2–3` gave a bounded-set reduction for `λ^A` through the minimiser `μ⋆`; (P) has no
 minimiser (Theorem O), so the `λ^P` statement has to be uniform over *near-optimal feasible* `μ`.
 Theorem 3.3ᴾ (§3) does this: with `B := A_T − C₀ = 7.62100976` and `G(ε) := λ^P + ε + B`,
 ```
 R(ε,η;T) = 2π\exp\big(1 + C₀ + G(ε)/η\big)
 ```
 makes `μ(|τ| ≥ R) ≤ η` for **every** (P)-feasible `μ` of value `≤ λ^P + ε`, and Paper 47
 Theorem V′(iii) says the shape `e^{B/η}` cannot be improved. `PROVED`.
5. **A by-product worth recording: the quadrature had to change, and the change is reusable.** The
 composite-Simpson enclosure of `R155_004 §2.3` would need `~10⁵` interval nodes here. Composite
 Gauss–Legendre with the classical panel remainder and the same Bernstein/Leibniz derivative bounds
 does it in `≈ 3300` nodes (§2.3). The first version of the Gauss–Legendre nodes was **wrong**
 (`Σ w_i = 2.189`) and produced an interval that did **not** contain the true value; the `Σ w_i = 2`
 check now guards every run and is archived (`gl_residual < 10⁻⁶⁰`). Recorded because it is exactly the
 kind of silent failure that an interval computation is supposed to prevent and did not.

---

## §1. Corpus check (greps run over `03-research`, `04-papers`, `05-meta-and-planning`)

| idea used below | grep hits (file:line) | pre-existing? | status here |
|---|---|---|---|
| Theorem TK at a single `(τ₀,φ)`; `c ≤ a + b·β` | `R155_001 §4.3`; `04-papers/47-row-d-dual-certificates/main.tex:1237` (`prop:TK`); `R155_004 §2.2` | yes | reused verbatim; only the window `T` and the contact set change |
| interval enclosure of a `β`-uniform ceiling | `R155_004 §2` (`Ceil(8,½log3) ≤ −5.6974·10⁻³`), `scripts/r2_a_enclosure.py` | yes, at **one** window and one `M` | §2 is the same argument at `T = 0.68, log2` and 23 values of `M`; the quadrature is new (§2.3) |
| Lemma 2.2 (convex midpoint bracket of the `ψ`-tail), `C₀` Gauss digamma, `∫φ = P‖q‖²`, Bernstein bounds | `R155_004 §2.3`, audited `R155_007 §1.2` | yes | reused verbatim, extended from order `4` to order `2p` |
| Gauss–Legendre panels in this programme | `R153_007:137`, `R153_019:99`, `R155_002:7` (the audit's independent check), `phase-113/113_09:286` | the *rule* yes, never inside an **interval** enclosure | the rigorous panel remainder `H^{2p+1}(p!)⁴/((2p+1)((2p)!)³)\sup|f^{(2p)}|` with the corpus's own derivative bounds is new here |
| `Ceil(24,0.68) < 0`, `Ceil(24,\log2) < 0` | `R155_004 §3` Run 2 (`DIAGNOSTIC`), `R155_007 R-3` (refined `−7.512·10⁻⁶`), `R155_010 §1` (label) | yes, **as `DIAGNOSTIC`** | §2 makes them `PROVED (machine-verified)`; the refined double value `−7.512289·10⁻⁶` is reproduced to 7 figures and the certified bound is `−7.4931·10⁻⁶`, i.e. `99.7 %` of it |
| Theorem B (`‖β‖₂ ≤ (V⋆−c)/r₀`) and its constants | `R155_004 §4`, `scripts/r2_c_beta_bound.py`; `main.tex:873` (`lem:W`) | yes, at `½log3` and `0.58` | constants recomputed at `0.68` and `log2` (`scripts/r3b/betabox.py`); no new mathematics |
| `R-2` (the box constants are not interval-enclosed) | `R155_007 R-2`, `R155_010 §1` | yes, an open disclosure | §2.4 answers it with a **tolerance of six orders**, not with a sharper constant |
| bounded-set reduction for `λ^A` (Theorem 3.3, Lemmas 3.1–3.2, Prop. L1.1, Cor. L1.2) | `R155_001 §3` (amended), `R155_002 §0` item 8 (`CONFIRMED`) | yes, **for `λ^A` only** | §3 is the `λ^P` statement that `R155_003` repair (1) and `R155_010 §5` record as still owed; grep `"λ^P version of Theorem 3.3"` returns only those two orders and no statement |
| Theorem V′ (mass–value exchange is `Θ(\log R)`; no rate uniform over the feasible set) | `main.tex:930–1000` (`thm:Vp`), Remark after it | yes | §3.2 uses (i) as the tail bound and (iii) as the **optimality** of `R(ε,η)`; this is the first place the corpus uses V′ as a *positive* statement |
| Lemma 4.1 / `lem:mbounds` (`m` increasing; `\log(τ/2π) − 1/τ − 1/2τ²` lower bound) | `main.tex:624` | yes | used to make `R(ε,η)` explicit |
| Theorem R (`Ceil(M,T;β) ≤ ∫σ_Tdμ + Δ·μ(|τ|>P/2)`), `Δ(M,β)` | `R155_004 §6.2` | yes | §3.4 combines it with §3.1's *uniform* tail bound to give the first explicit `M`-rate; unconditionally `O(1)`, and `O((\log M)^{−δ})` on the sub-family of §3.3 |
| envelope threshold `2πe^{A_T+‖ν‖_TV}` | `main.tex:937` (`prop:env`) | yes | §3.5 compares `R(ε,η)` against it (`59.5` multiplier-free; `~10⁴⁰` for the §5 certificate) |
| "start above the TK ceiling" rule | `R155_010 §2` item 3 | yes | §2.6 gives the rule its two-prime numbers |

**Nothing below duplicates a corpus statement.** Theorem N′ (§2), Theorem 3.3ᴾ with its `R(ε,η;T)` and
Corollaries Aᴾ–Cᴾ (§3), and the Gauss–Legendre interval scheme (§2.3) are new; everything else is cited.

---

## §2. Theorem N′ — the certified negative class statements at `T = 0.68` and `T = log 2`

### 2.1 Statement

> **Theorem N′ (class impossibility at the two-prime windows). `PROVED (machine-verified)`.**
> Let `T ∈ {0.68, \log2}`, `C₀ = ψ(¼) − \logπ`, `N_T = {2,3}`, `v_2 = 2\log2/\sqrt2`,
> `v_3 = 2\log3/\sqrt3`, `σ_T(τ) = m(τ) − v_2\cos(τ\log2) − v_3\cos(τ\log3)`. Let `M ∈ {1,…,24}`,
> `d = 2T/M`, let `ν` be **any** finite even signed measure supported on the lattice `{±jd : j ≥ M}`
> (any range, any number of atoms, any signs) and `β ∈ ℝ²` **arbitrary**. Then
> ```
> inf_{τ∈ℝ} [ σ_T(τ) + ν̂(τ) + β₀ĝ₀(τ) + β₁ĝ₁(τ) ] < 0.
> ```
> Consequently **no dual certificate of Paper 47 Def. 3.1 supported on a lattice of step `2T/M` with
> `M ≤ 24` has non-negative value**, and none proves `λ^P(0.68) > 0` or `λ^P(\log2) > 0` — for any `β`,
> any range, any atom count, and any tail lemma (`lem:F1`, `lem:T`, `lem:hybrid`), since all of those
> only *verify* the pointwise inequality that Theorem N′ refutes.

These are the programme's **first proved negative class statements at a two-prime window**. At
`½\log3` (Theorem N, `R155_004 §2`) the window has a single contact and the barrier was at `M ≤ 8`;
here the barrier reaches `M ≤ 24`, i.e. the resolution at which the archived positive certificate at
`½\log3` lives (`main.tex` Thm C, `M = 24`, 437 atoms, `c = 8.8577·10⁻⁵`). **The `M = 24` class that
carries the endpoint of record at `½\log3` is provably empty at `0.68` and at `\log2`.**

### 2.2 The proof, and the data

Suppose `f := σ_T + ν̂ + β·ĝ ≥ c` on `ℝ` with `c ≥ 0`.

**Step 1 (`β` is bounded).** Theorem B (`R155_004 §4`) with the constants recomputed at these two
windows (`scripts/r3b/betabox.py`, archived `r3b_beta_box.json`):

| `T` | `A_T` | `r₀` | `V⋆` | `0` interior | `B = V⋆/r₀` for `c ≥ 0` | used in the enclosure |
|---|---:|---:|---:|:--:|---:|---:|
| `0.68` | `2.24882634` | `2.430921·10⁻⁴` | `4.595697` | yes | `18905.2` | `B = 1.90·10⁴` |
| `\log2` | `2.24882634` | `2.671951·10⁻⁴` | `4.550671` | yes | `17031.3` | `B = 1.71·10⁴` |

(`A_T` is the same at both windows: the contact set `{n : \log n < 2T}` is `{2,3}` throughout
`(½\log3, ½\log5)`.)

**Step 2 (one test kernel).** Fix the archived pair `(τ₀, q)` for this `(T,M)` (Table 2.2). Put
`φ(τ) = |Σ_{k<M} q_k e^{ikdτ}|² ≥ 0`, `W = [τ₀, τ₀+P]`, `P = 2π/d = πM/T`.
**[amended per R155_027]** Non-negativity of `φ` is structural, not a certified positivity
property of the specific `q`: the code evaluates `φ = re² + im²` (`r3b_enclosure.py:181`), so `φ ≥ 0`
for **any** complex `q` and any rounding of it, with degree `≤ M−1` by construction; no eigenvector
property of `q` is used or needed. Since `ν̂` is `P`-periodic
with Fourier modes in `{|j| ≥ M}` and `φ` has modes in `{|j| ≤ M−1}`, `∫_W ν̂φ = 0` (Lemma 4.1 of
`R155_001`). Integrating `f ≥ c` against `φ ≥ 0` over `W` and dividing by `∫_Wφ = P‖q‖²` (exact) gives
`c ≤ a + b₀β₀ + b₁β₁` with `a = (P‖q‖²)^{-1}∫_Wσ_Tφ` and `b_j = (P‖q‖²)^{-1}∫_W ĝ_jφ`.

**Step 3 (enclosure).** With Step 1, `c ≤ a + (|b₀|+|b₁|)·B`. The three scalar integrals are enclosed
in `mpmath` interval arithmetic (§2.3). Every row below is `< 0`, contradicting `c ≥ 0`. ∎

**Table 2.2 — the 32 enclosures.** `Ceil` (double) is the double-precision `β`-uniform ceiling on the
121-point `τ₀` grid and is `DIAGNOSTIC`; it is printed only because it is the provenance of the test
pair and shows how much of it the single-kernel bound recovers. `a` is the **upper endpoint** of the
enclosure, which is what the proof uses; `B·|b|₁` is the whole `β`-allowance; "`B` tolerance" is the
largest `B` for which the row still closes (`|a|/|b|₁`). Runtimes are wall-clock, single process,
`OMP_NUM_THREADS=1`.

| `T` | `M` | `tau0` | `Ceil` (double, DIAGNOSTIC) | `a` (upper end) | `\|b\|₁` | `B·\|b\|₁` | quad. err on `a` | **bound** | err/`\|a\|` | `B` tolerance | s |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.68 | 6 | -8.870 | -1.1164e-01 | -1.006152e-01 | 8.8e-17 | 1.7e-12 | 1.4e-09 | **-1.006152e-01** | 0.0% | 1.1e+15 | 56 |
| 0.68 | 7 | -19.404 | -6.5250e-02 | -6.524982e-02 | 6.3e-16 | 1.2e-11 | 1.7e-09 | **-6.524982e-02** | 0.0% | 1.0e+14 | 15 |
| 0.68 | 9 | -29.106 | -8.6497e-02 | -6.393168e-03 | 5.0e-17 | 9.4e-13 | 3.7e-09 | **-6.393168e-03** | 0.0% | 1.3e+14 | 95 |
| 0.68 | 11 | -30.492 | -1.5569e-02 | -1.556921e-02 | 2.3e-16 | 4.5e-12 | 4.7e-09 | **-1.556921e-02** | 0.0% | 6.6e+13 | 20 |
| 0.68 | 13 | -40.841 | -3.6644e-03 | -3.664365e-03 | 1.5e-16 | 2.9e-12 | 6.1e-09 | **-3.664365e-03** | 0.0% | 2.4e+13 | 22 |
| 0.68 | 14 | -46.569 | -7.4992e-02 | -7.499134e-02 | 2.3e-16 | 4.3e-12 | 8.7e-09 | **-7.499134e-02** | 0.0% | 3.3e+14 | 24 |
| 0.68 | 15 | -22.176 | -3.4028e-03 | -3.402724e-03 | 4.9e-17 | 9.3e-13 | 8.6e-09 | **-3.402724e-03** | 0.0% | 7.0e+13 | 55 |
| 0.68 | 16 | -36.960 | -1.3231e-03 | -1.323029e-03 | 9.8e-17 | 1.9e-12 | 1.0e-08 | **-1.323029e-03** | 0.0% | 1.4e+13 | 45 |
| 0.68 | 17 | -40.841 | -9.4012e-04 | -9.394105e-04 | 3.6e-17 | 6.9e-13 | 1.1e-08 | **-9.394105e-04** | 0.0% | 2.6e+13 | 40 |
| 0.68 | 18 | -19.958 | -1.4968e-03 | -1.496756e-03 | 8.5e-17 | 1.6e-12 | 1.3e-08 | **-1.496756e-03** | 0.0% | 1.8e+13 | 29 |
| 0.68 | 19 | -40.379 | -2.0453e-04 | -2.044912e-04 | 7.2e-17 | 1.4e-12 | 1.4e-08 | **-2.044912e-04** | 0.0% | 2.9e+12 | 21 |
| 0.68 | 20 | -46.200 | -2.1073e-06 | -2.091693e-06 | 1.1e-16 | 2.1e-12 | 1.5e-08 | **-2.091691e-06** | 0.7% | 1.9e+10 | 31 |
| 0.68 | 21 | -48.510 | -6.6510e-07 | -6.473676e-07 | 6.9e-17 | 1.3e-12 | 1.6e-08 | **-6.473663e-07** | 2.5% | 9.4e+09 | 25 |
| 0.68 | 22 | -46.754 | -4.1659e-07 | -3.988523e-07 | 8.5e-17 | 1.6e-12 | 1.8e-08 | **-3.988506e-07** | 4.5% | 4.7e+09 | 26 |
| 0.68 | 23 | -59.505 | -3.0461e-07 | -2.823566e-07 | 1.1e-17 | 2.1e-13 | 1.9e-08 | **-2.823564e-07** | 6.7% | 2.6e+10 | 25 |
| 0.68 | 24 | -19.958 | -7.5123e-06 | -7.493131e-06 | 7.5e-17 | 1.4e-12 | 2.4e-08 | **-7.493129e-06** | 0.3% | 1.0e+11 | 51 |
| log2 | 6 | -8.158 | -1.3833e-01 | -1.019969e-01 | 2.9e-16 | 5.0e-12 | 1.7e-09 | **-1.019969e-01** | 0.0% | 3.5e+14 | 61 |
| log2 | 7 | -19.036 | -1.6685e-01 | -1.668520e-01 | 7.7e-16 | 1.3e-11 | 2.3e-09 | **-1.668520e-01** | 0.0% | 2.2e+14 | 15 |
| log2 | 9 | -28.554 | -1.1671e-01 | -7.469885e-03 | 5.0e-17 | 8.6e-13 | 3.7e-09 | **-7.469885e-03** | 0.0% | 1.5e+14 | 75 |
| log2 | 11 | -29.914 | -3.5666e-02 | -3.566574e-02 | 8.6e-17 | 1.5e-12 | 5.1e-09 | **-3.566574e-02** | 0.0% | 4.1e+14 | 17 |
| log2 | 13 | -18.855 | -1.4559e-02 | -1.455855e-02 | 8.9e-17 | 1.5e-12 | 7.1e-09 | **-1.455855e-02** | 0.0% | 1.6e+14 | 19 |
| log2 | 14 | -34.265 | -4.6687e-04 | -4.668105e-04 | 2.7e-16 | 4.7e-12 | 7.7e-09 | **-4.668105e-04** | 0.0% | 1.7e+12 | 24 |
| log2 | 15 | -20.396 | -2.1135e-03 | -2.113431e-03 | 7.5e-17 | 1.3e-12 | 8.8e-09 | **-2.113431e-03** | 0.0% | 2.8e+13 | 28 |
| log2 | 16 | -63.816 | -6.0686e-05 | -5.423434e-06 | 1.9e-16 | 3.3e-12 | 1.1e-08 | **-5.423431e-06** | 0.2% | 2.8e+10 | 28 |
| log2 | 17 | -20.033 | -1.4109e-05 | -1.408584e-05 | 1.2e-17 | 2.0e-13 | 1.2e-08 | **-1.408584e-05** | 0.1% | 1.2e+12 | 24 |
| log2 | 18 | -17.948 | -1.3421e-04 | -1.341447e-04 | 1.7e-16 | 3.0e-12 | 1.5e-08 | **-1.341447e-04** | 0.0% | 7.8e+11 | 23 |
| log2 | 19 | -63.725 | -3.7360e-04 | -3.735565e-04 | 1.4e-16 | 2.4e-12 | 1.6e-08 | **-3.735565e-04** | 0.0% | 2.6e+12 | 27 |
| log2 | 20 | -48.949 | -2.3443e-06 | -2.319961e-06 | 5.6e-17 | 9.5e-13 | 1.5e-08 | **-2.319960e-06** | 0.6% | 4.2e+10 | 28 |
| log2 | 21 | -13.325 | -4.5666e-06 | -4.547749e-06 | 9.8e-17 | 1.7e-12 | 1.7e-08 | **-4.547747e-06** | 0.4% | 4.6e+10 | 32 |
| log2 | 22 | -47.862 | -1.6339e-06 | -1.601960e-06 | 6.8e-18 | 1.2e-13 | 1.8e-08 | **-1.601960e-06** | 1.1% | 2.4e+11 | 33 |
| log2 | 23 | -12.509 | -4.3798e-04 | -3.884289e-04 | 8.6e-18 | 1.5e-13 | 2.0e-08 | **-3.884289e-04** | 0.0% | 4.5e+13 | 34 |
| log2 | 24 | -54.388 | -6.8361e-07 | -6.584333e-07 | 5.1e-17 | 8.7e-13 | 2.2e-08 | **-6.584324e-07** | 3.3% | 1.3e+10 | 29 |

**How to read the margins honestly.**

* The `β`-allowance is **not** the binding term anywhere: `B·|b|₁ ≤ 1.3·10⁻¹¹` in every row, i.e. at
 least four orders of magnitude below the smallest `|a|` in the table (`2.82·10⁻⁷`). The optimisation
 of §2.3(v) drives `|b|₁` to the `10⁻¹⁶`–`10⁻¹⁸` level.
* The binding term is the **quadrature error on `a`**, and it is between `0.0 %` and `6.7 %` of `|a|`.
 The four tightest rows are `T = 0.68, M = 23` (`6.7 %`), `M = 22` (`4.5 %`), `T = \log2, M = 24`
 (`3.3 %`), `T = 0.68, M = 21` (`2.5 %`). All close, but a further decade of margin there costs only a
 smaller panel width `H` (the error scales as `H^{12}`).
* The headline rows: `Ceil(24, 0.68) ≤ −7.493129·10⁻⁶` against the refined double value
 `−7.512289·10⁻⁶` (the enclosure recovers `99.7 %` of it), and `Ceil(24, \log2) ≤ −6.584324·10⁻⁷`
 against `−6.836140·10⁻⁷` (`96.3 %`).
* **[amended per R155_027]** `M = 6` at both windows also required the placement-scan remedy of §2.5 (`ncand = 8`, not a single argmin placement), recovering `90 %` (`T = 0.68`) and `74 %` (`T = \log2`) of the double-precision ceiling. This was previously disclosed only for `M = 9`; it is disclosed here for completeness.
* `R155_007 R-3` is answered: the refined double value `−7.512·10⁻⁶` at `(0.68, 24)` is reproduced to
 seven figures with a 121-point grid, confirming the audit's refinement and not the archived
 `−2.279·10⁻⁷`. **Nothing in the proof depends on either number.**

### 2.3 The enclosure, in full

Everything is in `mpmath`'s interval context at `iv.dps = 30`; the only non-interval inputs are the
rational `τ₀` and the decimal `q`, which are *data of the certificate*, not approximations: **any**
`(τ₀,q)` gives a valid upper bound, so their provenance (a double-precision eigenvector) is irrelevant
to the proof.

**(i) Unchanged from `R155_004 §2.3`.** `C₀ = −γ − π/2 − 3\log2 − \logπ` from `iv.euler, iv.pi, iv.log`;
`m(τ) = C₀ + Σ_{k<K}t_k(τ) + R`, `t_k = τ²/(a_k(τ²+4a_k²))`, `a_k = k+¼`, `K = 100`, with the tail `R`
bracketed by Lemma 2.2 (the convex midpoint bracket, `R ∈ [Λ−E, Λ]`); `ĝ₀, ĝ₁` as closed-form interval
expressions; `∫_Wφ = P‖q‖²` exactly, so no quadrature error enters the denominator. The only change to
`σ_T` is the **second contact**: `σ_T = m − v_2\cos(τ\log2) − v_3\cos(τ\log3)`.

**(ii) The quadrature is new.** Composite Simpson with the fourth-derivative bound of `R155_004` would
need `~10⁵` interval nodes here (`P = πM/T ≈ 111` instead of `45.75`, and `|a| ~ 10⁻⁶` instead of
`6·10⁻³`, so the required absolute accuracy rises by `10³`). We use **composite Gauss–Legendre** of
order `p` on `N = ⌈P/H⌉` panels of width `H`, with the classical remainder per panel
```
 |E_panel| ≤ H^{2p+1}\frac{(p!)^4}{(2p+1)((2p)!)^3}\,\sup|f^{(2p)}|,
```
and `\sup|f^{(2p)}|` from the same Leibniz/Bernstein bounds as `R155_004 §2.3(iii)`, extended from
order `4` to order `2p`:
```
 |m^{(j)}| ≤ 2^{-j}j!\,ζ(j+1,¼) ≤ 2^{-j}j!(4^{j+1}+ζ(j+1)) (j ≥ 1)
 |m| ≤ max(|C₀|, m(τ_max)) (j = 0; m even, increasing in |τ|)
 |(v_n\cos(τ\log n))^{(j)}| ≤ v_n(\log n)^j (n = 2, 3)
 |ĝ₀^{(j)}| ≤ 2\cosh T(2T)^{j+1}/(j+1), |ĝ₁^{(j)}| ≤ 2\sinh T(2T)^{j+2}/(j+2)
 |φ^{(j)}| ≤ (d(M−1))^j Σ_l|γ_l| ≤ (d(M−1))^j(Σ_k|q_k|)²
 |f^{(2p)}| ≤ Σ_{j≤2p}\binom{2p}{j}\sup|X^{(2p−j)}|\sup|φ^{(j)}|, X ∈ {σ_T, ĝ₀, ĝ₁}.
```
The `j = 0` entry matters: the crude `|m| ≤ |C₀| + \log(τ_{max}/2π) + 1` of `R155_004` is replaced by
`max(|C₀|, m(τ_{max}))` with `m(τ_{max})` itself interval-enclosed, which is both sharper and shorter
to justify (`m` is even and increasing on `[0,∞)`, `lem:mbounds`(i)).

At `T = 0.68, M = 24`, `p = 6`, `H = 0.19978` (`N = 555` panels, `3330` nodes): the Gauss–Legendre
constant is `1.8809·10⁻¹⁶`, `\sup|(σ_Tφ)^{(12)}| ≤ 2.879·10¹⁴`, `\sup|(ĝ₀φ)^{(12)}| ≤ 1.238·10⁶`,
giving remainders `2.428·10⁻⁸`, `1.044·10⁻¹⁶`, `7.221·10⁻¹⁷` on the three integrals. The `10⁸`-fold
asymmetry between the `σ`-error and the `ĝ`-errors is exactly what the problem needs: `a` may be known
to `10⁻⁸`, but `b` is multiplied by `B ≈ 1.9·10⁴`. Runtime: `24.6 s` of interval quadrature.

**(iii) Nodes and weights.** Legendre roots are Newton-refined at `mp.dps = 60` from the
double-precision `numpy.polynomial.legendre.leggauss` seeds, `w_i = 2/((1−x_i²)P_p'(x_i)²)`, and both
are widened by `10⁻⁴⁵` before entering interval arithmetic — so the interval sum encloses the **exact**
Gauss–Legendre sum, to which the classical remainder applies. Each JSON carries
`gl_residual = max(\max_i|P_p(x_i)|, |Σ_i w_i − 2|)`; it is `3.1·10⁻⁶¹` in every run.
**[amended per R155_027, rigour note N-3]** The `10⁻⁴⁵` widening plus the archived residual
is *not* itself a certified node-error bound: turning `|P_p(x_i)|` into a bound on `|x_i − x_i^{true}|`
needs a lower bound on `|P_p'|` near the node and a separation argument, which is not carried out here.
With `res ≈ 3·10⁻⁶¹` and `|P_6'|` of order `1` this is a formality, covered by the same margin as the
rest of the enclosure — the same species of gap as `R155_007` R-2, closed by margin rather than by a
certificate.

**(iv) A failure worth recording.** The first version computed the nodes with `mpmath.findroot` from
Chebyshev seeds `\cos(π(i−¼)/(p+½))`. Two seeds converged to the **same** root; `Σ_i w_i = 2.1894`
instead of `2`; the rule was wrong by `≈ 6·10⁻⁶` in the integral, and the resulting "enclosure" of `a`
at `(0.68, 24)` was `[−7.5816, −7.5604]·10⁻⁶`, which **does not contain** the true value
`−7.5123·10⁻⁶`. It was caught only because `b₀, b₁` came out at `6·10⁻⁸` where an independent
`2²²`-node `numpy` Simpson gave `4·10⁻¹⁷` (`scripts/r3b/dbg.py`). The `Σ w_i = 2` check is now computed
and archived in every run. *An interval computation is only as rigorous as its least-checked input;
this one had a silent one.*

**(v) The choice of `q` — the one place where the old script had to change substantively.**
`r2_a_enclosure.py` used the bottom eigenvector of `C_M(τ₀,β⋆)`, which makes `a` as negative as
possible and lets `b` fall where it may (at `½\log3, M = 8` it fell at `3·10⁻⁹`, which sufficed
because `|a| = 6·10⁻³`). Here `|a|` is `10²`–`10⁴` times smaller while `B` is of the same size, so `b`
must be *designed*. We minimise `a + B(|b₀|+|b₁|)` over the span of the `r = 3` (or `4`) lowest
eigenvectors of `C_M(τ₀,β⋆)`, by Nelder–Mead from ten starts. When the minimax has a single active
period placement, strong duality guarantees a rank-one optimum with `b = 0` exactly, and the optimiser
reaches `|b|₁ ≈ 10⁻¹⁶`–`10⁻¹⁸` while `a` stays within a fraction of a percent of the ceiling (Table
2.2, column `Ceil` versus column `a`). The three Toeplitz families are recomputed at the selected `τ₀`
with `n = 2²⁰` Simpson nodes first: `tk_common.coeff_families` at the default `n = 2¹⁶` carries `~10⁻⁸`
error in the `ĝ` families, which is `10⁸` times the `|b|` being aimed at, and the optimiser would
otherwise be nulling the error rather than the coefficient. **This is what the `B`-tolerance column of
Table 2.2 buys, and it is why `R155_007 R-2` stops being a live issue (§2.4).**


### 2.4 The tolerance on `B` — answering `R155_007 R-2`

R-2 objected that Theorem N is `PROVED (machine-verified)` while resting on `r₀, V⋆` that are 30-digit
floating point with a double-precision `ConvexHull` inradius. The right answer is a tolerance, and here
it is enormous: the last column of Table 2.2 gives, row by row, the largest `B` for which the bound
still closes. It is `10¹¹`–`10¹⁵` in most rows, and its **minimum over the whole
table is `4.7·10⁹`** (`T = 0.68, M = 22`), against the Theorem-B constants `1.89·10⁴` and
`1.70·10⁴`. So Theorem N′ survives any error in `V⋆/r₀` up to a factor of **`2.5·10⁵`**, and the
qualitative content of Theorem B — that *some* finite a priori box exists — is all that is used.
The same reading applies retrospectively to Theorem N at `½\log3`, whose tolerance `R155_007` computed
as `9.7·10⁵` (a factor `21`); the present rows are four to nine orders better because of §2.3(v) — the
optimisation of `q` against the box, which `r2_a_enclosure.py` did not do.

### 2.5 Why `M = 9` (and `M = 6`) needed a second attempt, and what that says [amended per R155_027]

At `M = 9` (both windows) the bottom eigenvector at the argmin period placement gives `|b|₁ ≈ 10⁻⁴`,
not `10⁻¹⁶`, and the enclosure is **positive**. The reason is structural: `Ceil(M,T) = \sup_β
\inf_{τ₀}λ_{\min}(C_M(τ₀,β))` is a minimax, and when **two** period placements are active at the
optimal `β`, strong duality attains `b = 0` only for a *mixture* of two test kernels living on two
different windows — no single `(τ₀,q)` can do it. Two remedies exist, and the cheap one suffices:
scanning the `12` best `τ₀` of the grid and keeping the placement whose optimised
`a + B(|b₀|+|b₁|)` is smallest finds, at `τ₀ = −29.106` (`T = 0.68`) and `τ₀ = −28.554` (`T = \log2`),
kernels with `|b|₁ ≈ 5·10⁻¹⁷` and bounds `−6.393168·10⁻³`, `−7.469885·10⁻³`. The price is that the
single-kernel bound recovers only `7 %` and `6 %` of the double-precision ceiling there — an honest loss,
and irrelevant to the sign. *(The principled remedy, for the record: `c ≤ Σ_iλ_i Q(τ₀_i,φ_i,β)` for any
convex weights `λ`, since Theorem TK holds at each placement separately; minimising over `λ` is a
two-variable LP. Not needed here.)* These two runs took `95 s` and `75 s` and are the **only** two in the
round that exceed the `60 s` single-process guideline; they are declared as such, and re-running either
alone is one command. **[amended per R155_027]** The same mechanism affects `M = 6` at both windows: the argmin placement's minimax has two active `τ₀`, and the `ncand = 8` placement scan is used there too, recovering `90 %` (`T = 0.68`) and `74 %` (`T = \log2`) of the double-precision ceiling. §0.2 and §2.2 now state this explicitly.

### 2.6 Scope, stated as a limit

* **Steps `d` with `2T/d ∉ ℕ` are not covered.** As in `R155_004 §2.4`: for such `d` the mode gap is
 `M' = ⌈2T/d⌉` and the matrix is built on the period `2π/d`; each such `d` needs its own enclosure (one
 run of the same script), no new mathematics. Recorded as a scope limit, not claimed.
* **Theorem N′ says nothing about `λ^P(0.68)` or `λ^P(\log2)`.** It is an upper bound on what a *class*
 can certify. Whether those two numbers are positive is exactly what the programme does not know, and
 the Galerkin upper bounds `λ^A(0.68) ≤ 3.24·10⁻⁷`, `λ^A(\log2) ≤ 1.09·10⁻⁷` are the only thing on
 file.
* **It is consistent with, and sharper than, the recorded LP data.** The off-machine sweep E1 at
 `T = 0.58` is untouched (different window); at `0.68` and `\log2` the rule of `R155_010 §2` item 3 —
 *"start above the TK ceiling"* — now has its numbers: **any search over lattice certificates of order
 `M ≤ 24` at these two windows is provably searching an empty set.**

---

## §3. The `λ^P` version of Theorem 3.3

### 3.0 What was owed, and why it is not a restatement

`R155_001 §2–3` proves the bounded-set reduction through the **minimiser `F⋆` of `𝔞_T` on `P_T`**, i.e.
through the single measure `μ⋆ = |\hat F⋆|²dτ/2π`, and the amendment of `R155_001 §2` states in terms
that "every occurrence of `λ` and of `λ^{prim}` in §2–§3 means `λ^A`". Problem A, however, is about
`λ^P`, the value of the programme (P) of Paper 47 Def. 3.1 — and (P) has **no minimiser**: Theorem O
forbids attainment, and `main.tex:562` says so explicitly. So the `λ^A` proof does not transpose by
renaming: there is no `μ⋆` to integrate against. The statement has to be made **uniform over the
near-optimal feasible set**, and that is what changes the character of the result — the radius `R`
becomes a function of `ε` and `T` alone, not of an unknown extremal.

Throughout: `T > 0` fixed, `C₀ = ψ(¼) − \logπ = −5.3721834192256654…`, `A_T = Σ_{n∈N_T}v_n`,
`B := A_T − C₀ > 0`, `σ_T = m − Σ_n v_n\cos(τ\log n)`, `λ^P` the value of (P), and
`\mathcal F_ε := {μ` feasible for (P) with `∫σ_T dμ ≤ λ^P + ε}`, non-empty for every `ε > 0` by
definition of the infimum. At the two-prime windows `A_T = 2.248826344663675` and `B = 7.62100976388934`
(Paper 47's `7.621`).

### 3.1 The uniform tail bound

> **Proposition P1 (`PROVED`).** For every `ε > 0`, every `μ ∈ \mathcal F_ε` and every `R > 0`,
> ```
> ∫(m − C₀)\,dμ ≤ G(ε) := λ^P + ε + B, μ(\{|τ| ≥ R\}) ≤ \frac{G(ε)}{m(R) − C₀}.
> ```

*Proof.* `m − C₀ ≥ 0` (`m` even, increasing on `[0,∞)`, `m(0) = C₀`: Paper 47 Lemma `lem:mbounds`(i)),
and `∫σ_T dμ = ∫m\,dμ − ∫Σv_n\cos(τ\log n)dμ ≥ ∫m\,dμ − A_T` by `lem:mbounds`(iii). Hence
`∫(m−C₀)dμ ≤ ∫σ_Tdμ + A_T − C₀ ≤ λ^P + ε + B`. Chebyshev on `{|τ| ≥ R}`, where `m − C₀ ≥ m(R) − C₀`. ∎

This is Paper 47 Theorem V′(i) read as a tail bound; the point is that the right-hand side involves **no
datum of `μ`**, so it is uniform on `\mathcal F_ε`.

> **Corollary P2 (the explicit radius; `PROVED`).** For `ε > 0` and `η ∈ (0,1)` put
> ```
> R(ε,η;T) := 2π\exp\Big(1 + C₀ + \frac{G(ε)}{η}\Big), G(ε) = λ^P + ε + B.
> ```
> Then `μ(\{|τ| ≥ R\}) ≤ η` for every `μ ∈ \mathcal F_ε` and every `R ≥ \max\{R(ε,η;T), 2\}`.

*Proof.* By `lem:mbounds`(ii), `m(R) ≥ \log(R/2π) − 1/R − 1/(2R²) ≥ \log(R/2π) − 1` for `R ≥ 2`. So
`m(R) − C₀ ≥ G/η` as soon as `\log(R/2π) ≥ 1 + C₀ + G/η`. Apply P1. ∎

Since `λ^P ≤ λ^A` and the Galerkin upper bounds of `main.tex:960–975` give
`λ^A(0.68) ≤ 3.24·10⁻⁷`, `λ^A(\log2) ≤ 1.09·10⁻⁷`, the radius is numerically the same at both windows to
six figures:

| `ε` | `η` | `G(ε)` | `R(ε,η;T)`, `T ∈ \{0.68, \log2\}` |
|---:|---:|---:|---:|
| `1` | `0.5` | `8.621010` | `2.441·10⁶` |
| `0.5` | `0.5` | `8.121010` | `8.978·10⁵` |
| `0.25` | `0.5` | `7.871010` | `5.445·10⁵` |
| `0.5` | `0.25` | `8.121010` | `1.016·10¹³` |
| `0.1` | `0.25` | `7.721010` | `2.052·10¹²` |
| `0.1` | `0.1` | `7.721010` | `2.700·10³²` |

### 3.2 The radius is optimal in form

> **Remark P3 (`PROVED`, from Paper 47 Thm V′(ii)).[amended per R155_027, N-6 — the
> previous boxed claim overstated what the proof delivers and misattributed the construction to
> V′(iii); corrected form below.]** No radius with `\log R'(ε,η) = o(1/η)` can work; the exponential
> dependence on `1/η` is forced, and the constant in the exponent is open between `ε` and `G(ε)`.
> Theorem V′(ii) constructs, for every `δ > 0`, large `R` and `η ∈ [0,1]`, a (P)-feasible `μ'_{η,R}`
> with `μ'(\{|τ| ≥ R−\sqrt R\}) ≥ η(1−o(1))` and `∫σ_T dμ' ≤ λ^P + δ + η(\log R + C_1) + o(η)`; such a
> `μ'` lies in `\mathcal F_ε` as soon as `η(\log R + C_1) ≤ ε − δ`, i.e. as soon as `\log R ≲ (ε−δ)/η`,
> and it has mass `≥ η(1−o(1))` beyond `R − \sqrt R`. So the threshold radius at which mass `η` is
> forced to be gone is `\log R ≍ (\text{const})/η`, exactly the shape of Corollary P2; only the
> constant (`G(ε)` versus `ε`) is open — this is the honest content, and it is what is proved, not the
> stronger `o(e^{cB/η})` claim of the earlier box. **The exponential in `1/η` is not an artefact of
> Chebyshev.**

### 3.3 The value-tail, and the one place where explicitness has a price

The deficit statement needs `∫_{|τ|>R}(f−c)dμ`, and `f − c ≤ m + E_R` there (Lemma 3.2 of `R155_001`,
`E_R := A_T + ‖ν‖_{TV} + |β₀|k₀(R) + |β₁|k₁(R) − c`). Proposition P1 controls
`∫_{|τ|>R}(m−C₀)dμ` **only by `G(ε)`**, not by anything small — and by Theorem V′ no uniform rate
exists. The honest statement therefore has two layers.

> **Theorem 3.3ᴾ (`λ^P` bounded-set reduction; `PROVED`).** Let `(ν,β)` be dual feasible of value `c`,
> `ε > 0`, `η ∈ (0,1)`, `R ≥ \max\{R(ε,η;T),2\}` and `μ ∈ \mathcal F_ε`, and suppose
> **[amended per R155_027, N-5] `E_R + C₀ ≥ 0`**. Then
> ```
> 0 ≤ λ^P − c ≤ ∫_{[−R,R]}(f−c)\,dμ + ε_{\mathrm{tail}}(μ,R),
> ε_{\mathrm{tail}}(μ,R) := ∫_{|τ|>R}(f−c)\,dμ ≤ ∫_{|τ|>R}(m−C₀)\,dμ + (E_R + C₀)^+·η,
> ```
> with `∫_{|τ|>R}(m−C₀)dμ ≤ G(ε)` always, and `→ 0` as `R → ∞` for each fixed `μ`. **[N-5]** Without
> the hypothesis `E_R + C₀ ≥ 0`, replace `(E_R + C₀)` by `(E_R+C₀)^+` throughout and the statement
> holds unconditionally; since `C₀ = −5.3721834192 < 0`, the hypothesis can fail for certificates with
> small `‖ν‖_{TV} + A_T + |β|k − c`, though it holds for every certificate on file
> (`‖ν‖_{TV} ≈ 48.7`).

*Proof.* Weak duality (`prop:weak`) gives `∫ f dμ = ∫σ_T dμ` for feasible `μ`, hence
`∫(f−c)dμ = ∫σ_T dμ − c ∈ [λ^P − c, λ^P + ε − c]`; in particular `λ^P − c ≤ ∫(f−c)dμ`. Split the
integral at `R`, bound the tail integrand by `m + E_R = (m−C₀) + (E_R + C₀)` — using `(E_R+C₀)^+` if
`E_R+C₀ ≥ 0` is not assumed — and use Corollary P2 on the second piece and P1 on the first.
Non-negativity of both pieces is `f ≥ c`. ∎

> **Corollary Aᴾ (what a window-only verification can be worth; `PROVED`, fully explicit).**
> Suppose `(ν,β)` satisfies `f ≥ c` **only on `[−R,R]`** with `R ≥ \max\{R(ε,η;T),2\}`, and put
> `W := A_T + ‖ν‖_{TV} + |β₀|\hat g_0(0) + |β₁|\hat g_1(0) − C₀`, so that `f ≥ −W` on all of `ℝ`
> (`lem:mbounds`, `lem:gbounds`, `|\hat g_j| ≤ \hat g_j(0)`). Then for every `ε > 0`
> ```
> c ≤ \frac{λ^P + ε + Wη}{1 − η}.
> ```
> *Proof.* Take `μ ∈ \mathcal F_ε`. Then
> `λ^P + ε ≥ ∫σ_T dμ = ∫f dμ ≥ c·μ([−R,R]) − W·μ(|τ|>R) ≥ c(1−η) − Wη` when `c ≥ 0`
> (and trivially otherwise). ∎

This is the `λ^P` face of the reduction: the **whole value lives on an explicitly computable window**,
and a certificate verified only there cannot claim more than `λ^P` plus an explicit, certificate-dependent
loss `Wη/(1−η)`. It is uniform over the class in the only variables a class controls: `‖ν‖_{TV}` and
`|β|` (the latter now bounded a priori by Theorem B).

> **Corollary Bᴾ (an explicit rate on a sub-family; `PROVED`, with a non-explicit `K(ε)`).** Suppose
> in addition that `μ` satisfies `∫(m−C₀)^{1+δ}dμ ≤ K` for some `δ > 0`. Then by Hölder
> ```
> ∫_{|τ|>R}(m−C₀)\,dμ ≤ K^{1/(1+δ)}\,μ(|τ|>R)^{δ/(1+δ)} ≤ K^{1/(1+δ)}η^{δ/(1+δ)},
> ```
> and `ε_{\mathrm{tail}} ≤ K^{1/(1+δ)}η^{δ/(1+δ)} + (E_R+C₀)η → 0` explicitly in `η`. Such `μ` exist in
> `\mathcal F_ε` for every `ε > 0`: by `thm:Vp`(ii) the `F_0 ∈ C_c^∞(I_T)` with `c_{F_0} ∈ K'` are dense
> in the primitive class, and for those `\hat F_0` is Schwartz, so `∫(m−C₀)^p dμ_{F_0} < ∞` for all `p`.
> **`K = K(ε,δ,T)` is not explicit**, and by Remark P3 it cannot be made uniform over `\mathcal F_ε`.

### 3.4 Consequence for the ceiling: the `M`-rate

> **Corollary Cᴾ (`PROVED`).** With `P = πM/T`, `Δ(M,β) = [m(P/2) − C₀] + 2A_T + 2|β₀|\hat g_0(0) +
> 2|β₁|\hat g_1(0)` as in Theorem R (`R155_004 §6.2`), and `μ ∈ \mathcal F_ε`,
> ```
> Ceil(M,T;β) ≤ λ^P + ε + Δ(M,β)·μ(|τ| > P/2).
> ```
> *(a) Unconditionally*, Proposition P1 gives `μ(|τ|>P/2) ≤ G(ε)/(m(P/2)−C₀)` and hence
> ```
> Ceil(M,T;β) ≤ λ^P + ε + G(ε)\Big[1 + \frac{K_β}{m(P/2)−C₀}\Big],
> K_β := 2A_T + 2|β₀|\hat g_0(0)+2|β₁|\hat g_1(0),
> ```
> which is `O(1)`, not `o(1)`: **Theorem R's convergence cannot be made quantitative on the full feasible
> set**, and this is not a defect of the proof — it is Theorem V′ again.
> *(b) On the sub-family of Corollary Bᴾ*, `μ(|τ|>P/2) ≤ K/(m(P/2)−C₀)^{1+δ}` and therefore
> ```
> Ceil(M,T;β) ≤ λ^P + ε + \big[(m(P/2)−C₀) + K_β\big]\frac{K}{(m(P/2)−C₀)^{1+δ}}
> = λ^P + ε + O\big(K\,(\log M)^{−δ}\big),
> ```
> since `m(P/2) − C₀ = \log(πM/4πT) + O(1) = \log M + O_T(1)`. This is the **first explicit `M`-rate for
> the test-kernel ceiling** in the corpus; it replaces nothing (`R155_004 §6.3`'s `O(1/M)` remains
> `CONDITIONAL` on the withdrawn tail law and the measured `p = 1.25` remains `DIAGNOSTIC`), and it is
> certainly not sharp — but it is unconditional except for `K(ε,δ,T)`.

### 3.5 Check against Paper 47's `prop:env` scales

Paper 47 Prop. 6.4(iii) records the verification thresholds `2πe^{A_T} = 59.5` (multiplier-free) at
`T = \log2` — the same `A_T` serves `T = 0.68` — and `2πe^{A_T+‖ν‖_{TV}} ≈ 10⁴⁰` for the certificate of
§5. The reduction radius of Corollary P2 sits **between** them: `R(0.5,0.5) = 8.98·10⁵`,
`R(0.25,0.25) = 3.74·10¹²`, `R(0.1,0.1) = 2.70·10³²`. The two families are not the same object — `prop:env`
is the radius beyond which `f ≥ 0` is *automatic*, `R(ε,η)` the radius beyond which the primal *mass* is
`≤ η` — but they scale alike (`e^{\text{const}}` with the constant of size `A_T` resp. `B/η`), and
`R(ε,η)` is the smaller of the two for the certificates actually built (`‖ν‖_{TV} ≈ 48.7` in the
comb-vanishing runs of `R155_016`, versus `B/η = 15.2` at `η = 0.5`). Consistent; no contradiction.

### 3.6 What this does **not** do

It does not bound `λ^A − λ^P` (Paper 47 declines to, `main.tex:376`), it gives no lower bound on `c` for
any class, and it therefore does **not** solve Problem A: §3 is still the converse half. What it removes
is the last place where the round-1 material spoke about `λ^A` while Problem A speaks about `λ^P`.

---

## §4. Labels

| statement | label |
|---|---|
| **Theorem N′**: no lattice certificate of step `2T/M` with `M ≤ 24` proves `λ^P(T) > 0`, at `T = 0.68` and at `T = \log2`, `β`-uniformly, for any range, atom count or tail lemma | **PROVED (machine-verified)** — 16 enclosures per window archived in `scripts/r3b/r3b_enclosure_*.json`; `M ∈ \{1,2,3,4,5,8,10,12\}` by sublattice inclusion |
| the certified numbers `Ceil(24,0.68) ≤ −7.4931·10⁻⁶`, `Ceil(24,\log2) ≤ −6.5843·10⁻⁷` | **PROVED (machine-verified)**; the upper endpoints of the enclosures, `β`-allowance included |
| `M = 9` at both windows (`−6.393168·10⁻³`, `−7.469885·10⁻³`) | **PROVED (machine-verified)** after the period-placement scan of §2.5; the first attempt (single placement) failed and is recorded |
| the scope limit: steps `d` with `2T/d ∉ ℕ` are not covered (as in `R155_004 §2.4`) | recorded (§2.6) |
| the Gauss–Legendre panel scheme with the classical remainder and the corpus's Bernstein/Leibniz derivative bounds extended to order `2p`; the `Σw_i = 2` / `\|P_p(x_i)\|` guard | **PROVED** (the remainder formula is classical; the derivative bounds are `R155_004 §2.3(iii)`) |
| Theorem-B constants at `0.68` and `\log2` (`r₀`, `V⋆`, `B`) | **PROVED (machine-verified at 30 digits, not interval-enclosed)**, as at `½log3`; §2.4 gives the **tolerance** (`B ≤ 1.0·10¹¹` suffices at `M=24, T=0.68` [amended per R155_027: stale digit `9.7·10¹⁰` corrected to agree with §0.3 and Table 2.2]), which is what `R155_007 R-2` asked for |
| **Proposition P1**, **Corollary P2** (the explicit `R(ε,η;T)`), **Theorem 3.3ᴾ**, **Corollary Aᴾ** | **PROVED**, fully explicit |
| **Remark P3** (the exponential in `1/η` is forced) | **PROVED**, from Paper 47 `thm:Vp`(ii) [amended per R155_027: corrected from `(iii)`; the boxed `o(e^{cB/η})` overclaim replaced by the proved form, see §3.2] |
| **Corollary Bᴾ**, **Corollary Cᴾ(b)** (rate `O(K(\log M)^{−δ})`) | **PROVED**, with `K = K(ε,δ,T)` **not explicit** and, by P3, not uniformisable |
| **Corollary Cᴾ(a)** (unconditional: `Ceil(M,T;β) ≤ λ^P + ε + O(1)`) | **PROVED**; it is the honest unconditional content of Theorem R |
| the double-precision `Ceil(M,T)` column of §2, the argmax `β`, `τ₀` | **DIAGNOSTIC** (they are only the provenance of the test pair, and the proof does not use them) |
| Problem A (`c ≥ λ^P − D(T,d,U)`) | **OPEN**, untouched |
| is the test-kernel family lossy at **fixed** `M`? | **OPEN** (`R155_004 §8.4`) |

**FATAL-rule compliance.** No statement above concerns the zeros of `ζ`. No sign is claimed for any
`T > \log2`; both windows are `≤ \log2`. The endpoint of record is unchanged
(`λ_{\min}(A_{½\log3}) ≥ 8.8577·10⁻⁵`, Paper 47 Thm C). No LP and no branch-and-bound were run. Every
statement of §2 is an **upper** bound on what a class can achieve, i.e. a negative result; none of them
says anything about whether `λ^P(0.68)` or `λ^P(\log2)` is positive.

---

## §5. Changes proposed to Paper 47 (not applied — the orders forbid touching the paper)

1. **§8, after Theorem N.** Add **Theorem N′** as a second display with the table of §2.2: the same
 statement at the two-prime windows, `M ≤ 24` **including `M = 9`** [amended per R155_027:
 `M = 9` is PROVED (machine-verified), not excepted — see §4; the first single-placement attempt
 failed but the placement-scan remedy of §2.5 closes it], with the certified numbers
 `−7.4931·10⁻⁶` and `−6.5843·10⁻⁷`. This is the paper's first negative class statement at a window
 where the staircase is actually stuck, and it retires the `DIAGNOSTIC` sentences that `R155_010 §1`
 still carries for `Ceil(24,0.68)` and `Ceil(24,\log2)`. Half a page (the machinery is already there
 for Theorem N); one extra sentence for the `M = 9` witness-failure-then-scan-remedy story (and, per
 §2.5, the same for `M = 6`).
2. **§8, in the Theorem-N paragraph.** Replace the sharp `β`-box constant by the **tolerance** form
 (`R155_007 R-2`): "any `B` below `10^{10}` suffices", with the per-row tolerance column of §2.2. This
 is the repair R-2 asked for, and it now has data at three windows.
3. **§8 (or §4).** Add **Corollary Cᴾ(a)** as the honest unconditional reading of Theorem R:
 `\limsup_M Ceil(M,T;β) ≤ λ^P` is qualitative, and no rate uniform over the feasible set exists,
 *because* of Theorem V′. One paragraph, with Cᴾ(b)'s `(\log M)^{−δ}` on the Schwartz sub-family as the
 quantitative statement that survives.
4. **§3 or §4.** Add **Theorem 3.3ᴾ** with Corollaries P2 and Aᴾ. It is the `λ^P` companion of
 `prop:env` and `thm:Vp`: `prop:env` says where `f ≥ 0` becomes automatic, `thm:Vp` says the exchange
 rate, and `3.3ᴾ` says where the primal mass has to be. The `R(ε,η;T)` table of §3.1 and the comparison
 of §3.5 are one short table and one paragraph. This closes `R155_003` repair (1) and
 `R155_010 §5`/`R155_018 §4(iv)`.
5. **§9 (labels table).** The four rows of §4 above: Theorem N′ `PROVED (machine-verified)`; `M = 9`
 **[amended per R155_027] `PROVED (machine-verified)`, not `DIAGNOSTIC`** — see §4, which
 already carries the correct label; Theorem 3.3ᴾ and Cor. Aᴾ `PROVED`; Cor. Bᴾ/Cᴾ(b) `PROVED with a
 non-explicit constant`.
6. **Methods appendix (if one is ever written).** The Gauss–Legendre interval scheme of §2.3, including
 the `Σ w_i = 2` guard and the reason it is needed (the failure recorded in §0.5). Paper 47 currently
 documents only the Simpson enclosure of Theorem C.

---

## §6. Recommendation for round 4

1. **The mixture bound, for when a single placement is not enough.** `M = 9` was rescued by a scan
 (§2.5); the principled version is `c ≤ Σ_iλ_iQ(τ₀_i,φ_i,β)` for convex `λ`, a two-variable LP on top
 of the existing enclosures. Worth implementing once, because it is what will be needed if the
 enclosure is ever pushed to `M` where several placements are active simultaneously.
2. **Do not push `M` upward by enclosure.** The double-precision ceiling crosses zero between `M = 24`
 and `M = 64` at these windows (`R155_004 §3` Run 2, with the `M = 64` sign **withdrawn** per R-4); the
 informative number is the crossing `M`, and finding it needs a converged `τ₀` scan, not more
 enclosures. One refined scan, `DIAGNOSTIC`, would locate it.
3. **Problem A proper.** Everything in rounds 1–3B is upper-bound side. Corollary Aᴾ is the first
 statement that couples a *class* datum (`‖ν‖_{TV}`, `|β|`) to the deficit with an explicit radius; the
 lower-bound half — `c ≥ λ^P − D(T,d,U)` — remains untouched and is the only thing that would make the
 ceiling two-sided.
