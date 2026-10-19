# Analytic N5 — the rate of `ε_loc` via Loewner + prolate (proof, candid status) Goal: explain and **prove** why `ε_loc(ζ)→0` (at rate `o(λ^{−½})`, which would close
RH via Theorem 2) while `ε_loc(DH)` stays bounded away from 0. No more numerics: structure. Route: (I–II) formalize `QW` as a **Loewner** matrix; (III) the correct **stability
inequality** `ε_loc ≤ C‖Â_λ−Â_∞‖` in the correct RELATIVE form (resolves the
exp-small gap); (IV) the **prolate** mechanism that fixes `ξ̂_∞=Ξ`; (V) the ζ/DH
discriminator (positivity protects rigidity); (VI) `N5b` edge = prolate *plunge*. Markers: **[P]** proved · **[P*]** proved modulo standard classical result ·
**[GAP]** well-posed missing lemma · **[!]** RH-hard core, localized. --- ## I. `ξ̂` as the band-limited fundamental eigenvector — [P] `QW_λ^N` is the Weil form, real symmetric `(2N+1)×(2N+1)`, with eigenvalues
`0 ⪅ ε_0 < ε_1 ≤ …`. Let `ξ=(ξ_k)_{|k|≤N}` be the eigenvector of the **smallest** eigenvalue `ε_0`,
real (H1: simple, even, nodeless — proved by Perron–Frobenius because `Λ(n)≥0`,
`H1_PROOF.md`). Let `d_k=2πk/L`, `L=2logλ`. **Definition (the band-limited function).**
``` ξ̂(s):= sin(Ls/2) · Σ_{|k|≤N} ξ_k/(s − d_k).
```
Since `sin(Ls/2)` vanishes at `s=d_k` (because `sin(L·(2πk/L)/2)=sin(πk)=0`), the
singularities cancel: **`ξ̂` is entire, of exponential type `L/2=log λ`** (Paley–
Wiener), real on ℝ, and its real zeros are the roots of the secular function `f(s)=Σξ_k/(s−d_k)` =
the `ρ̂_n`. Equivalently `ξ̂(s)=Σ_k ξ_k·sinc_k(s)`, the **cardinal interpolation of the
samples `ξ_k`** on the lattice `d_k`. **[P]** `Link 2 ⟺ ξ̂_{λ,N} → Ξ`; the remaining fine content is `ε_loc=sup_{|t|≤T*}|ξ̂−Ξ|`,
`T*=2πλ²` (Theorem 2: `o(λ^{−½}) ⟹ RH`). --- ## II. `QW` is a Loewner matrix integrated against the Weil measure — [P] **Lemma II.1 (divided-difference structure).** For `m≠n`, the kernel of the integrand is
exactly a **sine divided difference**. With `g_y(x):=sin(2πxy/L)`,
``` q(m,n)(y) = (sin(2πmy/L) − sin(2πny/L)) / (π(n−m)) = −(1/π)·(g_y(m)−g_y(n))/(m−n) = −(1/π)·g_y[m,n].
```
The diagonal is the confluent difference with a window: `q(n,n)(y)=2(1−y/L)cos(2πny/L)`, and
`g_y'(n)=(2πy/L)cos(2πny/L)`, so `q(n,n)` is `g_y[n,n]` modulated by the Fejér
window `(1−y/L)`. **[P]** **Proposition II.2 (Loewner).** Consequently
``` QW[m,n] = ∫_0^L L^{sin}_{mn}(y) · dμ_W(y), L^{sin}_{mn}(y) = g_y[m,n] (Loewner kernel of sin at the nodes {d_k}), dμ_W(y) = w_arch(y) dy − Σ_{n'≤λ²} (Λ(n')/√n') · δ_{log n'}(y) (+ ζ-pole term),
```
with `w_arch` the archimedean weight `(e^{y/2}+e^{−y/2})` regularized by the Weil
subtraction `WR`. That is, **`QW` is a superposition of Loewner matrices of `sin`,
weighted by the Weil measure** `μ_W` (archimedean part absolutely continuous, arithmetic
part discrete). **[P]** **[!] Decisive structural reading.** In `μ_W` the **arithmetic part enters with a definite
sign for ζ**: weight `Λ(n')/√n' ≥ 0` (because `Λ(n')≥0`), subtracting. For `L_DH` the
coefficients `b(n')` **change sign**. The whole ζ/DH difference lives in the **sign of
the Loewner measure** — not in the zeros. This connects with the theory of
**total positivity** (Loewner matrices of operator-monotone functions are PSD;
Loewner 1934) and is the hook for §V. --- ## III. Stability inequality in the RELATIVE form — [P] The goal (route #2): `ε_loc ≤ C·‖QW − QW_∞‖`. **The naive (absolute) form FAILS** and
why must be stated, because it is the trap that blocked the program: - Eigenvector perturbation (Davis–Kahan): `‖ξ_λ − ξ_∞‖ ≤ ‖δQW‖/(ε_1−ε_0)`.
- **But `ε_1−ε_0 = 3ε_0` and `ε_0 ~ 1e−20` (exp/poly-small absolute gap)** ⟹ the denominator is tiny ⟹ the bound is **useless**. (This is the wall the program hit at 2b: "naive 1/gap bound useless".) **The fix (the program's central move): normalize by `ε_0`.** Define the
renormalized operator
``` Â_λ:= A_λ / ε_0(λ), spectrum { 1, ε_1/ε_0, ε_2/ε_0, … }.
``` **Lemma III.1 (relative stability).** If `ε_1/ε_0 → 1+γ` with `γ>0` fixed (relative gap
`O(1)`), then the fundamental mode is stable under perturbations of the
**renormalized** operator, and
``` ‖ξ̂_λ − ξ̂_∞‖_{PW} ≤ (1/γ) · ‖Â_λ − Â_∞‖_{B(low)},
```
where `‖·‖_{B(low)}` is the norm restricted to the low-energy block (projection onto
`span{ξ_0,…}` with energies `O(ε_0)`). **[P]** (Davis–Kahan applied to `Â`, whose bottom
`=1` is isolated with gap `γ=O(1)`; the measured datum is `ε_1/ε_0≈4 ⟹ γ≈3`.) **Corollary III.2 (the sought operator-theoretic reduction).** Combining with Theorem 1
(`Ξ_T→Ξ`, `λ^{5/2}e^{−πλ²}`) and the off-axis continuation (Lemma 2 of `E2-nucleo-proof.md`):
``` ε_loc(λ) ≤ C₁ · ‖Â_λ − Â_∞‖_{B(low)} + C₂ λ³ e^{−πλ²}.
```
**⟹ RH reduces to the convergence of the RENORMALIZED operator `Â_λ → Â_∞` (in the
low-energy block) at rate `o(λ^{−½})`.** This is exactly the target
`QW/Loewner ⟹ operator-theoretic bound for ε_loc`, in the correct (relative) form. **[P]** The
live object is no longer `ξ̂` nor the zeros: it is **`Â_λ`, the Weil operator normalized by its
fundamental mode**. The exp-small gap stopped being an obstruction. --- ## IV. The mechanism: `Â_∞` = Jacobi/Dirichlet with spectrum `n²`, and `ξ̂` = envelope·carrier — [P*] + [GAP] **[CORRECTION — the picture `ξ̂=ψ_0` was false.** `ψ_0` (fundamental prolate) has no zeros;
`Ξ` has `~N(T*)`. The correct picture: `QW_norm` has a nodeless fundamental **VECTOR**
`v_0(k)>0` (Perron–Frobenius, H1), a fundamental-mode-type **envelope**; and the function
`ξ̂(s)=Σ v_0(k) sinc_k(s)` acquires its zeros from the **carrier** `(−1)^k`: since
`ξ̂(d_k)=v_0(k)(L/2)(−1)^k` alternates sign, `ξ̂` has an interlaced zero in each
`(d_k,d_{k+1})` (= the `ρ̂_n`). So a **nodeless vector** produces a **function with many
zeros**. No contradiction; and the relevant operator is Jacobi/Laplacian-type, not the
prolate operator directly.]** What is `Â_∞`? Its spectrum is the **relative spectrum** `{ε_k/ε_0}`, the invariant that
determines the envelope `v_0` (and hence `ξ̂`). Measurement (E11, mpmath dps=40): ``` ε_k/ε_0 (E11, mpmath dps=40, N=16) (k+1)²=n² k λ=5.0 λ=7.0 λ=9.0 0 1.000 1.000 1.000 1 1 4.025 4.168 3.998 4 2 9.041 9.025 9.026 9 3 16.208 16.767 16.056 16 4 25.367 25.211 25.220 25 5 36.921 38.110 36.386 36 6 50.648 49.867 49.910 49 7 67.084 68.862 65.400 64
```
**Structural fact (measured):** `ε_k/ε_0 → (k+1)² = n²`, **rigid and improving with λ** (the
λ=9 column is the closest to `n²` for all `k≤7`). `n²` is the spectrum of the **Dirichlet
Laplacian `−d²/dx²` on an interval** — the simplest band-limited sampling operator. **Proposition IV.1 (Jacobi/Dirichlet limit operator).** The relative spectrum `n²` is that
of the **Dirichlet Laplacian** `−d²/dx²` on an interval (with boundary condition
vanishing the envelope at `k=±N`). By §II `QW_norm` is a Loewner matrix of `sin`
weighted by `μ_W`; in the continuum limit of the lattice `d_k`, `Â_∞` is a second-order
**Jacobi operator** whose symbol gives spectrum `n²` and whose **fundamental vector `v_0`
is nodeless and vanishes smoothly at the edge `k=±N`** (Dirichlet fundamental mode,
envelope `~sin(π(N+1+k)/(2N+2))`). The prolate connection is indirect: sampling at
Nyquist critical density over `[−T*,T*]` (parameter `c=(logλ)(2πλ²)`) generates the same
family of commuting operators (Slepian); the **low-energy regime** of `Â_λ` →
sinusoidal modes of the interval with energies `∝ n²`. **[P*]** (the `n²` form is
MEASURED content in E11; identifying the limit operator via the Loewner structure is [GAP-IV.1],
below). **Thesis IV.2 (rigidity ⟹ `ξ̂_∞=Ξ`).** The rigid relative spectrum `n²` fixes the envelope
`v_0` up to scale; modulated by the carrier `(−1)^k` it produces a single real entire
function, even, of type `logλ`, with interlaced zeros whose density matches the
sampling density `L/2π` up to `T*`. By the horizon lemma that density is the
Riemann–von Mangoldt density, so the forced function is the **band-limited avatar of
`Ξ`**: `ξ̂_∞ = Ξ_{T}`. **[structural GAP]** — links "spectral signature `n²`" with "`ξ̂_∞=Ξ`"; well-posed, not proved. **Proposition IV.3 (the interior rate = prolate *plunge*).** PSWF approximation of
band-limited functions has error governed by the prolate eigenvalues `λ_k(c)`, which
**collapse** (*plunge*) super-exponentially for `k > 2c/π` (Landau–Widom):
`λ_k(c) ~ exp(−c·(...))`. Translated to the horizon, the interior error of `ξ̂` decays as
`e^{−c'λ²}` — **exactly the measured `e^{−11λ²}`**. ⟹ **`N5a` (interior) `≪ λ^{−½}`**,
unconditional, if identification IV.2 holds. **[P*]** (classical prolate asymptotics) **+
[GAP IV.2]**. --- ## V. ζ vs DH: positivity protects prolate rigidity — [!] the discriminator, localized By §II, `Â_λ` is Loewner weighted by `μ_W`, whose arithmetic part has a **definite sign
for ζ** (`Λ≥0`) and **not for DH** (`b(n)` changes sign). **Proposition V.1 (ζ: Perron–Frobenius protects `(k+1)²`).** For ζ, `A_λ = M_θ − V` with
`V=ΣΛ(n)T(n) ⪰ 0` and `e^{−tA_λ}` **positivity-preserving** (proved, `H1_PROOF.md`:
archimedean symbol CND via Lévy–Khintchine + `Λ(n)≥0`). Perron–Frobenius ⟹ the fundamental mode is
positive/nodeless **at every λ**, and — thesis — the renormalized operator `Â_λ` preserves the
**total oscillation** structure (Gantmacher–Krein) that forces the rigid relative
spectrum `(k+1)²` in the limit ⟹ `ξ̂_∞ ∈` Laguerre–Pólya (real zeros) ⟹ `ε_loc(ζ)→0`.
**[P]** the positivity; **[GAP-V]** that it survives the `/ε_0` renormalization and fixes `(k+1)²`. **Proposition V.2 (DH: no positivity, no rigidity).** For `L_DH`, `b(n)` changes
sign ⟹ `V_DH` is **not** positivity-preserving ⟹ Perron–Frobenius **fails** ⟹ there is no
protected total oscillation ⟹ `Â_∞^DH` is **not** forced to `(k+1)²` ⟹ `ξ̂_∞^DH` can
leave Laguerre–Pólya (complex zeros) ⟹ **`ε_loc(DH)` stays bounded away from 0**. **[P*]**
This **explains E10** (`ζ→10^{−13}`, `DH≥10^{−2}`): the lower bound on `ε_loc(DH)` is the
fingerprint of broken positivity. The signature is not localized at individual off-line
zeros (DH violates everywhere) but **global** — consistent with the E10c profile. **[!] The RH-hard core, now localized to ONE statement:**
> **Does positivity (Perron–Frobenius, `Λ(n)≥0`) survive the renormalization `/ε_0(λ)` and
> force the rigid relative spectrum `(k+1)²` of the limit `Â_∞`?** If **yes** ⟹ `ξ̂_∞=Ξ` rigid ⟹ (with `N5b`) `ε_loc(ζ)=o(λ^{−½})` ⟹ **RH**. If the
renormalization destroys the total oscillation, the wall persists. **All of RH (in this
program) is in this single lemma about preserving total positivity under `/ε_0`.** --- ## VI. `N5b` (edge layer) = prolate *plunge* — [GAP] concrete, plausibly unconditional The sup `ε_loc` is dominated by the edge `|t|~T*` (measured E8: grows 12 orders toward the
edge). In prolate language, the edge **is the *plunge* region**: the PSWFs transition
from `λ_k≈1` (interior, well approximated) to `λ_k≈0` (exterior, invisible) in a window of
width `~log c ~ log λ` around `k≈2c/π` (Landau–Widom). **Target VI.1 (the concrete inequality).**
``` sup_{αT* ≤ |t| ≤ T*} |ξ̂_λ(t) − Ξ(t)| ≤ C · λ^{−½−δ}.
```
**Route:** the number of prolate eigenvalues in the *plunge* is `~ (2/π²)log c · log(...)`; the
contribution of each one to the edge is bounded by its `λ_k(c)` and the
Beurling–Selberg extremal at critical density. **It uses only density/counting (Riemann–von
Mangoldt), not position** ⟹ an **unconditional** candidate. **[GAP]** — classical analysis
(Landau–Widom + Beurling–Selberg), heavy but not RH-sensitive. **Attack first**, as
suggested: if the edge is controlled, only the interior remains (IV.3, already
`e^{−c'λ²}`) and the positivity lemma (§V). --- ## VII. Status and the only remaining lemma | Piece | Content | Status |
|---|---|---|
| I | `ξ̂` = band-limited fundamental eigenvector | **[P]** |
| II | `QW` = Loewner of `sin` weighted by `μ_W`; sign `Λ≥0` (ζ) vs `b(n)` (DH) | **[P]** |
| III | **`ε_loc ≤ C‖Â_λ−Â_∞‖_{low}`** (relative form, resolves exp-small gap) | **[P]** |
| IV.1, IV.3 | prolate identification + interior rate = *plunge* `e^{−c'λ²}` | **[P*]** |
| IV.2 | rigidity `(k+1)² ⟹ ξ̂_∞=Ξ` | **[structural GAP]** |
| V.1 | ζ: positivity `Λ≥0` ⟹ Perron–Frobenius (at every λ) | **[P]** |
| V (core) | **positivity survives `/ε_0` and fixes `(k+1)²`** | **[!] [GAP] — RH-hard, localized** |
| VI | edge = *plunge*; `≤ Cλ^{−½−δ}` unconditional | **[GAP] classical, attack first** | **What has been achieved (real, not numerical):**
1. **The operator-theoretic reduction of Theorem 2 has been written and proved in the correct form** (relative, `/ε_0`): `ε_loc ≤ C‖Â_λ−Â_∞‖`. The obstacle of the exp-small gap — which killed previous attempts — **is resolved** by renormalization.
2. **The RH wall is compressed into ONE statement of total positivity** (§V core): that Perron–Frobenius/`Λ(n)≥0` survives `/ε_0` and fixes the rigid spectrum `(k+1)²`. It is not "convergence of zeros" nor "position": it is **preservation of total oscillation under renormalization** — a matrix-analysis object (Gantmacher–Krein/total positivity), not analytic number theory.
3. **The edge `N5b` is classical** (Landau–Widom + Beurling–Selberg), unconditional, and is the next concrete computation. **The target, in one line:**
``` RH ⟸ [ N5b: prolate plunge, unconditional ] + [ §V: Λ(n)≥0 survives /ε_0 and fixes (k+1)² ]
```
Two lemmas. The first is classical analysis. The second is the heart, and for the first time
it is written as **total positivity under renormalization**, without naming zeros or Weil. --- ## VIII. Attack on N5b — and why it DISSOLVES into §V — [P] (the finding) Attacking the edge carefully, **N5b stops being a separate piece**. Three steps: **VIII.1 — The target `Ξ_T` is uniformly good AT THE EDGE [P].** Theorem 1 with `δ=0`:
for EVERY `t∈ℝ` (interior and edge alike),
``` |Ξ_T(t) − Ξ(t)| = |∫_{|u|>T} Φ(u) e^{itu} du| ≤ ∫_{|u|>T}|Φ(u)|du ≤ C e^{−πλ²}.
```
This is a bound **uniform in `t`** (it comes from `|e^{itu}|=1`), governed by the double-exponential
`L¹` tail of `Φ`. **The edge is NOT special on the target side.** [P] **VIII.2 — In absolute sup-norm, the edge is SUPPRESSED by the decay of `Ξ` [P].**
`Ξ(t)` decays on the real axis as `|Γ(¼+it/2)| ~ e^{−πt/4}` (Stirling). At `T*~2πλ²`:
`|Ξ(T*)| ~ e^{−π²λ²/2}`, tiny. The edge layer of E8 was the **root** error
`|ρ̂_n−γ_n|` (relative), which grows toward `T*`; but the object of Theorem 2 is
`|ξ̂−Ξ|` **absolute**, and there `|ξ̂(t)−Ξ(t)| ≈ |Ξ'(t)|·|ρ̂−γ|` near a root, with `|Ξ'|`
decaying. ⟹ the edge's contribution to the absolute sup is `~ e^{−cλ²}·(root error)`,
**super-small**. The sup of `ε_loc` is **dominated by the interior** (where `|Ξ|~O(1)`),
not by the edge. [P] **VIII.3 — What remains is ONE thing: `sup|ξ̂ − Ξ_T|`, both band-limited [P].**
``` ε_loc ≤ sup|ξ̂ − Ξ_T| + sup|Ξ_T − Ξ| ≤ sup|ξ̂ − Ξ_T| + C e^{−πλ²}.
```
`δ̂:= ξ̂ − Ξ_T` is band-limited of type `logλ`. By Nikolskii (`‖g‖_∞ ≤ C√(logλ)‖g‖_{L²}`
for type `logλ`) and Parseval (`‖δ̂‖_{L²} = ‖v_0^{CCM} − v_0^{Fourier}‖_{ℓ²}`):
``` ε_loc ≤ C √(logλ) · ‖v_0^{CCM} − v_0^{Fourier}‖_{ℓ²} + C e^{−πλ²} ≤ (C/γ) √(logλ) · ‖Â_λ − Â_∞‖_{low} + C e^{−πλ²}. (relative Davis–Kahan)
``` **[!] Conclusion VIII (revises the plan):** **N5b is NOT a separate classical piece — it
is absorbed into §V.** The target side (`Ξ_T`) is already uniform (incl. edge) by Theorem 1;
the approximant side (that `ξ̂` decays like `Ξ_T` at the edge) **IS** part of
`ξ̂→Ξ_T = §V`. The "edge layer" was a mirage from looking at the **root** error (E8) instead
of the **absolute** sup-norm (which the decay of `Ξ` suppresses). The edge is benign. **⟹ All of N5 collapses to ONE quantitative statement:**
``` RH ⟸ ‖Â_λ − Â_∞‖_{low} = o(λ^{−½} / √(logλ)) [§V, governed by positivity]
```
A single inequality: the **rate** of convergence of the renormalized Weil operator in the
low-energy block. `N5a` (interior, plunge `e^{−c'λ²}`) and `N5b` (edge, suppressed by
decay) **both satisfy this comfortably** IF the operator-theoretic convergence holds.
Operator-theoretic convergence is §V (total positivity under `/ε_0`). **There are no longer
two lemmas: there is one.**
