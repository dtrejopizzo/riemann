# E72.273 -- Pole-even bordered minor identity

**Purpose.** Repair the bordered-minor endpoint after the pole-even correction.

E72.79 proved the algebraic identity:

```text
<a,C^{-1}b> = - det [[C,b],[a^*,0]] / det(C).
```

But E72.79 used the old reduced space:

```text
E_even cap k^perp,
```

where `k` was later found in E72.261 to be an accidental normalized near-zero even vector. Therefore
the old source split involving `Q=I-kk^*` and `h=k-xi` cannot be used as a proof-facing object.

## Corrected identity

In the pole-even geometry:

```text
C_E = B_even^T(H_actual-e_pole I)B_even,
```

with the full even sector retained. For any finite vectors `a,b` in this corrected coordinate space:

```text
<a,C_E^{-1}b>
= - det [[C_E,b],[a^*,0]] / det(C_E).
```

### Proof

This is the Schur complement:

```text
det [[C_E,b],[a^*,0]]
= det(C_E) det(-a^*C_E^{-1}b)
= -det(C_E)<a,C_E^{-1}b>.
```

Dividing by `det(C_E)` proves the identity.

## Numerical check

The companion script verifies the identity in the corrected pole-even harness for two explicit source
vectors:

```text
E72.273 pole-even bordered minor identity
Checks <a,C^-1 b> = -det[[C,b],[a*,0]]/det(C) in corrected pole-even geometry.
```

The source vectors are deliberately simple (`xi` and `1`) because the purpose of E72.273 is only to
verify the corrected algebraic minor identity, not to assert the old HPAC source formula.

## Consequence

The inverse in the pole-even scalar WRL endpoint can still be replaced by a bordered determinant:

```text
EV-CERT-pole-even:
N_x(s,b) / det(C_E) -> 0,

N_x(s,b) := det [[C_E,b],[a_s^*,0]].
```

What changes is the source vector `b`.

## Corrected open target

The old E72.79 source:

```text
b_j = B^T W_j(k,xi)
```

depends on the invalid `k`-projection. It must be replaced by a pole-even HPAC source derived directly
from:

```text
B_even,
C_E,
xi_x,
A_x(tau),
and the finite Weyl equation.
```

Thus the repaired endpoint is:

```text
1. derive the correct pole-even HPAC source b_j^{PE};
2. prove N_x(s,b_j^{PE})/det(C_E) -> 0.
```

## Status

Closed: the bordered-minor algebra survives the pole-even correction.

Open: the HPAC source vector must be rederived in the corrected geometry before claiming scalar WRL
divisibility.
