# Phase 0 — Foundations & Translation (work plan)

**Goal:** convert our localized Weil quadratic form Q into the language of the deep frameworks,
and — the advisor's key point — **determine whether the missing truncation lemma is "technical"
or "RH in disguise"** before investing in Phase 1. No RH risk; highest intellectual return per hour.

Phase 0 has two halves: **0.A Translation** (does Q already exist under another name?) and
**0.B Cartography of the lemma** (is the lemma reachable or is it RH-equivalent?).

---

## 0.A — Translation: write Q in four languages

Our object: Q_{jk} = W(φ_j ⋆ φ̃_k), where W is the Weil functional (explicit formula,
zero-side minus arithmetic-side) and {φ_j} is the Hermite–Gauss localized basis at (T₀, σ), dim J.

**0.A.1 Weil / Guinand.** Write W(f) = Σ_ρ ĥ(γ) − A_∞(f) − Σ_{p,k} (log p) p^{−k/2} f(k log p)
with explicit ĥ and archimedean term A_∞. State exactly which admissible class our φ_j live in,
and the precise pairing that makes Q a Gram matrix of the Weil inner product. *Output: the exact
formula, with our normalization pinned.*

**0.A.2 Connes (adelic trace).** Express W(f) as a trace over the adèle class space
A_Q/Q^× (Connes 1999; Connes–Consani arithmetic site). Identify Q as the compression of the
trace operator to span{φ_j}. **Key question:** Connes' "Weil positivity = positivity of a trace"
— does the trace carry a *manifest* ≥0 structure that could survive basis restriction? This is
the lead for Phase 3. *Output: Q as a finite compression of the Connes operator + whether
positivity is structural there.*

**0.A.3 de Branges.** Our localized reproducing kernels generate a de Branges space H(E) of
entire functions. Identify the structure function E(z). RH ⟺ E has no zeros in the open lower
half-plane (equivalently, a monotonicity / chain condition on the canonical system). **Key
question:** does our numerically-observed locality correspond to the de Branges chain growing
monotonically? *Output: E(z) identified; chain condition stated as a testable inequality.*

**0.A.4 Function-field template.** Read the proven RH for curves over F_q (Weil; Bombieri's
exposition; Deligne) as **positivity of the intersection form** (Hodge index theorem on the
surface C×C). Identify the arithmetic analogue object whose positivity would be our (LB).
*Output: the dictionary entry "intersection-form positivity ↔ (LB)", with the gap named.*

**Deliverable 0.A:** `phase0-translation.md` — Q in all four languages + the verdict: *is Q a
known object, a variant of one, or genuinely new?* All three answers are valuable. Publishable
as an expository note regardless.

---

## 0.B — Cartography of the lemma (does it hide RH?)

The truncation lemma (Phase 1.2): the error Q_finite − Q_Weil is uniformly dominated over the
test-function family. The advisor's warning: "todo depende de este lema" has two outcomes —
**good** (technical, provable by harmonic analysis) or **bad** (equivalent to RH disguised).
We must decide which *before* Phase 1, by mapping implications from known results.

**0.B.1 Forward implications — does a known hypothesis IMPLY the lemma?**
Map, for each, whether it gives the uniform truncation bound:

| Known result | What it controls | Does it imply the truncation bound? |
|---|---|---|
| GRH | zero-free region, |ζ| on the line | likely controls the zero-sum tail — check strength |
| Lindelöf Hypothesis | |ζ(½+it)| ≪ t^ε | controls oscillation of the zero-sum truncation |
| Zero-density estimates (e.g. N(σ,T)) | # zeros off the line | bounds the off-critical contribution directly |
| Montgomery pair correlation | zero spacing statistics | controls the zero-sum tail variance |
| Vinogradov–Korobov zero-free region | unconditional zero-free strip | gives an *unconditional* partial bound — the best hope for "technical" |

**0.B.2 Backward implication — does the lemma IMPLY RH?**
If a version of the lemma implies RH, that version is RH-equivalent → do NOT spend years on it;
instead treat it as a reformulation (still valuable, see Phase 2). Determine the *weakest* form
of the lemma that suffices for the Phase-1 detector theorem, and check whether *that* weak form
is unconditional or hypothesis-strength.

**0.B.3 The verdict that decides Phase 1's strategy:**
- **Technical case:** the weak lemma needed for the detector follows from an *unconditional*
  zero-free region + standard explicit-formula error analysis → Phase 1 is real, do it.
- **Hypothesis-strength case:** the lemma needs GRH/Lindelöf → the detector theorem is
  *conditional*; still publishable, but reframe honestly.
- **RH-equivalent case:** the full uniform lemma ⟺ RH → stop trying to "prove" it; pivot all
  energy to Phase 3 (structural positivity) and Phase 2 (reformulation).

**Deliverable 0.B:** `phase0-cartography.md` — the implication table filled in, plus the verdict.
This single document determines whether Phase 1 is "harmonic analysis" or "another RH reformulation."

---

## Why Phase 0 first

- It has **zero RH risk** and **guaranteed output** (an expository note + a verdict).
- It may reveal Q is already known (saves years) or genuinely new (a result on its own).
- **It tells us, before Lise Science run 8 invests compute, whether the lemma is worth a frontal assault.**
- It is the cheapest possible insurance against the advisor's central worry.

**Sequence:** 0.A.1 → 0.B (cartography, highest priority) → 0.A.2/3/4 in parallel with Lise Science run 8.
