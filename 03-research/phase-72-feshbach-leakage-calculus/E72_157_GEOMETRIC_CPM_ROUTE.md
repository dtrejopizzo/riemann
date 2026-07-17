# E72.157 -- Geometric CPM route

**Date:** 2026-07-09.
**Role:** replace root-specific `CPM-ORTH` by a uniform geometric kernel estimate.

## 0. Uniform kernel estimate

For:

```text
M_x=B_x^*P_HLK_x,
```

define:

```text
UKERN:
sup_{0<tau<=T} ||P_Row(M_x)Y_x(tau)||/||Y_x(tau)|| <= C_T/L.
```

Since:

```text
||M_xY|| <= ||M_x||||P_Row(M_x)Y||,
```

`UKERN` implies:

```text
||M_xY_x(tau_j)|| <= C_TL^(-1)||M_x||||Y_x(tau_j)||,
```

for every finite root `tau_j<=T`.  Thus:

```text
UKERN => CPM-ORTH => CPM-Q => CPM-scale.
```

## 1. Refined route

The current route may be stated as:

```text
GCOER,
PSD-DIST,
B-scale,
Y-scale,
OPM,
UKERN,
ROP,
CGE-K
```

imply scalar WRL resonance annihilation.

### Proof

`UKERN` implies `CPM-ORTH` as above.  E72.152 then gives:

```text
B-scale + Y-scale + OPM + CPM-ORTH => MSB.
```

E72.146 gives:

```text
GCOER + PSD-DIST + MSB + ROP + CGE-K => scalar WRL.
```

`QED`

## 2. Meaning

This removes one root-specific cancellation gate.  The source estimate is now geometric:

```text
the packet family Y_x(tau) lies within O(1/L) of ker(B^*P_HLK)
uniformly on compact tau windows.
```

The main signed arithmetic gate remains:

```text
PSD-DIST.
```

## 3. Status

```text
proved: UKERN implies the CPM side of the refined certificate;
open:   prove UKERN and PSD-DIST uniformly.
```
