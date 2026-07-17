# E73.230 - Closed scalar interval wrapper

Date: 2026-07-14.

## 1. Purpose

E73.228 combined

```text
R_etaH + R_coeff + R_weight
```

as an ultraconservative ledger.  That is safe, but it double-counts the
uncertainty of `eta` if the proof-facing scalar is evaluated in the closed
coefficient/weight representation.

The closed scalar certificate should instead use:

```text
C_a=sum c_omega W_omega+sum l_omega V_omega
```

with coefficient balls and weight balls.

## 2. Closed interval radius

For each frequency:

```text
c in B(c0,rc),       W in B(W0,rW),
l in B(l0,rl),       V in B(V0,rV).
```

Then:

```text
rad(cW) <= |W0|rc + |c0|rW + rc rW,
rad(lV) <= |V0|rl + |l0|rV + rl rV.
```

Therefore

```text
R_closed =
sum |W_omega|rad(c_omega)
+sum |c_omega|rad(W_omega)
+sum rad(c_omega)rad(W_omega)
+sum |V_omega|rad(l_omega)
+sum |l_omega|rad(V_omega)
+sum rad(l_omega)rad(V_omega).
```

This is the actual closed scalar interval radius.

## 3. Result

The closed interval is dominated by the coefficient-radius term:

```text
R_closed ~= R_coeff.
```

The weight-radius and product terms are much smaller:

```text
R_weight << R_coeff,
R_prod   << R_weight.
```

Worst inflated-sector ratio:

```text
R_closed/|C_a| = 1.6e-14.
```

## 4. Relation to E73.228

E73.228 remains a useful cross-check because it also transports the interval
through the matrix-route scalar `q_aHeta`.  But the proof-facing closed scalar
certificate should not add `R_etaH` on top of `R_coeff`: both represent the
same `eta` uncertainty through different coordinate systems.

Thus the authoritative finite closed scalar route is:

```text
closed center + coefficient balls + weight balls.
```

## 5. Status

```text
implemented: closed scalar interval wrapper without matrix-route double count;
verified: worst tested ratio 1.6e-14 under C_sec=1e6;
remaining: uniform production in L/windows.
```
