# Repair of the three 🟠 points: Normalization, N5c-DH, IV.2≡§V (conflation) Pure mathematical resolution. The third (IV.2) uncovered a deeper finding: **H1 over-claims
"QW PSD"**, and the `/ε_0` renormalization has Weil positivity (RH) baked in. --- ## 1. Normalization — cleanly RESOLVED **The loose end:** `ξ̂_λ` is an eigenvector, defined up to scale; `ε_loc=sup|ξ̂_λ−Ξ|` is not well
defined without fixing the scale. **Resolution:** the conclusion of the chain is **Hurwitz**, which is **invariant under a
nonzero constant**: if `c_λ ξ̂_λ → Ξ` uniformly with `c_λ≠0` and `ξ̂_λ` real-rooted, then `Ξ` is
real-rooted (the roots of `c_λ ξ̂_λ` = those of `ξ̂_λ` = real). Therefore the normalization
is **free** and is fixed canonically:
``` ξ̂_λ(0):= Ξ(0) (match of value at the center; both even, central value ≠0).
```
Concretely `ξ̂_λ(0)=ξ_0·L/2` (residue `k=0`), nonzero (even fundamental); `ξ` is rescaled
to match `Ξ(0)`. With this:
- `ε_loc=sup|ξ̂_λ−Ξ|` becomes **well defined**.
- `Γ=sup|ξ̂_λ| = O(1)` (not `O(logλ)`): `ξ̂_λ≈Ξ`, `sup|Ξ|=O(1)` by the gamma decay. **Improves N2.**
- The RH conclusion is **independent** of the choice (Hurwitz-invariant). **[RESOLVED]** Loose end closed for N2, III, Thm 2. (In III the `L²` normalization can
also be used; both are valid and Hurwitz-invariant.) --- ## 2. N5c-DH — RESOLVED to named inputs (and along the way corrects the source of real-rootedness) **The loose end:** the bound `sup|ξ̂_f−Ξ_f| ≥ |Ξ_f(x₀)|>0` uses (i) `ξ̂_f` real-rooted and (ii)
convergence on the real axis `ξ̂_f(x₀)→Ξ_f(x₀)`, assumed. **Resolution of (i) — and finding:** `ξ̂_DH` **IS** real-rooted, and this **does NOT come from
`Λ(n)≥0`/PF** (DH has `b(n)` with sign changes, PF fails) but from the **self-adjoint spectral
realization of CCM** (the secular roots of the fundamental eigenvector of a
self-adjoint operator). Empirically confirmed (E9b: real DH roots 78,…,85.73,…).
**This corrects the source of E1:** real-rootedness holds for ζ **and** DH ⟹ it cannot
depend on the sign of the coefficients ⟹ its mechanism is Hermite–Biehler/self-adjoint, not
Perron–Frobenius. (Consistent with the E1 repair: the counterexample showed that
positivity does not give it, and here we see it is not even necessary — DH has it without
positivity.) **Resolution of (ii):** the convergence on the real axis `ξ̂_f(x₀)→Ξ_f(x₀)` at a fixed
interior point `x₀` (well below the horizon for large `λ`) **is** the analogue for `f`
of the E2.a + horizon scaffolding (proved for ζ, same construction mechanism). It is not
free, but **it is not a new gap**: it is the already-proved scaffolding, instantiated at `f`. **[RESOLVED to named dependencies]:** N5c-DH is **solid modulo** (i) real-rootedness of
CCM [self-adjoint, true for DH] + (ii) axis-convergence [= E2.a/horizon scaffolding].
The monotonicity `|g(x+iy)|≥|g(x)|` is correct. It is not a deep gap; it inherits E1 (real-root) and
E2.a (axis). Drops from 🟠 to "solid modulo scaffolding". --- ## 3. IV.2≡§V — there is NO conflation, BUT it uncovers that H1 over-claims and `/ε_0` assumes Weil≥0 **The loose end (2 parts):** (1) "dim=N(T*) pins down `g∝Ξ_T`" heuristic; (2) conflation: is the
CCM operator `A_λ` the raw Weil form? **Resolution of (2) — there is NO conflation:** by Weil's explicit formula,
``` QW = (archimedean) − (arithmetic) = Σ_ρ g(γ_ρ) conj(g(conj γ_ρ)) [zero side].
```
The entries `QW[m,n]=∫q_{mn}w_arch − Σ Λ(n)/√n q_{mn}` **are** the Weil form. ⟹ the
CCM ground state `ξ̂_λ` **IS** the Weil minimizer. **They are not distinct operators.** The
variational argument is over the correct object. **[conflation RULED OUT]** **Resolution of (1) — refined, not exact:** the minimizer `g_0` is the bottom eigenvector of
the frame operator `S=Σ_ρ K_{γ_ρ}⊗K_{γ_ρ}|_{PW_Ω}`. It is NOT exactly `Ξ_T` at finite `λ`;
it is `g_0 = Ξ_T + O(deficit)`, and `g_0 → Ξ_T` as `λ→∞` (the deficit
`ε_0 ~ C_0/λ² → 0`). The count `dim≈N(T*)` (critical density, Landau–Beurling) makes the
low-dimensional near-null space contain `Ξ_T`. **Rigorizable** (frame-deficit
analysis), but "exactly `Ξ_T`" is **false at finite λ** — it is a limit. **DEEPER FINDING (the important part):** since `QW = Weil form`,
``` QW PSD (all ε_k≥0) ⟺ Weil-positivity at bandwidth log λ ⟺ RH up to height T*.
```
Consequences:
- **H1 OVER-CLAIMS.** The memo says "H1 proves QW PSD unconditionally via PF". **False.** Perron–Frobenius gives a **simple bottom + positive eigenvector** (structure of the ground state), **NOT** `ε_0≥0` (PSD). The sign of `ε_0` IS Weil-positivity ⟺ RH-up-to-T*. PF ≠ PSD. If H1 proved unconditional PSD, it would prove RH — impossible. **Correction to H1: PF gives structure, not positivity.**
- **The `/ε_0` (III) renormalization assumes `ε_0>0` = Weil-positivity-up-to-T*** (≈RH-up-to-T*). That is, the "trick" that dissolves the exp-small gap **has RH baked in** via `ε_0>0`. (Patchable using `/|ε_0|`, but the structure of the bottom is RH-dependent.) ⟹ III is conditional **also** on `ε_0>0`, in addition to (H-gap)+(H-lim).
- This **confirms and deepens** that IV.2≡§V is the RH core: not only is the limit `ξ̂_∞=Ξ` RH-equivalent; the **renormalization itself** that supports III carries Weil-positivity. **[RESOLVED]:** conflation ruled out (QW=Weil form, same object); heuristic refined to
`g_0=Ξ_T+O(deficit)→Ξ_T` (limit, Landau–Beurling); and it was **uncovered** that H1 over-claims PSD
and that `/ε_0` assumes `ε_0>0`=Weil. The narrative does not collapse (there is no logical
conflation crack), but **Weil positivity shows up in more places than the picture admitted** (H1, III). --- ## Summary of the three | point | resolution |
|---|---|
| **Normalization** | **RESOLVED**: `ξ̂_λ(0)=Ξ(0)`, Hurwitz-invariant; `Γ=O(1)` |
| **N5c-DH** | **RESOLVED to inputs**: real-rootedness (self-adjoint CCM, not PF) + axis-conv (E2.a scaffolding) |
| **IV.2 conflation** | **ruled out** (QW=Weil form); heuristic→limit; **finding: H1 over-claims PSD, `/ε_0` assumes Weil≥0** | **The most valuable part:** (a) the **feared conflation does NOT exist** — `ξ̂_λ` IS indeed the
Weil minimizer, the narrative is coherent. (b) But the audit uncovered that **H1 over-claims**
("PSD" is RH, not PF) and that **the `/ε_0` renormalization assumes Weil-positivity** — the RH-hardness
is more distributed than the picture showed. (c) And the **source of
real-rootedness** was corrected: it is self-adjoint/HB (holds for DH without `Λ≥0`),
**not** Perron–Frobenius — which aligns with the E1 repair.
