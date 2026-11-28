# Closure of phase 214 — explicit bounds and reconstruction

**Status: closed and archived. Closure date: 28 November 2026.**

The phase is identified as `phase-214-explicit-bounds-and-reconstruction`. It keeps the explicit bounds for the form W_T, the program checking their parameters and the reconstruction notes for the analytic and arithmetic inputs.

## Result and scope

EXPLICIT-BOUND.md develops a strictly positive bound in each window **taking as input the spectral conclusion of paper 46**. This dependence is retained: the filter argument is not an independent proof of that same conclusion. `verify_bounds.py` evaluates the parameters by means of Arb; running it does not replace the functional inequality.

`reconstruction.md` keeps the mathematical work and its boundaries of scope as they were recorded. It is a cumulative research document; closing the phase administratively does not turn all its historical obligations into proved theorems. The later global review and the verdict on the chain with supplements belong to phase 215.

## Material preserved

- [Bounds and conditional proof](EXPLICIT-BOUND.md).
- [Reconstruction notes](reconstruction.md).
- [Parameter check](verify_bounds.py).

In this closure the content of the reconstruction and of the program was not modified, nor were mathematical computations repeated. This memo was added and the README was reorganised as a guide to the phase; the proof it contained was preserved in full in EXPLICIT-BOUND.md.

## Continuity

The result of the global review is in the [final memo of phase 215](../phase-215-private-certification-grh-rh-with-supplements/FINAL-MEMO.md). The development of new connections is reserved for the future phase 216, which is not started in this closure operation.
