# E73.094 - Tail LC finite certificate

## 1. Purpose

E73.091 gives the local rational nodal budget `N_LC(A,L)`.
E73.093 shows that the finite Fourier tail uses the same nodal data.

This note proves the finite implication:

```text
TAIL-LC-BUD => local TAIL-NODAL-5.
```

## 2. Tail identity

By E72.391:

```text
Lcal(B_z^tail)
= -2i/L sum_w w G_x(w) R_M(z,w),
```

where:

```text
G_x(w)=(1-e^(wL))H_0(w),
```

and:

```text
R_M(z,w)
= sum_{|m|>M} (1-e^(zL))/[(iz-d_m)(w^2+d_m^2)].
```

By E72.392, on the fixed shifted compact strip:

```text
|(-2i/L)wR_M(z,w)|
<= C_K e^(sigma L)L^2/M^2 |w|.                       (1)
```

The harmless extra `|w|` is kept explicit in the local window.

## 3. Local tail nodal budget

Let:

```text
Wloc(A,L):=max_{w in Z_loc(A,L)} |w|.
```

On the critical line:

```text
|1-e^(wL)| <= 2.
```

Thus:

```text
sum_{w in Z_loc/+-}|w||G_x(w)|
<= 2 Wloc(A,L) sum_{w in Z_loc/+-}|H_0(w)|
<= 2 Wloc(A,L) N_LC(A,L).                             (2)
```

The last inequality is E73.091.

## 4. Tail LC budget

Define:

```text
TAIL-LC-BUD(A,L):
C_K e^(sigma L)L^2/M^2
S_FAR(A,L) Wloc(A,L) N_LC(A,L)
<= C_tail L^-5.
```

Constants absorb the factor `2`.

## 5. Theorem

**Theorem 94.1.**  If `TAIL-LC-BUD(A,L)` holds, then the local part of `TAIL-NODAL-5(A,L)` holds.

*Proof.*  For each FAR3 evaluation row `z_k`, use (1) and sum over the local window:

```text
|TailOperator_{z_k}^{loc}|
<= C_K e^(sigma L)L^2/M^2
   sum_{w in Z_loc/+-}|w||G_x(w)|.
```

Apply (2):

```text
|TailOperator_{z_k}^{loc}|
<= C_K e^(sigma L)L^2/M^2 Wloc(A,L)N_LC(A,L).
```

Multiplying by `W_k(A,L)` and summing over `D_3(A,L)` gives:

```text
sum_{gamma_k in D_3} W_k(A,L)|TailOperator_{z_k}^{loc}|
<=
C_K e^(sigma L)L^2/M^2 S_FAR(A,L)Wloc(A,L)N_LC(A,L).
```

The right side is at most `C_tail L^-5` by `TAIL-LC-BUD`. `□`

## 6. Relation with LOCK-COMP-BUD

Compare:

```text
LOCK-COMP-BUD:
e^(sigma L) S_FAR N_LC <= O(L^-5),
```

up to fixed constants, with:

```text
TAIL-LC-BUD:
e^(sigma L) S_FAR N_LC * Wloc L^2/M^2 <= O(L^-5).
```

Thus the tail is lower order whenever:

```text
Wloc(A,L)L^2/M^2
```

is bounded by a harmless power already allowed in the global gate.  Under polynomial active cutoff
`M>=L^(1+epsilon)` and fixed natural-height local windows, this factor is:

```text
O(L^(-2epsilon)).
```

## 7. Status

```text
proved: local TAIL-NODAL-5 follows from TAIL-LC-BUD;
verified: E73.093 shows finite slack;
remaining: outside-window tail contribution and the uniform GATE-73 theorem.
```
