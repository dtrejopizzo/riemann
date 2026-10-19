# R154.021 — Closing decision, round 7 (pure mathematics: approximation theory of the certificate).

| item | statement | label |
|---|---|---|
| Reformulation | Weil positivity at support `T` = one-sided majorant problem with spectral gap `2T` (Beurling–Selberg with the band condition complemented; Carneiro–Littmann vanishing condition ↔ our two multipliers). No rate theory exists on the gapped side (literature; three arXiv ids to verify). | `PROVED` (identity) / literature `DIAGNOSTIC` |
| **Theorem K** | relaxed-feasible `μ` with `supp ⊆ [−τ_c,τ_c]` and `N` forced zeros of `μ̌` in `(0,u_max]` ⇒ `τ_c ≥ πN/(e·u_max)` (constant correct: `π/2` from `|Λ| ≤ e^{τ_c|Im z|}`, factor 2 from evenness; Cartwright/Levinson gives sharp density constant 1, so thresholds uncertain by a factor up to `e`). **Not a rate theorem**: bounds the support radius, not the value (Fejér witness). Corollary K0 (auditor): the relaxed minimiser is atomic with `≤ N+3` atoms, so compact support is automatic. | `PROVED` (as a support bound); "rate", "`M_crit`", "`α = 1` deficit law" `WITHDRAWN` (heuristic at best) |
| Calibration of `M_crit` | cited LP values that R154_010 itself declares fictitious; no crossing of `c(M)` has ever been measured | `REFUTED` |
| Second contact | the off-lattice `log 3` hypothesis (earlier) is **refuted**: prime atoms lie inside the window where `ν ≡ 0`; the cost of the second contact is the jump of `τ₁` (16.7 → 59.5). The `(3.75)²` inference | `PROVED` (refutation) / inference `WITHDRAWN` |
| Remedy | cluster the atoms on `[2T, V]` — only the density enters the support bound; the tail lemma F1 survives with `P′ = 2π/h′`; F1's slack (`1.8·10⁻²`) may be the real wall at `log 2` | theorem-candidate `OPEN`; **single falsifier LP at 0.58 authorised** (≤ 15 min, one process, matched control) |
| Proposition E | multiplying Theorem W by `conj F̂_★` destroys the gap (`supp(H⋆F̃_★) ⊆ [0,∞)`); "no analytic near-certificate exists" | `PROVED` (identity) / non-existence `DOWNGRADE` (one route) |
| Proposition P | `β₀ = 2` is the unique multiplier restoring the polar terms; the limit `β₀ → 2` is `OPEN`; the recorded values are at different `T`, so there is neither convergence nor drift on record | `PROVED` (identity); R154_012 "polar term" row amended accordingly |
| (P154.6) | Turán/Remez stability is the wrong missing lemma; the needed one is mass-vs-value (exchange rate logarithmic, `R ≳ τ₁e^{B/ε}`) | `OPEN`, reformulated |

FATAL rule clean; nothing certified this round; the endpoint remains `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (R5a).

**Reading.** The pure-math round removed a wrong hypothesis of the earlier (incommensurability), produced the exact approximation-theoretic
frame (spectral-gap majorants) and a correct support bound, and failed to produce a rate: the value/mass exchange is the missing lemma and it
is logarithmic, i.e. unfavourable. As a uniform route (all `T`) this is closed: `τ₁` grows doubly exponentially in `T` and the certificate
class must grow with it. As a finite construction, one affordable falsifiable test remains (clustered atoms at 0.58).

**Amendment to R154_012 §1 "The polar term" row:** replace the limit claim by "`β₀ = 2` is the unique multiplier restoring the two polar
terms (Prop. P, identity). Whether the optimal duals converge to it as the class exhausts is OPEN; the recorded `β₀` values (2.0026 at
`½log3`, 2.0400 at 0.58) are at different `T` and do not measure a limit."
