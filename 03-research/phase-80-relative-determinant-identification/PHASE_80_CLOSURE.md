# Phase 80 closure - Corrected minimal cut to Omega7

## 1. Outcome

This phase closes at reduction grade.  It does not prove `Omega7`.  It replaces
the inherited mixed ledger by exact equivalences, counterexamples and a minimal
set of theorem obligations.

Two corrections govern the result:

```text
1. the comparison object is the bilateral core characteristic, including the
   external-mesh quotient;
2. arithmetic identification is a two-scale assertion: finite-section
   convergence at fixed L, followed by outer identification as L->infinity.
```

The stronger fixed-`L` equality with the hard finite Euler product is not used.

## 2. Closed mathematics

```text
C1  independent Euler--Gamma product E_L, zero-free on Re s>1;
C2  exact identities E_L'/E_L=H_L and E_L->(2xi)^2;
C3  equivalence of relative projective flatness, derivative defect and
    normalized relative-ratio convergence along any directed family;
C4  coherence plus summable real-spectral convergence does not determine the
    arithmetic limit;
C5  HPR-DIV is exactly the directional cell scalar in the Cauchy-gauge
    quotient, but is not an established resolvent-trace identity;
C6  GAP-Z is sufficient but not minimal; VITALI-Z is a weaker convergence
    route;
C7  full-solution disk uniqueness forces dimension one and nonzero
    normalization, so the proposed mu-free bypass is impossible;
C8  absolute radical-tail smallness is insufficient under unbounded bordered
    response; directional continuity on the actual tail subspace is sufficient;
C9  a Feshbach denominator bracket alone does not imply BTG divergence.
```

## 3. Minimal open cut

The remaining chain is partitioned without hidden implications.

```text
A. finite-section convergence
   A1  RDI-CONV through MIN-CONV: GAP-Z or VITALI-Z;

B. arithmetic identification
   B1  RDI-ANCHOR: the intrinsic defect D_L tends to zero as L->infinity;

C. corrected LP
   C1  BTG-DIV for the moving CCM boundary source;
   C2  MU-FREE-COMPLETENESS, clauses MF-1--MF-6;

D. radical and Fourier tails
   D1  RDP-SHELL;
   D2  DIRECTIONAL-TAIL-CONTINUITY for PROLATE;
   D3  DIRECTIONAL-TAIL-CONTINUITY for WEIL-TAIL.        (3.1)
```

Once `A1`--`D3` hold, the already proved cofinal diagonal and normal-family
arguments give `SR-SAFE`, then `Omega7`.

## 4. Location of the hard arithmetic step

`B1` is the only item in (3.1) required to distinguish the zeta construction
from a build without the Euler product.  This makes it the arithmetic
discriminant.  It does not prove that `A1`, `C1`, `C2`, or `D1`--`D3` are
automatic.  They remain independent analytic obligations.

The conservation principle is therefore recorded precisely as

```text
at least one member of the sufficient cut carries force-RH;
the current architecture locates the required arithmetic separation in B1;
the other members must still be proved build-neutrally.                 (4.1)
```

## 5. Handoff

The next phase attacks `B1` through the exact rank-one perturbation determinant
behind the finite transfer.  The other modules remain quarantined until their
own proof phases; none may be imported as an unproved lemma into the arithmetic
identification.

## 6. Status

```text
phase result:
  closed at reduction grade;

proved here:
  C1--C9;

open toward Omega7:
  A1--D3 in (3.1);

next phase:
  rank-one secular form of RDI-ANCHOR.
```

