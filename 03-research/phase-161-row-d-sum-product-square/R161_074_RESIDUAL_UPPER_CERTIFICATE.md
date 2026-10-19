# R161_074 — A residual upper certificate for the stabilized moment matrix

Use R161_073's primitive Hilbert space, S=H+R*R and M=RS^(-1)R*. Suppose a quantitative bound S>=alpha I with alpha>0 has been certified. Existence of alpha alone is not a numerical certificate.

## Exact residual identity

Choose a finite collection of approximate solutions, represented by U:C^L -> Dom S. Set

    E=R*-SU,
    M_0=RU+U*R*-U*SU.

Direct expansion proves

    M=M_0+E*S^(-1)E.                         (1)

Indeed expanding (R*-SU)*S^(-1)(R*-SU) gives M-RU-U*R*+U*SU. Consequently

    M_0 <= M <= M_0+alpha^(-1)E*E.           (2)

These are finite matrix inequalities. They preserve all cross terms among the moment right-hand sides. A sufficient certificate for exclusion of a first-contact kernel is

    I-M_0-alpha^(-1)E*E > 0.                 (3)

If interval arithmetic supplies only upper enclosures for the matrices, those enclosures must also be included in (3). The theorem does not assume (3).

## Why Galerkin alone cannot certify strictness

For a Galerkin solution U=V(V*SV)^(-1)V*R*, equation (1) has M_0=RV(V*SV)^(-1)V*R*. Thus its directly computed matrix is a lower bound for M. Finding M_0<I cannot rule out an eigenvalue 1 of M.

An exact two-dimensional test makes the failure visible. Take

    H=[[1,-1],[-1,1]], R=[1,0],
    S=[[2,-1],[-1,1]], U=(1/2,0)^t.

H is nonnegative with kernel spanned by (1,1). R detects that kernel and S is invertible, as required by R161_073. Yet

    M=1, M_0=1/2, E=(0,1/2)^t,
    E*S^(-1)E=1/2.

The entire apparent strict margin is consumed by the omitted residual. Since alpha=lambda_min(S)=(3-sqrt(5))/2, the upper bound in (2) is (7+sqrt(5))/8>1 and correctly fails to certify strictness.

## Actual arithmetic work still required

For the Weil operator, U must have rigorously admissible columns; a smooth function on the closed window belongs to the logarithmic form domain but that alone does not assert it belongs to Dom S with an L2 residual. A form-dual residual version is possible, but needs its own certified dual norm. Neither domain nor residual control may be inferred from a finite grid.

To apply (3) one must provide, at each window under consideration: a detecting observation R or a direct coercivity certificate for S; a quantitative alpha; admissible approximate solutions U; and bounds for the complete residual E. These are necessary inputs to this certificate, not quantities proved here.

This gives an operational upper bound to target. A finite computation at selected windows would not prove D for every T. A global closure would require estimates or coverage valid at every possible first-contact window.

Status: (1)–(3) proved; the finite counterexample checked exactly; no arithmetic certificate satisfying (3) has been constructed. D remains open.
