# D.66 directed delta-cover audit

## Result

Write

\[
\delta=2T-\log 2.
\]

The analytic bridge in D.65 closes the range through the exact rational
endpoint \(\delta=0.000037\).  The directed Arb computation in
`114_d_66_delta_cover_verify.py` proves strict positivity of
\(q_{19}+10H\) on 24 exactly adjacent leaves from that endpoint through
\(\delta=0.0008529\).  Since

\[
0.0008529>0.694-\log 2,
\]

this is a rational over-cover through \(T=0.347\); it is not a rounded
identification of the target endpoint.

## Directed numerical contract

All transcendental evaluation and interval propagation uses Arb at 192-bit
precision.  Each leaf uses 350 normalized indicator cells: one cell on each
boundary component and 348 cells in the middle component.  Reflection
symmetry gives two 175-dimensional parity blocks.

The kernel diagonal is evaluated by a cancellation-free alternating series
with a rigorous first-omitted-term remainder.  Off-diagonal entries use
factored `expm1` expressions.  The analytic projection residual is subtracted
from every diagonal before the spectral test; throughout the cover it is
strictly below \(0.09279\).

Floating-point eigendata are used only to propose a rational change of basis
\(Q\).  The proof itself certifies:

1. invertibility of \(Q\) by a positive Gershgorin lower bound for
   \(Q^{\mathsf T}Q\);
2. an upper bound for \(\lVert Q\rVert^2\) by directed row sums;
3. positivity of \(Q^{\mathsf T}A_0Q\) by Arb Gershgorin disks selected by
   their lower endpoints;
4. transfer back to \(A_0\) after division by the certified norm bound;
5. Weyl control of the complete interval matrix by the Frobenius norm of all
   entry radii.

An interval is retained only if both parity margins are strictly positive.
Failed parents are bisected and are not recorded as certificate leaves.
The least final margin occurs on
\([0.000592,0.000657225]\) and is certified as

\[
\text{odd margin}>0.0009261413093>0.0009.
\]

## Reproduction and independent structural check

Run the full directed recomputation with python-flint exposed on
`PYTHONPATH`:

```bash
python3 114_d_66_delta_cover_verify.py
```

It terminates with `COVERAGE_PASS 24` and emits its full JSON manifest.
The checked-in conservative manifest is
`114_d_66_delta_cover_manifest.json`; its exact decimal adjacency and strict
recorded margins are checked without floating point by:

```bash
python3 114_d_66_delta_cover_manifest_check.py
```

The earlier `114_d_66_first_leaf_arb_verify.py` is deliberately retained as
a rejected monolithic pilot: its interval variation is too large, and it is
not part of this certificate.

## Scope

This closes only the directed positivity segment from the D.65 bridge through
\(T=0.347\).  It does not by itself claim the later segment up to the separate
D.63 certificate near \(T=0.4\).
