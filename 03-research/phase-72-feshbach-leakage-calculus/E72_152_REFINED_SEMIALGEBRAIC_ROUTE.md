# E72.152 -- Refined semialgebraic route

**Date:** 2026-07-09.
**Role:** replace the black-box `MSB` product by structural finite estimates.

## 0. From MSB to scale and alignment

E72.146 used:

```text
MSB:
sup ||b_H||||c_H^{pm}(tau_j)||=O(1).
```

E72.149--E72.151 split this into:

```text
B-scale:
||b_H||=O(sqrt(L)),

Y-scale:
||Y_x(tau_j)||=O(sqrt(x)L),

OPM:
||M_x||=O(1),        M_x=B_x^*P_HLK_x,

CPM-ORTH:
||M_xY_x(tau_j)|| <= C L^(-1)||M_x||||Y_x(tau_j)||.
```

Then:

```text
||c_H^{pm}(tau_j)||
 = (2/(Lsqrt(x)))||M_xY_x(tau_j)||
 <= C/(sqrt(L)).
```

Together with `B-scale`, this gives `MSB`.

## 1. Refined theorem

Assume:

```text
GCOER,
PSD-DIST,
B-scale,
Y-scale,
OPM,
CPM-ORTH,
ROP,
CGE-K.
```

Then scalar WRL resonance annihilation holds.

### Proof

`B-scale + Y-scale + OPM + CPM-ORTH` imply `MSB` by the calculation above.  Then apply E72.146:

```text
GCOER + PSD-DIST + MSB + ROP + CGE-K => scalar WRL.
```

`QED`

## 2. Current meaning

The two remaining cancellation estimates are now explicit finite orthogonality statements:

```text
PSD-DIST:
relative arithmetic perturbation is within distance <1 of the PSD cone;

CPM-ORTH:
finite root packets are almost orthogonal to the large singular directions of B^*P_HLK.
```

The rest are size/coercivity estimates:

```text
GCOER, B-scale, Y-scale, OPM, ROP, CGE-K.
```

## 3. Status

```text
proved: refined estimates imply the E72.146 certificate;
open:   prove PSD-DIST and CPM-ORTH uniformly from the finite CCM construction.
```
