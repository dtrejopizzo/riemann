# R144.000 — Blueprint, phase 144: the fixed-index inequality

set; transfer 12.3-B4 unconditional; `(b′)_{B4}` true under RH; index-local RH content; `Ξ_a` fails at a
fixed finite index; auditor's target), `R143_001` §D.34 (Definitions of `B4^{g,0}`, `t_n`, Thms D.34.5,
D.34.8, D.34.9′, D.34.10, D.34.16, Remark D.34.16c), `R141_001` §D.26 (traces; polar term of
`I_∞(E, τ_{log n}g)`), `R142_001` §D.31 (Lemma D.31.4 cosh bound; witness family), Paper 46 §§11–12.*

Standing rules as before. FATAL rule: a proof that `t_m(E) ≥ 0` for all `E ∈ S_0` and **all** `m` would,
with Thm D.34.8, prove RH — so a proof at a fixed `m` must be checked against `Ξ_a` at the index where
`Ξ_a` fails, and must name the A3-line (two polar exponents). Any argument valid verbatim for `Ξ_a` at its
failing index is wrong.

## The object
For admissible `g` (fix `g = g_λ = K + λh` of Lemma D.34.9′ unless a better choice is argued), `E ∈ D^W`,
`S_0 := {deg E > 0, R(E) = ½I_∞(E,E) − ¼deg E > 0}`, and a fixed index `m ≥ 1`:

    (P_m):  t_m(E) := I_∞(E, τ_{log m} g) ≥ 0   for all E ∈ S_0.

Explicit formula: `t_m(E) = m^{½}Φ_g(1)·b + m^{−½}Φ_g(0)·a − Σ_ρ Φ_E(ρ)Φ_g(1−ρ) m^{½−ρ}` with `b = Φ_E(0)`,
`a = Φ_E(1)` (check the pairing against D.26.1). Arithmetic side: `t_m(E) = PRIME − ARCH` of
`E ⋆ (τ_{log m}g)^∨` (Lemma 11.4a). RH ⟺ `(P_m)` for all `m` (R143_005 §2). Under RH each `(P_m)` holds
(Thm D.34.10). For `Ξ_a`, `(P_m)` fails at some fixed `m` (Remark D.34.16c).

## D.37 — The failing index for `Ξ_a`
1. From Remark D.34.16c: the family `E_r = rF₊ + K_a` with the sign of `r` chosen; compute the traces
   `t^{(a)}_m(E_r)` exactly (polar part with four exponents `m^{½−p}`, `p ∈ {−a,a,1−a,1+a}`, weighted by
   `Ξ_a(p)`; zero part), find the **smallest** `m` at which `t^{(a)}_m(E_r) < 0` for suitable `r`, as a
   function of `a` and of the test class `g_a`. Is it `m = 1` (the diagonal trace `I_∞(E,g)`)? `m = 2`?
   Prove the minimal index or give a certified value for a specific `a` (e.g. `a = ¼`).
2. Identify **why** it fails there: the polar part for `Ξ_a` is `Σ_p Ξ_a(p)Φ_{g_a}(1−p)Φ_E(p) m^{½−p}`,
   whose four terms with exponents `±(½±a)` cannot be bounded below by a constant times `√(product)`
   uniformly in `m` (no AM–GM floor); exhibit the `m`-dependence that makes it drop below the zero part.
   State this as a lemma about polar exponent sets: *a two-point equimodular set `{½−θ, ½+θ}` has a uniform
   AM–GM floor `2√(·)`; a four-point set with two moduli does not* — the A3-line, made precise.

## D.38 — The `ξ`-inequality `(P_m)` at the smallest failing index
1. Write `(P_m)` for `ξ` at that `m` (and at `m = 1` regardless): `m^{½}Φ_g(1)b + m^{−½}Φ_g(0)a ≥
   Σ_ρ Φ_E(ρ)Φ_g(1−ρ)m^{½−ρ}` for all `E ∈ S_0`. The left side is `≥ 2√(abΦ_g(0)Φ_g(1))` (AM–GM, the floor
   `ξ` has and `Ξ_a` lacks). The right side, **unconditionally**, is `Σ_ρ Φ_E(ρ)Φ_g(1−ρ)m^{½−ρ}`, with
   `|m^{½−ρ}| = m^{½−Re ρ} ≤ m^{½}` (since `Re ρ > 0`): so `|zero part| ≤ m^{½}Σ_ρ|Φ_E(ρ)||Φ_g(1−ρ)|`. The
   question is whether `R(E) > 0` controls `Σ_ρ|Φ_E(ρ)||Φ_g(1−ρ)|` **without** RH. Under RH,
   `W(E) = Σ|Φ_E(ρ)|² < 2ab` does it via Cauchy–Schwarz. Unconditionally `W(E) = Σ_ρ Φ_E(ρ)Φ_E(1−ρ)` is not a
   sum of squares. **Task:** determine exactly what `R(E) > 0` gives unconditionally about the zero data of
   `E` (e.g. via the Lemma D.31.4-type bounds, via Thm 11.14's exact constant, via the D.26 necessary
   conditions), and whether it suffices for `(P_m)` at the fixed `m`. Three possible outcomes, each a
   result: (i) `(P_m)` unconditional for `ξ` at that `m` (then check `Ξ_a` at its failing index — the proof
   must break at the A3-line; if it does not, the proof is wrong); (ii) `(P_m)` at fixed `m` is equivalent
   to RH already (the clause does not decompose by index — prove it: exhibit, assuming an off-line zero,
   an `E ∈ S_0` with `t_m(E) < 0` at that fixed `m`; this is a Landau/Theorem-F-type construction at one
   index); (iii) OPEN with the exact missing estimate.
2. **The head as a finite system.** If `(P_m)` at a single index is not decidable, consider the head
   `{(P_m) : m < N}` on a degree slice `{R > 0, 0 < deg ≤ d}` under the RH-uniform bound `N ≤ 64d²`
   (D.34.16(iv)): under RH the whole content of RH on the slice is a finite system of `≤ 64d²` linear
   inequalities in the traces over a quadratic region — write it out for `d = 1` (the slice containing
   `K` and the classes `rF + K` that Thm 12.3-B4 actually uses: check their degrees) and determine which of
   the `≤ 64` inequalities are unconditional and which carry the zero information. **Warning:** the bound
   `N ≤ 64d²` is itself RH-conditional; unconditionally the slice's head is finite per class but not
   uniformly — say so at every use.
3. **The diagonal trace `m = 1`:** `t_1(E) = I_∞(E, g)`. `(P_1)` says: `R(E) > 0, deg E > 0 ⟹ I_∞(E,g) ≥ 0`
   for the fixed admissible `g`. With `g = K + λh` this is `½deg E + λI_∞(E,h) ≥ 0`, i.e.
   `I_∞(E,h) ≥ −deg E/(2λ)` on `S_0` — a Thm-11.14-type bound **on `S_0` instead of on the effective cone**.
   Is it unconditional? (Thm 11.14 gives it on effective classes with the constant `C_h`; on `S_0` the
   question is whether `R > 0` gives a bounded-density constant — exactly the (★)-question of phase 142
   in the direction that was NOT refuted: there `(★)` failed for the *effective* clause because
   `C_{F₀}` was too small by `s₁`; here the constant is `1/(2λ)`, which is *large*. Compute whether `(P_1)`
   holds unconditionally on `S_0` for `g_λ` with small `λ`; if yes, that is the first unconditional
   fixed-index positivity and D.37.2 must be checked against `Ξ_a` at `m = 1`.)

## D.39 — Synthesis input
One page: the failing index for `Ξ_a` and the lemma on polar exponent sets; the status of `(P_m)` for `ξ`
at that index and at `m = 1` (unconditional / ⟺ RH / OPEN); what the head looks like on the `d = 1` slice;
recommendation for phase 145.

## Deliverables and rounds
`R144_001_ROUND1.md` (D.37; D.38 items 1–3 with the decisions; D.39; corpus check per idea — grep
for "fixed index", "single trace", "diagonal trace", "I_∞(E,g) ≥ 0", "bounded density on" in 03-research;
paper-facing; open list; label), README; audit `R144_002`, repairs, confirmation, `R144_005`.
Scripts only to certify the `Ξ_a` failing index for a specific `a` (`--fast`, margin).

## Warnings
* Every positivity claim for `ξ` at a fixed index must be re-run for `Ξ_a` at its failing index; if it
  survives there, it is wrong.
* Do not use `N ≤ 64d²` as if unconditional.
* `g = K + λh` has `Φ_g(ρ) = λΦ_h(ρ)`: the zero part scales with `λ`, the polar floor does not — make the
  `λ`-dependence explicit in every inequality; do not let a `λ → 0` limit prove something for free
  (the Baire condition needs `λ > 0`, and `λ → 0` makes `g → K`, which is inadmissible).
