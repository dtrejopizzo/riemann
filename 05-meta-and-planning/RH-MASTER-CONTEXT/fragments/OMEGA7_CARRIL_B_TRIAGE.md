# Omega7 carril B triage

## Conclusion

The LP+IDENT/RDI route does not currently contain a mechanism that produces
the Li sign

[
  lambda_n\ge0
]

literally. BTG and GAP-Z may still be useful infrastructure, but the present
chain does not close points 17--25. It should remain suspended unless one of
the two missing links below is supplied:

[
  \mathrm{RDI}\Longrightarrow \lambda_n\ge0\quad(n\ge1),
]

or

[
  \mathrm{RDI}\Longrightarrow \text{all zeros of }\Xi\text{ are real}.
]

The second link would imply the first through the usual Li sum-of-squares
identity on the line. Neither link is presently proved.

## Pointwise status

| Point | Status | Missing mathematical content |
|---|---|---|
| 17. BTG-DIV in the true measure `mu_L` | Open | Divergence in the true `mu_L`; shell cancellation and the anchor--drift connector. Finite tests with `mu_ref` do not certify the limit. |
| 18. LP interface free of circular `mu_L` choice | Open | A replacement interface that does not choose the target measure in advance, plus projective response convergence. |
| 19. GAP-Z including ZERO | Open | Signed ZERO cancellation, local uniformity and summability. MESH and BND are not enough. |
| 20. RDI-ANCHOR/core | Open / force-RH | An independent Euler--Gamma cell identity identifying the core. Convergence and numerical discrimination do not imply this identity. |
| 21. RDP-SHELL | Open | A cofinal shell theorem with directional tails after signed pairing. |
| 22. SAFE-PROLATE-BRIDGE | Open | Transfer through PROLATE/WEIL-TAIL without importing Weil positivity. |
| 23. SAFE-LIMIT-POINT | Conditional assembly only | Needs effective LP and IDENT with a common normalization and declared order of limits. |
| 24. SR-SAFE | Open hypothesis; downstream implication known | The implication from SR-SAFE to real zeros is available, but SR-SAFE itself is not proved. |
| 25. RDI implies Li | Missing | No formula transports the RDI core to each Li coefficient. |

## First missing bridge

The first bridge worth attempting, if carril B is reopened, is the locally
uniform convergence

[
  \log\Theta_{L,N(L)}(-i\sigma)
  \longrightarrow
  2\log{\Xi(1/2+\sigma)\over\Xi(1/2+\sigma_0)}
  \qquad(\sigma>1/2),
]

derived from the RDI core with all limits justified. If this were proved with
the required normalizations, the known Hurwitz/normal-family passage would
give reality of zeros and then

[
  \lambda_n
  =
  4\sum_{\gamma>0}\sin^2\left({n\theta_\gamma\over2}\right)\ge0.
]

This is a full force-RH bridge, not a neutral build statement.

## Decision

Carril B is not closed. It is also not the priority path. The direct Li
carril should remain first until a literal RDI-to-Li or RDI-to-real-zeros
theorem is formulated and proved.
