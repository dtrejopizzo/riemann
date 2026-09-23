# R149.002 — Hostile audit of `R149_001_BUILDER_ROUND1.md`

*Auditor: Opus 5 (senior analytic number theory reading), commissioned by the lead 2026-09-19.
Inputs: `R149_000_LEAD_BLUEPRINT.md`, `R149_001_BUILDER_ROUND1.md`, `HANDOFF-2026-09-15-FASE-149.md`.
Section numbers refer to `R149_001`. Labels: STANDS / DOWNGRADE / WITHDRAW.*

---

## 0. Verdict table

| item | verdict | single most damaging attack |
|---|---|---|
| **D.59** (extraction) | **STANDS**, with the (E)/(C′) bookkeeping repaired | It is `Ξ_a`-uniform (D.59.4, D.63.1) and therefore a Hölder inequality `‖·‖_{ℓ^∞} ≤ ‖·‖_{ℓ^{2k}}`, not a transfer of Weil I 3.2. Calling the Farey family "the family" and `α=0` "the fibre" is analogy; any paper must open with that. Remark D.59.0b's retreat to (C′) is unnecessary for (E) and unproved for `q_0>1`. |
| **D.60** (kill test, W-H) | **STANDS**; **DOWNGRADE** the scope of D.60.7 and of "nothing unconditional for `k ≥ 2`" | The `2k`-th-power leg of D.60.7(ii) uses the counterexamples' *constructed* size as if it were an unconditional upper bound at `q ≍ log log N`; unconditionally only Siegel–Walfisz is available there. The de la Bretèche–Fiorilli / Harper–Soundararajan **unconditional Ω-results for even moments were never compared against `H(k,c)`** — the one check that could refute the hypothesis from below was not run. |
| **D.61** (coinvariant block, fifth wall) | **DOWNGRADE** — the mathematics stands, the headline does not | "Nothing known transports between the two squares" is false as written: `V_Λ(x;q) = φ(q)^{−1}Σ_{χ≠χ_0}|ψ(x,χ)|²` is an exact transport at every `q`, used by the document itself in §3.6. The wall survives only as *no transport of the polar/positivity structure*; at the second-moment layer it is the Goldston–Montgomery bridge, crossable (RH-conditionally) and sign-free. D.61.7's constant-level identification `xQκ(0)` is off by `log 2π + 1`. |
| **D.62 / (P149)** | **STANDS as a problem; DOWNGRADE the claim that it is "the object to create"** | Prop. D.62.1 shows `H(k,c)` ⟺ a `2k`-fold additive-energy bound for `Λ − M_Q` with square-root cancellation. For `k=2` that is the Hardy–Littlewood pair correlation on average with square-root error — an existing, named open problem. (P149) is the `k`-tuple conjecture in Deligne costume; its five required properties are a wish-list for a `Q`-analogue of Katz equidistribution (Keating–Rudnick over the wrong base). D.62.2 cites the wrong theorem for the sharp half. |

**Row D: no label, no sign** — concurred. Nothing in phase 149 touches a sign; §4.5 concedes the additive pairing is positive-definite, hence index-free (fourth corpus instance of "positivity on the square constrains nothing"). The honest headline of the phase is D.61.8/D.61.9 — **exponents add on the additive square, subtract on the multiplicative square** — not D.61.10 as worded.

---

## 1. D.59 — digest and audit

**What is proved.** With `w ∈ C_c^∞`, `w ≥ 0`, `supp w ⊆ [1,2]`, `Q = N^c`, `M_Q(n) = Σ_{q≤Q}(μ(q)/φ(q))c_q(n)`, `b_n = (Λ(n)−M_Q(n))w(n/N)`, `S̃(α) = Σ b_n e(nα)`: if `H(k,c): M_{2k} ≤ C_k(log N)^{B_k}Q²N^k`, then since `a/q = 0` is inside the Farey family, `|S̃(0)|^{2k} ≤ M_{2k}`, so `|S̃(0)| ≤ N^{1/2+c/k+o(1)}`; with (E) this is `ψ_w(N) − Nŵ(0)`. Correct, three lines, and correctly self-labelled "folklore chain, first stated here". Corrections C2, C3 (Selberg majorant fails (E) with PNT-strength error; `M ≡ 1` fails for `k≥2` since `Σ_q μ²(q)φ(q)^{1−2k}` converges) check out. `M_Q` = Vaughan's `ρ(x;q,a)`, correctly attributed. The family `w_θ` (D.59.1a) and the Mellin identity `∫ψ_{w_θ}(N)N^{−s−1}dN = (−ζ'/ζ)(s)W(s+θ)` are right; `W` vanishing on a horizontal line forces `W ≡ 0`, contradicting `W(1)>0`. Bernstein (D.59.2) correct.

**Gaps flagged.**
1. **(C) vs (C′) muddled, in the wrong place.** D.59.1 uses **only (E)**, not (C). (E) is not in danger at `c ≥ 1/2`: at `q_0 = 1` the frequencies are `b/q` with `‖b/q‖ ≥ 1/Q`, so `N‖β‖ ≥ N^{1−c} → ∞` for every `c<1`; Poisson gives `O_A(QN^{−A})` throughout. The `Q^{−2}` spacing arises only for `q_0>1`, where the theorem does not need it. The claim that (C′) "follows from the large sieve applied to `M_Q`" is asserted, not computed. **Repair:** standalone (E)-lemma for all `c<1`; demote (C)/(C′) to a plausibility clause for `H(k,c)`, proved or labelled `OPEN`. Nothing downstream breaks.
2. **Constants.** `C_k(log N)^{B_k}` is decorative for the stated conclusion: for fixed `k`, `C_k^{1/2k}(log N)^{B_k/2k} = N^{o(1)}`. Growth in `k` matters only for a `k`-uniform conclusion (`k = k(N)`): one needs `log C_k + B_k log log N = o(k log N)`, which Gaussian `C_k = (2k−1)!!`, `B_k = O(k)` satisfies with `k ≍ log N/log log N`, giving `ψ(N)−N ≪ N^{1/2}exp(O(log N/log log N))`. The "Gaussian moments" framing is stronger than needed for `N^{1/2+ε}` and exactly what is needed for RH-sharp `N^{1/2}log²N`. Say so.
3. **D.59 is not a theorem about primes.** D.59.4 and D.63.1 prove this. "Four of Deligne's five ingredients present over `Z`" (§6.4) must be read as "one of them is a Hölder inequality".
4. **D.59.3 strictness.** ATRH ⟹ `ψ_w(N,χ) ≪ q^{1/2+ε}N^{1/2+ε}` uses finite Fourier inversion on the *uncentred* `S`; the `M_Q`-contribution `Σ_n M_Q(n)χ(n)w(n/N)` is not estimated (small by Ramanujan-sum orthogonality, but unwritten). Minor.

**Nothing in D.59 is wrong.**

## 2. D.60 — kill test, W-H, `k ≥ 2`

**W-H: agreed, with a caveat.** Attributions (Fiorilli–Martin JEMS 25 (2023); Hayani arXiv:2407.01045) correct. Legs (i)–(iii) of D.60.7 sound: counterexamples at `q ≍ log log x` / `Q ≤ √(log log x)`, an `N^{o(1)}` segment of `[1,N^c]`; contribution `N^{1+o(1)} = o(Q²N)`; mechanism Littlewood-type `Ω_±(x^{1/2}log log log x)`, RH-compatible. Hayani's "smoothing does not rescue Hooley" correctly imported. **Caveat:** leg (ii) at `2k`-th powers uses `|ψ(x,χ)|² ≪ x(log log log x)²` — the size of the *constructed* oscillation, not an unconditional bound at those `q`. Unconditionally only `|ψ(x,χ)| ≪ x exp(−c√log x)` is available, giving `Q_0²N^{2k}exp(−2kc√log N)`, not obviously `o(Q²N^k)`. **Rescope D.60.7** to: "the counterexample mechanism is RH-compatible and its contribution to `M_2` is negligible".

**"Nothing unconditional for `k ≥ 2`": right for upper bounds, sloppy as stated.** de la Bretèche–Fiorilli prove **unconditional Ω-results for all weighted even moments** and GRH lower bounds for moments of moments; Harper–Soundararajan give unconditional variance lower bounds of conjectured order for `x^{1/2+ε} ≤ Q ≤ x`. **The check not run:** do those Ω-results contradict `H(k,c)`? Reading: no — they are of Gaussian order, inside the `(log N)^{B_k}Q²N^k` budget — but the comparison must be performed; it is the one check that could fire the FATAL rule from the other side. Cheap to close.

**Further:** (a) Hooley VII conjectures higher moments only in the range `x(log x)^{−A} ≤ Q = o(x/log x)`, i.e. `c → 1`, exactly where D.60.0 makes the extraction vacuous for `k=1` and marginal for `k=2`: *the literature conjectures the hypothesis only where it is useless*. (b) The "sharp block at `c = 1/2`" is a `k=1` phenomenon; for `k ≥ 2` the hypothesis is both useful and open at every `c`. The executive-summary table needs a `k=1` header. (c) D.60.6 (restriction exponent saturated by major arcs, `∫|F|^r ≫ N^{r−1}Σ_{q≤Q_0}φ(q)^{1−r}`) is correct and the best technical observation in §3.

**FATAL rule:** independently confirmed — no chain produces a zero-free region.

## 3. D.61 — the fifth wall, sharpest form

**What stands.** D.61.8 (Landau useless additively: abscissa of `Σ R(n)n^{−s}` is the a-priori pole `s=2`, above every `ρ+ρ'`; Paper 46 Thm 17.14 works because the multiplicative pairing `ρ ↔ 1−ρ̄` puts the top pole at the critical value) and D.61.9 (additive nonnegativity comes from `Λ ≥ 0`, destroyed by twisting; `|ψ(x,χ)|² ≥ 0` is twist-stable). **Exponents add vs exponents subtract** is the phase's genuine idea.

**What is false as written.** "Nothing known transports between them." Plancherel on `(Z/q)^×` gives, for each `q`, `V_Λ(x;q) = φ(q)^{−1}Σ_{χ≠χ_0}|ψ(x,χ)|²`, the identity Fiorilli–Martin use and the document quotes in §3.6. The additive-square family moment at level `q` **is** a multiplicative-square moment, exactly, for every `q`.

**What genuinely does not cross** (correct statement of the wall): the identity is one of *counting functions at fixed `x`*, not of *Dirichlet series in `s`*. Three things fail to cross: (1) **polar structure** — the family sum `Σ_χ L(s,χ⊗χ̄)`-avatar has no Euler product and no functional equation, hence no a priori polar divisor; the additive side's polar divisor is a priori but dominated by `s=2`; (2) **positivity** — no object is simultaneously a square and has an a-priori polar divisor; (3) **`k ≥ 2`** — Fourier identity is Parseval (`k=1`); for `k≥2` additive energy and `2k`-th moments of `ψ_χ` relate only by Hölder, loss-making direction.

**The object that would identify the two squares over `Z`:** a Rankin–Selberg theory for the additive pencil — a meromorphic `D(s)` (or `D(s,s')`) whose coefficients are the pair correlations `C_2(d) = Σ_n b_n b̄_{n+d}`, which is (a) the diagonal of a genuine square (Landau applies) and (b) has polar divisor determined by `𝔖(d)`/`κ(d)` alone. Over `F_q` this is `L(U, F ⊗ F^∨, T)`. Over `Z`, `κ` and `𝔖` exist only as *densities*, not as *residues*. **The missing object is the promotion of the singular series from a density to a polar divisor** — sharper form of Doc 106's Lema Faltante 5.3; recommended as the phase's statement of the wall.

**Goldston–Montgomery in disguise?** Partly. Known partial transports: Hardy–Littlewood ⟹ Montgomery `F(α)` (Bogomolny–Keating for `n`-level); Goldston–Montgomery (short-interval variance ⟺ pair correlation, under RH); Montgomery–Soundararajan; Goldston–Suriajaya (2023, Fujii's error ↔ short-interval variance). **At the second-moment layer the fifth wall is the GM bridge, already crossable.** It transports second moments, RH-conditionally, sign-free (NG-B8); it does **not** transport positivity/index, `k ≥ 2`, or any polar/Landau structure. **Restate D.61.10:** "no transport of the polar/positivity structure; the moment-level transport is classical (Parseval over `χ`; Goldston–Montgomery), RH-conditional and sign-free."

**Smaller defects.** (a) D.61.7: `xQκ(0) = xQ log Q + C_0 xQ` vs Hooley's `xQ log Q − c_0 xQ`, `C_0 ≠ −c_0` (differ by `log 2π + 1`); the `(1+o(1))` hides a discrepancy of the order of Hooley I's whole content. (b) D.61.4 mixes `Q = ∞` (`κ(d) = d/φ(d)`) with finite level (`κ(0) = log Q + C_0`) in one statement. Closed form and `C_0` independently verified.

## 4. `H(2,c)` vs RH (D.62.2)

**Yes, `H(2,c)` ⟹ RH — but the sharp half is mis-cited.** `H(2,c)` forces `C_4(0) ≪ (log N)^{B_2}N²`; `∫_0^1|S̃|⁴ = Σ_d|(b*b)(d)|²`; Cauchy–Schwarz gives `Σ_{n≤N}|R̃(n)| ≪ N^{3/2+ε}`; since `M_Q` is zero-blind the zero term `H(x) = −2Σ_ρ x^{1+ρ}/(ρ(1+ρ))` is not absorbed, so `β>1/2` contributes `≫ x^{1+β}` — full RH by the Ω-argument. Right citation: **Granville, Funct. Approx. 37 (2007) Thm 1A + Corrigendum 38 (2008)**, with Fujii / Languasco–Zaccagnini for the converse. **Bhowmik–Ruzsa** Thm 2.1 gives only quasi-RH (`β < 1 − δ/6`; at `δ=1/2`, `β<11/12`). Repair: Bhowmik–Ruzsa = unconditional quasi-RH half; Granville+corrigendum = equivalence at exponent `3/2`. With that, "`H(2,c)` at or above RH" is an understatement (off-diagonal and `q`-uniformity are extra).

## 5. Minimum repairs before any of this is paper-facing

(i) standalone (E)-lemma, (C′) demoted or proved; (ii) D.60.7 rescoped; (iii) dlB–F / Harper–Soundararajan Ω-check run against `H(k,c)`; (iv) D.61.10 restated as *no transport of the polar/positivity structure*, citing Parseval and Goldston–Montgomery as the transports that exist and what they fail to carry; (v) D.62.2 citation corrected to Granville (2007)+Corrigendum (2008); (vi) Hooley's `c_0` verified in Crelle 274/275 (keep `CERTIFIED` until read).

## 6. Labels after audit (provisional until `R149_003`)

| item | R149_001 label | after audit |
|---|---|---|
| D.59.1 / D.59.1a / D.59.2 | PROVED (folklore chain) | **STANDS** — reword as Hölder, not Weil I 3.2 |
| D.59.3 | PROVED (equivalence) | STANDS; write the `M_Q` estimate |
| D.60.1–D.60.6 | PROVED | STANDS (add `k=1` header to the dichotomy) |
| D.60.7 | PROVED | **DOWNGRADE** scope (mechanism RH-compatible; `M_2` contribution negligible) |
| "nothing unconditional for `k≥2`" | IMPORTED | DOWNGRADE wording; run Ω-check |
| D.61.4–D.61.9 | PROVED / RESTATEMENT | STANDS (fix D.61.7 constant, split D.61.4 levels) |
| **D.61.10** | PROVED, finding of record | **DOWNGRADE** headline; restate as polar/positivity non-transport |
| D.62 (P149) | problem | STANDS as problem; **DOWNGRADE** "object to create" → "`k`-tuple conjecture in Deligne costume" |
| D.62.2 | PROVED | STANDS with corrected citation |
| D.63.1–3 | PROVED | STANDS |
