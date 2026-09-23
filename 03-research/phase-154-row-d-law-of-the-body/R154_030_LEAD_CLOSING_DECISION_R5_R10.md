# R154.030 — Lead closing decision, phase 154 rounds 5–10 (the two-prime step). Date 2026-09-21.

## 1. Theorems of record added in rounds 5–10 (labels after hostile audit)
| id | statement | label |
|---|---|---|
| F1 / D2.3 (two-frequency form) | periodic block rows for lattice ν; the prime term needs no periodicity; the "incommensurability obstruction" never existed | `PROVED` (⟸ only) |
| F3 | second-order Taylor branch-and-bound; verification cost `∝ target^{−1/2}`; ½log3 bound raised to `8.8577·10⁻⁵` (same certificate as round 4, better verification) | `PROVED` |
| Lemma T / Prop. T0 / Cor. T1, T2 | exponential and Laguerre columns outside the window: exact transforms `Re[e^{2iTτ}k!/(s−iτ)^{k+1}]`, bound `k!/(s²+τ²)^{(k+1)/2}`, single monotone tail row; tail cost **linear** in ℓ¹ (not removed; useless for atomic classes) | `PROVED` |
| Theorem E | the exponential class exhausts the dual sup (`= λ_min`) | `PROVED` |
| Identity M | `σ_T + ν̂_K = m(0) + c_K + ∫_0^{2T}(1−cos τu)K − Σv_n cos(τ log n)`, `ν_K = ½K·1_{|u|≥2T} = 2e^{−T}ν_{½,0}`: the Lévy tail outside the window band-limits the symbol; privileged scale `s = ½` | `PROVED` (identity) |
| Lemma W | the two primitivity moments are `Q₀ = AB`, `Q₁ = A′B − AB′`; the moment map of the relaxed primal has 0 in its interior (witness `(1,0,0,∓1)` after repair) | `PROVED` (repaired) |
| Lemma V′ | mass-vs-value exchange on the primitive relaxation is exactly `Θ(log R)`: no rate lemma uniform in `R` exists; class-dependent rate lemmas untouched | `PROVED` (scope restricted) |
| Hybrid Lemma | lattice atoms + smooth columns certified jointly (exact rows for `k < N`, monotone caps at `k = N`) | `PROVED` |
| Theorem K | support bound `τ_c ≥ πN/(e·u_max)`; not a rate | `PROVED` (as support bound) |
| Prop. X | the canonical column's tail charge at `N = 2` exceeds the deficit at 0.58; effect on the certificate value | arithmetic `PROVED`; conclusion `UNRESOLVED` |
| Refutations | clustering (round 8); shape transfer within a contact set (round 6); lead's incommensurability hypothesis (round 7); calibration of `M_crit` (round 7); "tail solved / wall gone" (round 9) | `REFUTED`/`WITHDRAWN` |

Endpoint of record unchanged: `λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵` (Theorem C, F3-verified). Nothing certified at `T = 0.58` (best `≥ −3.1802·10⁻³`).

## 2. Diagnosis of the two-prime step (honest)
The tail is mathematically finished: with F1 for atoms and Lemma T for columns, certificates can be verified on a bounded range. What
remains at `T = 0.58` is a **value problem**: the class of finitely many atoms/columns must reach within `2.2·10⁻⁴` of `λ_min`, and (i) no
rate theorem can predict the needed size (Lemma V′), (ii) the LP solver at the needed size returned void results, (iii) every lever tried
(more atoms, clustering, smooth columns, hybrid at `N = 2`) either failed or is unresolved, and the licensed remedy (`N ≥ 6` blocks) has
logarithmic return. This is a computation with unfavourable scaling, not a mathematical gap; and it cannot be run on the owner's machine.
The uniform route (all `T`) is closed by the doubly exponential growth of `τ₁(T)`.

## 3. What would settle it
- **Computation elsewhere**: the hybrid LP with `N ≥ 6`, high-precision solver (or exact rational post-processing), then F3 verification —
  hours on a workstation. Not authorised here.
- **Mathematics**: a class-dependent value bound `c(class) ≥ λ_min − D(class)` (the only kind Lemma V′ leaves open). No idea in hand.

## 4. Decision
Rounds 5–10 closed. Phase 154's deliverables of record: R154_012 (as amended), R154_021, R154_023, this document. Row D: the dual theory
(Theorems A, O, D1, E), the first certificate with a prime (Theorem C), the tail theory (F1, T, Hybrid), and the negative rate theorem (V′)
are the phase's contribution. The global sign is unchanged. Owner's decisions: (a) write-up (Paper 47) after reading Zhu, Groskin, Suzuki,
Bombieri 2000, Yoshida 1992; (b) whether to fund the `N ≥ 6` computation off-machine; (c) whether to open a pure-math phase on
class-dependent value bounds.
