# E73.092 - Global finite gate after paired Mellin divisibility

## 1. Purpose

Phase 73 has now removed the hidden Mellin divisibility step from the scalar WRL route.

This note states the current global gate in one place, separating:

```text
proved algebraic identities;
finite sufficient certificates;
the remaining uniform theorem.
```

## 2. Proved algebraic inputs

The complete-mesh Mellin packet satisfies:

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).       (E73.075)
```

The finite Fourier tail is an explicit nodal operator:

```text
Lcal(B_z^tail)
= -2i/L sum_w w G_x(w)R_M(z,w),                       (E72.391)
```

with:

```text
|R_M(z,w)| <= C_K e^(Re z L)L^3/M^2.                  (E72.392)
```

The finite Cauchy divisor is rational:

```text
H_0(i gamma)=-i C_x(-gamma),
C_x(t)=P_x(t)/D_x(t).                                 (E73.038)
```

## 3. Local finite gate

For each natural-height off-line cluster `A`, E73.091 defines the local budget:

```text
N_LC(A,L)
= locked root-proximity contribution
 + companion rational residual contribution.
```

The local certificate is:

```text
LOCK-COMP-BUD(A,L):
4(1+e^(sigma L))/sigma * S_FAR(A,L) * N_LC(A,L)
<= C_LC L^-5.
```

E73.091 proves:

```text
LOCK-COMP-BUD(A,L) => LOCAL-HWIN-5(A,L).
```

## 4. Tail finite gate

The local finite-tail certificate is:

```text
TAIL-LC-BUD(A,L):
C_K e^(sigma L)L^2/M^2 S_FAR(A,L)Wloc(A,L)N_LC(A,L)
<= C_tail L^-5.
```

E73.094 proves:

```text
TAIL-LC-BUD(A,L) => local TAIL-NODAL-5(A,L).
```

At polynomial active cutoff, this is the same finite nodal budget as `LOCK-COMP-BUD`, with the extra
lower-order factor `Wloc L^2/M^2`.

## 5. Outside-window gate

Let:

```text
K_L = critical natural-height window,
D_3(A,L)=FAR3 evaluation rows,
Z_loc(A,L)=cluster-local zero nodes.
```

All critical rows not controlled by the local FAR3 packet are assigned to the already separated
FAR3-tail/outside-window budget:

```text
OUT-FAR(A,L):
OUT-FAR_fin(A,L)+OUT-HIGH(A,L)
<= C_out L^-9.
```

E73.096 defines:

```text
OUT-FAR_fin(A,L)
=
sum_{gamma_k in K_L \ D_3(A,L)}
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|
```

and imports `OUT-HIGH` from E72.394.  This is the finite nodewise certificate of E73.052--E73.054
plus the natural-height high-zero tail:

```text
FAR3-main + FAR3-tail => WCS.
```

## 6. Global finite certificate

For fixed `L` and cluster box `A`, the following finite certificate implies scalar WRL:

```text
GATE-73(A,L):
1. LOCK-COMP-BUD(A,L);
2. TAIL-LC-BUD(A,L);
3. OUT-FAR(A,L);
4. FAR3 nodewise rational bounds for the three main WCS rows.
```

Every term is finite and explicit:

```text
A_L,B_L                 elementary;
P_x,D_x                 finite polynomials/rational Cauchy sum;
Div(P_x)                finite Cauchy roots;
W_k                     elementary Hermite/mesh weight;
TailOperator            finite nodal operator with explicit kernel R_M;
FAR3 set                selected by W_k dist(-gamma_k,Div(P_x)), not by T_k.
```

## 7. Theorem

**Theorem 92.1.**  If `GATE-73(A,L)` holds for every natural-height off-line cluster box at scale
`L`, then the scalar WRL branch holds at scale `L`.

*Proof.*  `LOCK-COMP-BUD` gives `LOCAL-HWIN-5` by E73.091.  This implies the complete-mesh part of
`FACTOR-MAIN-5` by E73.078 and E73.087.  `TAIL-LC-BUD` gives the local tail part by E73.094, while
the outside-window tail is assigned to `OUT-FAR`.  Together:

```text
FACTOR-MAIN-5 + TAIL-NODAL-5
=> BALANCED-PACKET-ROW-5.
```

The outside-window and FAR3 nodewise assumptions give:

```text
FAR3-main + FAR3-tail => WCS
```

by E73.052--E73.054.  E73.042 proves:

```text
WCS => scalar WRL.
```

Therefore `GATE-73(A,L)` implies scalar WRL at scale `L`. `□`

## 8. Remaining uniform theorem

The route to Omega7/RH is now:

```text
Uniform GATE-73:
there exist L0 and constants C_LC,C_tail,C_out,B
such that GATE-73(A,L) holds for every L>=L0 and every natural-height off-line cluster A.
```

This is the current exact frontier.

It is not a hidden matrix statement and not a raw positivity statement.  It is a finite family of
rational/elementary inequalities over the pole-even CCM data and the FAR-selected critical rows.

## 9. What has been closed

The specific Mellin spectral divisibility problem has been closed at the complete-mesh level:

```text
Pair_z^infty(w) belongs exactly to the ideal (H_0(w),H_0(-w)).
```

The actual finite-packet problem is reduced to:

```text
local rational nodal suppression + explicit tail nodal operator.
```

Thus the remaining obstacle is no longer "find the Mellin divisor"; it is proving the uniform
finite gate above.
