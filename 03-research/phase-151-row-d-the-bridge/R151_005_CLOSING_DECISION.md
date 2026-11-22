# R151.005 — Closing decision, phase 151 ("the bridge", T6)

* No repairs round: the audit's findings
are accepted as written; the labels below are the labels of record.*

## 1. Labels of record

| item | label | basis |
|---|---|---|
| Lemma 2.2 (abscissa of the fibre's mean square = `β_max` over the `θ`-family) | **RESTATEMENT** (= Cor. 26.5's proof; "Mellin–Plancherel" misnomer; `E(s)` has a simple pole at `s=1`, also to be corrected in `main.md` l.≈10914) | `R151_002` §1 |
| Lemma 2.3 (`|S'_w| ≪ 1`) | PROVED | |
| **Lemma 2.4** (ascent `σ_{2k} ≥ 2kσ_2`, Hölder + dyadic pigeonhole) | **PROVED, new** — the one new piece of mathematics of the phase | `R151_002` §2 |
| Lemma 2.5 (max of abscissae) | PROVED (trivial) | |
| T6(i) `σ_c(k) ≥ 2kβ_max` for every nonnegative additive family | PROVED | |
| T6(ii) a priori bound `M_{2k} ≪ N^{a_k+ε}` ⟹ `β_max ≤ a_k/2k`; optimality | forward **RESTATEMENT** (Thm 26.4 + Cor 27.10a); optimality PROVED | |
| T6(iii) no cancellation between fibres | PROVED (trivial) | |
| T6(iv) "rationality is the one ingredient without additive counterpart" | (A) PROVED; (B) **misstated** (`F^{⊗k}⊗F̄^{⊗k}` has weight `2kw`, `H²_c` pole `q^{kw+1}`; spurious `H⁰_c`); (C) **INTERPRETATION**, not a theorem | `R151_002` §3 |
| Cor 3.2 ("new: `H(k,c)` ⟹ `β_max ≤ ½ + c/k` without (26.9a)") | **WITHDRAWN as new**: it is Thm 26.4's display at fixed `k` fed into Cor 27.10a, with a strictly stronger hypothesis (all `w_θ`) | `R151_002` §4 |
| §4 classification (additive-family / spectral / index / counting) | (β),(γ) closed **on the declared carrier and named enlargements**, not as shapes; exhaustiveness CERTIFIED only; **the partition is not one**: `⟨Hf,f⟩ = Σλ_j|⟨f,e_j⟩|²` is itself a nonnegative additive sum — **the real axis is summand vs numerator** (new open item O-151.4) | `R151_002` §5 |
| Blueprint correction (Landau-oscillation route gives only `(2k+1)β_max − 1`) | PROVED, useful (closes a route) | `R151_001` |
| §8 proposed Paper 47 text | **HELD** (prints withdrawn novelty claims) | |
| FATAL | not triggered | |

**Row D: no label, no sign.**

## 2. Reading of record — the bridge question, answered

1. For every family in which the fibres enter as nonnegative summands, the a priori moment exponent needed for a
   Deligne-type extraction is the zero bound itself (T6(i)–(iii)): the "bridge" is not a reduction but a
   restatement, at every `k`. This includes the spectral realizations where positivity is `⟨Hf,f⟩ = Σλ_j|⟨f,e_j⟩|²`
   (auditor, O-151.4): what distinguishes Deligne is not "spectral vs additive" but that **the fibre zeros enter
   the family identity with the numerator sign** (odd cohomology) so that Pringsheim–Landau places them left of
   the a priori pole.
2. Over `Z` the numerator-sign mechanism exists and is classical: de la Vallée Poussin. The corpus already
   recorded (phase 37, Doc 111 §3.2) that it is "the pole repels the zero" and that its depth is `O(1/log γ)`
   because the positivity budget at height `γ` is the archimedean sea `≍ log γ`. This closing round adds the quantitative
   reason no Rankin-type amplification by nonnegative trigonometric polynomials `P` can deepen it: the penalty is
   `(Σ_{j≥1}a_j)·(½)log γ = (P(0) − a_0)(½)log γ`, the gain is capped by Fejér (`a_1 ≤ 2a_0`), and negative
   coefficients cost `|a_j|/(σ−1)` against the pole; the balance forces `σ − 1 ≍ 1/log γ`. Classical (optimal
   dlVP constants: Kadiri; Mossinghoff–Trudgian); recorded, not claimed.
3. Hence a genuinely new approach must be a **numerator-sign mechanism with a bounded archimedean penalty**, or
   a mechanism that is not a positivity at all. The corpus check (fourteen non-positivity
   mechanisms; see plan §10) leaves as never-analyzed: fractal-uncertainty / Dolgopyat resonance gaps;
   Berkovich–Poineau global analytic spaces over `Z`; measure rigidity of the `×p` semigroup; model-theoretic
   methods; the transcendence / auxiliary-function toolkit. None has, today, a formulated statement that would
   yield the sign.

## 3. Decision

Phase 151 **CLOSED**. Paper 47: add only Lemma 2.4 (as a lemma to §27) and the blueprint correction (as a
remark), and correct the `E(s)` pole at l.≈10914; do not add T6 as a theorem (it is Thm 26.4 + Cor 27.10a in
different words); add O-151.4 to §28.3. Open: **O-151.4** (summand vs numerator as the correct axis of the
classification of positivity mechanisms), O-151.1 (θ-family dependence).

Next: phase 152, round 0 (feasibility, not construction) on the two never-analyzed non-positivity mechanisms
with the most concrete objects — (A) resonances of the modular surface (`= ρ/2`) and the Dolgopyat /
fractal-uncertainty gap mechanism; (B) Poineau's Berkovich spectrum `M(Z)` with the Frobenius lattice
`{k log p}` as its integer points — each with a kill criterion stated in advance.
