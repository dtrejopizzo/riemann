# Phase 182 — rectangular Gram tunnel

The phase builds a rectangular (non-square) Gram factorization combining the
positive block H = A*A with an orientation corner R = B*A, aiming to show
that a first-contact vector in ker H is automatically annihilated by the
orientation operator R_L, which would exclude first contact and give
W_T ≥ 0 for every T. It then audits the construction against prior corpus
results and against a candidate fiber-by-fiber realization.

## Results
- Rectangular tunnel lemma: ker H ⊆ ker R for any Gram block H = A*A,
  R = B*A; applied to a first-contact vector this gives R_LF = 0.
  **PROVED**, but identified as already present as the bordered null anchor
  law of R170_862.
- Energy factorization criterion (three equivalent conditions for R to
  factor through H^{1/2}) in finite dimension, with the necessary-but-not-
  sufficient version in infinite dimension. **PROVED**
- A local, fiber-by-fiber ansatz realizing the needed product-fiber
  Euler-Poisson isometry (EPG) is impossible: the coherent channel built
  from the oriented prime weights has infinite rank on the relevant space,
  while the Tate conditions cut only a codimension-two subspace, so no
  local construction can produce the required second null vector.
  **PROVED / NO-GO**
- The conservative part of the rectangular coligation architecture
  duplicates prior results (D.244–D.247, D.256–D.262); claims of novelty in
  the first version of the file are withdrawn.
- Remaining open piece: a single **nonlocal** joint factorization (NGF) of
  the Chebyshev–Gamma column, to be built before any pseudo-inverse; a
  literature audit (Connes–Consani scaling Hamiltonian, numerical Weil/Suzuki
  realizations) found no existing construction of this factor. **OPEN**

## Documents
- `R182_RECTANGULAR_TUNNEL.md` — the rectangular tunnel lemma, the
  circularity test, the local ansatz (EPG) and its failure.
- `R182_201_AUDIT_AND_NONLOCAL_GATE.md` — audit confirming the rank
  obstruction to the local version, the Schur/Douglas correction, and the
  statement of the remaining nonlocal factorization target (NGF).

## Relation to other phases
Builds on the bordered null anchor law (R170_862) and the prime-local
rectangular coligation of D.244–D.247, D.256–D.262; supersedes the
complex-square mechanism of phase 181 by moving the orientation off the
diagonal block. Leaves the nonlocal factorization as an open target for
later phases.
