# E73.096 - OUT-FAR finite certificate

## 1. Purpose

This note turns the remaining outside-window term in `GATE-73` into an explicit finite certificate.

There are two outside pieces:

```text
OUT-HIGH: zeros above the natural height T_L=e^L L^A;
OUT-FAR_fin: critical rows inside K_L but outside the FAR3 selected set.
```

## 2. High zero tail

E72.394 proves that for the paired packet transform:

```text
sum_{|Im w|>T_L}|F_z(w)| <= C_K L^B
```

and, more precisely:

```text
<= C_K e^((theta+sigma_K-1)L)L^(B+1-A),
```

with `T_L=e^L L^A`, `theta<1/2`, and `theta+sigma_K<1`.

Taking `A` large makes this contribution lower order for the finite gate.

## 3. Finite FAR complement

Inside the natural-height window `K_L`, define:

```text
OUT-FAR_fin(A,L)
:=
sum_{gamma_k in K_L \ D_3(A,L)}
W_k(A,L)|C_x(i gamma_k)|.
```

Using the finite Cauchy divisor:

```text
C_x(i gamma_k)=P_x(-gamma_k)/D_x(-gamma_k),
```

this becomes the explicit rational sum:

```text
OUT-FAR_fin(A,L)
=
sum_{gamma_k in K_L \ D_3(A,L)}
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

The selected set `D_3(A,L)` is determined by:

```text
F_k(A,L)=W_k(A,L)dist(-gamma_k,Div(P_x)),
```

not by `|C_x(i gamma_k)|`.

## 4. OUT-FAR certificate

Define:

```text
OUT-FAR(A,L):
OUT-FAR_fin(A,L) + OUT-HIGH(A,L) <= C_out L^-9.
```

For the weaker main-scale gate, `L^-9` may be replaced by `L^-5`, but the Phase 73 budget keeps the
sharper tail scale.

## 5. Theorem

**Theorem 96.1.**  Assume `OUT-FAR(A,L)`.  Then all outside-window rows not controlled by the local
FAR3 packet contribute at most `C_out L^-9` to the WCS budget.

*Proof.*  Split the critical rows into:

```text
K_L = D_3(A,L) union (K_L \ D_3(A,L)),
```

and split the zero height range into:

```text
|Im w|<=T_L,     |Im w|>T_L.
```

The first complement is exactly `OUT-FAR_fin(A,L)`.  The high part is `OUT-HIGH(A,L)`, controlled by
E72.394.  Their sum is bounded by `C_out L^-9` by the certificate. `□`

## 6. Role in GATE-73

With E73.091 and E73.094:

```text
LOCK-COMP-BUD controls the complete-mesh local packet;
TAIL-LC-BUD controls the local finite Fourier tail;
OUT-FAR controls all nonlocal rows and high zeros.
```

Thus the remaining main work in `GATE-73` is only the three FAR3 main nodewise rational bounds:

```text
T_k(A,L)
= W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|
```

for `gamma_k in D_3(A,L)`.

## 7. Status

```text
proved: OUT-HIGH by E72.394;
finite certificate: OUT-FAR_fin is an explicit rational positive sum;
verified: E73.095 shows OUT-FAR_fin is tiny in the finite harness;
open: uniform proof of OUT-FAR_fin for the natural-height window.
```
