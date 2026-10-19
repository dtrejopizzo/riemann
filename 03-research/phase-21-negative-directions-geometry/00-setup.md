# Phase 21 — Geometry of Negative Directions

**Predecessor:** Phase 20 (ω-information barrier, T4/T4.1/T5)  
**Status:** Active

---

## Absolute rules of the phase

This phase does NOT use:
- numerical experiments
- Python or external computations
- pair correlation as an axiom
- de Branges systems as input
- SURF, Hilbert–Pólya, GUE as hypotheses
- any criterion equivalent to RH as a starting point

Every result must come from pure mathematical reasoning.

---

## Central object

Let $Q$ be the localized Weil form (quadratic Kreĭn form on test functions).

Definition: $\mathcal{N}$ = maximal negative subspace of $Q$.

Definition: $\kappa = \dim\mathcal{N}$.

RH $\iff \kappa = 0$.

The object of study of this phase is $\mathcal{N}$ itself, not $\kappa=0$.

---

## Strategic principle

Instead of asking: "Why is $\kappa = 0$?"

Ask: "What properties must every nonzero negative subspace necessarily have?"

If every possible geometry of $\mathcal{N}$ is eventually impossible → RH follows.

But the immediate goal is NOT to prove RH. It is to build a mathematical theory of $\mathcal{N}$.

---

## Goals

### 21-A: Parity Theorem (Class B, unconditional)

Study whether $\kappa \equiv 0 \pmod{2}$ for $\zeta$ and real L-functions.

Hypothesis: off-line zeros come in complete orbits under the Klein group $V = \{id, \sigma, \iota, j\}$. Each complete orbit contributes exactly 2 independent negative directions.

### 21-B: Angular Separation (Class B/A)

Develop a geometric theory of the interaction between negative directions.

Hypothesis: distinct frequency packets (orbits at different heights) are exponentially near-orthogonal.

### 21-C: Defect Measure (Exploratory)

Define the measure $\mu_\kappa$ associated with the negative directions and study its support and rigidity.

### 21-D: Exclusion Principle (Class A if successful)

Look for a rigidity theorem: if $\kappa > 0$, what global structure must necessarily exist in $\mathcal{N}$?

---

## Phase documents

- `00-setup.md` — this document
- `01-parity-and-geometry.md` — Parity Theorem + Angular Separation

## Paper

P32 — `06-papers/P32-negative-packet-theory/main.tex`
