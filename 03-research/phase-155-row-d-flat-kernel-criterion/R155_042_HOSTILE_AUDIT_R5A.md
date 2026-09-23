# R155.042 — Hostile audit of R155_039 (builder round 5a)

*2026-09-22. Target: `R155_039_BUILDER_ROUND5A_H1_AND_SEVEN.md`, `scripts/r5a/`. Reruns: `r5a_04_lower.py`
only (<1 s); `r5a_01/02/03` exceed the 60 s rerun cap and were audited from their JSON. Verdict:
**mathematics sound, four numerical/scope errors, one label to demote.** No endpoint changes.*

## §1 Verdicts

| item | verdict |
|---|---|
| (i) trace formula `tr M₋ = (2T/π)∫₀^{τ₀}(−m)` | **CORRECT.** `tr(Q_T f(D) Q_T) = (2T/2π)∫_ℝ f`; `m₋` even and supported in `\|τ\|<τ₀` ⇒ `(2T/π)∫₀^{τ₀}`. Constant misprinted, see E2 |
| `M₊ > 0` gapless (Paley–Wiener) | **CORRECT**, and the no-gap mechanism is the right obstruction |
| BS negative (`584 / 3548`) | **ACCEPT as recorded negative.** Stronger than stated: since `M₊` has spectrum accumulating at `0`, the *true* `tr(M₊^{−1}M₋)` is plausibly `+∞`; the Galerkin values are lower bounds growing with `N`. Say so |
| `ε`-shift sign argument | **CORRECT** (`A_∞ ≤ (M₊+ε)−M₋` ⇒ `n₋(A_∞) ≥ n₋(shifted)`, wrong direction) |
| "CLR unavailable in `d=1`" | **FAIR** (CLR/Cwikel–Lieb–Rozenblum needs `d ≥ 3`; `d=1,2` fail), and `M₊` is non-elliptic |
| **Theorem J** | **PROVED, proof valid as written.** Dirichlet sines `sin(jπ(t+T)/2T)` on `H¹₀(−T,T)` extended by `0` ⇒ Plancherel `∫τ²\|F̂\|²/2π = ‖F′‖²` ✓; `dμ = \|F̂\|²dτ/(2π‖F‖²)` is a probability measure ✓; `φ` complete Bernstein ⇒ concave and strictly increasing (`thm:S`) ⇒ Jensen ceiling ✓; `φ(τ₀²) = −C₀` reproduced (`r5a_04`: diff `−1.24·10⁻¹⁰`) ✓; strictness from `kπ/2T < τ₀` + strict monotonicity ✓; `codim P_T = 2` ⇒ `−3` ✓. Count `#{k≥1 : k < 2Tτ₀/π} = ⌈2Tτ₀/π⌉−1` ✓ (non-integer case) |
| Theorem J's numbers | reproduced: `2Tτ₀/π = 2.1996 / 2.7755 / 3.2034` at `½log3 / log2 / 0.80`; `n₋(Γ) ≥ 2/2/3`, `n₋(A_∞\|P_T) ≥ 0/0/1`. **The `P_T` bound is vacuous at both `½log3` and `log 2`** — see E5 |
| `T₂` hard constant | **mechanism CORRECT** (`⌈x⌉−3 ≥ 2 ⇔ ⌈x⌉ ≥ 5 ⇔ x > 4 ⇔ T > 2π/τ₀`); **constant WRONG**, see E1 |
| "PROVED on both sides" | **ACCEPTED**, but only because `R155_023` Prop 3(ii)'s *upper* half is `PROVED` (min–max) per its 2026-09-22 amendment. Prop NC's `68.51·T` is a different, explicit, non-matching bound and must not be cited as the matching side |
| **Theorem J′** | **NOT A THEOREM** — a reading; see E6 |
| **Lemma N** | **PROVED**; derivation checked (unfold `τ_a`, `Re` symmetrises `a ↔ −a`, evenness identifies the halves, support `(a−T,a+T)∩(−T,T) = (a−T,T)` for `0<a<2T`) ✓. Reproduced from `r5a_02.json`: `−v₂I(log2) = +0.18662`, `−v₃I(log3) = −0.14102` vs matrix atoms `+0.18672 / −0.14098`, sum `+0.04573 = π₁₃` ✓ (`R155_032:144`) |
| zeros of `I`, straddle | reproduced from `r5a_03.json`: `log 2`: `0.21276, 0.60873, 1.02248`, `I(log2) = −0.19043 < 0 < I(log3) = +0.11106` ⇒ straddle ✓; same at `T = 0.62` (`0.91390`) and `0.65` (`0.95840`), `log 3 = 1.0986 < 2T` in both ✓. Correctly labelled `DIAGNOSTIC`; the `T±z` tracking (`≤0.015 / ≤0.003`) is a heuristic and is labelled `DIAGNOSTIC` ✓ |
| **Prop G** | **CORRECT** as a conditional sign-forcing statement; the lobe signs it consumes are `DIAGNOSTIC` and the label says so ✓. `a* = T+z_e = 1.17172` ✓; miss `1.17172 − 1.09861 = 0.0731` ✓, but see E7 |
| `F* ≥ 0` **REFUTED** | **CORRECT and cleanly argued**: the two Tate constraints are `∫F e^{±u/2} = 0`, which for even `F` both read `∫F cosh(u/2) = 0`; `cosh > 0` ⇒ `F` changes sign. Nodes `±0.31516` (`r5a_02.json`) ✓ |

## §2 Errors (file:line)

- **E1 (numeric, in three places).** `2π/τ₀ = 6.2831853/6.2898360 = **0.9989426**`, not `0.998988`.
  `R155_039:118`, `:219` print `0.998988`; `:27` prints `0.99895` (a third value — internally inconsistent).
  Also the inequality is non-strict at the endpoint: `T > 2π/τ₀` kills `(H1)`, so `T₂ ≤ 2π/τ₀`. Correct
  wording: **`T₂ ≤ 0.9989426`**.
- **E2 (numeric).** `(2/π)·7.061945658 = **4.495774**`, not `4.4956`. `R155_039:68`, `:214`. (The derived
  values `2.4696 / 3.1162` are right — they were computed from the exact integral, not from `4.4956`.)
- **E3 (scope error).** `R155_039:133` writes `2 ≤ n₋(Γ_{log2}) ≤ 47`. The `2` is on `L²(−T,T)`; the `47`
  is Prop NC's bound for `n₋(A_∞|P_T)` (`main.tex:2599–2610`, `R155_033:271`). Mixing spaces. Either
  `2 ≤ n₋(Γ_{log2}) ≤ 49` (adding the codim-2 slack) or, on `P_T`, `0 ≤ n₋(A_∞|P_{log2}) ≤ 47`.
- **E4 (statement).** `R155_039:24` drops the ceiling: `≥ 2Tτ₀/π − 3` should be `≥ ⌈2Tτ₀/π⌉ − 3`.
- **E5 (presentation, must not survive into Paper 47).** At the two windows of record Theorem J gives
  `n₋(A_∞|P_T) ≥ 0` — vacuous. `§0.2` and `§4` read as if a `P_T` bound had been obtained at `log 2`;
  the only non-vacuous `P_T` content there is asymptotic, plus the `T₂` consequence at `T > 0.9989`.
- **E6 (label).** `R155_039:125,220` label **Theorem J′ `PROVED`**. It quantifies over an unformalised
  class ("every Jensen/moment/Dirichlet argument") and the "⟺ prolate spread bound" is informal.
  Demote to **`OBSERVATION` / remark (`HEURISTIC` as a no-go)**. The one formal ingredient — concavity
  of `φ` gives only the ceiling `Γ_T(F)/‖F‖² ≤ C₀ + φ(‖F′‖²/‖F‖²)` — *is* `PROVED` and may be stated.
- **E7 (rounding).** `R155_039:176` "misses by `0.073` (`6 %`)": the relative miss is `0.0731/1.09861 =
  **6.65 %**` (or `6.24 %` of `a*`). Write `≈ 7 %` or give both.
- **E8 (minor).** `R155_039:150` "verified to `4` digits": the agreement is `0.18662` vs `0.18672`, i.e.
  3 digits. Write "3 digits (quadrature level)".
- **E9 (minor).** Declared compute `4 min` (`:7`, `scripts/r5a/README.md`) vs the README's own per-script
  times `150+100+150+1 ≈ 6.7 min`. Declare `≈ 7 min`.

## §3 Readiness for Paper 47

1. **Theorem J — READY** after E4. Permissible wording: *"`n₋(Γ_T) ≥ ⌈2Tτ₀/π⌉ − 1` on `L²(−T,T)`, hence
   `n₋(A_∞|P_T) ≥ ⌈2Tτ₀/π⌉ − 3`; the latter is vacuous for `T ≤ 2π/τ₀`."* The last clause is mandatory.
2. **`T₂` remark — READY** with E1's constant: *"`(H1)` can hold only for `T ≤ 2π/τ₀ = 0.9989426`."*
   The asymptotic corollary may be stated as *"`n₋(A_∞|P_T) = (2τ₀/π)T + O(log T)`, `2τ₀/π = 4.004234`,
   both bounds proved (upper: min–max, `R155_023` Prop 3(ii); lower: Theorem J)"* — with no reference to
   Prop NC's `68.51·T`, which is the explicit-in-`T` bound, not the matching one.
3. **Theorem J′ — READY only as an unlabelled remark after `cor:mono`**, phrased as: concavity of `φ`
   makes `cor:mono` an upper bound; a companion lower bound requires a lower bound on the spread of
   `|F̂|²`, i.e. an explicit prolate concentration estimate. No "no-go theorem" claim (E6).
4. **Lemma N — READY** as printed; the `π₁₃` example is `DIAGNOSTIC` and must be marked so (E8).
5. **Prop G — READY as a remark**, with the hypothesis "`e > 0` on `(z_e,T)` and `F < 0` on `(−T,−z_F)`"
   stated explicitly as an input, and the `log 2` numbers (`a* = 1.1717`, miss `≈ 7 %`) `DIAGNOSTIC` (E7).
6. **Birman–Schwinger material — correctly not proposed.** Keep in the phase record.

**Endpoint of record unchanged**: `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`. `(H1)` remains `HYPOTHESIS`.
