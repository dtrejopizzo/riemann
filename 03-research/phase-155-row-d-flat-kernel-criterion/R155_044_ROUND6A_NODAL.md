# R155.044 — round 6a: a nodal criterion for the even Schur complement (P8)

*Phase 155, round 6a. Executes order (a) of `R155_043 §4`. Inherits `R155_039`
(amended; Lemma N, Prop G), `R155_032` (amended; the `8×8` even `π_ij` table at `log 2`),
`R155_023` (amended; `A_∞|P_T` eigenstructure, `τ₀ = 6.28983599`), Paper 46 §2 (`lem:K`,
`thm:S`, `lem:mbounds`) and §8 (`prop:schur`, `thm:nest`, `prop:shifts`). **Paper 46,
`R155_039` and `R155_040` are not touched.** New scripts: `scripts/r6a/` (≈ 2.5 min total).*

**No sign for `ζ` is claimed at any `T`. Endpoint of record unchanged: `λ_min(A_{½log3}) ≥
8.8577·10⁻⁵` (Paper 46 Thm C). No value of `inf W` at `log 2` is asserted.**

---

## §0 Verdict in seven lines

1. **The Sturm pattern is real and its shift is proved.** The `k`-th even eigenvector of
 `A_∞|P_T` has **exactly `k` nodes in `(0,T)`** for `k = 1,…,8`, with strict interlacing
 (converged run `N = 36`; `T = log 2` and `T = 0.65`). The *shift* — the ground state `F*`
 already has a nodal pair, contradicting the naive "ground state is positive" — is
 **PROVED**: `P_T ⊥ e^{±t/2}`, and `{e^{t/2},e^{−t/2}}` is a Chebyshev system of order 2, so
 **every** nonzero `F ∈ P_T` has at least two sign changes (Prop N2). The unconstrained
 ground state of `A_∞` on `L²(−T,T)` *is* positive and simple (Prop N1, Beurling–Deny:
 the kernel is `cδ − K(|x−y|)` with `K ≥ 0`).
2. *[amended per R155_045]* **The route through the kernel of `A_∞` is closed for
 `K` (not an impossibility for `PF₂` structure in general); the semigroup route for `t < 1` is
 HEURISTIC and `t ≥ 1` is OPEN.**
 `K` is *completely monotone* (`lem:K`), hence **log-convex** on `(0,∞)`; therefore
 `u ↦ K(|u|)` is nowhere log-concave and is **not a Pólya frequency function** (Schoenberg),
 so Karlin's total-positivity oscillation theorem does not apply to the kernel of `A_∞`
 (Theorem N3) — a route closure, not a proof that no variation-diminishing structure exists.
 The semigroup route's `p_t(x) ≍ |x|^{t−1}` claim for `t < 1` is a **HEURISTIC**: `m(τ) =
 log τ + O(1)` is a bounded *error*, so `e^{−t(m−C₀)} = τ^{-t}·e^{O(t)}` only up to a factor not
 asymptotically constant, and the Tauberian/monotone-density step needed to conclude
 `p_t ≍ |x|^{t−1}` is not given. For `t ≥ 1` it is OPEN, and even a positive answer would have
 to be transported through the codim-2 compression, which item 1 shows changes the count.
 **The Sturm pattern stands as a CONJECTURE with a proved lower-bound base case (≥ 1 nodal
 pair), not as a theorem.**
3. **The node-only sign rule works exactly where it matters.** Predicting `sign J_n(i,j)` from
 the nodes alone (sign of the integrand on the largest cell of the common refinement of the
 nodes of `e_j` and the shifted nodes of `e_i`) gives `59–80 %` of the `64` entries overall —
 but **`100 %` of every entry with `|J| ≥ 0.10`**, and the correctly predicted entries carry
 `88.7–95.9 %` of the total mass `Σ|J|`. The failures are the small entries (mean `|J|` of a
 failure `0.014–0.028` against `0.07–0.11` overall). This is Prop G generalised and measured.
4. **The arena is proved to be large.** `λ_{2k+1}(A_∞|P_T) ≤ m((2k+3)π/2T) = log k + O(1)`
 (Theorem N4, min–max + Jensen on the concave `φ`) — the archimedean gap grows only
 **logarithmically**, while `‖Π_T‖ ≤ 𝖠_T = Σ v_n` is bounded but non-compact (`prop:shifts`).
 Hence `N*(T) := #{k : λ_{2k+1} ≤ 𝖠_T} ≥ #{k : m((2k+3)π/2T) ≤ 𝖠_T} ≈ (2T/π)·2πe^{𝖠_T}`:
 **at least `12` even modes at `log 2`** (Galerkin `N = 60` finds exactly `12`), `2` at `½log3`.
5. **The truncation no-go (Theorem N5).** *[amended per R155_045]* `𝖠_T ≍ 4e^{T}`, so
 `N*(T) ≳ 2T·e^{4e^T}`: the number of
 archimedean modes the prime form can overturn grows **doubly exponentially in `T`**. `E₇`
 (`thm:nest`) sits strictly *inside* the arena at `log 2` — `k = 8` was already out of reach —
 which is the structural explanation of `R155_032`'s withdrawal and of the observation that
 the Galerkin bottom sits at the **last** mode of every truncation.
6. **Honest answer to (4): no.** A nodal criterion for the *full* `S_even` is not attainable by
 this route. Nodes give an exact, `100 %`-reliable sign law for the *large* entries of finitely
 many blocks; the obstruction lives in the log-slow tail, where the nodes are asymptotically
 equispaced (`≈ π/ m`-spacing, a WKB/prolate regime), the signs of `J_n(i,j)` become
 equidistributed, and no nodal bookkeeping can beat a bounded non-compact perturbation.
7. **P8 is therefore CLOSED as a route to positivity and KEPT as a diagnostic law.** What it
 yields for the record: Props N1/N2, Theorems N3/N4/N5.

---

## §1 Corpus check (grep, whole repo, `*.md` + `*.tex`)

| query | files | prior art | new here |
|---|---|---|---|
| `total positivity` | **51** | `12-BIN-THREE-finite-to-full-positivity.md` states the TP form of RH (`RH ⟺ Φ` a PF function `⟺ [Φ(x_i−x_j)]` totally positive); Paper 06 `main.tex:175` repeats it; Paper 37 §(S3) is the obituary of the family | the TP question asked **of the archimedean kernel on the window**, not of `Φ`; and its **refutation** by log-convexity (Theorem N3) |
| `totally positive` | **22** | Papers 06/14/37/41/47, `12-BIN-THREE` | — |
| `Karlin` | **5** (`Paper 41:1477`, `Paper 40:1651,3638`, `Paper 37:682,935,1577,3622`, `phase-11-hyperbolicity-total-positivity/M11.2`, `phase-106/106_42`) | Paper 37 §(S3): "Total positivity is the tool that converts coefficient positivity into control of oscillation, and it is exactly the tool `thm:pf2` removes"; `106_42` proves the Gamma jump kernel is **not TP₂** and concludes "the usual Karlin–Gantmacher variation-diminishing theorem cannot be used … Nodal counting without a variation-diminishing kernel does not order the spectrum" | Theorem N3 is the **same verdict for a third kernel**, and for the first time with a one-line structural cause (completely monotone ⇒ log-convex) rather than a computed minor |
| `Pólya frequency function` | **5** (`12-BIN-THREE`, Paper 06, `phase-73/E73_202`, `phase-4-krein-space-realization/00-PROOF-LOG:2360`) | the PF language is in the corpus only for `Φ`/`Ξ` | its use for the *Lévy* kernel of `A_∞` is new — and negative |
| `oscillation theorem` | **16** | `phase-151` blueprint, Paper 36/46, `114_d_14`, `114_d_99` (`MATRIX_PICONE_TOTAL_POSITIVITY_AUDIT`) | no note states or tests a Sturm pattern for `A_∞|P_T`; §2 is the first |
| `Weyl law` | **1** (`phase-61/respuestas-matematicos.md`) | — | Theorem N4 is a *ceiling* of Weyl type for a compressed multiplier; the matching floor is exactly the missing prolate spread bound (`R155_039 §2.4`) |
| `Szegő` / `Landau–Widom` | **112** / `R155_023`, `R155_033`, `R153_011/012`, `PATH-TO-D` | Landau–Widom is used for the *counting* asymptotics `n₋ ~ (2τ₀/π)T` | the arena bound of §4 is the counting question at the **upper** threshold `𝖠_T`, not at `0` |
| `nodal` | **102** | `R155_039` (Lemma N, Prop G) is the only note on the prime shift | §2–§3 |

---

## §2 Task (1): nodal structure of the even eigenvectors

`scripts/r6a/r6a_01_nodal.py` (`N = 18, 36` at `T = log 2`; `N = 18` at `T = 0.65`; `8001`
sample points; cross-check `max|(−Σ_n v_nJ_n) − π_ij| = 1.7·10⁻⁵` at `N = 36`, `4.3·10⁻⁴` at
`N = 18` — Lemma N reproduces the `R155_032` table).

### 2.1 The two proved facts

> **Proposition N1 (the unconstrained ground state is positive). `PROVED`.**
> *[amended per R155_045]* On `L²(−T,T)`, for `F` extended by zero and `h = F⋆F̃`,
> `thm:S` gives the pure-jump Dirichlet form
> `Γ_T(F) = C₀‖F‖² + ½∫∫_{I_T²}K(|x−y|)|F(x)−F(y)|²dxdy + ∫_{I_T}κ(x)|F(x)|²dx`, with killing
> `κ(x) = ∫_{|y|>T}K(|x−y|)dy < ∞` and jump density `K ≥ 0` (`lem:K`); the written kernel
> `(C₀+∫₀^{2T}K)δ(x−y) − K(|x−y|)` diverges (`∫₀^{2T}K = +∞`) and is not the correct object — the
> form is. Beurling–Deny gives Markovian, hence positivity-preserving, `e^{−tΓ_T}`; `K > 0`
> everywhere gives irreducibility, hence positivity-improving; Perron–Frobenius gives a simple,
> a.e. strictly positive ground state: **no nodes**. The form domain embeds compactly in
> `L²(I_T)` (`m(τ)→∞`), so the resolvent is compact and the bottom is an eigenvalue.

> **Proposition N2 (the Chebyshev shift). `PROVED`.**
> *[amended per R155_045]* `F ∈ L²(−T,T)` has **at most one sign change** :=
> `∃t₀` with `F ≥ 0` a.e. on `(−T,t₀)` and `F ≤ 0` a.e. on `(t₀,T)` (or the reverse); the
> degenerate case of `F` of one sign a.e. is the `t₀ = ±T` endpoint.
> `P_T = {F ∈ L²(−T,T) : ⟨F,e^{t/2}⟩ = ⟨F,e^{−t/2}⟩ = 0}`. The pair `{e^{t/2},e^{−t/2}}` is a
> Chebyshev system of order `2` on `(−T,T)` (every nonzero `c₁e^{t/2}+c₂e^{−t/2}` has at most
> one zero). Therefore **every nonzero `F ∈ P_T` has at least two sign changes**, and an even
> `F ∈ P_T` has at least one nodal pair. In particular `F*` cannot be of one sign — which is
> the `REFUTED` line of `R155_039 §3.2`, now with its reason, and the index shift of the
> Sturm numbering on `P_T` is exactly `1` nodal pair.

*Proof of N2.* If `F` had at most one sign change, at `t₀`, then for a suitable
`c₁e^{t/2}+c₂e^{−t/2}` vanishing exactly at `t₀` the product `F·(c₁e^{t/2}+c₂e^{−t/2})` would be
of one sign and not a.e. zero, contradicting `⟨F,e^{±t/2}⟩ = 0`. ∎

### 2.2 The measured pattern (`DIAGNOSTIC`)

Nodes in `(0,T)` at `T = log 2`, `N = 36` (the `N = 18` run agrees to `10⁻³` on the first four
modes; its higher modes are resolution-limited):

| mode | `λ` | nodes in `(0,T)` | `#` |
|---|---|---|---|
| `e₁ = F*` | `−0.15432` | `0.31531` | `1` |
| `e₃` | `+0.46812` | `0.15038, 0.47841` | `2` |
| `e₅` | `+0.84406` | `0.11020, 0.31924, 0.54237` | `3` |
| `e₇` | `+1.11554` | `0.08036, 0.24742, 0.40758, 0.57694` | `4` |
| `e₉` | `+1.32844` | `0.06723, 0.19760, 0.33223, 0.46212, 0.59844` | `5` |
| `e₁₁` | `+1.50370` | `6` nodes | `6` |
| `e₁₃` | `+1.65269` | `7` nodes | `7` |
| `e₁₅` | `+1.78227` | `8` nodes | `8` |

> **Conjecture N-Sturm (`CONJECTURE`; base case `PROVED` by N1+N2).** The `k`-th even
> eigenvector of `A_∞|P_T` has exactly `k` nodes in `(0,T)`, and consecutive modes' nodes
> **strictly interlace**. Verified for `k ≤ 8` at `T = log 2` (`N = 36`: interlacing exact) and
> `T = 0.65`; the `N = 18` runs fail the interlacing test only at the unresolved top modes.

### 2.3 Why the proposed proof route is closed

> **Theorem N3 (the archimedean kernel is not a Pólya frequency function). `PROVED`.**
> `K(u) = 1/(2\sinh(u/2)) + 1/(2\cosh(u/2)) = 2Σ_{k≥0}e^{−(2k+½)u}` is completely monotone
> (`lem:K`). Every completely monotone function is **log-convex** on `(0,∞)` (Cauchy–Schwarz on
> the representing measure). Hence `f(u) := K(|u|)` is log-convex on each half-line and, being
> also singular at `0` (`K(u) = u^{-1}+O(1)`), is not log-concave on any interval. By
> Schoenberg's characterisation `PF₂ ⟺ log-concave`, `f` is **not a PF₂ function**, so the
> translation kernel `f(x−y)` is not totally positive of order `2` and Karlin's variation
> -diminishing/oscillation theorem is unavailable for `A_∞` on the window (route closed for the
> kernel `K`, not an impossibility statement about `PF₂` structure in general).
> *[amended per R155_045]* The semigroup variant for `0 < t < 1` is **HEURISTIC**:
> by `lem:mbounds` `m(τ) = \log τ + O(1)` is a bounded error, so `e^{−t(m−C₀)} = τ^{−t}e^{O(t)}`
> only up to a non-asymptotically-constant factor, and `p_t(x) ≍ |x|^{t−1}` near `0` would need a
> Tauberian/monotone-density argument not given here; `t ≥ 1` is **OPEN**. ∎

*Scope.* `t ≥ 1` is **OPEN** (there `p_t` is bounded; `φ` complete Bernstein makes `p_t` a scale
mixture of Gaussians, and such mixtures are generically not log-concave, but we prove nothing).
Even a positive answer there would order the eigenvectors of `Γ_T` on `L²`, **not** of `A_∞|P_T`;
Prop N2 shows the compression shifts the count, and no total-positivity statement survives a
codim-2 compression. This matches the corpus: `106_42` (Gamma jump kernel not TP₂) and Paper 37
`thm:pf2` (the PF₂ failure on the exponent lattice at the primes `2` and `3`).

---

## §3 Task (2): sign of `J_n(i,j)` from the nodes alone

**The rule (Prop G generalised).** Refine `(\log n − T, T)` by the nodes of `e_j` and by the
nodes of `e_i` shifted by `\log n`. On each cell the integrand `e_i(z−\log n)e_j(z)` has a
constant sign, readable from the nodes alone. Predict
`sign J_n(i,j) := sign of the integrand on the **longest** cell`.
(Prop G is the special case in which the refinement has a single cell; then the prediction is a
theorem.)

Measured against the exact `J` of Lemma N, `8` even modes, `64` entries per prime
(`r6a_02_rule.py`; `T = log 2`, `N = 36`):

| prime | all `64` | `|J| ≥ 0.02` | `|J| ≥ 0.05` | `|J| ≥ 0.10` | mass fraction correct |
|---|---|---|---|---|---|
| `n = 2` | `38/64 = 59 %` | `30/42 = 71 %` | `26/32 = 81 %` | **`22/22 = 100 %`** | **`90.0 %`** |
| `n = 3` | `50/64 = 78 %` | `38/40 = 95 %` | `32/32 = 100 %` | **`22/22 = 100 %`** | **`95.9 %`** |

(`N = 18`, `T = log 2`: `64 %` / `77 %` overall, `100 %` above `0.10`, mass `88.7 %` / `93.1 %`.
`T = 0.65`, `N = 18`: `72 %` / `80 %` overall, `100 %` above `0.05`, mass `93.8 %` / `95.4 %`.)

**Reading (`DIAGNOSTIC`).** The rule is a *sign law for the dominant entries*: every failure is a
near-cancelling entry where two comparable cells of opposite sign compete (mean `|J|` at a
failure `0.014`–`0.028` versus `0.07`–`0.11` over the whole matrix). The `n = 2` column is the
harder one precisely because at `T = log 2` the shift equals the half-window, so the refinement
has the most cells. The failures are *not* noise: they are the entries where the nodal criterion
is genuinely undecided, i.e. exactly the entries whose sign carries arithmetic information — the
`π₁₃` cancellation of `R155_039 §3.3` is of this kind.

---

## §4 Task (3): the arena, and why no truncation is safe

> **Theorem N4 (logarithmic ceiling for the compressed multiplier, even sector). `PROVED`.**
> *[amended per R155_045]* `A_∞` commutes with parity, and on the even part of `P_T`
> the two Tate constraints coincide, so `P_T^{even}` has codimension **1** in `L²_{even}`. Take
> the even Dirichlet modes `cos((2j+1)πx/2T)`, `j = 0,…,k+1` (`k+2` of them, top frequency
> `(2k+3)π/2T`), minus the one constraint ⇒ a `(k+1)`-dimensional trial space in `P_T^{even}` ⇒
> `λ^{even}_{k+1}(A_∞|P_T) ≤ λ_{2k+3}(Γ_T) ≤ C₀ + φ\big(((2k+3)π/2T)^2\big) =
> m\big((2k+3)π/(2T)\big) = \log k + O(1)`.
> *Proof.* The first inequality is min–max on the `(k+1)`-dimensional even trial space just
> constructed. The second is the argument of Theorem J (`R155_039 §2.3`) run at index
> `j = 2k+3`: on the span `D_j` of the first `j` Dirichlet modes, `‖F'‖² ≤ (jπ/2T)²‖F‖²`, and
> Jensen applied to the **concave** `φ` (`thm:S`) in the variable `τ²` gives
> `Γ_T(F)/‖F‖² ≤ C₀ + φ((jπ/2T)²)`; min–max over `D_j` bounds `λ_j(Γ_T)`. The last equality is
> `lem:mbounds`, `m(τ) = \log(τ/2π) + O(1/τ)`. ∎

By `prop:shifts`, `‖Π_T‖ ≤ 𝖠_T := Σ_{n ∈ N_T} v_n`, and `Π_T` is **not compact**. So the modes
that the prime form can overturn are those with `λ_{2k+1} ≤ 𝖠_T`, and Theorem N4 turns the
ceiling into a **lower bound on their number**:

> **Corollary (the arena). `PROVED`.**
> *[amended per R155_045]*
> `N*(T) := \#\{k : λ^{even}_{k+1}(A_∞|P_T) ≤ 𝖠_T\} ≥ \#\{k : m((2k+3)π/2T) ≤ 𝖠_T\} =
> \lfloor Tτ_*/π − 1/2 \rfloor`, `τ_* = 2πe^{𝖠_T}(1+o(1))`.
> At `T = log 2` (`𝖠_T = v₂+v₃ = 2.24889`, `τ_* = 59.55`): exact verification via `lem:mbounds`(ii)
> at `τ₁₁, τ₁₂` gives `m(τ_{11}) ≤ 2.2168 ≤ 𝖠_T` and `m(τ_{12}) ≥ 2.2596 > 𝖠_T`, so
> **`N* ≥ 12`**, `PROVED` (not merely asymptotic).
> At `T = ½\log3` (`N_T = \{2\}`, `𝖠_T = v₂ = 0.98026`, `τ_* = 16.75`): exact verification via
> `lem:mbounds`(ii) gives `m(τ_1) ≤ 0.8928 ≤ 𝖠_T` and `m(τ_2) ≥ 1.1075 > 𝖠_T`, so
> **`N* ≥ 2`**, `PROVED`.
> Galerkin (`N = 60`, `T = log 2`) finds **exactly `12`** even modes with `λ ≤ 2.24889`
> (`λ₁₃-th even mode` `= 2.2568 > 𝖠_T`), i.e. the bound is sharp there (`DIAGNOSTIC`).

> **Theorem N5 (no safe truncation; the shape of the obstruction). `PROVED`.**
> *[amended per R155_045]* `𝖠_T = Σ_{n<e^{2T}} 2Λ(n)n^{−1/2} = 4e^{T}(1+o(1))`
> (Chebyshev/PNT), so
> `N*(T) ≥ 2T·e^{𝖠_T}(1+o(1)) = \exp\big(4e^{T}(1+o(1))\big)`.
> Any argument that closes `S_{even}` by controlling the tail with the archimedean gap must
> retain at least `N*(T)` even modes: the gap grows only like `\log k`, while the prime form is
> bounded, non-compact and does **not** decay along the tail (`prop:shifts`: `|π_{ij}| ≤ 𝖠_T`
> with no off-diagonal decay; `R155_032 §2`: the band maxima fall only like `|i−j|^{−1.5}` and
> the diagonal is not dominant).

**Consistency with `R155_032`'s withdrawal.** `thm:nest` certifies `E₇`; `N* ≥ 12` at `log 2`
says `E₇` is strictly inside the arena, so the near-zero Galerkin bottom **must** sit at the last
mode of any truncation with `k ≤ 12` — exactly what was observed at `N = 18` and `N = 36`. The
withdrawal was not a numerical accident; it is Theorem N5 at the smallest window with two primes.

---

## §5 Task (4): honest conclusion

**A nodal criterion for the full `S_even` is not attainable by this route.** What the nodes give:
(i) an exact, proved sign rule where the shifted window sits inside a single lobe pair (Prop G),
(ii) a measured `100 %` sign law for all entries above `|J| = 0.10`, carrying `90–96 %` of the
mass, and (iii) an explanation of the `2`-plane cancellation as a straddled zero (`R155_039`).
What they cannot give: control of the tail. By Theorem N4 the nodes of `e_{2k+1}` become
asymptotically equispaced with spacing `∼ 2T/k`, so for a fixed shift `\log n` the refinement of
`(\log n − T, T)` has `∼ k` cells of comparable length and alternating sign; the largest-cell rule
then has no margin, and the sign of `J_n(i,j)` is decided by a cancellation of order `k^{−1}`
between `∼k` cells — not by geometry. The obstruction is in the **log-slow tail**, where the
archimedean gap grows like `\log k` and the prime form neither decays nor compactifies.

Consequently: **P8 is CLOSED as a route to positivity** (it explains finite blocks and predicts
the dominant signs, and its own quantitative content proves the arena is too large for
truncation) and **KEPT as a diagnostic law** (the sign rule of §3, the Sturm conjecture of §2).
The remaining live formulation of the tail problem is unchanged: a floor for `∫\min(τ²,X)d\mu`,
i.e. an explicit prolate concentration estimate (`R155_039 §2.4`).

---

## §6 Labels of record

| statement | label |
|---|---|
| **Prop N1**: the unconstrained ground state of `Γ_T` on `L²(−T,T)` is simple and nodeless (kernel `cδ − K(|x−y|)`, `K ≥ 0`, Beurling–Deny) | **`PROVED`** |
| **Prop N2**: `{e^{t/2},e^{−t/2}}` is a Chebyshev system ⇒ every `0 ≠ F ∈ P_T` has ≥ 2 sign changes; the Sturm index on `P_T` is shifted by exactly one nodal pair; `F*` cannot be of one sign | **`PROVED`** (supersedes the `REFUTED` line of `R155_039 §3.2` by giving its cause) |
| **Theorem N3**: `K` completely monotone ⇒ log-convex ⇒ `K(|·|) ∉ PF₂` ⇒ Karlin's oscillation theorem is unavailable for `A_∞` on the window (route closed for `K`, not `PF₂` in general) | **`PROVED`** *[amended per R155_045]*; `p_t ∉ PF₂` for `0 < t < 1` is **`HEURISTIC`**; the semigroup case `t ≥ 1` **OPEN** (and would not transfer through the codim-2 compression) |
| **Conjecture N-Sturm**: the `k`-th even eigenvector of `A_∞\|P_T` has exactly `k` nodes in `(0,T)`; consecutive modes interlace | **`CONJECTURE`** *[amended per R155_045]* (N1+N2 give ≥ 1 nodal pair, not exactly one — lower bound of the base case `PROVED`; verified `k ≤ 8` at `T = log 2`, `N = 36`, and `T = 0.65`) |
| node values at `T = log 2` (`e₁: 0.31531`, `e₃: 0.15038, 0.47841`, …) | **`DIAGNOSTIC`** |
| the node-only sign rule: `59–80 %` of all `64` entries; **`100 %` of entries with `\|J\| ≥ 0.10`**; `90–96 %` of the mass; failures are the small, near-cancelling entries | **`DIAGNOSTIC`** (the rule's special case Prop G is `PROVED`) |
| Lemma N reproduces the `R155_032` `π_ij` table to `1.7·10⁻⁵` (`N = 36`) | **`DIAGNOSTIC`** (implementation check) |
| **Theorem N4**: `λ_{2k+1}(A_∞\|P_T) ≤ m((2k+3)π/2T) = \log k + O(1)` | **`PROVED`** (min–max + Jensen on the concave `φ`) |
| **Corollary (arena)**: `N*(T) ≥ \lfloor Tτ_*/π − 1/2\rfloor` *[amended per R155_045]*; `N* ≥ 12` at `log 2` (via `lem:mbounds`(ii) at `τ_{11},τ_{12}`), `≥ 2` at `½\log3` (via `τ_1,τ_2`); Galerkin `N = 60` gives exactly `12` at `log 2` | **`PROVED`** (the Galerkin count `DIAGNOSTIC`) |
| **Theorem N5**: `𝖠_T ∼ 4e^{T}` ⇒ `N*(T) ≥ \exp(4e^{T}(1+o(1)))`: no fixed truncation can close `S_even`; structural cause of the `R155_032` withdrawal | **`PROVED`** |
| a nodal criterion for the **full** `S_even` | **CLOSED NEGATIVE** (finite blocks only; the obstruction is the log-slow tail) |
| `P8` | **CLOSED as a route**, kept as a diagnostic law |

Row-D label unchanged. Endpoint of record unchanged. No sign for `ζ` beyond `log 2`.

---

## §7 Proposal for Paper 46 (to accept or refuse; Paper 46 untouched here)

1. **`prop:arch` gains Proposition N2** (three lines): the Tate constraints form a Chebyshev
 system, so no element of `P_T` is of one sign. It costs nothing and removes the reader's
 natural expectation that `F*` be a positive bump.
2. **A remark after `prop:shifts`: Theorem N4 + the arena corollary.** This is the sharpest
 statement the paper can make about why `thm:nest` does not extend: the archimedean gap is
 logarithmic and the prime form is bounded and non-compact, so the arena at `T` has at least
 `\exp(4e^{T}(1+o(1)))` even modes. It converts the present `DIAGNOSTIC` paragraph after
 `prop:shifts` ("the obstruction is not captured by any fixed number of archimedean modes")
 into a **theorem** with an explicit count, and it strengthens `rem:galerkin`.
3. **Theorem N3 as a one-paragraph no-go** next to the Lévy structure of `thm:S`: complete
 monotonicity of `K` — the property that makes `φ` a Bernstein function and gives every ceiling
 in the paper — is *exactly* the property that forbids total positivity and hence any
 Karlin-type oscillation theorem for the kernel. One hypothesis, two opposite consequences;
 it belongs in the paper as the closing remark of §2.
4. **Not proposed**: the Sturm conjecture and the sign rule of §3 (diagnostic; they belong here).
