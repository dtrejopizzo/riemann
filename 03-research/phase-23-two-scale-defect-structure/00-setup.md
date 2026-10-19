# Phase 23 — Two-scale structure and spectral compatibility of the defect

**Predecessor:** Phase 22 (modified explicit formula, invariant audit, Step 22-D)
**Status:** Active

---

## Exact starting point

Phase 22 established:

1. Under Hypothesis D: $\psi = \psi_0 - D_m$ exactly.
2. $D_j(e^t)/e^{t/2} = A_j e^{b_j t}\cos(\gamma_j t) + O(e^{-b_j t})$ — exponential growth.
3. Structure function: $S_2^{(D)}(\tau, T) \asymp e^{2b_j T}$ — diverges exponentially.
4. The Paley-Wiener method reaches exactly the boundary $\Re(s) = 1$.
5. The three invariant candidates fail or are circular.

Phase 22 also proposed: if the GMC with $\beta=1$ satisfies $S_2 = O(\log T)$, there is incompatibility with $e^{2b_j T}$. This was the direction of Phase 23.

Phase 23 evaluates that direction and carries out the exact computations.

---

## Absolute rules

- No numerical computation, no Python.
- Only definitions, lemmas, propositions, theorems, proofs.
- Every argument must be evaluated by whether it contributes to excluding $m \geq 1$.
- If a line does not lead to $m = 0$, it is abandoned and documented frankly.

---

## The question of Phase 23

Under Hypothesis D, the off-line zero $\rho_j = \sigma_j + i\gamma_j$ manifests in two ways:

**Scale $x$** (prime-counting variable): $D_j(x) \asymp x^{1/2+b_j}\cos(\gamma_j\log x)$ — algebraic growth.

**Scale $t$** (imaginary heights, variable of $\zeta$ on the critical line): effect on $\log|\zeta(1/2+it)|$ near $t = \gamma_j$ — localized depression of finite depth.

Questions:
1. What exactly is the effect on $\log|\zeta(1/2+it)|$? (computable from the Hadamard product)
2. Is that effect compatible or incompatible with the GMC?
3. Can $S_2^X(\tau,T)$ be bounded from above using the Euler product?
4. Does it produce any contradiction with $m \geq 1$?

---

## Documents of the phase

- `00-setup.md` — this document
- `01-exact-hadamard-effect.md` — exact computation of the effect of the off-line orbit on $\log|\zeta(1/2+it)|$
- `02-structure-function-analysis.md` — analysis of $S_2$ from above and below
- `03-barrier-formulation.md` — precise formulation of the final obstacle

## Paper

P34 — `06-papers/P34-two-scale-structure/main.tex`
