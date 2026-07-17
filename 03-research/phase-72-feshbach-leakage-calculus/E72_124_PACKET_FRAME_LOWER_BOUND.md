# E72.124 -- Packet frame lower bound for YLOW

**Date:** 2026-07-09.
**Role:** identify the finite lower-bound theorem behind `YLOW`.

## 0. Packet components

The packet in E72.123 is:

```text
Y_x(tau)=(sigma_n^E(tau),dot_sigma_n^E(tau))_n,
```

where:

```text
sigma_n^E(tau)
 = int exp(-i tau r)sin(d_nr)dE_x^leftarrow(r),

dot_sigma_n^E(tau)
 = int exp(-i tau r)r cos(d_nr)dE_x^leftarrow(r).
```

The `YLOW` condition is:

```text
||Y_x(tau_j)|| >= c sqrt(x)L
```

for finite root-height windows.

## 1. Finite packet-frame theorem

The exact theorem needed for `YLOW` is:

```text
Packet frame lower bound:
sum_n |int exp(-i tau_j r)sin(d_nr)dE_x^leftarrow(r)|^2
+sum_n |int exp(-i tau_j r)r cos(d_nr)dE_x^leftarrow(r)|^2
 >= c^2 x L^2.                                             (PFLB)
```

This is a finite frame lower bound for the endpoint discrepancy measure against the CCM sine/cosine
packet at the finite root `tau_j`.

No zeta zero is used; `tau_j` is a finite CCM root.

## 2. Why this is plausible but nontrivial

The packet has about `O(L)` physical samples in fixed height windows.  The derivative block carries an
extra endpoint factor `r`, so a `sqrt(x)L` scale is natural for a prime-minus-continuous signed measure
with endpoint fluctuation of size `sqrt(x)`.

But `PFLB` is a lower bound on a signed discrepancy packet.  It cannot be replaced by PNT.  It must use
the finite CCM frame and the fact that the bad subspace has already been removed in the final gate.

## 3. Diagnostic

The companion script:

```text
E72_124_packet_component_probe.py
```

separates `sigma`, `dot_sigma`, and the prime/continuous contributions.

Representative output:

```text
E72.124 packet component probe
 lam   L roots  ||Y||/(sqrtxL)  sigma%  dsigma%  disc/cont sigma  disc/cont dsigma
   6  3.58     3       1.781e+00   0.715    0.746       1.234e+00         1.508e+00
   8  4.16     4       1.778e+00   0.703    0.809       1.178e+00         1.440e+00
  10  4.61     3       1.891e+00   0.629    0.883       1.010e+00         1.428e+00
  12  4.97     4       2.058e+00   0.651    0.849       1.107e+00         1.363e+00
  14  5.28     4       1.865e+00   0.624    0.835       1.061e+00         1.238e+00
```

Both packet blocks contribute.  The prime and continuous pieces are comparable, so the packet size is
not a leftover unremoved background.

## 4. Updated S-FIN route

E72.123 reduces `S-FIN` to:

```text
YLOW + BUP.
```

E72.124 identifies `YLOW` as the finite frame lower bound `(PFLB)`.

Thus `S-FIN` can be attacked as:

```text
PFLB:
the full endpoint discrepancy packet has energy >= c xL^2,

BUP:
the finitely many bad packet tests have energy <= C x.
```

This is the cleanest current separation:

```text
full packet energy: sqrt(x)L,
bad tests:          sqrt(x).
```

## 5. Status

```text
proved: PFLB implies YLOW;
observed: packet scale is stable and uses both sigma/dot_sigma blocks;
open:   prove PFLB uniformly for finite CCM roots.
```
