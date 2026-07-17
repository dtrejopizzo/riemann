# E73.177 - Stable divisor bridge for BT-QG

Date: 2026-07-14.

## 1. Purpose

E73.175 reduces `QG` to:

```text
BT-QG:
|B_{r,L}(0)| <= L^B e^(-alpha L), r=1,2,3.
```

E73.176 shows:

```text
B_{r,L}(0)
= 2 sum_{j=1}^5 conjugate(q_r(L)_j) G_L(i gamma_j).
```

This note asks whether the quotient projection itself produces the smallness,
or whether the smallness is already present in the raw critical nodal values:

```text
G_L(i gamma_j).
```

## 2. Diagnostic

Compare:

```text
raw  = ||G_L||,
quot = ||P_Q,L G_L||.
```

If `quot/raw` is small, the quotient is the mechanism.  If `quot/raw` is
order one, then `BT-QG` is essentially raw critical nodal smallness.

## 3. Result

The probe shows:

```text
log_L ||P_QG|| - log_L ||G|| ~= 0
```

in trusted rows.  Thus the quotient does not add a decisive scale gain.

The active smallness is already:

```text
G_L(i gamma_j) = (1-e^(i gamma_j L)) sum_m xi_L(m)/(-gamma_j-d_m)
```

being tiny at the true critical zeros.

## 4. Interpretation

This identifies the current endpoint with a finite nodal form of stable
divisor identification:

```text
SDI-node:
For each fixed critical zero gamma_j,
G_L(i gamma_j) = O(L^B e^(-alpha L)).
```

Then `BT-QG` follows immediately because the quotient coefficient matrix has
operator norm `1`.

Conversely, `BT-QG` by itself is weaker than full stable divisor
identification, because it only controls three quotient combinations of five
critical nodal values.  But numerically those combinations are not smaller
than the raw vector by a useful factor, so a proof should target `SDI-node`,
not hidden quotient cancellation.

## 5. Relation to Phase 71

Phase 71 isolated the hard CAND-1 theorem:

```text
the intrinsic stable divisor of (D_N,xi_N) converges to the divisor of Xi.
```

E73.177 shows that the current Phase 73 endpoint has returned to the same
frontier, but in a very concrete local form:

```text
critical-node vanishing of the finite Cauchy numerator G_L.
```

This is not a failure.  It prevents a false search for cancellation in the
rank-three quotient and locates exactly what must be proved.

## 6. Current theorem

The proof-facing theorem is now:

```text
SDI-node theorem:
For every fixed finite set of critical zeros {gamma_1,...,gamma_J},

max_{1<=j<=J}
|(1-e^(i gamma_j L)) sum_m xi_L(m)/(-gamma_j-d_m)|
<= L^B e^(-alpha L).
```

Together with E73.170--E73.176 and `QPI`, this implies `QUOT-NORM` and hence
the Phase 73 scalar WRL endpoint.

## 7. Status

```text
proved:   quotient does not create a hidden extra scale in tested windows;
reduced:  BT-QG to SDI-node as the proof-facing target;
open:     prove SDI-node from the finite CCM eigenvector construction.
```
