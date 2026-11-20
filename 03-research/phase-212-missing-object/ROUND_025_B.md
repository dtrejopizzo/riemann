# Round 25, memo B — Logical attack on the "existence + rigidity" scheme (R)/(E)/(WF)

Notation of the common statement: `a^w_T(F) = Arch(F) − Σ_{n≥2} w_n c_F(log n)` on `P_T`, `v_n = 2Λ(n)/√n`, `d = w − v`,
`D(τ) = Σ d_n (n^{iτ} + n^{−iτ})`. Sources opened: ROUND_021_A §1 (family `Π_T(M∗φ)`, identity (1.1), bounds
(1.2)–(1.3)), ROUND_022_A filter, ROUND_024_A §2 (profile of `M`, boundary layer), P47 `thm:coer-schur` (l.≈5239),
`rem:coer-size`, `thm:index` (l.2527–2532). Not opened: ROUND_019_A complete, P46 thm:radical (only via citations of 021_A).
Index: grep only (l.486 "multigenerator rigidity", l.1861 "unique weight δ_{N=1}", l.558–559 deletions/Beurling);
those memos were not opened: the novelty cross-check is not part of this memo.

## Verdicts

| Step | Verdict |
|---|---|
| (R) rigidity | **FALSE as argued** (concrete gap §1); a correct weak version remains, and the rest is OPEN |
| (E) existence | **CORRECT** (with the box bound of §2, which must be written) |
| (WF) duality | **CORRECTABLE**: holds with closure; "v unique multiplier" is FALSE at fixed T |
| (d) circularity | `K_T ≠ ∅` is **strictly weaker** at fixed T; ∀T it equals the target only if (R) holds |
| (e) controls | coprime-to-p: nontrivial prediction (WF fails), consistent; Beurling: the chain breaks at (R) |

## §1 (R): where it breaks

**What does work (ARGUED, on the bounds of ROUND_021_A).** Let `φ ∈ C_c^∞` of fixed length `ℓ` and `X = Π_T(M∗φ)`.
By (1.3), `a^v_T(X)/‖X‖²` is doubly exponentially small as `T → ∞` with `ℓ` fixed. Moreover `c_{M∗φ}` decays
doubly exponentially outside `[−2ℓ−C, 2ℓ+C]`, so only `n ≲ e^{2ℓ+C}` enter: it is a finite sum, independent
of `T`. The truncation `Π_T` costs `≤ (Σ_{n<e^{2T}} |d_n|)·e^{cT}e^{−2πe^{2(T−ℓ−O(1))}}`. This is absorbed if
`|d_n| ≲ log n`, a bound that §2 gives from the hypothesis itself: **w does need to be bounded**, and the hypothesis does it.
The sign of `w` does not intervene. Normalizing, `a^w_T ≥ 0 ∀T` gives
`⟨|Φ_M|² D, |φ̂|²⟩ ≤ 0` for every `φ ∈ C_c^∞`. By Bochner–Schwartz, `−|Φ_M|²D` is a positive measure. Hence:

  **(R′)** `D ≤ 0` as a distribution on `ℝ \ Z`, where `Z` is the (discrete) set of zeros of `Φ_M(½+iτ)`.

**The gap.** The quasi-radical family has `|X̂|² = |Φ_M|²|φ̂|²`, which vanishes on `Z`: **it does not see `D` on `Z`**. The step
"`D ≤ 0` in local mean + mean zero ⇒ `D = 0`" requires `D ≤ 0` on all of `ℝ`. With `D ≤ 0` only outside `Z`, the
Fejér argument (`D̂` vanishes on `(−log 2, log 2)`; convolve with the Fejér kernel `K ≥ 0`, `supp K̂ ⊂ (−log 2, log 2)`, and
obtain `D∗K ≡ 0`) only proves that the part of `D` outside `Z` is compensated by a distribution supported on `Z`.
**Counterexample to the argument (not to the statement):** `d = −s v`, `0 < s < 1`, i.e. `w = (1−s)v`. By the explicit formula
(CITED, Weil), `D_v = A − (masses on Z)`, with `A > 0` a smooth density. Thus `D = −sA + s·(masses on Z)`, which is `≤ 0`
outside `Z`: it passes all quasi-radical tests. Directly, `a^{(1−s)v}_T(X) = (1−s)a^v_T(X) + s·Arch(X)`, and `Arch(X) > 0`
on that family. Excluding `(1−s)v` requires information about the directions where Arch is negative
(`n_−(Arch|P_T) ≥ 1` from `T*_ev`):
`a^{(1−s)v}_T ≥ 0 ⟺ s ≤ s_T := inf_{Arch(F)<0} a^v_T(F)/(a^v_T(F) − Arch(F))`, and (R) needs `inf_T s_T = 0`. That
statement is quantitative, independent and OPEN. More generally, (R) reduces to classifying the pairs `(D, Z)`:
distributions with spectrum in `±log ℕ_{≥2}` that are `≤ 0` outside `Z` (Fourier quasicrystal type). OPEN; no opened source
of the corpus resolves it.
**Mean zero and window T:** the mean-zero argument survives (the sum is finite at fixed `ℓ` and Fejér controls it
exactly), but that is not where it fails.
**Weights of other functions:** with the same archimedean factor and conductor 1 there is no other candidate in degree 1. The
even characters of conductor `q` add `(log q)c_F(0)`, which is not in the form. There is no contradiction with what is known.

## §2 (E): box bound and inverse limit

**K_T bounded (sketch PROVED).** For each `n < e^{2T}` take `F = f ± f(·−log n)` with `f` of width
`h < min(log 2, min_{m≠n}|log m − log n|)/2 ≍ 1/n`. Correct with fixed `u_±` to enter `P_T`; the correction is `O(‖f‖_{L¹}) = O(h^{1/2}‖f‖)`.
Then `c_F(log m) ≈ 0` for `m ≠ n` and `c_F(log n) = ±‖f‖²`, and `Arch(F) ≤ (log(1/h)+C)‖F‖²`.
Therefore `|w_n| ≤ C(log n + 1)`. Moreover `K_T` is closed (intersection of half-spaces) and convex.
**Restriction:** extension by zero preserves `∫F e^{±t/2}`, `c_F` and `Arch` (local, P47: `a_T = W_*` on functions
supported in `I`). Thus `a^{w}_{T'}(F) = a^{w|_{n<e^{2T}}}_T(F)` for `F ∈ P_T`, and the restriction maps `K_{T'}` into `K_T`. CORRECT.
**Inverse limit:** a sequence `T_k ↑ ∞` suffices, because every window is contained in one of them. An inverse limit of
nonempty compacts is nonempty (Tychonoff). It gives `w` with `a^w_T ≥ 0` for EVERY `T`. CORRECT.

## §3 (WF): exact statement

`C_T := {(Arch(ρ), (c_ρ(log n))_{2≤n<e^{2T}}) : ρ ⪰ 0 trace class, range in P_T, Arch(ρ) < ∞} ⊂ ℝ^{1+N}`.
Separation in finite dimension: there exists `(1, −w) ∈ C_T*` ⟺ `C_T* ⊄ {λ ≤ 0}` ⟺ `(−1, 0) ∉ cl C_T`.

**Likely statement (PROVED, standard separation):**
- Signed weights: `K_T ≠ ∅` ⟺ there is no sequence `ρ_k` with `Arch(ρ_k) → −1` and `c_{ρ_k}(log n) → 0` for every `n < e^{2T}`.
- Weights `w ≥ 0`: the same with `c_{ρ_k}(log n) → p_n ≥ 0` (the cone `C_T + {0}×(−ℝ^N_+)` is used).

**Version with "there exists an exact ρ":** requires `C_T` to be closed. Not proved. `Arch` is bounded below on `P_T`,
but the trace may blow up: mass on the `n_−` negative directions compensated by positive mass. Moreover
`ρ ↦ c_ρ(log n)` is not weak-* continuous, because translation is not compact. Slater is not needed on the dual side
(finite dimension); the difficulty is in the closure of the primal. CORRECTABLE: state with sequences or with `cl C_T`.
**"v is the unique multiplier":** FALSE at fixed `T`. For `T ∈ (½log3, T*_ev)`, `T*_ev ∈ (0.58, 0.60)`, P47 thm:index gives
`n_−(Arch|P_T) = 0`, hence `0 ∈ K_T`; and `v ∈ K_T` (Theorem A up to `log 2`). Uniqueness would only hold in the limit and
depends on (R).

## §4 (d) Circularity and small T

- `T < ½log 2`: no `n` enters. `K_T = {∅}` is nonempty ⟺ `Arch ≥ 0` on `P_T` ⟺ the target in that window: they coincide.
- `n = 2` enters at `T = ½log 2 ≈ 0.347`; `n = 3`, at `½log 3 ≈ 0.549`. For `T < T*_ev` one has `0 ∈ K_T`: `K_T ≠ ∅` is
  **trivial**, while `a^v_T ≥ 0` in that window is real content (P47 Theorem A). Therefore, at fixed `T`,
  `K_T ≠ ∅` is strictly weaker.
- `T > T*_ev`: `0 ∉ K_T`, and `K_T ≠ ∅` is no longer trivial. I know no certificate of `K_T ≠ ∅` other than exhibiting `v`.
- ∀T: `[K_T ≠ ∅ ∀T] ⟸ target` always. `⟹` is CONDITIONAL on full (R), which today is OPEN (§1). The
  weight-free formulation is not circular by definition, but its strength comes entirely from (R).

## §5 (e) Controls

- **Lattice of integers coprime to `p`.** There are fewer constraints, so there are more admissible states and WF(coprime) is
  stronger than WF(ℕ). If `K^{(p)}_T ≠ ∅` for every `T`, (E) would give a `w` with `w_{p^k} = 0`, and (R) would force `w = v`, with
  `v_p ≠ 0`: contradiction. Hence (R)+(E) **predict** that WF(coprime) fails at some `T`. This is consistent with the
  certified deletions (index l.558). Step (R′) already sees it: the symbol `2Re Σ_k log p·p^{−k(½+iτ)}` has mean zero and is not
  `≤ 0` outside `Z`. Good control, but the concrete `T` remains unquantified.
- **Beurling-type systems.** There is no entire `Φ_M` with the same archimedean factor and functional equation, so no
  quasi-radical family exists. The chain breaks at the first step of (R). (E) and (WF) still hold and only give that some `w` is
  in the intersection, without identifying it. Therefore a system where WF holds and `a^{v_N}` fails does **not** falsify the chain.
  It is consistent: all the arithmetic weight is in (R).

## Conclusion

(E) and the duality, in their closed form, are correct, but they carry no sign. The content is in (R), and (R) has a
concrete gap: quasi-radical tests are blind on `Z` and do not exclude `w = (1−s)v`. Closing it requires
(i) `inf_T s_T = 0` on the directions where Arch is negative and (ii) a classification of the crystalline pairs `(D, Z)`.
Both are OPEN and neither is weaker than what is sought on P_T.
Labels: (R′) ARGUED; box bound PROVED (sketch); (E) PROVED; closed (WF) PROVED; (R) OPEN.
