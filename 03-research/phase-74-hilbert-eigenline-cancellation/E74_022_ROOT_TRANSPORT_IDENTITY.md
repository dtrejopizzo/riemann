# E74.22 - Critical root transport identity

Date: 2026-07-16.

## Exact relation

Let

```text
C_L(t)=sum_n xi_L(n)/(t-d_n)=P_L(t)/D_L(t)
```

and let `tau_L` be a simple finite Weyl root near a fixed critical zero
`gamma`.  The mean-value identity gives

```text
C_L(gamma)=C_L'(theta_L)(gamma-tau_L)
```

for a point between `gamma` and `tau_L` in the real formulation.  Therefore,
under polynomial upper and lower bounds for the normalized derivative,

```text
CAUCHY-EIG-LOC at gamma
<=>
|tau_L-gamma|=O_M(L^(-M)).
```

This is the root-transport form of `CRIT-NUM-DIV`.

## Probe result

`E74_022_root_transport_probe.py` uses Newton iteration initialized at each
critical zero.  On resolved zeta windows, the finite root and the critical
zero agree at about `1e-14`, the available double-data floor.  Evaluating at
`gamma+1/L` destroys the cancellation by roughly 16--20 powers of `L`.

Thus the Phase 74 directional scalar is explained by finite-root locking, not
by neighborhood regularity or a small operator row.

## Remaining theorem

```text
CCM-ROOT-LOCK:
For every fixed natural-height critical window and every M,
|tau_{j,L}-gamma_j| <= A_M L^(-M),
```

with polynomial derivative separation and a zero-independent identification
of the matching finite root.

This must be proved from the Euler/Gamma CCM construction.  Numerical Newton
locking is a detector, not a proof of the rate.

