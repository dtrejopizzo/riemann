# R153.017 — Lead closing decision, round 5 (construction of Φ_N at the symbol level)

*Lead: Fable 5.1, 2026-09-19. Input: R153_015 (blueprint), R153_016 (builder). No hostile audit run: the round's outcome is negative
on its own terms and the negative results are elementary; a hostile pass is required only if any item below is to be cited as PROVED
outside this phase.*

## 1. Verdicts (provisional labels; hostile audit pending for citation)

| item | statement | label |
|---|---|---|
| symbol identity | `⟨A_T F,F⟩ = (2π)^{-1}∫σ_T|F̂|²` on `P_T`, `σ_T = Re ψ(¼+iτ/2) − log π − 2Σ_{n<e^{2T}} w_n cos(τ log n)` (Paper 42's `−ψ(¼)` bookkeeping cancels against `m_0`); classical Weil symbol; in the corpus for the band-limited space (phase 60 RH-PROOF-PAPER.md:46) | `RESTATEMENT` |
| `N_T = {σ_T < 0}` | not a neighbourhood of 0: two wells to `τ = 10.5` at `½log3`, six wells to `τ = 46.1` at `log 2`; proved bound `τ_1(log 2) = 59.5`, `τ_1 ≍ 2πe^{2S_T}`; `σ(0) = −6.35` (`½log3`, only `n=2`), `−7.62` (`log 2`) | `PROVED`/`DIAGNOSTIC-NUMERIC` |
| prime bands | `Φ_2, Φ_3` simultaneously positive only on `(2.266, 4.289)` | `PROVED` |
| uncertainty | `θ(T,τ_*) ≤ 2Tτ_*/π`; prolate `λ_0(Tτ_0) = 0.84, 0.79`; constraint-free reduction `⟨A_TF,F⟩ = (2π)^{-1}∫(τ²+¼)²σ_T|Ĝ|²` | `PROVED` |
| **hand proof** | closes at **neither** endpoint: budget `2Tτ_*/π = 3.68` (`½log3`), `20.4` (`log 2`) — vacuous; `(τ²+¼)²` amplifies the far wells by `10⁶`. Not a constants problem. | `REFUTED` (as a route) |
| no soft minorant proof | Krein/autocorrelation LP reformulation; Bochner forces any pointwise minorant to be `≥ 0`, so no proof using only `|F̂|² ≥ 0` exists | `PROVED` (elementary), consistent with corpus ES-14 |
| `R(T) = 2Tτ_0(T)/π` | `σ_T(π/2T) < 0` at both endpoints; `R` crosses 1 at `T_c = 0.6898`, 0.5% below `log 2`, where `c(T)` peaks (R153_014) | `DIAGNOSTIC-NUMERIC`, filed (P153.15) |
| T5 (`Ξ_a`) | separation is **depth**, not width nor moment geometry: `σ^{(a)}(0)/σ(0) = 6.54` (`a=.45`), `2.62`, `2.05`, from weights `n^a+n^{-a}`; `Ξ_{0.45}` has *more* origin suppression yet is negative | `DIAGNOSTIC-NUMERIC`; correction for Paper 46 §28.3 |

FATAL rule clean; no sign claimed for ζ beyond `log 2`.

## 2. Reading
The symbol-level Φ_N is the right closed form of "how the primes pay" (bands of `cos(τ log n)`), but it cannot be turned into a proof
by uncertainty alone: `N_T` extends to `τ ≍ e^{2T}` (the same prime scale as the clearing height of R153_014), and the concentration
budget of `P_T` is an order of magnitude too small already at `½log3`. Positivity is a cancellation *across* the wells, which only the
full Krein positive-definiteness of the kernel on `[−2T,2T]` expresses. The corpus's ES-14 (Kreĭn extensions, ABANDONED: existence of
some extension does not identify the arithmetic kernel) applies verbatim to the uniform version. The stepwise version — whether the atom
`w_N` at `log N` lies inside the Krein-admissible band determined by the kernel on `[0, log N)` — is new as a *computation* and would
explain "critical at `log 2`" as "`w_3` at the edge of its band"; its uniform version is RH and it is not a route to the sign.

## 3. Decision
Round 5 closed, negative. Phase 153 closed; row D unchanged. Open added: (P153.14) stepwise Krein band at `N = 3, 4, 5` (measurement only,
owner's call); (P153.15) `R(T_c) = 1` coincidence with the `c(T)` peak; Paper 46 §28.3 to receive the depth correction of T5.
