# Carril B - Points 17 through 25

## Bridge criterion

The RDI route contributes to \(\Omega_7\) only if it proves one of:
\[
  {\rm RDI}\Longrightarrow \lambda_n\ge0\quad(n\ge1),
\]
or
\[
  {\rm RDI}\Longrightarrow \hbox{all zeros of }\Xi\hbox{ are real}.
\]

Without one of these bridges, BTG, GAP-Z and downstream safety statements are
infrastructure rather than a proof of Li positivity.

## Ledger

| Point | Statement | Status in this phase | Minimal missing theorem |
|---|---|---|---|
| 17 | BTG-DIV in the true \(\mu_L\) | Open | Prove divergence for the moving CCM boundary source in the true limiting measure. |
| 18 | LP interface independent of circular \(\mu_L\) | Open | Build the LP interface without defining the target measure from the desired endpoint. |
| 19 | GAP-Z with ZERO cancellation | Reduced | GAP-Z is sufficient for convergence, but not a Li-sign bridge. Need a signed ZERO statement tied to Li. |
| 20 | RDI-ANCHOR/core | Open | Prove the intrinsic arithmetic anchor, not only convergence of normalized ratios. |
| 21 | RDP-SHELL | Open | Prove directional shell control on the actual residual subspace. |
| 22 | SAFE-PROLATE-BRIDGE | Conditional | Prove the bridge without importing Weil positivity. |
| 23 | SAFE-LIMIT-POINT | Conditional | Close both LP uniqueness and IDENT arithmetic identification. |
| 24 | SR-SAFE | Open | Derive the safety statement from the previous modules with all limits fixed. |
| 25 | RDI implies Li | Missing | Produce a formula mapping the RDI core to every Li coefficient or to real-rootedness. |

## Conclusion

Carril B does not currently close \(\Omega_7\). Its minimal live theorem is:

\[
  {\rm RDI\mbox{-}CORE}
  \Longrightarrow
  \left[
    -n+\int_1^\infty(\psi(y)-y)f'_{n,0}(y)\,dy
    \ge -\lambda_n^{\rm arch}
  \right]
  \quad(n\ge8),
\]
with the boundary regulator and all cofinal limits included.

No such formula is present in the audited material. Until it appears, the
direct Li route remains the main route.
