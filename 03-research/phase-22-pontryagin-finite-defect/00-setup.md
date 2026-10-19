# Phase 22 — Arithmetic Consequences of the Finite Pontryagin Defect

**Predecessor:** Phase 21 (geometry of the negative space, P32)
**Status:** Active

---

## Starting point

Phase 21 established:

1. **Parity Theorem** (unconditional): $\kappa = 2m$, $m \geq 0$.
2. **Lorentz Decomposition** (unconditional): $\mathcal{N} \cong \bigoplus_{j=1}^m \mathbb{R}^{1,1}_j$.
3. **Theorem 9.1 / Corollary 9.2** (conditional on $\kappa < \infty$): under $\kappa = 2m < \infty$,
   $$\xi = \xi_0 \cdot P_{4m}$$
   where $\xi_0$ is entire with all zeros on the critical line and $P_{4m}$ is the polynomial of the $4m$ off-line zeros.
4. **Conjecture EX**: $\kappa \in \{0\} \cup \{\infty\}$ (no finite positive value).
5. **Wall W4-RSRP**: candidate wall, Spectral Rigidity of the Pontryagin Regime.

Phase 22 starts from the hypothesis $0 < \kappa = 2m < \infty$ (which we call **hypothesis D**) and
asks: what does a **finite** set of off-line zeros leave behind in the prime-counting function?

---

## Absolute rules of the phase

This phase does NOT use:
- numerical experiments or Python
- pair correlation as an axiom
- de Branges systems as input
- SURF, Hilbert–Pólya, GUE as hypotheses
- any criterion equivalent to RH as a starting point
- non-rigorous derivations of explicit formulas

Every result must be derived from:
- Perron's formula + the factorization $\xi = \xi_0 P_{4m}$
- the Euler product of $\zeta$
- the functional equation
- pure algebra/complex analysis

---

## Central object

Under hypothesis D, define:

$$D_m(x) := \sum_{\rho \in Z_{\text{off}}} \frac{x^\rho}{\rho}, \qquad
Z_{\text{off}} = \{\text{off-line zeros of } \zeta\}$$

We call $D_m(x)$ the **arithmetic defect of degree** $m$.

Questions:
1. What is the exact form of $D_m(x)$?
2. What invariants of $\psi(x)$ are marked by $D_m$?
3. Can $D_m$ be compatible with the structure of the Euler product?
4. Does $D_m$ connect with the $\omega$ class (multiplicative chaos)?

---

## Goals

### 22-A: Modified Explicit Formula (Class B — provable)

Rigorously derive the decomposition:
$$\psi(x) = \psi_0(x) - D_m(x) + O(\log^2 x)$$

where $\psi_0(x)$ is the Chebyshev analogue of $\xi_0$ and $D_m$ is the finite sum of oscillations.

Compute the exact coefficients: amplitudes, phases, growth rates.

### 22-B: Anatomy of the Defect (Class B — provable)

For each orbit $\mathcal{O}_j = \{\sigma_j \pm i\gamma_j, (1-\sigma_j) \pm i\gamma_j\}$ with $b_j = \sigma_j - \frac{1}{2} > 0$:

- Compute $D_j(x)$ explicitly.
- Study the structure of the **Lorentz block** via the explicit formula.
- Compute the "defect energy" $\mathcal{E}_j(X) = \int_X^{2X} |D_j(t)|^2 t^{-2}\,dt$.

### 22-C: Incompatible Invariants (Exploratory → potential Class A)

Look for a functional $\mathcal{F}$ such that:
- $\mathcal{F}(\psi)$ has a known value (from the Euler product)
- $\mathcal{F}(\psi_0 - D_m)$ is incompatible with that value for every $m \geq 1$

Candidates: Selberg's second-moment integrals, the Mertens function, sieve-type integrals.

### 22-D: Connection with class $\omega$ (Exploratory)

Via multiplicative chaos (M13 and predecessors): can the fluctuation $D_m$ coexist with the fine-grained chaos statistics?

---

## Phase documents

- `00-setup.md` — this document
- `01-modified-explicit-formula.md` — Steps 22-A and 22-B
- `02-invariants.md` — Step 22-C (to be written)
- `03-omega-connection.md` — Step 22-D (to be written)

## Paper

P33 — `06-papers/P33-arithmetic-defect/main.tex`
