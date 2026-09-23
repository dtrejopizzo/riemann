# R155.032 — Builder, round 4a: the even-sector Schur complement at `T = log 2`

*[amended 2026-09-22 per R155_036]*

*Phase 155, round 4a, 2026-09-22. Executes order (a) of `R155_029 §3`. Inherits `R155_026`
(amended) + `R155_028` + `R155_023` (amended), `scripts/r3a/arch_core.py` and the interval
machinery of `scripts/r3c/r3c_04_enclosure_iv.py`. New scripts: `scripts/r4a/`.
**Paper 47 is not touched; no file in `scripts/r3a`, `scripts/r3b`, `scripts/r3c` is modified.**
No sign for `ζ` is claimed at any `T`. Endpoint of record unchanged:
`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Paper 47 Thm C).*

---

## §0 Verdict

*`R155_036` regenerated this `M = 16000, k ≤ 7` run independently (97.5 s) and reproduced every
printed digit of this section.*

**Certified `k = 7`.** For the seven explicit degree-`17` polynomials `e₁ = F*, e₃, e₅, …, e₁₃`
archived in `scripts/r4a/r4a_01.json` (the even `N = 18` Galerkin archimedean eigenvectors at
`T = log 2`), the complete Weil form `W_{log2} = A_∞ + Π_{log2}` is **positive definite on every
nested subspace `E_k = span{e₁,…,e_{2k−1}}`, `k = 1,…,7`**, with rigorous interval-arithmetic lower
bounds on the smallest eigenvalue of the form's matrix in that (orthonormal to `1.1·10⁻¹⁵`) basis:

| `k` | `dim` | **rigorous `λ_min ≥`** | float midpoint | max entry width |
|---|---|---|---|---|
| 1 | 1 | **`3.421189·10⁻²`** | `3.421·10⁻²` | `5.3·10⁻⁶` |
| 2 | 2 | **`2.113566·10⁻³`** | `2.121·10⁻³` | `1.1·10⁻⁵` |
| 3 | 3 | **`4.045259·10⁻⁴`** | `4.124·10⁻⁴` | `2.0·10⁻⁵` |
| 4 | 4 | **`9.076318·10⁻⁵`** | `1.042·10⁻⁴` | `2.9·10⁻⁵` |
| 5 | 5 | **`4.095108·10⁻⁵`** | `6.607·10⁻⁵` | `3.7·10⁻⁵` |
| 6 | 6 | **`2.215585·10⁻⁵`** | `6.603·10⁻⁵` | `4.1·10⁻⁵` |
| 7 | 7 | **`6.568676·10⁻⁶`** | `4.139·10⁻⁵` | `4.7·10⁻⁵` |

(`16000` panels, `118.9 s` in one process — above the `60 s` per-script guideline; the same script at
`5000` panels certifies `k = 5` in `49.6 s`, at `1500` panels `k = 3` in `12 s`. Comparison windows:
`T = 0.62` certified to `k = 5` with `λ_min ≥ 3.92·10⁻⁴` (`32.1 s`); `T = 0.65` to `k = 5` with
`λ_min ≥ 1.70·10⁻⁴` (`37.7 s`).)

**`k = 8` is not certified and is out of reach at feasible panel cost**: at `N = 18` the eighth even mode carries
the Galerkin bottom down to `9.94·10⁻⁷`, `1.6` orders below the entry widths.

> **This is NOT positivity of the form.** `E₇` is a `7`-dimensional subspace of the
> infinite-dimensional `P_{log2}^{even}`; positivity on it says nothing about the rest, and §4 shows
> that the near-zero bottom of the Galerkin problem is carried by the **last** even mode included, at
> both `N = 18` and `N = 36`, i.e. it is **not** captured by any fixed finite `k`. What is proved is:
> *the Weil form at `T = log 2` is positive definite on an explicit `7`-dimensional space of
> polynomials, with a certified margin `6.57·10⁻⁶`*. It extends Theorem 3c.3 (`k = 1`) from a line to
> a `7`-plane and does not touch the endpoint of record.

Two further proved structural facts (§2, §5): **`b = P_V Π_T F*`** — the Schur coupling vector is
*purely* the prime form, the archimedean part contributes nothing (Thm 4a.1) — and **`Π_T` is minus
the real part of a sum of `#contacts` truncated shifts, each a partial isometry with
infinite-dimensional defect** (Prop 4a.4), so it is neither finite rank nor compact; "rank structure"
is the wrong question and the right one is the ℓ²-row bound of Prop 4a.5.

---

## §1 Corpus check (grep-verified, `03-research` + `04-papers`)

| query | hits | prior art | new here |
|---|---|---|---|
| `Feshbach` | **381** files | the Schur/Feshbach reduction is standard equipment in the corpus; the closest is `phase-116/previous-phase-114/114_d_56_PARITY_FESHBACH_INERTIA_CERTIFICATE_AND_STRUCTURAL_NOGOS.md` (D.56): parity splitting of a Schur matrix + interval enclosures of Feshbach entries, on the prolate core. `R155_026 §1` already credits it | nothing about the *method* is new; the pivot (`F*`, prime-independent), the window (`log 2`) and the object (nested even subspaces of `P_T`) are as in `R155_026`, and what is added is the **matrix** enclosure rather than the single value |
| `2x2 block` | 4 files: `phase-77/E77_7AQ_EVEN_CHANNEL_REDUCTION.md`, `E77_7AR`, `E77_7AS`, `phase-78/E78_4` | E77_7AQ/7AR already localise a difficulty "**inside the even 2x2 block**" and lock an eigendirection there — the **same phenomenon, different object** (the Weyl limit-point pencil of phase 77, not `W_T` on `P_T`) | the `2 × 2` block here is `span{F*, e₃}` of `W_{log2}`, with a *rigorous enclosure* of its determinant; phase 77's block is diagnostic |
| `2×2 block` (typographic) | 0 | — | — |
| `third eigenvector` | **0** | nothing | the identification of `e₃` as the direction carrying `99.46 %` of the `S_even` ground state is `R155_026 §5(c)`; here its coupling numbers to `F*` are decomposed by prime |
| `e_3` | 6 files, all unrelated (Witt Gram, Eulerian idempotents, stage-3 status) | — | — |
| `nested subspace` | 1 file (`phase-3-uniform-inequality/phase3-plan.md`, a plan line) | **no note in the corpus certifies positivity of the Weil form on an explicit finite-dimensional subspace beyond one direction** | §3 is the first |
| `interval Cholesky` | **0** | — | the certification device of §3 is new to the corpus |
| `partial isometr` | 31 files (`P124_014`, `MAP_5`, `P122_016`, …), all about Frobenius/determinant carriers | — | Prop 4a.4 (the truncated shift decomposition of `Π_T`) is new *in this form*; it is elementary |

---

## §2 Structure of the prime form on the even archimedean eigenbasis

`scripts/r4a/r4a_01_structure.py` (`25.0 s`, `DIAGNOSTIC` except Thm 4a.1 / Props 4a.4–4a.5).

### Theorem 4a.1 (the Schur coupling vector is purely prime). `PROVED`.

Let `F*` be a unit eigenvector of `A_∞|P_T` with eigenvalue `λ₁`, `V = F*^⊥ ∩ P_T`,
`b := P_V W_T F*`. Then

> **`b = P_V Π_T F*`**,

i.e. the archimedean form contributes **nothing** to the off-pivot coupling.
*Proof.* `W_T F* = A_∞ F* + Π_T F* = λ₁ F* + Π_T F*`, and `P_V F* = 0`. ∎
*(Numerically `‖b − P_VΠ_TF*‖/‖b‖ ≤ 4.7·10⁻¹⁵` at all four runs — an implementation check, not a
proof input.)*

**Consequence.** The `0.06`–`0.31` failure of the ideal condition `λ₃ − ‖b‖²/w₁₁ > 0` recorded in
`R155_026 §5(c)` is a statement **entirely about the primes**: `‖b‖²/w₁₁ = ‖P_VΠ_TF*‖²/w₁₁`. The
"cancellation inside `V_even`" is thus a cancellation *of the prime form against itself* — its
rank-one projection along `F*` against its restriction to `V` — with `A_∞` entering only through the
spectral gap `λ₃` and through `w₁₁`'s denominator.

### The matrix `π_ij = Π_{log2}(e_i,e_j)` on the first 8 even archimedean eigenvectors

`N = 18`, `T = log 2`, contact set `{2,3}`, `λ`-labels `λ₁ = −0.15428`, `λ₃ = 0.46817`,
`λ₅ = 0.84413`, `λ₇ = 1.11588`, `λ₉ = 1.33900`, `λ₁₁ = 1.61312`, `λ₁₃ = 2.06131`, `λ₁₅ = 3.23383`
(all `DIAGNOSTIC`; signs of eigenvectors are a gauge, so individual off-diagonal signs are not
invariant, but `|π_ij|` and the sign of `π_ij π_jk π_ki` are):

```
        e1       e3       e5       e7       e9      e11      e13      e15
 e1  +0.1885  +0.0457  +0.0302  -0.1338  -0.0511  +0.0175  -0.0456  -0.0268
 e3  +0.0457  -0.4009  -0.0449  -0.1765  -0.0481  -0.0001  -0.0293  -0.0090
 e5  +0.0302  -0.0449  +0.6563  -0.4553  -0.1352  +0.0590  -0.0870  -0.0653
 e7  -0.1338  -0.1765  -0.4553  -0.2084  -0.2128  +0.1769  -0.0889  -0.0587
 e9  -0.0511  -0.0481  -0.1352  -0.2128  +0.1815  +0.2808  -0.0018  -0.0406
e11  +0.0175  -0.0001  +0.0590  +0.1769  +0.2808  -0.2358  -0.3423  +0.0982
e13  -0.0456  -0.0293  -0.0870  -0.0889  -0.0018  -0.3423  -0.0790  +0.0140
e15  -0.0268  -0.0090  -0.0653  -0.0587  -0.0406  +0.0982  +0.0140  +0.0017
```

Readings (`DIAGNOSTIC`).
1. **No band structure, no decay worth the name.** The maxima of `|π_ij|` by `|i−j|` are
   `0.656, 0.455, 0.177, 0.134, 0.087, 0.065, 0.046, 0.027` — a factor `24` over seven bands, i.e.
   roughly `|i−j|^{-1.5}`, with the diagonal *not* dominant (`|π₇₉| = 0.213 > |π₉₉| = 0.182`,
   `|π₅₇| = 0.455 > |π₇₇| = 0.208`). The prime form does **not** decouple the archimedean modes; it
   mixes them at full strength across the whole even sector. This is the structural reason why the
   Galerkin bottom (§4) is not carried by a few low modes.
2. `π₁₁ = +0.1885` is the number `Π_T[F*]` of `R155_026 §3`; `π₃₃ = −0.4009` is strongly negative and
   **eats `86 %` of the archimedean gap `λ₃ = 0.4682`**: the `(3,3)` entry of `W` is only `+0.0673`.
   The `2 × 2` block of `W` on `span{F*, e₃}` is therefore
   `[[0.034212, 0.045730],[0.045730, 0.067280]]` — a nearly singular matrix by construction.
3. `b`'s even components are `(0, +0.04573, +0.03023, −0.13379, −0.05113, +0.01746, −0.04561,
   −0.02679)` and its odd components are `≤ 1.3·10⁻¹⁵` (parity, `R155_026 §5(b)`). **`b` is not
   dominated by `e₃`**: its largest component is on `e₇` (`0.1338`, `b₇/‖b‖ = 0.820` of the norm,
   i.e. `67 %` of the mass `b₇²/‖b‖² = 0.6724`), and
   `e₃` carries only `8 %` of the mass. The `99.46 %`-on-`e₃` fact of `R155_026 §5(c)` is about the
   ground state of `S_even`, not about `b`: `e₃` wins there because it is divided by the smallest
   available gap (`λ₃ = 0.468` against `λ₇ = 1.116`), not because the coupling points at it.

### The two shifts

`Π_T(F,G) = −Σ_{n<e^{2T}} v_n · ½⟨F, (τ_{log n} + τ_{log n}^*)G⟩`, `(τ_u G)(t) = G(t−u)` truncated to
`(−T,T)`, `v_2 = 2log2/√2 = 0.98026`, `v_3 = 2log3/√3 = 1.26857`. So at `log 2` the prime form is
exactly **two** shift forms. Their separate matrices `−v_n C_n` on the even eigenbasis (`r4a_01.json`,
keys `shift_2`, `shift_3`):

| entry | `n = 2` part | `n = 3` part | sum `= π_ij` | cancellation |
|---|---|---|---|---|
| `(1,1)` | `+0.4434` | `−0.2549` | `+0.1885` | `58 %` |
| `(1,3)` | `+0.1867` | `−0.1410` | **`+0.0457`** | **`76 %`** |
| `(1,5)` | `+0.0212` | `+0.0090` | `+0.0302` | — |
| `(1,7)` | `−0.0614` | `−0.0724` | `−0.1338` | — |
| `(3,3)` | `−0.3986` | `−0.0022` | `−0.4009` | `0 %` |
| `(5,5)` | `+0.3871` | `+0.2691` | `+0.6563` | — |

**How `e₃` couples to `F*`**: through the `log 2` shift with amplitude `+0.1867` and through the
`log 3` shift with `−0.1410`; the two nearly cancel, leaving `π₁₃ = +0.0457`, four times smaller than
either. The single number that decides the `2 × 2` block (§3) is therefore a **`76 %` cancellation
between the atoms at `2` and at `3`** — and, by Theorem 4a.1, that number *is* the coupling `b₃`.
The diagonal `π₃₃ = −0.4009` is, by contrast, carried almost entirely by the `log 2` atom
(`−0.3986`); the `log 3` atom is inert on `e₃` (`−0.0022`).

---

## §3 The theorems: rigorous positive definiteness on nested even subspaces at `log 2`

`scripts/r4a/r4a_lib.py` + `scripts/r4a/r4a_02_nested_enclosure.py`.

### The device

`R155_026 §4` encloses `W_T[F]` for **one** polynomial. The obstruction to enclosing a *matrix* is
that the affine kernel sandwich of step 4 there is licensed by `G = c(0) − c ≥ 0` (Cauchy–Schwarz),
which holds for an **auto**correlation and fails for a cross-correlation. The fix used here is
**polarisation**: for `i ≠ j`,

  `W_T(e_i,e_j) = ¼(W_T[e_i+e_j] − W_T[e_i−e_j])`,

so only quadratic values are ever enclosed and every step of `r3c_04_enclosure_iv.py` applies
verbatim. Second, the panel work is refactored: because the panelwise affine bounds
`K_lo ≤ K ≤ K_hi` do **not** depend on `G`, and `G ≥ 0`,

  `T∫_δ² G(s)K(Ts)ds ∈ [⟨L_lo, G⟩, ⟨L_hi, G⟩]`

for two fixed linear functionals `L_lo, L_hi` on the `36` monomial coefficients of `G`, computed once
over the `M` panels. Each further form value then costs one `36`-dimensional interval dot product plus
the exact polynomial autocorrelation. This is what makes `k(k+1)/2` enclosures affordable.

### Proposition 4a.2 (polarisation enclosure). `PROVED`.
If `W[e_i±e_j] ∈ [p^-,p^+]`, `[m^-,m^+]`, then `W(e_i,e_j) ∈ [(p^- − m^+)/4, (p^+ − m^-)/4]`, and the
interval matrix `𝑴 = (M_ij)` so obtained contains the true matrix of `W_T` on
`span{e₁,…,e_{2k−1}}`. *Proof.* Bilinearity of `W_T` (Paper 47 `thm:A`, `thm:S`(iii): every term is a
bilinear functional of `(F,G)` through the symmetric cross-correlation) plus interval inclusion
monotonicity. ∎

### Proposition 4a.3 (certification). `PROVED` (standard interval linear algebra).
If the interval Cholesky factorisation of `𝑴 − μI` runs to completion with every pivot interval
strictly positive, then **every** real symmetric matrix in `𝑴` has `λ_min > μ`. Bisection on `μ`
gives the certified lower bounds of §0. *(Alefeld–Herzberger / Rump: a successful interval Cholesky
is a verified positive-definiteness certificate. Implemented in `r4a_lib.lam_min_lower`.)*

### Theorem 4a.A (the `2`-plane at `log 2`). `PROVED` (interval arithmetic, `r4a_02`).

For the two explicit degree-`17` polynomials `F* = e₁` and `e₃` archived in
`scripts/r4a/r4a_01.json` (`T = log 2`, basis orthonormal to `1.1·10⁻¹⁵`), the matrix of `W_{log2}`
on `span{F*, e₃}` is enclosed by

  `w₁₁ ∈ [0.0342119, 0.0342172]`, `w₁₃ ∈ [0.0457297, 0.0457375]`, `w₃₃ ∈ [0.0672858, 0.0672971]`,

hence `det = w₁₁w₃₃ − w₁₃² ∈ [2.1005·10⁻⁴, 2.1151·10⁻⁴] > 0` and

> **`W_{log2}` is positive definite on the `2`-plane `span{F*, e₃}`, with `λ_min ≥ 2.113566·10⁻³`.**

Equivalently, in the notation of the order, `w₁₁(λ₃ + π₃₃) − π₁₃² > 2.10·10⁻⁴`: the `76 %`
prime-atom cancellation in `π₁₃` (§2) is exactly what makes this determinant positive. Had the two
atoms *not* cancelled — e.g. at `π₁₃ = 0.1867` (the `log 2` atom alone) — the determinant would be
`0.0342·0.0673 − 0.0349 = −0.0326 < 0` and the form would be indefinite already on this `2`-plane.
**The positivity of `W` at `log 2` is visible, in two dimensions, as a cancellation between the atom
at `2` and the atom at `3`.**

### Theorem 4a.B (the nested tower at `log 2`). `PROVED` (interval arithmetic, `r4a_02`, `118.9 s`).

With `e₁,…,e₁₃` the seven archived even polynomials, `W_{log2}` is positive definite on every
`E_k = span{e₁,…,e_{2k−1}}`, `k ≤ 7`, with the certified `λ_min` of §0; in particular

> **`W_{log2}[F] ≥ 6.5686·10⁻⁶·‖F‖²` for every `F ∈ E₇`**
> (the Gram matrix of the basis is enclosed and differs from `I` by at most `1.07·10⁻¹⁵` per entry,
> so the Rayleigh transfer costs nothing at this precision).

### Theorem 4a.C (comparison windows). `PROVED` (same machinery).
At `T = 0.62`: `λ_min ≥ 3.924·10⁻⁴` on `E₅`. At `T = 0.65`: `λ_min ≥ 1.696·10⁻⁴` on `E₅`.
(`4000` panels, `32.1 s` / `37.7 s`.) The certified margin shrinks with `T`, monotonically, exactly
as the `w₁₁` sequence of `R155_026 §3` does.

### Scope, stated plainly
`E₇` is `7`-dimensional; `P_{log2}^{even}` is not. Nothing here bounds `W_{log2}` from below on
`P_{log2}`, on `V`, or on `S_even`; nothing here improves `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`; nothing
here bears on `ζ`. The honest content is: *the complete Weil form at `log 2`, primes included, is
rigorously positive definite on an explicit `7`-dimensional space of polynomials* — the first
statement in the corpus about the Weil form on a subspace of dimension `> 1`.

---

## §4 The Galerkin trend, and the dimension of the obstruction (`DIAGNOSTIC`)

`λ_min` of `W` on `E_k` as `k` grows (`r4a_01.json`, key `trend_even`):

| `k` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| `N = 18`, `log 2` | `3.421e−2` | `2.117e−3` | `4.090e−4` | `1.005e−4` | `6.229e−5` | `6.225e−5` | `3.771e−5` | **`9.942e−7`** |
| `N = 36`, `log 2` | `3.415e−2` | `2.110e−3` | `4.070e−4` | `9.630e−5` | `6.805e−5` | `3.463e−5` | `3.379e−5` | `3.377e−5` |

`N = 36` continues: `k = 9…17` give `3.322e−5, 3.205e−5, 3.046e−5, 2.806e−5, 2.578e−5, 2.061e−5,
1.398e−5, 6.308e−6,` **`1.049e−7`**.

**Answers to the order's question.**
1. **Monotone: yes**, strictly decreasing in `k` at both `N` (min–max forces it: `E_k ⊂ E_{k+1}`).
2. **Which `k` first captures the near-zero bottom: the last one, at every `N`.** At `N = 18` the
   bottom `9.94·10⁻⁷` appears only at `k = 8 = dim P_T^{even}`; at `N = 36` the bottom `1.05·10⁻⁷`
   appears only at `k = 17 = dim P_T^{even}`. The drop in the final step is a factor `38` (`N = 18`)
   and `60` (`N = 36`); the previous step drops by `2.7` and `2.2`.
3. **Therefore the "dimension of the obstruction" is not finite in this sense.** The near-zero bottom
   is carried by the **highest** even archimedean mode present in the truncation, and the bottom
   itself keeps falling with `N` (`9.94·10⁻⁷ → 1.05·10⁻⁷`, a factor `9.5` from `N = 18` to `N = 36`).
   The Galerkin value is an **upper** bound on the infimum, so this is consistent both with a
   positive but tiny infimum and with a *negative* one; **the `N`-trend at `log 2` does not
   stabilise, and no claim about `inf W_{log2}|P_T` is made or supportable from it.** This is the
   sharpest honest reading of round 4a and it *weakens*, not strengthens, the `DIAGNOSTIC`
   `λ_min(W_{log2}|P_T) ≈ 10⁻⁶`–`10⁻⁷` of `R155_026 §3`.
4. Consistency with §2.1: the prime matrix has no band decay, so the minimiser is spread over all
   even modes with weight on the top — which is what item 2 measures.
5. Odd sector for reference: `λ_min(W|V_odd) = 3.23·10⁻⁵` (`N = 18`), `1.12·10⁻⁵` (`N = 36`) — an
   order above the even bottom at both `N`. The even sector is where everything happens, as
   `R155_026 §5(b)` proved it must be.

---

## §5 Pure math on `Π_T`

### Proposition 4a.4 (what `Π_T` is). `PROVED`.
Let `R_T` be restriction to `(−T,T)` and `τ_u` translation by `u`. On `L²(−T,T)`,

  `Π_T = −Σ_{n<e^{2T}} v_n · Re(U_n)`, `U_n := R_T τ_{log n} R_T`,

and each `U_n` is a **partial isometry** with initial space `L²(−T, T−log n)`, final space
`L²(−T+log n, T)`, and defect spaces of dimension `∞` (namely `L²(T−log n,T)` and `L²(−T,−T+log n)`).
Consequently: `‖U_n‖ = 1`, `‖Π_T‖ ≤ A_T := Σ v_n` (`= 2.24883` at `log 2`), and `Π_T` is
**neither finite rank nor compact** (a partial isometry with infinite-dimensional initial space is
not compact, and `Re(U_n)` inherits non-compactness whenever `log n < 2T`; the clean argument for any
`#contacts ≥ 1`: let `a₀ = min_n log n` over the active `n` and take `f` supported in
`(−T,−T+a₀)`; then `R_Tτ_{−log n}R_T f = 0` for every active `n`, so `Π_T f = −½Σ_n v_nτ_{log n}f`
restricted to `(−T,T)`, a fixed non-zero multiple of an isometry on the infinite-dimensional subspace
of functions supported in `(−T,−T+a₀)` — hence `Π_T` is not compact). So the
order's first guess ("rank `≤ 2·#contacts`") is **false**, and the correct finiteness statement is
that `Π_T` is a finite sum of *fixed-norm shift forms*, not a finite-rank perturbation.
*Proof.* `c_{F,G}(u) = ⟨F, R_Tτ_uR_TG⟩`; `τ_u` is unitary on `L²(ℝ)` and `R_T` is an orthogonal
projection, so `R_Tτ_uR_T` is a contraction which is isometric exactly on the vectors supported in
`(−T,T−u)`; `Π_T(F,G) = −Σ v_n·½(c_{F,G}(log n) + c_{G,F}(log n))` is the real part. ∎

### Proposition 4a.5 (the honest matrix bounds). `PROVED`.
For any orthonormal system `(e_i)` in `L²(−T,T)`:
**(i)** `|Π_T(e_i,e_j)| ≤ Σ_n v_n ‖e_i‖‖e_j‖ = A_T` (the order's requested bound);
**(ii)** better, **`Σ_j Π_T(e_i,e_j)² ≤ A_T²` for every `i`** — each *row* of the matrix is `ℓ²` with
norm `≤ A_T`, because `(Π_T(e_i,e_j))_j` are the coefficients of the single vector `Π_T e_i`, and
`‖Π_T e_i‖ ≤ A_T`. Measured row norms at `log 2` on the eight even modes: `0.25, 0.42, 0.81, 0.62,
0.39, 0.50, 0.37, 0.11` — well inside `A_T = 2.249`, and **not** decaying in `i`.
*Proof.* (i) Cauchy–Schwarz termwise with `‖U_n‖ = 1`. (ii) Bessel. ∎

### Regularity of the archimedean eigenvectors — `CONDITIONAL`, stated honestly.
On `P_T` the form is `A_∞[F] = (C₀ + ∫_{2T}^∞K)‖F‖² + ∫₀^{2T}(‖F‖² − c_F(u))K(u)du`, whose operator is
`(C₀ + ∫_{2T}^∞K + κ(t))·I − 𝒦`, where `𝒦` has kernel `½K(|t−t'|)` on `(−T,T)²` and
`κ(t) = ∫₀^{2T}K` is a divergent constant cancelling the diagonal singularity of `𝒦`; i.e. `A_∞|_{P_T}`
is a **finite-part (hypersingular, `log`-type) convolution operator** plus the two rank-one
constraints. Its eigenfunctions are therefore real-analytic in the **interior** of `(−T,T)` (elliptic
regularity for a convolution with an analytic symbol away from the singular support) but generically
have **endpoint singularities** of the airfoil/prolate type, `(T²−t²)^{±1/2}`-flavoured; the
Legendre-Galerkin approximants absorb this into their top coefficients, which is visible as the
`k = dim` drop of §4. **No decay of `Π_T(e_i,e_j)` in `|i−j|` follows**, and none is observed (§2.1:
band maxima fall only like `|i−j|^{-1.5}` over seven bands). Any statement of the form "`e_i` smooth
`⟹ π_ij` decays" is therefore **not available**; the ℓ²-row bound of Prop 4a.5(ii) is the true
statement, and it is not a decay statement. `CONDITIONAL` (the interior analyticity), `PROVED`
(Prop 4a.5), `REFUTED as stated` (a `|i−j|`-decay strong enough to truncate the even sector).

---

## §6 Labels

| statement | label |
|---|---|
| **Thm 4a.1** `b = P_V Π_T F*` (the Schur coupling is purely prime) | **`PROVED`** (two lines) |
| **Prop 4a.2** polarisation enclosure of the matrix | **`PROVED`** |
| **Prop 4a.3** interval Cholesky ⟹ verified `λ_min > μ` | **`PROVED`** (standard, Alefeld–Herzberger/Rump) |
| **Thm 4a.A** `W_{log2} > 0` on `span{F*,e₃}`, `λ_min ≥ 2.113566·10⁻³`, `det ≥ 2.10·10⁻⁴` | **`PROVED`** (machine-verified interval arithmetic, `mp.iv` `dps = 60`, no error budget) |
| **Thm 4a.B** `W_{log2} ≥ 6.5686·10⁻⁶‖·‖²` on the explicit `7`-plane `E₇` | **`PROVED`** (same) |
| **Thm 4a.C** `E₅` at `0.62` (`≥ 3.924·10⁻⁴`) and `0.65` (`≥ 1.696·10⁻⁴`) | **`PROVED`** (same) |
| `k = 8` (the full `N = 18` even sector) certified | **not achieved**; out of reach at feasible panel cost |
| **Prop 4a.4** `Π_T = −Σ v_n Re(R_Tτ_{log n}R_T)`, partial isometries, not compact, not finite rank | **`PROVED`** |
| **Prop 4a.5** `|π_ij| ≤ A_T`; `Σ_j π_ij² ≤ A_T²` | **`PROVED`** |
| decay of `π_ij` in `|i−j|` sufficient to truncate the even sector | **`REFUTED` as stated** (`DIAGNOSTIC` evidence, §2.1) |
| interior analyticity of the archimedean eigenvectors; endpoint singularity type | **`CONDITIONAL`** |
| the `π_ij` table, the two-shift decomposition and its `76 %` cancellation at `(1,3)` | `DIAGNOSTIC` (Galerkin, `N = 18`) |
| the trend table; bottom carried by the last even mode at both `N`; `9.94e−7 → 1.05e−7` in `N` | `DIAGNOSTIC`; **and it does not support any claim about `inf W_{log2}\|P_T`** |
| `λ_min(W_{log2}\|P_T) ≈ 10⁻⁶` as a *converged* number | **withdrawn as unsupported**; it is an unconverged Galerkin upper bound |
| positivity of the form `W_{log2}` on `P_{log2}`, any sign for `ζ`, any change to the endpoint of record | **not claimed, unchanged** |

---

## §7 Proposal for Paper 47 (not applied; Paper 47 untouched)

1. **§8, after the `thm:w11` remark: a short subsection "Positivity on explicit subspaces".**
   Theorem 4a.B with its scope paragraph, and Theorem 4a.A written out as the `2 × 2` determinant
   with the prime-atom cancellation displayed — it is a one-page, fully checkable illustration that
   the complete Weil form is a *rigorously computable* bilinear form on explicit polynomials, and
   that at `log 2` its positivity is an arithmetic cancellation between the atoms at `2` and `3`
   rather than an archimedean margin. Together with `thm:w11` (`k = 1`) this reads as a natural
   strengthening; the `k = 7` margin `6.57·10⁻⁶` and the explicit basis belong in the repository.
2. **§8, Theorem 4a.1 as a displayed remark** in the Schur subsection proposed by `R155_026 §7`:
   it is two lines, and it sharpens the statement of the obstruction — *the Schur correction
   `bb*/w₁₁` is built only from the prime form*, so every impossibility proved for the complement
   (Prop TK, Theorem N′) is an impossibility about the primes' self-cancellation, not about the
   archimedean gap.
3. **§8 or §2, Proposition 4a.4** as the structural description of `Π_T` (a finite sum of truncated
   shifts = partial isometries, `‖Π_T‖ ≤ A_T`, non-compact). It costs four lines, it is the correct
   replacement for any "finite rank" intuition, and it is what rules out the truncation strategies
   §5 discusses.
4. **A cautionary sentence, §8 or the concluding section:** the Galerkin bottom at `log 2` is carried
   by the top mode of the truncation and falls by an order between `N = 18` and `N = 36`; Paper 47
   should not cite any numerical value of `inf W_{log2}|P_{log2}`.

---

*Deliverables: this file; `scripts/r4a/` (`README.md`, `r4a_lib.py`, `r4a_01_structure.py`,
`r4a_02_nested_enclosure.py`, `r4a_01.json`, `r4a_02_log2.json`, `r4a_02_0.62.json`,
`r4a_02_0.65.json` — the archived Legendre coefficient vectors of every eigenvector used are in
`r4a_01.json`, key `even_coef`). `scripts/r3a`, `scripts/r3b`, `scripts/r3c`, `R155_024`, `R155_026`
and Paper 47 untouched.*
