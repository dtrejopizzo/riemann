# The first open gate: full residual audit at `T=(1/2) log 5`

Status: reproducible binary64 sizing result. No interval sign conclusion is
claimed in this note.

## 1. Why the old five-column certificate does not close the gate

The certified decomposition in paper 42 is

    P_T = D_5 direct-sum S_163 direct-sum Q_200.

The old contracted Gram controls the action of the five post-Schur graph
columns, but the certified lower bound `Q A Q > 0.218 Q` applies only to the
orthogonal complement of the whole `V_200`.  The safe block still couples to
that complement.  Thus the two missing quantities are the complete residual
of `V_200` and the Green operator after shorting the safe block.

## 2. Source rebuild

The physical constrained Ritz frame was regenerated from the definitions:

- polynomial-exact Arb contact matrix for the active iterates `2,3,4`;
- the complete Hurwitz--Lerch Gamma block;
- the exact two-by-two Tate graph imposing both primitive equations.

At `N=200` the directed finite compression passes. Its first physical Ritz
values are

    3.11563928e-12, 6.25438580e-10, 3.11759310e-7,
    3.12085199e-5, 2.08735114e-3, 5.85139876e-2.

This agrees with the historical finite calculation while avoiding its
retracted complement inference.

## 3. Complete residual Gram

Let `X` be the 198-column physical Ritz frame, `P` the `V_200` projection and
`A=-B_nuc`. The script

    scripts/p3_log5_full_residual_diagnostic.py

forms

    H = (A X)^*(A X) - (P A X)^*(P A X)
      = (Q A X)^*(Q A X) >= 0

and diagonalizes the dimensionless coupling

    M = B^(-1/2) H B^(-1/2),

where `B=X^* A X`.  This retains every safe-to-tail cross term that was
absent from the five-column computation.

At `2^18` FFT points, the first generalized values are

    .286065, .272363, .244422, .243954, .239704,
    .239316, .234971, .234176, .223252, .222660,
    .201586, .187920, ...

At `2^20` points they are

    .333223, .321944, .244500, .244335, .239771,
    .239732, .235129, .234278, .224701, .223333,
    .205088, .196533, ...

At both resolutions exactly ten values exceed the certified scalar
complement gap `delta=.218`.  The leading values are not converged because a
uniform grid resolves the endpoint layers of the highest Legendre modes
poorly; the stable promotion count is a sizing observation, not a bound.

## 4. Structural consequence

The ten high-coupling directions have negligible mass in the five delicate
Ritz modes and concentrate mainly in Ritz indices near `100--197`.  Therefore
the failure is not a new almost-null arithmetic direction. It is a boundary
resolution defect of `V_200`.

Within the scalar-gap argument, merely relabelling those ten directions as a
larger dangerous block cannot help: an eigenvalue of
`B^(-1/2) H B^(-1/2)` above `delta` already says that the two-block estimate

    B - delta^(-1) H > 0

fails in that direction. The live alternatives are:

1. enlarge `V_N` so the offending endpoint action is absorbed into the
   finite block, while retaining the inherited `Q_N A Q_N > .218 Q_N`;
2. replace the scalar gap by the true positive Green operator
   `A_QQ^(-1)`, exactly as required by the geometric polarization plan.

This is useful calibration for P3: a candidate geometric unitary must encode
the direction-dependent Green response. A uniform coercivity constant cannot
be the global Hodge mechanism.

## 5. Next falsifiable computation

Regenerate the constrained `V_260` frame and repeat the same residual audit.
If its generalized residual falls below `.218`, intervalize the finite block
and the residual band/tail. If it does not, compute the Galerkin Green

    H_G = C^* (Q A Q)^(-1) C

on nested complements and certify only its remaining analytic tail.  The
second route is the analytic finite-section shadow of the desired P3
polarization, not an unrelated workaround.

