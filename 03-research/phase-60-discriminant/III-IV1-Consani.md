# III and IV.1 by pure mathematics — ruling C. > Referee: **Caterina**. CCM Program, `phase-60-discriminant`.
> Rule: cold. A forced theorem is worse than an admitted gap. **RH is not proved.**
> Input (not re-derived): QW real symmetric Weil form `(2N+1)²`; `ε₀=λ_min(QW)`,
> `sign(ε₀)=RH-up-to-T*`, `T*=2πλ²`. Horizon lemma (mine, B.2):
> `N(T*)=2λ²logλ−λ²+O(logλ)`, `DOF(PW_Ω)=4λ²logλ`, zero density/Nyquist `=1−1/(2logλ)<1`,
> deficit `m≈2λ²`. `S_λ` = zero frame, `λ_min(S_λ)=0`, kernel of dimension `≈2λ²`.
> `L=2logλ`, `Ω=logλ`, `d_k=2πk/L`. --- ## 0. The separation that governs everything (anti-conflation C.2) Before any asymptotics, I fix the distinction that the panel flagged as C.2 and which is the
source of every possible self-deception in III/IV.1: ``` S_λ = Σ_{|γ_ρ|≤T*} K_{γ_ρ} ⊗ K_{γ_ρ} (ZERO FRAME, reproducing kernel of PW_Ω) QW = full Weil form = S_λ-part + archimedean w_arch + pole 𝒫
``` - `λ_min(S_λ) = 0` **unconditionally**, because `S_λ` is a sum of rank-1 PSD terms with nontrivial kernel (underspanning, B.2). This is **trivial and RH-neutral**.
- `ε₀ = λ_min(QW)`. Its **size** `|ε₀|` is analysis. Its **sign** is RH-up-to-T*. **The trap.** The pre-audit master document wrote "deficit `ε₀~C₀/λ²`" as if the
sub-critical count of `S_λ` controlled `ε₀`. **This is false at the root:** the count controls the
geometry of `S_λ` (kernel dimension, frame gap), not the smallest eigenvalue of `QW`, which
receives the contribution of `w_arch` and `𝒫` — and that contribution is exactly what carries the
sign. Everything that follows respects this separation to the letter. What the count DOES
control is proved below (Lemma III.1); what it does NOT control I declare RH-hard, with reason (§III.4). --- ## III. What the sub-critical count says — and what it does not ### III.1 — The count controls the frame geometry, not the sign of ε₀ **Lemma III.1 (lower frame gap, unconditional). [SOLID]**
Let `S_λ` be the frame operator of the zeros on `PW_Ω` restricted to `[−T*,T*]`, and let
`P_λ` be the projection onto the orthogonal complement of `ker S_λ` (the effective range, `dim ≈ 4λ²logλ`).
Then on `ran P_λ`,
``` B_- ‖g‖² ≤ ⟨g, S_λ g⟩ ≤ B_+ ‖g‖², 0 < B_-, B_+ < ∞,
```
with Plancherel–Pólya bounds: `B_+ ≤ C logλ` (local zero density `≈ (logλ)/2π`,
Nikolskii on `PW_Ω`), and `B_- > 0` by uniform separation of the `γ_ρ` (Riemann–von
Mangoldt gaps `≥ c/logT > 0` for `|γ|≤T*`). *Proof.* On `ran P_λ` the system `{K_{γ_ρ}}_{|γ_ρ|≤T*}` is a Riesz frame for its span,
by the Plancherel–Pólya inequality for `PW_Ω`: for nodes `{γ_ρ}` with separation
`δ_ρ ≥ c/logT`, `Σ_ρ |g(γ_ρ)|² ≍ ‖g‖²` with constants depending only on `δ` and `Ω`. The
upper bound `B_+ = O(logλ)` is Nikolskii (the same constant as `‖ξ̂‖²_{L²}=πlogλ` from N2). The
lower bound `B_->0` is the lower half of Plancherel–Pólya, finite because the separation is
uniform. ∎ **Reading.** The sub-criticality `1−1/(2logλ)<1` does NOT degrade `B_-` to 0 on `ran P_λ`: the
underspanning lives **entirely** in `ker S_λ` (the `≈2λ²` missing directions), and `ran P_λ`
is left with a genuine Riesz frame. This is as much as the count alone gives, and it is
pure analysis. **It does not touch `ε₀`.** ### III.2 — Why underspanning does NOT force ε₀→0 (refutation of a tempting shortcut) It would be tempting to argue: "since `ker S_λ` has dim `≈2λ²` and `Ξ_T` almost-lives there
(`Ξ_T(γ_ρ)=O(e^{−πλ²})`), the smallest eigenvalue of QW collapses with `λ`." **This is a
non-sequitur**, and I prove it: **Obs III.2.** `λ_min(QW) = ε₀` is NOT bounded by `λ_min(S_λ)=0`. For a form
`QW = S_λ + W` with `W = w_arch + 𝒫` symmetric, Weyl gives only
``` λ_min(S_λ) + λ_min(W) ≤ ε₀ ≤ λ_min(S_λ) + λ_max(W), ⟹ λ_min(W) ≤ ε₀ ≤ λ_max(W).
```
The term `S_λ` **falls outside** the bound (its `λ_min=0` imposes nothing on `ε₀` except via
`W`). That is: **the smallest eigenvalue of QW is fixed by the archimedean+pole part `W`
restricted to the kernel and range of `S_λ`, not by the degeneracy of the frame.** The count gives
the geometry of `S_λ`; the sign and size of `ε₀` are given by the projected `W` — and that is exactly the
Weil positivity. ∎ **Conclusion III.2.** *Underspanning does NOT force `ε₀→0`.* What underspanning forces is
that `ε₀` is decided on a subspace of codimension `≈2λ²` (where `S_λ` is non-degenerate) PLUS the
action of `W` on `ker S_λ`. The rate of `ε₀` is left undetermined by the count. **This
disables, with proof, the heuristic `ε₀~C/λ²` as a consequence of the count.** ### III.3 — Unconditional SIZE bound for |ε₀| (what analysis does give) What I can prove unconditionally is an **upper bound** on `|ε₀|` by the Rayleigh method
with a test vector — without touching the sign. **Lemma III.3 (unconditional upper bound on |ε₀|). [SOLID]**
``` |ε₀| = |λ_min(QW)| ≤ min_{‖g‖=1, g∈PW_Ω} |⟨g,QW g⟩| (if the form changes sign)
```
and in particular, taking as test the near-kernel element `g₀ = Ξ_T/‖Ξ_T‖`,
``` ⟨g₀, S_λ g₀⟩ = Σ_ρ |Ξ_T(γ_ρ)|² / ‖Ξ_T‖² = O(λ² e^{−2πλ²}/‖Ξ_T‖²) (super-small), ⟹ |ε₀| ≤ ⟨g₀, QW g₀⟩ = ⟨g₀, W g₀⟩ + O(e^{−2πλ²}).
```
*Proof.* Courant–Fischer min-max: `ε₀ ≤ ⟨g,QW g⟩` for any unit `g`; with `g₀` the
`S_λ` term is exponentially small by the quasi-vanishing property of `Ξ_T` at the
zeros. What remains, `⟨g₀,W g₀⟩`, is **a determined, analytic number** (archimedean
integral + pole residue evaluated at `Ξ_T`). ∎ **Candidly about the rate.** `⟨g₀,W g₀⟩` is the **Weil explicit formula evaluated at `Ξ_T`**:
it is the archimedean term `∫ Ξ_T · (Γ′/Γ)(¼+it/2)…` minus the pole term, normalized by
`‖Ξ_T‖² ≍ logλ` (Plancherel–Pólya). Its order of magnitude is `O(1)` on the absolute scale and
`O(1/logλ)` after normalizing by `‖Ξ_T‖²`. **But its SIGN is exactly the Weil positivity
at `Ξ_T` = local RH.** Hence: ``` ┌─────────────────────────────────────────────────────────────────────┐ │ |ε₀| ≲ |W(Ξ_T)|/‖Ξ_T‖² = O(1/logλ) — SIZE, analysis (upper bound) │ │ sign(ε₀) = sign of the Weil form at its minimizer — local RH │ └─────────────────────────────────────────────────────────────────────┘
``` **Critical clarification against the master document.** This bound is `O(1/logλ)`, **not** `C/λ²`. The
pre-audit claim `ε₀~C₀/λ²` **does not hold up** via this unconditional route: it confused
the frame gap (geometric, `O(λ²)` directions) with the eigenvalue of QW. What the Rayleigh method
candidly delivers is `O(1/logλ)` (via `‖Ξ_T‖²≍logλ`), and **only as an upper bound on the absolute
value**. I cannot derive the exact power of `λ` without the edge-operator asymptotics (IV.1),
which is open. I declare `ε₀ ~ C/λ²` **NOT PROVED** by counting means. ### III.4 — The sign of ε₀ is RH, and the count cannot reach it (with proven reason) **Prop III.4.** The sub-critical count is **invariant under reflecting a zero off the
axis**. *Proof:* moving `γ_ρ → x_ρ ± iη_ρ` does not change `N(T*)` (the count counts zeros with
`|γ|≤T*` by their real part / modulus, Riemann–von Mangoldt is stable under small perturbations of
the ordinates) nor `DOF(PW_Ω)` (which depends only on `Ω` and `T*`). Hence the density
`=1−1/(2logλ)` holds in **both** regimes (RH-true and RH-false). ∎ **Corollary (the wall).** Since the count does not distinguish RH-true from RH-false, **no
purely counting/density argument can fix the sign of `ε₀`.** The sign enters through the
**indefiniteness** of the form: under RH, `A_λ(g,g)=Σ_ρ|g(γ_ρ)|²≥0` (sum of squares, `ε₀≥0`);
without RH, the terms `g(γ_ρ)conj(g(conj γ_ρ))` with `γ_ρ∉ℝ` are **cross terms**, the form is
indefinite, `ε₀<0` possible. That is structure of the quadratic form, not of the count. **C.2/C.1
confirmed: the sign is RH-hard.** ### III.5 — Consequence for the gap γ(λ) (separating finite from uniform) **Lemma III.5.** At each finite `λ`, `γ(λ)=ε₁/ε₀−1>0` (B.3, H1 simplicity). The sub-critical
count does **not** give `liminf_λ γ(λ)>0`, and I prove it: *Proof of the obstruction.* `ε₁/ε₀` is a ratio of two eigenvalues of QW; both inherit their
scale from `W` projected onto subspaces of `ran P_λ ⊕ ker S_λ`. The count fixes the
**dimension** of those subspaces (`≈2λ²` of kernel), but not the **relative gap** between the
two lowest eigenvalues, which is a datum of the edge operator after `/ε₀` (IV.1). Since the
count is RH-invariant (III.4) and `γ` is not necessarily so (it depends on `W`), **the count
cannot deliver the uniformity**. ∎ **Verdict III.** Proved unconditionally by the count: (a) Lemma III.1, Riesz frame
on `ran P_λ` with `B_->0`; (b) Obs III.2, underspanning **does not** force `ε₀→0`; (c) Lemma
III.3, size upper bound `|ε₀|=O(1/logλ)`; (d) Prop III.4, the count is RH-neutral, hence
the **sign of `ε₀` remains RH-hard**; (e) Lemma III.5, `γ(λ)>0` finite but **uniformity
open**. The claim `ε₀~C/λ²` is **withdrawn** as underived. (H-pos) remains
RH-up-to-T*. --- ## IV.1 — The limit operator upon rescaling by density ### IV.1.0 The factor 1−1/(2logλ) and the horizon rescaling The density factor `ρ(λ)=1−1/(2logλ)` measures how much the zeros undersample the band. The
question is: is there a natural limit operator upon rescaling the horizon by `ρ`? **Lemma IV.1.1 (natural horizon scale). [SOLID, analysis]**
Define the rescaled horizon coordinate `τ = t/T*`, `τ∈[−1,1]`, and the local zero
density in that coordinate,
``` n_λ(τ) dτ = #{γ_ρ ∈ [T*τ, T*(τ+dτ)]}.
```
By Riemann–von Mangoldt, `n_λ(τ) = (T*/2π)·log(T*τ/2π)·(1+o(1)) = λ²·(logλ + log|τ|+…)`.
Normalizing by the Nyquist density `ν = T*·Ω/π = λ²·2logλ` (DOF per unit `τ`):
``` n_λ(τ)/ν = ½ · [1 + (log|τ|)/(2logλ)] → ½ uniformly on compacts of (0,1].
```
*Proof.* Direct ratio of the two asymptotics; the `log|τ|` term gets divided by `2logλ→∞`. ∎ **Reading.** Rescaling by density **collapses the factor `1−1/(2logλ)` to the constant
`½`** in the bulk: the zero density tends to half of Nyquist in horizon scale. The
defect `1/(2logλ)` is a **uniform subprincipal-order** effect, not localized — it lives
distributed over the whole band, not at an edge. **This is informative, and it is what the count gives.** ### IV.1.2 — Why the count ALONE does not determine the limit operator (proof) Now the severe point. The rescaling gives a **limit sampling measure** (density `½` of
Nyquist), but **not** an operator. I prove it: **Prop IV.1.2 (non-determination). [SOLID]** Two operators with the same asymptotic eigenvalue
count can have different limit operators after `/ε₀`. *Proof by exhibition:* the
measured relative spectrum is `ε_k/ε₀ → (k+1)² = n²` with alternating parity `(−1)^k`. The Weyl
count of a 2nd-order Sturm–Liouville operator on `[0,1]` with boundary conditions gives
`N(E) ~ (√E)/π · (length)`, i.e. `E_k ~ c k²` — **compatible with `n²`**. But the **same**
count `E_k~ck²` is shared by:
- the Dirichlet Laplacian `−d²/dx²` (constant),
- any `−d²/dx² + V(x)` with `V∈L¹` (same Weyl leading order, `V` only shifts subprincipal terms),
- and Loewner/compact integral operators with a kernel tuned to the same count. The count `n²` only fixes the **principal symbol** (2nd order, one spatial dimension), **not** the
potential `V` nor the variable coefficient. ∎ **Corollary IV.1.2.** The relative spectrum `n²` is **necessary but not sufficient** to
identify `Â_∞`. The count determines:
- the **order** of the limit operator: 2 (from `E_k ~ k²`),
- the **dimension**: 1 (from the one-dimensional Weyl law),
- the parity `(−1)^k`: the signature of a self-adjoint 2nd-order operator with simple spectrum on an interval (eigenfunctions with `k` nodes), and it does **not determine**: the potential `V(x)`, the variable coefficients, the exact
boundary conditions (`ω*≈0.966π` is a boundary datum **not** captured by the count). This is C.4 of
the panel, now with proof: **the compactness of the crude Loewner kernel + the non-uniqueness of Weyl
obstruct deriving the operator from the count.** ### IV.1.3 — What IS fixed: the class of the limit operator **Theorem IV.1.3 (partial unconditional classification). [SOLID]** If the scaling
limit `Â_∞ = lim_λ A_λ/ε₀` exists in strong resolvent sense (H-lim, open), then it is a
self-adjoint operator on `L²(0,1)` (or `(0,ω*/π)`) with:
1. compact resolvent (discrete spectrum `ε_k/ε₀→n²`),
2. 2nd-order principal symbol (Weyl's law `n²` ⟹ it cannot be of order ≠2 nor dim ≠1),
3. a simple ground state of... sign **NOT determined**: the boundary carrier `ω*≈0.966π≠π` forbids a definite sign (this is exactly the E1 obstruction, see M1). *Proof.* (1)+(2) by the inverse one-dimensional Weyl law (Birman–Schwinger / Weyl: the growth
order of the eigenvalues fixes the order and dimension of the limit differential operator,
uniquely among differential operators). (3) by the measured boundary carrier. ∎ **What is missing to close IV.1 (stated plainly).** Pinning down `V(x)` and the exact boundary conditions requires the
fine asymptotics of the edge operator: **Landau–Widom** (eigenvalue asymptotics of Toeplitz/Wiener–Hopf-type
truncated operators — the correct regime for sub-critical band-limited frames)
or **de Branges** theory of the `H(E)` space associated to `ξ̂`. This is
**hard analysis but NOT RH-hard**: the limit operator `Â_∞` is an unconditional spectral
question. Identifying it does NOT close RH; it would only close (H-gap-uniform) and (H-lim). The
RH wall remains in IV.2 (`ξ̂_∞=Ξ`), untouched by IV.1. ### IV.1.4 — Landau–Widom connection (the correct route, sketched) The sub-critical regime `density = 1−1/(2logλ) < 1` is **exactly** the Landau–Widom regime
for concentration operators (prolate/Wiener–Hopf) **below** the critical threshold. In that regime
the number of eigenvalues "close to 1" of the concentration operator
`P_Ω 1_{[−T*,T*]} P_Ω` is `≈ (density)·DOF`, with a **transition layer of width
`O(log(T*Ω))`** around the threshold. My unconditional prediction:
``` #{concentration eigenvalues ∈ (δ,1−δ)} = O(log(T* Ω)) = O(logλ),
```
which matches in order the amplitude `Γ=O(logλ)` from N2 (not a coincidence: both measure
the Landau–Widom transition layer). The edge operator `Â_∞` is the **rescaled limit of
that transition layer**, and its spectrum `n²` is the spectrum of the layer's generator
(2nd order, by Slepian's theory of the prolate bulk-edge). **This gives a concrete, falsifiable
candidate identification, not a phenomenological one — but its verification is the open
IV.1 residual.** --- ## Final verdict (III + IV.1) **Proved unconditionally (pure analysis):**
- **III.1** Riesz frame on `ran P_λ`, `0<B_-≤B_+=O(logλ)` (Plancherel–Pólya/Nikolskii).
- **III.2** underspanning does **NOT** force `ε₀→0` (Weyl: `S_λ` falls outside the bound on `ε₀`).
- **III.3** **size** upper bound `|ε₀| = O(1/logλ)` via Rayleigh with test `Ξ_T` (not `C/λ²` — withdrawn as underived).
- **III.4** the count is **RH-neutral** (invariant under reflecting zeros) ⟹ the sign of `ε₀` is out of its reach.
- **III.5** `γ(λ)>0` finite (B.3); uniformity `liminf γ>0` **open** (not given by the count).
- **IV.1.1** rescaling by density collapses `1−1/(2logλ)→½` (half-Nyquist density).
- **IV.1.2** the count `n²` fixes order=2, dim=1, parity `(−1)^k`, and does **NOT** fix the potential/boundary conditions (Weyl non-uniqueness + Loewner compactness = C.4 with proof).
- **IV.1.3** partial classification of `Â_∞` (self-adjoint, compact resolvent, 2nd order).
- **IV.1.4** Landau–Widom route as a falsifiable candidate identification (open residual). **RH-hard (with proven reason, not moved an inch):**
- **sign(ε₀)** = Weil positivity up to T* (III.4): the count is RH-invariant.
- **(H-pos)** and **H1′** remain RH-up-to-T*.
- **IV.2 (`ξ̂_∞=Ξ`)** untouched: IV.1 would only identify the *form* of `Â_∞`, not that its ground state is `Ξ_T` (that is the frame deficit, RH-hard, C.1). **Final sentence (C.).** The sub-critical count is an instrument of **geometry** (kernel
dimension, frame gap, sampling density, boundary operator order) and delivers all of that
cleanly. But it is **structurally blind to the sign**: invariant under reflecting a zero,
it cannot see RH. The temptation to read `ε₀~C/λ²` from the count was a **conflation of
`S_λ` vs `QW`** (C.2) and is refuted: what is candid is `|ε₀|=O(1/logλ)` as a size bound, with
the sign RH-hard. IV.1 is hard analysis (Landau–Widom) that would close the uniform gap but **does not
touch the wall**. The core does not move. — C.
