# R132.003 — Closing audit of round 1 (Paper 45 rebuilt on the true carrier)

Independent of the
audit R132.002 (in progress when written).

## 1. Re-derived and found correct

| statement | check |
|---|---|
| Lemma 9.1 | `Φ_F` entire, (9.1) by `N` integrations by parts, `g(½+iτ) = \|F̂(τ)\|²` for real `F`, `h` even ✓ |
| Lemma 9.2 | argument principle on `R_j`; `ξ` has no poles; horizontal sides `O(X_j^{−4}\log²X_j)` with (E3) ✓ (see LF2 on the import) |
| Lemma 9.3 | substitution `s = 1−u` reverses orientation; `∫_{L_{1−c}}gA = ∫_{L_c}g(u)A(1−u)du`; with `A(1−s) = −A(s)` the bracket is `2∫_{L_c}gA` ✓ (independently recomputed here) |
| Thm 9.4 (a) | residues of `gA_0` at `0,1` are `g(0), g(1)`; `(1/πi)∫_{L_c}gA_0 = g(0)+g(1) = 2Φ_F(0)Φ_F(1)` ✓ |
| Thm 9.4 (b) | `A_Γ` holomorphic on `Re s>0`; shift to `L_{1/2}`; odd imaginary part integrates to zero; `(1/2π)∫\|F̂\|²[Re ψ(¼+iτ/2) − \log π]` ✓ |
| Thm 9.4 (c) | expansion on `L_c` by Fubini; each `g(s)n^{−s}` entire ⇒ shift with no residue; `(1/πi)∫ = 2n^{−1/2}h(−\log n)`; evenness of `h` gives the symmetric bracket ✓. R132.001's correction of the blueprint (factor 2 from the reflection; `F` real) is right, as is Rem 9.5(2) (the bracket must not be split termwise: `−½\log π` would be annihilated) |
| Thm 9.6 signs | `T_∞(Γ_h) = Σ Λ n^{−1/2}[h(\log n)+h(−\log n)] + (1/2π)∫\|F̂\|²[\log π − Re ψ]`; with (9.6) this gives `T_∞(Γ_{F⋆F^†}) = 2Φ_F(0)Φ_F(1) − Σ_ρ g(ρ)` ✓; consistent with Paper 44 (8bis.14e) and with independent numerics (`scripts/lead_explicit_formula_check.py`: `Σ_ρ = polar + gamma − prime` to 20 digits) |
| Thm 9.6′ | eventual exactness of the chart sequence by Paper 43 Thm 8A.7c(a): shells at `ℓ` have modulus `ℓ^{−k} ∉ supp h` for `\log ℓ > R(Γ_h)`; archimedean term chart-independent for radial classes; unit packets vanish ✓ |
| Lemma 9bis.1, Thm 9bis.2, Cor 9bis.3 | `A(s) = −ξ'/ξ + 1/s + 1/(s−1)`, `A(s)+A(1−s) ≡ 0` ✓ (R132.000's supplement, verified to 25 digits); the sharpening that `f_p` has no pole at `s=1` and the pole there comes from `f_p(1−s)` is right; principal-component restriction correctly stated |
| Thm 9bis.4 | R132.001's refutation of the blueprint's Mertens mechanism is **correct**: in Paper 43 Thm 10.8b the archimedean term is exponentially small and the value 1 comes from the finite places; Mertens governs `s = 1`, not the residue count at `s = 0`. Accepted; the blueprint's §2.2 is withdrawn in favour of Thm 9bis.2/9bis.4 |
| Thm 7.5 | `a(s) = 1/s + O(1)`; residue transport `r ↦ −ir`; `ζ_∞(s) = 1/s` ✓ |
| Thm 8.1, Rem 8.2 | `M(Γ_F) = (λ_−,λ_+) = (Φ_F(1),Φ_F(0))` is the swap of `z(F)`; `β_T` swap-invariant ✓; the correction to the ruling labels is real and harmless |
| Thm 12.2 | `\hat T_S` even on `𝔠_0`; density of `\{ĝ\}` in Schwartz space; `\hat T_S(𝔠_0,0) ≥ 5.372 > 0` (Paper 43 (14.2)) so the zero set is discrete; `ĥ ≡ 0` ✓. Rem 12.3's point that this is **not** a corollary of `𝓝 = 0` is right |
| Thm 10.4, (10.1) | the `C10` fix is the real-linear isomorphism `(a,b) ↦ a + b s_0²`. **P3 closed here:** `106_11` uses `ρ = ½ + is` (its (2)), so `s_0 = x_0 + iy_0` with `y_0 = −(β_0−½) ≠ 0` (off the line) and `x_0 = γ_0 ≠ 0`; its own (20) is `Im s_0² = 2x_0y_0 ≠ 0` and (21) is the isomorphism. The paper's reading is correct; the hypothesis `x_0 ≠ 0` is the classical fact that `ζ` has no real nontrivial zeros, which must be **named** (LF1) |
| §9.6 order of limits, §11, §13 ledger, §14.2 table, §14.4 | consistent; "used or declined with a reason" executed |
| scripts | `verify_132_explicit_formula.py` 22/22 (re-run here) |

## 2. Findings

**LF1 (MINOR) — an unnamed import in Thm 10.4.** The `C10` fix needs
`Re s_0 ≠ 0` in `106_11`'s variable, i.e. `γ_0 ≠ 0`: nontrivial zeros of `ζ`
are not real (`ζ(σ) ≠ 0` on `(0,1)`). Add it to (E2) and cite it at (10.1).

**LF2 (MINOR) — (E3) as stated is two imports.** `N(T) = O(T\log T)` gives the
existence of `X_j` with distance `≥ c/\log j` from every ordinate; the bound
`ξ'/ξ(σ ± iX_j) = O(\log²X_j)` uniformly on `1−c ≤ σ ≤ c` is a **separate**
classical lemma (`ζ'/ζ(s) = Σ_{\|γ−t\|<1}1/(s−ρ) + O(\log t)` in the strip,
Davenport Ch. 15–17; on `Re s = c` it is bounded by (E1); on `Re s = 1−c` by
the functional equation). Split (E3) into (E3a), (E3b) with sources; the proof
is unaffected.

**LF3 (MINOR) — Thm 9.6′'s wording "converge, for every real `F`"** should say
"are eventually constant, for every real `F`" in the statement, not only in the
proof: the distributional limit is a limit of an eventually constant sequence
pointwise in `F`, which is weaker than distributional convergence in any
topology on the tests and stronger pointwise; say exactly which.

**LF4 (NOTE) — §0.1 item (3) rhetoric (R132.001's P1).** Acceptable as written:
`A` is defined by its meromorphic continuation and Cor 9bis.3 says the two
operations do not commute. Keep the phrase "formal colimit symbol" in every
statement of §9bis; do not write `T̂_∞` without `^{mer}` anywhere.

**LF5 (NOTE) — cross-paper edits authorized here**, to be made in round
2 (these are the "connected well" items): (a) Paper 44
Thm 8bis.4(ii): relabel the explicit formula from `CLASSICAL` to
`PROVED-IN-REPOSITORY (Paper 45 Thm 9.4)`, keeping Weil's *criterion*
(iii) `CLASSICAL`; (b) Paper 43 §13.8 / clause ledger row "`𝓝_∞^W = 0`:
`CLASSICAL`, row C": Paper 45 §0.2 declines it — record in Paper 43's row
"declined by row C (Paper 45 §0.2, §14.3); not claimed anywhere"; (c) Paper 43
§14.1a "what rows B and C may use": add the line that row C used Thm 10.8b
only as the structure constant of `β_T` (Paper 45 Thm 9bis.4(ii)) and Thm 14.1
as Warning 8.5; (d) Paper 44 §9 / §10.4: add "row C received Thm 9.1 as
Paper 45 Thm 5.1 and (C1) as its standing convention". Each edit one sentence,
marked `[phase 132]`, with the theorem number.

## 3. Interim ruling

Round 1 is the strongest single round of the three phases: the explicit
formula is proved in the repository with a correct contour argument, the
comparison theorem is stated with every hypothesis carried, and the Tate-pole
question is settled by the vanishing of the meromorphic colimit symbol. No
error of substance found here. Pending: the audit R132.002, then
one repair round for LF1–LF3, LF5 and the auditor's findings.
