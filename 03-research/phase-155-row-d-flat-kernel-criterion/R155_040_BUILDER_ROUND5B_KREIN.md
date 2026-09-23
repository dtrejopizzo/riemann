# R155_040 — Builder, round 5b: the Kreĭn extension problem for the ζ window datum (P5) — 2026-09-22

Inputs: Paper 47 §7 (`def:W`, `thm:Z`, `thm:Zexh`, `cor:RH`, `lem:fdict`, `thm:finZ`, `rem:loc`,
`cor:infinite`, `prop:finuniv`, the unnumbered *Remark (Kreĭn extension)* after `rem:RHcert`),
`R155_014` §2.2 Remark 2.5 (amended), `R155_031` §3(iv) and §4 P5, `R155_038` §3 (iii).
Corpus grep for `Krein|Kreĭn|indeterminate|determinate|extension problem|screw|de Branges|Suzuki`:
`R155_031` §3(iv) and `R155_014` Rem. 2.5 are the only places where the *extension problem for the
window datum* appears; everything else (`00-MAP`, phases 21–26, `NO-GO-LIST` OK-6, papers 31–34) is
the unrelated Kreĭn **space** / Pontryagin index κ arc, and the de Branges hits are the canonical-system
arc, closed as a route (`05-meta-and-planning/09`, `07`). No prior file states or proves anything about
determinacy of the ζ window datum. Nothing in the corpus cites Suzuki for this.

## §0 Verdict

P5 is answered, and the answer **inverts the premise under which it was ranked**.

1. Indeterminacy of the Kreĭn extension problem for ζ at a window `T` is **not** a removable technical
   obstruction that is "necessary but not sufficient" and "likely routine" (`R155_031` §4 P5). It is
   **equivalent to the existence of a flat-top certificate at `T`**, up to the single boundary case
   `λ^W_T = 0`, and therefore, quantified over all windows, **equivalent to RH** (Thm 3). Proving it for
   ζ is exactly as hard as row D; it is not a lemma on the way to row D.
2. The finite-`Z` half is genuinely determinate, and more strongly than `thm:finZ` states: `μ_Z` is the
   **unique finite positive symmetric solution**, with no decay hypothesis on anything (Thm 4). This is a
   real strengthening of `thm:finZ`, obtained by re-reading its Steps 1–4 with the lattice step `a` as a
   free variable.
3. **Correction of record.** The task premise "Theorem C ⟹ indeterminate at `½log3` unconditionally" is
   **false as stated**, and so is the corresponding reading of Rem. 2.5. Theorem C's dual point has
   `β = (2.00256…, −0.00965…) ≠ (2,0)`, and `g_0, g_1` are supported **inside** the window
   (`main.tex` l. 294). Its certificate therefore solves the extension problem for the *perturbed* datum
   `g + (β₀−2)g₀ + β₁g₁`, not for `g`. The defect is not absorbable: `|β₀−2|·ĝ₀(0) = 0.00256·4\sinh T
   = 5.9·10⁻³ ≫ c = 8.86·10⁻⁵`. **[amended 2026-09-22 per R155_041]** This does *not* mean no
   unconditional indeterminacy at any window is established: Zhu 2026 Thm 1.2 certifies the **complete**
   form `W_T` on `supp ⊆ [−0.8, 0.8]` (`main.tex` l. 994–997, `CITED-NOT-VERIFIED`), so
   `λ^W_T ≥ λ^W_{0.8} ≥ 8.9·10⁻¹⁸ > 0` for every `T ≤ 0.8`, and by Thm 3(a) below `KEP(T)` is
   **unconditionally indeterminate for every `T ≤ 0.8`**, in particular at `T = ½log3 = 0.549`. What
   Theorem C alone does *not* give is that indeterminacy (its certificate solves the perturbed datum
   `g_β`, not `g`); the unconditional result comes from Zhu, not from Theorem C. Rem. 2.5's ζ sentence
   ("indeterminate at every scale") stays outside the `PROVED` column only for `T > 0.8` — there it is
   labelled RH-equivalent, not heuristic.

Net: P5 delivers three theorems and one correction, removes the "moderate difficulty / routine" ranking,
and produces no new access to the sign. Recommend closing P5 as a route.

## §1 Corpus (what was already there)

| source | content | status |
|---|---|---|
| `R155_014` Rem. 2.5 | finite `Z` = Carathéodory–Fejér/Kreĭn determinate case; "for ζ the extension problem is indeterminate at every scale, and the obstruction disappears" | first sentence `PROVED` (= §2 of that file); ζ sentence and the `dim ℋ(E_N)=2N` gloss `HEURISTIC` (amended per `R155_015`) |
| `R155_031` §3(iv), §4 P5 | the dichotomy is the right frame, never proved for ζ; "indeterminacy is necessary, not sufficient"; difficulty "moderate … likely routine" | **superseded by §3 below on both counts** |
| Paper 47, Remark (Kreĭn extension) | a certificate of value `λ^W_T` is a PD extension of `σ̌_T + 2g₀ − λ^W_T δ₀`; the distributional version of Kreĭn's theorem "not pursued"; would give a third proof of `thm:D1` | the present file pursues it for the *complete* datum `g` and finds the equivalence, not a third proof |
| Paper 47 open item (5) | "the distributional Kreĭn extension route to Theorem D1" | untouched; see §4(iii) |

Kreĭn's theorem itself (M. G. Kreĭn 1940; Akhiezer, *The Classical Moment Problem*, continuous analogue;
Sasvári, *Positive definite and definitizable functions*) is **cited nowhere in the proofs below** — every
statement of §3 is proved from Paper 47 and elementary Fourier analysis. That is deliberate: the classical
theorem is stated for *continuous* PD functions on an interval, and our datum is a distribution with atoms,
so the citation would be a gap. `CITED-NOT-VERIFIED` marks are therefore unnecessary.

## §2 Formulation

**The window datum.** For even `h ∈ C_c^∞(ℝ)` put
```
⟨g, h⟩ := C₀h(0) + ∫₀^∞ (h(0) − h(u)) K(u) du − Σ_{n≥2} v_n h(log n) + 2∫_ℝ h(u) cosh(u/2) du .     (2.1)
```
This is the right-hand side of the Weil explicit formula in the normalisation of Paper 47 (`thm:Z`(ii)),
read as a tempered distribution: `g` is the even distribution
```
g = [C₀ + ∫₀^∞K]·δ₀ − ½ Pf K(|u|) + 2cosh(u/2) − Σ_{n≥2} (v_n/2)(δ_{log n} + δ_{−log n}),          (2.2)
```
the first two terms being the Lévy-regularised pair whose Fourier transform is the archimedean multiplier
`m(τ) = C₀ + ∫₀^∞(1−cos τu)K(u)du ≥ 0` (Paper 47 `thm:A`, `eq:m`); the `2cosh(u/2)` term is not tempered
on ℝ but every pairing below is against a `w ∈ 𝒲_T` (exponential decay `> ½`), which is what
`def:W` is for. By `thm:Z`, for `w ∈ 𝒲_T^{reg}`,
```
⟨g, w cos(τ·)⟩ = f_w(τ) = Σ_ρ ŵ(τ − γ_ρ) ,          i.e.   (w·g)^ = f_w ,  and  "ĝ = μ_ζ".          (2.3)
```
`w ≡ 1` on `[−2T,2T]` is exactly the statement that `w·g` and `g` agree **on the window**.

**Definition 2.1 (KEP(T)).** For `T > 0` let
```
𝔈(T) := { ν : ν a positive symmetric tempered measure on ℝ with ⟨ν̂ − g, h⟩ = 0 for all even h ∈ C_c^∞(−2T,2T) } .
```
KEP(T) is *solvable* if `𝔈(T) ≠ ∅`, *determinate* if `#𝔈(T) = 1`, *indeterminate* if `#𝔈(T) ≥ 2`.

Symmetry is imposed for the same reason as in `prop:finuniv`(ii) (amended `R155_014` §1.3): even test
functions determine only the even part of a representing measure, so without it every problem is
trivially indeterminate. "PD on the window" is *defined* as solvability (Schwartz/Bochner: PD tempered
distributions are transforms of positive tempered measures); no extension theorem is assumed.

**Lemma 2.2 (one negative square in the polar term).** `PROVED.` The kernel `(s,t) ↦ 2cosh((s−t)/2)` has,
at any `n ≥ 2` distinct points, a Gram matrix `ab^T + ba^T` with `a_i = e^{t_i/2}`, `b_i = e^{−t_i/2}`,
whose eigenvalues are `(a·b) ± |a||b|` on `span{a,b}` and `0` elsewhere: signature `(1,1)`. So `2cosh(u/2)`
has **exactly one negative square** on every interval, and is PD on none.
*Consequence.* Solvability of KEP(T) is never automatic, at any window however small: the datum (2.2) is a
sum of a PD part (`m ≥ 0`), a κ=1 part (the pole), and a negative part (the prime atoms). This is the
Kreĭn-space index `κ` of phases 21–26 appearing here as the *polar* summand, and it is the structural
reason `β₀ → 2` in `rem:RHcert`.

## §3 Theorems

**Theorem 1 (certificate ⟹ indeterminate, with a continuum).** `PROVED.`
Let `T ≥ ½log2` and let `w ∈ 𝒲_T^{reg}` satisfy `f_w ≥ c` on ℝ.
(i) If `c ≥ 0`, then `ν_w := f_w(τ)dτ/2π ∈ 𝔈(T)`; in particular KEP(T) is solvable, by an **absolutely
continuous** solution.
(ii) If `c > 0`, then `𝔈(T)` contains a continuum of pairwise distinct absolutely continuous measures, so
KEP(T) is indeterminate.
(iii) If moreover RH holds, `μ_ζ ∈ 𝔈(T)` as well, and it is purely atomic, hence `≠ ν_w`.

*Proof.* (i) `w ∈ C_c^∞` even, so `w·g` is a tempered distribution and (2.3) gives `(w·g)^ = f_w`, a
continuous function with `f_w(τ) = log|τ| + O(1)` (`lem:mbounds`, `thm:Dtail`), hence tempered; Fourier
inversion gives `ν̂_w = w·g`, which equals `g` on `(−2T,2T)` because `w ≡ 1` there. `f_w ≥ 0` makes `ν_w`
positive, and it is symmetric because `w` and `g` are even.
(ii) Fix `χ ∈ C_c^∞(ℝ)` even, `χ ≥ 0`, `χ ≢ 0`, `supp χ ⊂ {|u| > 2T}`. For `ε ∈ ℝ`, `w_ε := w + εχ ∈
𝒲_T^{reg}`, and `f_{w_ε} = f_w + ε·r_χ` with
`r_χ(τ) = 2∫χ(u)cosh(u/2)cos τu du − Σ_n v_n χ(log n)cos(τ log n) − ∫_{|u|>2T} χ K cos τu du`,
a bounded continuous function (`χ` is compactly supported away from the singularity of `K`), say
`|r_χ| ≤ R`. For `|ε| < c/R` we get `f_{w_ε} > 0`, so `ν_{w_ε} ∈ 𝔈(T)`. These are pairwise distinct:
`ν_{w_ε} − ν_{w_{ε'}} = ((ε−ε')/2π) r_χ dτ`, and `r_χ = 0` would force `χ·g = 0`, whereas on
`supp χ ⊂ {|u| ≥ 2T} ⊂ {|u| ≥ log2 > 0.3}` the density of `g` is `D(u) = 2cosh(u/2) − ½K(u) > 0`
(positivity and monotonicity of `D` on `[0.3,∞)` are proved in `thm:Zexh`), so `χ·g ≠ 0`.
(iii) Under RH `μ_ζ` is a positive symmetric tempered measure and `μ̂_ζ = g` on all of ℝ by (2.3). ∎

**Theorem 2 (solvable ⟹ Weil positivity at that window).** `PROVED.`
If `𝔈(T) ≠ ∅` then `W_T(F) ≥ 0` for every `F ∈ C_c^∞(−T,T)`, i.e. `λ^W_T ≥ 0`.
*Proof.* Let `ν ∈ 𝔈(T)`, `F ∈ C_c^∞(−T,T)`, `h = F ⋆ F̃`. Then `h` is even, `supp h ⊂ (−2T,2T)`, and
`ĥ = |F̂|² ≥ 0`. By Definition 2.1 and the explicit formula in the form (2.1),
`W_T(F) = ⟨g, h⟩ = ∫ ĥ dν = ∫ |F̂|² dν ≥ 0`. ∎
(The first equality is `thm:A`/`eq:Aform` with the polar term, i.e. `main.tex` l. 604.)
**[amended 2026-09-22 per R155_041, M1]** This gives `W_T ≥ 0` on `C_c^∞(−T,T)`; the further step
`⟹ λ^W_T ≥ 0` (the infimum of `W_T` over the unit sphere of `L^2(I_T)`) additionally needs
`C_c^\infty(I_T)` to be a form core for `\mathfrak a_T` (`main.tex` l. 123 states the form domain but
not the core property); with that one line, `λ^W_T ≥ 0` follows by density.

**Theorem 3 (the dichotomy, and its RH-equivalence).** `PROVED` (given Paper 47 `cor:RH`, `thm:Zexh`).
(a) *Per window, `T ≥ ½log2`.* `λ^W_T > 0 ⟹ KEP(T) is indeterminate ⟹ λ^W_T ≥ 0.`
Hence certificates and indeterminacy coincide except on the boundary set `{T : λ^W_T = 0}`.
(b) *Global.* The following are equivalent: **(1)** RH; **(2)** KEP(T) is solvable for every `T > 0`;
**(3)** KEP(T) is indeterminate for every `T > 0`; **(4)** for every `T > 0`, `𝔈(T)` contains a continuum
of absolutely continuous measures.
(c) *Contrapositive form (the dichotomy).* For every `T > 0`: **either** KEP(T) is indeterminate, with
`μ_ζ` and a continuum of absolutely continuous elements in `𝔈(T)`, **or** RH is false. Equivalently:
if at a single window the problem is unsolvable, or solvable and determinate, then RH fails.
*Proof.* (a) forward: `λ^W_T > 0` and `thm:Zexh`(i) give `w ∈ 𝒲_T^{reg}` with `inf f_w > 0`; apply
Theorem 1(ii). Backward: Theorem 2. (b) (1)⟹(4): under RH `cor:RH`'s proof gives `λ^W_T > 0` for every
`T ≥ ½log2` (the Jensen/exponential-type argument), hence (4) at those `T` by (a); for `0 < T < ½log2`
note `𝒲_{T'} ⊂ 𝒲_T` for `T' > T`, so a certificate at `T' = ½log2` is one at `T`, and Theorem 1 applies.
(4)⟹(3)⟹(2) trivially. (2)⟹(1): by Theorem 2, `W_T ≥ 0` on `C_c^∞(−T,T)` for every `T`, i.e. Weil's
functional is nonnegative on all compactly supported test functions, which is Weil's criterion
(`cor:RH`, (c)⟹(a)). (c) restates (b) window by window using the (1)⟹(4) implication. ∎
**[amended 2026-09-22 per R155_041, E3]** For `0 < T < ½log2` the perturbing `χ` transported from
Theorem 1(ii) must be taken supported in `{|u| ≥ log2}`, where `D > 0` is established (`thm:Zexh`), not
merely in `{|u| ≥ 2T}`; the certificate at `T' = ½log2` restricts correctly but the perturbation
argument needs this sharper support to guarantee `χ·g ≠ 0`.

**Remark 3.1 (what Theorem 3 does to P5).** `R155_031` §4 P5 ranks the item as "moderate, likely routine"
and warns that indeterminacy is "necessary, not sufficient". Theorem 3(a) says the warning is too weak in
one direction and too strong in the other: indeterminacy is **not** merely necessary — it is sufficient for
`λ^W_T ≥ 0` and equivalent to a certificate off a boundary set — and it is therefore **not routine**: a
proof of indeterminacy at every window is a proof of RH. There is no free lunch in the Kreĭn frame.

**Theorem 4 (finite zero sets: determinacy, unconditionally and without decay).** `PROVED.`
Let `Z ⊂ ℝ\{0}` be a finite symmetric multiset, `|Z| = d ≥ 2`, `g_Z(u) = Σ_{γ∈Z} cos(γu)`, `T > 0`, and let
`ν` be a **finite** positive symmetric measure on ℝ with `ν̂ = g_Z` on `(−2T,2T)`. Then `ν = μ_Z`.
*Proof.* `ν` finite ⟹ `φ := ν̂` is continuous, bounded, real, even and positive definite. Fix `a` in the
interval `(0, 2T/d]` outside the discrete exceptional set of Step 1 of `thm:finZ`, so that the distinct
elements `w_1,…,w_r` of `Z` give pairwise distinct `z_j = e^{i w_j a}` and `φ(ka) = g_Z(ka)` for `|k| ≤ r`.
Steps 2–4 of `thm:finZ` use only: continuity and positive definiteness of `φ`, and its agreement with `g_Z`
at `0,a,…,ra`. They give `φ(ma) = g_Z(ma)` for every integer `m ≥ 0`. (Step 5, the only place where
`φ(u) → 0` is used, is not needed here.) Now let `m ≥ 1` be fixed and let `a` vary: the conclusion holds for
all `a` in `(0, 2T/d]` minus a discrete set, and both `φ` and `g_Z` are continuous, so `φ(ma) = g_Z(ma)`
for **all** `a ∈ (0, 2T/d]`. Taking the union over `m ≥ 1` of `m·(0,2T/d]` covers `(0,∞)`; with evenness,
`φ = g_Z` on ℝ, and `ν = μ_Z` by `prop:finuniv`(ii)/uniqueness of the spectral measure. ∎
*Relation to `thm:finZ`.* `thm:finZ` is the corollary: a flat-top certificate would give the finite positive
measure `ν_w = f_{w,Z}dτ/2π` (finite because `f_{w,Z} = (w g_Z)^ ∈ L¹` with `∫ = 2π φ(0) = 2πd`), hence
`ν_w = μ_Z`, hence `w g_Z = g_Z`, contradicting `w → 0` and `limsup|g_Z(ma)| ≥ 1`. Theorem 4 is strictly
stronger: it removes the decay hypothesis and the product form, and it is the **determinacy statement**
that Rem. 2.5 asserted without proof.

**Theorem 5 (the perturbed problem at `T = ½log3`).** `PROVED.` Let `β = (β₀,β₁)` be the multipliers of
`thm:C` and `g_β := g + (β₀−2)g₀ + β₁g₁`, with `g₀ = cosh(u/2)1_{|u|<2T}`, `g₁ = u sinh(u/2)1_{|u|<2T}`.
Then the extension problem for `g_β|(−2T,2T)` at `T = ½log3` is solvable and indeterminate,
unconditionally: `ν := (σ_T + ν̂ + β₀ĝ₀ + β₁ĝ₁)dτ/2π ≥ c dτ/2π > 0` by `thm:C`, and the perturbation
argument of Theorem 1(ii) applies verbatim (the atomic `ν` of `thm:C` lives outside the window).
**It says nothing about KEP(½log3)** via Theorem C, because `g₀, g₁` are supported inside the window and
`|β₀−2|·ĝ₀(0) = 5.9·10⁻³ ≫ c = 8.86·10⁻⁵`, so the defect cannot be absorbed into `c`.
**[amended 2026-09-22 per R155_041, E1]** `λ^W_{½log3} > 0` unconditionally is **not open**: it is
**KNOWN**, via Zhu 2026 Thm 1.2, which certifies `Q(f) ≥ 8.9·10⁻¹⁸‖f‖²` for `supp f ⊆ [−0.8,0.8]` **for
the complete form `Q = W_T`** (`main.tex` l. 994–997, `CITED-NOT-VERIFIED`). Since `λ^W_T` is
nonincreasing in `T` (`main.tex` l. 1781) and `½log3 = 0.5493 < 0.8`,
`λ^W_{½log3} ≥ λ^W_{0.8} ≥ 8.9·10⁻¹⁸ > 0`, so by Theorem 3(a) `KEP(T)` is **unconditionally
indeterminate for every `T ≤ 0.8`**, in particular at `T = ½log3`. This does not come from Theorem C
or `Paper42` (both bound only the **primitive/`A`** form, `λ^W_T ≤ λ^P_T ≤ λ^A_T`, `rem:Kprim`) — it
rests on Zhu alone. The genuinely open question is `λ^W_T > 0` unconditionally for `T > 0.8`.

## §4 What indeterminacy buys

(i) **Not a new target.** By Theorem 3(a) the extension frame is isomorphic to the certificate frame; the
Nevanlinna/resolvent-matrix parametrisation of `𝔈(T)` in the indeterminate case would be a description of
the set of certificates, available only once one member is known. The hoped-for "certificate as an
extension rather than an optimisation" (`R155_031` §4 P5, *Success*) is therefore circular as stated.
(ii) **A genuine widening, of measure zero.** `𝔈(T)` is strictly larger than the set of `ν_w`: solutions
need not be of product form `w·g`. But by Theorems 1–3 the two existence questions differ only at
`λ^W_T = 0`. So the widening buys nothing for existence, and could only matter for *constructions*.
(iii) **Extremal extensions — the one live route.** `CONJECTURE / HEURISTIC.` In the indeterminate case the
solution set has extremal elements (Kreĭn–von Neumann and Friedrichs, i.e. the ends of the Nevanlinna
parameter). Conjecture: `μ_ζ` is the extremal *singular* solution and the a.c. solutions of Theorem 1 are
interior, with `c = inf f_w` a coordinate on the parameter; the "certificate at infinity" of `rem:RHcert`
(`f_w → 2π μ_ζ` as `w ↑ 1`) is precisely the statement that the certificates approach that extreme point.
If made exact this would identify `λ^W_T` with a Nevanlinna-parameter boundary value. No part of this is
proved here, and by Theorem 3 any proof of it is RH-hard.
(iv) **Lemma 2.2 is reusable.** The polar term carries exactly one negative square at every window; this is
the extension-problem shadow of the phase-21–26 index κ and of the two primitivity multipliers.
**[amended 2026-09-22 per R155_041, E2]** Lemma 2.2 explains the rank/one-negative-square structure of
the polar term, not the coefficient `β₀ = 2` itself: uniqueness of `β₀ = 2` is already `PROVED` in
`prop:P` (`main.tex` l. 604 ff., via `\Rel(A\bar B)` taking both signs), and comes from the polar term
`2\Rel(A\bar B)`, not from Lemma 2.2. What remains heuristic in `rem:RHcert` is only the convergence of
optimiser duals to `(2,0)` (Paper 47 open item (2)).

## §5 Labels

| statement | label |
|---|---|
| Lemma 2.2 (`2cosh(u/2)` has exactly one negative square on every interval; PD on none) | `PROVED` |
| Thm 1 (flat-top certificate at `T` ⟹ `ν_w ∈ 𝔈(T)`; strict ⟹ a continuum of a.c. solutions) | `PROVED` |
| Thm 2 (solvability of KEP(T) ⟹ `λ^W_T ≥ 0`) | `PROVED` |
| Thm 3 (dichotomy; RH ⟺ KEP(T) indeterminate for every `T > 0`) | `PROVED` (uses `cor:RH`, `thm:Zexh`) |
| Thm 4 (finite `Z`: `μ_Z` the unique finite positive symmetric solution, no decay hypothesis) | `PROVED` — strengthens `thm:finZ` |
| Thm 5 (perturbed datum `g_β` indeterminate at `½log3`, unconditionally) | `PROVED` |
| "Theorem C ⟹ KEP(½log3) indeterminate unconditionally" | **FALSE AS STATED / CORRECTION OF RECORD** (`β ≠ (2,0)`, `g₀,g₁` inside the window) |
| `λ^W_{½log3} > 0` unconditionally | **[amended 2026-09-22 per R155_041]** **KNOWN** (Zhu 2026 Thm 1.2, `CITED-NOT-VERIFIED`; `λ^W_{½log3} ≥ λ^W_{0.8} ≥ 8.9·10⁻¹⁸ > 0`), *not* `OPEN` — not via Theorem C or `Paper42` |
| KEP(T) indeterminate for every `T ≤ 0.8` | **[amended 2026-09-22 per R155_041]** `PROVED` unconditionally (Zhu 2026 + Thm 3(a)) |
| Rem. 2.5's "for ζ the extension problem is indeterminate at every scale, and the obstruction disappears" | for `T ≤ 0.8`: `PROVED` unconditionally (Zhu + Thm 3(a)); for `T > 0.8`: reclassified from `HEURISTIC` to **RH-EQUIVALENT** (Thm 3(b)) |
| §4(iii) extremal-extension route | `HEURISTIC` |
| Row-D label | **unchanged**; no sign, no new endpoint |

## §6 Proposal for Paper 47 (not applied here — Paper 47 untouched by instruction)

1. Replace the unnumbered *Remark (Kreĭn extension)* of §7 by a short subsection "§7.x The extension
   problem", containing Definition 2.1, Lemma 2.2, and Theorems 1–3 with the proofs above. It costs ≈ one
   page, uses only `thm:Z`, `thm:Zexh`, `cor:RH`, and it converts `cor:RH` into a statement about a
   classical object (Kreĭn's extension problem) with no new hypothesis — a genuine reformulation, correctly
   flagged as an equivalence and not as progress.
2. Add Theorem 4 immediately after `thm:finZ` as "Corollary (determinacy)", or restructure: prove Theorem 4
   first and derive `thm:finZ` from it in three lines (as in §3 above). The second option is better
   mathematics — the decay hypothesis on `w` is then seen to be inessential to the phenomenon — and it
   supplies the determinacy half of the contrast that the closing paragraph of §7.2 already draws in words.
3. Amend the paper's open item (5): the distributional Kreĭn route does **not** give "a third proof of
   `thm:D1`" for the complete datum; by Theorem 3 it gives an equivalence with RH. **[amended 2026-09-22
   per R155_041, E1]** State the remaining honest question as: *is `λ^W_T > 0` unconditionally for
   `T > 0.8`?* — not at `½log3`, which Zhu 2026 (`main.tex` l. 994–997) already settles unconditionally.
   Also sharpen `main.tex` l. 284–286 ("Theorem C is an independent proof … not a new range") to add
   "of the **primitive** form", since Zhu's certificate is for the complete form.
4. `R155_014` Rem. 2.5: replace the `HEURISTIC` amendment by a pointer to Theorems 3 and 4 of this file —
   the finite half is now proved in the strong form, the ζ half is proved unconditionally for `T ≤ 0.8`
   (via Zhu + Thm 3(a)), and proved RH-equivalent for `T > 0.8`.
5. **[added 2026-09-22 per R155_041]** Add the unconditional indeterminacy statement for `T ≤ 0.8` (Zhu
   2026 + Thm 3(a)) as an explicit corollary alongside the §7.x reformulation of item 1.
