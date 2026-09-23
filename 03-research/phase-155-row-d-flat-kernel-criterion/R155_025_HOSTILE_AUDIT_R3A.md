# R155.025 — Hostile audit of R155.023 (round 3a: the archimedean threshold)

*2026-09-22. Target: `R155_023_BUILDER_ROUND3A_ARCHIMEDEAN_THRESHOLD.md`, `scripts/r3a/`.
All four scripts rerun (`r3a_01` 102 s, `r3a_02` 74 s/9 windows, `r3a_03` 119 s, `r3a_04` 34 s).
Every number in §3/§4 of the target reproduced to the digits printed. No sign for `ζ` is claimed
anywhere below; the endpoint of record `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` is untouched.*

## §0 Verdict table

| # | item | verdict |
|---|---|---|
| 1 | definitions/normalisation, Galerkin assembly, Lévy cross-check | `PROVED WITH REPAIRS` (cross-check numbers mislabelled; see §1) |
| 2 | thresholds `T*_∞ = 0.3716`, `T*_{∞,P} = 0.5958` | `DIAGNOSTIC`, reproduced; direction of error missing (§2) |
| 3 | `λ^∞_min ≤ λ^{∞,P}_min ≤ C₀ + φ((3π/2T)²)`; `T₀(0)=0.74921`; limit `→ C₀` | `PROVED` |
| 4 | `≥ 0` for `2T < log 2` | `PROVED BY CITATION` — space caveat, see §4 |
| 5 | `τ₀ = 6.28983599`; `n₋ ~ (2τ₀/π)T` | value `PROVED`/`DIAGNOSTIC`; asymptotic **`HEURISTIC`**, mislabelled `PROVED` |
| 6 | `‖P_T‖` values and conventions | `PROVED`/reproduced; notation collision |
| 7 | §5 corollary for `D`, `β ≈ (2,0)` | mostly `HEURISTIC`; one `PROVED` label overreaches (§7) |
| 8 | eight-window validation | correctly labelled `DIAGNOSTIC`; two count/value slips |
| 9 | refutation of the order's ordering | `CONFIRMED` |
| 10 | corpus check | good, one gap (§10) |

## §1 Definitions, assembly, cross-check
`arch_core.py:1–30` implements exactly `W_T = 2AB + C₀‖F‖² + ∫₀^∞(‖F‖²−c_F)K − Σ v_n c_F(log n)`,
`v_n = 2Λ(n)/√n`, `K = 1/(2sinh(u/2)) + 1/(2cosh(u/2))`; on `P_T = {a·x = b·x = 0}` the rank-2 pole
block is annihilated by construction (`restrict`, `arch_core.py:85–92`), so `A_∞|P_T = (1/2π)∫m|F̂|²`. ✓
Legendre basis is orthonormal and supported in `(−T,T)`, so every Galerkin value is an **upper bound**
on the corresponding infimum, and the `P_T`-restricted ones are upper bounds on `λ_min(·|P_T)`. ✓

**Error 1 (`R155_023:131–133`).** The Lévy-vs-direct cross-check is quoted as
`1.0118, 1.0148, 1.0157` against `1.0161`, i.e. `0.4 %` at the coarsest cutoff. The rerun of the
actual script at the working accuracy (`N = 18`) prints `Lévy = 2.14514723` against
`direct(|τ|<500) = 1.86645`, `direct(|τ|<2000) = 2.05753` — `13 %` and `4 %`. The quoted triple is
the `N = 10` run recorded in `scripts/r3a/README.md:9`, not the one the text is describing.
**Repair:** quote the `N = 18` numbers and keep the monotone-slow-convergence caveat; the check is
still a genuine (weak) corroboration, not a `0.4 %` agreement.

**Error 2 (consistency with phase 154).** `R155_023` reports `λ_min(a_T|P_T)(½log3) = 9.7692·10⁻⁴`;
`R155_004 §6` (`:497`) reports the Galerkin upper bound `9.893·10⁻⁴`. Both are upper bounds, and the
new one is the tighter, so **no contradiction** — but the spread is `1.3 %`, fifty times the claimed
`2.5·10⁻⁵` `N = 18` vs `N = 36` stability (`R155_023:127`). The stability claim is an *absolute*
figure and must be stated as such, or the two numbers read as a clash. Both remain consistent with
Theorem C's certified `λ ≥ 8.8577·10⁻⁵` (a lower bound, an order below).

Reproduced: `λ^{∞,P}_min(½log3) = +8.256587·10⁻²` ✓ (`+0.08255`),
`λ^∞_min(½log3) = −4.302532·10⁻¹` ✓ (`−0.43027`).

## §2 The thresholds
`r3a_03` reproduces `T*_∞ ∈ [0.371602, 0.371641]`, `T*_{∞,P} ∈ [0.595781, 0.595859]` exactly.
Monotonicity in `T` (Thm 1(a)) is correct and its proof is complete: `A_∞` is `T`-free, the feasible
sets are nested under extension by zero, the Tate constraints are `T`-free. ✓ Verified in the scan:
both columns are strictly decreasing over `0.300 → 0.800`.

**Error 3 (missing direction, `R155_023:167, 277`).** Galerkin gives `λ_Gal ≥ λ_true`. Hence a
positive computed value does **not** certify positivity, and the true thresholds satisfy
`T*_true ≤ T*_computed`. The document states the thresholds are `DIAGNOSTIC` but never states this
direction; as written a reader may take `T*_∞ ≥ ½log2` as established, when only
`T*_computed ≥ ½log2` is. The lower bound `T* ≥ ½log2` is nevertheless safe, since it comes from
Thm 1(b) (citation), not from the numerics. **Repair:** add "the computed thresholds are upper
bounds for the true ones".

**Error 4 (table row, `R155_023:144`).** The `T = 0.3466` row lists `‖P_T‖ = 0`, `A_T = 0`. At
`T = 0.3466`, `2T = 0.6932 > log 2`, so `N_T = {2}`: the rerun at `0.3466` gives `A_T = 0.9803`,
`‖P_T‖ = 0.01261`, `λ_min(W_T) = +1.3287·10⁻³`. Numerically harmless, but the row as printed
misstates the contact set at the very landmark the section is about.

## §3 The chain `λ^∞_min ≤ λ^{∞,P}_min ≤ C₀ + φ((3π/2T)²)`
Re-read `main.tex:393–407` (`cor:mono`) and `:1896–1915` (`thm:SC`). The builder's reading is
**correct and needs no repair**. `cor:mono`'s proof has exactly the two steps claimed: (i) the
bottom of `Lev` on the codimension-2 space `P_T` is `≤ λ₃ ≤ φ((3π/2T)²)` by Song–Vondraček — this
step uses no test function and no prime; (ii) `−Σ v_n c_F(log n) ≤ A‖F‖²`, vacuous at `A = 0`. The
bound `|c_F| ≤ ‖F‖²` enters only in (ii). `thm:SC` is already stated for an *arbitrary* contact set
`N ⊆ {n : log n < 2T}` with nonnegative weights of mass `A`, so `N = ∅`, `A = 0` is a legitimate
instance of a published theorem, not an extrapolation: the bound `C₀ + φ((3π/2T)²)` on `P_T` is
immediate. ✓ `T₀(0) = 0.74921` matches `main.tex:1905` and the independent evaluation
`φ((3π/2·0.74921)²) = 5.37218 = −C₀` ✓ (`arch_core.phi_bernstein`). The limit
`λ^{∞,P}_min → C₀` is correct (`Lev ≥ 0` gives `≥ C₀`, `φ(0⁺) = 0` gives the other side). The first
inequality is set inclusion. `PROVED`.

## §4 Prime-free positivity
The corpus does contain the prime-free reduction: `phase-115/115_08 §4` (Props 0+5) proves that on
the Connes–Consani window the finite contact term vanishes identically and row (d) reduces to
`−G_∞ ≥ 0`. But `115_08 §5.1(2)` records explicitly that **`−G_∞ ≥ 0` is false in general and holds
only on the constrained space** (the run reports `|Ĝ(±i/2)| = 0.504` for Gaussians). So the corpus
does *not* hold an independent proof of archimedean positivity on all of `L²(−T,T)`; what carries
Thm 1(b) is the cited `W_T ≥ 0` for `T ≤ log 2` (`main.tex:276`, `Paper42/Yoshida1992/Bombieri2000`)
together with `N_T = ∅`. That is legitimate, but the citation is for the *unconstrained* window
form and Yoshida 1992 is not in `00-references` (`R154_013`). **Label repair:** Thm 1(b) is
`PROVED BY CITATION (unverified source for the unconstrained space)`, not plain `PROVED`; the
strictness is already correctly `CONDITIONAL`. The self-contained fallback bound at
`R155_023:88` is correct as stated (I checked the three pieces: `|c_F| ≤ 1`, `∫_{2T}^∞K = Ktail`,
`|A|,|B| ≤ (2 sinh T)^{1/2}`) and indeed only reaches `T ≲ 0.031`. Interestingly the finding of §3
— `λ^∞_min < 0` past `0.3716` on all of `L²` — is *consistent* with `115_08`'s warning; the document
should cite that corroboration.

## §5 Proposition 3
`τ₀ = 6.28983599` reproduced (`r3a_03`, Brent `10⁻¹²`, `m(0) = −5.372183 = C₀`); `m` increasing on
`[0,∞)` is `lem:mbounds`(i), so `m < 0 ⟺ |τ| < τ₀`. ✓ (i) is a tautology from the definition. ✓

**Error 5 (label, `R155_023:206, 281`).** (ii) is labelled `PROVED (Landau–Widom, standard)`. The
argument at `:207–216` is a sketch with two unquantified steps: "`‖F − B_{τ₀}F‖` is small in the
`L²`-averaged sense" on the Slepian span, and "a standard splitting … on a subspace of codimension
`O(log T)` makes the form strictly negative". Neither is carried out; the `log τ` growth of `m` off
the band is exactly what such a splitting has to beat, and no constant is produced. The matching
upper bound (min–max on `B_{τ₀}^⊥` where `m ≥ 0`) *is* correct and gives `n₋ ≤ 2Tτ₀/π + O(log T) + 2`.
**Repair:** label (ii) `HEURISTIC (upper bound `PROVED`, lower bound sketched)`. The document's own
"Honesty" paragraph already concedes the asymptotic is invisible at `T ≤ 0.8` (`4.004·T` predicts
`3.2` at `T = 0.80`, computed `n₋ = 1`), which makes the `PROVED` label harder to defend, not easier.

## §6 `‖P_T‖`
Reproduced: `0.49013` at `½log3`, `0.79004` at `0.58`, `0.89997` at `log 2`, `0.46089/0.48862` on the
`{2}` plateau, `0.68637` at the first `{2,3}` window `T = 0.560`, rising to `0.89997` at `log 2`,
`1.19515` at `0.80`. The `{2} → {2,3}` step `0.490 → 0.686` is real. ✓
Conventions check: `Cmat` returns the **symmetrised** `½(C + Cᵀ)`, and the prime block is
`−Σ v_n C(log n)` with `v_n = 2Λ(n)/√n`, i.e. kernel `−Σ_n v_n[δ(x−y−log n) + δ(x−y+log n)]/2`. This
reproduces the explicit-formula prime term `Σ_n (Λ(n)/√n)(h(log n) + h(−log n))` for `h = F⋆F̃` (even),
so the factor convention is right. ✓ `np.linalg.norm(Pi, 2)` is the spectral norm of a symmetric
matrix = `max|P_T(F)|` at `‖F‖ = 1`. ✓

**Error 6 (notation).** `P_T` denotes both the primitive subspace and the prime quadratic form
throughout §2–§3; `‖P_T‖` and `F ∈ P_T` sit in the same sentence at `:120` and in the same table
header at `:177`. Rename the form (e.g. `Π_T`) before any of this reaches Paper 47 §8.

## §7 §5 (the corollary for `D`)
- §5.1: `β = (2,0)` being the unique polar choice is `prop:P` ✓; that the optimum sits `1.3·10⁻³`
  away is `OBSERVED` ✓; but the *explanation* ("the reason the optimum is near `(2,0)` is that the
  certificate is not asked to create positivity") is a narrative, not a deduction — nothing in §2–§4
  forces the optimiser near `(2,0)`. Label `HEURISTIC`, not `PROVED (necessity) + OBSERVED`.
- §5.2 **Error 7 (`:243–249`).** What Corollary 2 + Prop 3(i) prove is only: past `T*_{∞,P}` any proof
  must show `P_T(F) ≥ −A_∞(F)` on a nonempty negative cone. The further claim that "`ν` reaches the
  inside comb *only* through `ν̂`'s oscillation at frequencies `≲ τ₀`" does **not** follow from
  Paper 47 §7: `main.tex:1052, 1070` show the inside and outside prime terms combining into a single
  `−Σ_{n≥2} v_n w(log n) cos(τ log n)` valid at **all** `τ`; the restriction to `|τ| < τ₀` is where
  positivity is *needed*, not where the outside atoms *act*. The stated "sign pattern in phase with
  the inside comb on `|τ| < τ₀`" is a plausible reading, not a necessary condition.
  **Repair:** keep the Corollary-2 necessity as `PROVED`; demote the frequency-window mechanism to
  `HEURISTIC`.
- §5.3: already `CONDITIONAL`, and honestly so (the `½log3` window degrades too, below `T*_{∞,P}`,
  which the text itself flags as the counterexample to its own mechanism). ✓
- §5.4: a methodological warning, not a theorem; unlabelled. Mark `HEURISTIC`.

## §8 The eight-window validation
`r3a_01` reproduced: `λ_min(W_T) = +7.5748·10⁻³, +1.3322·10⁻³, +1.8232·10⁻⁴, +1.6434·10⁻⁵,
+9.5835·10⁻⁷, +5.6461·10⁻⁸, +3.1344·10⁻⁹, +1.4007·10⁻¹⁰` at `T = 0.30, 0.3465, 0.40, 0.45, 0.50,
0.55, 0.60, log2`, and `λ_min(a_T|P_T)(log2) = +9.9559·10⁻⁷`. These are Galerkin upper bounds and
therefore prove nothing; the document says so explicitly at `:286–287` ("§3 is a Galerkin computation
and gives *upper* bounds on `λ_min`, never lower ones") and labels every table entry `DIAGNOSTIC`. ✓
The windows are all `≤ log 2`, so the owner's rule is respected and the run "reproduces the known
theorem" only in the sense of failing to contradict it — the text's phrase "reproducing the known
theorem" (`:136`) is acceptable given the explicit disclaimer, but "consistent with" is the honest verb.

**Error 8 (`:134–137`).** "eight windows" is followed by six values; `T = 0.45` (`+1.6434·10⁻⁵`) and
`T = 0.60` (`+3.1344·10⁻⁹`) are missing from the list. And `λ_min(a_T|P_T)(log2)` is quoted as
`+9.96·10⁻⁷` in §3 but tabulated as `9.9416·10⁻⁷` at `:161, 181` (`r3a_04` uses a different
restriction path than `r3a_02`); the two agree only to `1.5·10⁻³` relative, which is the real
accuracy of the restricted eigenvalue and should be stated.

## §9 The ordering
Confirmed. `P_T ⊂ L²(−T,T)` and `A_∞` is `T`-free, so `inf` over the subspace is `≥` the `inf` over
the whole space: `λ^∞_min ≤ λ^{∞,P}_min`. The order's `λ^{∞,P}_min ≤ λ^∞_min` is `REFUTED`, verified
at all nine reproduced windows (`−0.43025` vs `+0.08257` at `½log3`; `−0.92643` vs `−0.30175` at
`0.80`). The builder's `REFUTED` label is correct and correctly argued.

## §10 Corpus check
The §1 table is honest about hit counts and about what is new; the `Yoshida` row correctly records
`R154_013`'s finding that the 1992 volume is absent from `00-references`, and uses the citation only
for `≥ 0`. **Gap:** the Connes–Consani row cites the prime-free window but not `115_08 §5.1(2)`, the
one place in the corpus that *already* records archimedean positivity failing off the constrained
space — the closest prior art to this round's main finding, and a corroboration the document should
be claiming. Add it. No other omission found: `grep` for `lambda^inf`, `archimedean threshold`,
`T\*_` returns nothing outside phase 155.

## §11 What is paper-ready for Paper 47 §8

**Ready, as a proposition with `DIAGNOSTIC` values.**
> *Proposition (archimedean thresholds).* Let `A_∞` be the prime-free Weil form. Then `λ^∞_min` and
> `λ^{∞,P}_min` are non-increasing in `T`; `λ^∞_min ≥ 0` for `2T < log 2`; and
> `λ^∞_min ≤ λ^{∞,P}_min ≤ C₀ + φ((3π/2T)²) < 0` for `T ≥ T₀(0) = 0.74921` (Thm SC at `A = 0`).
> Hence thresholds `T*_∞ ≤ T*_{∞,P}` exist in `[½log2, 0.74921]`. Galerkin (`N = 18`, `DIAGNOSTIC`,
> upper bounds): `T*_∞ ≈ 0.3716`, `T*_{∞,P} ≈ 0.5958`.

The structure is `PROVED`; only the two numbers are `DIAGNOSTIC`, and the sentence must say they are
upper bounds. This is a genuine sharpening of `thm:SC` at `A = 0` (`0.5958` against `0.74921`, a
`20 %` loss in the Song–Vondraček step) and belongs in §8.

**Ready as `DIAGNOSTIC` only.** The necessity statement `η_P(log 2) = 0.154`: past `T*_{∞,P}` a
certificate must *create* that much positivity rather than preserve it. The *shape* (Corollary 2) is
`PROVED`; the *value* `0.154` is a Galerkin upper bound on a deficit, hence a lower bound on nothing
— state it as `DIAGNOSTIC` and never as a certified obstruction size. Same for
`P_T(F*_∞)/η = 1.075, 1.054, 1.059` and for `0.58 < T*_{∞,P}` (`R155_023 §7.3`).

**Not ready.** Prop 3(ii) (`HEURISTIC`), all of §5.1–5.2's causal readings (`HEURISTIC`), the `0.4 %`
Lévy cross-check (wrong run).
