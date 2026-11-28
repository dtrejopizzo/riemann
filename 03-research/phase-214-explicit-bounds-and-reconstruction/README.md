# Phase 214 — Explicit window bounds and reconstruction

**Status: CLOSED.** The main result is **CONDITIONAL**: it takes as input the spectral conclusion of Paper 46. The closing statement and its limits are in [FINAL-MEMO.md](FINAL-MEMO.md).

## Question

Obtain an explicit lower bound for the full form W_T on each window, starting from its positive spectral representation, and reconstruct the analytic and arithmetic inputs that enter the conclusion of Paper 46.

## What was done

- A contractive filter was built that annihilates the two Tate moments and enlarges the support in a controlled way.
- The explicit formula, a bound for the prime operator, the archimedean growth and an estimate for the leakage of mass in frequency were combined.
- Explicit parameters were fixed for an inequality W_T(f) ≥ exp(−K)‖f‖₂², and an Arb program was prepared to evaluate the size of K.
- Reconstruction notes were written on means, multiplicity, determinants, counts, representations and periods of theta chains, keeping the hypotheses and obligations of each step.

## Results

| Result | Status |
|---|---|
| Explicit strictly positive bound on each window | **CONDITIONAL** on the non-trivial zeros lying on the critical line, as in the spectral conclusion of Paper 46 that is used |
| Parameters for the radii 5 and 10 | **NUMERICAL**: reproducible evaluation with Arb; it does not replace the functional proof |
| Reconstruction of the inputs of Paper 46 | Developed by blocks; the notebook keeps its partial results and obligations and does not claim an independent global proof |

The spectral comparison of the filter uses exactly the location of the zeros. Using it to prove that same input would be circular. The finite-height certificate alone does not give the sign of the terms of the zeros outside it.

## Files

1. [FINAL-MEMO.md](FINAL-MEMO.md): result of the phase and scope of the closure.
2. [EXPLICIT-BOUND.md](EXPLICIT-BOUND.md): statement, parameters and proof of the explicit bound.
3. [verify_bounds.py](verify_bounds.py): evaluation of log10 K with python-flint/Arb; run `python3 verify_bounds.py` from this folder.
4. [reconstruction.md](reconstruction.md): mathematical notebook of the reconstruction of the inputs.

## Relation to other phases

[Phase 213](../phase-213-new-constructions/) contains the antecedents of the filters and of the leakage estimates. [Phase 215](../phase-215-private-certification-grh-rh-with-supplements/README.md) holds the later review of the global chain with its supplements; that verdict does not remove the hypotheses used in the proof of this phase. [Phase 216](../phase-216-new-arithmetic-connections/README.md) develops autonomous results from those connections.
