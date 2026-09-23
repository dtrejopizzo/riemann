# R149.005 — Lead closing decision, phase 149 (the additive pencil)

*Lead: Fable 5.1, 2026-09-19. Record: `R149_000` (blueprint), `R149_001` (round 1), `R149_002` (hostile audit),
`R149_003` (repairs, same day). Labels below are the labels of record; where `R149_003` and this table differ,
this table governs.*

## 1. Labels of record

| item | label | note |
|---|---|---|
| D.59.0a (model dichotomy; Vaughan's `M_Q` admissible) | PROVED / IMPORTED (attribution Vaughan) | (E) as standalone lemma for all `c<1`; (C′) demoted to plausibility clause |
| D.59.1, D.59.1a, D.59.2 (extraction; `⟹ RH` over `w_θ`; Bernstein) | PROVED — **folklore chain, a Hölder inequality** `‖·‖_∞ ≤ ‖·‖_{2k}`, not a transfer of Weil I 3.2 | `Ξ_a`-uniform (D.59.4): carries no arithmetic |
| D.59.3 (`H^{cont}` ∀k ⟺ ATRH; ATRH ⟹ GRH-quality) | PROVED (equivalence); strictness OPEN | the `M_Q` term in the finite Fourier step written in `R149_003` |
| D.60.0–D.60.6 (kill test; `c = 1/2` boundary for `k=1`; Hölder vacuous; restriction saturated by major arcs) | PROVED | the dichotomy table is a `k=1` statement |
| D.60.7 (W-H survival) | PROVED, **scope reduced**: the Fiorilli–Martin / Hayani mechanism is RH-compatible and its `M_2` contribution is negligible; the `2k`-power leg uses Siegel–Walfisz only | |
| "nothing unconditional for `k ≥ 2`" | IMPORTED, reworded: no unconditional *upper* bounds; de la Bretèche–Fiorilli and Harper–Soundararajan Ω-results exist and are of Gaussian order (compared against `H(k,c)`: no contradiction) | |
| D.61.4–D.61.9 (`κ(d) = d/φ(d)`; Bochner; zero-blindness; BDH main term; Landau useless additively; twisting kills additive positivity) | PROVED / RESTATEMENT (D.61.5) | D.61.7 identification at leading order only; D.61.4 split by level |
| **D.61.10** (the split of the two squares) | **RESTATED**: *no transport of the polar/positivity structure* between the additive and the multiplicative square; the moment-level transport is classical (Parseval over `χ`; Goldston–Montgomery) and sign-free | the finding of record is D.61.8–D.61.9: **exponents add on the additive square, subtract on the multiplicative** |
| D.62 (P149) | problem statement, **reclassified**: the Hardy–Littlewood `k`-tuple conjecture with square-root error on average, in Deligne costume | not "the object to create" |
| D.62.1 | PROVED | |
| D.62.2 (`H(2,c) ⟹ RH`) | PROVED with corrected citation: Granville 2007 Thm 1A + Corrigendum 2008 (sharp half); Bhowmik–Ruzsa gives quasi-RH only | |
| D.63.1–D.63.3 (falsifiers) | PROVED | |
| Hooley's `c_0` | CERTIFIED (verify in Crelle 274/275 before quoting) | |

**Row D: no label. No sign claimed. FATAL rule not triggered.**

## 2. Reading of record

Four of Deligne's five ingredients exist over `Z` only in the sense that one of them is a Hölder inequality
(extraction), one is Parseval (the `k=1` invariant theory, `RESTATEMENT`), one is the classical Goldbach explicit
formula (Künneth), and one is twist-stable Rankin positivity on the *other* square. The missing ingredient — a
polar divisor for the family determined by local data, i.e. the singular series promoted from density to
residue — is Doc 106's Lema Faltante 5.3 in additive form, and it is equivalent to the `k`-tuple conjecture with
square-root error. Phase 150 (T5) then shows that no `L²`-orthogonality can supply it.

## 3. Open list (carried)

O-149.1 (`H(k,c)` for one `k ≥ 2`; presumed unprovable by present means; FATAL if claimed), O-149.2, O-149.3,
O-149.4 = (P149) = `k`-tuples, O-149.5 = O-148.2 (two faces of one question). Phase 149 **CLOSED**.

## 4. Amendments after `R149_003` (same day)

* **(E) upgraded**: Lemma D.59.0c gives `Σ_n M_Q(n)w(n/N) = Nŵ(0) + O_A(N^{−A})` for **all** `c < 1` (spacing at
  `q_0 = 1` is `Q^{−1}`); D.59.1/1a/2/4 depend on (E) only. **(C′) OPEN**: its large-sieve justification is false
  exactly in the range where it was invoked.
* **D.60.7′**: "not refuted" PROVED; "provably negligible" holds only for `k = 1, c > 1/2` (Siegel–Walfisz leg
  `o(Q²N^k)` iff `k < 2c`). Ω-check run: no contradiction with de la Bretèche–Fiorilli / Harper–Soundararajan
  (CERTIFIED shapes).
* **D.59.3**: the `M_Q` term is `≪ q^{1/2}N^{c+o(1)}`; the GRH-quality conclusion holds as stated for `c ≤ 1/2`
  and weakens to `q^{1/2+ε}N^{c+ε}` for `c > 1/2`.
* D.61.7 constant fixed (`κ_Q(0) − log 2π − 1`); D.61.4 split by level; D.61.10′ written with the two existing
  transports and their three failures. Two PROVED claims of `R149_001` withdrawn, one upgraded.
