# R155.045 — Audit of round 6a (`R155_044`, `scripts/r6a/`)

*Reran `r6a_02_rule.py` (0.9 s): output **byte-identical** to the archived
`r6a_02.json`. `r6a_01.json` audited as data (declared ≈150 s; the note's "≈2.5 min total"
and the `scripts/r6a/README.md` per-script timings are **declared correctly**).*

**Verdict: ACCEPT with three corrections (one mathematical, two of label). No claim about `ζ`
is affected. Endpoint of record unchanged.**

---

## §1 Prop N1 — `PROVED`, but the written kernel is divergent (`R155_044:84–86`)

The conclusion is right, the display is not. `K(u)=u^{-1}+O(1)` (`lem:K`), so
`∫₀^{2T}K = +∞` and the kernel `(C₀+∫₀^{2T}K)δ(x−y) − K(|x−y|)` **does not exist**: both terms
diverge. The correct object is the form, not the kernel. For `F ∈ L²(−T,T)` extended by zero,
`h = F⋆F̃`, `thm:S` gives

`Γ_T(F) = C₀‖F‖² + ∫_ℝ K(|u|)(h(0)−h(u))du/2·2 = C₀‖F‖² + ½∫∫_{I_T²}K(|x−y|)|F(x)−F(y)|²dxdy + ∫_{I_T}κ(x)|F(x)|²dx`,
`κ(x) = ∫_{|y|>T}K(|x−y|)dy < ∞`,

i.e. a **regular Dirichlet form of pure-jump type with killing** `κ` and jump density `K ≥ 0`
(the `u→0` divergence is absorbed by `|F(x)−F(y)|² = O(|x−y|²)` on the form domain). Beurling–Deny
then gives Markovian, hence positivity-preserving, `e^{−tΓ_T}`; `K > 0` everywhere gives
irreducibility, hence positivity-**improving**; Perron–Frobenius gives a simple, a.e. strictly
positive ground state. One hypothesis is still missing from the note: that the bottom is an
**eigenvalue** — it is, since the form domain embeds compactly in `L²(I_T)` (`m(τ)→∞`), so the
resolvent is compact. **Required edit:** replace the `cδ − K` kernel line by the form display +
compactness remark. Label `PROVED` stands after that edit.

## §2 Prop N2 — `PROVED`, one hypothesis to state (`R155_044:89–99`)

`{e^{t/2},e^{−t/2}}` is a Chebyshev system of order 2 (`c₁e^{t/2}+c₂e^{−t/2}` vanishes only where
`e^t = −c₂/c₁`: at most one zero) ✓; the duality proof is correct and does not need continuity —
but "sign change" must be defined for `F ∈ L²`: *`F` has at most one sign change* := `∃t₀` with
`F ≥ 0` a.e. on `(−T,t₀)` and `F ≤ 0` a.e. on `(t₀,T)` (or the reverse); the product argument is
then exactly valid, and the degenerate case `F` of one sign a.e. is the `t₀ = ±T` endpoint. Add
that sentence. The supersession of the `REFUTED` line of `R155_039 §3.2` is fair.

## §3 Theorem N3 — split the label (`R155_044:124–141`, `:241`)

Proved and correct: completely monotone ⇒ log-convex (Cauchy–Schwarz on the representing
measure) ✓; Schoenberg `PF₂ ⟺ log-concave` ✓; hence `K(|·|) ∉ PF₂` ✓. **This is a theorem about
`K`, not an impossibility theorem about oscillation.** The operator is `Γ_T = c − K∗`, whose
relevant TP object is the semigroup `p_t`, not `K`; so the honest statement of the second half is
*"the direct Karlin route through the kernel of `A_∞` does not apply"* — a **route closure**, not
a proof that no variation-diminishing structure exists. The note says this in its *Scope*
paragraph but `§0.2` ("the oscillation theorem itself is CLOSED NEGATIVE") and the `§6` label
overstate it; `t ≥ 1` is admitted OPEN two lines later, which contradicts "closed".
The semigroup half (`:132–134`) is **not proved**: `m(τ) = log τ + O(1)` is a bounded *error*,
so `e^{−t(m−C₀)}` is `τ^{−t}` only up to a factor `e^{O(t)}` that is not asymptotically constant;
deducing `p_t(x) ≍ |x|^{t−1}` needs a Tauberian/monotone-density argument that is not given.
**Required:** label the `p_t` claim **`HEURISTIC`**, and the Karlin conclusion
**`PROVED` (as non-applicability of the TP hypothesis) / route closed, not impossibility**.

## §4 Sign-rule statistics — **all confirmed** (`R155_044:157–171`)

Rerun of `r6a_02_rule.py` reproduces `r6a_02.json` exactly. Against the JSON:
`N=36`, `n=2`: `38/64 = 59 %`, `30/42 = 71 %`, `26/32 = 81 %`, `22/22 = 100 %` at `|J| ≥ 0.10`,
mass `0.9004` ✓; `n=3`: `50/64`, `38/40 = 95 %`, `32/32`, `22/22`, mass `0.9587` ✓.
`N=18`: `41/64 = 64 %`, `49/64 = 77 %`, masses `0.8869/0.9313` ✓. `T = 0.65`: `46/64 = 72 %`,
`51/64 = 80 %`, `100 %` above `0.05`, masses `0.9383/0.9539` ✓. Failure means
`0.0140–0.0285` vs overall `0.0697–0.1135` ✓ (note's `0.014–0.028` / `0.07–0.11`).
Cross-check `max|(−Σv_nJ_n) − π_ij| = 1.746·10⁻⁵` at `N=36` ✓ (`4.30·10⁻⁴` at `N=18`,
`1.51·10⁻³` at `T=0.65`, the last not quoted in the note — add it or drop the claim for that run).
*Nit:* `§0.3` says mass `89–96 %`, `§3` says `90–96 %`; the true range over all three runs is
`88.7–95.9 %`. Use one range. Labels `DIAGNOSTIC` correct. The `N=18`/`N=36` spectra disagree
from `e₁₁` on (`1.613` vs `1.504`), correctly flagged as resolution-limited.

## §5 Theorem N4 — the bound is right, **the index bookkeeping does not prove the even statement**

`λ_j(A_∞|P_T) ≤ λ_{j+2}(Γ_T)` (codim 2) ✓; `λ_{2k+3}(Γ_T) ≤ C₀+φ(((2k+3)π/2T)²)` by min–max on
the first `2k+3` Dirichlet modes with `‖F′‖² ≤ (jπ/2T)²‖F‖²` and Jensen on the concave `φ`
(`thm:S`) ✓; `= m((2k+3)π/2T)` ✓. It is the `k`-th case of `prop:arch`(ii) (`k=0` is exactly
`C₀+φ((3π/2T)²)`), which is a good consistency check.
**But** `λ_{2k+1}` here is the `(2k+1)`-st eigenvalue of the *whole* restricted operator; the note
then reads `N*` as a count of **even** modes (`§0.4`, `§4`, and the Galerkin comparison). That
identification needs parity alternation of the spectrum of `A_∞|P_T`, which is nowhere proved,
and the inequality runs the wrong way (`#{all ≤ 𝖠_T} ≥ #{even ≤ 𝖠_T}`).
**Fix (available, cleaner, same constant):** `A_∞` commutes with parity; on the *even* part of
`P_T` the two Tate constraints coincide, so `P_T^{even}` has codimension **1** in `L²_{even}`.
Take the even Dirichlet modes `cos((2j+1)πx/2T)`, `j = 0,…,k+1` (`k+2` of them, top frequency
`(2k+3)π/2T`), minus one constraint ⇒ a `(k+1)`-dimensional trial space in `P_T^{even}` ⇒
`λ^{even}_{k+1}(A_∞|P_T) ≤ m((2k+3)π/2T)`. This is exactly the even statement `§4` wants and
exactly the index the script counts. **Required edit** to the proof of N4.

## §6 Arena corollary — count correct, **closed form off by one**; rigour recoverable

The script is right, the note's formula is not. `m(τ) ≤ 𝖠_T ⇔ (2k+3)π/2T ≤ τ_*` gives
`k ≤ Tτ_*/π − 3/2`, hence `N* ≥ ⌊Tτ_*/π − 3/2⌋ + 1 = ⌊Tτ_*/π − 1/2⌋`, **not**
`⌊Tτ_*/π − 1⌋` (`R155_044:191–192`) nor `2Te^{𝖠_T} − 1` (`:247`). At `T = log2` both give `12`;
at `T = ½log3` the note's formula gives **`1`** while the true count (and `r6a_02.json`) is `2`.
**Required edit:** use `⌊Tτ_*/π − 1/2⌋`.
Rigour: `τ_* = 2πe^{𝖠_T}(1+o(1))` is asymptotic and cannot carry a `PROVED` label at these two
windows; but the counts survive with `lem:mbounds`(ii) applied at exact `τ`, which this audit did:
at `T = log2`, `m(τ_{11}) ≤ log(56.655/2π)+1/τ+½log(1+1/4τ²) = 2.2168 ≤ 𝖠_T = 2.24889` (so
`N* ≥ 12`) and `m(τ_{12}) ≥ 2.2596 > 𝖠_T` (so 12 is sharp for the ceiling); at `T = ½log3`,
`m(τ_0) ≤ 0.4297`, `m(τ_1) ≤ 0.8928 ≤ 𝖠_T = 0.98026` (so `N* ≥ 2`), `m(τ_2) ≥ 1.1075 > 𝖠_T`.
With those two lines the corollary is genuinely `PROVED`; without them it is `DIAGNOSTIC`.
Galerkin `N=60` finding exactly `12` (`r6a_01.json:growth.k_with_lam_le_2249 = 12`,
`λ₁₃^{even} = 2.2568 > 𝖠_T`) ✓ `DIAGNOSTIC`, and consistent.
**Theorem N5:** `𝖠_T = Σ_{n<e^{2T}}2Λ(n)n^{−1/2} ~ 4e^{T}` by PNT + partial summation ✓;
`N* ≥ exp(4e^T(1+o(1)))` ✓. The prefactor is `2Te^{𝖠_T}`, not the `4T·e^{𝖠_T}` of `:44`/`:200`
(harmless inside the `exp`, but inconsistent with the note's own `§6` line — unify).

## §7 Conclusion (§5) and residual overstatements

Fair. "A nodal criterion for the full `S_even` is not attainable by this route" is supported by
N4+N5 plus the equidistribution reading, and is correctly labelled as a route closure, not as an
impossibility for all methods; keeping the sign rule as a diagnostic law is right; naming the
explicit prolate concentration floor (`R155_039 §2.4`) as the live problem is consistent with
`R155_043`. Two residual overstatements to fix: `§0.2` "CLOSED NEGATIVE" (see §3 above) and the
`§6` line "Conjecture N-Sturm … base case `PROVED`" (`:242`) — N1+N2 prove `F*` has **at least**
one nodal pair, not exactly one, so the base case `k=1` of *exactness* is **not** proved. Write
"lower bound of the base case `PROVED`".

## §8 Readiness of the Paper 47 proposals

| proposal | verdict |
|---|---|
| Prop N2 → after `prop:arch` | **READY** once the `L²` sign-change definition is stated. Three lines, correct, and it pre-empts the reader's expectation that `F*` be a positive bump. |
| Thm N4 + arena → remark after `prop:shifts`, strengthening `rem:galerkin` | **READY AFTER EDITS**: the even-subspace proof of §5 above, the corrected `⌊Tτ_*/π − 1/2⌋`, and the two `lem:mbounds` verifications of §6. It then converts the `\textsc{diagnostic}` paragraph at `main.tex:2590–2598` ("not captured by any fixed number of archimedean modes") into a theorem with an explicit count — the single strongest upgrade available here. Quote `N* ≥ 12` / `N* ≥ 2` as proved, the Galerkin `12` as diagnostic. |
| Thm N3 → closing no-go of §2 | **READY for the `K` half** (one paragraph: complete monotonicity gives every ceiling in the paper *and* forbids `PF₂` — the same hypothesis, two opposite consequences). **Drop or explicitly label `heuristic`** the `p_t ≍ |x|^{t−1}` sentence; say "does not apply", not "is impossible". |
| Sturm conjecture, §3 sign rule | correctly **not proposed**. |

**Labels of record after the required edits:** N1 `PROVED`, N2 `PROVED`, N3 `PROVED` (as
non-`PF₂`; route closure, `p_t` half `HEURISTIC`, `t ≥ 1` `OPEN`), N-Sturm `CONJECTURE`
(lower-bound base case proved), N4 `PROVED` (even-subspace proof), arena `PROVED` (with the
`lem:mbounds` lines), N5 `PROVED`, P8 closed as a route / kept as diagnostic — unchanged.
Row-D label unchanged; no sign for `ζ`; no claim beyond `log 2`.
