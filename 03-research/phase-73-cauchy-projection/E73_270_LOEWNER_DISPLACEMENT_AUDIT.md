# E73.270 - Loewner displacement audit for the master scalar

Date: 2026-07-14.

## 1. Purpose

E73.269 reduced the scalar WRL gate to the master finite scalar

```text
S_{a,w,L}=q_aH_LR_wxi_L,
```

with equivalent forms `CELL-CTM`, `COEFF-ETA`, `SECOND-ABEL`, and
`COMM-TRANSPORT`.  This note audits the next possible analytic input against
the previous Loewner/displacement work, so that the proof attempt does not
repeat a known failed shortcut.

## 2. Exact Loewner structure already proved

Phase 72 proved the finite CCM overlap identity

```text
Q_y=2cos(yD)-(2/L)Lo_y,                         (1)
Lo_y=D(sin(yD))[J],
[D,Lo_y]=[sin(yD),J],
```

where `D=diag(2*pi*n/L)` and `J=11^T`.  Therefore the current transverse
packet

```text
B_{a,w,L}(y)=q_aQ_yR_wxi_L
```

has the exact decomposition

```text
B(y)=2q_acos(yD)R_wxi_L
     -(2/L)q_aLo_yR_wxi_L.                      (2)
```

This is an identity, not an estimate.

## 3. What the previous program already ruled out

The following consequences were already audited:

```text
E72.55:
  the two pieces in (2) are usually much larger than their sum.
  Therefore separate absolute bounds on the diagonal cosine and Loewner
  pieces destroy the needed cancellation.

E72.56:
  near y=L-r,
  Q_{L-r}=(2r/L)J+higher endpoint terms.
  The diagonal/Loewner cancellation collapses the endpoint cell to rank one.

E72.58:
  literal rank-one endpoint suppression is false:
  <v,1><1,k> is not the small quantity.

E73.192:
  the correct correction is an explicit balanced ramp subtraction, leaving a
  double-zero packet.  The rank-one endpoint source must be absorbed into the
  model main term, not assumed negligible.

E73.017:
  a finite displacement reduction exists for a local off-line ideal, but its
  remaining core is FDL-2: explicit partial-fraction closure with endpoint
  bookkeeping.  It is not yet a proof of the current master scalar.
```

Thus the Loewner identity is useful only as a coupled finite displacement
identity.  It cannot be used as:

```text
1. separate norm bounds for cos and Loewner;
2. literal endpoint rank-one suppression;
3. a generic finite-displacement slogan without endpoint bookkeeping;
4. a rank-two Cauchy-plane transport formula involving Q_wxi_L.
```

## 4. Consequence for the master scalar

Combining E73.269 with (2), the load-bearing scalar can be written as

```text
S_{a,w,L}
=F_L[B]
=F_L[2q_acos(yD)R_wxi_L]
 -(2/L)F_L[q_aLo_yR_wxi_L],                    (3)
```

where `F_L` denotes any of the equivalent prime-minus-archimedean functionals:

```text
F_L[B]
=mathcal A_L[B]
 -sum_{p^k<=e^L}(log p)p^(-k/2)B(klog p)
=sum c_omega W_omega+sum l_omega V_omega
=int_0^L K_L(t)(B^bal)''(t)dt.
```

Equation (3) is not a proof because the two terms on the right are not small
separately.  The theorem must preserve the cancellation in the full expression

```text
F_L[2q_acos(yD)R_wxi_L-(2/L)q_aLo_yR_wxi_L].
```

## 5. The surviving analytic theorem

The non-circular theorem left after the audit is:

### Coupled Loewner Master Divisibility

For every `M`, uniformly over admissible rows/windows,

```text
F_L[
  2q_acos(yD)R_wxi_L
  -(2/L)q_aD(sin(yD))[J]R_wxi_L
] = O_M(L^-M).                                  (CLMD)
```

Equivalently, after the E73.192 ramp normalization, the theorem splits into
two explicit pieces:

```text
RAMP-MATCH:
  B'(0)F_L[y(1-y/L)] is part of the model main term;

DOUBLE-ZERO-CLMD:
  F_L[B^rem]=O_M(L^-M),
  B^rem(0)=(B^rem)'(0)=B^rem(L)=0,
```

with `B^rem` still built from the coupled Loewner expression (2).  The
double-zero condition is the first place where integration by parts in the
second-Abel form can be used without reintroducing the false rank-one
suppression.

## 6. Relation to earlier no-go walls

This is not the old Sonin/prolate/Feshbach route by itself.  The differences
are load-bearing:

```text
old endpoint/prolate attempts:
  try to bound a channel or endpoint layer directly;

current CLMD:
  bounds the prime-minus-archimedean functional on the transverse eigenpacket
  after exact Cauchy projection and balanced endpoint subtraction.

old Loewner split:
  diagonal and Loewner pieces estimated separately;

current CLMD:
  only the coupled commutator/Fréchet expression is admissible.

old Cauchy transport:
  uses Q_wxi_L and becomes circular;

current CLMD:
  uses R_wxi_L inside B(y), and the smallness is exactly the theorem to prove.
```

## 7. Status

```text
proved: exact insertion of the Loewner identity into the E73.269 master scalar;
audited: previous Loewner/endpoint shortcuts and their failure modes;
survives: Coupled Loewner Master Divisibility (CLMD), preferably in the
          ramp-normalized double-zero second-Abel form;
open:    prove CLMD uniformly from the coupled displacement identity and the
         eigenline equation, without splitting absolute values and without
         using Q_wxi_L as input.
```

